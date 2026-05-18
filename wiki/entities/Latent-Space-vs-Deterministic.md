---
type: entity
title: Latent-Space-vs-Deterministic
aliases:
  - Latent Space vs Deterministic
  - 潜在空间 vs 确定性
definition: "GBrain 的核心设计洞察——让 LLM 在'潜在空间'（Latent Space）中决定'做什么'（判断、分析、综合），让代码在'确定性'（Deterministic）中保证'在哪里'和'如何做'（构建链接、验证格式、执行计算）"
created: 2026-05-13
updated: 2026-05-13
tags:
  - AI
  - agent
  - architecture
related_entities:
  - "[[GBrain]]"
  - "[[Thin-Harness-Fat-Skills]]"
source_raw:
  - "[[深度解析LLM Wiki  Obsidian-Wiki  GBrain：Agent时代知识的“自组织”与“自进化”]]"
---

# Latent-Space-vs-Deterministic

> [!definition] 定义
> **潜在空间 vs 确定性（Latent Space vs Deterministic）** 是 GBrain 的核心设计洞察：最差的 Agent 系统总是把错误的工作放在错误的一边。正确的分工是——让 LLM 在"潜在空间"中决定"做什么"（判断、分析、综合），让代码在"确定性"中保证"在哪里"和"如何做"（构建交叉验证链接、验证引用格式、执行精确计算）。

## 关键数据点

| 对比维度 | 潜在空间（Latent Space） | 确定性（Deterministic） |
|---------|------------------------|------------------------|
| 特点 | 智能——阅读、解释、决策 | 信任——相同输入总是产生相同输出 |
| 适合场景 | 判断、分析、综合 | SQL、计算、链接构建 |
| 执行者 | LLM 处理 | 代码处理 |
| 示例 | "这条信息是否属于某人的页面" | 构建交叉验证链接、验证引用格式 |

## 前提与局限性

- 潜在空间与确定性的边界划分依赖领域理解——如果边界划错，可能让 LLM 做它不擅长的事或浪费代码实现灵活性
- LLM 在潜在空间中的判断可能存在幻觉和不一致性
- 确定性代码的维护成本随规则复杂度增长
- 两者的交互接口设计是关键——LLM 的判断结果如何可靠地传递给确定性代码层

## 关联概念

- [[GBrain]] — 潜在空间 vs 确定性是 GBrain 架构的核心设计洞察
- [[Thin-Harness-Fat-Skills]] — Harness 中的确定性逻辑，Skills 中的潜在空间判断
- [[Jagged-Intelligence]] — LLM"代码超人、常识脆弱"的锯齿状智能是这种分工的基础
- [[Verifiability]] — 确定性代码提供了可验证性保障，潜在空间输出则需要人工验证
