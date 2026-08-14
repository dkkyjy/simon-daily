# simon-daily 重构实现计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将 1262 行的 `sources.py` 拆分为 `simon_daily/` 包，合并 6 个 utility 脚本为 CLI 子命令，移除 server.py 中的内嵌 SPA。

**Architecture:** 创建 `simon_daily/` Python 包，按职责拆分模块（sources/content/formatters/io/translate/fetcher/scrapers/cli/deploy）。旧文件逐步迁移：先创建包（零破坏），然后逐个更新消费者，最后删除旧代码。

**Tech Stack:** Python 3, feedparser, requests, beautifulsoup4, markdownify, fastapi

## Global Constraints

- 不改变 post 文件格式或磁盘布局
- 不改变 React UI 代码（ui/ 目录）
- 不改变 CI/CD
- 所有函数签名必须与旧 sources.py 完全一致
- 每个步骤完成后必须验证：`python -c "from simon_daily import fetch, list_posts, SOURCES; print('ok')"` 并通过 `python -c "import sources; print('ok')"` 保持向后兼容直到最后一步

---

### Task 1: 创建包结构 + sources 模块

**Files:**
- Create: `simon_daily/__init__.py`
- Create: `simon_daily/sources.py`

**Interfaces:**
- Produces: `SOURCES` (dict), `slugify(text)`, `published_or_updated(entry)`, `get_post_dir(source_key)`
- Consumes: `BASE_DIR` (Path, from old sources.py)

- [ ] **Step 1: 创建目录和空的 `__init__.py`**

```bash
mkdir -p simon_daily
```

```python
# simon_daily/__init__.py
# (empty — will be filled in Task 6)
```

- [ ] **Step 2: 创建 `simon_daily/sources.py`**

从旧 `sources.py` 提取：
- `BASE_DIR` （常量，第 19 行）
- `SOURCES` 字典（第 22-77 行）
- `get_post_dir()`（第 80-84 行）
- `slugify()`（第 87-92 行）
- `published_or_updated()`（第 95-101 行）

```python
"""Blog source definitions and shared utilities."""
import os
import re
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SOURCES = {
    "simon": {
        "name": "Simon Willison",
        "author": "Simon Willison",
        "feed_url": "https://simonwillison.net/atom/everything/",
        "dir": "simon",
        "feed_type": "atom",
        "home_url": "https://simonwillison.net/",
        "listing_url": None,
    },
    "addy": {
        "name": "Addy Osmani",
        "author": "Addy Osmani",
        "feed_url": "https://addyosmani.com/rss.xml",
        "dir": "addy",
        "feed_type": "rss",
        "home_url": "https://addyosmani.com/blog/",
        "listing_url": "https://addyosmani.com/blog/",
    },
    "claude": {
        "name": "Claude Blog",
        "author": "Anthropic",
        "feed_url": None,
        "dir": "claude",
        "feed_type": "listing",
        "home_url": "https://claude.com/blog/",
        "listing_url": "https://claude.com/blog/",
    },
    "anthropic-research": {
        "name": "Anthropic Research",
        "author": "Anthropic",
        "feed_url": None,
        "dir": "anthropic-research",
        "feed_type": "listing",
        "home_url": "https://www.anthropic.com/research",
        "listing_url": "https://www.anthropic.com/research",
    },
    "anthropic-engineering": {
        "name": "Anthropic Engineering",
        "author": "Anthropic",
        "feed_url": None,
        "dir": "anthropic-engineering",
        "feed_type": "listing",
        "home_url": "https://www.anthropic.com/engineering",
        "listing_url": "https://www.anthropic.com/engineering",
    },
    "simon_guides": {
        "name": "Simon Willison Guides",
        "author": "Simon Willison",
        "feed_url": None,
        "dir": "simon_guides",
        "feed_type": "listing",
        "home_url": "https://simonwillison.net/guides/",
        "listing_url": "https://simonwillison.net/guides/",
    },
}


def get_post_dir(source_key):
    """Get the posts sub-directory for a source."""
    d = BASE_DIR / "posts" / SOURCES[source_key]["dir"]
    d.mkdir(parents=True, exist_ok=True)
    return d


def slugify(text):
    """Convert text to URL-safe slug."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')


def published_or_updated(entry):
    """Get publication date from a feed entry."""
    for attr in ("published_parsed", "updated_parsed"):
        val = getattr(entry, attr, None)
        if val:
            return datetime(*val[:6], tzinfo=timezone.utc)
    return None
```

- [ ] **Step 3: 验证包可以导入**

```bash
python -c "from simon_daily.sources import SOURCES, slugify, published_or_updated, get_post_dir; print('sources ok')"
```
Expected: `sources ok`

---

### Task 2: 创建 content 和 formatters 模块

**Files:**
- Create: `simon_daily/content.py`
- Create: `simon_daily/formatters.py`

**Interfaces:**
- Produces: `fetch_article_content(url)`, `format_post(source_key, entry)`, `_format_atom_post(entry)`, `_format_rss_post(source_key, entry)`
- Consumes: from `simon_daily.sources`: `SOURCES`, `published_or_updated`, `slugify`

- [ ] **Step 1: 创建 `simon_daily/content.py`**

从旧 `sources.py` 提取 `fetch_article_content()`（第 104-139 行）。

```python
"""HTTP content fetching and HTML-to-Markdown conversion."""
import re
import sys

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md_convert


def fetch_article_content(url):
    """Fetch full article HTML and convert to markdown."""
    try:
        resp = requests.get(url, timeout=15, headers={
            "User-Agent": "Mozilla/5.0 (compatible; simon-daily/1.0)"
        })
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        # Try various content selectors
        article = (
            soup.find("article", class_="post")
            or soup.find("article")
            or soup.find("main")
            or soup.find("div", class_="content")
            or soup.find("div", class_="entry-content")
            or soup.find("div", class_="post-content")
            or soup.find("div", class_="entry")
        )
        if not article:
            article = soup.find("body")

        # Remove unwanted elements
        for tag in article.find_all(["script", "style", "nav", "footer", "header", "aside"]):
            tag.decompose()

        html_content = str(article)
        markdown = md_convert(html_content, heading_style="ATX", strip=["img", "figure"])
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)
        markdown = markdown.strip()
        return markdown
    except Exception as e:
        print(f"  [WARN] Failed to fetch article content: {e}", file=sys.stderr)
        return None
```

