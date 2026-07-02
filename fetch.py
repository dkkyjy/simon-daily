#!/usr/bin/env python3
"""Fetch latest entries from Simon Willison's blog and save as Markdown."""

import argparse
import html
import os
import sqlite3
import re
import sys
import textwrap
from datetime import datetime, timezone, timedelta

import feedparser


DB_PATH = os.path.expanduser("~/.simon_daily.db")
POSTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "posts")
FEED_URL = "https://simonwillison.net/atom/everything/"


def get_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS seen (id TEXT PRIMARY KEY, fetched_at TEXT)"
    )
    return conn


def slugify(text):
    s = text.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[-\s]+", "-", s)
    return s[:80].rstrip("-")


def strip_html(html_text):
    text = re.sub(r"<[^>]+>", " ", html_text)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def published_or_updated(entry):
    for key in ("published_parsed", "updated_parsed"):
        val = getattr(entry, key, None)
        if val:
            try:
                from time import mktime
                return datetime.fromtimestamp(mktime(val), tz=timezone.utc)
            except Exception:
                pass
    return datetime.now(timezone.utc)


def extract_content(entry):
    content_html = ""
    if hasattr(entry, "content") and entry.content:
        content_html = entry.content[0].get("value", "")
    elif hasattr(entry, "summary") and entry.summary:
        content_html = entry.summary
    return strip_html(content_html)


def make_markdown(entry, content):
    title = getattr(entry, "title", "Untitled")

    pub_date = published_or_updated(entry)
    date_str = pub_date.strftime("%Y-%m-%d")
    date_display = pub_date.strftime("%Y-%m-%d %H:%M UTC")
    link = getattr(entry, "link", "")

    tags = []
    if hasattr(entry, "tags"):
        for t in entry.tags:
            label = getattr(t, "label", None) or getattr(t, "term", None)
            if label:
                tags.append(label.strip())
    tag_line = ", ".join(tags) if tags else ""

    words = content.split()
    if len(words) > 300:
        content = " ".join(words[:300]) + "\n\n*(truncated, see original)*"

    md = textwrap.dedent(f"""\
        # {title}

        **Date:** {date_display}
        **Link:** {link}
        {"**Tags:** " + tag_line if tag_line else ""}

        ---

        {content}
    """).strip() + "\n"

    return date_str, md


def save_post(date_str, md, title):
    safe_title = slugify(title)
    filename = f"{date_str}-{safe_title}.md"
    filepath = os.path.join(POSTS_DIR, filename)

    if os.path.exists(filepath):
        return None

    os.makedirs(POSTS_DIR, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(md)
    return filename


def fetch(days=1):
    db = get_db()
    seen = set(
        row[0] for row in db.execute("SELECT id FROM seen").fetchall()
    )

    print(f"Fetching {FEED_URL} ...", file=sys.stderr)
    feed = feedparser.parse(FEED_URL)

    if feed.bozo and not feed.entries:
        print(f"Error: {feed.bozo_exception}", file=sys.stderr)
        return 1

    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    new_count = 0
    skip_count = 0
    saved = []

    for entry in feed.entries:
        entry_id = getattr(entry, "id", "") or getattr(entry, "link", "")
        pub_date = published_or_updated(entry)

        if pub_date < cutoff:
            break

        if entry_id in seen:
            skip_count += 1
            continue

        content = extract_content(entry)
        date_str, md = make_markdown(entry, content)
        title = getattr(entry, "title", "Untitled")
        filename = save_post(date_str, md, title)

        db.execute(
            "INSERT OR IGNORE INTO seen (id, fetched_at) VALUES (?, ?)",
            (entry_id, datetime.now(timezone.utc).isoformat()),
        )
        db.commit()
        new_count += 1

        if filename:
            saved.append(filename)
            print(f"  Saved: {filename}", file=sys.stderr)
        else:
            print(f"  Skipped (already saved): {title}", file=sys.stderr)

    print(
        f"\nDone: {new_count} new, {skip_count} already seen, "
        f"{len(saved)} saved to disk",
        file=sys.stderr,
    )

    for fname in saved:
        print(fname)

    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Fetch Simon Willison's latest blog posts"
    )
    parser.add_argument(
        "--days",
        type=int,
        default=1,
        help="How many days back to fetch (default: 1)",
    )
    args = parser.parse_args()
    sys.exit(fetch(days=args.days))


if __name__ == "__main__":
    main()