---
type: entity
title: MosaicLeaks
aliases:
  - MosaicLeaks
  - MosaicLeaks基准
definition: "ServiceNow 提出的用于评估深度研究智能体（Deep-Research Agent）隐私泄露风险的基准测试，通过模拟包含公共和私有信息的多步研究任务，定量评估智能体在外部检索查询中泄漏本地私密信息的程度。"
created: 2026-06-19
updated: 2026-06-19
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
- **基本泄露率**: 在测试的多款大语言模型中，在未加防护的情境下，深度研究智能体存在 34.0% 的 Answer/Full-Information 泄露率。
- **任务强化负作用**: 仅针对任务成功率进行强化的智能体，虽然成功率提升，但泄露率显著攀升至 51.7%。

## 前提与局限性
- **合成文档限制**: 基准测试中使用的本地企业文档是合成数据，并且使用的网页语料库也是固定受控的，与真实复杂的异构数据网络环境存在差异。
- **对抗性场景覆盖**: 目前主要侧重于常规深度研究流程中的被动泄漏（Outbound Queries），未能涵盖高级对抗性提示注入或主动恶意通信的隐私窃取情况。

## 关联概念
- [[PA-DR]]：针对该泄露风险提出的强化学习训练方法。
- [[Mosaic-Effect]]：描述泄露背后的拼凑累积效应。
- [[Agent-Harness]]：用于运行和测试该基准的底层智能体评测框架。
