"""Anthropic Research listing scraper."""
import re
import sys
from datetime import datetime, timezone

import requests
from bs4 import BeautifulSoup

from simon_daily.content import fetch_article_content
from simon_daily.io import save_post, get_post_dir
from simon_daily.translate import translate_post
from simon_daily.sources import SOURCES, slugify


_ANTHROPIC_DATE_RE = re.compile(r'^([A-Z][a-z]{2})\s+(\d{1,2}),\s*(\d{4})$')
_ANTHROPIC_DATE_INNER = r'([A-Z][a-z]{2})\s+(\d{1,2}),\s*(\d{4})'
_MONTH_MAP = {m: i for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], start=1)}


def _parse_anthropic_research_listing(soup, base_url="https://www.anthropic.com"):
    """Parse the Anthropic research listing page for articles."""
    articles = []
    items = soup.find_all("li")
    for li in items:
        text = li.get_text(separator="|", strip=True)
        m = re.match(_ANTHROPIC_DATE_INNER, text)
        if not m:
            continue
        date_str = m.group(0)
        link = li.find("a")
        if not link:
            continue
        href = link.get("href", "")
        full_url = href if href.startswith("http") else f"{base_url}{href}"

        # Extract title from the title element (not the full link text which includes date+category)
        title_el = link.find("span", class_=lambda c: c and "title" in c)
        if title_el:
            title = title_el.get_text(strip=True)
        else:
            # Fallback: get the last span/div text
            all_spans = link.find_all(["span", "div"])
            title = all_spans[-1].get_text(strip=True) if all_spans else ""
        articles.append({
            "url": full_url,
            "title": title,
            "date_str": date_str,
        })
    return articles


def _strip_anthropic_research_prefix(content):
    """Strip the category/date/Read-paper prefix from Anthropic article markdown."""
    lines = content.split("\n")
    stripped = []
    skip_until_after_date = True
    for line in lines:
        if skip_until_after_date:
            stripped.append(line)
            if re.match(_ANTHROPIC_DATE_RE, line.strip()):
                skip_until_after_date = False
                stripped.append("")
            continue
        # Skip "[Read the paper]" link line
        if re.match(r'^\[Read the', line.strip()):
            continue
        stripped.append(line)
    return "\n".join(stripped).strip()


def fetch_from_listing_anthropic_research(lang_code="zh-cn", model=None, no_translate=False, max_articles=None):
    """Fetch all Anthropic Research articles."""
    base_url = "https://www.anthropic.com"
    url = f"{base_url}/research"
    src = SOURCES["anthropic-research"]
    print(f"Scraping Anthropic Research listing from {url} ...")

    try:
        resp = requests.get(url, timeout=20, headers={
            "User-Agent": "Mozilla/5.0 (compatible; simon-daily/1.0)"
        })
        resp.raise_for_status()
    except Exception as e:
        print(f"  [ERROR] Failed to fetch listing: {e}", file=sys.stderr)
        return 1

    soup = BeautifulSoup(resp.text, "html.parser")
    articles = _parse_anthropic_research_listing(soup, base_url)
    print(f"Found {len(articles)} articles")

    articles = articles[:max_articles] if max_articles else articles

    post_dir = get_post_dir("anthropic-research")
    existing_slugs = set()
    for f in post_dir.glob("*.md"):
        if ".zh-cn" not in f.name and ".zh." not in f.name:
            existing_slugs.add(f.stem)

    new_count = 0
    saved = []
    translated = []

    for i, art in enumerate(articles):
        print(f"\n  [{i+1}/{len(articles)}] {art['title']}")

        safe_title = slugify(art["title"])
        slug = f"{safe_title}"
        if slug in existing_slugs:
            print(f"    [SKIP] Already saved")
            continue

        full_content = fetch_article_content(art["url"])
        if not full_content:
            print(f"    [SKIP] Failed to fetch content")
            continue

        content = _strip_anthropic_research_prefix(full_content)
        content = re.sub(r'^#\s+.*?\n', '', content, count=1)

        # Parse the date
        date_str = ""
        pub_date = None
        dm = re.match(_ANTHROPIC_DATE_RE, art["date_str"])
        if dm:
            month_name, day, year = dm.groups()
            m_num = _MONTH_MAP.get(month_name, 1)
            pub_date = datetime(int(year), m_num, int(day))
            date_str = pub_date.strftime("%Y-%m-%d")

        if not date_str:
            print(f"    [SKIP] Could not parse date: {art['date_str']}")
            continue

        md = f"""# {art['title']}

**Date:** {pub_date.strftime('%Y-%m-%d %H:%M UTC') if pub_date else ''}
**Link:** {art['url']}

---

{content}
"""
        filepath = save_post(date_str, md, art["title"], "anthropic-research")
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
