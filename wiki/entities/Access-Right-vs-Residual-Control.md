---
type: entity
title: Access-Right-vs-Residual-Control
aliases:
  - Access Right vs Residual Control
  - 权力本体迁移定理
  - 接入权与剩余控制权
definition: "AI 时代权力本体在迁移：从'剩余控制权'（对未约定资产的处置/否决）迁向'接入权'（调 frontier 算力/模型/数据）+ 新生的'对 agent 的剩余判断权'（因 agent 不可契约化而派生）。CTO→IC 在剩余控制权维度放弃了权力，在接入权维度换到了更高——A/B 描述的是权力本体迁移的两个维度，不是同一现象两面。"
created: 2026-07-16
updated: 2026-07-16
evidence_level: medium
claim_type: synthesized
tags:
  - organization
  - power
  - incomplete-contract
  - AI-Agent
related_entities:
  - "[[Flattening-as-Governance-Consequence]]"
  - "[[L1L2L3-Power-Decomposition]]"
  - "[[Recursive-Self-Improvement]]"
  - "[[Captain-Mindset]]"
source_raw:
  - "[[20260715-anthropic-talent-strategy-2026]]"
---

# Access-Right-vs-Residual-Control（权力本体迁移定理）

> [!definition] 定义
> AI 时代权力本体在迁移：从 **剩余控制权**（Hart：合同写不完所有 contingencies，谁拥有对未约定资产的处置/否决权谁掌权）迁向 **接入权**（调 frontier 算力/模型/数据的权限）+ 新生的 **对 agent 的剩余判断权**（因 agent 不可契约化而派生）。CTO→IC 在剩余控制权维度确实放弃了权力，在接入权维度换到了更高——A/B 描述的是迁移的两个维度，不是同一现象两面。

## 三种权力形态

| 权力形态 | 定义 | AI 时代变化 |
|---------|------|------------|
| 剩余控制权（旧） | 对未约定技术资产的处置/否决最终权力 | CTO→IC 时交还原组织，确实放弃 |
| 接入权（新） | 调 frontier 算力/模型/数据的权限 | CTO→IC 时换到更高，正替代剩余控制权成新权力源 |
| 对 agent 的剩余判断权（新派生） | 批不批 agent 的 PR、信不信它说"我测过了" | 因 agent 不可契约化而派生，浓缩在操作者手里，原 CTO 没有 |

## 契约理论框架

Oliver Hart 的剩余控制权理论：任何执行单元的不可契约化程度越高，围绕它的剩余控制权就越值钱。

- **人类员工**相对可契约化（合同+KPI+HR 流程兜底）→ 传统管理岗的剩余控制权被稀释。
- **agent** 不可契约化 → 围绕 agent 的剩余控制权高度浓缩在直接操作者手里。

这解释了为什么是"降级为 IC"——AI 时代权力浓度最高的位置，恰恰是最贴近不可契约化执行单元（agent）的那个位置。CTO→IC 不是放弃权力，是**权力浓度梯度的迁移**——从稀释端（管可契约化的人）迁向浓缩端（管不可契约化的 agent）。

## CTO→IC 的双维度

```
剩余控制权维度：Workday CTO 对 Workday 技术栈有剩余控制权
                → 去 Anthropic 做 IC 这部分交还 (↓ 放弃, A 在此维度成立)

接入权维度：    原 CTO 调 Workday 内部资源
                → IC 调 frontier 算力/模型/数据 (↑ 换到更高, B 在此维度成立)

agent 判断权：  原 CTO 管 100 个可契约化的人
                → IC 管 N 个不可契约化的 agent (↑ 新权力源, 支持 B)
```

A 和 B 都对，但描述的是权力的两个不同维度——A 描述剩余控制权维度，B 描述接入权维度。它们不是同一现象的两面，是**权力本体在迁移**：从剩余控制权迁向接入权+agent 判断权。

## Karpathy 的一线表述

"我的杠杆从来不是管多少人，是我能调动多少算力、能写多少进生产环境的代码。2026 年算力就是杠杆，代码就是权力。"

这把抽象的"接入权"落到可操作物：算力配额 + 生产环境写入权。CTO 放下的是"为算力和代码做政治背书的冗余中间层"，这个岗位在算力可以直接买到、agent 可以直接调动的时代是冗余的。

## 关键数据点

- Karpathy 自述："算力就是杠杆，代码就是权力"（[[Recursive-Self-Improvement]] RSI 一手数据）
- Anthropic RSI：工程师人均合并量 8x、团队规模不变——接入权（算力+代码写入权）放大 IC 产出的直接证据
- Pentagon 红线事件：Anthropic 拒取消致命武器限制→被列供应链风险→采用率反升 6.3%——剩余控制权维度"付代价=可置信承诺"的实例

## 前提与局限性

- 接入权能否长期替代剩余控制权成稳定权力源，取决于 frontier 算力/模型是否持续稀缺。若算力彻底商品化、模型开源普及，接入权贬值，剩余控制权重回主导——**此迁移可逆**。
- "对 agent 的剩余判断权"被 [[L1L2L3-Power-Decomposition]] 的 Graham 反驳修正：它是 L3 框内判断权，被 L1 画框权压一头（IC 在别人画的算力配额框内判断）。接入权高不等于画框权高。
- 接入权的实际边界由配额审批者（Dario 层）决定，IC 的接入权仍在组织级 L1 画框之内。

- 接入权的实际边界由配额审批者（Dario 层）决定，IC 的接入权仍在组织级 L1 画框之内。

## 关联概念

- [[Flattening-as-Governance-Consequence]] — 接入权迁移的底层是 agent 不可契约化
- [[L1L2L3-Power-Decomposition]] — agent 判断权归 L3，被 L1 画框权约束
- [[Framing-Right-Layering]] — 接入权高低不等于画框权层级
- [[Recursive-Self-Improvement]] — "算力即杠杆、代码即权力"的 RSI 一手数据基础
- [[Captain-Mindset]] — 船长=高接入权+高 agent 判断权+部门级画框权的组合
