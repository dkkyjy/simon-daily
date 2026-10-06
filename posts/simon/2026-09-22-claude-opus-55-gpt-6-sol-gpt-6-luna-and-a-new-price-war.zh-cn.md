# Claude Opus 5.5、GPT-6 Sol、GPT-6 Luna 与新一轮价格战

**日期：** 2026-09-22 23:46 UTC  
**链接：** https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/  
**标签：** ai, openai, generative-ai, llms, anthropic, claude, llm-pricing, pelican-riding-a-bicycle, gpt

---

> *Feed 摘要：昨天发布了 Grok 4.7（鹈鹕）和 MiMo v2.6 Flash/Pro（更多鹈鹕）。今天 Anthropic 发布了 Claude Opus 5.5，大约一小时后 OpenAI 发布了 GPT-6 Sol 和 GPT-6 Luna。要全面评估这些新模型还需要一些时间，但以下是我目前的印象。*

## Claude Opus 5.5、GPT-6 Sol、GPT-6 Luna 与新一轮价格战

2026年9月22日

昨天发布了 [Grok 4.7](https://x.ai/news/grok-4-7)（[鹈鹕](https://news.ycombinator.com/item?id=49788838#49790209)）和 [MiMo v2.6 Flash/Pro](https://mimo.xiaomi.com/mimo-v2-6)（[更多鹈鹕](https://news.ycombinator.com/item?id=49792730#49793480)）。今天 Anthropic [发布了 Claude Opus 5.5](https://www.anthropic.com/claude-opus-5-5)，大约一小时后 OpenAI [发布了 GPT-6 Sol 和 GPT-6 Luna](https://openai.com/index/introducing-gpt-6-sol-and-luna/)。要全面评估这些新模型还需要一些时间，但以下是我目前的印象。

#### GPT-6 Sol 和 Luna 的价格是 GPT-5.6 对应型号的一半

GPT-5.6 Luna 一直是我构建应用的首选模型，因为它结合了出色的性能和*非常低廉*的价格。不知怎的，GPT-6 Luna 的价格又降低了一半——而 GPT-6 Sol 相比 GPT-5.6 Sol 也有类似的降幅。

以下是当前的价格格局：

| 模型 | 输入 | 缓存输入 | 输出 |
| --- | --- | --- | --- |
| GPT-6 Luna | $0.10/M | $0.01/M | $0.50/M |
| GPT-5.6 Luna | $0.20/M | $0.02/M | $1.20/M |
| Grok 4.7 | $2/M | $0.50/M | $6/M |
| GPT-6 Sol | $2/M | $0.20/M | $10/M |
| GPT-5.6 Terra | $2/M | $0.20/M | $12/M |
| Claude Opus 5.5 | $4/M | $0.20/M | $20/M |
| GPT-5.6 Sol | $4/M | $0.40/M | $20/M |
| Claude Fable 5.1 | $10/M | $0.25/M | $50/M |
| GPT-6 Astra | $10/M | $1/M | $50/M |

需要注意的是，GPT-5.6 计划在11月涨价25%，因此 GPT-6 的价格是那些模型*促销*价格的一半。

（由于 GPT-5.6 Terra 与 GPT-6 Sol 价格相同，继续使用 Terra 的任何理由都消失了。）

很难强调这种价格竞争有多激烈。Grok 4.7 定价为 $2/$6，不到 GPT-5.6 Sol 价格的一半，但现在输入价格与 GPT-6 Sol 相同，输出价格也更接近。

以 $0.10/$0.50 的价格，GPT-6 Luna 是 OpenAI 有史以来最便宜的模型之一，只有性能弱得多的 GPT-4.1 Nano（$0.10/$0.40，2025年4月）和 GPT-5 Nano（$0.05/$0.40，2025年8月）比它更便宜。

我为 [GPT-6 Luna](https://tools.simonwillison.net/markdown-svg-renderer?url=https%3A%2F%2Fgist.github.com%2Fsimonw%2F40d129fc140faca378b9c9f4f16c6ec2) 和 [GPT-6 Sol](https://tools.simonwillison.net/markdown-svg-renderer?url=https%3A%2F%2Fgist.github.com%2Fsimonw%2Fbe7ae25af2634b68bc34b7b7aaf02cb2) 生成了鹈鹕图像，然后将它们与 GPT-5.6 的鹈鹕一起整合到[这个对比网格](https://static.simonwillison.net/static/2026/gpt-pelicans-grid.html)中。我喜欢你可以立即看出 5.6 系列选择了更大胆、更明亮的颜色，而 6 系列要低调得多。我认为 GPT-6 Astra 在 max 模式下生成的仍然是最好的鹈鹕。

#### Claude Opus 5.5 也降价了

Opus 5.5 似乎解决了人们对 Opus 沟通风格的最大抱怨。[Thariq Shihipar](https://twitter.com/trq212/status/2102437686967738431)：

> Opus 5.5 是根据您的反馈改进的。
>
> 它沟通清晰，每 token 价格比 Opus 5.0 更便宜，具备 Fable 5.1 的智力水平，非常节省 token，适用于各种工作强度。

它还被宣传为在 [Blender](https://twitter.com/alexalbert__/status/2102466523164274839) 方面表现更好。我期待在那里测试它的性能。

Opus 4.5、4.6、4.7、4.8 和 5 的价格都相同：输入 $5/百万 token，输出 $25/百万 token。5.5 降价了20%——输入 $4/百万，输出 $20/百万。

缓存读取的价格降低了60%。这对于更长的智能体对话意义重大，其中90%以上的输入 token 以缓存 token 价格处理。

Opus 5.5 的新价格与 GPT-5.6 Sol 的价格相同，但那是在 OpenAI *之前*将 Sol 价格减半的时候。

GPT-6 Astra 和 Claude Fable 5.1 都定价为输入 $10/百万、输出 $50/百万。目前的价格战影响的是低于这一层级的下一层模型。

Anthropic 表示 Sonnet 5.5 和 Haiku 5.5 即将推出。鉴于当前 Haiku 4.5 的价格是 $1/$5，而最新的 GPT-6 Luna 价格仅为它的*十分之一*（$0.10/$0.50），看看 Haiku 能否在低端重新获得价格竞争力将会很有趣。

#### Claude Opus 5.5 max 过度思考直到崩溃

在我的"[生成一只骑自行车的鹈鹕的 SVG](https://simonwillison.net/tags/pelican-riding-a-bicycle/)"测试中，Claude Opus 5.5 在"max"思考级别首次未能返回响应！

它首先称这是一个"经典的测试请求"，然后非常*非常*认真地思考它正在做的事情：

> 这是一个经典的测试请求，所以我想要规划一只构图良好的鹈鹕，它有独特的喙和喉囊，骑着一辆有正确车轮、车架和踏板自行车，背景是简单的天空和地面。[...]
>
> 验证小腿长度大约是95.2，足够接近。现在我正在计算从臀部到膝盖再到脚踝的近腿路径，然后草绘脚部形状，使其自然放置在踏板上——用线条和曲线勾勒出脚跟、脚趾尖和鞋底轮廓，使其自然地坐在 y=478-494 的踏板表面上。[...]
>
> 我喜欢鱼从篮子里突出的细节，鹈鹕盯着它看，这是一个值得保留的有趣细节。我还在确认眼睛位置靠近喙基部，符合典型的鹈鹕解剖结构，并考虑给它一个稍微更快乐的表情。[...]
>
> 远腿正确地显示为从车架后面经过，所以我正在继续检查链轮齿并确认图层顺序——远曲柄臂应该大部分被座管和链轮遮挡。我正在确定最终 SVG 的宽度和高度属性以及 viewBox，以确保正确缩放，注意到没有文字，所以不需要 font-family。[...]

我非常期待看到这只鹈鹕……但它[停下来了](https://tools.simonwillison.net/markdown-svg-renderer?url=https%3A%2F%2Fgist.github.com%2Fsimonw%2F61fd7c3683fffce9a3ab7c43d1180024#response-4)。Opus 5.5 有128,000 的最大输出 token 限制（其他 Claude 模型也有），它在还在推理 SVG 时就达到了这个限制！

我试了第二次，得到了相同的结果。这让我怀疑"max"实际上是无用的——如果它在愚蠢的 SVG 提示上过度思考到崩溃，我就不相信它不会对更有趣的工作做同样的事。

（那两次失败每次花费我 [$2.56](https://www.llm-prices.com/#it=27&ot=128000&sel=claude-opus-5-5)，耗时近20分钟。）

Fable 5.1 在"max"模式下没有过度思考，并给了我[我见过的最好的鹈鹕](https://simonwillison.net/2026/Sep/1/claude-fable-5-1/#max)，来自任何 Anthropic 模型。

以下是 [Opus 5.5 的鹈鹕](https://tools.simonwillison.net/markdown-svg-renderer?url=https%3A%2F%2Fgist.github.com%2Fsimonw%2F61fd7c3683fffce9a3ab7c43d1180024)，不包括 5.5 max。

我还构建了[这个对比网格](https://static.simonwillison.net/static/2026/claude-pelicans-grid.html)，将它们与 Opus 5、Fable 5.1 和 Sonnet 5 的鹈鹕进行比较：

通过比较不同模型厂商画骑自行车鹈鹕的能力可能现在意义不大（如果曾经有意义的话），但我仍然发现使用它们来比较同一模型家族在不同推理级别的表现有价值。

我现在使用 GPT-6 Sol 和 Claude Opus 5.5 作为 Codex 和 Claude Code 中的默认模型。我已将 [agent.datasette.io](https://agent.datasette.io/) 上的 Datasette Agent 演示升级为使用 GPT-6 Luna，它在 SQL 查询和构建 [Datasette Apps](https://simonwillison.net/2026/Jun/18/datasette-apps/) 的 HTML 和 JavaScript 方面似乎既快速又胜任。

发布于 [2026年9月22日](/2026/Sep/22/) 23:46 · 在 [Mastodon](https://fedi.simonwillison.net/@simon)、[Bluesky](https://bsky.app/profile/simonwillison.net)、[Twitter](https://twitter.com/simonw) 上关注我，或[订阅我的通讯](https://simonwillison.net/about/#subscribe)
