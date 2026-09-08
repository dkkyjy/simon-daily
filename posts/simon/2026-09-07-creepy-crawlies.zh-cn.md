# 毛骨悚然的爬虫

         **日期：** 2026-09-07 23:08 UTC
         **链接：** https://simonwillison.net/2026/Sep/7/creepy-crawlies/
         **标签：** crawling, git, linux, datasette, ai-ethics

         ---

         > *摘要：毛骨悚然的爬虫
康斯坦丁·里亚比采夫从 git.kernel.org（Linux 内核的官方 Git 仓库）的角度，讨论了恶意爬虫的"背景辐射"已经恶化到了何种程度*

2026年9月7日 - 链接博客

**[毛骨悚然的爬虫](https://people.kernel.org/monsieuricon/creepy-crawlies)**（[via](https://news.ycombinator.com/item?id=49491791 "Hacker News")）康斯坦丁·里亚比采夫从 [git.kernel.org](https://git.kernel.org/)（Linux 内核的官方 Git 仓库）的角度，讨论了恶意爬虫的"背景辐射"已经恶化到了何种程度：

> 长话短说：我们在为抓取器渲染提交上花费的 CPU 周期，比在所有其他类型的合法访问（包括 git 克隆）上花费的还要多。在任意时刻，跨 5 个地理分布式节点，有 14 个 CPU 核心在纯粹做一件事——将 git 提交渲染为 HTML。

从 Datasette 的角度来看，我非常担心这个问题，因为它提供了大量可爬取的网页。

发布于 [2026年9月7日](/2026/Sep/7/) 晚上 11:08

