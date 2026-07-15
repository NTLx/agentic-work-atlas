---
type: entity
title: Self-Hosted Models
aliases:
  - self-hosted models
  - 自托管模型
  - local models
definition: "组织自行托管开源/开放权重模型而非依赖前沿模型 API 的实践。驱动力包括：token 成本上升、模型主权需求、信息安全约束、以及开源模型追赶前沿模型的速度加快。"
created: 2026-07-14
updated: 2026-07-14
evidence_level: medium
claim_type: extracted
tags:
  - infrastructure
  - models
  - sovereignty
related_entities:
  - "[[Agent-Harness]]"
  - "[[Enterprise-AI-Model-Sourcing]]"
  - "[[Closed-Frontier-Models-vs-Open-Model-Economy]]"
source_raw:
  - "[[20260713-martin-fowler-fragments-july-2026]]"
---

# Self-Hosted Models

> [!definition] 定义
> **Self-Hosted Models** 是组织自行托管开源/开放权重模型而非依赖前沿模型 API 的实践。驱动力不仅是成本，还包括模型主权、信息安全和独立性。

## 驱动力

1. **Token 成本上升**：增加的成本使自托管开放权重模型更有吸引力
2. **追赶速度加快**：开源模型追赶前沿模型的时间在缩短（RedMonk, 2026）
3. **模型主权**：美国政府曾干预以拒绝模型访问，增加了独立性需求
4. **信息安全**：某些场景无法向外部模型提供必要数据
5. **学习归属**："if someone else hosts the model then their model learns rather than your model"

## 当前最佳实践

Thoughtworks FOSE retreat 参与者报告：
- **Qwen 3.6** 是当前本地 agentic programming 的最佳平衡点（Birgitta Böckler, Sebastian Raschka）
- 部分公司已自托管长达两年

## 与 Private Cloud 的历史类比

Martin Fowler 提出的关键问题：Self-hosted models 是否会重蹈 **half-arsed private clouds** 的覆辙？

答案取决于：模型托管是否比云托管更简单（可能因为更简单的交互协议）。

硬约束：
- GPU 人才稀缺——管理推理数据中心不是广泛可用的技能
- 资本成本（GPU）和持续成本（电力）
- 数据中心的物理设计影响最优使用

可能的演化：
- **Fine-tuning** 与自托管结合——领域特定模型需要更少推理、消耗更少 token、运营成本更低
- **Model broker**——模型自身充当经纪人，决定哪个模型最适合特定任务
- 专业服务公司帮助企业管理自托管模型

## 策略建议

"the big win isn't finding the right answer, but coming up with a strategy that will cope with the inevitable and unpredictable changes."（Martin Fowler）

## 前提与局限性

- GPU 人才稀缺是硬约束，短期内难以缓解
- 云服务商可能很快提供托管推理服务降低门槛
- Self-hosting 的兴趣可能部分是过渡期现象
- 开放权重模型追赶速度是经验观察，可能放缓

## 关联概念

- [[Agent-Harness]] — 自托管模型需要对应的 harness 调优
- [[Enterprise-AI-Model-Sourcing]] — 自托管是模型采购策略的一种
- [[Closed-Frontier-Models-vs-Open-Model-Economy]] — 自托管位于开放模型经济的一端
- [[Harness-Engineering]] — 自托管模型的 harness 可能需要更厚的控制层

## 关键数据点

- Thoughtworks FOSE retreat (2026-07): Qwen 3.6 被认为是当前本地 agentic programming 的最佳平衡点（Birgitta Böckler, Sebastian Raschka）
- RedMonk (2026): 开源模型追赶前沿模型的时间在缩短
- 部分公司已自托管长达两年
