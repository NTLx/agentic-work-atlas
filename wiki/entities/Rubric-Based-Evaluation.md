---
type: entity
title: Rubric-Based Evaluation
aliases:
  - rubric-based evaluation
  - rubric evaluation
  - Agent Optimizer
definition: "用具体行为检查项（rubric）取代泛化指标（groundedness/coherence）来评估生产 Agent 的方法。每个 rubric 是针对特定用例的 yes/no 检查，由拥有该 Agent 的团队编写。Microsoft 的 Agent Optimizer 可基于 rubric 失败自动生成候选修复。"
created: 2026-07-14
updated: 2026-07-30
evidence_level: high
claim_type: mixed
tags:
  - evaluation
  - production-agents
related_entities:
  - "[[Agent-Verification]]"
  - "[[Agent-Harness]]"
  - "[[Harness-Engineering]]"
  - "[[LLM-as-a-Judge]]"
  - "[[Evaluator-Miscalibration]]"
  - "[[Goodharts-Law]]"
source_raw:
  - "[[20260713-microsoft-ships-ai-agents-enterprise-scale]]"
  - "[[20260729-similarweb-langsmith-agent-report-evaluation]]"
---

# Rubric-Based Evaluation

> [!definition] 定义
> **Rubric-Based Evaluation** 是用具体行为检查项（rubric）取代泛化指标来评估生产 Agent 的方法。每个 rubric 是针对特定用例的 yes/no 检查，反映 Agent **实际应该做什么**。"Generic metrics tell you whether the agent works. They don't tell you whether the agent works right."（Marco Casalaina）

## 泛化指标的天花板

通用评估指标（groundedness、coherence、task completion）有用但有上限：
- 可以判断 Agent 是否调用了正确的工具
- 无法判断 Agent 是否做了正确的中间步骤

例：餐厅预订 Agent 成功创建了预订，但没有询问用户偏好的时间、没有确认可用性——技术上成功，用户体验失败。

## Rubric 设计

Rubric 是针对特定用例的 yes/no 行为检查：

- 当用户给出部分请求时，Agent 是否询问缺失信息？
- 在声称预订可用前，Agent 是否验证了系统可用性？
- 完成预订后，Agent 是否向用户确认了详情？

关键特征：**由拥有 Agent 的团队编写**，因此反映实际期望行为而非抽象指标。

## 分级锚点 vs yes/no 检查（SimilarWeb 2026 补充）

Microsoft 的 rubric 是 yes/no 行为检查，回答"行为有没有做"；SimilarWeb Data Studio 案例（`[[20260729-similarweb-langsmith-agent-report-evaluation]]`）把 rubric 扩展为**分级评分锚点**，回答"做得有多好"——开放式长文输出（同一问题可有多份合格报告）无法用 yes/no 覆盖：

- 每个质量维度独立 rubric，带显式锚点（如 `source_integration` 的 0.0/0.3/0.8/1.0 四档描述），裁判返回每维度分数而非单一总判。
- 每个标准返回三件套：score + gap（差距摘要）+ detail（一句话理由）——低分永远附带可检查的理由。
- rubric 之外叠加 faithfulness 检查（每条论断是否由检索数据支持，捕捉"自信但无根据"陈述）与 A/B 基线裁判（新版本与已接受历史版本并排比较）。

关键失效模式：锚点措辞即激励结构。奖励"来源数量"的锚点会被"堆模糊引用"游戏化（[[Goodharts-Law]] 的评估层形态）；两个标准互相拉扯时聚合分数掩盖冲突——详见 [[Evaluator-Miscalibration]]。修复方式是把锚点改为奖励真正想要的东西（命名、可验证、绑定具体论断的来源），同一份报告的分数从 0.7 落到 0.3，与评语一致。

## Self-Improving Loop（Agent Optimizer）

Microsoft 的 Agent Optimizer 将 rubric 评估与自动改进结合：

1. 运行 Agent 对抗测试交互集
2. 对每个 rubric 评分
3. 当 rubric 失败时，自动生成多个候选修复（改写 system prompt、调整工具使用、切换模型、调优 skills）
4. 并行评分各候选
5. 提升最优版本为新 Agent 版本

**同一循环既度量 Agent 也改进 Agent。**

Foundry 还可以从 Agent 配置和生产 traces 自动草拟 rubric——从真实流量而非空白页出发。

## 与 Continuous Evaluation 的配合

| 评估类型 | 回答的问题 | 时机 |
|---------|-----------|------|
| Continuous Evaluation | 行为是否变化了？ | 实时流量采样 |
| Rubric-Based Evaluation | 行为是否正确？ | 测试交互集 |
| Agent Optimizer | 如何自动修复？ | rubric 失败时 |

三者构成完整的生产评估管线：continuous 发现漂移 → rubric 定位问题 → optimizer 生成修复。

## 前提与局限性

- Rubric 质量取决于团队对 Agent 期望行为的理解深度
- 自动草拟的 rubric 仍需人工审核
- Optimizer 自动改写 prompt 有失控风险——如果 rubric 有缺陷，可能收敛到错误行为
- 主要来源是 Microsoft Foundry 的产品叙事，独立验证有限
- **锚点即激励**：rubric 锚点写错会被 game（模糊引用刷广度分），且标准间冲突会被聚合分数掩盖——校准错误的评估比没有评估更糟（[[Evaluator-Miscalibration]]）；rubric 需要像代码一样接受迭代验证

## 关联概念

- [[Agent-Verification]] — Rubric 是 verification 的一种结构化形式
- [[Agent-Harness]] — 评估是 harness 的关键层
- [[Harness-Engineering]] — rubric 设计是 harness engineering 的实践之一
- [[Validation-Pipeline]] — rubric 可集成到验证管线中

## 关键数据点

- Microsoft Agent Optimizer (2026-07): 基于 rubric 失败自动生成候选修复——改写 prompt、调整工具、切换模型、调优 skills，并行评分后选最优
- Foundry 可从 Agent 配置和生产 traces 自动草拟 rubric，从真实流量而非空白页出发
- 生产评估管线三件套：Continuous Evaluation（检测漂移）→ Rubric（定位问题）→ Optimizer（生成修复）
