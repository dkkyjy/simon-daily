# 统计 Safari 标签页数量

        **日期:** ...
        **链接:** https://simonwillison.net/2026/Jun/29/safari-tab-count/
        **标签:** safari, til, applescript

        ---

2026 年 6 月 29 日

最微小的 TIL，使用 AppleScript 统计 Safari 浏览器中打开的标签页数量：

```
osascript -e 'tell application "Safari" to count tabs of every window'
```

发布于 [2026 年 6 月 29 日](/2026/Jun/29/) 下午 6:36
