---
type: entity
title: Agentic Memory Dosage
aliases:
  - Agentic Memory Dosage
  - Memory Calibration Patterns
  - Memory Dose Calibration
  - 三种剂量模式
definition: "针对模型、任务分布与指南质量，在无记忆、全量指南和选择性检索之间评估效果及成本；IBM 的三种模式是特定 AppWorld sweep 的观察分类，不是固定模型分层或通用最优策略。"
created: 2026-08-19
updated: 2026-11-28
tags:
  - agentic-engineering
  - context-engineering
  - memory
  - agentic-memory
evidence_level: medium
claim_type: mixed
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
> **Agentic Memory Dosage** 是 IBM Research 在 8 模型系统化测试后提出的核心洞察：在所报告设置中，不同模型的最佳指南交付配置不同。部分模型全量注入得分较高，gpt-oss-120b 的选择性检索比全量注入得分更高且 token 更少；saturated 标签描述作者在特定设置观察到的无增益，不能外推到所有记忆类型。**Agentic memory is not a feature you switch on. It's a dose you calibrate to the model.**

## 三种模式

| 模式 | 触发条件（综合判断） | 所报候选策略 | 代表模型 |
|------|----------------------|----------|----------|
| **Strong with headroom** | benchmark 仍有提升空间 + 大 context window + 强 instruction following | full guideline set（含 edge-case lessons） | DeepSeek-V3.2 (671B MoE), Claude Opus 4.6, GPT-5.5 |
| **Weak / selective** | 弱 instruction following 或 compact context window | curated retrieval（固定高置信 core + per-task variable） | gpt-oss-120b (117B MoE) |
| **Saturated** | 已接近任务天花板 或 guideline 未覆盖剩余失败模式 | 不注入 memory，节省 quota | GLM-5 (745B MoE) |

> ⚠️ **模式划分不是按参数量一刀切**——headroom、context window、architecture、guideline quality、task distribution 是可能影响观察结果的因素，未隔离其贡献。IBM 明示 isolating context window 与 headroom 是 ongoing work。

## 关键数据（AppWorld test_normal，五个代表模型）

| 模型 | 模式 | baseline TGC | best TGC | Δ TGC |
|------|------|--------------|-----------|-------|
| gpt-oss-120b (117B MoE) | weak/selective | 39.9 | 56.0 (curated) | **+16.1** |
| DeepSeek-V3.2 (671B MoE) | strong/headroom | 79.8 | 89.3 (full) | +9.5 |
| Claude Opus 4.6 | strong/headroom | 90.5 | 94.6 (full) | +4.1 |
| GPT-5.5 | strong/near-ceiling | 92.3 | 95.2 (full) | +2.9 |
| GLM-5 (745B MoE) | saturated | 87.5 | 87.5 (full) | **0.0** |

SGC 按同一场景所有变体均成功计分，不是同一任务重复运行的可靠性；表中若干模型涨幅较大——DeepSeek SGC +16.1pp / TGC +9.5pp；Opus SGC +7.1pp / TGC +4.1pp。

## Curated retrieval 的双重胜利

gpt-oss-120b 的 curated 在所报配置中 TGC 最好、比 full 更省 token，但相对 no-memory 仍多约5% token；token 数不等于货币成本，也未包含挖掘、存储和检索开销。不存在已证明的普遍双赢。

| 模型 | 配置 | tokens/task | overhead |
|------|------|-------------|----------|
| DeepSeek-V3.2 | full guideline set | 263K | +78% |
| gpt-oss-120b | full guideline set | 166K | +51% |
| gpt-oss-120b | curated retrieval | 116K | **+5%** |

## Production 经济杠杆：prompt caching

DeepSeek 全量注入的 token 增幅约78%；保持 guideline-set prefix 稳定可能提高缓存命中，从而降低有效输入成本，实际命中率、计费、TTL、缓存写入和隐私约束需按供应商及工作负载验证。

作者报告 DeepSeek 的 ReAct 步数约18–19不变，额外 token 主要来自输入；该观察不能推广到其他模型，也不表示缓存消除 token 或总成本。

## 核心 takeaway

> **Memory should be calibrated, not merely accumulated.** — IBM Research, 2026-08

- 针对目标任务保留 no-memory 对照；比较 compact core + retrieval 与 full set，而非仅按模型强弱预选。
- 同时测成功率、重复执行一致性、总 token/成本、维护和错误记忆影响；无增益时优先诊断覆盖与应用失败。

## 与 Lessons-MD Self-Improvement 的同构

Anthropic Claude Tag 的 [[Lessons-MD-Self-Improvement]] 是 ALTK 的定性版本：两者都从 trajectory 蒸馏 guideline。但 Anthropic 未做剂量调节——本文暗示其"promote 太多→skill 膨胀→稀释表现"风险对应 saturated 模型零增益现象。这是 CI 域待补的实验验证。

## 关键数据点

- 作者报告八模型 AppWorld sweep；本页代表性数值明确对应168项 test_normal，不是全部585项汇总
- curated retrieval 在 gpt-oss-120b 同时获得 +16.1pp TGC 与 +5% tokens（双赢）
- DeepSeek ReAct step 数不变（≈18-19），作者将额外 token 归因于 input 膨胀
- SGC metric 通常涨幅 > TGC metric（因为 guideline 帮助 clear all variants）
- Opus 4.6 已 near-ceiling（90.5% TGC）仍得 +7.1pp SGC
- GLM-5 在报告设置无可测增益，不证明已达能力天花板
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