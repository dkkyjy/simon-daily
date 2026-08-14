---
title: 多智能体系统
created: 2026-04-18
updated: 2026-04-20
type: concept
tags: [multi-agent]
sources: [raw/articles/stackone-ai-agent-landscape-2026.md]
---

# 多智能体系统

## 概述

多智能体系统模式正成为生产环境的标准而非单智能体方案。核心问题不再是"是否需要多智能体"，而是"如何协调多个智能体"。

## 协调模式

| 模式 | 描述 | 适用场景 |
|---|---|---|
| **委派** | 编排者将子任务分配给子智能体 | 可分解任务 |
| **协作** | 智能体共享状态、协同解决 | 需要持续沟通的任务 |
| **编排者** | 中心化调度器路由工作 | 需要集中控制 |
| **对等方式** | 智能体直接相互通信 | 分布式、去中心化场景 |

## 参考实现

- [[crewai]] — 基于角色的多智能体"团队"
- [[microsoft-autogen]] — 对话式智能体组
- [[langgraph]] — 状态图模式的多智能体编排

## 关键挑战

- **通信开销** — 智能体间消息传递的成本
- **状态一致性** — 多智能体共享状态的同步
- **循环依赖** — 智能体之间相互等待导致的死锁
- **评估** — 如何评估多智能体协作的整体效果

## 趋势

- [[multi-agent-systems]] 正成为生产标准而非单智能方案
- [[agent-protocols]]（A2A）使多智能体间的动态路由成为可能

## 参见

- [[agent-architecture-patterns]] 架构模式
- [[agent-protocols]] 协议标准
- [[crewai]] CrewAI 框架
- [[microsoft-autogen]] Microsoft AutoGen
