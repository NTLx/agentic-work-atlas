---
type: entity
title: Settlement Mechanism
aliases:
  - 结算机制
  - Settlement Seam
definition: "Thousand Token Wood 游戏案例中的 authored settlement seam：交易后由系统规则覆盖参考价格；作为受控状态提交点的设计类比，不等同真实金融结算或普遍正确性机制。"
created: 2026-06-12
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - multi-agent
  - market-design
  - emergence
related_entities:
  - "[[Agent-Heterogeneity]]"
  - "[[Emergence]]"
  - "[[Multi-Agent-System-Pathology]]"
source_raw:
  - "[[20260608-thousand-token-wood-v3]]"
---

> [!definition] 定义
> 本页特指 Thousand Token Wood 游戏中的 post-clearing 价格覆盖，不是支付、交易清算或结算协议的一般定义。可迁移的设计问题是：在哪个受控状态提交点执行不可妥协的规则，哪些上游选择允许开放；规则正确性、覆盖范围与外部效果仍须验证。

## 关键数据点

- 实验: Agent 自由交易 honey → settlement 时强制价格减半 → short 获利 +40
- 对比: 作者三次 live run 未实现目标（-15、-26、-27）；不代表所有输入策略必然失败。
- 设计原则: "Emergence for texture, authored control for moments that must happen"
- 关键区分: Settlement seam 在所有决策下游，agent 的 emergent 行为仍然自由发生在上游

## 前提与局限性

- **游戏化限制**: 该游戏按作者指定规则改价，并非从真实市场结算制度获得的证据；不能把价格覆盖等同真实结算、协议授权或业务结果正确性。
- **时机选择**: 何时触发 settlement 需要精确判断，过早或过晚都可能破坏 emergent 层
- **可扩展性**: 在更大规模的 agent 经济中，settlement seam 的设计可能更复杂
- **信任问题**: 如果 agent 知道结果会被 override，可能改变行为（Lucas critique）

## 关联概念

- [[Agent-Heterogeneity]] — 异质性可能改变上游行为，但不决定结算设计
- [[Emergence]] — Settlement 是 emergent 和 authored control 的分界线
- [[Multi-Agent-System-Pathology]] — 受控提交点可约束部分状态转换，不能自动解决多 Agent 系统病理
