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
