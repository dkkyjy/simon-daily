---
title: 智能体工程 Wiki 模式
---

# Wiki 模式

## 领域

智能体工程——在生产系统中构建、部署和编排 AI 智能体的系统化研究与实践。涵盖智能体架构、框架、工具使用、规划、记忆、多智能体系统、评估、安全和实际部署模式。

## 约定

- 文件名：小写、连字符分隔、不含空格（如 `tool-use-patterns.md`）
- 每个 Wiki 页面以 YAML frontmatter 开头（见下文）
- 使用 `[[wikilinks]]` 在页面间链接（每页至少 2 条出站链接）
- 更新页面时，务必更新 `updated` 日期
- 每个新页面必须按正确分类添加到 `index.md`
- 每个操作必须追加到 `log.md`
- 页面位于当前目录（非 ~/wiki）

## Frontmatter

```yaml
---
title: 页面标题
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [来自下方分类法]
sources: [raw/articles/source-name.md]
---
```

## 标签分类法

### 架构
- **agent-pattern** — 智能体架构模式（ReAct、Plan-and-Execute 等）
- **multi-agent** — 多智能体系统与协调
- **framework** — 构建智能体的框架和工具包
- **infrastructure** — 基础设施、部署或运行时相关

### 能力
- **tool-use** — 工具调用和函数调用
- **planning** — 规划与推理
- **memory** — 短期、长期或工作记忆
- **orchestration** — 工作流编排与控制流

### 数据与集成
- **api-integration** — 连接外部 API 和服务
- **code-execution** — 沙箱代码执行（E2B 等）
- **data-access** — 数据库、向量存储、知识检索
- **human-in-the-loop** — 审批节点与人类监督

### 评估与安全
- **evaluation** — 评估框架、基准、指标
- **safety** — 安全、护栏或隔离
- **observability** — 监控、追踪、调试

### 人物与来源
- **company** — 从事智能体工程的公司
- **researcher** — 关键研究人员或思想领袖
- **paper** — 基石性或有影响力的论文
- **article** — 有影响力的文章或博客
- **tool** — 特定工具或库

## 页面阈值

- **创建页面**：当一个实体/概念出现在 2+ 个来源中，或是某个来源的核心内容时
- **添加到已有页面**：当一个来源提及已覆盖的内容时
- **不要创建页面**：传递性提及、次要细节或超出领域范围的内容
- **拆分为**超过 ~200 行的页面——拆入子主题并交叉链接
- **归档页面**：当内容被完全取代——移到 `_archive/`，从索引中移除

## 实体页面

每个重要实体建一个页面，包含：
- 概述 / 它是什么
- 关键事实与日期
- 与其他实体的关系（`[[wikilinks]]`）
- 来源引用

## 概念页面

每个概念或主题建一个页面，包含：
- 定义 / 解释
- 当前知识状态
- 待解决的问题或争议
- 相关概念（`[[wikilinks]]`）

## 对比页面

并排分析。包含：
- 对比什么及为什么
- 对比维度（优先使用表格格式）
- 结论或综合
- 来源

## 更新政策

当新信息与现有内容冲突时：
1. 检查日期——较新的来源通常取代较旧的内容
2. 如果确实矛盾，记录两种立场及其日期和来源
3. 在 frontmatter 中标记矛盾：`contradictions: [page-name]`
4. 在 lint 报告中标记给用户审核
