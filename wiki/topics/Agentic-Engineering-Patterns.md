---
type: topic
title: Agentic Engineering Patterns
description: "Simon Willison 的 Agentic Engineering 指南系列，定义 AI 编程代理时代的工程范式"
created: 2026-04-10
updated: 2026-05-28
tags:
  - AI-Agent
  - coding-agents
  - best-practices
related_entities:
  - '[[Agentic-Engineering]]'
  - '[[Coding-Agents]]'
  - '[[Code-Execution]]'
  - '[[Compound-Engineering]]'
  - '[[Dominator-Analysis]]'
  - '[[Raj-Nandan-Sharma]]'
  - '[[Simon-Willison]]'
  - '[[Technical-Debt-Avoidance]]'
  - '[[Vibe-Coding]]'
  - '[[Harness-Engineering]]'
  - '[[Agent-Harness]]'
  - '[[AI-First]]'
  - '[[Agentic-Workflow-Token-Efficiency]]'
  - '[[Laziness-Virtue]]'
  - '[[AI-Lacks-Laziness]]'
  - '[[AI-Restraint]]'
  - '[[YAGNI]]'
  - '[[ITBench]]'
source_raw:
  - '[[What is agentic engineering? - Agentic Engineering Patterns]]'
  - '[[20260410-code-is-cheap]]'
  - '[[20260410-hoard-things-you-know]]'
  - '[[20260410-better-code]]'
  - '[[20260410-anti-patterns]]'
  - '[[20260413-why-ai-first-strategy-wrong]]'
  - "[[Validating agentic behavior when “correct” isn’t deterministic]]"
  - "[[The Anatomy of an Agent Harness]]"
  - "[[Improving token efficiency in GitHub Agentic Workflows]]"
  - "[[20260414-martin-fowler-fragments]]"
  - "[[Agent pull requests are everywhere. Here's how to review them.]]"
  - "[[The PR you would have opened yourself]]"
  - "[[ITBench-AA Frontier Models Score Below 50% on the First Benchmark for Agentic Enterprise IT Tasks — by Artificial Analysis and IBM]]"
  - "[[Coding agents in the social sciences]]"
  - "[[Using LLMs to secure source code]]"
---

# Agentic Engineering Patterns

> **作者**：Simon Willison
> **定位**：识别能产生实际结果、且不会因工具进步而过时的模式

## 核心定义

**Agentic Engineering** 是使用 Coding Agents 辅助开发软件的实践。

### Agent 定义

> **Agents run tools in a loop to achieve a goal**

- 调用 LLM，传入 prompt 和工具定义
- 执行 LLM 请求的工具
- 将结果反馈给 LLM
- 循环直到目标达成

### Coding Agents

能**编写和执行代码**的 agents：

- Claude Code
- OpenAI Codex
- Gemini CLI

---

## 指南章节

### Principles（原则）

| 章节 | 核心观点 |
|------|---------|
| **What is agentic engineering** | Code Execution 是决定性能力 |
| **Writing code is cheap now** | 代码成本从昂贵到几乎免费 |
| **Hoard things you know** | 囤积可运行代码示例作为资产 |
| **AI should help produce better code** | 用助手预防技术债务 |
| **Anti-patterns** | 不要提交未审查的代码 |

### Working with Coding Agents

| 章节 | 核心观点 |
|------|---------|
| **Using Git** | Agent 深度理解 Git，可处理复杂操作 |
| **Subagents** | 并行代理处理独立任务 |

### Testing and QA

- Red/green TDD
- First run the tests
- Agentic manual testing
- **[[Dominator-Analysis|Dominator Analysis]] 验证 Agent 行为**: 将编译器理论中的支配者分析应用于 Agent 执行图，自动区分 essential states 与 optional noise。
- **少量 trace 建模**: 仅需 2-10 次成功 trace 即可构建 ground truth。实验 F1=100% vs Agent 自评 69.8%。
- **来源**: [[Validating agentic behavior when “correct” isn’t deterministic|GitHub Blog: Validating Agentic Behavior]]

### Cost and Observability

- **[[Agentic-Workflow-Token-Efficiency|Token Efficiency]]**: 生产级 Agentic Workflow 不能只问“能否完成任务”，还要问每次自动触发是否在消耗不可见成本。
- **可优化系统**: GitHub 的实践显示，API 代理记录、每日 token 审计、MCP 工具裁剪和 CLI 替代，能把 Agent 工作流从黑盒花费变成可优化系统。
- **确定性前置**: 许多 agent turns 只是数据读取，不需要推理。把 PR diff、文件列表、issue 元数据等提前用 CLI 写入工作区，可以把确定性读取移出 LLM 循环。
- **质量混淆**: token 下降不必然代表效率提升，也可能是工作做少了；需要同时看模型层级、工作负载、turn 数、工具完成率和结果质量。

---

## 核心洞察

### Code Execution 是关键

> [!important] 决定性能力
> 没有 Code Execution，LLM 输出价值有限。
> 有了 Code Execution，Agent 可以迭代出**可验证工作的软件**。

### 代码成本范式转变

