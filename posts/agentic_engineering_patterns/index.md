# 智能体工程 Wiki

> 内容目录。每个 Wiki 页面按类型分类，附一行摘要。
> 查询时首先阅读此文件以找到相关页面。
> 最后更新：2026-04-20 | 总页面数：18

## 实体

- [[claude-code]] — Claude Code；Claude Code 是 Anthropic 发布的 CLI 编码智能体
- [[crewai]] — CrewAI；基于角色的多智能体编排框架，快速原型开发
- [[lab-specific-sdks]] — 厂商专属 SDK（OpenAI Agents SDK、Google ADK、Anthropic Agent SDK）；深度集成但存在厂商锁定风险
- [[langchain]] — LangChain；最初的 & 最大的 LLM 框架（12.6 万星）；生态系统的基石层
- [[langgraph]] — LangGraph；有向状态图框架（S 级）；可视化调试，显式控制流
- [[microsoft-autogen]] — Microsoft AutoGen；微软 Conversational Agent 框架；与 Semantic Kernel 合并
- [[blog-to-newsletter]] — Blog-to-Newsletter；Simon Willison 的博客转 Substack 通讯工具；Datasette + SQL → HTML

## 概念

- [[agent-architecture-patterns]] — 从链式到状态图；核心架构模式（ReAct、有向无环图、基于角色的多智能体）
- [[agent-infrastructure]] — 智能体基础设施：记忆、可观测性、集成与推理层
- [[agent-protocols]] — 协议三件套：MCP（智能体到工具）、A2A（智能体到智能体）、AG-UI（智能体到用户）
- [[browser-automation]] — 智能体的浏览器自动化：视觉大模型（Skyvern）对比 DOM 方案（Playwright MCP）
- [[coding-agents]] — 编码智能体：工具分化为辅助模式 vs 自动驾驶模式；Claude Code 领先
- [[evaluating-agents]] — 评估智能体：智能体专用评估工具与维度（任务完成、工具正确性、可靠性）
- [[memory-systems]] — 记忆系统：工作记忆、情景记忆、语义记忆和程序性记忆；专用记忆层正成为标准
- [[multi-agent-systems]] — 多智能体系统：委派、协作、编排者和对等方式
- [[reference-code-prompting]] — 参考代码提示：克隆参考代码库以最少提示传达复杂上下文
- [[tool-use]] — 工具使用：函数调用 vs 基于 MCP 的工具发现；鉴权与合规集成层

## 对比

- [[framework-comparison]] — LangGraph、CrewAI、LangChain、AutoGen、Mastra 并排对比与排名

## 查询
