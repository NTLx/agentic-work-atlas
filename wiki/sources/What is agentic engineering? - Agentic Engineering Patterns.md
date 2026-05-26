---
type: source-summary
title: "What is agentic engineering? - Agentic Engineering Patterns"
source_raw:
  - "[[What is agentic engineering? - Agentic Engineering Patterns]]"
created: 2026-05-24
updated: 2026-05-25
tags:
  - source-summary
  - agentic-engineering
  - coding-agent
  - software-engineering
---

# What is agentic engineering? - Agentic Engineering Patterns

## 编译摘要

### 1. 浓缩

- **核心结论1**: Agentic engineering 是在 coding agents 协助下开发软件，其定义核心不是“会聊天”，而是 agent 能写代码、运行代码，并在工具循环中迭代。
  - 关键证据: Simon Willison 定义 coding agents 为能 write and execute code 的 agents，举例包括 Claude Code、OpenAI Codex、Gemini CLI；agent 的工作方式是调用 LLM、传入工具定义、执行模型请求的工具，再把结果反馈给模型。
  - 关键机制: “Agents run tools in a loop to achieve a goal”是本文最核心的定义。对 coding agents 来说，代码执行工具是决定性能力。
- **核心结论2**: 代码执行把 LLM 生成从静态建议变成可验证迭代；没有执行能力，LLM 输出的工程价值有限。
  - 关键证据: 作者明确说，without direct code execution, anything output by an LLM is of limited value；有了执行能力，agent 可以不断运行、观察错误、修改，直到软件 demonstrably works。
  - 对本库的意义: 这支撑了 [[Verifiable-Agent-Engineering]] 主线：agentic engineering 的核心不是“模型写代码”，而是工具、测试、运行环境和反馈循环让输出可验证。
- **核心结论3**: 人类在 agentic engineering 中仍然负责问题定义、约束选择、结果验证和经验沉淀。
  - 关键证据: 作者强调软件工程从来不只是写代码，而是决定写什么代码；任何问题都有多种解法和 tradeoffs。LLM 不会从过去错误中自动学习，但人类可以通过更新 instructions 和 tool harnesses 把经验外化。
  - 关键边界: Vibe coding 应保留原义，指未经审查、原型质量的 LLM 生成代码；不能把所有 LLM 辅助编程都混称为 vibe coding，否则会抹平质量标准。

### 2. 质疑

- **关于定义范围的质疑**: “在 coding agents 协助下开发软件”很清楚，但 agentic engineering 是否包含组织流程、review policy、CI、security gate、成本治理等更大系统，本文只开了头。
- **关于“代码执行决定性”的质疑**: 执行能力确实关键，但执行并不等于正确。许多错误只在边界数据、长期维护、性能、并发、权限或用户体验中暴露。
- **关于“LLM 不学习”的质疑**: 模型参数不会因你的项目错误立刻改变，但 agent 系统可以通过 memory、CLAUDE.md、tests、lint rules、skills 和 harness 更新来形成局部学习。这里应区分模型学习与系统学习。
- **关于 vibe coding 的质疑**: 作者对 vibe coding 的边界定义很重要，但社区用法已经泛化。Wiki 中需要明确保留本库定义，避免把“AI 写过代码”与“不审查原型代码”混为一谈。

### 3. 对标

- **对标 [[Agentic-Engineering]]**: 本文是该 entity 的基础定义来源，提供 agent、coding agent、agentic engineering、vibe coding 四个核心边界。
- **对标 [[Agentic-Engineering-vs-Vibe-Coding]]**: 文中对 vibe coding 的澄清直接支撑该 comparison：生产级 agentic engineering 必须包含审查、测试、约束和迭代，而不是忘记代码存在。
- **对标 [[Agent-Harness]]**: 作者提到 instructions 和 tool harnesses 会承载经验，这与本库的 harness 观点一致：模型能力需要外部运行时壳层才能变成稳定工程能力。
- **可迁移场景**: coding agent 使用规范、工程团队 onboarding、AI 编程培训、工具选型、质量门禁设计。任何团队在引入 Claude Code、Codex 或 Gemini CLI 前，都应先统一这组概念边界。

### 关联概念

- [[Agentic-Engineering]]
- [[Coding-Agents]]
- [[Vibe-Coding]]
- [[Agent-Harness]]
- [[Verifiable-Agent-Engineering]]
- [[Agentic-Engineering-vs-Vibe-Coding]]
