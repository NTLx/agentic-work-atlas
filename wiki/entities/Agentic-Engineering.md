---
type: entity
title: Agentic Engineering
aliases:
  - Agentic Engineering
  - Agentic Coding
  - 代理式工程
definition: "用 coding agents 辅助开发软件的工程实践；Simon Willison 系统化了 code execution、测试和反模式等实践，Karpathy 则将其与 Vibe Coding 区分为保持专业质量上限的严肃工程纪律"
created: 2026-04-09
updated: 2026-05-22
tags:
  - AI-Agent
  - Software-Engineering
  - Development-Paradigm
related_entities:
  - '[[Code-Execution]]'
  - '[[Coding-Agents]]'
  - '[[Vibe-Coding]]'
  - '[[Harness-Engineering]]'
  - '[[Agent-Harness]]'
  - '[[Compound-Engineering]]'
  - '[[Git-Fluent-Agents]]'
  - '[[Security-Hardening-Phase]]'
  - '[[Adversarial-Distillation]]'
  - '[[Verifiability]]'
  - '[[Software-3.0]]'
  - '[[Jagged-Intelligence]]'
  - '[[Agent-PR-Review]]'
  - '[[Agentic-Workflow-Token-Efficiency]]'
  - '[[渐进式重构]]'
  - "[[Essential-Complexity]]"
  - "[[Friction-as-Design-Signal]]"
source_raw:
  - '[[Andrej Karpathy: From Vibe Coding to Agentic Engineering]]'
  - '[[Using Git with coding agents - Agentic Engineering Patterns]]'
  - '[[What is agentic engineering? - Agentic Engineering Patterns]]'
  - '[[20260413-why-ai-first-strategy-wrong]]'
  - '[[20260409-ai-capability-gap-ai-psychosis]]'
  - "[[20260127-claude-coding-notes]]"
  - "[[20260414-cybersecurity-proof-of-work]]"
  - '[[工程师抗拒被"蒸馏"，企业的Skills从何而来？五大招破局]]'
  - '[[The Anatomy of an Agent Harness]]'
  - "[[MachinaCheck Building a Multi-Agent CNC Manufacturability System on AMD MI300X]]"
  - "[[Why I Don’t Vibe Code]]"
---

# Agentic Engineering

> [!definition] 定义
> **Agentic Engineering** 是使用 Coding Agents 辅助开发软件的实践。

## 核心定义

> **Agents run tools in a loop to achieve a goal**

这里采用 Simon Willison 的操作性定义：Agentic Engineering 是使用 coding agents 辅助开发软件的实践。Karpathy 在 2026 年 Sequoia 演讲中补充了更强的边界：Vibe Coding 提升所有人的软件能力底线，而 Agentic Engineering 要在不牺牲安全、可靠和专业质量的前提下获得更高杠杆。

Agent 软件：
1. 调用 LLM，传入用户提示和工具定义
2. 执行 LLM 请求的工具
3. 将结果反馈给 LLM
4. 循环直到目标达成

### Code Execution：决定性能力

> [!important] 核心洞察
> **Code Execution is the defining capability that makes agentic engineering possible.**
> 
> 没有直接运行代码的能力，LLM 输出价值有限。
> 有了 Code Execution，Agent 可以迭代出**可验证工作的软件**。

## 核心原则（Simon Willison）

| 原则 | 说明 | 实践意义 |
|-----|------|---------|
| **Writing code is cheap now** | 代码成本趋近于零 | 可以更雄心勃勃地尝试 |
| **Hoard things you know how to do** | 囤积可运行代码示例 | 记录可复用的解决方案 |
| **AI should help produce better code** | AI 应帮助产出更好的代码 | 不是更快，而是更好 |
| **Anti-patterns** | 不要提交未审查的代码 | 你的工作是交付能工作的代码 |

## 与 Vibe Coding 的区别

| 维度 | Vibe Coding | Agentic Engineering |
|------|-------------|---------------------|
| **代码质量** | 原型级、未审查 | 生产级、已验证 |
| **验证方式** | 无/凭感觉 | 自动测试 + 运行验证 |
| **人类角色** | "忘记代码存在" | 验证者、迭代者 |
| **目标** | 快速原型 | 可工作软件 |

> [!warning] 保持区分
> Vibe Coding 应保持原意：**未经审查、原型质量的 LLM 生成代码**，与已提升到生产标准的代码区分开来。

## 核心实践

