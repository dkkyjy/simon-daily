# Simon Willison Daily Reader

多源博客抓取器，支持 [Simon Willison's Weblog](https://simonwillison.net/)、[Addy Osmani](https://addyosmani.com/blog/)、[Claude Blog](https://claude.com/blog/)、[Anthropic Research](https://www.anthropic.com/research)、[Anthropic Engineering](https://www.anthropic.com/engineering) 和 [Simon Willison's Guides](https://simonwillison.net/guides/)。

抓取文章保存为本地 Markdown，并使用 [fabric-ai](https://github.com/danielmiessler/fabric) 的 `translate` / `summarize` pattern 翻译成中文或生成摘要。提供 FastAPI 后端和 React 前端。

## 安装

```bash
pip install feedparser requests beautifulsoup4 markdownify fastapi uvicorn
```

翻译和摘要功能需要 [fabric-ai](https://github.com/danielmiessler/fabric) 在 PATH 中可用。

## 用法

### 抓取文章

```bash
python fetch.py                                          # 默认抓取 Simon Willison 最近 1 天
python fetch.py --source addy --days 3
python fetch.py --source anthropic-research --no-translate
python fetch.py --source claude
python fetch.py --source anthropic-engineering
python fetch.py --source simon_guides
python fetch.py --lang ja-jp --model gpt-4o              # 指定翻译目标语言和模型
```

### CLI 子命令

```bash
python fetch.py summarize --source claude                # 生成 AI 摘要
python fetch.py translate-remaining                      # 翻译所有未翻译的文章
python fetch.py fetch-all-anthropic                      # 批量抓取所有 Anthropic Research 文章
```

### Web UI

```bash
python server.py                    # FastAPI 后端 http://127.0.0.1:8080
cd ui && npm run dev                # React 开发服务器 :5173（代理 /api 到 :8080）
cd ui && npm run build              # 生产构建 → ui/dist/
```

### 每日任务

```bash
python daily_task.py                # 抓取所有来源 + 部署中文版到个人网站
python daily_task.py --days 3 --dry-run
```

### 在 Python 中使用

```python
from simon_daily import SOURCES, fetch, list_posts, translate_post

print(SOURCES.keys())                        # ['simon', 'addy', 'claude', ...]
fetch(source_key="simon", days=1)            # 抓取并翻译
posts = list_posts(source_key="addy")        # 列出已保存文章
translate_post(posts[0]["orig_file"])        # 翻译单篇文章
```

## 数据源

| Key | 名称 | 方式 |
|-----|------|------|
| `simon` | Simon Willison | Atom Feed |
| `addy` | Addy Osmani | RSS + 全文抓取 |
| `claude` | Claude Blog | 列表抓取（分页） |
| `anthropic-research` | Anthropic Research | 列表抓取（单页） |
| `anthropic-engineering` | Anthropic Engineering | 列表抓取（单页） |
| `simon_guides` | Simon Willison Guides | 列表抓取（单页） |

无 RSS 的源（`feed_url: None`）调用 `fetch()` 时会自动切换到列表抓取模式。所有文章以 Markdown 格式保存到 `posts/<source-dir>/`：

- 原文：`YYYY-MM-DD-slugified-title.md`
- 中文译文：`YYYY-MM-DD-slugified-title.zh-cn.md`
- AI 摘要：`YYYY-MM-DD-slugified-title.summary.md`

去重基于文件名，已抓取的文章会自动跳过。

## 项目结构

```
simon_daily/                          # 核心包
├── sources.py                        # SOURCES 注册表、BASE_DIR、slugify
├── content.py                        # HTML→Markdown 转换
├── formatters.py                     # 文章格式化（Atom/RSS）
├── io.py                             # 文件读写、文章列表
├── translate.py                      # fabric-ai 翻译和摘要封装
├── fetcher.py                        # 抓取编排（feed + listing 分发）
├── cli.py                            # 命令行子命令
├── deploy.py                         # 部署流水线
└── scrapers/                         # 特定来源的 listing 抓取器
    ├── claude.py
    ├── anthropic_research.py
    └── anthropic_engineering.py

ui/                                   # React/TypeScript 前端（Vite）
fetch.py                              # 入口：委托 cli.main()
daily_task.py                         # 入口：委托 deploy.daily_main()
server.py                             # FastAPI 应用
```

## API 端点

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/api/sources` | 可用来源列表 |
| GET | `/api/posts[?source=&search=]` | 文章列表（支持搜索和筛选） |
| GET | `/api/posts/{slug}?lang=` | 文章内容（原文/中文） |
| POST | `/api/fetch/{source_key}?days=N` | 触发抓取（后台线程） |
| POST | `/api/translate/{slug}` | 翻译一篇文章 |
| GET/POST | `/api/posts/{slug}/summary` | 查看/生成摘要 |

## GitHub Actions

`.github/workflows/fetch.yml` 每天 UTC 0:00/12:00 自动抓取 Simon Willison 的最新文章（仅原文，不翻译）。
