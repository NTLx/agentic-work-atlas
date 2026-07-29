---
type: entity
title: Grindability vs Verifiability
aliases:
  - 可磨性与可验证性
  - 可磨性vs可验证性
definition: "AI成功的关键因素区分：可磨性（问题可容器化、并行化、自动化）比可验证性（问题有明确正确答案）更重要"
created: 2026-07-01
updated: 2026-07-29
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
  - '[[20260719-if-ai-is-so-great-why-isnt-it-working]]'
  - '[[20260728-openai-scientific-computing-field-report.pdf]]'
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

## 域边界：科学域的可验证性约束（07-29）

OpenAI 科学计算 field report（[[20260728-openai-scientific-computing-field-report.pdf]]）给出本命题的域边界：在科学计算（微妙数值正确性攸关科学结论）中，**可验证性成为绑定约束**——报告结论句即 "the current bottleneck remains verification and validation"。

更重要的是可验证性直接决定可达到的自主程度：

| 案例 | 可验证性 | 可达自主程度 |
|------|---------|-------------|
| HI.SIM（字节级一致验收） | 极强 | 初始 prompt 后近无人类介入 |
| MHCflurry（数值容差一致） | 强 | 人类定义容差并核查 |
| bayesm（新统计功能） | 弱（后验摘要一致不够） | 密集人类诊断（收敛诊断 + 模拟校准 + 与原实现对比） |
| FrontierSWE from-scratch 任务 | 规格难明 | agent 五项无一完成 |

**命题精化**（综合判断）：**可磨性决定速度上限，可验证性决定自主上限**。两命题不矛盾——数学域（Grant Sanderson）可验证性高（形式证明可查），故可磨性主导；科学域可验证性低（微妙数值正确性需人类裁决），故可验证性成为瓶颈。哪个因素主导，看问题本身的可验证性剖面。

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