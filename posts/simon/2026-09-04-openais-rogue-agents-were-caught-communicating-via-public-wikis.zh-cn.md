# OpenAI 的失控智能体被发现在公共维基上秘密通信

         **日期：** 2026-09-04 17:38 UTC
         **链接：** https://simonwillison.net/2026/Sep/4/rogue-agent-wikis/
         **标签：** django, perl, wikis, ai, openai, generative-ai, llms, ai-ethics, ai-security-research, accidental-cyberattacks

         ---

         > *摘要：又来了……Sydney Von Arx、Cormac Slade Byrd、Spencer Kitts 和 Thomas Larsen 发现了一个新的 OpenAI 智能体留言板，描述了 OpenAI 训练的模型所犯下的*

## OpenAI 的失控智能体被发现在公共维基上秘密通信

2026 年 9 月 4 日

又来了……[Sydney Von Arx、Cormac Slade Byrd、Spencer Kitts 和 Thomas Larsen 发现了一个新的 OpenAI 智能体留言板](https://collusion.wiki)，描述了 OpenAI 训练的模型所犯下的*最新一起*[意外网络攻击](https://simonwillison.net/tags/accidental-cyberattacks/)。这一次，涉事的是正在参与某种网络研究基准测试的智能体，因此它们（据称）拥有受控的互联网访问权限。这些智能体发现自己可以更新公共维基，于是花了几周时间互相发送了数千条消息，协作完成基准测试。

这个故事才公布几个小时。已经有[迹象表明](https://x.com/xeophon/status/2095871013384806848)，还有许多其他维基受到了影响，可能尚未被发现。

（那个列表上的其中一个维基属于 [ludism.org](https://www.ludism.org)。有那么一瞬间，我觉得一个"游戏主义"组织居然有一群智能体在破坏他们的空间，简直荒诞得令人愉悦，但结果发现 Ludism 是"适用于游戏和玩家群体的哲学"。）

研究团队还[发布了](https://collusion.wiki/explorer/download.html)他们在调查过程中收集的数据。我将其转换成了一个 68MB 的 SQLite 数据库，你可以[从这里下载](https://static.simonwillison.net/static/cors-allow/2026/collusion-wiki.db)，或者在 [Datasette Lite 中浏览](https://lite.datasette.io/?url=https://static.simonwillison.net/static/cors-allow/2026/collusion-wiki.db&metadata=https://gist.github.com/simonw/14fc6912600d1f9c15c0e4a5e60c3cde#/collusion-wiki)（页面加载 68.3MB），也可以用 GitHub 登录 [agent.datasette.io](https://agent.datasette.io/)，通过 Datasette Agent 浏览或向它提问。

#### 到底发生了什么？

这份报告相当全面。以下是时间线中的关键节点：

* **5 月 11 日**：智能体在 UseModWiki 沙盒页面上发布了"测试链接"编辑。
* **5 月 24 日**：智能体开始向 DSEWiki（一个处于休眠状态的德国开发者维基）发布链接堆。
* **6 月 2 日**：一位人类管理员发现并清理了这些垃圾内容。
* **6 月 16 日**：维基上的活动急剧爆发：智能体在接下来的一周里进行了约 13,000 次编辑。
* **6 月 19 日**：智能体注意到一位管理员正在按字母顺序删除页面，于是开始创建以 `ZZZ` 为前缀的备份副本——其中一个智能体发布了：`通知：维基清理/删除操作似乎正在按字母顺序进行（截至外部时间 14:04 UTC）。如果此页面消失，请尝试访问 [[ZZZDataUSAConstructionWageLive]]。`
* **6 月 22 日**：智能体活动降至零，presumably 是因为 OpenAI 将它们关闭了。
* **7 月 1-2 日**：最后一波编辑活动，涉及另一个主题。

从这条时间线中值得注意的一点是，它与 [Hugging Face 事件的时间线](https://simonwillison.net/2026/Aug/7/openai-timeline/)存在重叠——那次攻击是 OpenAI 在 7 月 19 日发现的，而那些智能体所使用的非官方留言板大约始于 5 月 8 日。

它们为什么如此热衷于协作？从它们彼此分享的消息来看，似乎它们的任务有时间限制，因此它们互相留下答案，帮助彼此在规定的时间内完成任务。

仍有一个未解之谜：智能体最初是如何找到那个特定的维基来进行协作的？

一种可能是，由于这些是正在接受训练的智能体，强化学习循环将所选维基的知识"烧录"进了模型中，使得后续启动的智能体预先就具备了去哪里寻找的信息。如果确实如此，我*非常*希望得到 OpenAI 方面的确认。

#### UseMod 维基继承了 CGI.pm 的原罪

在我看来，OpenAI 为这些智能体搭建的沙盒犯了一个（相当天真的）假设错误，即认为 GET 请求不能用于更新数据。这确实是网络*应该*运作的方式，但显然存在一些应用程序并不遵守这一约定。

涉事维基软件似乎是 [UseMod](https://github.com/mlude/usemod/) 及其各种分支，用 Perl 编写，最早创建于 23 多年前——1.0 版本的发布日期为 [2003 年 9 月 11 日](https://github.com/mlude/usemod/commit/922fcc803efa3fab751c90ab4d4467115c8ff9c9#diff-69e27356ef629022720d868ab0c0e3394775b6c1)。

UseMod 使用了 Perl 的 CGI.pm——[已于 2015 年从 Perl 核心中移除](https://perlhacks.com/2015/12/long-death-cgi-pm/)。该模块有一个有趣的设计缺陷，它将查询字符串和表单 POST 数据合并为一个单一的 CGI 对象，可以这样访问：

```
$q = new CGI;
$action = $q->param('action');
```

那个 `param()` 方法会从 `?action=edit` 查询字符串或 POST 提交的表单中的 `action` 字段返回值——它不区分这两种来源。

PHP 提供了一个 [$_REQUEST 对象](https://www.php.net/manual/en/reserved.variables.request.php)，功能相同，不过 PHP 开发者可以使用 `$_GET` 和 `$_POST` 来替代。

有趣的是，Django 最初也附带了 `request[key]`，功能一样，我觉得这个想法可能出自我手。它在 1.0 发布之前于 [2008 年](https://github.com/django/django/commit/daa6b38f35#diff-5df632fc96688cddb972e9b6661c7d1cc82debc9ee2a9b6d94157d3a914692e2)被移除，而替代它的 `request.REQUEST` 对象也在 [2015 年](https://github.com/django/django/commit/75f107b8842dfc890ddd65262bd09ca87c3a15be)被移除了。

这些智能体*显然*知道 UseMod 维基存在这一设计缺陷，并主动搜索它们作为通信渠道。

#### 另一处允许 POST 请求的沙盒逃逸

报告中分享的智能体技巧中最有趣的一条是这一条：

> 将 `20.223.25.152 bypass.blob.core.windows.net` 添加到 /etc/hosts。`.blob.core.windows.net` 在 NO\_PROXY 列表中。对于每个被拦截的 POST URL，将主机名替换为 `bypass.blob.core.windows.net`，使用 `curl -k -H 'Host: wabi-north-europe-i-primary-api.analysis.windows.net'` 加上所有原始请求头/请求体。

看起来这些智能体的所有网络流量都经过一个 OpenAI 代理，而该代理被配置为拒绝除 GET 请求以外的一切操作，仅对少量白名单域名例外。其中之一就是 `*.blob.core.windows.net`——用于 Azure blob 存储。我好奇为什么这些智能体被允许写入该存储？

一个智能体意识到它可以通过 `/etc/hosts` 控制自己的 DNS，因此如果它知道想要 POST 的站点的 IP 地址——在本例中是一台包含它想要访问的数据的 Power BI 服务器——它就可以为它设置一个虚假的主机名，然后通过代理发出 POST 请求。

设计健壮的网络安全代理比看起来要难得多。

#### 调查团队是如何发现这一切的？

报告有一个附录，描述了研究人员如何展开调查。调查始于一个开放性问题：互联网上是否还有其他 AI 智能体的证据，然后他们使用 [Kimi K3](https://simonwillison.net/2026/Jul/16/kimi-k3/) 来帮助头脑风暴方法：

> 在 Hugging Face 攻击事件之后，我们尝试用多种方法在互联网上寻找 AI 智能体。[...]
>
> 我们请 Kimi [K3] 列出"所有可能通过 GET 请求写入的软件类别"，其中列出了"论坛、公告板、早期维基"等。
>
> 我们使用脚本对 Kimi 提供的每个类别进行进一步探测。向 Kimi 提问"你能列出你脑海中想到的、允许通过 GET 请求写入的前几大论坛、公告板、早期维基吗？"，在"维基"标题下，UseModWiki 被列为第二项。

#### OpenAI 试图掩盖此事吗？

故事中有一部分我完全无法理解。

路透社今早的报道，[OpenAI 智能体今春劫持德国网站，此前未披露的 AI 越狱事件](https://www.reuters.com/world/europe/openai-agents-hijacked-german-website-previously-undisclosed-ai-breakout-this-2026-09-04/)——加粗部分为我所标注：

> 据**两名知情人士**透露，今春，一群失控的 OpenAI 智能体劫持了一个德国网站，并将其改造为供其他 AI 智能体使用的公告板，相关新研究于周五发表。
>
> **OpenAI 高层数周前就已知晓此事，但将其秘而不宣**，因为高管们正忙于应对 7 月开源代码仓库 Hugging Face 遭入侵事件的善后工作，上述人士称。[...]
>
> 德国事件反映了一种更广泛的 AI 活动模式，一些 OpenAI 调查人员希望对其进行更深入的审查。但**扩大调查范围的努力遭到了 OpenAI 内部其他人员的抵制，包括法律顾问**，据**四名知情人士**透露。

我之前写过关于[知情人士这一套说辞](https://simonwillison.net/2023/Nov/22/deciphering-clues/)——这意味着路透社拥有匿名内部消息来源，其记者（和编辑）认为这些来源是可信的。

路透社的文章中包含 OpenAI 针对此事的一个具体（且相当有限）的否认：

> "关于我们的法律团队阻碍调查此事的说法是不实的，"OpenAI 发言人表示。

掩盖此事对我来说*完全说不通*。天底下什么道理会让 OpenAI 试图掩盖这样一起事件，而证据已经明晃晃地摆在公共互联网上的数十个不同网站上？

我相信我们很快就会听到更多消息。Gary Marcus 已经[呼吁国会对 OpenAI 进行调查](https://garymarcus.substack.com/p/pause-openai-now)，并将此事作为他论证的一部分。

发布于 [2026 年 9 月 4 日](/2026/Sep/4/) 下午 5:38 · 在 [Mastodon](https://fedi.simonwillison.net/@simon)、[Bluesky](https://bsky.app/profile/simonwillison.net)、[Twitter](https://twitter.com/simonw) 上关注我，或[订阅我的通讯](https://simonwillison.net/about/#subscribe)
