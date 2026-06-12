---
type: entity
title: Settlement Mechanism
aliases:
  - 结算机制
  - Settlement Seam
definition: "多 agent 经济系统中，在 agent 自由交易之后、结果固化之前的一个确定性覆盖点；在此处 authored override 可以强制设定结果，而 agent 的 emergent 行为仍然自由发生在上游"
created: 2026-06-12
updated: 2026-06-12
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
> Settlement Mechanism 是多 agent 经济系统中的一个设计模式：agent 自由交易（emergent 层），但在结算时由系统强制覆盖结果（authored control 层）。核心洞察：不靠 shock inputs 控制 agent，而是选择精确的 seam 做 deterministic override。

## 关键数据点

- 实验: Agent 自由交易 honey → settlement 时强制价格减半 → short 获利 +40
- 对比: Rumor/windfall 等 shock inputs 全部失败（-15, -26, -27）
- 设计原则: "Emergence for texture, authored control for moments that must happen"
- 关键区分: Settlement seam 在所有决策下游，agent 的 emergent 行为仍然自由发生在上游

## 前提与局限性

- **游戏化限制**: Settlement override 本质上是"作弊"——在真实市场中没有这样的 seam
- **时机选择**: 何时触发 settlement 需要精确判断，过早或过晚都可能破坏 emergent 层
- **可扩展性**: 在更大规模的 agent 经济中，settlement seam 的设计可能更复杂
- **信任问题**: 如果 agent 知道结果会被 override，可能改变行为（Lucas critique）

## 关联概念

- [[Agent-Heterogeneity]] — 异质环境下更需要 settlement mechanism
- [[Emergence]] — Settlement 是 emergent 和 authored control 的分界线
- [[Multi-Agent-System-Pathology]] — 设计 settlement 是解决多 agent 系统不可控性的方案之一
