---
type: entity
title: Model Distillation
aliases:
  - Model Distillation
  - 模型蒸馏
  - Knowledge Distillation
definition: "把大模型（教师）的能力压缩到小模型（学生）的技术，使更小更快的模型继承大模型的推理能力"
created: 2026-05-30
updated: 2026-05-30
tags:
  - AI
  - machine-learning
related_entities:
  - "[[Adversarial-Distillation]]"
  - "[[Continual-Learning]]"
  - "[[World-Model]]"
  - "[[Agentic-Engineering]]"
source_raw:
  - "[[20260529-gemini-co-leads-origins]]"
---

# Model Distillation（模型蒸馏）

> [!definition] 定义
> **Model Distillation** 是把大模型（教师）的推理能力转移到小模型（学生）的技术。学生模型不需要看到原始训练数据，而是从教师的软标签（soft labels）或输出来学习，从而用更少的参数、更低的推理成本获得接近教师的能力。

## 为什么重要

模型蒸馏是"每一代小模型超越前代大模型"这一现象的核心引擎。它意味着：

1. **能力民主化**：昨天只有旗舰模型能做的事，明天小模型也能做——降低推理成本、扩大部署场景
2. **算法复利**：蒸馏让每代架构改进、数据改进、训练改进的成果被压缩到更小的模型中，形成累积效应
3. **产品杠杆**：小模型更快、更便宜、延迟更低，直接转化为用户体验优势

蒸馏也揭示了模型能力的**可压缩性**——大量"智能"可以被装进更少的参数，这暗示当前模型可能远未达到其信息论容量上限。

> [!important] 与 Adversarial Distillation 的区别
> **Model Distillation**（本文）是机器学习技术——教师模型输出软标签，学生学习分布。
> **[[Adversarial-Distillation|Adversarial Distillation]]** 是组织行为学概念——工程师为避免被 Skills 系统替代而采取消极抵抗、质量投毒、上下文污染等策略。
> 二者同名但完全不同层面：技术蒸馏几乎没有遇到组织蒸馏面临的激励和信任问题。

## 关键数据点

- **Gemini Flash 代际超越 Pro**：每一代 Flash 模型都超越前代 Pro 模型，且这个趋势似乎在加速（Oriol Vinyals, 2026-05）
- **方法出奇简单**：Jeff Dean 确认 Gemini 蒸馏"甚至比最初的论文更简单"——一个好老师 + 一个学生，基本沿用 Hinton 2015 年原始论文 recipe，加上"modest tweaks"
- **早期规模化验证**：2012-2013 年 Jeff Dean 和 Oriol Vinyals 在 Google Brain 用 50 个模型的 ensemble 训练了 3 亿张图片，然后通过蒸馏压缩为单一模型——精度远超直接在原始数据上训练的单模型
- **"挤柠檬"隐喻**：Oriol Vinyals 描述蒸馏为"squeezing the lemon"——把大模型的"汁液"（好的部分）压进小模型
- **LLM 数据效率差距**：人类一生听到约 `10^9`（10 亿）词，LLM 在 `10^{12}`（万亿）词上训练——效率差约 1000 倍。蒸馏和算法创新是缩小这个差距的关键方向

## 前提与局限性

- **信息论地板**：蒸馏不可能把无限知识压进有限参数。"每代 Flash > 前代 Pro"的趋势终将遇到模型容量的理论上限
- **教师质量上界**：学生的能力天花板由教师决定。如果教师模型在某个领域表现不佳，蒸馏无法创造新能力
- **创造者困惑**：Oriol Vinyals 承认"I'm still mesmerized how can we pack so much intelligence per parameter"——连技术的创造者也不完全理解其有效性的边界
- **与推理时计算的区别**：蒸馏压缩的是训练时获得的知识，不替代推理时的思考预算（thinking tokens）。二者是互补关系

## 关联概念

- [[Adversarial-Distillation]] — 同名但不同层面的概念：组织知识抽取中的抵抗行为
- [[Continual-Learning]] — 蒸馏传递的是训练时的快照知识，不替代运行时的持续学习
- [[World-Model]] — 蒸馏能否传递世界模型（因果结构）vs 只是传递统计模式，是开放问题
- [[Agentic-Engineering]] — 小模型的低延迟对 Agent 工具链至关重要
