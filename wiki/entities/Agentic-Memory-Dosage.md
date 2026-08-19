---
type: entity
title: Agentic Memory Dosage
aliases:
  - Agentic Memory Dosage
  - Memory Calibration Patterns
  - Memory Dose Calibration
  - 三种剂量模式
definition: "Agentic memory（self-distilled guideline set）的最优剂量依赖模型能力——按 (headroom + context window + architecture + guideline quality + task distribution) 多因子，将模型划分为 strong-with-headroom / weak-selective / saturated 三种模式，分别对应 full set / curated retrieval / no-memory 的最优策略"
created: 2026-08-19
updated: 2026-08-19
tags:
  - agentic-engineering
  - context-engineering
  - memory
  - agentic-memory
evidence_level: high
claim_type: extracted
related_entities:
  - "[[ALTK-Evolve]]"
  - "[[Structured-Agent-Memory]]"
  - "[[Context-Engineering]]"
  - "[[Lessons-MD-Self-Improvement]]"
  - "[[Context-Rot]]"
source_raw:
  - "[[20260819-ibm-altk-evolve-memory-dosage]]"
---

# Agentic Memory Dosage（Agentic 记忆剂量调节）

> [!definition] 定义
> **Agentic Memory Dosage** 是 IBM Research 在 8 模型系统化测试后提出的核心洞察：Agentic memory 的最优剂量不是"越多越好"，而是按模型能力分层调节。Strong-with-headroom 模型用 full guideline set 获益最大；weak/selective 模型用 compact core + per-task retrieval 同时最准且最便宜；saturated 模型注入任何 memory 都不产生 improvement。**Agentic memory is not a feature you switch on. It's a dose you calibrate to the model.**

## 三种模式

| 模式 | 触发条件（综合判断） | 最优策略 | 代表模型 |
|------|----------------------|----------|----------|
| **Strong with headroom** | benchmark 仍有提升空间 + 大 context window + 强 instruction following | full guideline set（含 edge-case lessons） | DeepSeek-V3.2 (671B MoE), Claude Opus 4.6, GPT-5.5 |
| **Weak / selective** | 弱 instruction following 或 compact context window | curated retrieval（固定高置信 core + per-task variable） | gpt-oss-120b (117B MoE) |
| **Saturated** | 已接近任务天花板 或 guideline 未覆盖剩余失败模式 | 不注入 memory，节省 quota | GLM-5 (745B MoE) |

> ⚠️ **模式划分不是按参数量一刀切**——headroom、context window、architecture、guideline quality、task distribution 多因子共同决定模式归属。IBM 明示 isolating context window 与 headroom 是 ongoing work。

## 关键数据（AppWorld TGC）

| 模型 | 模式 | baseline TGC | best TGC | Δ TGC |
|------|------|--------------|-----------|-------|
| gpt-oss-120b (117B MoE) | weak/selective | 39.9 | 56.0 (curated) | **+16.1** |
| DeepSeek-V3.2 (671B MoE) | strong/headroom | 79.8 | 89.3 (full) | +9.5 |
| Claude Opus 4.6 | strong/headroom | 90.5 | 94.6 (full) | +4.1 |
| GPT-5.5 | strong/near-ceiling | 92.3 | 95.2 (full) | +2.9 |
| GLM-5 (745B MoE) | saturated | 87.5 | 87.5 (full) | **0.0** |

SGC（更严格 all-or-nothing）通常涨幅更大——DeepSeek SGC +16.1pp / TGC +9.5pp；Opus SGC +7.1pp / TGC +4.1pp。

## Curated retrieval 的双重胜利

弱模型在 curated retrieval 上同时最准且最便宜——gpt-oss-120b +16.1pp TGC at +5% tokens。**Better performance here does not require more inference cost**——accuracy 与 cost 的双赢消除了常见 trade-off 假设。

| 模型 | 配置 | tokens/task | overhead |
|------|------|-------------|----------|
| DeepSeek-V3.2 | full guideline set | 263K | +78% |
| gpt-oss-120b | full guideline set | 166K | +51% |
| gpt-oss-120b | curated retrieval | 116K | **+5%** |

## Production 经济杠杆：prompt caching

即使全注入策略成本高（DeepSeek +78%），保持 guideline-set prefix 稳定可被 prompt cache 大幅降低——cache-aware prompt design 是 production 必备工程。

memory 不会让 reasoning loop 更长（DeepSeek ReAct step 数 ≈18-19 与 baseline 持平），成本全来自 input 膨胀；cache 化是消除该膨胀的主要手段。

## 核心 takeaway

> **Memory should be calibrated, not merely accumulated.** — IBM Research, 2026-08

- 弱模型：compact core + per-task retrieval（同时最好最便宜）
- 强模型 with headroom：full set + prompt caching
- 饱和模型：节省 quota，待 failure mode 理解后再说

## 与 Lessons-MD Self-Improvement 的同构

Anthropic Claude Tag 的 [[Lessons-MD-Self-Improvement]] 是 ALTK 的定性版本：两者都从 trajectory 蒸馏 guideline。但 Anthropic 未做剂量调节——本文暗示其"promote 太多→skill 膨胀→稀释表现"风险对应 saturated 模型零增益现象。这是 CI 域待补的实验验证。

## 关键数据点

- 8 模型 + 1 benchmark（AppWorld 585 tasks）的 sweep 结果
- curated retrieval 在 gpt-oss-120b 同时获得 +16.1pp TGC 与 +5% tokens（双赢）
- DeepSeek ReAct step 数不变（≈18-19），cost 增量全在 input 膨胀
- SGC metric 通常涨幅 > TGC metric（因为 guideline 帮助 clear all variants）
- Opus 4.6 已 near-ceiling（90.5% TGC）仍得 +7.1pp SGC
- GLM-5（745B MoE）饱和零增益
- "the right dose of memory depends on the model, and we can calibrate it"

## 前提与局限性

- **saturated 模式未消融**：GLM-5 零增益是观察性归纳，因果未隔离（headroom / context window / guideline coverage / application failure）
- **AppWorld 单一 benchmark**：calendar/messaging/payments 等结构化任务是否能代表开放域 agent 工作流未验证
- **context window 未隔离**：作者承认是 hypothesis，未 controlled experiments
- **cosine similarity ranking 不完美**：outcome signal 训练的 selector 是 open problem
- **weak 模型 self-distillation 无信号**：teacher-distilled memory 是 separate problem

## 关联概念

- [[ALTK-Evolve]] — IBM Research 的方法/工具
- [[Structured-Agent-Memory]] — Berkeley EPIC 多属性记忆，与 dosage 正交
- [[Context-Engineering]] — dosage 是 context engineering 的核心议题
- [[Lessons-MD-Self-Improvement]] — 同构现象的定性版本（CI 域）
- [[Context-Rot]] — 上下文腐烂的近端问题
- Prompt Caching — production 经济杠杆
- ACE 论文（arxiv:2510.04618）— 与 ALTK 对比的前代框架（delivery 方式差异）
- [[Retrieval-as-a-Subagent]] — outcome signal 替代 cosine ranking
- [[Compaction]] — context window 管理的替代技术路径