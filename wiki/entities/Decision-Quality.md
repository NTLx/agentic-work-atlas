---
type: entity
title: Decision Quality
aliases:
  - Decision Quality
definition: "在任务目标、验证成本、失败代价和组织约束之间做出高质量取舍，并决定何时让 AI 执行、何时由人承担的能力"
created: 2026-04-09
updated: 2026-06-07
tags:
  - AI-Agent
  - Decision-Making
  - organization
  - delegation
related_entities:
  - '[[Judgment]]'
  - '[[Taste]]'
  - '[[Ownership]]'
  - '[[AI-First]]'
  - '[[Allocation-Economy]]'
source_raw:
  - '[[Management as AI superpower]]'
  - '[[20260413-why-ai-first-strategy-wrong]]'
  - '[[Knowledge Work Is Dying—Here’s What Comes Next]]'
---

# Decision Quality

> [!definition] 定义
> Decision Quality 是 AI 时代的人类核心能力之一：在不确定条件下，为人类或 AI 选择更优执行路径，明确边界、设置验收标准，并承担后果。

## 为什么重要

- AI 让执行成本下降，组织的稀缺点从“谁能做”转向“什么值得做、谁来做、做到什么算完成”。
- 同一个任务里，AI 过程时间、人类检查时间、失败代价和成功概率经常彼此冲突，不能靠默认设置解决。
- 当 Agent 产出看起来都“差不多能用”时，真正有价值的是识别隐藏风险、方向错误和验收假象。

## 核心结构

| 维度 | 低决策质量 | 高决策质量 |
|-----|-----------|-----------|
| 任务分配 | 看到 AI 能做就直接委托 | 先比较 AI 时间、检查成本、失败代价 |
| 验收方式 | 只看表面是否“像样” | 提前定义验证标准和回滚条件 |
| 风险判断 | 把责任隐含地推给模型 | 明确谁承担后果、何时必须转人工 |
| 组织作用 | 加快错误扩散 | 把速度转化为有效学习 |

### 1. 任务判断
- 这个任务是否适合委托给 AI
- 成功是否可验证
- 失败是否可逆

### 2. 边界设计
- 给 Agent 什么上下文、权限和工具
- 哪些步骤必须设置检查点
- 什么结果必须升级给人

### 3. 验收与追责
- 结果是否真正解决了问题，而不只是生成了产物
- 谁有权否决“看起来能跑”的错误方案
- 是否能从失败中沉淀为下次更好的判断

## 关键数据点

- [[Management as AI superpower]] 把决策问题具体化为委托公式：人类基准时间、AI 过程时间、检查时间和成功概率共同决定是否值得委托。
- [[20260413-why-ai-first-strategy-wrong]] 指出 AI-assisted 常只有 10% 到 20% 效率提升，而 AI-first 的价值来自重写流程后的人类判断层，而不是单纯增加生成速度。
- [[Knowledge Work Is Dying—Here’s What Comes Next]] 把公司的两块基石压缩为 decisions 和 relationships，说明知识商品化后，判断本身变成更稳定的人类价值。

## 操作化问题

在 AI 工作流里，Decision Quality 可以落成一组反复追问：

1. 这个任务应不应该交给 AI，而不是“能不能”交给 AI？
2. 如果交给 AI，最便宜的可靠验证是什么？
3. 如果验证成本过高，是否其实不该委托？
4. 这次错误若发生，谁承担损失？
5. 今天做出的判断，能否沉淀为下一次更好的 SOP、评测或审查标准？

## 前提与局限性

- **前提**：组织至少具备基本验证能力，否则“判断”只能退化为主观拍板。
- **前提**：人类仍掌握任务上下文、风险边界和真实后果，不能把这些外包给模型。
- **局限**：当任务极其标准化、失败成本极低时，Decision Quality 的边际价值会下降，执行速度更重要。
- **局限**：它不能脱离领域知识独立存在；没有专业背景的人很难判断 AI 输出的隐藏问题。

## 关联概念

- [[Judgment]] - Decision Quality 是 Judgment 在组织与任务分配层面的落地形式
- [[Taste]] - Taste 负责识别“哪里不对”，Decision Quality 负责决定“下一步怎么做”
- [[Ownership]] - 没有承担后果的权力与责任，决策质量无法稳定提升
- [[AI-First]] - AI-first 组织把人的价值从代码产出迁移到决策质量
- [[Allocation-Economy]] - 分配经济要求人类持续决定任务该交给谁或什么模型

## 来源

- [[Management as AI superpower]]
- [[20260413-why-ai-first-strategy-wrong]]
- [[Knowledge Work Is Dying—Here’s What Comes Next]]
