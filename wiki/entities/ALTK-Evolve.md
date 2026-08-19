---
type: entity
title: ALTK-Evolve
aliases:
  - ALTK-Evolve
  - ALTK Evolve
  - Agent Toolkit Evolve
definition: "IBM Research 发布的 agent learning library——通过 extraction、consolidation、retrieval 三阶段让 agent 从自身过去的 trajectory 中蒸馏 reusable guideline set，在推理时注入以提升表现；不更新模型权重，不需要人类标注，可移植到任意模型"
created: 2026-08-19
updated: 2026-08-19
tags:
  - agentic-engineering
  - agentic-memory
  - ibm-research
  - tool
  - context-engineering
evidence_level: high
claim_type: extracted
related_entities:
  - "[[Agentic-Memory-Dosage]]"
  - "[[Structured-Agent-Memory]]"
  - "[[ACE]]"
  - "[[Context-Engineering]]"
  - "[[Lessons-MD-Self-Improvement]]"
  - "[[Retrieval-as-a-Subagent]]"
source_raw:
  - "[[20260819-ibm-altk-evolve-memory-dosage]]"
---

# ALTK-Evolve

> [!definition] 定义
> **ALTK-Evolve** 是 IBM Research 2026-08 发布的 agent learning library（[github.com/AgentToolkit/altk-evolve](https://github.com/AgentToolkit/altk-evolve)），通过 extraction → consolidation → retrieval 三阶段流水线让 agent 从自身过去的 trajectory 中蒸馏 reusable guideline set，在推理时注入到 ReAct 每步以提升表现。整个循环不改模型权重、不需要人类标注，可在任意模型上便携运行。

## 三阶段流水线

| 阶段 | 输入 | 输出 |
|------|------|------|
| **Extraction** | agent 的成功 + 不成功 trajectory | 行为 guideline（策略、避坑、边界 case） |
| **Consolidation** | 多个 trajectory 提取的 guideline | consolidated reusable guideline set |
| **Retrieval** | 当前任务描述 + guideline set | 当前步注入的 guideline 子集（或 full set） |

**Learning happens around the model, not inside it**——核心设计决策：不更新权重，只改 guidance。这让 adoption 便宜且 portable。

## 与 ACE 的关键差异

IBM Research 之前在姊妹文章中将 ALTK 与 ACE（[arxiv:2510.04618](https://arxiv.org/abs/2510.04618)）对比：差异在**deliver 方式**而非（"少量检索" vs "全量注入"）——前者驱动 accuracy 与 cost 的取舍；ACE 全量注入对照下 ALTK 选择性 retrieval 表现接近但成本更低。

## 在 8 模型上的评测

| 模型 | 类别 | 最佳配置 | Δ TGC | Δ SGC |
|------|------|---------|-------|-------|
| gpt-oss-120b (117B MoE) | weak/selective | curated retrieval | +16.1 | +16.1 |
| DeepSeek-V3.2 (671B MoE) | strong w/ headroom | full guideline set | +9.5 | +16.1 |
| Claude Opus 4.6 | strong w/ headroom | full guideline set | +4.1 | +7.1 |
| GPT-5.5 | strong (near-ceiling) | full guideline set | +2.9 | +7.2 |
| GLM-5 (745B MoE) | saturated | full guideline set | 0.0 | 0.0 |

评测基准：AppWorld（585 multi-step tasks = 168 test_normal + 417 test_challenge, 9 simulated apps）。度量：TGC（Task Goal Completion）+ SGC（Scenario Goal Completion，更严格的 all-or-nothing）。

## 三种剂量模式

参见 [[Agentic-Memory-Dosage]] 详述。三种模式不是简单按参数量划分，而是按 (headroom + context window + architecture + guideline quality + task distribution) 多因子决定。

## 关键数据点

- 训练数据：AppWorld training split only；测试 split 永不入 guideline 挖掘（防泄漏）
- baseline 配置：no memory，agent as shipped
- full set：每 ReAct step 注入所有 guideline
- curated retrieval：固定高置信 core + per-task variable portion
- DeepSeek-V3.2 tokens/task：148K baseline → 263K full（+78%）；ReAct step 数 ≈18-19 不变
- gpt-oss-120b tokens/task：110K baseline → 166K full（+51%）→ 116K curated（+5%）

## 关键设计决策

- **no weight updates**：所有学习发生在 guidance 层而非模型层；adoption 成本低、可移植
- **mining 阶段用 training split only**：避免 test split 泄漏污染 guideline
- **prompt caching 友好**：保持 guideline-set prefix 稳定即可 cache
- **三种配置策略可比**：报告按 strategy（full vs curated）而非 raw guideline count，因各模型挖掘能力差异使 raw 数不可比

## 前提与局限性

- **saturated 模式未消融**：GLM-5 零增益是观察性归纳，因果未隔离（headroom / context window / guideline coverage / application 失败）
- **AppWorld 是单一 benchmark**：calendar/messaging/payments 等结构化任务是否能泛化到开放域 agent 工作流未验证
- **cosine similarity ranking 不完美**：当前 retrieval 按 embedding 相似度，但相似度不预测效用；outcome-trained selector 是 open problem
- **weak 模型无信号**：低于最低能力阈值时 self-distillation 缺信号；teacher-distilled memory 是 separate problem
- **context window 未隔离**：作者承认这是 hypothesis，未做 controlled ablations

## What's Next（IBM 明示的下一步）

1. **learned selector**——用 outcome signal 替代 embedding ranking
2. **memory for very weak models**——teacher-distilled memory
3. **beyond AppWorld**——更广 agent benchmark 与真实部署验证
4. **isolating context window**——controlled experiments 隔离 context window size 与 raw capability

## 关联概念

- [[Agentic-Memory-Dosage]] — 三种模式 + 剂量调节的核心概念
- [[Structured-Agent-Memory]] — Berkeley EPIC 的多属性结构化记忆，与 ALTK 在记忆结构维度互补
- ACE 论文（arxiv:2510.04618）— 与 ALTK 对比的前代框架
- [[Context-Engineering]] — ALTK 是 context engineering 的关键议题
- [[Lessons-MD-Self-Improvement]] — Anthropic Claude Tag 的定性自蒸馏循环，与 ALTK 定量 sweep 互补
- [[Retrieval-as-a-Subagent]] — outcome signal 训练的 selector 替代 cosine ranking
- Prompt Caching — production 部署的核心成本杠杆
- [[Compaction]] — context window 管理的另一种技术路径
- IBM Agent Logic — IBM 整体 agent 战略下的 learning 层组件