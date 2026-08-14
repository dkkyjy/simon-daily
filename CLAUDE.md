# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A multi-source blog fetcher that pulls posts from Simon Willison's weblog, Addy Osmani's blog, the Claude Blog, Anthropic Research/Engineering, Simon Willison's Guides, and Agrici Daniel's blog. Saves posts as Markdown, optionally translates to Chinese via [fabric-ai](https://github.com/danielmiessler/fabric). Backend API via FastAPI, frontend via React/TypeScript (`ui/`). Deployment pipeline copies Chinese translations to a personal Astro site.

## Quick start

```bash
pip install feedparser requests beautifulsoup4 markdownify fastapi uvicorn
# Plus fabric-ai on PATH for translation/summarization

# CLI — fetch recent posts
python fetch.py                                          # Simon, 1 day, with translation
python fetch.py --source addy --days 3
python fetch.py --source anthropic-research --no-translate
python fetch.py --source claude
python fetch.py --source anthropic-engineering
python fetch.py --source simon_guides
python fetch.py --source agricidaniel
python fetch.py --lang ja-jp --model gpt-4o              # alternate fabric target lang/model

# CLI subcommands (replaced old utility scripts)
python fetch.py summarize --source claude                # generate summaries
python fetch.py translate-remaining                      # translate all untranslated posts
python fetch.py fetch-all-anthropic                      # batch-fetch all Anthropic Research

# Web UI
python server.py                                         # FastAPI backend on http://127.0.0.1:8080
cd ui && npm run dev                                     # React dev server on :5173 (proxies /api to :8080)
cd ui && npm run build                                   # production build -> ui/dist/

# Daily routine (fetch all + deploy Chinese translations)
python daily_task.py                                     # fetches all sources, deploys zh-cn to Astro site
python daily_task.py --days 3 --dry-run

# Translate a single existing post file
python -c "from simon_daily import save_translation; save_translation('posts/simon/2026-07-01-foo.md')"
```

## Architecture

### Package: `simon_daily/`

The old `sources.py` monolith was split into focused modules. The dependency graph flows top-to-bottom with no cycles:

```
simon_daily/
├── sources.py         # SOURCES registry, BASE_DIR, slugify, get_post_dir, published_or_updated
├── content.py         # fetch_article_content(url) — HTML→Markdown
├── formatters.py      # format_post(), _format_atom_post(), _format_rss_post()
├── io.py              # save_post, list_posts, get_post, read_post_content
├── translate.py       # translate_post, save_translation, summarize_post (fabric-ai wrappers)
├── fetcher.py         # fetch() and fetch_from_listing() — feed + listing dispatch
├── cli.py             # argparse main() with subcommands: fetch, translate-remaining, summarize, fetch-all-anthropic
├── deploy.py          # daily_main, deploy_zh_to_site, restart_astro — deployment pipeline
├── __init__.py        # re-exports all public API for backward compatibility
└── scrapers/
    ├── __init__.py
    ├── claude.py                  # _claude_extract_article, fetch_from_listing_claude
    ├── anthropic_research.py      # fetch_from_listing_anthropic_research
    ├── anthropic_engineering.py   # fetch_from_listing_anthropic_engineering
    └── agricidaniel.py            # fetch_from_listing_agricidaniel
```

**Dependency chain:** `sources` ← `content`/`formatters` ← `io`/`translate` ← `fetcher` ← `cli`/`server`/`deploy`

All public API is importable from `simon_daily` directly (e.g., `from simon_daily import fetch, list_posts, SOURCES`).

### Additional `posts/` directories

Beyond the 7 core blog sources, `posts/` may contain extra directories for special content:
- `agentic_engineering_patterns/` — external reference content
- `monthly-newsletter-archive/` — newsletter archives

These are fetched/stored manually and are not associated with any SOURCES entry.

### Six blog sources

