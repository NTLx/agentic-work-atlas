---
type: entity
title: Reflexion
aliases:
  - Reflexion
  - Reflexion Agent
definition: "用批评者反馈驱动 Agent 生成、验证、重试的自我纠错模式"
created: 2026-05-10
updated: 2026-05-25
tags:
  - AI-Architecture
  - Multi-Agent
related_entities:
  - "[[Agent-Orchestration]]"
  - "[[Agentic-Engineering]]"
  - "[[Corrective-RAG]]"
  - "[[Zero-PHI-Policy]]"
  - "[[Evaluation-Set]]"
  - "[[Verifiable-Agent-Engineering]]"
source_raw:
  - "[[OncoAgent A Dual-Tier Multi-Agent Framework for Privacy-Preserving Oncology Clinical Decision Support]]"
---

> [!definition] 定义
> Reflexion 是一种 Agent 自我纠正模式：生成者产出结果后，批评者（Critic）进行多层验证，失败时将具体反馈注入生成者上下文进行重试，形成"生成→评估→反馈→重试"的循环，直到通过或达到最大迭代次数。

## 关键数据点

- **三层验证级联**: 格式检查 → 安全检查 → LLM 蕴涵检查
- **确定性安全**: 批评者以确定性代码运行（非 LLM 控制逻辑），防止对抗性提示绕过安全检查
- **重试上限**: 通常设为 2 次迭代，防止无限循环
- **OncoAgent 实践**: 作为 8 节点 LangGraph 拓扑中的 Critic 节点，位于 Specialist 和 HITL Gate 之间
- **原始论文**: Shinn et al. (2023), NeurIPS — 使用语言强化学习实现 Agent 自我改进
- **失败路径**: OncoAgent 中若重试后仍不满足 schema、安全或蕴涵约束，系统进入 fallback 或 HITL，而不是继续生成
- **安全边界**: Critic 可以使用 LLM 做 entailment，但安全扫描和 schema 校验必须由确定性代码兜底

## 为什么 Critic 不能只是另一个 LLM

Reflexion 容易被误解为“让一个模型检查另一个模型”。在生产系统中，更稳的结构是分层批评者：

- 第一层检查格式和 schema，确保下游系统能解析。
- 第二层用确定性规则扫描禁忌输出、隐私泄露、危险建议和安全红线。
- 第三层才用 LLM 判断回答是否被证据支持、是否与检索上下文矛盾。
- 最后根据风险进入重试、拒绝或人工接管。

这样设计的原因很直接：LLM 适合做语义判断，但不适合承担不可绕过的安全边界。Reflexion 的工程价值在于把“模型自我感觉良好”改造成“可审计的失败反馈”。

## 前提与局限性

- **前提**: 需要明确定义的评估标准（格式、安全、蕴涵），否则批评者无法给出有效反馈
- **前提**: 重试有成本（延迟、token 消耗），需要设置合理的最大迭代次数
- **局限性**: 如果评估标准本身有缺陷，Reflexion 会反复尝试满足错误标准
- **局限性**: 对于需要全新思路的问题（而非渐进改进），重试可能无法突破
- **局限性**: Critic 与 Generator 若共享相同盲点，可能产生一致但错误的判断
- **局限性**: 高风险领域不能把 Reflexion 当作最终安全证明，它只能降低错误率，不能替代责任主体

## 关联概念

- [[Agent-Orchestration]] — Reflexion 是 Agent 编排中的关键反馈循环模式
- [[Corrective-RAG]] — Reflexion 常与 CRAG 配合，形成检索层+生成层的双重纠错
- [[Agentic-Engineering]] — Reflexion 是 Agentic 工程中提升输出可靠性的核心手段
- [[Zero-PHI-Policy]] — 医疗系统中，Critic 也必须处于去标识化数据边界内
- [[Evaluation-Set]] — Critic 规则和重试收益需要用失败样本评估
- [[Verifiable-Agent-Engineering]] — Reflexion 是输出验证和行为拒绝的核心机制
