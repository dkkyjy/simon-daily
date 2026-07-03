# Simon Willison Daily Reader

每天自动抓取 [Simon Willison's Weblog](https://simonwillison.net/) 的最新文章，保存为本地 Markdown 文件，并使用 [fabric](https://github.com/danielmiessler/fabric) 的 `translate` pattern 翻译成中文。

## 用法

```bash
# 安装依赖
pip install feedparser

# 获取最近 1 天的文章并翻译为中文
python fetch.py

# 获取最近 3 天的文章
python fetch.py --days 3

# 跳过翻译
python fetch.py --no-translate

# 指定其他目标语言（默认 zh-cn）
python fetch.py --lang ja-jp

# 指定 fabric 模型
python fetch.py --model gpt-4o
```

## 依赖

- Python 3 + `feedparser`
- [fabric-ai](https://github.com/danielmiessler/fabric)（用于翻译）需在 PATH 中可调用（`fabric-ai` 或 `fabric`）

## 输出

文章保存到 `posts/` 目录：

- 原文：`YYYY-MM-DD-slugified-title.md`
- 中文译文：`YYYY-MM-DD-slugified-title.zh-cn.md`

已抓取的文章 ID 记录在 `~/.simon_daily.db`（SQLite），避免重复处理。

## 自动运行

通过 GitHub Actions 每天北京时间 8:00 和 20:00 自动运行（UTC 0:00 和 12:00），只抓取原文，不执行翻译。详见 `.github/workflows/fetch.yml`。

翻译需在本地手动运行（需安装 fabric 并配置 LLM API key）：

```bash
# macOS 安装 fabric
brew install fabric-ai
fabric --setup  # 配置 API key 和默认模型

# 为所有尚未翻译的原文生成中文译文
python -c "
import fetch, os
for f in os.listdir('posts'):
    if f.endswith('.md') and not f.endswith('.zh-cn.md'):
        zh = f.replace('.md', '.zh-cn.md')
        if not os.path.exists(os.path.join('posts', zh)):
            fetch.save_translation(os.path.join('posts', f), lang_code='zh-cn')
"
```

## 配置项

| 参数 | 默认 | 说明 |
|------|------|------|
| `--days N` | `1` | 抓取最近 N 天的文章 |
| `--lang CODE` | `zh-cn` | fabric translate 的目标语言 |
| `--model NAME` | fabric 默认 | fabric 翻译使用的模型 |
| `--no-translate` | - | 跳过翻译步骤 |
