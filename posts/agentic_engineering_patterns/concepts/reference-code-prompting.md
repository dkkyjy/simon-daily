---
title: 参考代码提示
created: 2026-04-11
updated: 2026-04-20
type: concept
tags: [tool-use, planning]
sources: [raw/articles/adding-a-new-content-type.md, raw/articles/adding-a-new-content-type_lecture.md]
---

# 参考代码提示

**参考代码提示**是一种高效指导编码智能体（如 Claude Code）完成复杂开发任务的方法论。其核心是：指示智能体克隆一个**相关的参考代码仓库**（而非直接描述逻辑），让智能体自行阅读和理解业务逻辑、数据模型及实现惯例，从而用极其简短的提示词完成原本需要大量文字解释的任务。

> Telling agents to use another codebase as reference is a powerful shortcut for communicating complex concepts with minimal additional information needed.

---

## 背景

Simon Willison 在为其博客转 Substack 通讯工具（Blog-to-Newsletter）添加"Beats"（动态）内容类型时，用以下**极简短提示**让 Claude Code 完成了一项复杂任务：

```
1. Clone simonw/simonwillisonblog from github to /tmp for reference
2. Update blog-to-newsletter.html to include beats that have descriptions - similar to how the Atom everything feed on the blog works
3. Run it with python -m http.server and use `uvx rodney --help` to test it - compare what shows up in the newsletter with what's on https://simonwillison.net
```

仅用 3 条指令，Claude Code 就成功添加了 UNION 子查询、推导了 beat_type 到正式名称的映射，并通过了活数据验证。

---

## 核心技巧分解

### 1. 克隆参考代码库

```
Clone <repo> from github to /tmp for reference
```

- **为什么到 `/tmp`**：防止智能体在后续提交中意外混入参考代码
- 参考仓库编码了领域惯例、ORM 模型定义、过滤逻辑和类型映射——这些用文字描述需要数十行提示
- 智能体通过阅读代码**自主发现**规则和映射，而非依赖用户解释
- 例如：智能体从 Django ORM 定义中推导出了 `beatTypeDisplay` 映射

### 2. 明确修改目标与逻辑参照

```
Update blog-to-newsloader.html to include beats that have descriptions
```

- 直接命名目标文件即可锁定范围——无需用户详细描述逻辑
- 智能体会自行检查参考代码库获取实现指导
- Simon Willison 利用了自己博客已存在的 Atom Feed 过滤逻辑作为参照（"有描述的动态"才会出现在 Feed 中），省去了描述逻辑的开销

### 3. 提供验证与测试机制

```
用 python -m http.server 运行它，并用 uvx rodney --help 测试——比对通讯结果与博客主页内容
```

- 编码智能体在有验证机制时表现最佳
- 要求智能体运行本地服务器（`python -m http.server`）而非文件协议（`file://`），避免因协议差异导致数据获取失败
- 要求智能体将新生成的内容与博客主页进行交叉验证——利用活数据作为"真理来源"

---

## 何时使用

| 场景 | 说明 |
|---|---|
| **应用现有代码库的模式** | 需要在智能体的代码库中套用参考仓库中的数据模型、约定或业务逻辑 |
| **理解领域术语** | 智能体需要掌握特定领域的术语体系和类型映射 |
| **工具已有参考实现** | 目标工具/功能在别处已有实现，可作为参考锚点 |
| **想从代码推导而非描述** | 用代码传达远比用自然语言精确高效 |

---

## 工具链

| 工具 | 用途 |
|---|---|
| **Claude Code** | 接收自然语言指令并执行代码修改的编码智能体 |
| **Datasette** | 博客内容的数据后端（SQL 驱动） |
| **python -m http.server** | 本地 HTTP 服务器，用于测试 Web 应用（避免 file:// 协议问题） |
| **uvx rodney** | 通过 `uvx` 安装的浏览器自动化工具，用于协助功能测试 |
| **GitHub** | 托管参考代码库，使智能体可克隆和读取 |

---

## 一句话要点

通过提供参考代码、明确目标并指示验证方法，可以用最简短的提示词指导智能体完成复杂的编程任务。

---

## 参见

- [[coding-agents]] — Claude Code 与自主编码智能体
- [[browser-automation]] — 使用 Rodney 等工具进行自动化交叉验证
- [[agent-architecture-patterns]] — 智能体交互模式的演进
- [[blog-to-newsletter]] — Blog-to-Newsletter 工具详情
