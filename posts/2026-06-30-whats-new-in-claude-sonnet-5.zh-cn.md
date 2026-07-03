# Claude Sonnet 5 的新特性

        **日期：** 2026-06-30 13:23 UTC
        **链接：** https://simonwillison.net/2026/Jun/30/claude-sonnet-5/#atom-everything
        **标签：** ai, 生成式人工智能, 大语言模型, anthropic, claude, 大语言模型定价, 鹈鹕骑自行车, 大语言模型发布

        ---

        Claude Sonnet 5 的新特性 Claude Sonnet 5 今早发布了。我总是直接查看"新特性"开发者文档，因为它们往往比官方公告文章包含更多可操作的信息。Anthropic 对 Sonnet 5 的描述是："其性能接近 Opus 4.8，但价格更低"。系统卡片有助于解释他们是如何在不被美国政府阻止的情况下发布该模型的：Sonnet 5 在网络任务方面的能力明显低于 Mythos 5：因此其安全措施与我们应用于 Opus 4.7 和 Opus 4.8（这些模型比 Sonnet 5 能力更强，但远低于 Mythos 5）的措施类似。从"新特性"API 变更中值得注意的是：采样参数 temperature、top_p、top_k 不再受支持。它拥有 100 万个 token 的上下文窗口和 128,000 个最大输出 token。它具备"与 Claude Sonnet 4.6 相同的工具和平台功能集"。自适应思维默认开启，除非你指定 "thinking": {type: "disabled"}。定价与 Sonnet 4.6 相同：输入每百万 token 3 美元，输出每百万 token 15 美元，并在 8 月 31 日前提供 2 美元/10 美元的入门折扣。但是……该模型采用了新的分词器，其中"相同的输入文本产生的 token 数量比 Claude Sonnet 4.6 多约 30%。"——实际上相当于价格上涨了 30%。我使用我的 Claude Token Counter 工具测试了新的分词器。以下是我对几个较大文档的测试结果：文档 Sonnet 4.6 Opus 4.7 Sonnet 5 世界人权宣言（英文）2,356 3,347 1.42 倍 3,341 1.42 倍 世界人权宣言（西班牙文）3,572 4,753 1.33 倍 4,747 1.33 倍 世界人权宣言（中文，简体普通话）3,334 3,366 1.01 倍 3,360 1.01 倍 sqlite_utils/db.py（4,279 行 Python 代码）44,014 56,118 1.28 倍 56,113 1.27 倍 所以

*（已截断，请参阅原文）*
