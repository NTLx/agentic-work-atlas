---
type: entity
title: Sample Efficiency
aliases:
  - Sample Efficiency
  - 样本效率
  - Training Sample Efficiency
definition: "智能体为达到特定业务流利度和胜任力所需要接触/训练的数据量。样本效率高意味着使用更少的数据就能学会新知识或新技能。"
created: 2026-06-20
updated: 2026-06-20
tags:
  - concept
  - AI-scaling
  - cognitive-science
evidence_level: high
claim_type: mixed
related_entities:
  - "[[Amortized-Intelligence]]"
  - "[[API-Distillation-Catch-Up]]"
  - "[[World-Model]]"
  - "[[AI-Labor-Bottleneck-Shift]]"
source_raw:
  - "[[20260619-the-data-black-hole-at-the-center-of-ai]]"
---

# Sample-Efficiency（样本效率）

> [!definition] 定义
> **Sample-Efficiency（样本效率）** 是衡量一个智能体（人类或 AI）学习效率的核心指标。它定义为在给定领域中，为了达到特定的流利度、胜任力和操作水平，所需要接触或训练的数据总量。样本效率越高，学习新技能所需的数据量就越小。

## 核心差异：人类与 AI 的样本效率对比

目前前沿 AI 模型在样本效率上与人类相比存在 **3 到 6 个数量级** 的巨大鸿沟：

| 学习任务 | 人类学习数据量 | AI 学习数据量 | 数量级差距 |
|------|------|------|------|
| **语言与通用认知** | 约 `2亿` tokens（从出生到成年人平均听/见单词量）<br>即使算上全部多模态感官数据也仅在 `100亿` 到 `1000亿` tokens | 预训练需要数万亿至 `100万亿` 以上 tokens | **百万倍（6个数量级）** |
| **驾驶技术** | 约 `20小时` 的驾驶练习 | Tesla/Waymo 自动驾驶需要数十亿至数百亿英里的路测与模拟数据 | **3-4 个数量级** |
| **机器人操纵** | 约 `几小时` 的人类示范 | 数百万乃至上千万小时的动作数据和强化学习探索 | **3-4 个数量级** |

## 缩放定律的局限性

根据 Chinchilla 等缩放定律的数学表达式，参数量（Parameters）和训练数据量（Data）是独立对模型损失函数（Loss）做出贡献的。
即使通过增加无限的参数来试图最大化样本效率（在保持相同 Loss 的前提下尽量减少数据量），数学 constants 限制表明：
- **无限的参数量增加也仅仅能将所需的数据量减少约 10 倍。**
- 这一数学瓶颈表明，人类和当前的 Transformer 模型在根本上处于**完全不同的缩放曲线（Scaling curves）**上。人类大脑的高样本效率无法简单通过增加当前的参数规模来等效实现。

## 关键数据点

- **语言数据对比**：人类成年期前 ingests 约 2 亿 tokens，而前沿大模型使用 10T - 100T tokens。
- **参数与数据权衡**：理论上参数无限大时，数据需求量减少上限仅为 10 倍（基于 Chinchilla constants）。
- **基因预训练说反驳**：人类基因组仅 3GB 且仅 1-2% 编码蛋白质，无法存储等效于 Frontier Models 万亿参数量级的预训练权重；进化的贡献可能在于优化了损失函数与学习算法，但参数训练本身依旧是在极高样本效率下完成的。

## 前提与局限性

- **多模态对齐**：对人类 tokens 接触量的估算若将高分辨率视觉、听觉等全部多模态感官流转化为 token 计，人类数据规模将显著上升（达到百亿至千亿级），这在一定程度上会缩小纯语言 token 计算下的极端代差，但即使如此，差距依然存在数万倍。
- **任务局限性**：高样本效率学习主要体现在通用常识、物理世界交互（如驾驶、操纵）以及人类已有先验知识中。对于没有任何人类先验的纯抽象规则系统（如围棋、蛋白质折叠），AI 通过强化学习（RL）自我博弈的低效率是可以被物理计算速度抵消的。

## 关联概念

- [[Amortized-Intelligence]] — 摊销智能是抵消低样本效率高昂代价的经济手段。
- [[API-Distillation-Catch-Up]] — 数据蒸馏是当前非样本效率优化下，各模型快速缩短差距的路径。
- [[World-Model]] — 物理世界的“世界模型”是人类拥有极高样本效率的先验基础。
- [[AI-Labor-Bottleneck-Shift]] — 样本效率的缺失导致 AI 在面对全新的、OOD 的长尾任务时依然极其依赖人类专家数据。
