---
type: entity
title: Features Are Cheap Paradox
aliases:
  - Features Are Cheap Paradox
  - Features Cheap Paradox
  - Cheaper Features
  - Feature Economics Phase Change
definition: "AI 时代 feature 边际生成成本骤降带来的相变——'Features are cheap, that doesn't mean you should build them all'；选择标准从'能不能做'变成'哪些不该做'，prioritization、taste、judgment 比 feature 实现能力更稀缺"
created: 2026-08-20
updated: 2026-08-20
tags:
  - product-strategy
  - agentic-engineering
  - prioritization
  - jevons-paradox
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[Jevons-Paradox-for-Knowledge-Work]]"
  - "[[Captain-Mindset]]"
  - "[[Just-Do-Less]]"
  - "[[Capability-Overhang]]"
  - "[[Taste-vs-Judgment]]"
  - "[[Simon-Willison]]"
source_raw:
  - "[[20260820-talking-postgres-simon-willison-ai]]"
---

# Features Are Cheap Paradox（Feature 廉价悖论）

> [!definition] 定义
> **Features Are Cheap Paradox** 是 Simon Willison 在 Talking Postgres Ep 42 中强调的相变命题：**"Features are cheap. That doesn't mean you should build them all."**——当 AI 让 feature 边际生成成本骤降（小时级而非周级），"能不能做"不再是问题；新的稀缺资源是 prioritization、taste、judgment——"哪些 feature 不该做"的判断力。这是 [[Jevons-Paradox-for-Knowledge-Work]] 在产品域的具象。

## 相变前后对比

| 维度 | 廉价前 | 廉价后 |
|------|--------|--------|
| 主导稀缺资源 | 实现能力（编码时间） | 判断力（哪个不做） |
| 关键决策 | "能不能做？" | "该不该做？" |
| 团队瓶颈 | engineer hours | product judgment |
| 失败模式 | 工程延期 | feature bloat + 用户认知过载 |
| 关键人物 | engineer | product manager / designer with taste |
| 评估标准 | on-time delivery | outcome impact |

## 与 Jevons Paradox 的同构

- **Jevons 悖论**: 煤炭效率提升 → 总消耗上升（成本降低 → 使用增加）
- **Features Cheap 悖论**: feature 实现成本降低 → total feature 数上升，但使用价值不增

廉价悖论不是单纯"做更多"，而是"做更多 ≠做好"——选择标准从"生产可能性"翻转到"选择必要性"

## 跨域对标

- **[[Jevons-Paradox-for-Knowledge-Work]]**: 知识工作产出效率提升 → 知识工作总产出上升，但"产能"不等于"价值"
- **[[Capability-Overhang]]**: 用户使用率（vast majority using a sliver of true value）——廉价悖论的另一面：用户用不完所有 features
- **[[Just-Do-Less]]**: OpenAI Head of Design 主张克制新建、复用 primitives——廉价悖论在产品决策层的应用
- **[[Captain-Mindset]]**: 管理 skill 在 agent 时代复归——judgment 比 execution 稀缺
- **[[Taste-vs-Judgment]]**: "哪些 feature 不该做"是 judgment 而非 taste 的体现

## 关键数据点

- 提出者: Simon Willison（Talking Postgres Ep 42, 51:57 节）
- 同主题节目: 1:00:45 节 "Engineering management skills are so useful"
- 跨域证据: [[Capability-Overhang]] 指出多数用户只使用 5% features，廉价悖论放大了这一浪费

## 前提与局限性

- **前提 1**: feature 实现成本确实骤降（小时/天级），尚未达成的领域不适用
- **前提 2**: 用户需求过载（feature 太多→用户认知过载），需求欠载场景不适用
- **不替代工程标准**: 廉价不是"随便做"，单 feature 质量仍需 [[Explain-Test-Gold-Standard]] 等判据
- **悖论的解药不是少做**: 是"做对的事"——prioritization 是新的工程能力

## 应对策略

1. **产品层**: 引入"feature kill list"——主动列出不做的事项
2. **团队层**: prioritization 能力纳入招聘与晋升标准
3. **流程层**: 每个 feature 提案需回答"为什么这个值得做"（替代"为什么这个能做"）
4. **个人层**: 培养 judgment / taste / product sense——它们在廉价时代升值

## 关联概念

- [[Jevons-Paradox-for-Knowledge-Work]] — 知识工作领域的同构悖论
- [[Capability-Overhang]] — 廉价放大了 overhang
- [[Just-Do-Less]] — 产品决策层的应用
- [[Captain-Mindset]] — 管理 skill 复归
- [[Taste-vs-Judgment]] — judgment 取代 execution 的稀缺性
- [[Simon-Willison]] — 概念提出者