| 领域 | Agent 角色 | 人类角色 |
|------|-----------|---------|
| **Git 操作** | 执行复杂命令、解决冲突 | 设定目标、审核结果 |
| **测试** | Red/Green TDD、运行测试 | 定义测试策略 |
| **代码理解** | Linear walkthroughs、解释代码 | 提出问题 |
| **重构** | 后台异步重构 | PR 评估 |
| **历史管理** | History Rewriting | 编辑决策 |

## 反向边界：不要把摩擦全打掉

[[Why I Don’t Vibe Code]] 对 Agentic Engineering 的补充是：生产级 Agent 工程不应只问“能不能更快生成代码”，还要问“哪些摩擦必须保留为设计反馈”。

有经验工程师在 close reading、写 ADR、走开暂停和重新审视架构时，并不是在浪费时间，而是在处理 [[Essential-Complexity|本质复杂性]]。好的 Agentic Engineering 应让 Agent 执行可验证工作，同时保留人类对抽象、责任和协作边界的判断。


### Leverage：声明式指令 (Karpathy, 2026)

Karpathy 补充了获得 Agent 杠杆的关键方法：

> "Don't tell it what to do, give it success criteria and watch it go."

**声明式 vs 命令式**：

| 方式 | 示例 | 杠杆效果 |
|------|------|---------|
| **命令式** | "写一个排序函数" | Agent 执行一次，结果固定 |
| **声明式** | "测试通过后停止" | Agent 循环迭代，自我修正 |

**实践模式**：
1. 先写测试，让 Agent 循环直到测试通过
2. 给 Agent 配浏览器 MCP，让它自主探索验证
3. 先写朴素算法（确保正确），再让 Agent 优化


### 三阶段模型：开发/审查/硬化 (Breunig, 2026)

Drew Breunig 提出扩展的三阶段 Agentic Coding 模型：

| 阶段 | 任务 | 瓶颈 | 说明 |
|------|------|------|------|
| **开发** | 实现功能、快速迭代 | Human input | 人类直觉主导，反馈驱动 |
| **代码审查** | 文档、重构、PR 审查 | Human input | 异步应用最佳实践 |
| **安全硬化** | 识别漏洞、持续审计 | Money (tokens) | 自主运行直到预算耗尽 |

**关键洞察**：安全审计从"rare, discrete, inconsistent"变为"constant, within optimal budget"。

## 关键数据点

- Agent 定义：**Agents run tools in a loop to achieve a goal**
- Code Execution 是决定性能力：没有直接运行代码的能力，LLM 输出价值有限
- Vibe Coding 一词由 Andrej Karpathy 在 2025 年 2 月提出（Claude Code 发布前三周）
- Karpathy 的贡献是把 Vibe Coding 与 Agentic Engineering 区分为"提升底线"与"保持质量上限"两类实践
- 四项核心原则：代码成本趋近于零、囤积可运行代码示例、AI 应帮助产出更好的代码、不提交未审查的代码

## 前提与局限性

- Agentic Engineering 依赖 coding agents 具备代码执行能力，纯文本 LLM 无法胜任
- 人类角色从"写代码"转为"验证和迭代"，需要对结果负责
- LLM 不从过去错误中学习，需要人类显式更新指令和工具 harness
- Vibe Coding 和 Agentic Engineering 应保持区分：前者是未审查原型，后者是生产级代码
- Agentic Engineering 不能只追求消除摩擦；部分摩擦是设计信号，必须通过 review、ADR、测试和人工判断保留下来

## 关联概念

- [[Code-Execution]] - 决定性能力
- [[Coding-Agents]] - Claude Code, Codex, Gemini CLI
- [[Vibe-Coding]] - 对比概念
- [[Compound-Engineering]] - 持续改进模式
- [[Git-Fluent-Agents]] - Git 实践
- [[Corrective-RAG]] — Agentic 工程中提升 RAG 质量的核心模式
- [[Reflexion]] — Agentic 工程中提升输出可靠性的反馈循环
- [[Hardware-Sovereignty]] — 企业级 Agentic 部署的基础设施前提
- [[Essential-Complexity]] — Agentic Engineering 需要显式面对的复杂性
- [[Friction-as-Design-Signal]] — 判断哪些摩擦该保留为设计反馈

## 来源

- [[Using Git with coding agents - Agentic Engineering Patterns]]
- [[What is agentic engineering? - Agentic Engineering Patterns]]
- Simon Willison, [Agentic Engineering Patterns Guide](https://simonwillison.net/guides/agentic-engineering-patterns/)
