# Astra 的鹈鹕对比网格相当有趣

         **日期：** 2026-09-04 23:59 UTC
         **链接：** https://simonwillison.net/2026/Sep/4/astra-pelicans/
         **标签：** ai, openai, generative-ai, llms, pelican-riding-a-bicycle, gpt-6-astra

         ---

         > *摘要：今天下午我获得了 GPT-6 Astra 的使用权限，所以很自然地，我拿它生成了鹈鹕骑自行车的 SVG 图像——分别在低、中、高、xhigh 和 max 推理级别下（Astra 不支持 reasoning=*

## Astra 的鹈鹕对比网格相当有趣

2026 年 9 月 4 日

今天下午我获得了 GPT-6 Astra 的使用权限，于是很自然地，我拿它来生成[鹈鹕骑自行车的 SVG 图像](https://simonwillison.net/tags/pelican-riding-a-bicycle/)——分别在低、中、高、xhigh 和 max 推理级别下（Astra 不支持 reasoning=none）。然后我把这些鹈鹕和 GPT-5.6 的 Sol、Terra 以及 Luna 放在一起，做成了[一个对比网格](https://static.simonwillison.net/static/2026/gpt-6-and-5.6-pelicans.html)。除了好玩之外，结果竟然意外地实用。

查看[完整网格](https://static.simonwillison.net/static/2026/gpt-6-and-5.6-pelicans.html)可以看到全尺寸图像。以下是生成 GPT-6 Nova 鹈鹕的对话记录。

这个网格中有几个值得注意的有趣之处。

* Astra 生成的鹈鹕*好得多*。GPT-5.6-Sol 表现最好的那只鹈鹕（我个人觉得 xhigh 比 max 更好）仍然明显只是一堆抽象图形。而 Astra 的每一只鹈鹕，从 low 到 xhigh，都比它好看。Astra 的 max 版本确实非常出色。
* 在 max 以下，Astra 仍然无法可靠地让鹈鹕的双腿分布在车架两侧。
* 在成本方面，Astra 的价格大约是 Sol 的两倍（输入 10 美元/百万令牌，输出 50 美元/百万令牌，而 Sol 为 5 美元/30 美元），但它在每个级别使用的令牌数显著更少，使得不同级别之间的实际价格差距比预期要小。
* Astra low 生成的鹈鹕比 GPT-5.6 Sol 在任何级别下的任何模型都要好，而费用仅为 9.55 美分。花 10 美分在其他任何模型上，得到的结果都要差得多。
* 看看输入令牌数：Astra 和 Luna 都用了 16 个输入令牌，而 Sol 和 Terra 用了 26 个。这很有意思。

我想知道 Astra 和 Luna 之间的关联，是否比 OpenAI 公开承认的还要密切？

发布于 [2026 年 9 月 4 日](/2026/Sep/4/)，晚上 11:59 · 关注我的 [Mastodon](https://fedi.simonwillison.net/@simon)、[Bluesky](https://bsky.app/profile/simonwillison.net)、[Twitter](https://twitter.com/simonw)，或[订阅我的通讯](https://simonwillison.net/about/#subscribe)
