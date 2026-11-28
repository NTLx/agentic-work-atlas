---
type: entity
title: PA-DR
aliases:
  - PA-DR
  - Privacy-Aware Deep Research
definition: "针对深度研究智能体的隐私保护训练方法，通过结合情境化任务奖励（situational task reward）和学习到的隐私检测奖励（learned privacy reward）进行强化学习，在保持或提升任务成功率的同时，大幅降低对外检索时的隐私泄漏。"
created: 2026-06-19
updated: 2026-11-28
evidence_level: high
claim_type: mixed
tags:
  - concept
  - agent-safety
  - RL
related_entities:
  - "[[MosaicLeaks]]"
  - "[[Mosaic-Effect]]"
source_raw:
  - "[[20260618-mosaicleaks-privacy-agent]]"
---

# PA-DR

## 关键数据点
- **版本更新**：[MosaicLeaks v2](https://arxiv.org/html/2605.30727v2)（2026-11-19）表11：Qwen3-4B Privacy Leakage 34.0%→6.5%（历史博客9.9%），指标按 rollout 的至少一个 full/partial match；严格链成功率48.7%→58.1%（历史58.7%）。同版本 task-only 为59.3%/51.8%。版本变化不等于同模型连续部署改善。
- **跨模型边界**：v2 表13 Gemma 的基线0.7%、task-only 18.8%、PA-DR 3.7%；PA-DR 相对 task-only 降漏，但仍超过自身基线。不能把 Qwen 的 Pareto 改善外推到所有模型。
- **样本效率（历史实验）**：原博客183k vs 963k 比较的是 situational task reward 与 outcome reward 的训练样本数，不是隐私奖励本身的独立效率贡献，也不等于算力、费用或生产样本需求。

## 前提与局限性
- **隐私分类器盲区**: 其防御效果依赖于训练好的“隐私检测分类器”（在研究中为 Qwen3-4B 模型），若分类器存在未知的对抗性漏洞或在特定敏感域中泛化失效，泄露风险仍可能爆发。
- **分层防护**：v2 表16 PA-DR+Seen-Local NER 为57.5%严格链成功/2.0%泄露，All-Entity NER 为52.6%/1.1%；仅为该基准对照，实体过滤不保证保护所有敏感属性。训练不是授权或删除机制，见 [[Agent-Data-Minimization]]。
- **计算开销**: 结合了双重奖励机制，需要在训练或微调阶段生成额外的动作评估样本，具有一定的算力和时间开销。

## 关联概念
- [[MosaicLeaks]]：评测 PA-DR 表现的基准平台。
- [[Mosaic-Effect]]：PA-DR 所致力于削减和防御的核心隐私攻击通路。
