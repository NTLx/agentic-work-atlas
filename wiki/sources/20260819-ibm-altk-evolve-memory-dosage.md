---
type: source-summary
title: "How Much Memory Does Your Agent Actually Need?"
source_raw:
  - "[[20260819-ibm-altk-evolve-memory-dosage]]"
created: 2026-08-19
updated: 2026-08-19
tags:
  - source-summary
  - agentic-memory
  - context-engineering
  - ibm-research
  - research-methodology
evidence_level: high
claim_type: extracted
---

# How Much Memory Does Your Agent Actually Need?

## 编译摘要

### 1. 浓缩

- **核心结论1**: Agentic memory 的最优剂量依赖模型能力——把 8 个模型（30B dense 到 frontier proprietary）在 ALTK-Evolve 的两种配置上系统化测试，发现三种 recurring patterns：strong-with-headroom 模型（全 guideline set 注入获益，DeepSeek-V3.2 +9.5pp TGC / +16.1pp SGC）、weak/selective 模型（compact core + per-task retrieval 同时最好且最便宜，gpt-oss-120b +16.1pp TGC at +5% tokens）、saturated 模型（无任何可测增益，GLM-5 0.0/0.0）
  - 关键证据: 8-model sweep on AppWorld（585 tasks）；DeepSeek-V3.2 baseline TGC 79.8→89.3；gpt-oss-120b baseline TGC 39.9→56.0；Opus 4.6 +4.1 TGC/+7.1 SGC；GLM-5 zero gain
- **核心结论2**: 强模型仍能从 guideline set 获益直到接近天花板——Opus 4.6（near ceiling 90.5% TGC）和 GPT-5.5（92.3% TGC）仍得 +7.1pp 和 +7.2pp SGC，说明 memory 的"failure"不是"模型够强就用不上"，而是"guideline 没覆盖剩余失败模式"
  - 关键证据: "Memory keeps paying off as long as a model has a remaining failure mode to target"; SGC metric gains exceed TGC because guidelines help clear all variants of a scenario
- **核心结论3**: Prompt caching 是 production 经济杠杆——DeepSeek 在 full guideline set 下 tokens/task 从 148K 涨到 263K（+78%），但若保持 guideline-set prefix 稳定可被 cache；同时 curated retrieval 在 weak model 上既最准又最便宜（gpt-oss-120b +16.1pp at +5% tokens）
  - 关键证据: tokens/task 表（DeepSeek 148K→263K、gpt-oss-120b 110K→166K full / 110K→116K curated）；ReAct step 数 ≈18-19 与 baseline 持平（不是更长 trajectory）

### 2. 质疑

- **关于 "saturated 模式" 的因果**：作者诚实承认 "the label describes what we observed, not a proven cause"——GLM-5 零增益可能是任务已接近模型天花板、guideline 未覆盖剩余失败、或模型未有效应用 guidance，无法从单次 sweep 区分。本研究未做 controlled ablations 隔离这些因素
- **关于 AppWorld 的代表性**：单一 benchmark（585 tasks, 9 simulated apps）虽是"rigorous multi-step benchmark, but a single one"——calendar/messaging/payments 等结构化任务是否能代表开放域 agent 工作流未验证
- **关于 "context window size is hypothesized but not isolated"**：作者明示这是假设，未做 controlled experiments 隔离 context window 与 raw capability。这让"saturated vs selective"的预测因子清单（headroom / context window / architecture / guideline quality / task distribution）尚处于观察性归纳
- **关于 curated retrieval 的 ranking 质量**：cosine similarity ranking 不完美预测哪些 guideline 帮助给定任务——means selective 配置仍可被更好 selector 改进；这是 "What's next" 的核心 open problem
- **关于 "no human annotation" 的覆盖**：ALTK-Evolve 不需要人类标注，但需要 mining 阶段的 trajectory 足够覆盖失败模式；若 agent 极少失败某类问题，guideline 集中不会包含该类 fix

### 3. 对标与旁逸

- **跨域关联1**: *guideline set mining from past trajectories* 与 Anthropic Claude Tag 的 lessons.md→investigation skill 自蒸馏循环同构——Anthropic 是定性叙述，IBM 是定量 8 模型 sweep。两者合并给出 "agentic memory 不仅是蒸馏，更是剂量调节" 的双向证据
- **跨域关联2**: *三种剂量模式* 与 [[Structured-Agent-Memory]] 的属性匹配范式互补——后者讲记忆怎么组织，前者讲该喂多少。可组合：结构化记忆按 dosage 选择 full set vs retrieval
- **跨域关联3**: *gpt-oss-120b +16.1pp at +5% tokens* 是 [[Context-Engineering]] 的效率标准案例——同时改善 accuracy 和 cost 的策越稀少；提示 retrieval 不是 accuracy 成本 trade-off，而是可以双赢
- **跨域关联4**: *prompt caching + guideline prefix 稳定* 与 Anthropic 的 cache-aware prompt design 同构——把系统层优化引入 context engineering；这与 [[Compaction]] 的 prompt-cache 张力形成对照
- **跨域关联5**: *cosine similarity 不完美预测 guideline 效用* 是 retrieval-as-a-subagent [[Retrieval-as-a-Subagent]] 的潜在应用面——outcome signal 训练的 selector 比 embedding ranking 更能匹配效用

## 关联概念

- [[ALTK-Evolve]]（新建）— IBM Research 的工具/方法
- [[Agentic-Memory-Dosage]]（新建）— 三种模式 + 剂量调节的核心概念
- [[Structured-Agent-Memory]] — 与 ALTK 在记忆结构 vs 剂量的正交维度
- [[Context-Engineering]] — ALTK 是 context engineering 的关键议题
- [[Lessons-MD-Self-Improvement]] — 同构的 agent 自蒸馏循环
- [[Context-Rot]] — 上下文腐烂与饱和现象的关联
- ACE 论文（arxiv:2510.04618）— 与 ALTK 对比的前代框架
- [[Retrieval-as-a-Subagent]] — 替代 cosine ranking 的 outcome-trained selector
- Prompt Caching — production 部署的核心成本杠杆
- [[Compaction]] — context window 管理的另一种技术路径