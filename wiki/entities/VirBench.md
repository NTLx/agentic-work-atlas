---
type: entity
title: VirBench
aliases:
  - VirBench
definition: "一个针对科学研究智能体在病毒序列检索任务上的评估基准，包含 120 个具有手动验证 ground-truth 计数的真实查询。"
created: 2026-06-10
updated: 2026-06-10
tags:
  - benchmark
  - scientific-agents
related_entities:
  - "[[Scientific-Discovery-AI]]"
  - "[[gget-virus]]"
source_raw:
  - "[[20260608-paving-the-way-for-agents-in-biology]]"
---

# VirBench

> [!definition] 定义
> **VirBench** 是由 Anthropic 团队设计的基准测试，用于衡量科学智能体在操作 NCBI Virus 数据库时的准确性。

## 关键数据点
- 构成: 120 个真实查询，跨越 40 种病原体。
- 结果: 无工具时模型表现出极高的方差和低准确率（16.9% - 91.3%）。

## 前提与局限性
- **前提**: 需要人工验证的 Ground-truth 计数。
- **局限**: 目前仅限于病毒序列检索，尚未扩展到更广阔的生命科学实验领域。

## 关联概念
- [[Scientific-Discovery-AI]]
- [[gget-virus]]
- [[Deterministic-Retrieval]]
