"""Claude Blog listing scraper."""
import re
import sys
import time
from datetime import datetime, timezone

import requests
from bs4 import BeautifulSoup

from simon_daily.content import fetch_article_content
from simon_daily.io import save_post, get_post_dir
from simon_daily.translate import translate_post
from simon_daily.sources import SOURCES, slugify


def _claude_extract_article(url):
    """Fetch a single Claude blog article and return (title, date_str, date_obj, markdown)."""
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}
    try:
        resp = requests.get(url, timeout=20, headers=headers)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, 'html.parser')
        title = None
        title_tag = soup.find('title')
        if title_tag:
            title = title_tag.get_text(strip=True).replace(' | Claude Blog', '').strip()
        if not title:
            h1 = soup.find('h1')
            if h1:
                title = h1.get_text(strip=True)
        if not title:
            title = "Untitled"

        date_str = ""
        date_obj = None
        hero = soup.select_one('[class*="hero"], [class*="Hero"]')
        if hero:
            text = hero.get_text(separator=' ', strip=True)
            m = re.search(r'(\w+)\s+(\d+),?\s*(\d{4})', text)
            if m:
                month, day, year = m.groups()
                months = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
                          "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}
                m_num = months.get(month, 1)
                date_obj = datetime(int(year), m_num, int(day))
                date_str = date_obj.strftime("%Y-%m-%d")

        content_div = soup.select_one('div.u-rich-text-blog')
        if not content_div:
            content_div = soup.select_one('[class*="content"], [class*="Content"], article')
        if not content_div:
            content_div = soup.find('body')

        for tag in content_div.find_all(['script', 'style', 'nav', 'footer', 'header', 'aside']):
            tag.decompose()

        content_html = str(content_div)
        from markdownify import markdownify as md_convert
        markdown = md_convert(content_html, heading_style="ATX", strip=["img", "figure"])
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)
        markdown = markdown.strip()

        return title, date_str, date_obj, markdown
    except Exception as e:
        print(f"  [ERROR] Failed to extract Claude article: {e}", file=sys.stderr)
        return None


def fetch_from_listing_claude(lang_code="zh-cn", model=None, no_translate=False, max_pages=None):
    """Fetch all Claude blog articles by scraping the listing page."""
    BASE = "https://claude.com/blog"
    src = SOURCES["claude"]
    print(f"Scraping Claude blog listing from {BASE} ...")

    article_links = set()
    page = 1
    while max_pages is None or page <= max_pages:
        paginated_url = BASE if page == 1 else f"{BASE}?b7eea976_page={page}"
        print(f"  Page {page}: {paginated_url}")
        try:
            resp = requests.get(paginated_url, timeout=20, headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
            })
            resp.raise_for_status()
        except Exception as e:
            print(f"    [WARN] Failed to fetch page {page}: {e}")
            break

        soup = BeautifulSoup(resp.text, 'html.parser')
        links = soup.find_all('a', href=True)
        page_links = set()
        for a in links:
            href = a['href']
            if href.startswith('/blog/') and href != '/blog/':
                full_url = f"https://claude.com{href}"
                page_links.add(full_url)

        if not page_links:
            print(f"    No article links found on page {page}, stopping")
            break

        before = len(article_links)
        article_links.update(page_links)
        print(f"    Found {len(page_links)} links ({len(article_links) - before} new)")
        page += 1
        time.sleep(0.5)

    print(f"\nFound {len(article_links)} total article URLs")

    post_dir = get_post_dir("claude")
    existing_slugs = set()
    for f in post_dir.glob("*.md"):
        if ".zh-cn" not in f.name:
            existing_slugs.add(f.stem)

    new_count = 0
    saved = []
    translated = []

    for i, url in enumerate(sorted(article_links)):
        print(f"\n  [{i+1}/{len(article_links)}] {url}")

        result = _claude_extract_article(url)
        if result is None:
            continue
        title, date_str, date_obj, markdown = result
        if not date_str:
            print(f"    [SKIP] No date found for {url}")
            continue

        safe_title = slugify(title)
        slug = f"{date_str}-{safe_title}"
        if slug in existing_slugs:
            print(f"    [SKIP] Already saved")
            continue

        md = f"""# {title}

**Date:** {date_obj.strftime('%Y-%m-%d %H:%M UTC') if date_obj else ''}
**Link:** {url}

---

{markdown}
"""
        filepath = save_post(date_str, md, title, "claude")
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
