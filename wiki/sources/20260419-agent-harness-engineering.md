---
type: source-summary
title: "Agent Harness Engineering"
source_raw:
  - "[[20260419-agent-harness-engineering.md]]"
created: 2026-06-10
updated: 2026-06-10
tags:
  - source-summary
  - agent-harness
  - agentic-engineering
---

# Agent Harness Engineering

## 编译摘要

### 1. 浓缩
- **核心结论1**: **Agent = Model + Harness**。智能体不仅仅是模型，而是模型加上环绕它的所有脚手架（提示词、工具、沙箱、反馈环）。脚手架的设计往往比模型选择更能决定最终性能。
  - 关键证据: Claude Opus 4.6 在自定义 Harness 下的 Terminal Bench 2.0 评分远高于其在默认 Harness 下的表现；Viv Trivedy 的团队仅通过优化 Harness 将 Agent 排名从前 30 提升至前 5。
- **核心结论2**: **Harness Engineering 是一种“棘轮（Ratchet）”纪律**。每当 Agent 犯错，就应当通过工程化手段（更新 `AGENTS.md`、增加 Hook、拆分 Planner/Executor 等）确保该错误不再发生。
  - 关键证据: 将类型检查（Typecheck）作为背压信号接入循环，防止 Agent “完成”有问题的代码。
- **核心结论3**: **上下文腐烂（Context Rot）是长程任务的主要瓶颈**。Harness 必须承担上下文压缩（Compaction）、工具调用卸载和定时重置（Context Reset）的职责，以维持推理质量。
  - 关键证据: Anthropic 团队在处理长程任务时使用完整的上下文重置，通过结构化的“移交文件（Hand-off file）”在新会话中重建状态。

### 2. 质疑
- **关于“棘轮效应”的质疑**: 过度增加约束是否会导致系统变得过于僵化，无法适应新的代码风格或非预期的复杂场景？过度依赖 `AGENTS.md` 可能导致 Prompt 长度爆炸，反而加剧上下文腐烂。
- **关于“模型 vs Harness”的质疑**: 作者倾向于认为 Harness 是核心变量，但这可能是在模型能力处于平台期时的权宜之计。如果 GPT-5 或更高阶模型在原生状态下就能处理长程规划和自省，那么复杂的 Harness 是否会变成沉重的技术债务？
- **关于 HaaS 模式的质疑**: 随着 OpenAI 和 Anthropic 推出官方 Agent SDK，通用的 Harness 模式是否会扼杀垂直领域（如生物、医药）对高度定制化 Harness 的需求？

### 3. 对标
- **跨域关联1**: 类似于**软件工程中的 SRE（站点可靠性工程）**。SRE 不改代码逻辑，但确保代码在生产环境中稳定运行；Harness Engineering 不改模型权重，但确保模型在工作流中产出正确结果。
- **跨域关联2**: 类似于**编译器的脚手架环境**。模型是执行逻辑，而 Harness 是提供输入、捕获输出并进行错误处理的运行时。

### 关联概念
- [[Agent-Harness]]
- [[Harness-Engineering]]
- [[Context-Rot]]
- [[Ralph-Loops]]
- [[HaaS-Harness-as-a-Service]]
- [[AGENTS-md]]
- [[Context-Engineering]]
- [[Verifiable-Agent-Engineering]]
