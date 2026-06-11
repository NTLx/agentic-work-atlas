---
type: topic
title: Code as Conceptual Infrastructure
description: "代码作为概念基础设施：AI 让指令生成变便宜后，软件的核心资产上移为词汇、边界、模型和语义约束"
created: 2026-05-18
updated: 2026-05-22
tags:
  - software-engineering
  - knowledge-management
  - AI-Agent
related_entities:
  - "[[Conceptual-Model]]"
  - "[[Vocabulary-Building]]"
  - "[[Ubiquitous-Language]]"
  - "[[Bounded-Context]]"
  - "[[Cognitive-Debt]]"
  - "[[Programming-Languages-as-Thinking-Tools]]"
  - "[[Ontology]]"
  - "[[Knowledge-Compilation]]"
  - "[[LLM-Wiki]]"
  - "[[Context-Engineering]]"
  - "[[CLAUDE-md]]"
  - "[[Essential-Complexity]]"
  - "[[Friction-as-Design-Signal]]"
  - "[[Ownership]]"
source_raw:
  - "[[What Is Code?]]"
  - "[[20260420-ontology-enterprise-ai-agent]]"
  - "[[20260420-build-first-business-ontology]]"
  - "[[20260420-ontology-meets-agent-case-study]]"
  - "[[20260413-llm-wiki]]"
  - "[[深度解析LLM Wiki  Obsidian-Wiki  GBrain：Agent时代知识的“自组织”与“自进化”]]"
  - "[[Why I Don’t Vibe Code]]"
  - "[[The-Founders-Playbook-05062026_v3]]"
---

# Code as Conceptual Infrastructure（代码作为概念基础设施）

> [!summary] 核心洞察
> AI 让“写出指令”变便宜，但没有让“建立正确概念”变便宜。软件的核心资产正在从代码量转向词汇、边界、模型和语义约束。

## 代码不只是给机器执行

[[Conceptual-Model|概念模型]]把代码拆成两种属性：

- 指令属性：告诉机器怎么执行。
- 模型属性：告诉人类和 Agent 这个系统如何理解世界。

当 LLM 能快速生成指令属性时，真正稀缺的部分反而显形：哪些词该存在，边界画在哪里，哪些规则必须保持，哪些抽象应该被拒绝。

这意味着软件质量不再只问“代码能不能跑”，而要问“这套概念能不能被人和 Agent 继续思考”。

## 词汇是 AI 时代的接口

[[Vocabulary-Building|词汇构建]]不是命名洁癖。它是人、业务、代码和 LLM 之间的协议。

| 软件元素 | 过去常见理解 | AI 时代的新含义 |
|----------|--------------|----------------|
| 类名/函数名 | 代码组织 | Prompt 锚点和语义路标 |
| [[Bounded-Context]]（限界上下文） | 架构分区 | 防止 LLM 混淆词义的真相边界 |
| [[Ubiquitous-Language]]（通用语言） | 团队沟通方式 | 人机共享的业务协议 |
| 测试 | 防回归工具 | 概念不变量的可执行说明 |
| 文档/Wiki | 辅助材料 | Agent 的外部记忆和编译产物 |

词汇越精确，Agent 越不需要猜。词汇越混乱，模型越会用流畅输出掩盖错误理解。

## CLAUDE.md 是项目级概念合约

[[CLAUDE-md|CLAUDE.md]] 是这个主题在代码库里的最小可执行形态。它不是普通 README，而是给 coding agent 读取的项目级概念合约：哪些架构原则有效，哪些依赖不要引入，哪些业务规则不可破坏，哪些测试和审查才算完成。

《The Founder's Playbook》的关键提醒是：AI-native MVP 的风险不只是“写错代码”，而是每个会话都重新解释代码库，导致局部变更逐渐偏离原始设计。把架构决策、范围边界和业务不变量写进 CLAUDE.md，本质上是在给 Agent 提供可复用的概念基础设施。

## 认知债务是新的技术债务

[[Cognitive-Debt|认知债务]]的危险在于：代码可以运行，团队却不知道它意味着什么。

AI 会加速这种债务，因为它能轻易生成看似成熟的词汇：Repository、Controller、Orchestrator、Policy、Context、Graph。问题不在这些词本身，而在团队是否真的拥有这些词背后的模型。

```
AI 生成词汇
  ↓
代码可运行
  ↓
团队未建立概念模型
  ↓
修改变慢、评审变空、边界变脆
  ↓
认知债务复利增长
```

所以“不要过度抽象”在 AI 时代不只是工程审美，而是认知风险控制。

## 摩擦暴露概念问题

[[Friction-as-Design-Signal|摩擦作为设计信号]]补上了另一个角度：如果代码是概念基础设施，那么写代码时遇到的阻力并不总是低效。它可能说明词汇不清、边界错误、抽象层级不对，或者团队还没有真正理解这个领域。

[[Why I Don’t Vibe Code]] 的价值在于把这种摩擦从“要被 AI 消灭的成本”重新解释为工程反馈。LLM 可以帮忙生成实现，但它不会自动知道某个实现为什么“感觉不对”。这种感觉通常来自 [[Essential-Complexity|本质复杂性]]：现实比模型脏，抽象会遮蔽信息，系统需要人在后果中承担责任。

## 本体是企业级概念基础设施

[[Ontology|本体]]把这个问题推到企业尺度：如果一个组织想让 Agent 理解订单、库存、客户、权限、风险，它不能只靠 prompt 解释。它需要稳定的语义层。

TBox定义概念和规则，ABox承载事实实例。这个区分很关键：Agent 可以在事实层工作，但它必须被概念层约束。否则每个 Agent 都会临时发明一套业务世界。

这与代码中的限界上下文是同构问题：小系统需要清晰词汇，大企业需要清晰本体。

## LLM Wiki 是概念基础设施的个人形态

[[LLM-Wiki]]和[[Knowledge-Compilation|知识编译]]把同样原则应用到知识管理：

- Raw 是事实材料。
- Entity 是概念词汇。
- Topic 是概念之间的生成结构。
- Comparison 是边界和差异。
- Lint 是语义卫生。

这说明 wiki 本身也像代码库：不是存储更多文本，而是维护一套可被人和 Agent 继续运行的概念系统。

## 与现有 Topic 的关系

- [[Enterprise-Ontology-Application]]讲企业语义层。
- [[Agent-Knowledge-Management]]讲 Agent 知识如何自组织。
- 本 Topic 把代码、企业本体和 LLM Wiki 放到同一个结构中：它们都是概念基础设施。

## 结论

AI 时代的软件竞争，不是看谁生成更多代码，而是看谁拥有更干净的概念系统。

代码越便宜，概念越贵。