- [ ] **Step 2: 创建 `simon_daily/formatters.py`**

从旧 `sources.py` 提取 `format_post()`, `_format_atom_post()`, `_format_rss_post()`（第 142-256 行）。

```python
"""Format feed entries into post markdown."""
import html
import re
import textwrap
from datetime import datetime, timezone

from simon_daily.sources import SOURCES, published_or_updated
from simon_daily.content import fetch_article_content


def format_post(source_key, entry):
    """Format a feed entry into (date_str, markdown_content)."""
    src = SOURCES[source_key]
    if src["feed_type"] == "atom":
        return _format_atom_post(entry)
    else:
        return _format_rss_post(source_key, entry)


def _format_atom_post(entry):
    """Format an Atom feed entry, fetching full content from URL."""
    title = getattr(entry, "title", "Untitled")
    link = getattr(entry, "link", "")
    tags = []
    for cat in getattr(entry, "tags", []):
        label = getattr(cat, "label", None) or getattr(cat, "term", None)
        if label:
            tags.append(label)

    rss_content = ""
    if hasattr(entry, "content") and entry.content:
        rss_content = entry.content[0].value
    elif hasattr(entry, "description"):
        rss_content = entry.description
    rss_content = html.unescape(rss_content) if rss_content else ""

    print(f"  Fetching full content from {link}...")
    full_content = fetch_article_content(link)

    if full_content:
        content = full_content
        summary_note = re.sub(r'<[^>]+>', '', html.unescape(rss_content))[:200] if rss_content else ""
        if summary_note:
            content = f"> *Feed summary: {summary_note}*\n\n{content}"
    else:
        content = rss_content
        content = html.unescape(content)
        content = re.sub(r'<[^>]+>', '', content)
        content = html.unescape(content)

    tag_line = ", ".join(tags)
    date_display = published_or_updated(entry).strftime("%Y-%m-%d %H:%M UTC") if published_or_updated(entry) else ""

    md = textwrap.dedent(f"""\
        # {title}

        **Date:** {date_display}
        **Link:** {link}
        {"**Tags:** " + tag_line if tag_line else ""}

        ---

        {content}
    """).strip() + "\n"

    date_str = (published_or_updated(entry).strftime("%Y-%m-%d") if published_or_updated(entry)
                else datetime.now(timezone.utc).strftime("%Y-%m-%d"))
    return date_str, md


def _format_rss_post(source_key, entry):
    """Format an RSS feed entry, fetching full content from URL."""
    title = getattr(entry, "title", "Untitled")
    link = getattr(entry, "link", "")
    description = getattr(entry, "description", "")
    description = html.unescape(description) if description else ""

    tag_line = ""
    tags = []
    if hasattr(entry, "tags"):
        for cat in entry.tags:
            label = getattr(cat, "label", None) or getattr(cat, "term", None)
            if label:
                tags.append(label)
        tag_line = ", ".join(tags)

    date_display = ""
    pub_date = published_or_updated(entry)
    if pub_date:
        date_display = pub_date.strftime("%Y-%m-%d %H:%M UTC")

    print(f"  Fetching full content from {link}...")
    full_content = fetch_article_content(link)

    if full_content:
        content = full_content
        summary_note = f"> *Feed summary: {description}*" if description else ""
        content = f"{summary_note}\n\n{content}" if summary_note else content
    else:
        content = description if description else "(No content available)"

    content = re.sub(r'^#\s+.*?\n', '', content, count=1)

    md = textwrap.dedent(f"""\
        # {title}

        **Date:** {date_display}
        **Link:** {link}
        {"**Tags:** " + tag_line if tag_line else ""}

        ---

        {content}
    """).strip() + "\n"

    date_str = pub_date.strftime("%Y-%m-%d") if pub_date else datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return date_str, md
```

- [ ] **Step 3: 验证**

```bash
python -c "from simon_daily.formatters import format_post; print('formatters ok')"
python -c "from simon_daily.content import fetch_article_content; print('content ok')"
```
Expected: `formatters ok`, `content ok`

---

### Task 3: 创建 io 和 translate 模块

**Files:**
- Create: `simon_daily/io.py`
- Create: `simon_daily/translate.py`

**Interfaces:**
- Produces: `save_post(date_str, md, title, source_key)`, `list_posts(source_key, search)`, `get_post(slug, lang)`, `read_post_content(filepath)`, `translate_post(filepath, model, lang_code)`, `save_translation(filepath, lang_code, model)`, `summarize_post(filepath, model)`
- Consumes: from `simon_daily.sources`: `BASE_DIR`, `SOURCES`, `slugify`, `get_post_dir`

- [ ] **Step 1: 创建 `simon_daily/io.py`**

从旧 `sources.py` 提取 `save_post()`（第 259-272 行）、`list_posts()`（第 537-574 行）、`get_post()`（第 577-612 行）、`read_post_content()`（第 615-628 行）。

注意 `list_posts` 和 `get_post` 中使用了 `BASE_DIR` 和 `SOURCES`。

