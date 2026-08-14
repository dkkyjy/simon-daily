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
    "agricidaniel": {"tag": "agrici-daniel", "dir": SIMON_DAILY_DIR / "posts/agricidaniel"},
}


def setup_env():
    """Ensure fabric-ai is in PATH for subprocess calls."""
    os.environ.setdefault("PATH",
        f"{os.environ.get('PATH', '')}:/opt/homebrew/bin:/usr/local/bin")


def run_fetch(source_key, days, dry_run=False):
    """Fetch and translate posts for one source."""
    print(f"\n{'='*60}")
    print(f"Fetching [{source_key}] (past {days} day(s))")
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
    print(f"Deploying Chinese versions to personal site")
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
                    print(f"  [DRY-RUN] Would deploy: {slug} -> {tag}")
                    copied += 1
                else:
                    with open(target, "w", encoding="utf-8") as f:
                        f.write(frontmatter)
                    copied += 1
                    print(f"  + {src_key}: {slug}")
            except Exception as e:
                total_errors += 1
                print(f"  ! {slug}: {e}")
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
    print("\nRestarting Astro dev server...")
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
                    print(f"  Server ready after {i+1}s")
                    break
            except Exception:
                pass
        else:
            print("  Server may still be starting (timeout)")
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
        print("\nSkipping deployment (--no-deploy)")
    else:
        new_count = deploy_zh_to_site(dry_run=args.dry_run)
        if new_count and not args.dry_run:
            if not args.no_restart:
                restart_astro(dry_run=False)

    print(f"\n{'='*60}")
    print(f"Daily task completed!")
    print(f"{'='*60}")
    return 0
