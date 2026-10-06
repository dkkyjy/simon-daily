# 那么，你想使用 OpenRouter？

         **日期：** 2026-09-11 22:49 UTC
         **链接：** https://simonwillison.net/2026/Sep/11/so-you-want-to-use-openrouter/
         **标签：** ai, generative-ai, llms, openrouter

         ---

         > *摘要：那么，你想使用 OpenRouter？
OpenRouter 的卖点之一是它"能自动处理回退，并为每个请求选择最具性价比的选项"，因此你只需调用模型的单个 API 端*

2026年9月11日 - 链接博客

**[那么，你想使用 OpenRouter？](https://mmoustafa.com/blog/so-you-want-to-use-openrouter/)**（[via](https://news.ycombinator.com/item?id=49621546 "Hacker News")）OpenRouter 的卖点之一是它"能自动处理回退，并为每个请求选择最具性价比的选项"，因此你只需调用模型的单个 API 端点，即可被路由到最佳可用的后端服务商。

Mohamed Moustafa 指出，这种做法会带来一系列问题。不同的服务商运行不同的推理服务软件，具有不同的优化和配置，这意味着同一个 OpenRouter 端点所处理的模型请求可能表现出不同的行为。

一些服务商甚至缺乏对视觉模型的视觉能力支持，而且推理力度选项的处理方式也可能各不相同。

幸运的是，你可以使用 [provider.only 选项](https://openrouter.ai/docs/guides/routing/provider-selection#allowing-only-specific-providers) 来控制路由到哪个服务商。[/endpoints 方法](https://openrouter.ai/docs/api/api-reference/endpoints/list-all-endpoints-for-a-model) 可以返回特定模型 ID 的可用服务商列表。

发布于 [2026年9月11日](/2026/Sep/11/) 晚上 10:49
