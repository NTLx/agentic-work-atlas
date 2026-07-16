---
type: entity
title: L1L2L3-Power-Decomposition
aliases:
  - L1L2L3 Power Decomposition
  - 权力三层分解
  - L1画框 L2编排 L3判断
definition: "AI 时代组织权力的三层分解模型：L1 画框权（定战略边界/否决方向/批预算，影响做什么）+ L2 编排权（管人/管agent/定流程/分配资源，影响怎么做）+ L3 框内判断权（对具体产出的质量判断，影响做得多好）。AI 时代杠杆翻转的本质是 L2 被压缩、L3 因 agent 不可契约化而浓缩。"
created: 2026-07-16
updated: 2026-07-16
evidence_level: medium
claim_type: synthesized
tags:
  - organization
  - power
  - incomplete-contract
  - management
related_entities:
  - "[[Flattening-as-Governance-Consequence]]"
  - "[[Access-Right-vs-Residual-Control]]"
  - "[[Framing-Right-Layering]]"
  - "[[Captain-Mindset]]"
  - "[[Allocation-Economy]]"
source_raw:
  - "[[20260715-anthropic-talent-strategy-2026]]"
---

# L1L2L3-Power-Decomposition（权力三层分解）

> [!definition] 定义
> 把组织权力拆成三层：**L1 画框权**（定战略边界、否决方向、批预算——影响做什么）、**L2 编排权**（管人/管 agent、定流程、分配资源——影响怎么做）、**L3 框内判断权**（对具体产出的质量判断——影响做得多好）。传统 CTO 三层都有但 L2 占时间最多，L1/L3 被稀释；AI 时代杠杆翻转的本质是 L2 被压缩、L3 浓缩。

## 三层模型

| 层 | 名称 | 职能 | 影响 | AI 时代变化 |
|----|------|------|------|------------|
| L1 | 画框权 | 定战略边界/否决方向/批预算 | 做什么 | 分层化（见 [[Framing-Right-Layering]]），迁移常"下沉一层" |
| L2 | 编排权 | 管人/管agent/定流程/分配资源 | 怎么做 | 被压缩（agent 替代契约化转译） |
| L3 | 框内判断权 | 对具体产出质量判断 | 做得多好 | 浓缩（agent 不可契约化，剩余判断权归操作端） |

## 杠杆翻转的两条迁移路径

AI 压缩 L2 后产生两条迁移路径（判据：是否保留 L1）：

- **路径甲（真放弃权力）**：丢 L1，只保留 L3 做纯 IC。对应"放弃权力"叙事（A）。
- **路径乙（换更高杠杆）**：保 L1，把 L2 压缩到接近零。对应 Founder Mode（B）。
- **路径乙弱化版**：保部门级 L1（非组织级 L1），L2 压缩。Andrej Karpathy 进 Anthropic 负责"预训练团队"即此路径——保了部门级画框权，丢了组织级画框权。

## 为什么 A/B 二分是伪问题

"放弃权力 vs 换杠杆"的二分把连续迁移压成二选一。真实迁移是 L1 下沉一层 + L2 压缩 + L3 浓缩三件事同时发生，A 只见 L1 放弃，B 只见 L3 浓缩，都漏了另两层。

> [!math] 权力迁移公式
> `CTO→IC = L1 下沉一层 + L2 压缩 + L3 浓缩`
> 个体真实定价的不是"放不放弃权力"，而是"L1 愿下沉几层 vs L3 要多高浓度"。

## 职业阶梯重写

传统工程阶梯：IC → 管更多人 → 更高职级。
新工程阶梯：IC → 管更多 agent（L2 压缩但 L3 浓缩）→ 决定保留组织级/部门级/团队级哪层 L1。

晋升不再意味着管更多人，而意味着管更多 agent + 选择保留哪层画框权。这重写了整个工程职业阶梯。

## 证伪信号（成本递增）

1. **公开产出署名**（最便宜）：降级后 6-12 月公开技术产出（论文/模型/系统）署名权性质。集体挂名=路径甲；主导/通讯作者=路径乙。
2. **title 含"团队/负责人"**：含则保了部门级 L1（路径乙弱化版）。
3. **股权条款**（最硬但不公开）：standard grant（按职级定级 RSU）=路径甲；founder-tier/executive-tier 股权包（带战略对赌/否决权）=名义 IC 实际路径乙。

Karpathy 反例：负责"预训练团队"的 title 本身泄露其非纯 IC，是路径乙弱化版——单个反例即可动摇 source"降级=放弃权力"的归因框架。

## 关键数据点

- 传统管理岗 L2 占时间最多，L1/L3 被稀释（Grove《High Output Management》管理杠杆理论）
- Karpathy 进 Anthropic 负责"预训练团队"= 部门级 L1（路径乙弱化版的实测样本）
- Levels.fyi 2025：Staff +7.5% vs Entry +1.6%（5 倍 spread）——L3 浓缩的经济信号（experience return 上升快于 headcount return）
- Unit4 CTO 五职能模型：AI 取代管理者记忆/清障/转译三职能，剩政治合法性/职业命运两职能需人——L2 被压缩的职能级证据

## 前提与局限性

- 三层模型是分析工具，不是组织设计蓝图。实际岗位的 L1/L2/L3 比例连续可变。
- L2 不会归零：跨部门博弈、政治合法性、职业命运等职能 agent 暂时替不了（Unit4 CTO Claus Jepsen 的五职能模型中，剩两项需人）。
- 路径甲乙的真实分布在当前证据下 underdetermined（股权数据不公开），强说多数走甲或乙都是过度归因。

## 关联概念

- [[Flattening-as-Governance-Consequence]] — L2 被压缩的底层经济机制（agent 不可契约化）
- [[Framing-Right-Layering]] — L1 画框权本身的分层化
- [[Access-Right-vs-Residual-Control]] — L3 浓缩的权力本体迁移（剩余控制权→接入权+agent 判断权）
- [[Captain-Mindset]] — L3 浓缩的实践形态（船长=保 L1+L3，压缩 L2）
- [[Allocation-Economy]] — maker 变 manager 即 L2 职能扩散到个体
- [[Founder-Mode]] — 路径乙的极端形态（CEO 保 L1 + 回到 L3）