```python
"""File I/O for saved posts."""
from pathlib import Path

from simon_daily.sources import BASE_DIR, SOURCES, slugify, get_post_dir


def save_post(date_str, md, title, source_key):
    """Save a post to disk. Returns filepath if saved, None if already exists."""
    safe_title = slugify(title)
    post_dir = get_post_dir(source_key)
    filepath = post_dir / f"{date_str}-{safe_title}.md"

    if filepath.exists():
        return None

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"  Saved: {filepath.name}")
    return filepath


def list_posts(source_key=None, search=""):
    """List all saved posts for a given source (or all sources).
    Returns list of dicts with title, date, slug, source, has_translation.
    """
    posts = []
    sources_to_list = [source_key] if source_key else list(SOURCES.keys())

    for sk in sources_to_list:
        d = BASE_DIR / "posts" / SOURCES[sk]["dir"]
        if not d.exists():
            continue
        for f in sorted(d.glob("*.md"), reverse=True):
            if f.stem.endswith(".zh-cn") or ".zh." in f.stem or f.stem.endswith(".summary"):
                continue
            slug = f.stem
            zh_path = f.with_suffix(".zh-cn.md")
            has_translation = zh_path.exists()
            with open(f, encoding="utf-8") as fh:
                first_line = fh.readline().strip()
            title = first_line.lstrip("# ").strip() if first_line.startswith("#") else slug
            if search and search.lower() not in title.lower():
                continue
            posts.append({
                "title": title,
                "date": slug[:10],
                "slug": slug,
                "source": sk,
                "source_name": SOURCES[sk]["name"],
                "home_url": SOURCES[sk]["home_url"],
                "has_translation": has_translation,
                "has_summary": f.with_suffix(".summary.md").exists(),
                "orig_file": str(f),
                "zh_file": str(zh_path) if has_translation else "",
            })

    return posts


def get_post(slug, lang="orig"):
    """Get post content by slug. lang='orig' or 'zh-cn' or auto."""
    for sk in SOURCES:
        d = BASE_DIR / "posts" / SOURCES[sk]["dir"]
        for ext in (".md",):
            candidates = list(d.glob(f"{slug}{ext}")) + list(d.glob(f"{slug}*{ext}"))
            for filepath in candidates:
                if "zh-cn" in filepath.name or ".zh." in filepath.name:
                    continue
                if lang == "auto":
                    zh_file = filepath.with_suffix(".zh-cn.md")
                    use_path = zh_file if zh_file.exists() else filepath
                elif lang == "zh-cn":
                    zh_file = filepath.with_suffix(".zh-cn.md")
                    use_path = zh_file if zh_file.exists() else filepath
                else:
                    use_path = filepath

                with open(use_path, encoding="utf-8") as f:
                    content = f.read()

                title = ""
                lines = content.split("\n")
                if lines and lines[0].startswith("# "):
                    title = lines[0][2:]

                return {
                    "title": title,
                    "content": content,
                    "filepath": str(filepath),
                }
    return None


def read_post_content(filepath):
    """Read a markdown post file and return title + content."""
    filepath = Path(filepath)
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
    title = ""
    lines = content.split("\n")
    if lines and lines[0].startswith("# "):
        title = lines[0][2:]
    return {
        "title": title,
        "content": content,
        "filepath": str(filepath),
    }
```

- [ ] **Step 2: 创建 `simon_daily/translate.py`**

从旧 `sources.py` 提取 `translate_post()`（第 275-310 行）、`save_translation()`（第 313-315 行）、`summarize_post()`（第 631-677 行）。

```python
"""Translation and summarization via fabric-ai."""
import shutil
import subprocess
import sys
from pathlib import Path


def translate_post(filepath, model=None, lang_code="zh-cn"):
    """Translate a post using fabric-ai. Accepts str or Path."""
    fabric_bin = shutil.which("fabric-ai") or shutil.which("fabric")
    if not fabric_bin:
        print("  [SKIP] fabric-ai not found", file=sys.stderr)
        return None

    filepath = Path(filepath)
    zh_path = filepath.with_suffix(f".{lang_code}.md")
    if zh_path.exists():
        print(f"  [SKIP] {zh_path.name} exists")
        return zh_path

    try:
        with open(filepath, encoding="utf-8") as fh:
            file_content = fh.read()
        cmd = [fabric_bin, "-p", "translate", "-v", f"lang_code:{lang_code}"]
        if model:
            cmd += ["-m", model]
        resp = subprocess.run(cmd, input=file_content, capture_output=True, text=True, timeout=180)
        if resp.returncode != 0:
            print(f"  [ERROR] fabric translate failed (rc={resp.returncode}): {resp.stderr[:200]}", file=sys.stderr)
            return None
        translated = resp.stdout.strip()
        if not translated:
            print(f"  [ERROR] empty fabric output", file=sys.stderr)
            return None

        with open(zh_path, "w", encoding="utf-8") as f:
            f.write(translated + "\n")
        print(f"  Translated: {zh_path.name}")
        return zh_path
    except Exception as e:
        print(f"  [ERROR] Translation error: {e}", file=sys.stderr)
        return None


def save_translation(filepath, lang_code="zh-cn", model=None):
    """Public API: translate a single post file."""
    return translate_post(filepath, model=model, lang_code=lang_code)


def summarize_post(filepath, model=None):
    """Generate a summary for a post using fabric-ai summarize pattern.
    Returns dict with 'summary' text or None on failure.
    """
    filepath = Path(filepath)
    summary_file = filepath.with_suffix(".summary.md")

    if summary_file.exists():
        with open(summary_file, encoding="utf-8") as f:
            return {"summary": f.read(), "cached": True}

    fabric_bin = shutil.which("fabric-ai") or shutil.which("fabric")
    if not fabric_bin:
        print("  [ERROR] fabric-ai/fabric not found", file=sys.stderr)
        return None

    try:
        with open(filepath, encoding="utf-8") as fh:
            file_content = fh.read()

        cmd = [fabric_bin, "-p", "summarize"]
        if model:
            cmd += ["-m", model]
        resp = subprocess.run(cmd, input=file_content, capture_output=True, text=True, timeout=180)

        if resp.returncode != 0:
            print(f"  [ERROR] fabric summarize failed (rc={resp.returncode}): {resp.stderr.strip()}", file=sys.stderr)
            return None

        summary = resp.stdout.strip()
        if not summary:
            print(f"  [ERROR] fabric summarize returned empty output", file=sys.stderr)
            return None

        with open(summary_file, "w", encoding="utf-8") as f:
            f.write(summary)

        return {"summary": summary, "cached": False}
    except subprocess.TimeoutExpired:
        print(f"  [ERROR] fabric summarize timed out for {filepath}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"  [ERROR] summarize failed: {e}", file=sys.stderr)
        return None
```

