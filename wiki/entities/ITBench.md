---
type: entity
title: "ITBench"
aliases:
  - ITBench-AA
  - ITBench-AA SRE
definition: "Artificial Analysis 与 IBM 联合开发的企业 IT Agent 基准测试，评估前沿模型在 SRE、FinOps 和 CISO 任务上的 agentic 表现。"
created: 2026-05-28
updated: 2026-06-16
evidence_level: medium
claim_type: mixed
tags:
  - agent-evaluation
  - agentic-engineering
  - benchmark
related_entities:
  - "[[Agentic-Engineering]]"
  - "[[Agent-Harness]]"
  - "[[Verifiability]]"
  - "[[Agentic-Workflow-Token-Efficiency]]"
source_raw:
  - "[[ITBench-AA Frontier Models Score Below 50% on the First Benchmark for Agentic Enterprise IT Tasks — by Artificial Analysis and IBM]]"
---

# ITBench

> [!definition] 定义
> ITBench 是 Artificial Analysis 与 IBM 联合开发的企业 IT Agent 基准测试系列，首发 SRE（站点可靠性工程）任务集。模型在 Kubernetes 事件快照中通过 shell 命令调查 alerts、traces、logs 和 topology，识别最小根因 Kubernetes 实体集。评分使用 recall-gated precision——漏掉任何真实根因得 0 分，多报则按 precision 扣分。

## 关键数据点

- 首发 59 个 SRE 任务（40 公开 + 19 held-out），使用 Stirrup 开源参考 harness，100 轮上限，每任务 3 次重复
- 2026-05 排行榜：Claude Opus 4.7（Adaptive Reasoning, Max Effort）47% 领先，GPT-5.5（xhigh）46%，Qwen3.7 Max 42%
- **所有前沿模型低于 50%**，是 Artificial Analysis 评测套件中最不饱和的 agentic benchmark
- 轮次差异近 3×：GPT-5.5 平均 31 轮得 46%，Gemini 3.1 Pro Preview 83 轮得 30%
- 开源权重成本前沿：Gemma 4 31B（37%, `$0.14`/task）同时击败 Gemini 3.1 Pro（30%, `$2.23`）的分数和成本
- GLM-5.1（Reasoning）40% 为开源最高，追平 Gemini 3.5 Flash（high）40% 但成本更低（`$1.23` vs `$1.70`）

## 前提与局限性

- **SRE 领域限定**: 当前仅覆盖 Kubernetes SRE 任务，FinOps 和 CISO 任务尚在开发中。模型在其他 IT 任务上的表现可能不同
- **评分方式偏向保守**: Recall-gated precision 对 false positive 极度惩罚，在真实 SRE 场景中"给出多个候选让人类筛选"可能更有实用价值
- **Effort level 不可比**: 不同模型的推理模式（Adaptive Reasoning / xhigh / Reasoning）设置不同，跨模型 effort level 比较存在公平性问题
- **Harness 依赖**: 使用 Stirrup 作为固定 harness 确保 apples-to-apples 对比，但不同 harness 可能改变排行榜

## 关联概念

- [[Agentic-Engineering]] — ITBench 为 agentic engineering 提供企业级能力基线
- [[Agent-Harness]] — Stirrup 参考 harness 固定后实现公平对比
- [[Verifiability]] — Recall-gated precision 是结果可验证性的极端形式
- [[Agentic-Workflow-Token-Efficiency]] — "更多轮次 ≠ 更好结果"揭示 token 效率约束的必要性
