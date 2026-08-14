---
title: 工具使用
created: 2026-04-18
updated: 2026-04-20
type: concept
tags: [tool-use]
sources: [raw/articles/stackone-ai-agent-landscape-2026.md]
---

# 工具使用

## 概述

智能体的工具使用层负责连接外部系统——终端、代码执行沙箱、浏览器、API 等。两种核心方法各自有其适用场景。

## 方法对比

| 方法 | 描述 | 优点 | 缺点 |
|---|---|---|---|
| **函数调用** | 预定义工具 Schema，LLM 通过参数调用 | 标准化、可靠 | 需手动注册每个工具 |
| **基于 MCP** | 通过 Model Context Protocol 动态发现工具 | 无需手动集成 | 仍需标准化 |

## 工具集成层职责

- **鉴权管理** — 认证、授权、凭证存储
- **合规** — 审计日志、操作限制
- **错误处理** — 工具失败后的重试与回退
- **计费** — 按调用计费的集成

## 关键趋势

- MCP（Model Context Protocol）正在成为工具发现的标准协议
- 工具集成层正成为智能体基础设施的独立层
- 生产环境中工具使用的可观测性至关重要

## 参见

- [[agent-protocols]] MCP 协议详解
- [[integration-infra]] 集成与鉴权层
- [[browser-automation]] 浏览器作为工具
- [[code-execution]] 沙箱代码执行
