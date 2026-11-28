---
type: entity
title: Validation-Tether
aliases:
  - 验证系绳
  - Validation Tether
  - 实质验证依赖
definition: "Lovett 提出的理论关系：有效 AI 编排需要能够独立判断实质正确性的验证能力；表面合理性不等于领域正确性。该框架强调内部化精通，但尚未证明个人默会专长是所有任务验证的必要条件。"
created: 2026-08-13
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - expertise
  - judgment
related_entities:
  - "[[Internalized-Mastery]]"
  - "[[Distributed-Mastery]]"
  - "[[Cognitive-Commons]]"
  - "[[Verifiability]]"
  - "[[Over-Inference]]"
  - "[[Human-Governor-Agent-Operator]]"
source_raw:
  - "[[20260731-tragedy-cognitive-commons-ai-expertise]]"
---

# Validation Tether（验证系绳）

> [!definition] 定义
> **Validation Tether（验证系绳）** 指有效 AI 编排（[[Distributed-Mastery]]）对实践者 [[Internalized-Mastery]]（内化领域知识、稳健心智模型、默会理解）的根本依赖：AI 能产出"看起来正确"的输出，作者提出领域判断依赖；不能从该框架推出只有个人专家才能验证所有任务。独立测试、参考标准、真实实验与团队复核可能提供不同验证通道（本库综合）。职业级能力耗尽是待检验预测。

## 两级验证

| 级别 | 检测能力 | 依赖 |
|------|---------|------|
| 表面验证（Surface Validation） | 逻辑自洽、格式、总体合理性 | 可通过与 AI 共事的训练获得；不需要领域专长 |
| 实质验证（Substantive Validation） | 领域特定错误、上下文不恰当的推荐、表层下缺陷 | 依赖任务适用的独立证据与判断；原框架强调内化领域知识和默会理解 |

关键不对称：形式合理不保证领域正确。Vicente & Matute (2023) Experiment 3（197人，虚构医学分类与模拟偏置AI）中80.7%参与者察觉推荐有误，许多人仍依赖推荐；不是80.7%都继续遵从，也不是专家验证失败率。两阶段结果支持短期偏差延续；原实验明确排除了先验领域专长的影响，不能据此证明默会专长是唯一纠错机制。[原研究](https://www.nature.com/articles/s41598-023-42384-8)（本轮核对，未晋升新来源）。Dell'Acqua et al. (2026)：精英顾问在 AI 能力边界内的任务获益、边界外任务绩效下降，且无法可靠区分两种情境。

## 认识论前提（原文）

- Hayek（1945）：经济上关键的知识是分散且绑定特定时空的，无法被任何中心化表征捕获。
- Polanyi（1966）：人的知超过所能言传。
- 实质验证因此需要可言传之外的知识——作者对默会知识的理论解释；AI 能否辅助形成该能力仍需独立检验。这与 [[Over-Inference]] 的"表达 ≠ 拥有"镜像：AI 能说出的 ≠ 它能实质验证的。

## 公地含义

- 原文 Figure 1 为候选因果链（含岗位消除与无内化增强两条路径），不是已观察的代际结果。另区分专家存量减少与验证功能下降。
- 治理含义：风险应对偏好投资而非禁止——补贴保持发展性基础设施的公司、按质量而非数量奖励产出、持续教育要求周期性"无 AI 绩效评估"。

## 关键数据点

- Vicente & Matute (2023) Experiment 3：80.7%报告察觉错误；197人随机分两种辅助/无辅助次序（98/99）；偏差延续及部分泛化，非专业技能退化纵向试验
- Dell'Acqua et al. (2026)：精英顾问在 AI 能力边界内获益、边界外绩效下降，且无法可靠区分两种情境
- 概念来源：Lovett (2026)

## 前提与局限性

- 假设 AI 在可预见未来仍需人类实质验证——若 AI 达到高自主可靠性，问题变为 displacement 而非 depletion。
- AI 辅助表现不自动证明独立验证能力；是否通过有反馈的 AI 辅助学习形成该能力须测量，尚无直接纵向实验证明代际验证能力确实在下降（作者列为研究议程）。
- 原文 Table 2 的 validation tether strength 为植入错误检出率候选指标，并非已验证量表；需分别测错误检出、拒绝/修正、正确建议保留、独立验收及延迟迁移。领域知识、认识论立场、授权和工具证据是不同变量；与 CR-005 的共同纵向队列需求相容，不构成其结案。

## 关联概念

- [[Internalized-Mastery]] — 系绳的锚点
- [[Distributed-Mastery]] — 被系绳约束的专长形态
- [[Verifiability]] — 可验证性的认知侧面：识别 vs 生成的分离在此重演
- [[Human-Governor-Agent-Operator]] — 人类监督角色的领域知识前提
- [[Cognitive-Commons]] — 候选因果链中的验证功能退化，不等同专家存量耗尽