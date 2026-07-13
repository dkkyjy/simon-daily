"""Fetch orchestration: feed and listing dispatchers."""
from datetime import datetime, timezone, timedelta

from simon_daily.sources import SOURCES
from simon_daily.formatters import format_post
from simon_daily.io import save_post, get_post_dir
from simon_daily.translate import translate_post
from simon_daily.scrapers.claude import fetch_from_listing_claude
from simon_daily.scrapers.anthropic_research import fetch_from_listing_anthropic_research
from simon_daily.scrapers.anthropic_engineering import fetch_from_listing_anthropic_engineering


def fetch(source_key, days=1, lang_code="zh-cn", model=None, no_translate=False):
    """Fetch posts from a blog source. Auto-dispatches to fetch_from_listing
    for sources with feed_url=None (listing-based sources)."""
    src = SOURCES[source_key]

    if not src.get("feed_url"):
        return fetch_from_listing(
            source_key=source_key,
            lang_code=lang_code,
            model=model,
            no_translate=no_translate,
        )

    import feedparser
    print(f"Fetching {src['feed_url']} ...")
    feed = feedparser.parse(src["feed_url"])
    entries = feed.entries

    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    seen = set()

    new_count = 0
    saved = []
    translated = []

    for entry in entries:
        entry_id = getattr(entry, "id", "") or getattr(entry, "link", "")
        from simon_daily.sources import published_or_updated
        pub_date = published_or_updated(entry)

        if pub_date and pub_date < cutoff:
            break

        if entry_id in seen:
            continue
        seen.add(entry_id)

        title = getattr(entry, "title", "Untitled")
        print(f"  [{src['name']}] {title}")

        date_str, md = format_post(source_key, entry)
        filepath = save_post(date_str, md, title, source_key)
        if filepath:
            saved.append(filepath)
            new_count += 1
        else:
            print(f"    Skipped (already saved)")

    if not no_translate and saved:
        print(f"\nTranslating {len(saved)} new posts...")
        for fp in saved:
            zh = translate_post(fp, lang_code=lang_code, model=model)
            if zh:
                translated.append(zh)

    print(f"\nDone: {new_count} new, {len(seen)} seen, {len(saved)} saved, {len(translated)} translated")
    return 0


def fetch_from_listing(source_key, year=None, lang_code="zh-cn", model=None, no_translate=False):
    """Fetch posts by scraping the blog listing pages."""
    if year is None:
        year = datetime.now(timezone.utc).year

    # Dispatch to source-specific listing fetcher
    if source_key == "claude":
        return fetch_from_listing_claude(
            lang_code=lang_code, model=model, no_translate=no_translate, max_pages=None,
        )
    if source_key == "anthropic-research":
        return fetch_from_listing_anthropic_research(
            lang_code=lang_code, model=model, no_translate=no_translate,
        )
    if source_key == "anthropic-engineering":
        return fetch_from_listing_anthropic_engineering(
            lang_code=lang_code, model=model, no_translate=no_translate,
        )

    src = SOURCES[source_key]
    listing_url = src.get("listing_url")
    if not listing_url:
        print(f"  [ERROR] Source '{source_key}' has no listing URL configured")
        return 1

    import textwrap
    import re
    import requests
    from bs4 import BeautifulSoup
    from simon_daily.content import fetch_article_content
    from simon_daily.sources import slugify

    print(f"Scraping blog listing from {listing_url} ...")

    seen_urls = set()
    articles = []
    page = 1

    while True:
        url = listing_url if page == 1 else f"{listing_url.rstrip('/')}/page{page}/"
        print(f"  Page {page}: {url}")

        try:
            resp = requests.get(url, timeout=15, headers={
                "User-Agent": "Mozilla/5.0 (compatible; simon-daily/1.0)"
            })
            resp.raise_for_status()
        except Exception as e:
            print(f"    [WARN] Failed to fetch page {page}: {e}")
            break

        soup = BeautifulSoup(resp.text, "html.parser")
        cards = soup.find_all("article", class_="card")
        if not cards:
            break

        page_has_year_article = False
        for card in cards:
            time_tag = card.find("time", class_="card-date")
            link_tag = card.find("h3", class_="card-title")
            if not time_tag or not link_tag:
                continue
            a_tag = link_tag.find("a")
            if not a_tag:
                continue

            date_text = time_tag.get_text(strip=True)
            href = a_tag.get("href", "")
            title = a_tag.get_text(strip=True)

            try:
                pub_date = datetime.strptime(date_text, "%b %d %Y")
            except ValueError:
                continue

            if pub_date.year != year:
                if pub_date.year < year:
                    break
                continue

            page_has_year_article = True
            full_url = href if href.startswith("http") else f"https://addyosmani.com{href}"
            if full_url not in seen_urls:
                seen_urls.add(full_url)
                articles.append({
                    "url": full_url,
                    "title": title,
                    "date": pub_date,
                    "date_str": pub_date.strftime("%Y-%m-%d"),
                })

        if not page_has_year_article:
            break
        page += 1

    print(f"\nFound {len(articles)} articles from {year}")
    if not articles:
        return 0

    post_dir = get_post_dir(source_key)
    existing_slugs = set()
    for f in post_dir.glob("*.md"):
        if ".zh-cn" not in f.name and ".zh." not in f.name:
            existing_slugs.add(f.stem)

    new_count = 0
    saved = []
    translated = []

    for art in articles:
        safe_title = slugify(art["title"])
        slug = f"{art['date_str']}-{safe_title}"
        if slug in existing_slugs:
            print(f"  [SKIP] {art['title']} (already saved)")
            continue

        print(f"  [{src['name']}] {art['title']}")
        print(f"    Fetching full content from {art['url']}...")
        full_content = fetch_article_content(art["url"])

        if not full_content:
            print(f"    [SKIP] Failed to fetch content")
            continue

        content = full_content
        content = re.sub(r'^#\s+.*?\n', '', content, count=1)

        md = textwrap.dedent(f"""\
            # {art['title']}

            **Date:** {art['date'].strftime('%Y-%m-%d %H:%M UTC')}
            **Link:** {art['url']}

            ---

            {content}
        """).strip() + "\n"

        filepath = save_post(art["date_str"], md, art["title"], source_key)
        if filepath:
            saved.append(filepath)
            new_count += 1

    if not no_translate and saved:
        print(f"\nTranslating {len(saved)} new posts...")
        for fp in saved:
            zh = translate_post(fp, lang_code=lang_code, model=model)
            if zh:
                translated.append(zh)

    print(f"\nDone: {new_count} new, {len(saved)} saved, {len(translated)} translated")
    return 0
