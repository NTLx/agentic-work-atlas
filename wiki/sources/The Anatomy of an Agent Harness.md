---
type: source-summary
title: "The Anatomy of an Agent Harness"
source_raw:
  - "[[The Anatomy of an Agent Harness]]"
created: 2026-05-24
updated: 2026-05-25
tags:
  - source-summary
---

# The Anatomy of an Agent Harness

## 编译摘要

### 1. 浓缩
- **核心结论1**: Agent Harness 是区分玩具 demo 和生产 Agent 的关键；同一模型换一层执行基础设施，能力表现可能大幅变化。
  - 关键证据: 文章引用 LangChain 在 TerminalBench 上仅改变 harness 即从 Top 30 外升至第 5 名，以及独立研究用 LLM 优化 harness 达到 76.4% 通过率。无论这些 benchmark 是否可泛化，它们都说明 Agent 能力不只在权重里，也在循环、工具、状态和验证里。
- **核心结论2**: Harness 本质上是 Agent 的“操作系统”：管理上下文、工具、状态、权限、错误、记忆和终止条件。
  - 关键证据: 文章把 context 比作 RAM、外部数据库比作 disk、tool 比作 device driver、harness 比作 OS。典型循环包括 prompt assembly、inference、output classification、tool execution、result packaging、context update 和 loop/termination。
- **核心结论3**: Harness engineering 高于 prompt engineering 和 context engineering，因为它处理的是可重复运行的执行系统，而非单次提示。
  - 关键证据: 文章列出 orchestration loop、tools、memory、context management、prompt construction、output parsing、state management、error handling、guardrails、verification loops、subagent orchestration 等组件。它强调 context rot、lost in the middle、compaction、observation masking、JIT retrieval 和 subagent summary 都是系统工程问题。
- **核心结论4**: 生产 Agent 的可靠性由错误恢复和验证循环决定，不能只看单步准确率。
  - 关键证据: 若 10 步流程每步 99% 成功，端到端成功率约 90.4%；因此需要区分 transient、LLM-recoverable、user-fixable、unexpected 等错误，并加入 tests、linters、screenshots、LLM-as-judge、人类审批等验证机制。
- **核心结论5**: Harness 与模型会共进化，长期趋势可能是“薄 harness、胖技能”，但短期仍需要谨慎设计。
  - 关键证据: 文章提到 Manus 六个月内重建五次、每次移除复杂性；Vercel 移除 80% 工具后反而更好；Claude Code 通过 lazy loading 大幅降低上下文占用。模型能力提升会吞掉部分脚手架，但模型也可能与特定 harness post-training 绑定，导致随意更换框架降级。

### 2. 质疑
- **关于 benchmark 证据的质疑**: TerminalBench 是特定评测，改变 harness 可能针对 benchmark 优化，不能直接推断所有真实任务都会提升。还需要看长任务、权限、安全、成本和 failure recovery。
- **关于“12 个组件”的质疑**: 原文采用 12-component framing，但可见展开更像一组工程模块而非严格清单。将其当成检查表有用，但不应机械要求每个 Agent 产品都完整实现所有组件。
- **关于“薄 harness”的质疑**: 模型可能内化一部分 planning、tool use 和 memory 能力，但这不等于系统复杂度消失。权限、审计、状态持久化、失败恢复和业务验证仍属于外部工程责任。
- **关于厂商自述的质疑**: Claude Code、OpenAI Agents SDK、LangGraph、CrewAI、AutoGen、Vercel 等案例多来自框架或产品叙述，缺少统一独立评测。结论应作为架构启发，而非供应商性能证明。

### 3. 对标

- **跨域关联1：操作系统设计**：Agent Harness 与 OS 的类比精确：编排循环像调度器，工具层像系统调用，记忆像虚拟内存，上下文管理像页面置换，验证循环像异常处理。这说明 harness 工程越来越接近系统编程，而不是 prompt 技巧。
- **跨域关联2：建筑脚手架**：临时基础设施的隐喻适用于 CI/CD、容器编排和微服务网关：它们先补足底层能力缺口，随后被平台吸收。由此可判断，哪些 harness 组件会长期存在，哪些会被模型或平台吞掉。
- **跨域关联3：编译器与目标架构耦合**：模型与 harness 的锁定效应类似编译器后端与目标 CPU 的耦合；更换 harness 不是换 UI，而是换执行语义。这解释了为什么“同一模型换框架”可能显著退化。
- **跨域关联4：Building effective agents**: 这篇文章可作为 [[Building-Effective-Agents]] 的工程展开。Anthropic 强调先用简单 workflow、少抽象、直接暴露 tool；本文则把生产化时不可避免的状态、验证和错误恢复拆成组件。
- **跨域关联5：ACI 与工具边界**: Harness 的工具选择直接影响 [[ACI-Agent-Computer-Interface]]。Vercel 移除大量工具后效果更好，说明工具不是越多越好；Agent 需要的是少而清晰、可组合、反馈明确的接口。
- **迁移判断**：评估任何 Agent 产品时，不应只问模型是谁，还要问 harness 如何管理上下文、权限、工具、验证和失败恢复。Agent 产品的护城河往往在 harness，而不是单次 prompt。

### 关联概念
- [[Agent-Harness]]
- [[Harness-Engineering]]
- [[Context-Engineering]]
- [[Agent-Orchestration]]
- [[Agent-Workflow-Patterns]]
- [[Building-Effective-Agents]]
- [[ACI-Agent-Computer-Interface]]
- [[Thin-Harness-Fat-Skills]]
- [[Verifiable-Agent-Engineering]]
- [[Agentic-Engineering-Patterns]]
