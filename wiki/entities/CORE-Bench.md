---
type: entity
title: CORE-Bench
aliases:
  - CORE-Bench
  - CORE-Bench (Computer-Use)
  - 复杂推理基准
definition: "复杂推理任务的标准化评测基准——评估 AI 在多步推理、跨域知识整合、长时间视野任务上的能力；从 2024 的低个位数涨到 2026 接近饱和（约 15 月周期）"
created: 2026-06-06
updated: 2026-06-06
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
> **CORE-Bench (Computer-Use Reasoning Benchmark)** 是复杂推理任务的标准化评测基准——评估 AI 在多步推理、跨域知识整合、长时间视野任务上的能力。从 2024 的低个位数涨到 2026 接近饱和（约 15 月周期）。

## 关键数据点

- 起点（2024）：个位数通过率
- 终点（2026）：接近饱和
- 周期：约 15 月
- 与 [[SWE-Bench]] 对比：CORE-Bench 饱和周期更短（15 月 vs 24 月），说明 reasoning 维度进步更快
- 是 [[Task-Horizon]] 度量的配套 benchmark

## 前提与局限性

- 前提：任务可被设计成"可自动评分"
- 局限：单一 benchmark 可被针对性优化；任务定义本身可能有偏
- 配合 [[SWE-Bench]] 一起看更全面

## 关联概念

- [[SWE-Bench]] — 软件工程任务基准
- [[Task-Horizon]] — 任务视野度量
- [[Agentic-Engineering]] — 工程范式
