---
title: CrewAI
created: 2026-04-18
updated: 2026-04-20
type: entity
tags: [framework]
sources: [raw/articles/stackone-ai-agent-landscape-2026.md]
---

# CrewAI

## 概述

基于角色扮演范式的多智能体编排框架。智能体（"团队"）承担分配的角色、目标和工具，通过结构化交接进行协作。被评为与 LangGraph 并列的可靠生产级替代方案。

## 关键事实

- 4.4 万+ GitHub 星标
- 架构：基于角色的多智能体"团队"，目标驱动的任务委派
- 主要用途：快速原型开发和基于团队的智能体工作流
- 推荐：通过跨框架兼容性可用于 TypeScript 团队

## 为何出众

- 专注于**多智能体协作**而非单智能体编排
- 角色扮演范式使智能体行为直观且可组合
- 非常适合**快速原型开发**和研究用例
- 降低了多智能体模式的学习曲线

## 与其他实体的关系

- 与 [[langgraph]] 和 [[microsoft-autogen]] 在编排领域竞争
- 通过基于角色的团队模式解决 [[multi-agent-systems]]
- 广泛使用 [[tool-use]] 执行智能体操作
- 通过委派模式补充 [[agent-architecture-patterns]]
- 与 [[agent-protocols]]（MCP）配合实现外部工具访问

## 来源

- 在 [[stackone-ai-agent-landscape-2026]] 中排名："快速原型开发：CrewAI"
