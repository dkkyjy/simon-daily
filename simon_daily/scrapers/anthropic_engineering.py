"""Anthropic Engineering listing scraper."""
import re
import sys
from datetime import datetime, timezone

import requests
from bs4 import BeautifulSoup

from simon_daily.content import fetch_article_content
from simon_daily.io import save_post, get_post_dir
from simon_daily.translate import translate_post
from simon_daily.sources import SOURCES, slugify


_ENGINEERING_ARTICLE_CLASS_RE = re.compile(r"__article")


def _parse_anthropic_engineering_listing(soup, base_url="https://www.anthropic.com"):
    """Parse the Anthropic engineering blog listing for article URLs."""
    articles = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("/engineering/") and href != "/engineering/":
            article_div = a.find("div", class_=_ENGINEERING_ARTICLE_CLASS_RE)
            if not article_div:
                continue
            title_el = article_div.find("h2") or article_div.find("h3")
            title = title_el.get_text(strip=True) if title_el else ""
            if title:
                full_url = f"{base_url}{href}"
                articles.append({
                    "url": full_url,
                    "title": title,
                })
    return articles


def _extract_anthropic_engineering_date(url):
    """Extract the publication date from an Anthropic engineering article page."""
    try:
        resp = requests.get(url, timeout=20, headers={
            "User-Agent": "Mozilla/5.0 (compatible; simon-daily/1.0)"
        })
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        text = soup.get_text()
        m = re.search(r'(\w+)\s+(\d+),?\s*(\d{4})', text)
        if m:
            month, day, year = m.groups()
            months = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
                      "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}
            m_num = months.get(month, 1)
            return datetime(int(year), m_num, int(day))
        return None
    except Exception as e:
        print(f"  [WARN] Failed to extract date from {url}: {e}", file=sys.stderr)
        return None


def fetch_from_listing_anthropic_engineering(lang_code="zh-cn", model=None, no_translate=False, max_articles=None):
    """Fetch all Anthropic Engineering articles."""
    base_url = "https://www.anthropic.com"
    url = f"{base_url}/engineering"
    src = SOURCES["anthropic-engineering"]
    print(f"Scraping Anthropic Engineering listing from {url} ...")

    try:
        resp = requests.get(url, timeout=20, headers={
            "User-Agent": "Mozilla/5.0 (compatible; simon-daily/1.0)"
        })
        resp.raise_for_status()
    except Exception as e:
        print(f"  [ERROR] Failed to fetch listing: {e}", file=sys.stderr)
        return 1

    soup = BeautifulSoup(resp.text, "html.parser")
    articles = _parse_anthropic_engineering_listing(soup, base_url)
    print(f"Found {len(articles)} articles")

    articles = articles[:max_articles] if max_articles else articles

    post_dir = get_post_dir("anthropic-engineering")
    existing_slugs = set()
    for f in post_dir.glob("*.md"):
        if ".zh-cn" not in f.name and ".zh." not in f.name:
            existing_slugs.add(f.stem)

    new_count = 0
    saved = []
    translated = []

    for i, art in enumerate(articles):
        print(f"\n  [{i+1}/{len(articles)}] {art['title'][:60]}")

        safe_title = slugify(art["title"])
        slug = f"{safe_title}"
        if slug in existing_slugs:
            print(f"    [SKIP] Already saved")
            continue

        pub_date = _extract_anthropic_engineering_date(art["url"])
        if not pub_date:
            print(f"    [SKIP] Could not extract date")
            continue
        date_str = pub_date.strftime("%Y-%m-%d")

        full_content = fetch_article_content(art["url"])
        if not full_content:
            print(f"    [SKIP] Failed to fetch content")
            continue

        content = full_content
        content = re.sub(r'^#\s+.*?\n', '', content, count=1)

        md = f"""# {art['title']}

**Date:** {pub_date.strftime('%Y-%m-%d %H:%M UTC')}
**Link:** {art['url']}

---

{content}
"""
        filepath = save_post(date_str, md, art["title"], "anthropic-engineering")
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
