---
type: entity
title: Framing-Right-Layering
aliases:
  - Framing Right Layering
  - 画框权分层定理
  - 画框权分层
definition: "AI 时代的画框权（L1，定战略边界/否决方向/批预算的权力）不是二值的有/无，而是分组织级/部门级/团队级三层。人才迁移常'下沉一层'——保留部门级画框权，丢组织级画框权。CTO→IC 降的是画框权层级，不是职级。"
created: 2026-07-16
updated: 2026-07-16
evidence_level: medium
claim_type: synthesized
tags:
  - organization
  - power
  - management
related_entities:
  - "[[L1L2L3-Power-Decomposition]]"
  - "[[Flattening-as-Governance-Consequence]]"
  - "[[Access-Right-vs-Residual-Control]]"
  - "[[Captain-Mindset]]"
source_raw:
  - "[[20260715-anthropic-talent-strategy-2026]]"
---

# Framing-Right-Layering（画框权分层定理）

> [!definition] 定义
> 画框权（L1）不是二值的有/无，而是分**组织级/部门级/团队级**三层。AI 时代的人才迁移常"下沉一层"——保留部门级画框权，丢组织级画框权。所谓"CTO 降级为 IC"降的不是职级，是画框权的层级。

## 三层画框权

| 层级 | 范围 | 典型决策 | 持有者 |
|------|------|---------|--------|
| 组织级 L1 | 全公司战略 | 定技术范式、否决商业方向、批重大预算 | 创始团队/治理委员会 |
| 部门级 L1 | 单个部门/团队方向 | 定预训练范式、定架构方向、批团队预算 | 部门负责人/资深 IC |
| 团队级 L1 | 单个项目 | 定实现路线、批技术选型 | 项目负责人/资深 IC |
| 无 L1 | — | 只做框内判断（L3） | 纯 IC |

## Karpathy 自我修正案例

Andrej Karpathy 进 Anthropic 负责"预训练团队"。表面看是"保了 L1"（路径乙），但他在 Anthropic 的画框权与 OpenAI 早期不可比：

- **OpenAI 早期**：参与定整个组织的预训练范式 = 组织级 L1。
- **Anthropic**：定"预训练团队内部"技术方向 = 部门级 L1，非组织级 L1（组织级 L1 是 Dario 和治理委员会的）。

准确分类：**路径乙的弱化版**——保了部门级 L1，丢了组织级 L1。这构成 source"降级=放弃权力"叙事的反例（他没有纯丢 L1），但也修正了"换更高杠杆"的乐观（他确实下沉了一层）。

## 为什么分层化重要

分层化粉碎了 source 的二值归因框架。source 把"CTO→IC"当作单一的"放弃权力"事件，但分层后可见：

```
原 CTO: 组织级 L1 + L2 + L3
   ↓ 迁移: 下沉一层
进 Anthropic: 部门级 L1 + 压缩 L2 + 浓缩 L3
   (路径乙弱化版)
```

"降级"降的不是职级，是画框权的层级——从组织级降到部门级。不同 CTO 下沉的层数不同，走的路径不同（甲/乙/乙弱化），不可一概而论。

## 与"管更多 agent"新阶梯的关联

画框权分层化配合 [[L1L2L3-Power-Decomposition]] 的职业阶梯重写：新阶梯不是"管更多人→更高职级"，而是"管更多 agent（L3 浓缩）+ 选择保留哪层 L1"。个体真实定价的是"L1 愿下沉几层 vs L3 要多高浓度"，没有统一的"去科层化胜利"。

## 关键数据点

- Karpathy 案例对照：OpenAI 早期=参与定组织预训练范式（组织级 L1）；Anthropic=定预训练团队内部方向（部门级 L1）——同一下沉一层的实测样本
- Karpathy title "预训练团队负责人"——保部门级 L1 的可观测信号（路径乙弱化版的判据）

## 前提与局限性

- 三层划分是连续谱的离散化，实际边界模糊（如"部门级 vs 组织级"在中小公司重合）。
- 画框权的可观测代理：预算审批阈值、否决权范围、战略会议参与度——但目前无标准化度量。
- 下沉一层不总是被动损失：对某些个体，部门级 L1 + 高浓度 L3 + frontier 接入权的组合，总效用高于原组织级 L1（这正是 B 路径成立的微观基础）。

- 下沉一层不总是被动损失：对某些个体，部门级 L1 + 高浓度 L3 + frontier 接入权的组合，总效用高于原组织级 L1（这正是 B 路径成立的微观基础）。

## 关联概念

- [[L1L2L3-Power-Decomposition]] — 画框权是 L1，本定理细化 L1 的内部结构
- [[Flattening-as-Governance-Consequence]] — 分层化是扁平化的微观个体层映射
- [[Access-Right-vs-Residual-Control]] — 下沉 L1 常伴随换取更高接入权
- [[Captain-Mindset]] — 船长=保部门级 L1 + 浓缩 L3 的实践形态
