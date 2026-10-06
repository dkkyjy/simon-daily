# 软弃用 re.match()

         **日期：** 2026-09-11 14:47 UTC
         **链接：** https://simonwillison.net/2026/Sep/11/soft-deprecating-re-match/
         **标签：** python, regular-expressions

         ---

         > *摘要：软弃用 re.match()
Python 有一个"软弃用"的概念，即将 API 标记为"不应再用于编写新代码"，但不承诺也不威胁在未来将其移除。
Pyt*

2026年9月11日 - 链接博客

**[软弃用 re.match()](https://hugovk.dev/blog/2026/soft-deprecating-re.match/)**（[来自](https://lobste.rs/s/u7dr96/soft_deprecating_re_match "Lobste.rs")）Python 有一个[软弃用](https://peps.python.org/pep-0387/#soft-deprecation)的概念，即将 API 标记为"不应再用于编写新代码"，但不承诺也不威胁在未来将其移除。

Python 3.15 版本经理 Hugo van Kemenade 描述了在即将到来的 3.15 版本中，这个历史悠久却令人深感困惑的 `re.match()` 函数终于迎来了软弃用。它现在有了一个更为清晰的替代名称 `re.prefixmatch()`——反映了它锚定在字符串开头而非结尾的特性。

大多数情况下，你可能更需要 `re.search()`（在字符串的任意位置匹配该模式）或 `re.fullmatch()`（匹配整个字符串）。

发布于 [2026年9月11日](/2026/Sep/11/) 下午 2:47
