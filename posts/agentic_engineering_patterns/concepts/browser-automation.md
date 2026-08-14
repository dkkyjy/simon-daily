---
title: 智能体的浏览器自动化
created: 2026-04-18
updated: 2026-04-20
type: concept
tags: [tool-use]
sources: [raw/articles/stackone-ai-agent-landscape-2026.md]
---

# 智能体的浏览器自动化

## 概述

智能体需要具备真实的网页交互能力——填写表单、读取内容、导航多步骤流程。浏览器自动化正成为在 Web 界面这一物理世界中操作的智能体系统的关键基础设施。

## 方法对比

| 方法 | 工具 | 描述 |
|---|---|---|
| 视觉大模型 | [[skyvern]] | AI 像人类一样从视觉上读取网页 |
| 基于 DOM | [[playwright-mcp]] | 通过 DOM 结构化访问页面元素 |
| 爬虫聚焦 | [[crawl4ai]] | 高吞吐量内容提取 |
| 浏览器控制 | [[browser-use]] | 直接浏览器自动化配合智能体决策循环 |

## 关键权衡

- **视觉方案**处理动态/Canvas 内容，适用于任何网站（无需 API）
- **DOM 方案**对于文字密集型交互更快更可靠
- 两者共存是因为网页结构差异极大

## 生产考虑

- 速率限制与反爬虫检测
- CAPTCHA 处理
- 跨会话状态管理
- 法律与合规问题

## 参见

- [[tool-use]] 关于更广泛工具集成模型
- [[agent-protocols]] — Playwright MCP 提供工具访问
- [[integrations-infra]] 关于鉴权与合规层
