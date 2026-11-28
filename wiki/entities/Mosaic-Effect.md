---
type: entity
title: Mosaic Effect
aliases:
  - Mosaic Effect
  - 马赛克效应
definition: "在信息安全与隐私领域，指攻击者通过收集、拼凑多个单独看似无害或局部的公开数据片段（如智能体对外发出的多个检索查询），重构出完整的底层私密信息或推断出整体机密的效应。"
created: 2026-06-19
updated: 2026-11-28
evidence_level: high
claim_type: mixed
tags:
  - concept
  - privacy
related_entities:
  - "[[MosaicLeaks]]"
  - "[[PA-DR]]"
source_raw:
  - "[[20260618-mosaicleaks-privacy-agent]]"
---

# Mosaic Effect（马赛克效应）

## 关键数据点
- **通道威胁**: 即使智能体对外发送的单个网页检索没有泄露完整的敏感信息，攻击者通过拦截和累积分析检索日志，能推断出私密意图、答案，甚至在未读取本地文件时直接拼凑出事实描述。
- **训练相关观察**：[[MosaicLeaks]] 的 Qwen3-4B 实验中，任务训练增加外部查询和可推断信息；v2 基线34.0%→task-only 51.8%，不是所有强化学习的普遍效果。

## 前提与局限性
- **流量可见性假设**：MosaicLeaks 攻击者能读取按时间排列的外部查询文本，例如搜索服务商或具备相应权限的日志层。普通 DNS 观察并不能直接得到 HTTPS 查询内容；部分记录也可能泄露，完整日志不是概念成立的必要条件。
- **信息碎片可重组度**：泄露取决于信息内容、关联、外部辅助知识和观察能力；无证据支持难度随碎片化指数增长，撤回该量化命题。

## 关联概念
- [[MosaicLeaks]]：针对该效应评估深度研究智能体的基准测试。
- [[PA-DR]]：对抗检索马赛克效应的强化学习隐私对齐手段。
