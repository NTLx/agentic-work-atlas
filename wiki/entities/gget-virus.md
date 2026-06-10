---
type: entity
title: gget virus
aliases:
  - gget-virus
definition: "由 Laura Luebbert 等人开发的确定性检索工具，旨在将 NCBI Virus 等复杂生物数据库的过滤和检索逻辑封装为机器可读的编程接口。"
created: 2026-06-10
updated: 2026-06-10
tags:
  - tools
  - biology
  - scientific-agents
related_entities:
  - "[[Deterministic-Retrieval]]"
  - "[[Scientific-Discovery-AI]]"
  - "[[Biological-Data-Infrastructure]]"
source_raw:
  - "[[20260608-paving-the-way-for-agents-in-biology]]"
---

# gget virus

> [!definition] 定义
> **gget virus** 是 `gget` 开源生态中的一个模块。它在 NCBI Virus 数据库之上构建了一个隧道，解决了 virologist 在手动点击 Web 界面时面临的重复劳动问题，并使其可被 AI Agent 高效、准确地调用。

## 关键数据点
- 效果: 将检索准确率从 16.9% 提升至 99.7%。
- 整合: 跨越了多个底层 API（REST, Datasets, E-utilities）。

## 前提与局限性
- **前提**: 依赖 NCBI 提供的底层 API 稳定性。
- **局限**: 专注于病毒数据，其他生物领域需要类似的封装。

## 关联概念
- [[Deterministic-Retrieval]]
- [[Scientific-Discovery-AI]]
- [[Biological-Data-Infrastructure]]
