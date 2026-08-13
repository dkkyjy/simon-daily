"""同步 simon-daily 新增文章到个人网站 ac-site blog.

覆盖 deploy.py 未包含的 simon 本人源 + engineering 源新增文章。
- 排除 anthropic-research（论文，已从 ac-site 清理）
- 用 originalLink + 文件名双去重
- 输出格式与 deploy.py 一致（frontmatter 模板）

用法: python simon_daily/sync_simon_to_site.py [--dry-run]
"""
import argparse
import os
import re
import sys
from pathlib import Path

SIMON_DAILY_DIR = Path(__file__).resolve().parent.parent
SITE_BLOG = Path.home() / "storage/github/ac-site-template/src/content/blog"

SOURCES = {
    # 官方工程文章
    "anthropic-engineering": {"tag": "anthropic-engineering", "dir": "posts/anthropic-engineering"},
    # Simon Willison 本人博客
    "simon": {"tag": "simon-willison", "dir": "posts/simon"},
}


def norm_link(s: str) -> str:
    return s.strip().rstrip("*").split("#")[0].rstrip("/")


def get_site_links() -> set:
    links = set()
    if not SITE_BLOG.exists():
        return links
    for f in os.listdir(SITE_BLOG):
        if not f.endswith(".md"):
            continue
        txt = (SITE_BLOG / f).read_text(encoding="utf-8")
        m = re.search(r'originalLink:\s*["\']([^"\']*)["\']', txt)
        if m:
            links.add(norm_link(m.group(1)))
    return links


def parse_zh(filepath: Path):
    """解析 simon-daily 中文翻译文件 -> dict(title/pub_date/link/body) 或 None"""
    content = filepath.read_text(encoding="utf-8")
    title_m = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    if not title_m:
        return None
    title = title_m.group(1).strip()
    date_m = re.search(r"\*\*日期[：:]\s*\*\*\s*(\d{4}-\d{2}-\d{2})", content)
    pub_date = date_m.group(1) if date_m else None
    link_m = re.search(r"\*\*链接[：:]\s*\*\*\s*(https?://\S+)", content)
    orig_link = norm_link(link_m.group(1)) if link_m else None
    lines = content.split("\n")
    start = 0
    for i, ln in enumerate(lines):
        if ln.startswith("# "):
            start = i + 1
            break
    sep = None
    for i in range(start, len(lines)):
        if lines[i].strip() == "---":
            sep = i
            break
    body_lines = lines[sep + 1:] if sep is not None else lines[start:]
    body = re.sub(r"\n{4,}", "\n\n\n", "\n".join(body_lines).strip())
    return {"title": title, "pub_date": pub_date, "link": orig_link, "body": body}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="只打印将写入的文件，不实际写入")
    args = ap.parse_args()

    site_links = get_site_links()
    todo = []
    for src, cfg in SOURCES.items():
        d = SIMON_DAILY_DIR / cfg["dir"]
        if not d.exists():
            print(f"[SKIP] {src} dir not found")
            continue
        for f in sorted(os.listdir(d)):
            if not f.endswith(".zh-cn.md"):
                continue
            slug = f[: -len(".zh-cn.md")]
            target = SITE_BLOG / f"{slug}.md"
            if target.exists():
                continue
            p = parse_zh(d / f)
            if not p:
                print(f"[WARN] 解析失败: {f}")
                continue
            if p["link"] in site_links:
                continue
            if not p["pub_date"]:
                p["pub_date"] = slug[:10]
            todo.append({"src": src, "tag": cfg["tag"], "slug": slug, **p})

    print(f"待同步: {len(todo)} 篇")
    if not todo:
        print("无新增，完成。")
        return 0
    from collections import Counter

    print(dict(Counter(t["src"] for t in todo)))
    for t in todo:
        print(f"  + {t['src']}: {t['slug']}")
    if args.dry_run:
        print("[DRY-RUN] 未写入")
        return 0
    written = 0
    for t in todo:
        title = t["title"].replace('"', "'")
        frontmatter = (
            f"---\n"
            f'title: "{title}"\n'
            f'description: "{title}"\n'
            f'pubDate: "{t["pub_date"]}"\n'
            f'heroImage: "/post_img.png"\n'
            f'tags: ["{t["tag"]}"]\n'
            f'originalLink: "{t["link"]}"\n'
            f"---\n\n"
            f"{t['body']}\n"
        )
        (SITE_BLOG / f"{t['slug']}.md").write_text(frontmatter, encoding="utf-8")
        written += 1
    print(f"写入完成: {written} 篇")
    return 0


if __name__ == "__main__":
    sys.exit(main())
