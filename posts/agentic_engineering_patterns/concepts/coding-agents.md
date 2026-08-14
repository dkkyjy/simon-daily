---
title: 编码智能体
created: 2026-04-18
updated: 2026-04-20
type: concept
tags: [agent-pattern]
sources: [raw/articles/stackone-ai-agent-landscape-2026.md]
---

# 编码智能体

## 概述

编码工具已分化为两种模式：**辅助模式**（copilot，人机协作）和**自动驾驶模式**（autopilot，自主完成任务）。Claude Code 是该领域的领先者，已占据约 4% 的公开 GitHub 提交。

## 两种模式的对比

| 维度 | 辅助模式 (Copilot) | 自动驾驶模式 (Autopilot) |
|---|---|---|
| 自主程度 | 低 — 人工确认每个操作 | 高 — 自动执行并验证 |
| 适用场景 | 代码补全、小型重构、解释 | 全功能开发、复杂调试、任务修复 |
| 风险 | 低 — 人工始终在环 | 较高 — 需充分测试护栏 |
| 代表工具 | GitHub Copilot, Cursor | Claude Code, Devin |

## 为何自动驾驶模式是未来

- 公开 GitHub 提交中约 4% 由 Claude Code 驱动，显示生产采用率
- 从"辅助"到"自主"的范式转变正在加速
- 编码能力是最容易评估的智能体能力（代码正确性可测试）
- 为更广泛的智能体自主提供了样板

## 与其他概念的关系

- 是 [[agent-architecture-patterns]] 中"自动驾驶"趋势的体现
- 依赖于 [[tool-use]]（终端、编辑器、版本控制）和 [[code-execution]]（沙箱验证）
- 是 [[coding-agent-evolution]] 的核心案例
- 与 [[claude-code]]、[[cursor]]、[[devin]] 和 [[openhands]] 紧密相关

## 参见

- [[claude-code]] Claude Code 实体页
- [[agent-architecture-patterns]] 架构模式
- [[tool-use]] 工具集成
- [[evaluation-benchmarks]] 编码智能体评估
