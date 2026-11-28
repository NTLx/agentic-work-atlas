---
type: entity
title: CORE-Bench
aliases:
  - CORE-Bench
  - Computational Reproducibility Agent Benchmark
  - 计算可复现性智能体基准
definition: "评估 Agent 根据研究论文的代码与计算环境复现指定研究结果的基准；不等同通用推理、实际科学发现或任务视野测量。"
created: 2026-06-06
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - benchmark
  - reasoning
  - AI-evaluation
related_entities:
  - "[[SWE-Bench]]"
  - "[[Task-Horizon]]"
  - "[[Agentic-Engineering]]"
source_raw:
  - "[[20260604-anthropic-recursive-self-improvement]]"
---

# CORE-Bench

> [!definition] 定义
> CORE-Bench（Computational Reproducibility Agent Benchmark）面向科学论文的计算可复现性任务。原始论文描述了来自计算机科学、社会科学、医学三个领域的90篇论文及270项任务。给定论文相关代码与任务，三个难度层级分别提供已有计算输出、Dockerfile 或仅代码及说明；Easy 主要提取结果，Medium/Hard 涉及运行或建立计算环境。270项任务对应181个问题，并非270篇独立论文。原论文 Table 5 中最佳基线 CORE-Agent/GPT-4o 的 Hard 平均准确率21.48%，不是所有设置的起始通过率。并非 Computer-Use Reasoning Benchmark 或通用复杂推理基准。

## 关键数据点

- 定义核查：原论文 [arXiv:2409.11363](https://arxiv.org/html/2409.11363) 摘要及第2节；[作者仓库](https://github.com/siegelz/core-bench)。一手来源用于勘误，待正式来源晋升，不新增 source_raw。
- 已有 Anthropic 2026-06-04 报告将 CORE-Bench 从低个位数到饱和概括为约15个月。该句不是完整的可比时间序列；本轮未核各模型、难度分层、版本、执行预算与饱和阈值，不将其当作领域进步速度的定量证明。
## 前提与局限性

- 成功复现指定计算结果不等于证实论文假设、真实世界效果、方法独立性或新的科学发现。评测结果也受环境、依赖、评分与模型/harness 组合影响。
- [[SWE-Bench]] 评估软件问题解决，[[Task-Horizon]] 估计给定成功率下相应的人类任务时长；不同目标、分母和评分规则，不能直接据饱和用时比较通用推理进步速度。

## 关联概念

- [[SWE-Bench]] — 软件问题解决基准
- [[Task-Horizon]] — 另一类能力度量，不由 CORE-Bench 分数直接推出
- [[Agentic-Engineering]] — 计算环境、代码与结果验证
