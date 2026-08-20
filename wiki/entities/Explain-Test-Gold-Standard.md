---
type: entity
title: Explain Test Gold Standard
aliases:
  - Explain Test Gold Standard
  - Could I Explain This
  - Simon Willison Gold Standard
  - 可解释性金标准
definition: "Simon Willison 提出的 AI 生成代码可上线判据——'Could I explain this code to somebody else?' 是判断生成代码是否真正可用的金标准，单纯测试通过不够，因为测试可与实现相洽但与意图脱节"
created: 2026-08-20
updated: 2026-08-20
tags:
  - verification
  - agentic-engineering
  - code-review
  - evaluation-criteria
evidence_level: medium
claim_type: extracted
related_entities:
  - "[[Agent-Verification]]"
  - "[[Rubric-Based-Evaluation]]"
  - "[[Code-Cleanliness-Agent-Footprint]]"
  - "[[Simon-Willison]]"
  - "Verifier Mental Model（forward reference，未建 entity）"
source_raw:
  - "[[20260820-talking-postgres-simon-willison-ai]]"
---

# Explain Test Gold Standard（可解释性金标准）

> [!definition] 定义
> **Explain Test Gold Standard** 是 Simon Willison 在 Talking Postgres Ep 42 中提出的 AI 生成代码可上线判据：**"Could I explain this code to somebody else?"**——把"理解保真"作为生成代码可上线的金标准，单纯测试通过不够，因为测试可与实现相洽但与意图脱节。"解释能力"在 review 现场同时验证 reviewer 理解深度与意图保真度。

## 核心逻辑

```
AI 生成代码 → 通过测试 → 可上线？
    ↓
不够。测试可与"看起来对"的实现相洽
    ↓
真正的金标准：能否向同等水平工程师清晰解释代码做什么、为什么这样做
    ↓
解释动作同时验证：
  - reviewer 真的理解代码（不是表面 review）
  - 代码与意图一致（不是过度复杂/缺意图的实现）
  - 可维护性（能解释的代码才能被未来维护者改）
```

## 与传统判据的对比

| 判据 | 测试什么 | 失效模式 |
|------|----------|----------|
| 测试通过 | 输出与期望匹配 | 测试可与"看起来对"的实现相洽，与意图脱节 |
| Lint/type check | 形式合规 | 形式合规≠语义正确 |
| LLM-as-judge | 与 ground truth 接近 | 校准错误、模型偏误 |
| **Explain Test** | **理解保真 + 意图保真** | reviewer 先验差异；解释颗粒度模糊 |

## 适用边界

- **前提 1**: reviewer 与 author 是同等水平或以上的工程师
- **前提 2**: 代码有清晰的"做什么"和"为什么这样做"可解释
- **不适用**: trivial boilerplate（无解释价值）；高度依赖 framework 内部机制的代码（解释成本极高）
- **不替代**: 测试是必要不充分条件——可解释代码仍需测试

## 应用到非代码领域

Simon Willison 的金标准适用于一切 AI 生成产物：

- SQL query → 能向 DBA 解释 join 选择
- Commit message → 能向 reviewer 解释为什么这样写
- Agent trajectory → 能向 stakeholders 解释 agent 为什么走这条路
- Documentation → 能向新人解释如何使用

## 与现有 concept 的关系

- [[Agent-Verification]] — Explain Test 是 verification 在"理解保真"维度的具象化
- [[Rubric-Based-Evaluation]] — Explain Test 可作为 rubric 中的一项 binary check
- [[Code-Cleanliness-Agent-Footprint]] — 可解释的代码通常也是结构整洁的；两者正相关
- [[Slop-Proxy]] — Slop 是不可解释的伪装产出，Explain Test 是对抗 Slop 的关键工具

## 关键数据点

- 提出者: Simon Willison（Talking Postgres Ep 42, 23:01 节）
- 适用域: 一切 AI 生成代码与产物
- 与 [[Code-Cleanliness-Agent-Footprint]] 同向：file revisitation −34% 与 explainability 高相关

## 前提与局限性

- **依赖 reviewer 先验**: 资深工程师 5 秒解释 vs 新人 5 小时——"同等水平"假设
- **不适用 trivial 代码**: 重复样板不增加解释价值
- **不替代 testing**: 解释不验证正确性，只验证意图保真
- **解释颗粒度主观**: 解释到什么程度算"清晰"无统一标准

## 关联概念

- [[Agent-Verification]] — verification 的具体形态
- [[Rubric-Based-Evaluation]] — explain 可作为 rubric 检查项
- [[Simon-Willison]] — 概念提出者
- [[Code-Cleanliness-Agent-Footprint]] — explainable code 通常也是 clean code
- Verifier Mental Model（forward reference，未建 entity） — verifier 视角下 explain test 的价值
- [[Slop-Proxy]] — 反面：不可解释的产出是 slop proxy