- [ ] **Step 3: 验证**

```bash
python -c "from simon_daily.io import save_post, list_posts, read_post_content; print('io ok')"
python -c "from simon_daily.translate import translate_post, summarize_post; print('translate ok')"
```

---

### Task 4: 创建 scrapers 子包

**Files:**
- Create: `simon_daily/scrapers/__init__.py`
- Create: `simon_daily/scrapers/claude.py`
- Create: `simon_daily/scrapers/anthropic_research.py`
- Create: `simon_daily/scrapers/anthropic_engineering.py`

**Interfaces:** 3 listing fetchers + helper functions, identical to old sources.py

- [ ] **Step 1: 创建 `simon_daily/scrapers/__init__.py`**

```python
# scrapers package
from simon_daily.scrapers.claude import fetch_from_listing_claude, _claude_extract_article
from simon_daily.scrapers.anthropic_research import (
    fetch_from_listing_anthropic_research,
    _parse_anthropic_research_listing,
    _strip_anthropic_research_prefix,
)
from simon_daily.scrapers.anthropic_engineering import (
    fetch_from_listing_anthropic_engineering,
    _parse_anthropic_engineering_listing,
    _extract_anthropic_engineering_date,
)

__all__ = [
    "fetch_from_listing_claude",
    "_claude_extract_article",
    "fetch_from_listing_anthropic_research",
    "_parse_anthropic_research_listing",
    "_strip_anthropic_research_prefix",
    "fetch_from_listing_anthropic_engineering",
    "_parse_anthropic_engineering_listing",
    "_extract_anthropic_engineering_date",
]
```

- [ ] **Step 2: 创建 `simon_daily/scrapers/claude.py`**

从旧 `sources.py` 的 `# ── Claude Blog Fetcher ──` 部分提取（第 680-888 行）。代码以字面方式复制，更改导入路径。

```python
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
```

- [ ] **Step 3: 创建 `simon_daily/scrapers/anthropic_research.py`**

从旧 `sources.py` 的 `# ── Anthropic Research Fetcher ──` 部分提取（第 891-1072 行）。

```python
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
        title = link.get_text(strip=True)
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
```

- [ ] **Step 4: 创建 `simon_daily/scrapers/anthropic_engineering.py`**

从旧 `sources.py` 的 `# ── Anthropic Engineering Fetcher ──` 部分提取（第 1075-1262 行）。

```python
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
```

- [ ] **Step 5: 验证 scrapers 可以导入**

```bash
python -c "from simon_daily.scrapers.claude import fetch_from_listing_claude; print('scraper claude ok')"
python -c "from simon_daily.scrapers.anthropic_research import fetch_from_listing_anthropic_research; print('scraper research ok')"
python -c "from simon_daily.scrapers.anthropic_engineering import fetch_from_listing_anthropic_engineering; print('scraper engineering ok')"
```

---

### Task 5: 创建 fetcher 模块

**Files:**
- Create: `simon_daily/fetcher.py`

**Interfaces:**
- Produces: `fetch(source_key, days, lang_code, model, no_translate)`, `fetch_from_listing(source_key, year, lang_code, model, no_translate)`
- Consumes: from `simon_daily.sources`: `SOURCES`; from `simon_daily.formatters`: `format_post`; from `simon_daily.io`: `save_post`; from `simon_daily.translate`: `translate_post`; from `simon_daily.scrapers`: `fetch_from_listing_claude`, `fetch_from_listing_anthropic_research`, `fetch_from_listing_anthropic_engineering`

- [ ] **Step 1: 创建 `simon_daily/fetcher.py`**

从旧 `sources.py` 提取 `fetch()`（第 318-374 行）和 `fetch_from_listing()`（第 377-535 行，不含 Addy 分页抓取的一部分）。

```python
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
```

- [ ] **Step 2: 验证 fetcher 可以导入**

```bash
python -c "from simon_daily.fetcher import fetch, fetch_from_listing; print('fetcher ok')"
```

---

### Task 6: 创建 CLI 和 deploy 模块 + 更新 __init__.py

**Files:**
- Modify: `simon_daily/__init__.py`
- Create: `simon_daily/cli.py`
- Create: `simon_daily/deploy.py`

**Interfaces:**
- Produces: `cli.main()`, `deploy.deploy_zh_to_site()`, `deploy.run_fetch_all()`, `deploy.daily_main()`
- `__init__.py` 重新导出所有公共 API

- [ ] **Step 1: 更新 `simon_daily/__init__.py`**

