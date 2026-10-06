# 引用 Felix Rieseberg

         **日期：** 2026-10-05 23:56 UTC
         **链接：** https://simonwillison.net/2026/Oct/5/felix-rieseberg/
         **标签：** claude-cowork, anthropic, claude, generative-ai, ai, general-agents, llms

         ---

         > *Feed 摘要：Cowork 的"旧"版本在云端运行模型推理，并在我们发送到您电脑上的 Anthropic 提供的 VM 中执行工具调用。我们添加 VM 是为了能力、安全和安全原因*

2026 年 10 月 5 日

> Cowork 的"旧"版本在云端运行模型推理，并在我们发送到您电脑上的 Anthropic 提供的 VM 中执行工具调用。我们添加 VM 是为了能力、安全和安全原因——仅映射您明确添加到会话中的数据。人们喜欢他们能用 Claude 做的事情，但不喜欢本地运行 VM 带来的磁盘、电池和性能成本。此外，人们不喜欢关闭笔记本电脑意味着工作停止。
>
> Cowork 的"新"版本在云端运行模型推理和 VM。每个会话都有自己的沙盒，不与其他会话共享状态。当 VM 需要用户设备上的某些内容（如文件）时，桌面应用负责该文件访问工具调用。[...]
>
> 我们认为这解决了很多我们听到的问题（比如从手机使用 Cowork、保持工作运行，或在失去 VM 电池的情况下获得同样的能力）

— [Felix Rieseberg](https://twitter.com/felixrieseberg/status/2107206431376334975)，Anthropic，另见[此帮助页面](https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile#h_f951c27c48)

发布于 [2026 年 10 月 5 日](/2026/Oct/5/) 晚上 11:56
