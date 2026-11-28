---
type: entity
title: Grindability vs Verifiability
aliases:
  - 可磨性与可验证性
  - 可磨性vs可验证性
definition: "可磨性指候选尝试的可重置、可并行和成本特征；可验证性指结果及效果能否可靠检查。二者相互制约，不存在普适重要性排序。"
created: 2026-07-01
updated: 2026-11-28
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
  - "[[20261125-oneill-weekend-machine-mathematics]]"
  - '[[20260701-grant-sanderson-ai-math-future]]'
  - '[[20260719-if-ai-is-so-great-why-isnt-it-working]]'
  - '[[20260728-openai-scientific-computing-field-report.pdf]]'
---

# Grindability vs Verifiability

## 可磨性还有路线可达域的约束（O’Neill，2026-11）

[[20261125-oneill-weekend-machine-mathematics]] 的六阶矩实践发现，沿当前技术框架反复收紧参数仍存在低于研究目标的上限。作者观察到模型更容易持续优化固定路线，需要切换到重新评估方法的模式；建议使用目标和 checker 而非频繁人工打断。

- **综合判断**：可磨性决定固定路线上的搜索速度，可验证性约束自动采纳，**方法可达域**则决定继续搜索是否有意义。应记录路线理论上限、边际收益与停止条件，在预算内对照继续搜索和换路线；不能把运行时长视为进展。
- **边界**：一次自报实践，不是两种模式的控制实验；目标循环是作者事后提出的建议。

> [!definition] 定义
> 可磨性与可验证性是不同设计轴；可并行不等于可验证，能检验不等于能穷举。

## 核心要点

### 可磨性（Grindability）

**可磨性**是指问题可以容器化、并行化、自动化的程度。

**关键特征**：
- 可以在容器中运行
- 可以并行执行多个实例
- 尝试可重复或可比较；不要求结果确定
- 检查机制独立评价，不能由容器化推出正确

**例子**：
- 代码测试：可以容器化运行，自动验证结果
- 数学证明：可以形式化验证
- IMO几何问题：可以暴力求解

### 可验证性（Verifiability）

**可验证性**是指问题有明确正确答案的程度。

**关键特征**：
- 有可定义的验收或证据标准；可能有多个正确结果或统计不确定性
- 可以按协议检查结果、边界及实际影响
- 不一定可以并行化

**例子**：
- 证明定理：可以验证证明是否正确
- 网购包裹：可以验证是否送达
- 会议预订：可以验证是否成功

### 两轴为何需要分别测量

[原访谈](https://www.dwarkesh.com/p/grant-sanderson-2) 00:53:48后，Patel提出可重放、容器化及credit assignment的假设，Sanderson讨论形式化与自然语言IMO的变化。访谈未做因子对照，不支持可磨性普遍优于可验证性。容器可隔离状态但不保证确定性，diff相关不等于因果；独立验收、可信oracle及资源预算仍必需。

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

**命题精化**：搜索吞吐、验证成本及方法可达性是候选约束；真实自主性还取决于任务权限、安全、外部反馈、预算与风险。原两个“决定上限”作为启发式，不是数学定律。不同数学与科学任务均可有强/弱检查。

## 关键数据点

- 2024 AlphaGeometry 2接收形式化P4后19秒；不是端到端，也未单独识别并行的因果贡献。
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
- [[Sample-Efficiency]] — 并行提高尝试吞吐不等于减少达到同目标的样本量

## 来源

- [[20260701-grant-sanderson-ai-math-future]] — Grant Sanderson与Dwarkesh Patel的播客访谈