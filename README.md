# Simon Willison Daily Reader

每天自动抓取 [Simon Willison's Weblog](https://simonwillison.net/) 的最新文章，保存为本地 Markdown 文件。

## 用法

```bash
# 获取最近 1 天的文章
python fetch.py

# 获取最近 3 天的文章
python fetch.py --days 3
```

## 输出

文章保存到 `posts/` 目录，格式为 `YYYY-MM-DD-slugified-title.md`。

已抓取的文章 ID 记录在 `~/.simon_daily.db`（SQLite），避免重复。

## 自动运行

当前通过 crontab 每天 8:00 和 20:00 执行：

```
0 8,20 * * * cd /path/to/simon-daily && python fetch.py >> fetch.log 2>&1
```