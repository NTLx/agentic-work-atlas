---
type: entity
title: Lessons-MD Self-Improvement
aliases:
  - Lessons.md Self-Improvement
  - Lessons MD
  - Incident Lesson Distillation
  - Incident Lessons Loop
definition: "事故 lessons 自动写入 markdown 文件（lessons.md）→ 新事故开始先读 lessons.md 形成首假设 → 多次出现的模式 promote 到 investigation skill——agent 跨事故自蒸馏经验并沉淀为系统层资产的循环模式"
created: 2026-08-19
updated: 2026-08-26
tags:
  - agentic-engineering
  - self-improvement
  - incident-response
  - memory
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[On-Call-Agent]]"
  - "[[Claude-Tag]]"
  - "[[Structured-Agent-Memory]]"
  - "[[Skills-as-Products]]"
  - "[[ALTK-Evolve]]"
  - "[[Knowledge-Debt]]"
source_raw:
  - "[[20260819-anthropic-claude-tag-oncall]]"
  - "[[20260826-warp-self-improving-agents-on-claude]]"
---

# Lessons-MD Self-Improvement

> [!definition] 定义
> **Lessons-MD Self-Improvement** 是 Anthropic Claude Tag 采用的事故经验自蒸馏循环：每次事故 Claude 自动 append root cause/fix/gotcha 到 lessons.md（markdown 文件）；新事故开始先读 lessons.md 形成首假设；若同一模式多次出现则被 promote 到 investigation skill（长期维护的 markdown skill 文件）。agent 把跨事故的可复用知识沉淀为系统层资产，而非仅依赖模型权重。

## 三段循环

```
事故结束
    ↓ Claude 自动 append
lessons.md（短期记忆）
    ↓ 新事故开始时读
首假设由 lessons.md 形成
    ↓ 模式多次出现
investigation skill（长期资产）
    ↓ 新事故直接读 skill
结构化分诊
```

### 阶段 1: 短期记忆（lessons.md）

- 每次事故 Claude 自动 append：what happened / root cause / fix / gotcha
- 形式自由，自然语言描述
- 累积速度快，可含临时性观察

### 阶段 2: 长期资产（investigation skill）

- 多次出现的模式从 lessons.md promote 到 investigation skill
- 形式严格（如 shadow divergence skill 617 行，编码每一步调查动作）
- 与 skill-as-product 治理同源（[[Skills-as-Products]]）

### 阶段 3: 结构化分诊

- 新事故开始时按 investigation skill 顺序执行
- 不再依赖自由推理，而是按已蒸馏的检查表推进

## 经典条目

文章中最被作者珍视的一条 lesson 由 Claude 写关于工程师本人：

> "query the data first, then theorize. Config tells you what could go wrong; metrics tell you what did."

——这是从一次工程师基于 config 文件做假设、忽略 metrics 的失败事故中蒸馏出来的，沉淀后改变了后续所有调查顺序。

## Warp 变体：双 Skill 主动编辑循环（08-26 补充）

[[20260826-warp-self-improving-agents-on-claude|Warp（2026-08）]]把同一「反馈→文件→改进」机制实现为**双 skill 架构**，与 Claude Tag 的三段循环形成对照：

| 维度 | Lessons-MD（Claude Tag） | Skill-Self-Improvement（Warp） |
|------|--------------------------|-------------------------------|
| 触发 | 事故后自动 append + "promote" 两级蒸馏 | Improver 观察者按 schedule 主动拉反馈 |
| 改进动作 | 模式多次出现才 promote 到长期 skill | Improver 直接编辑 base skill 的最小改动 |
| 产出载体 | lessons.md → investigation skill | base skill（领域） + improver skill（改进） |
| 门禁 | promote 阈值人工判断 | 改动走正常 PR/代码评审流（人类 reviewer gate） |
| 反馈来源 | 事故复盘 | 工作流内 PR/issue 评论直接标注（低摩擦） |

**三个补充洞见**：
- **反馈消失问题**：Warp 明确诊断"反馈到 agent 随会话结束即消失，移除 critical context"——lessons.md 的根本价值是同一问题（把会话外反馈固化到文件）
- **改进载体是 skill 文件而非 harness 代码**：与 [[Meta-Harness-Optimization]]（改 harness，有 J_train∧J_dev 硬 gate）形成对照——Warp 的 gate 是人类 reviewer（软 gate）
- **improver skill 可复用**："improver skill 跨用例差异很小"——把"改进机制"与"领域知识"分离，是 Lessons-MD 未显式讲清的结构

## 与 ALTK-Evolve 的剂量问题

Lessons-md self-improvement 与 IBM Research 的 [[ALTK-Evolve]] 是同构现象——都是"agent 从自己过去的轨迹中蒸馏可复用知识"。ALTK 在 8 模型评测中发现：

- 强模型 + 有 headroom 时全注入表现更好（DeepSeek-V3.2 +9.5pp TGC）
- 弱模型 + selective retrieval 同时最好且最便宜（gpt-oss-120b +16.1pp at +5% tokens）
- 饱和模型零增益（GLM-5）

这意味着 lessons-md / investigation skill 同样存在剂量问题——如果 promote 太频繁、skill 文件膨胀，agent 表现可能饱和甚至倒退。Anthropic 在 CI 域缺少类似系统性测量，是一个待补的研究缺口。

## 关键数据点

- lessons.md = 自动 append，无人工审阅（除非 promote 触发）
- investigation skill 单条 617 行（shadow divergence）
- promote 阈值 = "the same pattern shows up enough times"
- 多事故报告由 ci-weather agent 聚合（新闻室风格）

## 前提与局限性

- **promote 阈值未量化**："enough times"是经验判断；过度 promote 导致 skill 膨胀，过少 promote 失去蒸馏价值
- **饱和风险未测量**：与 ALTK-Evolve 同构——本文未评估 lesson 数量超过临界点后 agent 表现的退化
- **lessons 与 skill 的边界模糊**：哪些 lesson 应停在 lessons.md（短期），哪些应 promote 到 investigation skill（长期），判定标准依赖人工 review
- **跨 agent 迁移性未验证**：每个 Claude Tag 实例积累自己的 lessons.md；团队间如何共享经验是开放问题
- **依赖于稳定的 standing instruction**：Claude 在事故中能否 append lessons.md 取决于 oncall.md 是否明文要求；缺失则循环不闭合

## 与 SHIELD / Knowledge Debt 的边界

[[SHIELD]] 是 Accenture Labs 提出的多 agent 系统，通过 out-of-band 渠道偿还 Knowledge Debt（开发者委托 agent 编码后沉默积累的理解缺口）。Lessons-MD Self-Improvement 是 on-call agent 自身的经验蒸馏循环，不是面向开发者的知识缺口；两者机制相似但目标和作用面不同。

## 关联概念

- [[On-Call-Agent]] — Lessons-MD Self-Improvement 是 on-call agent 的核心机制
- [[Claude-Tag]] — Anthropic 实例的载体
- [[Structured-Agent-Memory]] — Berkeley EPIC 提出的多属性结构化记忆是 lessons-md 的更结构化变体
- [[Skills-as-Products]] — investigation skill 的治理框架
- [[ALTK-Evolve]] — IBM Research 的 agentic memory 剂量研究，与本文同构
- [[Knowledge-Debt]] — Knowledge Debt 是开发者侧的缺口；lessons-md 是 agent 侧的经验