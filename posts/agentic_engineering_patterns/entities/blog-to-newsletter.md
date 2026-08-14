---
title: Blog-to-Newsletter
created: 2026-04-11
updated: 2026-04-20
type: entity
tags: [tool]
sources: [raw/articles/adding-a-new-content-type.md]
---

# Blog-to-Newsletter

## 概述

Simon Willison 开发的工具，将博客转 Substack 通讯工具。从 Datasette 实例获取内容并格式化为富文本 HTML，供粘贴到 Substack 编辑器。

## 工作原理

- **目的**：桥接博客文章到电子邮件通讯分发
- **机制**：通过 SQL 查询获取最新内容，渲染为 HTML
- **分发**：内容复制到剪贴板，粘贴到 Substack 编辑器
- **内容类型**：支持博客文章、Beats（外部内容）及其他策划类型

## 技术架构

### 数据源
- 由 simonw/simonwillisonblog 驱动（Django + Datasette）
- "Beats"功能收录发布在其他地方的内容（开源发布、新工具、博物馆等）
- Beats 可选添加评论/笔记来排名重要性

### 通讯生成
- `simonw/tools` 中的 HTML/JavaScript 应用
- 使用 SQL `UNION` 查询组合内容类型（文章 + Beats + 其他）
- 过滤掉草稿和无评论的 Beats
- 将内容类型简写映射为显示名称（如 `release` → `发布`，`museum` → `博物馆`）

## 与智能体工程的关系

该工具是 [[reference-code-prompting]] 的实战案例：Simon Willison 演示了如何通过提供参考代码库、明确文件目标和对照实时博客进行交叉验证，有效地提示编码智能体（Claude Code）来扩展此工具。

## 相关

- [[reference-code-prompting]] — 用此工具演示的提示技巧
- [[coding-agents]] — 修改此工具使用的智能体
