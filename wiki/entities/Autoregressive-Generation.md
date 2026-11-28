---
type: entity
title: Autoregressive Generation
aliases:
  - 自回归生成
  - 自回归
definition: "按条件概率逐步生成序列的一种方式；生成因子分解不直接限定模型的全局规划、推理或跨域连接能力。"
created: 2026-07-01
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - AI-capabilities
  - LLM
related_entities:
  - '[[AI-in-Mathematics]]'
  - '[[Conceptual-Breakthroughs]]'
  - '[[Sample-Efficiency]]'
source_raw:
  - '[[20260701-grant-sanderson-ai-math-future]]'
---

# Autoregressive Generation

> [!definition] 定义
> 自回归生成将序列联合概率分解为前缀条件概率，逐步采样或解码。模型可能利用完整可见前缀、工具、搜索及训练形成的表示；逐token生成并不逻辑蕴含缺乏全局结构。

## 核心要点

[原访谈](https://www.dwarkesh.com/p/grant-sanderson-2) 00:38:08后讨论跨领域连接与“刷新思路”。Sanderson提出架构及搜索疑问，Patel强调训练数据、任务与环境，二者未证明自回归存在跨域能力上限。2026单位距离反证使用代数数论处理离散几何，提示跨域连接已可在特定任务实现；见 [[AI-Mathematics-Future]]。不由此推出通用创造力。

并行候选、重新规划、重置上下文及探索不同证明/反证方向均可测试；候选相关性、预算、停止规则及验收应对照，增加熵不保证更好。原“扩散全局视野强、自回归弱、扩散跨域强”表无共同模型/任务对照，退役；扩散与自回归的生成方式不同，文本/图像均可采用多种方式。

## 关键数据点

2026单位距离反证提供具体跨领域连接实例；其原创性、数学正确性和生成机制贡献分别评价，参见 [[AI-Mathematics-Future]]。没有统一对照数据支持扩散/自回归的能力排序。

## 前提与局限性

- 生成概率、训练数据、搜索策略、工具及后训练的贡献不能由输出机制单独识别。
- 需要同任务、相当资源及独立验收；不把模型生成解释当内部机制证明。

## 关联概念

- [[AI-in-Mathematics]] — 自回归的局限性影响AI的数学能力
- [[Conceptual-Breakthroughs]] — 概念突破需要跨领域连接，自回归难以产生
- [[Sample-Efficiency]] — 自回归的并行化限制了样本效率

## 来源

- [[20260701-grant-sanderson-ai-math-future]] — Grant Sanderson与Dwarkesh Patel的播客访谈