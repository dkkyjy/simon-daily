# simon-daily 重构设计

## 概述

将 1262 行的 `sources.py` 单文件拆分为 `simon_daily/` Python 包，合并 6 个重复的 utility 脚本为 CLI 子命令，移除 server.py 中的内嵌 SPA，统一使用 React UI。

## 包结构

```
simon_daily/
  __init__.py         # re-export public API 保证向后兼容
  sources.py          # SOURCES 注册表（6 个源）、slugify、published_or_updated、get_post_dir
  content.py          # fetch_article_content() HTTP 抓取 + HTML→Markdown
  formatters.py       # format_post()、_format_atom_post()、_format_rss_post()
  io.py               # save_post()、list_posts()、get_post()、read_post_content()
  translate.py        # translate_post()、save_translation()、summarize_post()
  fetcher.py          # fetch()、fetch_from_listing() 编排器
  scrapers/
    __init__.py
    claude.py               # fetch_from_listing_claude()
    anthropic_research.py   # fetch_from_listing_anthropic_research()
    anthropic_engineering.py # fetch_from_listing_anthropic_engineering()
  cli.py              # python -m simon_daily {fetch, translate-remaining, summarize, ...}
  deploy.py           # daily_task 的部署逻辑（Astro 站点发布）
  server.py           # FastAPI（移除 HTML_TEMPLATE，serve React dist/）
```

## 模块职责

| 模块 | 职责 | 主要导出 |
|------|------|----------|
| `sources.py` | 6 个源的注册表、slugify、日期解析、目录路径 | `SOURCES`, `slugify`, `published_or_updated`, `get_post_dir` |
| `content.py` | HTTP 抓取 + BeautifulSoup + markdownify | `fetch_article_content(url)` |
| `formatters.py` | 把 feed entry 格式化为 Markdown | `format_post()`, `_format_atom_post()`, `_format_rss_post()` |
| `io.py` | 已保存文章的磁盘读写查询 | `save_post()`, `list_posts()`, `get_post()`, `read_post_content()` |
| `translate.py` | fabric-ai 翻译和摘要包装 | `translate_post()`, `save_translation()`, `summarize_post()` |
| `fetcher.py` | 抓取编排器（feed/listing 分发、去重、保存管道） | `fetch()`, `fetch_from_listing()` |
| `scrapers/` | 每个 listing 源的独立抓取器 | 各源的 listing 函数 |
| `cli.py` | CLI 子命令入口 | `main()` |
| `deploy.py` | 部署到个人 Astro 站点 | `deploy_zh_to_site()`, `daily_main()` |
| `server.py` | FastAPI 后端（移除内嵌 SPA，serve React dist） | app |

## 依赖关系（无循环）

```
sources.py ──► formatters.py ──► content.py
                  │
io.py ──► sources.py
translate.py ──► io.py
scrapers/* ──► content.py + sources.py
fetcher.py ──► formatters.py + io.py + translate.py + scrapers/*

cli.py ──► fetcher.py + translate.py + io.py
deploy.py ──► io.py
server.py ──► (通过 __init__.py 的 public API)
```

## CLI 子命令

6 个现有 utility 脚本合并为：

```
python -m simon_daily fetch [--source addy] [--days 3]
python -m simon_daily translate-remaining [--source claude]
python -m simon_daily summarize [--source claude]
python -m simon_daily fetch-all-anthropic
```

根目录的 `fetch.py` 保留为薄包装：
```python
from simon_daily.cli import main
main()
```
`daily_task.py` 同样保留为薄包装。

## Server 变更

- 删除 `HTML_TEMPLATE`（约 460 行内嵌 HTML/JS）
- 挂载 `ui/dist/` 为 FastAPI 静态文件目录
- `/api/*` 路由保持不变
- React 开发服务器依然通过 Vite proxy 访问 `:8080`

## 迁移步骤

1. 创建 `simon_daily/` 包目录和 `__init__.py`
2. `sources.py` → 拆分为：`sources.py`（精简）、`content.py`、`formatters.py`、`io.py`、`translate.py`、`fetcher.py`
3. 创建 `scrapers/` 子包，移入 3 个抓取器
4. 创建 `cli.py`，添加子命令
5. 创建 `deploy.py`，从 `daily_task.py` 提取逻辑
6. 清理 `server.py`：移除 `HTML_TEMPLATE`，挂载 React dist
7. 删除旧的 utility 脚本
8. 根目录的 `fetch.py` 和 `daily_task.py` 改为薄包装
9. 删除旧的 `sources.py`

## 不做的事

- 不改 post 文件格式或磁盘布局
- 不改 React UI 代码
- 不改 CI/CD
- 不加 pyproject.toml 或 pip 安装（可后续添加）
- 不加测试框架（可后续添加）
