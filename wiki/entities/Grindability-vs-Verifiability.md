---
type: entity
title: Grindability vs Verifiability
aliases:
  - 可磨性与可验证性
  - 可磨性vs可验证性
definition: "AI成功的关键因素区分：可磨性（问题可容器化、并行化、自动化）比可验证性（问题有明确正确答案）更重要"
created: 2026-07-01
updated: 2026-07-01
evidence_level: medium
claim_type: mixed
tags:
  - AI-capabilities
  - mathematics
  - software-engineering
related_entities:
  - '[[AI-in-Mathematics]]'
  - '[[Coding-Agents]]'
  - '[[Sample-Efficiency]]'
source_raw:
  - '[[20260701-grant-sanderson-ai-math-future]]'
---

# Grindability vs Verifiability

> [!definition] 定义
> **Grindability vs Verifiability** 是指AI成功的关键因素区分：**可磨性**（问题可容器化、并行化、自动化）比**可验证性**（问题有明确正确答案）更重要。

## 核心要点

### 可磨性（Grindability）

**可磨性**是指问题可以容器化、并行化、自动化的程度。

**关键特征**：
- 可以在容器中运行
- 可以并行执行多个实例
- 结果是确定性的
- 可以自动验证正确性

**例子**：
- 代码测试：可以容器化运行，自动验证结果
- 数学证明：可以形式化验证
- IMO几何问题：可以暴力求解

### 可验证性（Verifiability）

**可验证性**是指问题有明确正确答案的程度。

**关键特征**：
- 有明确的正确答案
- 可以验证结果是否正确
- 不一定可以并行化

**例子**：
- 证明定理：可以验证证明是否正确
- 网购包裹：可以验证是否送达
- 会议预订：可以验证是否成功

### 为什么可磨性更重要

Grant Sanderson指出，AI在数学中的成功依赖于**可磨性**，而非**可验证性**：

> "AI在数学中的成功不仅仅是可验证性；它必须是可磨的。"

**原因**：
1. 网站有机器人检测，难以并行化
2. 现实世界的任务难以容器化
3. 代码和数学可以容器化并行运行

### 可磨性的限制

**例子**：
- **网站交互**：有机器人检测，难以并行化
- **商业决策**：每天都在变化，难以容器化
- **市场交易**：需要与真实世界交互，难以并行化

## 关键数据点

- AlphaGeometry在19秒内解决IMO几何问题（可磨）
- 网站有机器人检测，难以并行化（不可磨）
- 代码可以容器化并行运行（可磨）
- 现实世界的任务难以容器化（不可磨）

## 前提与局限性

- **前提**：可磨性是AI成功的关键因素
- **前提**：可验证性重要，但不是充分条件
- **局限**：并非所有问题都具有可磨性
- **局限**：可磨性依赖于问题的结构特性

## 关联概念

- [[AI-in-Mathematics]] — AI在数学中的成功依赖于可磨性
- [[Coding-Agents]] — 代码的可磨性使其成为AI的理想应用领域
- [[Sample-Efficiency]] — 可磨性允许并行化，提高样本效率

## 来源

- [[20260701-grant-sanderson-ai-math-future]] — Grant Sanderson与Dwarkesh Patel的播客访谈