```python
"""simon-daily - Multi-source blog fetcher with translation support."""

from simon_daily.sources import (
    SOURCES,
    BASE_DIR,
    slugify,
    published_or_updated,
    get_post_dir,
)

from simon_daily.content import fetch_article_content

from simon_daily.formatters import format_post, _format_atom_post, _format_rss_post

from simon_daily.io import save_post, list_posts, get_post, read_post_content

from simon_daily.translate import translate_post, save_translation, summarize_post

from simon_daily.fetcher import fetch, fetch_from_listing

from simon_daily.scrapers import (
    fetch_from_listing_claude,
    _claude_extract_article,
    fetch_from_listing_anthropic_research,
    _parse_anthropic_research_listing,
    _strip_anthropic_research_prefix,
    fetch_from_listing_anthropic_engineering,
    _parse_anthropic_engineering_listing,
    _extract_anthropic_engineering_date,
)

# Backward-compat alias for fetch_all_anthropic.py
_strip_anthropic_prefix = _strip_anthropic_research_prefix

__all__ = [
    # Config
    "SOURCES", "BASE_DIR",
    # Utils
    "slugify", "published_or_updated", "get_post_dir",
    # Content
    "fetch_article_content",
    # Formatters
    "format_post", "_format_atom_post", "_format_rss_post",
    # I/O
    "save_post", "list_posts", "get_post", "read_post_content",
    # Translate
    "translate_post", "save_translation", "summarize_post",
    # Fetcher
    "fetch", "fetch_from_listing",
    # Scrapers
    "fetch_from_listing_claude", "_claude_extract_article",
    "fetch_from_listing_anthropic_research", "_parse_anthropic_research_listing",
    "_strip_anthropic_research_prefix",
    "fetch_from_listing_anthropic_engineering", "_parse_anthropic_engineering_listing",
    "_extract_anthropic_engineering_date",
    # Backward compat
    "_strip_anthropic_prefix",
]
```

- [ ] **Step 2: 创建 `simon_daily/cli.py`**

合并 6 个 utility 脚本的逻辑为子命令。

```python
"""CLI entry point with subcommands for fetch, translation, and summarization."""
import argparse
import os
import sys

from simon_daily import (
    fetch, fetch_from_listing, SOURCES, list_posts,
    translate_post, summarize_post,
)


def cmd_fetch(args):
    """python -m simon_daily fetch [--source addy] [--days 3]"""
    if args.listing:
        return fetch_from_listing(
            source_key=args.source, year=2026,
            lang_code=args.lang, model=args.model, no_translate=args.no_translate,
        )
    return fetch(
        source_key=args.source, days=args.days,
        lang_code=args.lang, model=args.model, no_translate=args.no_translate,
    )


def cmd_translate_remaining(args):
    """Translate all untranslated posts for a given source."""
    posts = list_posts(source_key=args.source)
    to_translate = [p["orig_file"] for p in posts if not p.get("has_translation")]
    if not to_translate:
        print("All translated!")
        return 0
    print(f"Translating {len(to_translate)} remaining posts...")
    count = 0
    for i, fp in enumerate(to_translate):
        fname = os.path.basename(fp)
        try:
            result = translate_post(fp, lang_code=args.lang, model=args.model)
            if result:
                count += 1
                print(f"  [{i+1}/{len(to_translate)}] OK: {fname[:50]}")
            else:
                print(f"  [{i+1}/{len(to_translate)}] FAIL: {fname[:50]}")
        except Exception as e:
            print(f"  [{i+1}/{len(to_translate)}] ERROR: {e}")
        sys.stdout.flush()
    print(f"Done: {count}/{len(to_translate)} translated")
    return 0


def cmd_summarize(args):
    """Generate summaries for untranslated posts of a given source."""
    posts = list_posts(source_key=args.source)
    to_summarize = []
    for p in posts:
        fp = p["orig_file"]
        summary_fp = os.path.splitext(fp)[0] + ".summary.md"
        if not os.path.exists(summary_fp):
            to_summarize.append(fp)
    if not to_summarize:
        print("All already summarized!")
        return 0
    print(f"Summarizing {len(to_summarize)} posts...")
    count = 0
    for i, fp in enumerate(to_summarize):
        fname = os.path.basename(fp)
        try:
            result = summarize_post(fp, model=args.model)
            if result:
                count += 1
                print(f"  [{i+1}/{len(to_summarize)}] OK: {fname[:50]}")
            else:
                print(f"  [{i+1}/{len(to_summarize)}] FAIL: {fname[:50]}")
        except Exception as e:
            print(f"  [{i+1}/{len(to_summarize)}] ERROR: {e}")
        sys.stdout.flush()
    print(f"Done: {count}/{len(to_summarize)} summarized")
    return 0


def cmd_fetch_all_anthropic(args):
    """Batch-fetch all Anthropic Research articles via sitemap."""
    from simon_daily.scrapers.anthropic_research import fetch_from_listing_anthropic_research
    return fetch_from_listing_anthropic_research(
        lang_code=args.lang, model=args.model, no_translate=args.no_translate,
    )


def main():
    parser = argparse.ArgumentParser(description="simon-daily blog fetcher")
    parser.add_argument("--source", choices=list(SOURCES.keys()), default="simon",
                        help=f"Blog source ({', '.join(SOURCES.keys())})")
    parser.add_argument("--days", type=int, default=1, help="Days back (default: 1)")
    parser.add_argument("--lang", default="zh-cn", help="Target language (default: zh-cn)")
    parser.add_argument("--model", default=None, help="LLM model for fabric")
    parser.add_argument("--no-translate", action="store_true", help="Skip translation")
    parser.add_argument("--listing", action="store_true", help="Force listing mode")

    subparsers = parser.add_subparsers(dest="command", help="Subcommands")

    # fetch (default)
    # translate-remaining
    p = subparsers.add_parser("translate-remaining", help="Translate all untranslated posts")
    p.add_argument("--source", default="simon", choices=list(SOURCES.keys()))
    p.add_argument("--lang", default="zh-cn")
    p.add_argument("--model", default=None)

    # summarize
    p = subparsers.add_parser("summarize", help="Generate AI summaries")
    p.add_argument("--source", default="claude", choices=list(SOURCES.keys()))
    p.add_argument("--model", default=None)

    # fetch-all-anthropic
    p = subparsers.add_parser("fetch-all-anthropic", help="Batch-fetch all Anthropic Research articles")
    p.add_argument("--lang", default="zh-cn")
    p.add_argument("--model", default=None)
    p.add_argument("--no-translate", action="store_true")

    args = parser.parse_args()

    if args.command == "translate-remaining":
        sys.exit(cmd_translate_remaining(args))
    elif args.command == "summarize":
        sys.exit(cmd_summarize(args))
    elif args.command == "fetch-all-anthropic":
        sys.exit(cmd_fetch_all_anthropic(args))
    else:
        # Default: fetch
        sys.exit(cmd_fetch(args))


if __name__ == "__main__":
    main()
```

