---
type: entity
title: Vocabulary Building (词汇构建)
aliases:
  - 词汇构建
  - Vocabulary Building
definition: "将领域语言（Domain Vocabulary）翻译并映射到技术实现中，从而在代码中发现并塑造新词汇的过程。"
created: 2026-05-13
updated: 2026-05-13
tags:
  - programming-theory
  - domain-driven-design
  - software-development-process
source_raw:
  - "[[What Is Code?]]"
---

# Vocabulary Building

> **核心洞察**：编码本质上是一种翻译和发现词汇的艺术。

## 定义

**词汇构建**（Vocabulary Building）是 [[Unmesh-Joshi]] 对编码本质的新定义。他认为开发者的核心工作不是敲击键盘产生字符，而是：
1. **获取**：深入理解业务领域的既有词汇（如银行、零售、医疗）。
2. **映射**：将这些词汇与技术领域的词汇（如 Web、数据库、并发模型）相结合。
3. **塑造**：在代码中通过类型、接口、类名创造出一套精确的、可执行的“新词汇”。

## 为什么词汇很重要？

1. **沟通中介**：词汇是人类、框架和 LLM 之间共享的协议。
2. **设计后果**：一个词（如 `Abstraction`）不仅是标签，它携带了约束、语义和设计上的连锁反应。
3. **LLM 指引**：精确、一致的词汇能让 LLM 更可靠地映射意图。模糊的词汇会导致 LLM “盲目猜测”。

## 词汇构建的过程

- **发现**：词汇通常不是预先设定好的，而是在 TDD（测试驱动开发）或持续重构中逐步浮现的。
- **固化**：框架和库（如 Spring）本质上是“被固化的词汇表”，捕捉了常见的应用模式。
- **本地化**：在核心业务逻辑中，词汇必须在特定的 [[Bounded-Context]] 内发现。

---

## 关键数据点

- 词汇构建需要主动参与（Active Engagement），而非被动评审 AI 生成的代码。
- 编程语言通过其约束（如 Rust 的 ownership）作为“思考工具”来帮助发现词汇。

## 前提与局限性

- **前提**: 假设高质量的软件需要深度的领域对齐。
- **局限性**: 在低代码/无代码平台，词汇构建可能被预定义的 UI 组件所屏蔽。
- **冲突点**: 过度关注词汇可能导致“过度设计”或命名上的反复纠结。

## 关联概念

- [[Conceptual-Model]] - 词汇构建的目标
- [[Ubiquitous-Language]] - 词汇构建的社会化表达
- [[Programming-Languages-as-Thinking-Tools]] - 构建词汇的工具
- [[Cognitive-Debt]] - 词汇缺失导致的后果
