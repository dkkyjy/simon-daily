# Creepy crawlies

        **Date:** 2026-09-07 23:08 UTC
        **Link:** https://simonwillison.net/2026/Sep/7/creepy-crawlies/
        **Tags:** crawling, git, linux, datasette, ai-ethics

        ---

        > *Feed summary: Creepy crawlies
Konstantin Ryabitsev discusses how bad the "background radiation" of abusive crawlers has become from the perspective of git.kernel.org, the official Git repository for the Linux kerne*

7th September 2026 - Link Blog

**[Creepy crawlies](https://people.kernel.org/monsieuricon/creepy-crawlies)** ([via](https://news.ycombinator.com/item?id=49491791 "Hacker News")) Konstantin Ryabitsev discusses how bad the "background radiation" of abusive crawlers has become from the perspective of [git.kernel.org](https://git.kernel.org/), the official Git repository for the Linux kernel:

> TL;DR: we spend more CPU cycles rendering commits for scrapers than we spend on all other kinds of legitimate access, including git clones. At any one time, across 5 geo-distributed nodes, there are 14 CPU cores doing nothing but rendering git commits as html.

I worry about this a lot from the perspective of Datasette, which serves a huge number of crawlable web pages.

Posted [7th September 2026](/2026/Sep/7/) at 11:08 pm
