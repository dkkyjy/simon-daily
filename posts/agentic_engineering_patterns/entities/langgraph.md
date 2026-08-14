---
title: LangGraph
created: 2026-04-18
updated: 2026-04-20
type: entity
tags: [framework]
sources: [raw/articles/best-ai-agent-frameworks-2026-tier-list.md, raw/articles/stackone-ai-agent-landscape-2026.md]
---

# LangGraph

## 概述

构建有状态、多步智能体的开源框架，具有结构化编排能力。属于 LangChain 生态。被 Paolo Perrone 评为生产智能体构建 **S 级**框架。

## 关键事实

- 2.4 万+ GitHub 星标
- 架构：将智能体建模为有向状态图（节点为操作，边为转换）
- 创造者组织：LangChain / Harrison Chase
- 主要用途：需要精确控制流的复杂生产智能体工作流

## 为何出众

基于图的编排正在取代生产智能体的链式模式。LangGraph 的状态图模型提供了：

- **可视化调试**——`graph.get_graph().draw_mermaid()` 揭示整个决策树
- **确定性控制流**——节点间显式边，无隐藏状态变更
- **结构化编排**——通过有向无环图实现 [[agent-architecture-patterns]]

## 与其他实体的关系

- 属于更广泛的 [[langchain]] 生态
- 与 [[crewai]]、[[microsoft-autogen]] 和厂商专属 SDK 竞争
- 使用 [[agent-architecture-patterns]]（状态图模型）
- 配合 [[tool-use]] 执行智能体操作
- 需要 [[memory-systems]] 来实现超越图状态的持久化
- 通过 [[agent-protocols]] 生态运行

## 来源

- 在 [[best-ai-agent-frameworks-2026-tier-list]] 中评为 S 级
- 在 [[stackone-ai-agent-landscape-2026]] 中被列为主要代码优先框架
