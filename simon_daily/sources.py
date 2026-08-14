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
    "agricidaniel": {
        "name": "Agrici Daniel",
        "author": "Agrici Daniel",
        "feed_url": None,
        "dir": "agricidaniel",
        "feed_type": "listing",
        "home_url": "https://agricidaniel.com/",
        "listing_url": "https://agricidaniel.com/blog",
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
