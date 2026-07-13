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
