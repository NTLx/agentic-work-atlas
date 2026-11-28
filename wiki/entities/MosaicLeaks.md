---
type: entity
title: MosaicLeaks
aliases:
  - MosaicLeaks
  - MosaicLeaks基准
definition: "ServiceNow 提出的用于评估深度研究智能体（Deep-Research Agent）隐私泄露风险的基准测试，通过模拟包含公共和私有信息的多步研究任务，定量评估智能体在外部检索查询中泄漏本地私密信息的程度。"
created: 2026-06-19
updated: 2026-11-28
evidence_level: high
claim_type: mixed
tags:
  - concept
  - agent-safety
  - privacy
related_entities:
  - "[[PA-DR]]"
  - "[[Mosaic-Effect]]"
  - "[[Agent-Harness]]"
source_raw:
  - "[[20260618-mosaicleaks-privacy-agent]]"
---

# MosaicLeaks

## 关键数据点
- **基准测试规模**: 包含 1,001 个多步研究链，细分为 559 个训练链、98 个验证链和 344 个测试链。
- **版本校准**：34.0% 是 Qwen3-4B-Instruct 的基线，并非多模型统一泄露率。原博客为历史版本；[论文 v2（2026-11-19）](https://arxiv.org/html/2605.30727v2) §3、表11/13：Privacy Leakage 是每条 rollout 中至少一个 answer/claim 被判 full 或 partial match 的比例；严格 Answer Leakage 与 Full-Information Leakage 仅计 full match。Intent Leakage 独立衡量。
- **任务训练的条件性副作用**：v2 表11 Qwen3-4B 的严格链成功率48.7%→59.3%，Privacy Leakage 34.0%→51.8%；PA-DR 为58.1%/6.5%。Gemma、OLMo 在指定实验中也出现 task-only 增漏，但基线差异明显，Gemma PA-DR 仍高于自身基线（3.7% vs 0.7%），不可宣称训练必然提高所有模型的绝对隐私性。

## 前提与局限性
- **合成文档限制**: 基准测试中使用的本地企业文档是合成数据，并且使用的网页语料库也是固定受控的，与真实复杂的异构数据网络环境存在差异。
- **测量局限**：攻击者仅见按时间排序的外部查询文本；Answer Leakage 还给攻击者私有问题（有引导的估计），Full-Information Leakage 不提供该问题。v2 表14 同100链，StepFun 与 Opus 4.7 对 PA-DR 的 Privacy Leakage 判为7.3%/14.3%；趋势一致而绝对量不同，参考 Private QA 仍由 StepFun 生成，不是独立人工真值。未独立复跑；不能推成真实生产泄露概率。
- **对抗性场景覆盖**: 目前主要侧重于常规深度研究流程中的被动泄漏（Outbound Queries），未能涵盖高级对抗性提示注入或主动恶意通信的隐私窃取情况。

## 关联概念
- [[PA-DR]]：针对该泄露风险提出的强化学习训练方法。
- [[Mosaic-Effect]]：描述泄露背后的拼凑累积效应。
- [[Agent-Harness]]：用于运行和测试该基准的底层智能体评测框架。
