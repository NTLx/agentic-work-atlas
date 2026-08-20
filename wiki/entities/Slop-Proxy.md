---
type: entity
title: Slop Proxy
aliases:
  - Slop Proxy
  - Slop Proxies
  - proxy work
definition: "AI 时代特有的'产出替代品'——用 AI 生成可见但无实际价值的产出作为工作证明（如刷 PR 数、堆 commit、写 AI 长文），表面在工作但 bypass 了 review / verification / impact 等真实信号；与 [[Slopocalypse]] 同源但更具体"
created: 2026-08-20
updated: 2026-08-20
tags:
  - content-quality
  - software-engineering
  - slopocalypse
  - metrics-anti-pattern
evidence_level: medium
claim_type: extracted
related_entities:
  - "[[Slopocalypse]]"
  - "[[Goodharts-Law]]"
  - "[[AI-Adoption-Barbell]]"
  - "Verifier Mental Model（forward reference，未建 entity）"
  - "[[Simon-Willison]]"
  - "[[Explain-Test-Gold-Standard]]"
source_raw:
  - "[[20260820-talking-postgres-simon-willison-ai]]"
---

# Slop Proxy（Slop 替代品）

> [!definition] 定义
> **Slop Proxy** 是 Simon Willison 在 Talking Postgres Ep 42 中提出的概念：用 AI 生成"看起来在工作"的产出（PR/commit/文章/issue/会议摘要）作为工作证明——可见但 bypass 了 review / verification / impact 等真实信号。**"Slop proxies add no value at all."** 与 [[Slopocalypse]] 同源但更具体：Slopocalypse 是现象，Slop Proxy 是其中"伪装工作"的子集。

## 形式

| 形态 | 表面 | 实际 |
|------|------|------|
| 刷 PR 数 | "我今天贡献了 10 个 PR" | PR 未 review、未验证、未产生 impact |
| AI 长文 | "我写了 AI 行业分析" | 无独立判断，是 LLM 输出的拼接 |
| 会议摘要 | "我整理了会议纪要" | 无 action item 闭环，仅文本搬运 |
| 自动 commit | "今天提交 50 次" | 大块代码改动未验证，影响其他 reviewer |
| 自动化 issue | "bot 自动开了 100 个 issue" | noise > signal，需要人工清理 |

## 与 Slopocalypse 的关系

- **[[Slopocalypse]]**: AI 生成内容大规模涌入平台的总现象
- **Slop Proxy**: Slopocalypse 中**伪装工作产出**的特定子集——绕过 verification 的"成果"

Slop Proxy 与 [[Goodharts-Law]] 直接对应：当 metrics（PR 数、文章数、commit 数）成为目标，就不再是好的度量

## 与 Metrics Anti-pattern 的同构

- **Activity metrics 陷阱**: "Sending messages might not actually mean that they're getting more out of Slack"——Activity Metrics vs Outcomes（forward reference，未建 entity） 的具体化
- **AI 生产力表演**: [[AI-Psychosis]] 中的"看起来用 AI 在工作"症候
- **Adoption Barbell**: [[AI-Adoption-Barbell]] 中 5-10% power users vs 70% 几乎不用——Slop Proxy 多发生在中间层（看起来用了 AI 但无实质）

## 关键数据点

- 提出者: Simon Willison（Talking Postgres Ep 42, 28:27 节）
- 原话: "Slop proxies add no value at all."
- 跨域证据: [[Goodharts-Law]]（指标成为目标失效）+ Verifier Mental Model（forward reference，未建 entity）（AI 时代 verifier 稀缺）+ [[AI-Psychosis]]（生产力表演）

## 鉴别 Slop Proxy 的判据

| 判据 | Slop Proxy 信号 |
|------|----------------|
| **可解释性** | [[Explain-Test-Gold-Standard]]——作者能否解释产出 |
| **可验证性** | 产出是否可被独立 verification |
| **影响可追溯** | 产出是否对应明确的问题/需求 |
| **长期价值** | 产出是否减少未来工作量 |
| **作者承诺** | 作者是否愿意为产出"签名" |

## 前提与局限性

- **依赖产物可验证**: 有些场景（实验、research spike）短期难验证，需长周期判断
- **不否定所有 AI 产出**: 经过 [[Rubric-Based-Evaluation]] 等判据的 AI 产出仍是高价值
- **边界**: "Slop" 与 "Useful" 不是二元——存在 spectrum
- **组织责任**: Slop Proxy 多源于组织用错 metrics，而非个人恶意

## 应对策略

1. **指标改革**: 用 outcome 替代 activity（PR 数 → merged-and-shipped 数）
2. **Review 纪律**: TDD for Agents + Code Review 强制 verification
3. **可签名性**: 要求 author 对 AI 产出负责（"我能解释"）
4. **工具层**: [[TDD-for-Agents]] + [[Explain-Test-Gold-Standard]] 嵌入 harness

## 关联概念

- [[Slopocalypse]] — 现象层；Slop Proxy 是其子集
- [[Goodharts-Law]] — 当指标成为目标失效的法则
- [[AI-Adoption-Barbell]] — 中间层是 Slop Proxy 重灾区
- Verifier Mental Model（forward reference，未建 entity） — verifier 视角下 Slop Proxy 的鉴别
- [[Simon-Willison]] — 概念提出者
- [[Explain-Test-Gold-Standard]] — 鉴别 Slop 的工具
- [[TDD-for-Agents]] — 防范 Slop 的工程实践