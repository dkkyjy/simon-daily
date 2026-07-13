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
