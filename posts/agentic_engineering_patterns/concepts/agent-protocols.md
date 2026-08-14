---
title: 智能体协议
created: 2026-04-18
updated: 2026-04-20
type: concept
tags: [infrastructure]
sources: [raw/articles/stackone-ai-agent-landscape-2026.md]
---

# 智能体协议

## 概述

智能体生态已收敛于一套"协议三件套"——每个生产智能体系统必须实现的三个互操作性标准。

## 协议三件套

| 协议 | 目的 | 状态 |
|---|---|---|
| **MCP（Model Context Protocol）** | 智能体到工具的连接 | 已捐献给 Linux 基金会 |
| **A2A（Agent-to-Agent）** | 智能体到智能体的通信 | 已捐献给 Linux 基金会；吸收 IBM 的 ACP |
| **AG-UI（Agent-User Interaction）** | 智能体到用户的交互标准 | 新兴标准 |

## MCP（Model Context Protocol）

- **目的**：将智能体连接到工具、数据源和外部服务
- **模式**：智能体与外部资源间的工具 Schema 共享
- **影响**：任何智能体都可使用任何 MCP 兼容工具，无需自定义集成

## A2A（Agent-to-Agent）

- **目的**：使自主智能体能发现、通信和协作
- **历史**：吸收 IBM 的 ACP（Agent Communication Protocol）作为统一标准
- **影响**：智能体现在可以动态在智能体间路由工作，而非硬连线

## AG-UI（Agent-User Interaction）

- **目的**：标准化用户与智能体的交互方式（输入、输出、审批节点）
- **影响**：跨不同智能体实现的一致用户体验

## 协议为何重要

如果没有标准协议，每个智能体框架都需要为每个工具、数据源和用户交互模式做自定义集成。协议三件套实现了：

1. **可组合性** — 基于不同框架的智能体可以协同工作
2. **工具复用** — 编写一次 MCP 服务器，配合任何智能体框架
3. **智能体互操作性** — 跨组织在智能体间路由工作
4. **基础设施独立** — 智能体不被锁定到单一供应商

## 参见

- [[langgraph]] 使用 MCP 进行工具访问
- [[crewai]] 配合 MCP 协议工作
- [[agent-architecture-patterns]] 了解协议如何融入智能体设计
- [[infrastructure]] 了解协议在整个栈中的位置
