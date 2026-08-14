"""Agrici Daniel blog scraper.

Site is a React SPA with server-rendered content. The listing page
has no dates — they are extracted from each article's JSON-LD or header.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone

import requests
from bs4 import BeautifulSoup

from simon_daily.content import fetch_article_content
from simon_daily.io import save_post, get_post_dir
from simon_daily.translate import translate_post
from simon_daily.sources import SOURCES, slugify

_DATE_RE = re.compile(r"([A-Z][a-z]+)\s+(\d{1,2}),\s*(\d{4})")
_MONTH_MAP = {m: i for i, m in enumerate(
    ["January", "February", "March", "April", "May", "June",
     "July", "August", "September", "October", "November", "December"], start=1)}


def _parse_agricidaniel_listing(soup: BeautifulSoup) -> list[dict]:
    """Parse the /blog listing page for article links and titles."""
    articles = []
    ul = soup.find("ul")
    if not ul:
        return articles

    for li in ul.find_all("li"):
        a = li.find("a")
        if not a:
            continue
        href = a.get("href", "")
        if not href.startswith("/blog/"):
            continue
        title = a.get_text(strip=True)
        if not title:
            continue
        articles.append({
            "url": href if href.startswith("http") else f"https://agricidaniel.com{href}",
            "title": title,
        })
    return articles


def _extract_date_from_article(soup: BeautifulSoup, url: str) -> str:
    """Extract the published date from an article page.

    Tries JSON-LD first, then the By-author header line, then meta tags.
    Returns YYYY-MM-DD string or empty string on failure.
    """
    # Try JSON-LD
    for script in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(script.string or "")
        except (json.JSONDecodeError, TypeError):
            continue
        graph = data if isinstance(data, list) else data.get("@graph", [])
        for item in graph:
            if isinstance(item, dict) and item.get("datePublished"):
                return item["datePublished"][:10]
    # Try meta tag
    meta = soup.find("meta", property="article:published_time")
    if meta and meta.get("content"):
        return meta["content"][:10]
    # Try header paragraph: "By Agrici Daniel | March 25, 2026"
    header = soup.find("header")
    if header:
        for p in header.find_all("p"):
            text = p.get_text(strip=True)
            m = _DATE_RE.search(text)
            if m:
                month_name, day, year = m.groups()
                m_num = _MONTH_MAP.get(month_name, 1)
                return datetime(int(year), m_num, int(day)).strftime("%Y-%m-%d")
    return ""


def _strip_header_prefix(content: str, title: str) -> str:
    """Remove the title and By/Date line from the markdown content."""
    lines = content.split("\n")
    # Remove first line if it's the title (already in our format)
    if lines and lines[0].strip().startswith("# "):
        lines = lines[1:]
    result = []
    skip_prefix = True
    for line in lines:
        if skip_prefix and line.strip().startswith("By ") and "|" in line:
            skip_prefix = False
            continue
        if skip_prefix and not line.strip():
            continue
        result.append(line)
    return "\n".join(result).strip()


def fetch_from_listing_agricidaniel(
    lang_code: str = "zh-cn",
    model: str | None = None,
    no_translate: bool = False,
    max_articles: int | None = None,
) -> int:
    """Fetch all Agrici Daniel blog articles."""
    src = SOURCES["agricidaniel"]
    listing_url = src["listing_url"]
    print(f"Scraping Agrici Daniel blog listing from {listing_url} ...")

    try:
        resp = requests.get(listing_url, timeout=20, headers={
            "User-Agent": "Mozilla/5.0 (compatible; simon-daily/1.0)",
        })
        resp.raise_for_status()
    except Exception as e:
        print(f"  [ERROR] Failed to fetch listing: {e}", file=sys.stderr)
        return 1

    soup = BeautifulSoup(resp.text, "html.parser")
    articles = _parse_agricidaniel_listing(soup)
    print(f"Found {len(articles)} articles")

    articles = articles[:max_articles] if max_articles else articles

    post_dir = get_post_dir("agricidaniel")
    existing_slugs = set()
    for f in post_dir.glob("*.md"):
        if ".zh-cn" not in f.name and ".zh." not in f.name:
            existing_slugs.add(f.stem)

    new_count = 0
    saved = []
    translated = []

    for i, art in enumerate(articles):
        print(f"\n  [{i+1}/{len(articles)}] {art['title']}")

        art_soup = None
        # Fetch the article page to get date
        try:
            art_resp = requests.get(art["url"], timeout=20, headers={
                "User-Agent": "Mozilla/5.0 (compatible; simon-daily/1.0)",
            })
            art_resp.raise_for_status()
            art_soup = BeautifulSoup(art_resp.text, "html.parser")
        except Exception as e:
            print(f"    [SKIP] Failed to fetch article: {e}")
            continue

        date_str = _extract_date_from_article(art_soup, art["url"])
        if not date_str:
            print(f"    [SKIP] Could not extract date")
            continue

        safe_title = slugify(art["title"])
        slug = f"{date_str}-{safe_title}"
        if slug in existing_slugs:
            print(f"    [SKIP] Already saved")
            continue

        # Fetch content as markdown
        full_content = fetch_article_content(art["url"])
        if not full_content:
            print(f"    [SKIP] Failed to fetch content")
            continue

        content = _strip_header_prefix(full_content, art["title"])
        content = re.sub(r'^#\s+.*?\n', '', content, count=1)

        # Parse date for display
        dm = _DATE_RE.search(
            art_soup.find("header").get_text() if art_soup.find("header") else ""
        )
        pub_date = None
        if dm:
            month_name, day, year = dm.groups()
            m_num = _MONTH_MAP.get(month_name, 1)
            pub_date = datetime(int(year), m_num, int(day))
        else:
            pub_date = datetime.strptime(date_str, "%Y-%m-%d")

        md = f"""# {art['title']}

**Date:** {pub_date.strftime('%Y-%m-%d %H:%M UTC') if pub_date else date_str}
**Link:** {art['url']}

---

{content}
"""
        filepath = save_post(date_str, md, art["title"], "agricidaniel")
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
