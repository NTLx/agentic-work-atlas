---
type: entity
title: PA-DR
aliases:
  - PA-DR
  - Privacy-Aware Deep Research
definition: "针对深度研究智能体的隐私保护训练方法，通过结合情境化任务奖励（situational task reward）和学习到的隐私检测奖励（learned privacy reward）进行强化学习，在保持或提升任务成功率的同时，大幅降低对外检索时的隐私泄漏。"
created: 2026-06-19
updated: 2026-06-19
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
- **泄露率降幅**: 使用 PA-DR 训练后的 Qwen3-4B，Answer/Full-Information 泄露率从 34.0% 大幅降低至 9.9%。
- **严格链成功率**: 相比于 Base 模型 48.7% 的成功率，PA-DR 成功率不降反升，达到 58.7%（仅做任务训练的模型为 59.3%）。
- **样本生成效率**: PA-DR 情境化奖励机制效率极高，仅用 183k 样本即达到 55% 的成功率，比传统 outcome-reward 训练（需 963k 样本）节省了 5-6 倍生成量。

## 前提与局限性
- **隐私分类器盲区**: 其防御效果依赖于训练好的“隐私检测分类器”（在研究中为 Qwen3-4B 模型），若分类器存在未知的对抗性漏洞或在特定敏感域中泛化失效，泄露风险仍可能爆发。
- **计算开销**: 结合了双重奖励机制，需要在训练或微调阶段生成额外的动作评估样本，具有一定的算力和时间开销。

## 关联概念
- [[MosaicLeaks]]：评测 PA-DR 表现的基准平台。
- [[Mosaic-Effect]]：PA-DR 所致力于削减和防御的核心隐私攻击通路。
