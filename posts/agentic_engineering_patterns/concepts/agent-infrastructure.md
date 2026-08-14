---
title: 智能体基础设施
created: 2026-04-18
updated: 2026-04-20
type: concept
tags: [infrastructure]
sources: [raw/articles/stackone-ai-agent-landscape-2026.md]
---

# 智能体基础设施

## 概述

生产环境中的智能体需要在智能体框架本身之下有一层支撑层——记忆、可观测性、集成管理和推理路由。2026 年，工程复杂性的大部分就存在于这层基础设施中。

## 基础设施栈

### 集成与鉴权层

- **Nango** — 托管 OAuth、Webhook 和 API 集成
- **Arcade AI** — 智能体集成平台
- **StackOne** — 1 万+ 动作、200+ 连接器
- 处理：动态工具发现、托管鉴权、企业合规

### 记忆层

- **pgvector** — 数据库内向量存储，部署最简单
- **Pinecone** — 托管向量 DB，在 LangChain 生态中流行
- **Weaviate** — 混合语义/向量搜索
- **Mem0** — 专用记忆层（AWS 独家）
- **Zep** — 长期记忆的时间知识图谱

### 可观测性与评估

- **Langfuse**（被 ClickHouse 收购）— 可观测性 + 评估
- **Portkey** — 100 亿+ 请求/月规模
- **LangSmith** — LangChain 的评估平台
- **AgentOps** — 智能体监控和测试

### 推理与云

- **OpenRouter** — 多模型路由
- **LiteLLM** — 跨提供商的统一 API
- **Groq** — 亚秒级延迟推理
- **Modal** — 无服务器 GPU 部署
- **CoreWeave** — GPU 基础设施（估值超 230 亿美元）

## 关键基础设施趋势

1. **多提供商路由**已成为成本、延迟和可用性的标准
2. **智能体集成层区别于传统 iPaaS** — 专为动态发现设计
3. **基于执行/信用的定价**正在取代按席位模式以应对突增智能体工作负载
4. **专用记忆层正成为必选项** — 有记忆的智能体胜过零样本方案

## 参见

- [[tool-use]] 介绍工具如何接入此基础设施
- [[memory-systems]] 记忆层详情
- [[evaluation-benchmarks]] 评估/监控层
- [[agent-protocols]] 协议层
