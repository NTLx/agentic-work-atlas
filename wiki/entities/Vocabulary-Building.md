---
type: entity
title: Vocabulary Building
aliases:
  - 词汇构建
  - Vocabulary Building
definition: “将业务领域语言与技术实现映射融合，在代码中发现并塑造可执行的新词汇”
created: 2026-05-13
updated: 2026-05-26
tags:
  - programming-theory
  - domain-driven-design
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[Conceptual-Model]]"
  - "[[Ubiquitous-Language]]"
  - "[[Programming-Languages-as-Thinking-Tools]]"
  - "[[Cognitive-Debt]]"
  - "[[Bounded-Context]]"
source_raw:
  - "[[What Is Code?]]"
  - "[[Anthropic's Boris Cherny: Why Coding Is Solved, and What Comes Next]]"
---

# Vocabulary Building（词汇构建）

> [!definition] 定义
> **Vocabulary Building（词汇构建）** 是编码的核心活动：深入理解业务领域的既有词汇，将它们与技术领域词汇相结合，在代码中通过类型、接口、类名创造出一套精确的、可执行的”新词汇”。

## 关键数据点

- 编码本质上是一种翻译和发现词汇的艺术，而非仅仅是敲击键盘产生字符。
- 词汇是人类、框架和 LLM 之间共享的协议；精确、一致的词汇能让 LLM 更可靠地映射意图。
- 框架和库（如 Spring）本质上是”被固化的词汇表”，捕捉了常见的应用模式。
- 编程语言通过其约束（如 Rust 的 ownership）作为”思考工具”来帮助发现词汇。

## AI 时代对词汇构建的影响

AI 让语法生成变便宜，但让概念建模、命名、边界和共享理解更关键。词汇构建在 AI 时代有三层新含义：

| 层次 | 传统含义 | AI 时代含义 |
|------|---------|------------|
| 沟通 | 团队间共享理解 | 人类、工具和 LLM 之间的共享协议 |
| 设计 | 一个词携带约束和语义 | 词汇携带设计连锁反应，影响 Agent 行为 |
| 质量 | 代码可读性 | LLM 映射意图的可靠度 |

好代码本身就是 LLM 的 context 和 harness：稳定抽象、测试、类型和不变量会约束模型，让自然语言接口更可靠。反之，如果代码词汇混乱，模型只能猜——这就是 [[Cognitive-Debt|认知负债]] 在 AI 时代的新形态。

## 词汇构建的过程

- **发现**：词汇通常不是预先设定好的，而是在 TDD（测试驱动开发）或持续重构中逐步浮现的。
- **固化**：框架和库本质上是”被固化的词汇表”，捕捉了常见的应用模式。
- **本地化**：在核心业务逻辑中，词汇必须在特定的 [[Bounded-Context]] 内发现，不能跨上下文混用。
- **主动参与**：词汇构建需要主动参与（Active Engagement），而非被动评审 AI 生成的代码。

## 前提与局限性

- **前提**：高质量的软件需要深度的领域对齐。
- **局限**：在低代码/无代码平台，词汇构建可能被预定义的 UI 组件所屏蔽。
- **风险**：过度关注词汇可能导致”过度设计”或命名上的反复纠结。
- **AI 时代风险**：LLM 可以快速引入看似合理的名词和结构，但团队若不理解其语义，就会积累认知负债。代码通过词汇膨胀制造了看似成熟、实则无人理解的系统。

## 关联概念

- [[Conceptual-Model]] — 词汇构建的目标：形成可执行的概念模型。
- [[Ubiquitous-Language]] — 词汇构建的社会化表达：团队共享的统一语言。
- [[Programming-Languages-as-Thinking-Tools]] — 构建词汇的工具：语言约束帮助发现新词汇。
- [[Cognitive-Debt]] — 词汇缺失或混乱导致的后果。
- [[Bounded-Context]] — 词汇的有效边界：跨上下文混用会导致语义崩溃。
