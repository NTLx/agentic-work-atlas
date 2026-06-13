---
type: source-summary
title: "Building effective agents"
source_raw:
  - "[[building-effective-agents-complete]]"
created: 2026-05-25
updated: 2026-05-25
tags:
  - source-summary
  - AI-Agent
  - LLM
  - workflows
  - tool-use
---

# Building effective agents

## 编译摘要

### 1. 浓缩

- **核心结论1**: Anthropic 的核心建议是先用最简单的方案，只有在能证明效果提升时才增加 agentic complexity。
  - 关键证据: 官方文章强调，许多应用只需要单次 LLM call、retrieval 和 in-context examples；agentic systems 会用更高 latency 和成本换取更好任务表现，必须判断 tradeoff 是否值得。
  - 对本库的意义: 这篇文章是 [[Building-Effective-Agents]] 与 [[Agent-Workflow-Patterns]] 的基础来源，提供“从 augmented LLM 到 workflows 再到 agents”的复杂度阶梯。
- **核心结论2**: Anthropic 把 agentic systems 分成 workflows 和 agents：前者走预定义路径，后者由 LLM 动态决定过程和工具使用。
  - 关键证据: 官方定义中，workflows 是 LLM 与工具由预定义代码路径编排；agents 是 LLM 自己动态指挥流程、选择工具并保持对完成方式的控制。
  - 关键模式: 文章列出 prompt chaining、routing、parallelization、orchestrator-workers、evaluator-optimizer 五类 workflow，再讨论更开放的 autonomous agents。
- **核心结论3**: Agent 的可靠性来自清晰工具、环境反馈、评测和人类检查点，而不是更复杂的框架。
  - 关键证据: Anthropic 建议框架可帮助起步，但会制造抽象层、遮蔽 prompt 与 response、诱导过度复杂；生产中应理解底层代码。工具定义要像 prompt 一样被工程化，ACI 需要示例、边界、参数命名、错误预防和测试。
  - 关键细节: 在 SWE-bench agent 中，Anthropic 花在工具优化上的时间超过整体 prompt，例如把相对路径参数改成绝对路径以减少模型误用。

### 2. 质疑

- **关于“简单优先”的质疑**: 简单是很好的默认策略，但不能被误读为“永远不用框架”。当团队需要审计、权限、回放、成本追踪、协作和可观测性时，框架或 harness 会成为必要基础设施。
- **关于 workflows vs agents 的质疑**: 二分有助于入门，但真实系统常混合使用：主流程可预测，局部步骤由 agent 动态决策；这需要更细的风险分层。
- **关于官方案例的质疑**: Anthropic 提到 customer support 和 coding agents 特别适合，因为有行动、反馈、清晰成功标准和人类监督；这不意味着所有企业流程都适合 autonomous agents。
- **关于 ACI 的质疑**: 工具定义优化容易被低估，但它需要大量具体任务样本。没有真实 eval set 和失败回放，工具文档很难只靠直觉设计好。

### 3. 对标

- **对标 [[Agentic-Engineering-Patterns]]**: 本文提供 agentic engineering 的通用系统模式，而 Simon Willison 系列更偏软件工程实践。两者共同强调少一点魔法、多一点可验证反馈。
- **对标 [[Agent-Harness-vs-Agent-Workflow-Patterns]]**: Anthropic 文章给的是模式层，harness 则负责运行时层。生产系统通常需要把 workflow pattern 放进权限、日志、状态、审计和人工验收壳层中。
- **对标 [[Verifiable-Agent-Engineering]]**: Evaluator-optimizer、coding agents、SWE-bench、test feedback 都说明 agent 成功依赖可验证环境。不能验证的任务需要更强的人类 checkpoint。
- **可迁移场景**: 客服 agent、coding agent、研究 agent、复杂搜索、内容生成、风险审查。迁移前必须先问：任务是否可分解、是否有评测、错误是否可恢复、工具接口是否清晰。

### 关联概念

- [[Building-Effective-Agents]]
- [[Agent-Workflow-Patterns]]
- [[ACI-Agent-Computer-Interface]]
- [[Agent-Harness]]
- [[Agentic-Engineering]]
- [[Code-Execution]]
- [[Verifiable-Agent-Engineering]]
