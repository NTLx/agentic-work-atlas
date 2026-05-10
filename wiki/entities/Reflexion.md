---
type: entity
title: Reflexion
aliases:
  - Reflexion
  - Reflexion Agent
definition: "一种通过语言反馈实现自我纠正的 Agent 模式，Agent 生成输出后由批评者评估，失败反馈注入上下文进行重试。由 Shinn et al. (2023) 在 NeurIPS 提出。"
created: 2026-05-10
updated: 2026-05-10
tags:
  - AI-Architecture
  - Multi-Agent
  - Agent-Pattern
related_entities:
  - "[[Agent-Orchestration]]"
  - "[[Agentic-Engineering]]"
  - "[[Corrective-RAG]]"
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

## 前提与局限性

- **前提**: 需要明确定义的评估标准（格式、安全、蕴涵），否则批评者无法给出有效反馈
- **前提**: 重试有成本（延迟、token 消耗），需要设置合理的最大迭代次数
- **局限性**: 如果评估标准本身有缺陷，Reflexion 会反复尝试满足错误标准
- **局限性**: 对于需要全新思路的问题（而非渐进改进），重试可能无法突破

## 关联概念

- [[Agent-Orchestration]] — Reflexion 是 Agent 编排中的关键反馈循环模式
- [[Corrective-RAG]] — Reflexion 常与 CRAG 配合，形成检索层+生成层的双重纠错
- [[Agentic-Engineering]] — Reflexion 是 Agentic 工程中提升输出可靠性的核心手段
