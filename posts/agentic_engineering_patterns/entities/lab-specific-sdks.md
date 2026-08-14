---
title: 厂商专属 SDK
created: 2026-04-18
updated: 2026-04-20
type: entity
tags: [framework]
sources: [raw/articles/stackone-ai-agent-landscape-2026.md]
---

# 厂商专属 SDK

## 概述

每个主要 AI 模型提供商（OpenAI、Google、Anthropic）都提供自己的智能体构建 SDK。这些 SDK 与各自模型提供最紧密的集成，但会造成厂商锁定。

## 主要 SDK

- **OpenAI Agents SDK** — 与 OpenAI 模型最紧密的集成
- **Google ADK**（Agent Development Kit）— Google 的智能体框架
- **Anthropic Agent SDK** — 原生 Claude 智能体构建工具

## 使用场景

- **最紧密的厂商集成** — 直接访问模型能力
- **最低延迟** — SDK 与模型 API 之间无抽象层
- **最前沿特性** — 新模型功能立即可用

## 避免原因

- **厂商锁定** — 在提供商间迁移需要完全重写
- **生态有限** — 跨平台框架的集成更多
- **单一模型聚焦** — 多模型路由需要手动编排

## 场景

根据 [[stackone-ai-agent-landscape-2026]]："厂商锁定/集成：厂商专属 SDK"——当深度模型集成是主要需求且不需要多提供商灵活性时选择这些。

## 与其他实体的关系

- 与 [[langgraph]]、[[crewai]] 和 [[microsoft-autogen]] 在框架领域竞争
- 使用 [[agent-protocols]]（尤其是 MCP）减少厂商锁定
- 配合 [[tool-use]] 实现外部集成
- 需要 [[memory-systems]] 来实现超越 API 会话的持久化
