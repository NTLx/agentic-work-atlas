---
type: source-summary
title: "What Is Code?"
source_raw:
  - "[[What Is Code?]]"
created: 2026-05-24
updated: 2026-05-25
tags:
  - source-summary
  - conceptual-model
---

# What Is Code?

## 编译摘要

### 1. 浓缩

- **核心结论1**: 在 LLM 时代，代码作为机器指令的部分被商品化，但代码作为问题领域概念模型的价值变得更重要。
  - 关键证据: Unmesh Joshi 区分 code 的两个方面：instructions to a machine 和 conceptual model of the problem domain。LLM 让生成可执行指令变便宜，但不会自动生成团队共享理解。
  - 关键含义: 代码不是只是让机器跑的文本，它也是人类、工具和 LLM 理解系统的中介。
- **核心结论2**: 编码是 vocabulary building：把业务领域、技术领域和编程语言构造映射成一套可执行、可讨论、可演化的本地词汇。
  - 关键证据: 文章用 retail、web、transactions、repositories、money、bounded context、ubiquitous language 等例子说明，变量名、方法边界、类型层级和接口关系都是概念发现的结果。
  - 关键机制: TDD、DDD、敏捷协作、与领域专家持续反馈，都是在塑造和验证这套词汇。
- **核心结论3**: 好代码本身是 LLM 的 context 和 harness；稳定抽象、测试、类型和不变量会约束模型，让自然语言接口更可靠。
  - 关键证据: 作者认为 well-structured code with clear semantics 可以减少对 prompt 精度的依赖；LLM 擅长把自然语言映射到已有 vocabulary，但如果代码词汇混乱，模型只能猜。
  - 对本库的意义: 这篇文章把 [[Code-as-Conceptual-Infrastructure]] 的论点说得很清楚：AI 让语法生成便宜，但让概念建模、命名、边界和共享理解更关键。

### 2. 质疑

- **关于代码必要性的质疑**: 如果未来 DSL、规格语言和自然语言接口更强，传统代码形态可能变化。但只要系统需要可执行不变量、可验证行为和共享语义层，某种“代码式概念模型”仍然必要。
- **关于短生命周期代码的质疑**: 对一次性脚本、低风险原型或可随时重写的小工具，理解完整 vocabulary 的必要性较低；本文更适用于长期演化、多人协作和高风险系统。
- **关于 LLM 适配的质疑**: 好代码能帮助 LLM，但不能消除上下文窗口、依赖漂移、测试盲区和模型迎合等风险。代码作为 harness 仍需配合外部 eval、lint、CI 和人类 review。
- **关于经验论证的质疑**: 文章主要是软件工程经验和概念分析，不是实证研究。应作为理论框架使用，而非量化结论。

### 3. 对标

- **对标 [[Code-as-Conceptual-Infrastructure]]**: 本文是该 topic 的核心来源。代码的价值从“写给机器执行”转向“让人和机器共享概念基础设施”。
- **对标 [[Cognitive-Debt-vs-Technical-Debt]]**: LLM 可以快速引入熟悉名词和结构，但团队若不理解其语义，就会积累 cognitive debt。代码通过词汇膨胀制造了看似成熟、实则无人理解的系统。
- **对标 [[Harness-Engineering]]**: 文章提醒不要只把 harness 看成外部脚手架；代码结构、命名、测试和不变量本身也是 harness 与 context。
- **可迁移场景**: LLM 辅助编程、遗留系统重构、领域建模、企业软件平台、DSL 设计、团队 onboarding。关键问题是：模型生成的代码是否增强了共享 vocabulary，还是只增加了没人理解的词。

### 关联概念

- [[Conceptual-Model]]
- [[Vocabulary-Building]]
- [[Cognitive-Debt]]
- [[Bounded-Context]]
- [[Ubiquitous-Language]]
- [[Programming-Languages-as-Thinking-Tools]]
- [[Code-as-Conceptual-Infrastructure]]
- [[Harness-Engineering]]