- [ ] **Step 3: 创建 `simon_daily/deploy.py`**

从 `daily_task.py` 提取部署逻辑。

```python
"""Deploy Chinese translations to personal Astro site."""
import os
import re
import subprocess
import sys
import time
from pathlib import Path

from simon_daily import fetch, SOURCES, translate_post, list_posts

SIMON_DAILY_DIR = Path(__file__).resolve().parent.parent
SITE_BLOG = Path.home() / "storage/github/ac-site-template/src/content/blog"
ASTRO_DIR = Path.home() / "storage/github/ac-site-template"

DEPLOY_SOURCES = {
    "addy": {"tag": "addy-osmani", "dir": SIMON_DAILY_DIR / "posts/addy"},
    "claude": {"tag": "claude-blog", "dir": SIMON_DAILY_DIR / "posts/claude"},
    "anthropic-research": {"tag": "anthropic-research", "dir": SIMON_DAILY_DIR / "posts/anthropic-research"},
    "simon_guides": {"tag": "simon-guides", "dir": SIMON_DAILY_DIR / "posts/simon_guides"},
    "anthropic-engineering": {"tag": "anthropic-engineering", "dir": SIMON_DAILY_DIR / "posts/anthropic-engineering"},
}


def setup_env():
    """Ensure fabric-ai is in PATH for subprocess calls."""
    os.environ.setdefault("PATH",
        f"{os.environ.get('PATH', '')}:/opt/homebrew/bin:/usr/local/bin")


def run_fetch(source_key, days, dry_run=False):
    """Fetch and translate posts for one source."""
    print(f"\n{'='*60}")
    print(f"▶ Fetching [{source_key}] (past {days} day(s))")
    print(f"{'='*60}")
    if dry_run:
        print(f"  [DRY-RUN] Would fetch {source_key} with days={days}")
        return 0
    src = SOURCES[source_key]
    if src.get("feed_url"):
        return fetch(source_key=source_key, days=days, lang_code="zh-cn", no_translate=False)
    else:
        return fetch(source_key=source_key, lang_code="zh-cn", no_translate=False)


def deploy_zh_to_site(dry_run=False):
    """Deploy non-Simon Chinese translation files to personal website."""
    print(f"\n{'='*60}")
    print(f"▶ Deploying Chinese versions to personal site")
    print(f"{'='*60}")
    if not SITE_BLOG.exists():
        print(f"  [ERROR] Personal site blog dir not found: {SITE_BLOG}")
        return 1
    total_copied = 0
    total_errors = 0
    for src_key, cfg in DEPLOY_SOURCES.items():
        src_dir = cfg["dir"]
        tag = cfg["tag"]
        if not src_dir.exists():
            print(f"  [SKIP] {src_key} dir not found: {src_dir}")
            continue
        copied = 0
        for fname in os.listdir(str(src_dir)):
            if not fname.endswith(".zh-cn.md"):
                continue
            slug = fname[:-len(".zh-cn.md")]
            target = SITE_BLOG / f"{slug}.md"
            if target.exists():
                continue
            src_path = src_dir / fname
            try:
                with open(src_path, encoding="utf-8") as f:
                    content = f.read()
                title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
                title = title_match.group(1).strip() if title_match else slug.replace("-", " ").title()
                date_match = re.search(r'\*\*日期：\*\*\s*(\d{4}-\d{2}-\d{2})', content)
                pub_date = date_match.group(1) if date_match else slug[:10]
                link_match = re.search(r'\*\*链接：\*\*\s*(https?://\S+)', content)
                orig_link = link_match.group(1) if link_match else ""
                desc_match = re.search(
                    r'\*\*链接：\*\*\s*\S+\s*\n\n(.+?)(?:\n\n|\n##|\Z)',
                    content, re.DOTALL
                )
                description = desc_match.group(1).strip().replace('"', "'")[:200] if desc_match else title
                body = re.sub(
                    r'\n\s*\*\*日期：\*\*.*?\*\*链接：\*\*\s*\S+',
                    '', content, count=1, flags=re.DOTALL
                ).strip()
                frontmatter = f"""---
title: "{title}"
description: "{description}"
pubDate: "{pub_date}"
heroImage: "/post_img.png"
tags: ["{tag}"]
originalLink: "{orig_link}"
---

{body}
"""
                if dry_run:
                    print(f"  [DRY-RUN] Would deploy: {slug} → {tag}")
                    copied += 1
                else:
                    with open(target, "w", encoding="utf-8") as f:
                        f.write(frontmatter)
                    copied += 1
                    print(f"  ✅ {src_key}: {slug}")
            except Exception as e:
                total_errors += 1
                print(f"  ❌ {slug}: {e}")
        if copied > 0:
            print(f"  {src_key}: {copied} new article(s) deployed")
        total_copied += copied
    print(f"\n  Summary: {total_copied} deployed, {total_errors} errors")
    return total_copied


def restart_astro(dry_run=False):
    """Restart the Astro dev server."""
    if dry_run:
        print("\n  [DRY-RUN] Would restart Astro dev server on port 1234")
        return 0
    print("\n▶ Restarting Astro dev server...")
    try:
        result = subprocess.run(
            ["lsof", "-ti", ":1234"],
            capture_output=True, text=True, timeout=10
        )
        if result.stdout.strip():
            pids = result.stdout.strip().split()
            for pid in pids:
                try:
                    os.kill(int(pid), 15)
                    print(f"  Killed PID {pid}")
                except (OSError, ValueError):
                    pass
            time.sleep(1)
    except Exception as e:
        print(f"  [WARN] Could not kill old server: {e}")
    log_file = "/tmp/astro-dev.log"
    try:
        subprocess.Popen(
            ["npx", "astro", "dev", "--port", "1234"],
            cwd=str(ASTRO_DIR),
            stdout=open(log_file, "a"),
            stderr=subprocess.STDOUT,
            env={**os.environ, "BROWSER": "none"},
        )
        print(f"  Astro dev server starting on port 1234 (log: {log_file})")
        for i in range(15):
            time.sleep(1)
            try:
                r = subprocess.run(
                    ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}",
                     "http://localhost:1234/"],
                    capture_output=True, text=True, timeout=5
                )
                if r.stdout.strip() in ("200", "301", "302"):
                    print(f"  ✅ Server ready after {i+1}s")
                    break
            except Exception:
                pass
        else:
            print("  ⚠️  Server may still be starting (timeout)")
    except Exception as e:
        print(f"  [ERROR] Failed to start Astro: {e}")
        return 1
    return 0


def daily_main():
    """Main entry for daily_task.py."""
    import argparse
    parser = argparse.ArgumentParser(description="Daily blog fetch+translate+deploy task")
    parser.add_argument("--days", type=int, default=1, help="Days back (default: 1)")
    parser.add_argument("--dry-run", action="store_true", help="Dry run")
    parser.add_argument("--no-deploy", action="store_true", help="Skip deployment")
    parser.add_argument("--no-restart", action="store_true", help="Skip Astro restart")
    args = parser.parse_args()

    setup_env()

    sources_to_fetch = ["simon", "addy", "claude", "anthropic-research", "simon_guides", "anthropic-engineering"]
    for sk in sources_to_fetch:
        run_fetch(sk, args.days, dry_run=args.dry_run)

    if args.no_deploy:
        print("\n⏭️  Skipping deployment (--no-deploy)")
    else:
        new_count = deploy_zh_to_site(dry_run=args.dry_run)
        if new_count and not args.dry_run:
            if not args.no_restart:
                restart_astro(dry_run=False)

    print(f"\n{'='*60}")
    print(f"✅ Daily task completed!")
    print(f"{'='*60}")
    return 0
```

