"""OpenAI Research listing scraper (RSC payload based).

OpenAI research index (https://openai.com/zh-Hans-CN/research/index/) and
article pages are Next.js App Router pages: content lives in
`<script>self.__next_f.push([1,"..."])</script>` RSC payloads, NOT in
server-rendered HTML. The listing items and article body are extracted from
those payloads with regexes on the JS-escaped JSON (`\\"` = escaped quote).
"""
import re
import sys
from datetime import datetime, timezone

import requests

from simon_daily.io import save_post, get_post_dir
from simon_daily.translate import translate_post
from simon_daily.sources import SOURCES, slugify

_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
}

_RSC_SCRIPT_RE = re.compile(r'<script>self\.__next_f\.push\(\[1,"(.*?)"\]\)</script>', re.S)

# Listing item: slug+title then publicationDate (order preserved)
_SLUG_TITLE_RE = re.compile(
    r'\\"slug\\":\\"index/([a-z0-9-]+)\\",\\"title\\":\\"((?:\\.|[^"\\])*?)\\"'
)
_DATE_RE = re.compile(r'\\"publicationDate\\":\\"([0-9T:+-]+)\\"')

# Noise patterns in article RSC payloads (cookie banner, nav, templates, image hashes, meta desc repeats)
_NOISE_RE = re.compile(
    r'Cookie|标识符|网站的运行|客户支持|OpenAI 相关话题|ChatGPT 了解|帮助中心|服务条款|'
    r'订阅|登录|注册|Hans-CN|zh-CN|zh-Hans|相关主题|newsletter|菜单|导航|'
    r'\{step\}|你似乎|超出我们的帮助范围|高级搜索|个性化展示|营销活动|同意选项|第三方平台|'
    r'/[a-f0-9]{16,}|SEO_Card|card__|hero-|Hero_|poster\.|\.png|\.jpg|\.webp|particle spiral|'
    r'[A-Za-z0-9]{14,}/[A-Za-z0-9._-]{10,}|'
    r'image\\?/|cdn\.openai|openai\.com/[a-z-]+/images/|'
    r'Twitter|LinkedIn|Reddit|YouTube|复制链接|分享此|'
    r'Static fallback image|^第 \{|^\{\{|'
    r'^C\d+\.\d+[^A-Za-z]{0,200}$|^[\d. ]{10,}$',
    re.I,
)
# Body paragraph: sentence-ending long-ish text (zh or en), no quotes/angles
_PARA_RE = re.compile(r'([A-Z\u4e00-\u9fff][^"<>\\]{50,900}?[。！？.!?]["»]?)')


def _rsc_scripts(html):
    return "".join(_RSC_SCRIPT_RE.findall(html))


def _unescape(payload):
    """Unescape one layer of JS-string escaping from __next_f payload."""
    s = payload.replace('\\"', '"').replace("\\n", "\n").replace("\\\\", "\\")
    s = re.sub(r"\\u\{([0-9a-fA-F]{4,6})\}", lambda m: chr(int(m.group(1), 16)), s)
    s = re.sub(r"\\u([0-9a-fA-F]{4})", lambda m: chr(int(m.group(1), 16)), s)
    return s


def _get(url, retries=3):
    last = None
    for i in range(retries):
        try:
            resp = requests.get(url, timeout=30, headers=_HEADERS)
            if resp.status_code == 200:
                return resp.text
            last = f"HTTP {resp.status_code}"
        except Exception as e:  # noqa: BLE001
            last = f"{type(e).__name__}: {e}"
        if i < retries - 1:
            import time
            time.sleep(4)
    print(f"  [ERROR] Failed to fetch {url}: {last}", file=sys.stderr)
    return None


def _parse_listing(html):
    """Parse the research index RSC payload into article dicts."""
    payload = _rsc_scripts(html)
    if not payload:
        return []
    articles = []
    for m in _SLUG_TITLE_RE.finditer(payload):
        slug = m.group(1)
        title = m.group(2).replace('\\"', '"').replace("\\\\", "\\")
        dm = _DATE_RE.search(payload, m.end())
        date_str = dm.group(1)[:10] if dm else ""
        articles.append({
            "slug": slug,
            "title": title,
            "date_str": date_str,
            "url": f"https://openai.com/zh-Hans-CN/index/{slug}/",
        })
    # De-dupe by slug
    seen = set()
    uniq = []
    for a in articles:
        if a["slug"] not in seen:
            seen.add(a["slug"])
            uniq.append(a)
    return uniq


def _extract_body(html, title):
    """Extract article body paragraphs from detail-page RSC payload."""
    payload = _rsc_scripts(html)
    if not payload:
        return ""
    s = _unescape(payload)
    paras = _PARA_RE.findall(s)
    # Clean + de-dupe
    seen = set()
    body = []
    for p in paras:
        p = p.strip()
        if len(p) < 30:
            continue
        if _NOISE_RE.search(p):
            continue
        # Skip exact title / meta-description repeats
        if p == title or p.startswith(title):
            continue
        if p in seen:
            continue
        seen.add(p)
        body.append(p)
    return "\n\n".join(body)


def fetch_from_listing_openai_research(lang_code="zh-cn", model=None, no_translate=False, max_articles=None):
    """Fetch OpenAI Research articles from the zh-Hans-CN index page."""
    src = SOURCES["openai-research"]
    url = src["listing_url"]
    print(f"Scraping OpenAI Research listing from {url} ...")

    html = _get(url)
    if not html:
        return 1
    articles = _parse_listing(html)
    print(f"Found {len(articles)} articles")
    if max_articles:
        articles = articles[:max_articles]

    post_dir = get_post_dir("openai-research")
    existing_slugs = set()
    for f in post_dir.glob("*.md"):
        if ".zh-cn" not in f.name and ".zh." not in f.name:
            existing_slugs.add(f.stem)

    saved = []
    translated = []

    for i, art in enumerate(articles):
        print(f"\n  [{i + 1}/{len(articles)}] {art['title']}")
        if not art["date_str"]:
            print("    [SKIP] No date found")
            continue
        slug = slugify(art["title"])
        if slug in existing_slugs:
            print("    [SKIP] Already saved")
            continue

        body_html = _get(art["url"])
        if not body_html:
            print("    [SKIP] Failed to fetch article")
            continue
        body = _extract_body(body_html, art["title"])
        if not body:
            print("    [SKIP] No body text extracted")
            continue

        pub_date = datetime.strptime(art["date_str"], "%Y-%m-%d")
        md = f"""# {art['title']}

**Date:** {pub_date.strftime('%Y-%m-%d %H:%M UTC')}
**Link:** {art['url']}

---

{body}
"""
        filepath = save_post(art["date_str"], md, art["title"], "openai-research")
        if filepath:
            saved.append(filepath)

    if not no_translate and saved:
        print(f"\nTranslating {len(saved)} new posts...")
        for fp in saved:
            zh = translate_post(fp, lang_code=lang_code, model=model)
            if zh:
                translated.append(zh)

    print(f"\nDone: {len(saved)} saved, {len(translated)} translated")
    return 0
