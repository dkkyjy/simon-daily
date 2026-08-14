---
title: 评估智能体
created: 2026-04-18
updated: 2026-04-20
type: concept
tags: [evaluation]
sources: [raw/articles/stackone-ai-agent-landscape-2026.md, raw/articles/adding-a-new-content-type.md]
---

# 评估智能体

## 概述

智能体评估不同于传统 API 评估——智能体的输出不是一个文本响应，而是一系列通过工具执行的动作及其结果。因此评估需要专门维度和工具。

## 评估维度

- **任务完成率** — 智能体是否成功完成给定目标
- **工具正确性** — 工具调用是否准确、参数是否正确
- **可靠性** — 多次运行的结果一致性
- **效率** — 完成任务所需的 token 数和步骤数
- **安全性** — 是否在安全边界内操作

## 评估工具

- **Langfuse / LangSmith** — 可观测性与评估管线
- **AgentOps** — 智能体监控和测试
- **Portkey** — 大规模请求监控

## 实践要点

- 智能体评估需要**多轮对话**的完整上下文
- 工具调用的正确性需要结合**执行结果**来评估
- 生产环境中应持续监控而非仅做离线评估

## 参见

- [[agent-infrastructure]] 关于评估基础设施
- [[tool-use]] 关于工具调用的评估
- [[agent-protocols]] 关于可观测性标准
