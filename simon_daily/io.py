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