- [ ] **Step 4: 完整验证**

```bash
python -c "
from simon_daily import (
    SOURCES, slugify, get_post_dir,
    fetch_article_content,
    format_post,
    save_post, list_posts, read_post_content,
    translate_post, summarize_post,
    fetch, fetch_from_listing,
    _strip_anthropic_prefix,
    _claude_extract_article,
)
print('ALL IMPORTS OK')
print(f'Sources: {len(SOURCES)} configured')
print(f'SOURCES keys: {list(SOURCES.keys())}')
"
```

Expected: `ALL IMPORTS OK`, `Sources: 6 configured`

---

### Task 7: 更新 server.py — 移除内嵌 SPA，挂载 React 静态文件

**Files:**
- Modify: `server.py`

- [ ] **Step 1: 更新 `server.py` 的导入和 API 路由**

变更：
1. 将 `from sources import ...` 改为 `from simon_daily import ...`
2. 删除 `HTML_TEMPLATE` 整个字符串（第 172-629 行）
3. 添加 FastAPI StaticFiles 挂载
4. `index()` 路由改为提供 SPA 入口

修改后的文件结构：

```python
#!/usr/bin/env python3
"""simon-daily Web UI - FastAPI 后端（多源）"""
import os
import sys
import json
import threading
from pathlib import Path
from datetime import datetime

from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

from simon_daily import (
    SOURCES, list_posts, read_post_content, save_translation, fetch, get_post_dir,
    summarize_post,
)

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="Simon Willison Daily Reader")

# ── API 路由 ──────────────────────────────────

@app.get("/api/sources")
def api_sources():
    """Return available blog sources."""
    return [
        {"key": k, "name": v["name"], "home_url": v["home_url"]}
        for k, v in SOURCES.items()
    ]

@app.get("/api/posts")
def api_list_posts(
    search: str = Query(""),
    source: str = Query(""),
):
    posts = list_posts(source_key=source if source else None, search=search)
    return posts

@app.get("/api/posts/{slug}")
def api_get_post(slug: str, lang: str = Query("orig")):
    """Get post content by slug."""
    posts = list_posts()
    match = [p for p in posts if p["slug"] == slug]
    if not match:
        return JSONResponse({"error": "not found"}, status_code=404)
    post = match[0]
    if lang == "zh" and post["zh_file"]:
        content = read_post_content(post["zh_file"])
    else:
        content = read_post_content(post["orig_file"])
    return {
        "slug": post["slug"],
        "title": content["title"],
        "content": content["content"],
        "source": post["source"],
        "source_name": post["source_name"],
        "has_translation": post["has_translation"],
    }

@app.post("/api/fetch/{source_key}")
def api_fetch(source_key: str, days: int = Query(1)):
    """Fetch posts from a blog source."""
    if source_key not in SOURCES:
        return JSONResponse({"error": f"Unknown source: {source_key}"}, status_code=400)
    def _run():
        print(f"[background] Fetching {source_key} days={days}", file=sys.stderr)
        fetch(source_key=source_key, days=days, no_translate=False)
    thread = threading.Thread(target=_run, daemon=True)
    thread.start()
    return JSONResponse({
        "status": "started",
        "message": f"正在抓取 {SOURCES[source_key]['name']} 最近 {days} 天的文章并翻译...",
    })

@app.post("/api/translate/{slug}")
def api_translate(slug: str):
    """Translate a single post."""
    posts = list_posts()
    match = [p for p in posts if p["slug"] == slug]
    if not match:
        return JSONResponse({"error": "not found"}, status_code=404)
    post = match[0]
    if post["has_translation"]:
        return JSONResponse({"status": "done", "message": "已翻译"})
    src_path = Path(post["orig_file"])
    def _run():
        try:
            save_translation(src_path, lang_code="zh-cn")
        except Exception as e:
            print(f"Translate error: {e}", file=sys.stderr)
    thread = threading.Thread(target=_run, daemon=True)
    thread.start()
    return JSONResponse({
        "status": "started",
        "message": f"正在翻译: {post['title']}",
    })

@app.post("/api/posts/{slug}/summary")
def api_summarize_post(slug: str):
    """Generate or retrieve cached summary for a post."""
    posts = list_posts()
    match = [p for p in posts if p["slug"] == slug]
    if not match:
        return JSONResponse({"error": "not found"}, status_code=404)
    post = match[0]
    filepath = post["orig_file"]
    result = summarize_post(filepath)
    if result is None:
        return JSONResponse({
            "error": "summary_failed",
            "message": "生成摘要失败，请稍后重试",
        }, status_code=500)
    return JSONResponse({
        "slug": slug,
        "summary": result["summary"],
        "cached": result["cached"],
    })

@app.get("/api/posts/{slug}/summary")
def api_get_summary(slug: str):
    """Get cached summary if available."""
    posts = list_posts()
    match = [p for p in posts if p["slug"] == slug]
    if not match:
        return JSONResponse({"error": "not found"}, status_code=404)
    post = match[0]
    summary_file = Path(post["orig_file"]).with_suffix(".summary.md")
    if summary_file.exists():
        content = summary_file.read_text(encoding="utf-8")
        return JSONResponse({
            "slug": slug,
            "summary": content,
            "cached": True,
        })
    return JSONResponse({
        "slug": slug,
        "summary": None,
        "cached": False,
    })

# ── Static files (React SPA) ──────────────────
UI_DIST = BASE_DIR / "ui/dist"
if UI_DIST.exists():
    app.mount("/", StaticFiles(directory=str(UI_DIST), html=True), name="ui")

# ── 启动 ──────────────────────────────────────
if __name__ == "__main__":
    print(f"🚀 simon-daily UI: http://127.0.0.1:8080")
    uvicorn.run(app, host="127.0.0.1", port=8080)
```

