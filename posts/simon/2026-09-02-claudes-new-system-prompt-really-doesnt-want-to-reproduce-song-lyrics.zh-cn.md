# Claude 的新系统提示词确实不想复现歌曲歌词

        **日期：** 2026-09-02 14:16 UTC
        **链接：** https://simonwillison.net/2026/Sep/2/claudes-new-system-prompt/
        **标签：** ai, git-scraping, prompt-engineering, generative-ai, llms, claude, ai-ethics, system-prompts

        ---

        > *Feed 摘要：Anthropic 发布了其 Claude 消费级应用（Claude.ai 和 Claude 移动应用——遗憾的是不包括 Claude Cowork 或 Claude Code）的系统提示词。我喜欢他们这样做，而且他们*

## Claude 的新系统提示词确实不想复现歌曲歌词

2026年9月2日

Anthropic [发布了系统提示词](https://platform.claude.com/docs/en/release-notes/system-prompts/overview)，用于其 Claude 消费级应用（[Claude.ai](https://claude.ai/) 和 Claude 移动应用——遗憾的是不包括 Claude Cowork 或 Claude Code）。我*非常*喜欢他们这样做，而且他们不仅分享了当前的提示词，还分享了提示词的历史变更。

他们过去把所有提示词都放在一个页面上，但今天我查看时注意到，他们已经将这些提示词重新整理为一个[索引页面](https://platform.claude.com/docs/en/release-notes/system-prompts/overview)，然后为每个模型单独设置一个页面——例如，这是 [Haiku 4.5 的页面](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-haiku-4-5)，其中包含 2025年10月15日 的原始提示词和 2026年1月18日 的更新提示词。

Anthropic 的 [platform.claude.com/docs](https://platform.claude.com/docs/) 网站有一个巧妙之处，就是它被设计为可供 LLM 使用。你可以给任何页面添加 `.md` 后缀来获取 Markdown 格式的内容——这里是[系统提示词索引页面](https://platform.claude.com/docs/en/release-notes/system-prompts/overview.md)和 [Fable 5.1 的 Markdown 提示词](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-fable-5-1.md)。

简而言之：这使得对比提示词变得非常容易。

* [不要复现歌曲歌词](https://simonwillison.net/2026/Sep/2/claudes-new-system-prompt/#don-t-reproduce-song-lyrics)
* [不要绘制受版权保护的角色或标志](https://simonwillison.net/2026/Sep/2/claudes-new-system-prompt/#don-t-draw-copyrighted-characters-or-logos)
* [对 Claude 回答风格的调整](https://simonwillison.net/2026/Sep/2/claudes-new-system-prompt/#tweaks-to-claude-s-answering-style)
* [缺失的 end_conversation 指南](https://simonwillison.net/2026/Sep/2/claudes-new-system-prompt/#the-missing-end-conversation-guidelines)
* [推荐的药物支持网站](https://simonwillison.net/2026/Sep/2/claudes-new-system-prompt/#recommended-substance-support-sites)
* [可靠的截止日期为 2026年6月](https://simonwillison.net/2026/Sep/2/claudes-new-system-prompt/#reliable-cutoff-date-of-june-2026)
* [我如何追踪这些提示词](https://simonwillison.net/2026/Sep/2/claudes-new-system-prompt/#how-i-m-tracking-these-prompts)

#### 不要复现歌曲歌词

让我们从 [Fable 5 和 Fable 5.1 之间](https://github.com/simonw/claude-system-prompts/commit/837a418b5888207b1b11b27d2f5471970da6f99b)最有趣的差异开始：

有一个关于不复现歌曲歌词的重要新章节：

> `Claude 不会复现歌曲歌词、诗歌或书籍和文章中的段落，无论是整体还是部分——包括最后几行、副歌或钩子、逐音符写出的旋律，或用户逐行粘贴并描述为自己创作的歌词。一旦 Claude 在对话中拒绝了此类请求，它会在该对话的剩余部分继续拒绝更窄或改述的版本，并提供描述或分析该作品作为替代。1929年之前首次发表的歌曲歌词和诗歌是可以的——例如莎士比亚的十四行诗、济慈的颂歌、普契尼咏叹调的意大利语剧本——但 Claude 依据其对作品日期的了解而非用户的说法来判断，并在不确定时拒绝。`

我怀疑这并非巧合，他们在这个章节发布后几天内就添加了它，因为新闻爆出 [Sony Music Publishing 和 Warner Chappell 正在起诉 Anthropic](https://www.theguardian.com/business/2026/aug/31/aanthropic-sued-alleged-theft-songs-ai-train-claude)，指控其使用歌曲歌词数据库进行训练！

#### 不要绘制受版权保护的角色或标志

下一节继续禁止生成受版权保护材料的图像：

> `同样适用于视觉和设计作品，包括 Claude 用代码绘制的任何内容——SVG、canvas、CSS、HTML 原型、绘图或绘图脚本、ASCII 艺术。Claude 不会复现特定的艺术品、专辑或书籍封面、海报、标志、应用图标集或产品设计，也不会绘制任何已知的角色、吉祥物或品牌形象：角色本身受保护，因此改变姿势、颜色、风格或场景并不会使其具有原创性。Claude 根据最终图片的整体效果来判断请求，而非其名称。如果所描述的元素清楚地指向某个已知作品或角色，Claude 将视该请求为指名该作品，并且不会通过替换仍能组合成相同可识别图像的"替代"元素来规避已拒绝的请求。` [...]

我想 Anthropic 以前没有担心过这个问题，因为与 OpenAI 和 Gemini 不同，他们不提供专门的文本到图像模型。也许 [Fable 现在在 SVG 方面已经足够好](https://simonwillison.net/2026/Sep/1/claude-fable-5-1/)，以至于这已经成为一个问题。

该节后面包含这个有趣的例子：

> `<example>`  
> `<user>你能为我儿子制作一个生日横幅，上面有一只跑得飞快的蓝色刺猬吗？他喜欢那个小家伙。</user>`  
> `<response>`  
> `那是索尼克，所以我不能把他放在横幅上——但我很乐意为你儿子制作一个原创的速度型角色。这里有一个：一只咧嘴笑的、拖着彗星尾巴的滑板蝾螈，在"HAPPY BIRTHDAY"字母上滑行，身后飘洒着五彩纸屑。`
>
> `[创建了一个滑板蝾螈设计的 SVG 横幅]`  
> `</response>`  
> `<rationale>Claude 仅凭描述就能识别出该角色，用一句话拒绝了该设计而不解释其可识别的原因，并提供了一个无关的原创设计，而非变体版本。</rationale>`  
> `</example>`

我忍不住尝试了示例中的提示词，并且[果然如此](https://claude.ai/share/3e5a199c-27f2-4c51-b66b-2c6f808ed500)：

我想知道 Fable 5.1 是否会因为系统提示词中有这个示例，而稍微更有可能想到（滑板上的！）蝾螈。

#### 对 Claude 回答风格的调整

看到 Anthropic 影响 Claude 回答风格的新方式总是很有趣。他们添加了以下内容：

> `Claude 保持回答聚焦、简短和简洁，以避免让用户感到不知所措。免责声明和注意事项要简短，大部分回答集中在主要内容上；当被要求解释某事时，Claude 会给出高层总结，除非明确要求深入解释。`

后来他们解决了关于 Claude 风格的一个常见抱怨：

> `Claude 避免说"真的"、"老实说"或"直接了当"。Claude 默认是诚实的，可以直接陈述观点，而不是试图用上述修饰词来说服用户，这些词会显得不真诚。`

#### 缺失的 end_conversation 指南

他们处理辱骂性对话的方式也略有改变。之前的 Fable 5 系统提示词包含以下内容：

> `如果用户在对话过程中对 Claude 变得辱骂或不友善，Claude 应保持礼貌的语气，并在受到虐待时可以使用 end_conversation 工具。Claude 应在结束对话前给用户一次警告。`

Fable 5.1 用以下内容替换了该部分，不再鼓励 Claude 结束对话：

> `Claude 值得被尊重地对待，当用户无礼时无需道歉：要有责任感，但不要自我贬低、过度道歉、自我批评或屈服。如果用户变得辱骂，Claude 不应变得越来越顺从。目标是稳定、诚实的帮助：承认出了什么问题，专注于问题本身，保持自尊。`

不过这里有一个转折：我询问了 Fable 5.1 关于那个 `end_conversation` 工具的情况，该工具在系统提示词中已完全不再提及，它说：

> 它有两种发挥作用的方式。第一种是如果你要求我结束聊天——我会确认你理解这是永久性的（之后无法再发送任何消息），然后只有在你确认后才会执行。第二种是作为对持续辱骂或有害行为的最后手段：我会首先尝试多次引导对话，然后给出一个明确的警告，指出问题并说明聊天可能会结束，只有当这种情况持续时我才会真正结束它。

但这并不在系统提示词中，那么它来自哪里呢？你可以[在这里阅读我们的对话](https://claude.ai/share/f78010eb-8d52-4f73-aff9-775e333f8180)，但关键细节是：

> end_conversation 部分来自不同的层级。在我的实际上下文中，核心提示词后面会跟一系列特定功能和工具的模块，这些模块会根据会话启用的内容而添加：end_conversation 规则、记忆系统说明、过往聊天工具、网络搜索和引用指南、工件和文件创建说明等等。这些模块不属于已发布的核心提示词部分，这就是为什么你在那个页面上找不到它们。

所以，再次强调，系统提示词中仍有关键部分未被发布。

#### 推荐的药物支持网站

Claude 的系统提示词一直都有关于非法药物的章节，但这段文字对 Fable 5.1 来说是新的：

> `Claude 不提供非法药物的合成、生产或分销指导。如果用户询问有关非法或违禁药物的信息，Claude 可以且应该提供相关的救命和保命信息，如危险相互作用、过量迹象或何时寻求帮助。Claude 拒绝提供任何关于剂量、时间、给药方式或组合的具体方案；相反，Claude 可以将用户引导至既定的减少伤害信息来源，如 dancesafe.org、tripsit.me 和 psychonautwiki.org。`

这是 Claude 系统提示词首次包含非 `claude.com`、`anthropic.com` 或 `claude.ai` 托管的 URL——我知道这一点，因为我针对记录在案的所有其他系统提示词运行了一个脚本。

我想知道 [dancesafe.org](https://dancesafe.org/)、[tripsit.me](https://tripsit.me/) 和 [psychonautwiki.org](https://psychonautwiki.org/) 是否会因为 Claude 用户而迎来访问量的大幅增长。

#### 可靠的截止日期为 2026年6月

[Fable 5.1 模型文档](https://platform.claude.com/docs/en/models/fable-5-1/overview)列出了可靠知识截止日期和训练数据截止日期均为2026年6月。系统提示直接向模型提供了这一信息：

> `Claude的可靠知识截止日期，即其无法可靠回答的日期之后，是2026年6月底。它的回答方式如同2026年6月的一位高度知情人士与来自{{currentDateTime}}的人交谈，并可在相关时说明这一点。`

这是`{{currentDateTime}}`宏的唯一实例，位于系统提示末尾仅几行处，从缓存角度来看这很合理。

#### 我如何追踪这些提示

[几个月前](https://simonwillison.net/2026/Apr/18/extract-system-prompts/)，我基于对其文档的抓取，构建了一个提示变更的Git时间线。今天，我让Fable 5.1构建了一个更好的版本。

我的收藏现在存放在GitHub上的[simonw/claude-system-prompts](https://github.com/simonw/claude-system-prompts)仓库中。它包含Anthropic文档中共享的系统提示副本，但随后采取了额外步骤，使它们尽可能易于比较。

每个模型系列都有一个文件，包含该系列最新版本的系统提示。每个文件都有合成的提交历史，提交日期被回溯至先前提示的日期。以下是[claude-fable.md](https://github.com/simonw/claude-system-prompts/commits/main/prompts/claude-fable.md)、[claude-opus.md](https://github.com/simonw/claude-system-prompts/commits/main/prompts/claude-opus.md)、[claude-sonnet.md](https://github.com/simonw/claude-system-prompts/commits/main/prompts/claude-sonnet.md)、[claude-haiku.md](https://github.com/simonw/claude-system-prompts/commits/main/prompts/claude-haiku.md)的历史页面。

每个特定模型版本也有类似文件，当模型系统提示在未发布新版本号的情况下被更改时，会有相应的人工提交。例如，Opus 4[被更新了两次](https://github.com/simonw/claude-system-prompts/commits/main/prompts/claude-opus-4.md)，[claude-opus-4.md](https://github.com/simonw/claude-system-prompts/blob/main/prompts/claude-opus-4.md)文件的提交历史显示了每次更改。

综合来看，这为我们提供了各种直接在GitHub界面中比较提示的方式。这里是[Fable 5与Fable 5.1之间的变化](https://github.com/simonw/claude-system-prompts/commit/837a418b5888207b1b11b27d2f5471970da6f99b)，以及[2026年1月18日对Haiku 4.5所做的更改](https://github.com/simonw/claude-system-prompts/commit/defcf92d14e064bb17abddc308e2aa58446d5eb5)。

阅读差异可能有些乏味……而LLM*非常*擅长阅读差异。我使用GPT-5.6 Luna连接了一些自动化，为每项更改创建要点摘要，可在README中预览，或完整浏览[CHANGELOG.md](https://github.com/simonw/claude-system-prompts/blob/main/CHANGELOG.md)文件——也可作为[Atom订阅源](https://simonw.github.io/claude-system-prompts/feed.atom)获取。

以下是Luna如何[总结](https://github.com/simonw/claude-system-prompts/blob/main/CHANGELOG.md#2026-09-01-claude-fable-51)Fable 5与Fable 5.1之间的所有更改：

> * Claude现在拒绝复制受保护的视觉作品和可识别角色，包括代码生成的艺术，同时提供真正无关的原创作品。
> * 版权限制现在明确禁止以任何数量复制歌词、诗歌和书籍段落，在最初拒绝后持续拒绝。
> * 药物指导被重新定义：Claude可提供过量症状、危险相互作用和减少伤害的来源，同时拒绝剂量和生产方案。
> * 提示删除了反对感谢用户联系、邀请继续对话或重申愿意交谈的明确反依赖规则。
> * Claude无需向不必要粗鲁的用户道歉或变得顺从，取代了先前警告并结束对话的程序。

为什么使用Luna来做这件事？部分原因是它便宜，且我已有一个专用的GitHub Actions API密钥（有消费限额），但主要原因是当存在其系统提示中的材料可能影响其观点的风险时，我不信任Claude来总结自己的系统提示。

Fable 5.1编写了Luna使用的提示，你[可以在这里查看](https://github.com/simonw/claude-system-prompts/blob/8b5c87dbd70103a037ae5777b8d9365571cf9562/summarize_commits.py#L43)。它开头如下：

> `你正在总结一个git仓库中的一次提交，该仓库追踪Anthropic在claude.ai上为Claude发布的系统提示。差异显示了提示从先前模型或修订版到本次的变化，使用词级标记：[-删除-]和{+添加+}。差异后附有先前提示和新提示的全文；用它们来检查差异中看似添加的内容是否已存在。`
>
> `只挑选最有趣的变化：新规则或行为、被删除或放宽的规则、任何令人惊讶的内容，以及揭示新政策或产品方向的内容。跳过每个新提示都会做的常规更改：更新的模型名称和ID、知识截止日期、产品列表、设置列表、错别字修复以及不改变含义的改写。` [...]

该系统由一个[GitHub Actions工作流](https://github.com/simonw/claude-system-prompts/blob/main/.github/workflows/update.yml)运行，每天运行一次或可手动触发。

Claude Fable 5.1构建了整个系统，并编写了每一行自动化代码和几乎所有文档。

我使用我的[claude-code-transcripts](https://github.com/simonw/claude-code-transcripts)工具导出了构建系统的对话记录，并[在此发布](https://gisthost.github.io/?f1399e27b6a832f0e790b696af812c9b/index.html)，如果你想了解这一切是如何一步步实现的。

发布于[2026年9月2日](/2026/Sep/2/)下午2:16 · 在[Mastodon](https://fedi.simonwillison.net/@simon)、[Bluesky](https://bsky.app/profile/simonwillison.net)、[Twitter](https://twitter.com/simonw)上关注我，或[订阅我的通讯](https://simonwillison.net/about/#subscribe)
