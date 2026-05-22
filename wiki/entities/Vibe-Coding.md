---
type: entity
title: Vibe Coding
aliases:
  - Vibe Coding
definition: "Andrej Karpathy 2025 年提出的概念——提升所有人的编程能力底线（raising the floor），让任何人都能通过自然语言和 agent 交互来生成软件；未经审查、原型质量是其特征而非缺陷"
created: 2026-04-10
updated: 2026-05-22
tags:
  - AI-Agent
  - coding-agents
  - programming
related_entities:
  - '[[Agentic-Engineering]]'
  - '[[Harness-Engineering]]'
  - '[[Code-Execution]]'
  - '[[Andrej-Karpathy]]'
  - '[[Software-2.0]]'
  - '[[AI-Capability-Gap]]'
  - '[[AI-Psychosis]]'
  - '[[Software-3.0]]'
  - '[[Jagged-Intelligence]]'
  - "[[Essential-Complexity]]"
  - "[[Friction-as-Design-Signal]]"
  - "[[Ownership]]"
source_raw:
  - '[[Andrej Karpathy: From Vibe Coding to Agentic Engineering]]'
  - '[[What is agentic engineering? - Agentic Engineering Patterns]]'
  - '[[20260413-llm-wiki]]'
  - '[[20260413-why-ai-first-strategy-wrong]]'
  - '[[20260409-ai-capability-gap-ai-psychosis]]'
  - "[[20260127-claude-coding-notes]]"
  - "[[用Agent评测思路管理AI Coding —— 31万行代码AI重构的实践]]"
  - "[[Why I Don’t Vibe Code]]"
---

# Vibe Coding（氛围编程）

> **核心特征**：忘记代码存在，专注于氛围和直觉

## 定义

**Vibe Coding** 是 Andrej Karpathy 于 2025 年 2 月提出的术语，描述一种 LLM 编程方式：

> "I just see things, say things, run things, and copy paste things, and it mostly works."

### 核心特征

1. **忘记代码存在** - 不关心代码细节
2. **原型质量** - 快速产出，不追求生产级
3. **未经审查** - 直接使用 AI 输出
4. **氛围驱动** - 凭直觉迭代

## 与 Agentic Engineering 的区别

Simon Willison 强调保持术语的原意：

| 维度 | Vibe Coding | Agentic Engineering |
|------|-------------|---------------------|
| **代码质量** | 原型级 | 生产级 |
| **审查程度** | 无 | 深度审查 |
| **验证方式** | 凭感觉 | 自动测试 |
| **目标** | 快速原型 | 可工作软件 |
| **心态** | "忘记代码" | 验证和迭代 |

## 适用场景

### 适合 Vibe Coding

- 快速原型验证
- 个人实验项目
- 学习和探索
- 一次性脚本

### 需要 Agentic Engineering

- 生产环境代码
- 团队协作项目
- 长期维护系统
- 安全敏感应用

## 不要滥用术语

> [!warning] 重要区分
> 不要把 Vibe Coding 扩展定义为"任何 LLM 生成代码的情况"。
> 
> 保持原意：**未经审查、原型质量的 LLM 生成代码**，与已提升到生产标准的代码区分开来。

## Karpathy 的完整论述

Andrej Karpathy 在 LLM Wiki 文章中进一步阐述：

> "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."

这揭示了 Vibe Coding 的深层含义：当 LLM 成为"程序员"，人类角色转变为：
- **Sourcing** — 提供知识源
- **Exploration** — 探索和验证
- **Questioning** — 提出正确的问题

---

## Vibe Coding 的工程治理代价

美团实践揭示了 Vibe Coding 在团队场景下的系统性风险：当 90%+ 代码由 AI 生成，不同背景成员各自用 AI Coding，系统会**加速腐化**而非收敛复杂度。

核心矛盾：Vibe Coding 提升了个体编码效率，但如果没有统一规范约束，AI 会把代码风格差异进一步放大——"千人千面"的代码在 31 万行体量下变成灾难。

解法：通过 [[人机对齐]] 方法论，先拉齐团队工程标准，再将标准落地为 AI Rule/Skill，从"氛围驱动"转向"约束驱动"。

## 关联概念

- [[Software-2.0]] - Vibe Coding 是 Software 2.0 的实践延伸
- [[Agentic-Engineering]] - 与 Vibe Coding 对比的工程范式
- [[Harness-Engineering]] - 超越 Agentic Engineering：不仅审查代码，而是构建让 Agent 有效工作的完整系统
- [[Code-Execution]] - Vibe Coding 不强调验证，Agentic Engineering 和 Harness Engineering 强调
- [[Andrej-Karpathy]] - 概念提出者

Vibe Coding 与 Software 2.0 的关系：

| Software 2.0 | Vibe Coding |
|--------------|-------------|
| 程序员写目标 | 用户说"氛围" |
| 神经网络生成程序 | LLM 生成代码 |
| 数据是源代码 | 对话是源代码 |


### Karpathy 的新观察 (2026-01)

在 Claude Coding Notes 中，Karpathy 补充了 Vibe Coding 的常见陷阱：

> "They really like to overcomplicate code and APIs, they bloat abstractions, they don't clean up dead code after themselves... They will implement an inefficient, bloated, brittle construction over 1000 lines of code and it's up to you to be like 'umm couldn't you just do this instead?'"

**模型倾向**：
1. 过度复杂化代码和 API
2. 膨胀抽象层
3. 不清理死代码
4. 实现冗余、脆弱的 1000 行方案，经提示后可压缩为 100 行

## 反向案例：为什么不 Vibe Code

Jacob Harris 的 [[Why I Don’t Vibe Code]] 给 Vibe Coding 提供了一个有价值的反例。它不是从“AI 是否有用”切入，而是从软件工作的不可外包部分切入：

- [[Essential-Complexity]] 仍然存在：AI 可以降低写代码的偶然复杂性，但不能替代抽象设计、边界选择和长期维护判断。
- [[Friction-as-Design-Signal]] 不能被一概消除：阅读陌生代码、写 ADR、暂停实现，都是让真实约束浮现的过程。
- [[Ownership]] 不能转交给模型：模型可以生成代码，但不能为公共服务故障、数据误读或系统伤害承担后果。
- 软件是协作实践：把产品、设计、测试、合规和 review 都视为“摩擦”，会让系统更快但未必更好。

## 关键数据点

- Andrej Karpathy 于 2025 年 2 月提出该术语
- Karpathy 的原始描述："I just see things, say things, run things, and copy paste things, and it mostly works."
- Claude Code 于 2025 年 3 月发布（Karpathy 提出术语后仅 3 周）
- LLM Wiki 的深层含义："Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."

## 前提与局限性

- 依赖前提：人类愿意接受"忘记代码存在"的开发方式
- 适用边界：快速原型、个人实验、学习探索、一次性脚本
- 局限性：不适用于生产环境、团队协作、长期维护系统、安全敏感应用
- 质量标准：未经审查、原型质量，与生产就绪代码有本质区别
- 术语滥用风险：不应将"任何 LLM 生成代码"都定义为 Vibe Coding
- 反向边界：当任务需要本质复杂性判断、团队协作和责任承担时，Vibe Coding 的收益会被隐藏成本抵消

---

> **来源**：Andrej Karpathy (2025-02, 2026-04), Simon Willison (Agentic Engineering Patterns, 2026)
