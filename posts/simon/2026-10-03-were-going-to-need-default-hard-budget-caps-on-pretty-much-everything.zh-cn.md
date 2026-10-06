# 我们几乎需要对所有服务都设置默认的硬性预算上限

         **日期：** 2026-10-03 23:34 UTC
         **链接：** https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/
         **标签：** amazon-web-services, ai, coding-agents

         ---

         > *Feed summary: Here's a product feature which the world is going to need a whole lot more of over the coming months and years: default hard budget caps. I'm talking about the feature of pay-by-usage services and API*

## 我们几乎需要对所有服务都设置默认的硬性预算上限

2026年10月3日

在未来几个月和几年里，世界将越来越多地需要这样一个产品功能：**默认的硬性预算上限**。我指的是按使用量付费服务和API中的一项功能，让你可以设定“每月超过$X后，关闭该服务并返回错误”。这些必须是**硬性**限制。软性上限，例如“每月超过$X后，给我发送一封警告邮件”，是不够的。

编码代理和个人代理（包装在不太吓人UI中的编码代理）大大降低了启动能够做有用事情的代码的摩擦。有时这些事情会产生费用——调用付费API、托管Web应用，或者可以为额外存储和计算计费的系统。

没有人希望醒来时收到一封午夜发送的邮件，警告预算上限，并发现他们的失控服务在他们睡觉时消耗了数百（或数千）美元的使用量。

反对这一点的一个论点是，企业不希望他们的托管应用因为超过某些预算而开始抛出错误。我认为大多数企业和个人会更愿意接受错误，而不是意外的10,000美元以上的账单。

我认为硬性预算上限应该是默认的。如果有人想冒险，他们可以这样做，但这必须是在选择加入的基础上。在某个显眼的位置放置一个清晰明了的复选框：

> 移除预算上限。如果我的应用超过配置的预算上限，它将不会被关闭，我将负责后续的收费。

我最希望看到这个功能的服务是AWS。我听到很多故事，人们拒绝在个人项目中使用AWS，因为他们（有理由地）担心失控的服务可能会让他们破产。我也听到一些故事，人们*没有*预料到这一点，最终遭受了严重的损失。

……事实证明，AWS终于在几周前推出了支出限制！根据他们9月16日的公告[新的AWS体验帮助构建者更快启动和发布](https://aws.amazon.com/about-aws/whats-new/2026/09/New-AWS-Builder-Experience/)：

> 当你准备好升级到付费计划时，你可以根据使用模式为你的项目设置月度支出上限，以确保你在预算范围内。如果项目的用量达到其支出上限，你的项目将在当月暂停。

参见[在AWS设置中创建支出上限](https://docs.aws.amazon.com/accounts/latest/reference/create-spend-limit.html)，尽管该页面警告说“我们目前只向有限数量的客户推出新体验”。希望这很快就能对现有账户全面开放。

Google Cloud在7月[推出了类似的功能](https://cloud.google.com/blog/topics/cost-management/new-early-anomalies-and-spend-caps-on-google-cloud-budgets)，称为支出上限，允许你“在项目的特定服务上设置月度财务上限”。看起来这正在成为一种趋势！

在理想的世界里，我们的代理可以帮助处理这个问题。如果代理开始倾向于推荐具有硬性预算上限的服务提供商，并警告新手和有经验的构建者不要使用无上限的服务部署应用，那就太好了，因为这些服务可能会让他们陷入麻烦。

发布于[2026年10月3日](/2026/Oct/3/) 23:34 · 在[Mastodon](https://fedi.simonwillison.net/@simon)、[Bluesky](https://bsky.app/profile/simonwillison.net)、[Twitter](https://twitter.com/simonw)上关注我，或[订阅我的通讯](https://simonwillison.net/about/#subscribe)