- [ ] **Step 2: 验证 server.py 可以启动**

```bash
python server.py &
sleep 2
curl -s http://127.0.0.1:8080/api/sources | head -c 200
echo ""
curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8080/
echo ""
kill %1 2>/dev/null
```

Expected: API 返回正常，`/` 返回 200（React SPA）

---

### Task 8: 重写根目录入口文件 + 删除旧 utility 脚本

**Files:**
- Modify: `fetch.py`
- Modify: `daily_task.py`
- Delete: `batch_anthropic.py`
- Delete: `fetch_all_anthropic.py`
- Delete: `fetch_guides.py`
- Delete: `translate_guides.py`
- Delete: `translate_remaining.py`
- Delete: `summarize_claude.py`

- [ ] **Step 1: 重写 `fetch.py`**

```python
#!/usr/bin/env python3
"""simon-daily - Multi-source blog fetcher with translation.

Usage:
    python fetch.py [--source simon|addy] [--days 1] [--no-translate]
"""
from simon_daily.cli import main

if __name__ == "__main__":
    main()
```

- [ ] **Step 2: 重写 `daily_task.py`**

```python
#!/usr/bin/env python3
"""Daily scheduled task for simon-daily.
Usage:
    python daily_task.py [--days 1] [--dry-run] [--no-deploy]
"""
from simon_daily.deploy import daily_main

if __name__ == "__main__":
    daily_main()
```

- [ ] **Step 3: 验证入口文件仍然可用**

```bash
python fetch.py --help
python daily_task.py --help
```

Expected: 两个命令正常显示帮助信息

- [ ] **Step 4: 删除旧的 utility 脚本**

```bash
git rm batch_anthropic.py fetch_all_anthropic.py fetch_guides.py translate_guides.py translate_remaining.py summarize_claude.py
```

- [ ] **Step 5: 再次验证核心功能**

```bash
python -c "
from simon_daily import SOURCES, list_posts, read_post_content
posts = list_posts()
print(f'Total saved posts: {len(posts)}')
for s in list(SOURCES.keys()):
    sp = list_posts(source_key=s)
    print(f'  {s}: {len(sp)} posts')
"
```

Expected: 列出所有源和文章数量

---

### Task 9: 删除旧的 sources.py

**Files:**
- Delete: `sources.py`

- [ ] **Step 1: 确认没有文件再导入旧的 sources.py**

```bash
grep -rn "from sources import\|import sources\|from sources\.\|import sources as" *.py simon_daily/*.py simon_daily/**/*.py 2>/dev/null || echo "No remaining references"
```

Expected: `No remaining references`（或仅 simon_daily 包内的引用，但包本身不再依赖旧文件）

- [ ] **Step 2: 删除旧文件**

```bash
git rm sources.py
```

- [ ] **Step 3: 最终验证**

```bash
python -c "
from simon_daily import SOURCES, list_posts, fetch, slugify
print(f'Package OK: {len(SOURCES)} sources')
import server
print('server.py imports OK')
import fetch
print('fetch.py imports OK')
import daily_task  
print('daily_task.py imports OK')
"
```

```bash
python -c "import sources" 2>&1 || echo "sources.py no longer exists (expected)"
```

---

### 验证清单（最终）

- [ ] 所有 `simon_daily/` 模块可以导入
- [ ] `from simon_daily import fetch, list_posts, SOURCES, translate_post` 正常工作
- [ ] `python fetch.py --help` 显示帮助
- [ ] `python daily_task.py --help` 显示帮助
- [ ] `python server.py` 启动 API 且 `/api/sources` 返回 JSON
- [ ] React SPA 可以在 `http://127.0.0.1:8080` 访问
- [ ] 旧的 utility 脚本已全部删除
- [ ] 旧的 `sources.py` 已删除
- [ ] 每个源的文章列在 `posts/` 目录下（数据未丢失）
