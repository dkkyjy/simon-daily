**日期：** 2026-08-04 23:58 UTC
        **链接：** https://simonwillison.net/2026/Aug/4/new-release-of-llm/#atom-everything
        **标签：** projects, releases, ai, openai, generative-ai, llms, llm, anthropic, llm-tool-use, llm-reasoning, model-context-protocol

        ---

        > *订阅源摘要：我今天早上发布了 LLM 0.32，这是该项目自首次发布以来最重要的新版本。新版本包括对可见推理痕迹、服务端提供 t 的支持*

## LLM 新版本增加对推理痕迹、OpenAI Responses、服务端工具和更智能日志的支持

2026年8月4日

我今天早上发布了 [LLM 0.32](https://llm.datasette.io/en/stable/changelog.html#v0-32)，这是该项目自首次启动以来最重要的新版本。新版本包括对可见推理痕迹、服务端提供方工具、重新设计的内容寻址 SQLite 日志、新模型，以及由 OpenAI Responses API 带来的新功能的支持。我还发布了 [llm-anthropic 插件](https://github.com/simonw/llm-anthropic) 的一个新版本，该版本本身也有大量更新。

#### LLM CLI 用户的主要功能

现在，针对推理模型运行 LLM 会将其**推理痕迹**显示到标准错误中，这样你就可以看到它们在“思考”什么，而该信息不会包含在你可能通过管道传递给其他工具的标准输出中。添加 `-R/--hide-reasoning` 可关闭此功能。

LLM 开箱即用地支持 **GPT-5.6 模型系列**，而 `llm "prompt"` 现在使用的新的默认模型是价格低廉但功能强大的 **GPT-5.6 Luna**。

LLM 调用现在可以使用来自各种提供方的**服务端工具**。OpenAI 提供了[一个代码执行环境](https://llm.datasette.io/en/stable/openai-models.html#code-interpreter)作为服务端工具；LLM 现在可以运行受益于此的提示，如下所示：

```
llm --tool CodeInterpreter 'Show current python and SQLite versions'
```

OpenAI 还获得了一个 [WebSearch](https://llm.datasette.io/en/stable/openai-models.html#web-search) 工具。

[llm-anthropic](https://github.com/simonw/llm-anthropic) 插件新增了 [WebSearch](https://github.com/simonw/llm-anthropic/blob/0.26/README.md#web-search)、[WebFetch](https://github.com/simonw/llm-anthropic/blob/0.26/README.md#web-fetch)、[CodeExecution](https://github.com/simonw/llm-anthropic/blob/0.26/README.md#code-execution) 和 [AnthropicMCP](https://github.com/simonw/llm-anthropic/blob/0.26/README.md#mcp-connector)，如下所示：

```
llm -m claude-sonnet-5 -T 'AnthropicMCP("https://datasette.simonwillison.net/-/mcp")' \
  'how many rows in the blog_blogmark table?'
```

这会让 Anthropic 在与他们的 API 的单次请求/响应交互中，对我的新 [datasette-mcp](https://simonwillison.net/2026/Jul/31/stateless-mcp/#datasette-mcp) 插件执行 MCP 调用。

新的 **llm openai endpoint** 命令提供了一个工具，可用来以一行命令的形式[针对 *任何* 兼容 OpenAI 的端点执行提示](https://llm.datasette.io/en/stable/other-models.html#run-against-an-endpoint-without-configuring-it)。这些不会被记录，因此它是针对任何使用 LLM API 世界通用语言的服务运行一次性提示的便捷工具。

下面是我如何使用它，通过 `uvx`（无需安装 LLM）并混入 [llm-tools-quickjs](https://github.com/simonw/llm-tools-quickjs) 工具插件，来对运行在我本地主机 [LM Studio](https://lmstudio.ai) API 中的 Gemma 4 12B 运行提示：

```
uvx --with llm-tools-quickjs \
  llm openai endpoint http://localhost:1234/v1 -m google/gemma-4-12b \
  -T QuickJS 'Use QuickJS to multiply 3434 * 2434' --td
```

#### Python API 中的新功能

LLM 的 Python API 之前要求你先创建一个会话，然后一次一条地向其发送消息。这是对 LLM 真实本质的一种抽象——每次请求都携带之前所有消息的完整历史。这种抽象在一些更高级的用例中开始造成阻碍，因此新版本引入了 `model.prompt(messages=[])` 参数，可以这样使用：

```
import llm
from llm import user, assistant, system

model = llm.get_model("gpt-5.6-luna")

response = model.prompt(messages=[
    system("You are a helpful pirate."),
    user("What is the capital of France?"),
    assistant("Paris, matey."),
    user("And Germany?"),
])
print(response.text())
```

LLM 以前从每个提示返回一个可迭代的字符串序列。当模型返回字符串响应时，这非常有效，但未能预测模型将演化出的怪异形态。如今，许多模型返回的是推理文本、输出字符串、工具调用甚至图像附件的混合体。使用 LLM 0.32，你可以[改为这样做](https://llm.datasette.io/en/stable/python-api.html#structured-messages-and-streaming-events)：

```
for event in model.prompt("Explain cats").stream_events():
    if event.type == "reasoning":
        print(f"[thinking] {event.chunk}", end="", flush=True)
    elif event.type == "text":
        print(event.chunk, end="", flush=True)
    else:
        print(f"Other event: {event}")
```

将这些功能结合起来，我们*终于*可以提供一个健壮的、半标准的 OpenAI chat completions API 实现，我现在已将其作为 [llm-chat-completions-server](https://github.com/simonw/llm-chat-completions-server) 插件发布：

```
llm install llm-chat-completions-server
llm chat-completions-server --port 9000
# Server is now running on http://127.0.0.1:9000/v1
```

现在，你可以使用新的 `llm openai endpoint` 命令，通过该服务器运行针对 LLM 的提示！

```
llm openai endpoint http://127.0.0.1:9000/v1 'hello' -m gpt-5.4-mini
```

这类 API 面临的更大挑战与日志记录有关。如果我们要支持在每次请求时追加消息序列的模式，那么理想情况下，我们可以避免在每一轮都记录所有重复的 JSON。

解决方案是新的[内容寻址消息存储](https://llm.datasette.io/en/stable/logging.html#the-message-store)，仿照 Git 构建。你可以在[文档](https://llm.datasette.io/en/stable/logging.html#sql-schema)中查看新的架构，但 `llm logs` 和 `llm logs --json` 命令都已升级，可将该格式转换回易于使用的内容。

#### 其余更新

这个版本中还有更多内容。[0.32 版本说明](https://llm.datasette.io/en/stable/changelog.html#v0-32)相当全面，而 [0.32rc2](https://llm.datasette.io/en/stable/changelog.html#rc2-2026-07-30)、[0.32rc](https://llm.datasette.io/en/stable/changelog.html#rc1-2026-07-30)、[0.32a3](https://llm.datasette.io/en/stable/changelog.html#a3-2026-06-09)、[0.32a2](https://llm.datasette.io/en/stable/changelog.html#a2-2026-05-12) 和 [0.32a0](https://llm.datasette.io/en/stable/changelog.html#a0-2026-04-28) 的说明应该可以填补任何空白。

现有的 LLM 插件应该都能继续工作，但提供额外模型的插件需要升级到 0.32 才能完全参与新的流式事件系统。文档中有一份关于使用[结构化消息和流式事件](https://llm.datasette.io/en/stable/plugins/advanced-model-plugins.html#structured-messages-and-streaming-events)实现插件的指南。

我已经更新了我自己的一些插件：

* [llm-anthropic 0.26](https://github.com/simonw/llm-anthropic/releases/tag/0.26) 增加了对 Claude 5 模型系列的支持，以及 `WebSearch`、`WebFetch`、`CodeExecution` 和 `AnthropicMCP` 服务端工具。
* [llm-gemini](https://github.com/simonw/llm-gemini)、[llm-openrouter](https://github.com/simonw/llm-openrouter) 和 [llm-mistral](https://github.com/simonw/llm-mistral) 已接近完成，即将发布。

#### 我想 LLM 现在是一个智能体框架了

本次发布中不少底层工具更改是由 [Datasette Agent](https://agent.datasette.io/) 的需求驱动的。当我开始开发 LLM 时，“agent”一词的定义还非常模糊，以至于我拒绝使用它。在 [2025 年 9 月](https://simonwillison.net/2025/Sep/18/agents/)，我开始认同这样的观点：“**LLM 智能体通过循环运行工具来实现目标**” 这一说法现在已经足够成熟，我可以不再完全回避这个词了。

工具链现在可以[暂停等待人工批准](https://llm.datasette.io/en/stable/python-api.html#python-api-tools-pause)，也可以[从存储的消息历史中恢复](https://llm.datasette.io/en/stable/python-api.html#python-api-tools-resume)——这两者都是 Datasette Agent 所需要的。

如今看 LLM，它已经开始变得很有智能体的样子了。能有一个 CLI 实用程序，把来自不同来源的不同工具与不同模型以一行命令混搭在一起，还带有一个足够强大的 Python 库来构建像 [Datasette Agent](https://agent.datasette.io/) 和 [llm-coding-agent](https://github.com/simonw/llm-coding-agent) 这样的系统，这实在很妙。

也许下一版 LLM 会把“智能体”的概念融入核心库。我仍在尝试弄清楚那会是什么样子。

发布于 [2026年8月4日](/2026/Aug/4/) 晚上 11:58 · 在 [Mastodon](https://fedi.simonwillison.net/@simon)、[Bluesky](https://bsky.app/profile/simonwillison.net)、[Twitter](https://twitter.com/simonw) 上关注我，或[订阅我的新闻通讯](https://simonwillison.net/about/#subscribe)
