# Qwen 3.8 27B 非常出色，但它默认会过度思考

        **日期：** 2026-08-16 22:00 UTC
        **链接：** https://simonwillison.net/2026/Aug/16/qwen-38-27b/
        **标签：** ai, generative-ai, local-llms, llms, qwen, pelican-riding-a-bicycle, llm-reasoning, llama-cpp, llm-release, coding-agents, lm-studio, ai-in-china, nvidia-spark, pi

        ---

        > *订阅源摘要：周五的重大发布是 Qwen 3.8 27B，这是阿里巴巴 Qwen 研究实验室推出的一款采用 Apache 2 许可、拥有 270 亿参数的视觉能力 LLM。我一直很期待这款模型：27B 是在配置合理的笔记本电脑上运行模型的绝佳尺寸，而其前代产品 [Qwen 3.6 27B](https://simonwillison.net/2026/Apr/22/qwen36-27b/) 也令人印象深刻。*

## Qwen 3.8 27B 非常出色，但它默认会过度思考

2026 年 8 月 16 日

周五的重大发布是 [Qwen 3.8 27B](https://huggingface.co/Qwen/Qwen3.8-27B)，这是阿里巴巴 Qwen 研究实验室推出的一款采用 Apache 2 许可、拥有 270 亿参数的视觉能力 LLM。我一直很期待这款模型：27B 是在配置合理的笔记本电脑上运行模型的绝佳尺寸，而其前代产品 [Qwen 3.6 27B](https://simonwillison.net/2026/Apr/22/qwen36-27b/) 也令人印象深刻。

Qwen 对该模型[自行报告的基准测试](https://huggingface.co/Qwen/Qwen3.8-27B#benchmark-results)结果令人大开眼界。结果显示，该模型相比 Qwen 3.6 27B *以及* 闭源的 Qwen 3.7-Plus 都有所提升，后者截至[今年五月](https://qwen.ai/blog?id=qwen3.7-plus)仍是 Qwen 所有尺寸中最强大的模型之一。独立基准测试对该模型的评价将会很有趣。

我一直在两台不同的机器上运行该模型：我的 128GB M5 Max MacBook Pro，以及一台 [NVIDIA DGX Spark](https://simonwillison.net/2025/Oct/14/nvidia-dgx-spark/)。在两台机器上，我都运行着 LM Studio 和[他们的 17GB Q4\_K\_M 量化版本](https://lmstudio.ai/models/qwen3.8)。我还尝试在 Spark 上直接使用 `llama-server`。

#### 默认的“超高”推理级别导致惊人的过度思考

Qwen 的文档将该模型描述为默认使用 `xhigh` 推理强度，而我一直尝试的 LM Studio GGUF 保留了该默认设置：

> Qwen3.8 官方支持 `reasoning_effort`，可用于调整推理深度并控制成本：
>
> * `xhigh`（默认）：适用于需要深入分析的复杂任务
> * `medium`：在准确性和速度之间取得平衡
> * `low`：高效推理，优化速度和成本

这是一个*滑稽*的默认设置。这绝对不是运行该模型的好方式，尤其是在消费级硬件上。我发现结果非常有趣。

我很快就遇到了 LM Studio 默认 8,192 token 上下文限制的问题——Qwen 在处理最平凡的问题时也会用完所有 token。我将模型加载为完整的 262,144 最大上下文长度，这个问题就解决了。

这是我使用增加后的上下文长度首次尝试得到的[骑自行车的鹈鹕](https://tools.simonwillison.net/markdown-svg-renderer#url=https%3A%2F%2Fgist.github.com%2Fsimonw%2Ffc909bea4fecf752c7bf9bad0e9dbf2a) SVG。生成它花了 **21 分钟**，使用了 22,276 个推理 token 来产生 3,223 个输出 token。你可以[在此处阅读推理过程](https://tools.simonwillison.net/markdown-svg-renderer#url=https%3A%2F%2Fgist.github.com%2Fsimonw%2Ffc909bea4fecf752c7bf9bad0e9dbf2a)。

这是迄今为止我能够用本地机器上运行的模型生成的最好的鹈鹕 SVG——而且这个 Qwen 相当小，磁盘上只有 17GB。有很多值得喜欢的地方：

1. 自行车车架形状正确
2. 自行车两侧都有腿——这*非常*罕见
3. 清晰漂亮的鹈鹕喉囊
4. 翅膀伸展到触及车把！
5. 运动线条在后方，而非前方
6. 背景很有品味——漂亮的太阳、云朵、山丘、花朵和草地。

等待 21 分钟值得吗？绝对不值得。

这是关闭推理后运行相同提示的结果——[此处为记录](https://tools.simonwillison.net/markdown-svg-renderer#url=https%3A%2F%2Fgist.github.com%2Fsimonw%2F1265cfa8dce2f9ad5eb160792ff45a49)。这次产生了 **3,715 个 token**，耗时 137 秒——刚过两分钟。

为了完整起见，我使用 OpenRouter 通过更大的 Qwen 3.8 2.4T-A95B（[上周](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)发布）运行了相同的提示，并得到了这个时髦的[动画 SVG](https://tools.simonwillison.net/markdown-svg-renderer#url=https%3A%2F%2Fgist.github.com%2Fsimonw%2F557016f0895b2abb4b9957caec781734)：

[![

您的浏览器不支持 HTML5 视频。
](https://static.simonwillison.net/static/2026/qwen-animated-first-frame.jpg)](https://static.simonwillison.net/static/2026/qwen-animated-small.mp4)

我说过 Qwen 在 xhigh 级别有过度思考的倾向，但实际情况到底有多糟？

我尝试了一个更简单的提示，同样使用默认的超高设置：

> `draw an svg of a circle`

Qwen 的推理过程是这样开始的：

> 用户要求绘制一个圆形的 SVG。简单的请求——但我想让它成为一件精心制作的作品。让我做一些超越简单 `<circle>` 的东西：一个独立的 SVG 文件，带有特色——也许是一个几何“圆形研究”，带有微妙的动画、分层圆环和独特的调色板。
>
> 控制好范围：他们要求的是一个圆形的 SVG。所以核心是一个圆。但我可以添加工艺：同心引导圆（像圆规/几何绘图）、刻度线、主圆上的柔和渐变填充、克制的环境运动（缓慢旋转的虚线圆环、脉动的光晕）。是否尊重 prefers-reduced-motion？这更多是 CSS 的事；SVG SMIL 或 SVG 内的 CSS 也可以。
>
> 调色板选项：暖纸上的深青色墨水？还是灰白色背景上的醒目朱红色圆加上海军蓝构造线——包豪斯/圆规绘图风格。让我采用“几何研究”的外观：凉爽的石板背景，还是明亮的纸白？纸白没问题，只要不是奶油色和赤陶色的组合。[...]

几分钟后，它[生成](https://tools.simonwillison.net/markdown-svg-renderer#url=https%3A%2F%2Fgist.github.com%2Fsimonw%2F6f9e48293be5c916652d29f0dc0b0657)了这个*绝对美丽*的动画圆形，这完全不是我要求的！

[![

您的浏览器不支持 HTML5 视频。
](https://static.simonwillison.net/static/2026/circle-web-first-frame.jpg)](https://static.simonwillison.net/static/2026/circle-web.mp4)

我的强烈建议：忽略那个默认设置。首先在低推理级别甚至无推理级别运行 Qwen 3.8 27B。它是一个很棒的模型，但那个默认设置确实是一个糟糕的起点。

#### 它非常擅长边界框

测试视觉模型的一个有趣方法是看它能否在照片中的物体周围返回边界框。我之前看到 Qwen 模型在这方面表现良好，所以我决定测试一下，在几只鹈鹕周围绘制边界框。

我之前看到要求 0-1000 比例尺能产生良好的结果。我尝试了这个：

```
llm -a https://static.inaturalist.org/photos/714731804/large.jpg \
  -m lmstudio/qwen/qwen3.8-27b \
  'Return JSON bounding boxes for the pelicans in this photo, 0-1000 scale for each dimension'
```

这是[推理过程](https://gist.github.com/simonw/a05cc78b2061555bd61d3bb9686e689f)，它产生了这个：

```
[
  {"bbox_2d": [195, 290, 370, 780], "label": "pelicans"},
  {"bbox_2d": [445, 320, 675, 850], "label": "pelicans"}
]
```

这*匹配得如此之好*。以下是这些框渲染在照片上的效果：

#### 构建一个标注边界框的工具

那个边界框的可视化是使用一个我让 Qwen 3.8 27B 为我构建的新自定义工具完成的，该工具在我的笔记本电脑上离线运行。

我忘了调低思考强度，所以它被*严重过度设计*了，但它确实设法从[这个单一提示](https://gist.github.com/simonw/121ad098860028b2fab603fa12da1fd9)中产生了[这个完整的界面](https://static.simonwillison.net/static/2026/qwen-over-thinking-bbox.html)：

> ```
> [
>    {"bbox_2d": [195, 290, 370, 780], "label": "pelicans"},
>    {"bbox_2d": [445, 320, 675, 850], "label": "pelicans"}
> ]
> ```
>
> `构建一个 HTML 页面，其中包含一个用于接受图片 URL 的输入框和一个用于接受上述样式 JSON 的文本区域。`
>
> `它将图片附加到页面，测量其宽度和高度，然后将 bbox_2d 中的坐标视为从 0-1000 缩放，并根据实际宽度和高度进行缩放，然后在图片上渲染带标签的框。`

这张截图展示了我*没有*要求的功能之一——一个演示场景，用于在你没有照片来测试工具时使用：

以下是思考过程中相关的部分，它决定绘制自己的鹈鹕，仅仅因为我在提示中给出的示例 JSON 中使用了“pelicans”标签：

> 还要一个“加载示例”，使用已知图片？不能依赖外部图片，但是……图片 URL 输入是用户提供的；我可以添加一个“尝试示例”按钮 [...] 嗯，我可以在画布上绘制一个简单的场景，将其导出为数据 URL，然后加载到图片中——这样既自包含又可演示！[...] 但用户的坐标是针对真实鹈鹕图片的；生成的占位图仍然可以演示缩放。生成一个 1000x1000 的占位图：渐变水面 + 两个放置在给定边界框处的模糊“鹈鹕”剪影（使用相同的比例——可爱：剪影位于精确的 0-1000 位置，显示框对齐）。这构成了一个有趣、自包含的演示。保持简单：天空渐变、太阳、水面、两个类似鹈鹕的形状（椭圆身体、圆形头部、喙）。放置在边界框中心。

（我有点担心世界各地的模型可能会有偏向于在任何可能的机会绘制鹈鹕的倾向，这是近两年来接触我自己愚蠢基准测试的结果。）

所有这些过度思考都是必要的吗？也许至少有一点是必要的。我尝试关闭推理并得到了[这个版本](https://static.simonwillison.net/static/2026/qwen-no-thinking-bbox.html)（[此处为记录](https://gist.github.com/simonw/8e78b1c64d9a56d08eedb954aa9445ee)），它几乎可以工作，但框显示在了错误的位置：

所以没有推理，它没能一次性生成一个可用的工具。我相信通过一些后续提示它可以做到，但这是一个很好的例子，说明推理可以产生不同。

#### 是的，它可以驱动编码代理

围绕本地模型的最大问题之一是它们是否有足够的马力来成功运行编码代理循环。编码代理需要长上下文、强大的代码生成支持和可靠的工具调用。从纸面上看，Qwen 3.8 27B 具备这三者，那么它能胜任这项任务吗？

我使用 [Pi](https://pi.dev/) 的初步实验非常有前景。我选择 Pi 是因为它的系统提示比其他大多数选项更短，更适合尝试较小的模型。

我通过将以下内容添加到 `~/.pi/agent/models.json`，将 Pi 配置为使用在 Spark 上的 LM Studio 中运行的 Qwen 3.8 27B（通过 `tailscale serve` 共享）：

{
  "providers": {
    "spark": {
      "baseUrl": "https://spark-18b3.tail68a31.ts.net/v1",
      "api": "openai-responses",
      "apiKey": "dummy",
      "models": [
        {
          "id": "qwen3.8-27b",
          "reasoning": true
        }
      ]
    }
  }
}
```

然后我在 `~/dev/datasette` 文件夹中运行了 `pi --provider spark --model qwen3.8-27b`，并提示：

> `auth 是如何工作的？`

在一系列推理和工具调用（访问了大量不同文件）之后，它生成了[这个回复](https://gist.github.com/simonw/6693d74a6bd45f641d43ceb9961dd95f#core-idea-actors--plugins-no-built-in-user-accounts)，内容非常扎实。

只有一个问题：我想分享那段对话记录。于是我将 Pi 和 Qwen 3.8 27B 指向 `~/.pi/agent/sessions/--Users-simon-Dropbox-dev-datasette--` 中的 JSONL 对话记录文件，并提示：

> `编写 Python 代码，将此 jsonl 转换为 markdown`

它构建并测试了这个 [pi\_jsonl\_to\_md.py](https://github.com/simonw/tools/blob/main/python/pi_jsonl_to_md.py)，完全满足了我的需求。这里是[那段会话记录](https://gist.github.com/simonw/491e55ac9d741202ea0af5d9d93775d4)，正是使用它创建的工具发布的。

#### 对速度的追求

到目前为止，这一切看起来都*非常*有前景。我们有一个 17GB 的模型，可以在高端消费级硬件上运行，能够编写代码、驱动工具、标注图像，基本上能完成我从 LLM 那里获得实际工作所需的一切。

但有一个非常显著的缺点：它感觉有点慢——尤其是当它开始过度思考时，但即使没有这种情况，它也不是特别敏捷。

我在 LM Studio 上大约能达到每秒 15-30 个 token。这不算糟糕，但速度慢到足以让我很难从托管 API 模型那边被吸引过来，后者返回结果的速度要快得多。Artificial Analysis [跟踪 token 速度](https://artificialanalysis.ai/models#speed)，显示 OpenAI 5.6 Sol 为每秒 74 个 token，而 5.6 Luna 则达到了令人印象深刻的每秒 184 个。

好消息是，自模型两天前首次发布以来，社区一直在探索加速的方法。

其中最有前景的优化之一已经内置于模型本身。Qwen 支持[多 Token 预测](https://sebastianraschka.com/llm-architecture-gallery/mtp/)，这是一种架构技巧，通过一个更廉价的机制来猜测后续几个 token，然后主模型可以快速验证这些猜测是否正确。这对推理性能可以产生相当显著的影响。

根据 `llama.cpp` 创建者 Georgi Gerganov 的[这条推文](https://twitter.com/ggerganov/status/2088340681701925253)，我尝试在 Spark 上像这样使用 MTP 运行模型：

```
llama serve \
 -hf  ggml-org/Qwen3.8-27B-GGUF:Q4_K_M \
 -hfd ggml-org/Qwen3.8-27B-GGUF:Q4_0 \
 --spec-default \
 --spec-type draft-mtp \
 --reasoning-preserve
```

果然，这给了我显著的提升。我让 GPT-5.6 在 Codex 中运行了[一个在 Spark 上的对比基准测试](https://gist.github.com/simonw/b08c7eb9c126c806ba8987e269ea736b)，`--spec-type draft-mtp` 服务器比 LM Studio 默认的 GGUF 性能高出约 72%。

我预计在接下来的几周内，我们会看到更多关于如何更快地服务这个模型的创新。MLX 社区可能也有一些技巧正在酝酿中。

#### 一些观察

一个 17GB 的文件能在我的家用机器上完成所有这些事情，这简直是一个*奇迹*。我再次对本地模型今年取得的巨大进步感到欣喜和惊叹。一年前，这还足以与最优秀、最昂贵的专有模型竞争——而今天，它可以在性能不错的笔记本电脑上运行。

唯一阻碍它成为日常主力工具的就是性能。在 M5 Mac 和 DGX Spark 上，它都感觉相当慢。这就是这些密集（非混合专家）模型的缺点——它们需要大量的内存带宽才能表现良好，而我能使用的这两台机器在这方面都不是顶尖的。

关于 Qwen 3.8 27B，最重要的一点是**它所展示的意义**。我们可以拥有一个开放权重的通用模型，具备长上下文、有效的工具调用、强大的视觉能力和合格的代码生成能力，而且整个模型可以装进一个仅 17GB 的文件中。

这个尺寸的模型继续以惊人的速度进步。我们不需要花费五十万美元购买数据中心级硬件，就能运行一个称职的模型。

发布于 [2026年8月16日](/2026/Aug/16/) 晚上10点 · 在 [Mastodon](https://fedi.simonwillison.net/@simon)、[Bluesky](https://bsky.app/profile/simonwillison.net)、[Twitter](https://twitter.com/simonw) 上关注我，或[订阅我的通讯](https://simonwillison.net/about/#subscribe)