```
传统：生产几百行代码需要一天
现在：编码代理几乎免费产出代码
```

**影响**：
- 重估所有权衡决策
- 对代码异味零容忍
- 异步代理后台重构

### 知识囤积

收集可运行代码示例的价值：

- 维护博客/TIL 记录解决方案
- GitHub repos 作为概念验证
- HTML tools 集合
- 用 prompt 指引 Agent 组合现有示例

### 复合工程

```
项目完成 → 回顾 → 记录有效做法 → 未来运行使用
```

小改进复合，编码助手意味着**可以兼得新功能 + 高质量**。

### AI 也需要懒惰和克制

[[20260414-martin-fowler-fragments]] 补充了一个反向原则：AI 不应把所有摩擦都解释为“需要生成更多代码”。Fowler 通过 [[YAGNI]] 经验提醒，很多好设计来自少做、晚做或不做。

[[Laziness-Virtue]] 在这里不是程序员笑话，而是质量控制机制：人类时间有限，所以会主动寻找更少代码、更低认知负担和更清楚抽象。[[AI-Lacks-Laziness]] 指出，LLM 默认没有这种未来维护痛感，容易把系统做大而不是做好。

同一组 fragments 也强调 [[AI-Restraint|克制]]：在错误代价不对称的场景里，正确行为可能是延迟行动、要求更多证据或转人工。Agentic Engineering 因此不只是让 agent 更能做事，也要设计 agent 何时不做。

---

## 与 Vibe Coding 的区别

| 维度 | Vibe Coding | Agentic Engineering |
|------|-------------|---------------------|
| 代码质量 | 原型级 | 生产级 |
| 审查程度 | 无 | 深度审查 |
| 验证方式 | 凭感觉 | 自动测试 |
| 目标 | 快速原型 | 可工作软件 |

> [!warning] 保持区分
> 不要把 Vibe Coding 扩展为"任何 LLM 生成代码"。
> 保持原意：**未经审查、原型质量的 LLM 生成代码**。

## Agent PR 的证据负担

Agentic Engineering 不能把生成成本下降变成 review 成本转嫁。[[Agent-PR-Review|Agent PR Review]] 和 [[Agent-Generated-PRs|Agent-Generated PRs]] 共同指向一个规则：AI 可以帮你更快产出 PR，但不能让维护者替你完成理解、验证和责任承担。

好的 Agent PR 至少要留下四类证据：

- 它为什么解决正确问题，而不是只解决表面 issue。
- 它如何被验证，包括测试、运行截图、数值对比或可复现实验。
- 它是否显式披露 agent-assisted，避免维护者误判上下文。
- 它是否足够小，能被人类在合理时间内审查。

这把 Agentic Engineering 与 Vibe Coding 再次区分开：前者降低生成摩擦，但提高证据标准；后者把“看起来能跑”当成完成。

---

## 相关主题

- [[Coding-Agents]] - 工具层面
- [[Agent-Workflow-Patterns]] - 架构模式
- [[ACI-Agent-Computer-Interface]] - 接口设计

## Agentic Engineering 到 Harness Engineering 的演进

| 阶段 | 核心问题 | 解决方案 | 来源 |
|------|---------|---------|------|
| **Agentic Engineering** | Agent 如何有效运行工具循环？ | Code Execution + TDD + Git Fluent | Simon Willison |
| **AI-First** | 如何围绕 AI 重建组织？ | 流程重设计 + 全职能 AI 原生 | CREAO / Peter Pang |
| **Harness Engineering** | 如何让 Agent 成为主要构建者？ | Monorepo + 自愈循环 + 6 阶段 CI/CD | OpenAI (2026.02) + CREAO |
| **Agent Harness** | Harness 的技术架构是什么？ | 12 组件 + 7 架构决策 + 脚手架隐喻 | Akshay Pachaar (综合分析) |

> [!quote] CREAO CTO Peter Pang
> "You build the system. The prompts are disposable."

## 参见

- [[Raj-Nandan-Sharma]] - AI Agent 实践文章作者
- [[Simon-Willison]] - Agentic Engineering 指南作者
- [[Technical-Debt-Avoidance]] - Agentic Engineering 核心模式：用助手预防技术债务
- [[Harness-Engineering]] - 让 Agent 成为主要构建者的完整系统框架
- [[Agent-Harness]] - Harness 的 12 组件 + 7 架构决策技术框架
- [[AI-First]] - 组织级 AI 优先范式
- [[Agentic-Workflow-Token-Efficiency]] - Agentic Workflow 的成本可观测与优化方法
- [[Laziness-Virtue]] - 用有限时间倒逼简化的工程美德
- [[AI-Lacks-Laziness]] - AI 默认缺少简化压力带来的质量风险

---

> **来源**：Simon Willison, [Agentic Engineering Patterns Guide](https://simonwillison.net/guides/agentic-engineering-patterns/)
>
> **案例来源**：Peter Pang (CREAO CTO), [Why Your "AI-First" Strategy Is Probably Wrong](https://x.com/intuitiveml/status/2043545596699750791), 2026-04-13
