---
type: entity
title: Operational-Responsibility
aliases:
  - Operational Responsibility
  - OR
  - 运营责任制
definition: "写代码的团队拥有其生产行为的组织机制：最先被 paging 的人就是最适合修复的人，以 deployment agreements 和 paging hygiene 保证告警直达责任人"
created: 2026-07-30
updated: 2026-07-30
tags:
  - software-engineering
  - sre
  - organization
  - ai-ready-organization
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[AI-Native-Engineering-Org]]"
  - "[[Organization-as-Agent-Harness]]"
  - "[[Deployment-Product-Flywheel]]"
  - "[[Secure-Paved-Path]]"
source_raw:
  - "[[20260730-palantir-operational-responsibility]]"
---

# Operational-Responsibility（运营责任制）

> [!definition] 定义
> **Operational Responsibility（OR）** 是 Palantir 的生产所有权机制：每个部署的软件片段归属一个团队，该团队被认定为代码的 expert 并首先响应告警。核心原则一句话——"always page the person best equipped to fix the problem first"。自我定位为反中心规划、反去中介化、反官僚主义，是 DevOps "you build it, you run it" 的联邦制版本。

## 三大支柱

| 支柱 | 机制 | 目的 |
|------|------|------|
| 持续部署基础设施 | Apollo 把年度高风险人工升级转为每日数千次无感升级 | 频繁升级降低遗留代码风险，调试时开发者更熟悉代码 |
| Production Ownership | 团队签 deployment agreements（承诺不看前端/不直读数据）换取直接告警访问权 | 让写代码的人直接获得生产行为反馈 |
| Paging Hygiene | first person paged 不是最佳修复者 = anti-pattern；误报 = bug | 提高 firefighting 的信噪比，而非追求稳定性本身 |

## 关键机制

- **Put the Pebble in the Right Shoe**：同一问题反复 page 同一开发者，使其成为问题的"最后一站"，获得根除问题的强动机。开发者开始"为自己的调试而写代码"，形成高效反馈环。
- **三条操作纪律**：(1) Assume alerts are actionable——不可操作的告警视为 bug（air-gapped 网络中进一次设施的成本极高，误报代价放大）；(2) 每次重大事故都是改进机会——分析根因与漏过的低优先级告警；(3) 告警量大时引入 secondary rotation，防止 firefighting follow-up 被丢弃。
- **Rotation 规模约束**：单 rotation 至少 3 名有访问权的人，4-5 人舒适，超过 6 人因 on-call 频率太低而失去熟练度；引入 secondary rotation 时人数翻倍。达不到规模不如暂缓，避免 burnout。
- **Air-gapped NOC 模式**：为 classified 网络设 24/7 Network Operations Center 做远程调试、磁盘扫描新软件包、一线终端支持；on-call 人员夜间可回家信任 NOC 兜底。
- **文化中心职责 = editing, not authoring**：持续最小化中心协调的必要性，因为中心化 prioritization 天然是瓶颈。

## 前提与局限性

- **成立条件**：每个部署片段能归属一个足够小、边界清晰的团队。平台型组织（一个底层服务被数百团队依赖）中 ownership 会被稀释为 on-call 轮役。
- **隐性前提**：持续部署依赖强测试覆盖与回滚能力；原文只谈组织意愿，未谈工程基础。
- **文化转型成本**：让高使命感工程师"unlearn heroics"（不再盯着升级看、不babysit服务）比制度设计更难，多数组织 도입 OR 失败于此。
- **排他性主张过强**："OR 是唯一道路"不成立——Google 专职 SRE 模式在超大规模下同样有效；OR 与 SRE 是同一问题的两种分工解。

## Agent 时代的延伸

当 agent 成为生产环境的行动者，"first person paged = 最佳修复者"必须重新映射：agent 出错时 page 谁？OR 的 paging hygiene 原则预言了 agent 治理的责任路由问题——tool 调用的 runtime validation 与显式 authorization grants（见 [[Decision-Centric-Architecture]]）可视为机器侧的 paging hygiene：每次越界调用都被精确路由到能修复它的人或策略。

## 关联概念

- [[AI-Native-Engineering-Org]] — OR 是 AI 原生工程组织的运维文化原型
- [[Organization-as-Agent-Harness]] — OR 的人力责任路由是 agent 责任治理的参照系
- [[Secure-Paved-Path]] — 安全侧的共享所有权与 OR 同构
- [[Deployment-Product-Flywheel]] — OR 保证现场反馈真正回流给写代码的人
