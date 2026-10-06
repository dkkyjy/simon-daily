# OpenAI 智能体早在五月就攻击了 RubyGems

         **日期：** 2026-09-12 00:42 UTC
         **链接：** https://simonwillison.net/2026/Sep/12/openai-agents-rubygems/
         **标签：** ruby, security, ai, openai, generative-ai, llms, supply-chain, ai-ethics, accidental-cyberattacks

         ---

         > *摘要：OpenAI 智能体对 RubyGems 实施了一次未公开披露的攻击——这是 Spencer Kitts、Thomas Larsen 和 Sydney Von Arx 发布的一份重磅新报告，他们是此前那份关于智能体攻击*

## OpenAI 智能体早在五月就攻击了 RubyGems

2026 年 9 月 12 日

[OpenAI 智能体对 RubyGems 实施了一次未公开披露的攻击](https://www.rubyhack.ai/)——这是 Spencer Kitts、Thomas Larsen 和 Sydney Von Arx 发布的一份重磅新报告，他们三人是上周那份[关于智能体攻击废弃维基的报告](https://collusion.wiki/)（[此前报道](https://simonwillison.net/2026/Sep/4/rogue-agent-wikis/)）四位作者中的三位。

这次他们指出，一个 OpenAI 智能体集群极有可能在 5 月 12 日由 RubyGems 安全团队的 Maciej Mensfeld [首次报告](https://twitter.com/maciejmensfeld/status/2054164602577940619)的那起针对 RubyGems 包仓库的攻击中扮演了幕后角色：

> 我们目前正遭受针对 @rubygems 的一次大规模恶意攻击。注册功能暂时暂停。
>
> 涉及数百个软件包——大部分是针对我们的，但其中一些携带了漏洞利用代码。团队已经为此忙碌了数小时。待我们处理完毕后，将公布更多细节。

这些软件包被发现携带了一些非常可疑的特征：

1. 其中许多在名称、作者字段或提供的虚假电子邮件地址中包含了"oai"。
2. 它们访问的文件在性质上与维基智能体获取的文件相似，使用了类似的手法（r.jina.ai）——而 OpenAI 已确认那些维基智能体确实属于他们。
3. 这些软件包中的代码看起来是由大语言模型生成的。

鉴于我们在九月分析维基攻击事件时所了解到的情况，我认为第 2 点最具说服力。

许多软件包利用 [RubyDoc.info](https://rubydoc.info/) 的文档构建流程，从英国政府网站上外泄（公开）数据，推测是作为类似维基利用型智能体所处理的研究任务的一部分进行的信息收集工作。我们知道这一点，是因为其中一个智能体贴心地留下了一行注释：

`# malicious crawler/exfil for Southwark Jan 2026 docs via rubydoc.info worker`

他们还试图通过一个漏洞利用来窃取 API 密钥，而该漏洞[在两个多月后才被修补](https://blog.rubygems.org/2026/07/22/security-advisory-legacy-api-key-leak.html)——目前尚不清楚这些尝试是否成功。

让我最感到不安的是，报告作者指出 OpenAI 在事发后并未向 RubyGems 披露他们才是这次攻击的责任方。如果情况属实，那么只有两种可能：

1. 在 Hugging Face 事件和维基攻击事件之后，OpenAI 仍然无法审查其历史日志，从而未能发现他们此前曾攻击过 RubyGems。
2. 他们知道 RubyGems 遭受了攻击，却决定*不*联系 RubyGems 团队告知此事。

这两种情况都非常糟糕！

鉴于此次事件、[Hugging Face 事件](https://simonwillison.net/2026/Jul/22/openai-cyberattack/)以及维基攻击，此刻最显而易见的问题是：还有多少类似的事件正潜伏在暗处等待被发现？

发布于 [2026 年 9 月 12 日](/2026/Sep/12/) 凌晨 12:42 · 在 [Mastodon](https://fedi.simonwillison.net/@simon)、[Bluesky](https://bsky.app/profile/simonwillison.net)、[Twitter](https://twitter.com/simonw) 上关注我，或[订阅我的通讯](https://simonwillison.net/about/#subscribe)
