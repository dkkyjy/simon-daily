#!/usr/bin/env python3
"""simon-daily Web UI - FastAPI 后端（多源）"""

import os
import sys
import threading
from pathlib import Path

from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

from simon_daily import (
    SOURCES, list_posts, read_post_content, save_translation, fetch, get_post_dir,
    summarize_post,
)

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="Simon Willison Daily Reader")


# -- API 路由 ----------------------------------------

@app.get("/api/sources")
def api_sources():
    """Return available blog sources."""
    return [
        {"key": k, "name": v["name"], "home_url": v["home_url"]}
        for k, v in SOURCES.items()
    ]


@app.get("/api/posts")
def api_list_posts(
    search: str = Query(""),
    source: str = Query(""),
):
    posts = list_posts(source_key=source if source else None, search=search)
    return posts


@app.get("/api/posts/{slug}/bilingual")
def api_get_post_bilingual(slug: str):
    """Get post content in both original and Chinese side by side."""
    from simon_daily import list_posts, read_post_content
    posts = list_posts()
    match = [p for p in posts if p["slug"] == slug]
    if not match:
        return JSONResponse({"error": "not found"}, status_code=404)
    post = match[0]

    orig_content = read_post_content(post["orig_file"])
    zh_content = read_post_content(post["zh_file"]) if post["zh_file"] else None

    return {
        "slug": post["slug"],
        "title": orig_content["title"],
        "orig": orig_content["content"],
        "zh": zh_content["content"] if zh_content else None,
        "source": post["source"],
        "source_name": post["source_name"],
        "has_translation": post["has_translation"],
    }


@app.get("/api/posts/{slug}")
def api_get_post(slug: str, lang: str = Query("orig")):
    """Get post content by slug."""
    posts = list_posts()
    match = [p for p in posts if p["slug"] == slug]
    if not match:
        return JSONResponse({"error": "not found"}, status_code=404)
    post = match[0]

    if lang == "zh" and post["zh_file"]:
        content = read_post_content(post["zh_file"])
    else:
        content = read_post_content(post["orig_file"])

    return {
        "slug": post["slug"],
        "title": content["title"],
        "content": content["content"],
        "source": post["source"],
        "source_name": post["source_name"],
        "has_translation": post["has_translation"],
    }


@app.post("/api/fetch/{source_key}")
def api_fetch(source_key: str, days: int = Query(1)):
    """Fetch posts from a blog source."""
    if source_key not in SOURCES:
        return JSONResponse({"error": f"Unknown source: {source_key}"}, status_code=400)

    def _run():
        print(f"[background] Fetching {source_key} days={days}", file=sys.stderr)
        fetch(source_key=source_key, days=days, no_translate=False)

    thread = threading.Thread(target=_run, daemon=True)
    thread.start()
    return JSONResponse({
        "status": "started",
        "message": f"正在抓取 {SOURCES[source_key]['name']} 最近 {days} 天的文章并翻译...",
    })


@app.post("/api/translate/{slug}")
def api_translate(slug: str):
    """Translate a single post."""
    posts = list_posts()
    match = [p for p in posts if p["slug"] == slug]
    if not match:
        return JSONResponse({"error": "not found"}, status_code=404)
    post = match[0]

    if post["has_translation"]:
        return JSONResponse({"status": "done", "message": "已翻译"})

    src_path = Path(post["orig_file"])

    def _run():
        try:
            save_translation(src_path, lang_code="zh-cn")
        except Exception as e:
            print(f"Translate error: {e}", file=sys.stderr)

    thread = threading.Thread(target=_run, daemon=True)
    thread.start()
    return JSONResponse({
        "status": "started",
        "message": f"正在翻译: {post['title']}",
    })


@app.post("/api/posts/{slug}/summary")
def api_summarize_post(slug: str):
    """Generate or retrieve cached summary for a post."""
    posts = list_posts()
    match = [p for p in posts if p["slug"] == slug]
    if not match:
        return JSONResponse({"error": "not found"}, status_code=404)
    post = match[0]

    filepath = post["orig_file"]
    result = summarize_post(filepath)

    if result is None:
        return JSONResponse({
            "error": "summary_failed",
            "message": "生成摘要失败，请稍后重试",
        }, status_code=500)

    return JSONResponse({
        "slug": slug,
        "summary": result["summary"],
        "cached": result["cached"],
    })


@app.get("/api/posts/{slug}/summary")
def api_get_summary(slug: str):
    """Get cached summary if available."""
    posts = list_posts()
    match = [p for p in posts if p["slug"] == slug]
    if not match:
        return JSONResponse({"error": "not found"}, status_code=404)
    post = match[0]
    summary_file = Path(post["orig_file"]).with_suffix(".summary.md")
    if summary_file.exists():
        content = summary_file.read_text(encoding="utf-8")
        return JSONResponse({
            "slug": slug,
            "summary": content,
            "cached": True,
        })
    return JSONResponse({
        "slug": slug,
        "summary": None,
        "cached": False,
    })


# -- Static files (React SPA) -----------------------
UI_DIST = BASE_DIR / "ui/dist"
if UI_DIST.exists():
    app.mount("/", StaticFiles(directory=str(UI_DIST), html=True), name="ui")


# -- 启动 -------------------------------------------
if __name__ == "__main__":
    port = int(sys.argv[1])
    print(f"simon-daily UI: http://127.0.0.1:{port}")
    uvicorn.run(app, host="127.0.0.1", port=port)