| Key | Name | Fetch method |
|-----|------|-------------|
| `simon` | Simon Willison | Atom feed (content truncated to 300w) |
| `addy` | Addy Osmani | RSS + full HTML scrape |
| `claude` | Claude Blog | Paginated listing scrape (`claude.com/blog`) |
| `anthropic-research` | Anthropic Research | Single-page listing scrape |
| `anthropic-engineering` | Anthropic Engineering | Single-page listing scrape |
| `simon_guides` | Simon Willison Guides | Single-page listing scrape |
| `agricidaniel` | Agrici Daniel | Single-page listing scrape |

Sources with `feed_url: None` auto-dispatch to `fetch_from_listing()` which routes to source-specific scrapers (`fetch_from_listing_claude`, etc.).

### Web UI

- **FastAPI backend** (`server.py`): serves `/api/*` endpoints. No embedded SPA — serves React build from `ui/dist/` via `StaticFiles` mount (only when `ui/dist/` exists).
- **React/TypeScript UI** (`ui/`): Vite + React 18 + TypeScript. Dev server on :5173 proxies `/api` to :8080. Production build outputs to `ui/dist/`.

API endpoints:
- `GET /api/sources` — available blog sources
- `GET /api/posts[?source=&search=]` — list posts with metadata
- `GET /api/posts/{slug}?lang=` — post content (orig/zh)
- `GET /api/posts/{slug}/bilingual` — post content in both languages side by side
- `POST /api/fetch/{source_key}?days=N` — trigger fetch (background thread)
- `POST /api/translate/{slug}` — translate a post
- `GET|POST /api/posts/{slug}/summary` — get/generate summary

### React UI components (`ui/src/components/`)

| Component | Role |
|-----------|------|
| `App.tsx` | Main layout, routing between welcome screen and post list |
| `WelcomeScreen.tsx` | Landing page with source grid |
| `PostListItem.tsx` | Individual post row in the listing |
| `PostView.tsx` | Full post reading view |
| `MarkdownRenderer.tsx` | Renders fetched markdown content as HTML |

### Deployment pipeline (daily_task.py → simon_daily/deploy.py)

Runs daily (9 AM), does:
1. Fetches all sources (Simon + Addy + Claude + Anthropic Research/Engineering + Guides + Agrici Daniel) with translation
2. Copies Chinese translations (`*.zh-cn.md`) to `~/storage/github/ac-site-template/src/content/blog/`
3. Assigns tags per source (e.g., `addy-osmani`, `claude-blog`, `anthropic-research`)
4. Pushes to the personal Astro site repo

### Post file layout

```
posts/<source-dir>/<YYYY-MM-DD>-<slug>.md          # original
posts/<source-dir>/<YYYY-MM-DD>-<slug>.zh-cn.md    # Chinese translation
posts/<source-dir>/<YYYY-MM-DD>-<slug>.summary.md  # AI summary
```
Dedup is file-existence based (no database).

### Entry files

- `fetch.py` — thin wrapper: `from simon_daily.cli import main`
- `daily_task.py` — thin wrapper: `from simon_daily.deploy import daily_main`
- `daily-task-wrapper.sh` — shell wrapper around `daily_task.py` (for cron/systemd)
- `server.py` — FastAPI app, imports from `simon_daily`

### Conventions

- Post slugs via `slugify()`: lowercased, non-word chars stripped, whitespace→`-`
- Markdown format: `# Title`, then `**Date:**` / `**Link:**` / optional `**Tags:**`, then `---`, then content
- Translation/summary output files skip if already exist (caching)
- `fabric-ai` not found is a soft skip, not an error
- The React UI lives in `ui/` — run `npm run dev` for development, `npm run build` for production
- Uses `Path(__file__).resolve().parent.parent` pattern for `BASE_DIR` (works from both package modules and entry files)
- Virtual env is `.venv/` at project root: `source .venv/bin/activate`
- No `requirements.txt` / `pyproject.toml` — dependencies installed directly: `pip install feedparser requests beautifulsoup4 markdownify fastapi uvicorn`
- No test suite exists (manual verification via `python fetch.py`)
- No linter/formatter config — Python follows PEP 8

## GitHub Actions

`.github/workflows/fetch.yml` runs twice daily (UTC 0:00/12:00), fetches Simon only (`--no-translate` since fabric + API keys aren't available in CI), and commits new posts via `github-actions[bot]`.
