# 使用 DSPy 评估和改进 Datasette Agent 的 SQL 系统提示

**日期：** 2026-07-02 18:25 UTC
**链接：** https://simonwillison.net/2026/Jul/2/dspy-datasette-agent-prompts/#atom-everything
**标签：** ai, datasette, generative-ai, llms, evals, dspy, datasette-agent, claude-mythos-fable

---

研究：使用 DSPy 评估和改进 Datasette Agent 的 SQL 系统提示 今天早上的 AIE 主题演讲之一介绍了 dspy，这提醒我一直想看看它是否能帮助我改进 Datasette Agent 使用的系统提示——因此我使用 Claude Fable 5 在 Claude Code for web 中启动了一项异步研究任务：Pip 安装最新的 Datasette alpha 版本、datasette-agent 和 dspy——然后弄清楚如何使用 dspy 评估和改进 Datasette Agent 用于执行只读 SQL 查询以回答用户关于数据的问题这一功能的主要系统提示。Fable 选择使用 GPT 4.1 mini 和 nano 进行测试，并确定了几个有前景的改进方向。我特别喜欢这一点：模式列表只给出了表名；"如果你已经拥有信息，不要调用 describe_table" 的建议导致了列名猜测（page_count、o.order_id、first_name）和基线追踪中的错误重试循环。要么在提示的模式列表中包含列名，要么软化这条建议。标签：ai , datasette , generative-ai , llms , evals , dspy , datasette-agent , claude-mythos-fable
