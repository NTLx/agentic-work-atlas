---
type: entity
title: Delegative-UI
aliases:
  - Delegative UI
  - 委派式交互
  - Slow Dialogue
  - 慢速对话
definition: "用户将目标或部分决策与执行委托给 Agent，通过进度观察、异常升级、干预及结果验收维持控制的交互设计。可与逐轮对话、直接操作和主动通知组合，反馈周期不是定义条件。"
created: 2026-07-17
updated: 2026-11-28
evidence_level: medium
claim_type: synthesized
tags:
  - interaction-design
  - AI-Agent
  - human-agent-interaction
  - delegation
  - organization
related_entities:
  - "[[Flattening-as-Governance-Consequence]]"
  - "[[Judgment-Degradation-Cascade]]"
  - "[[Permission-Ratchet-Mechanism]]"
  - "[[Carbon-Silicon-Division]]"
  - "[[ACI-Agent-Computer-Interface]]"
source_raw:
  - "[[20260717-openai-scorecard-ai-age]]"
  - "[[How Anthropic’s product team moves faster than anyone else - Cat Wu (Head of Product, Claude Code)]]"
---

# Delegative UI（委派式交互）

> [!definition] 定义
> 用户将部分工作委托给 Agent，并通过可观察进度、适当的澄清与干预、结果验收和异常升级维持控制。“慢速对话”是其中一种交互形态，不是充分必要定义：委派可伴随高频状态更新，交互式对话也可能跨天。

## 关键数据点

- [[20260717-openai-scorecard-ai-age]] 提供 ready-to-use / needs-correction / needs-escalation 的结果分类，以及行动前权限与 review 阈值的设计建议；属于厂商框架，不是 UI 对照试验。
- 本页 2026-07-17 原版来自模型模拟圆桌与 think 综合。所谓 Norman 矩阵、Simon 级联、Victor-Karpathy 度量约定定理、Seely Brown 四权利均未定位到这些学者发表相应命题的原始证据，不应归为其真实发言或定理。
- 暂无本页所需的不同交互方式长期能力保持、错误传播系数或通知频率效应的直接实测。以下是待验证的设计假设。

## 选择委派程度

| 任务条件 | 候选设计 |
|---|---|
| 目标稳定，路径明确 | 确定性自动化或有界委派；按成本和风险选择 |
| 目标稳定，路径不确定 | 可委派探索，限制权限，设置阶段证据及失败升级 |
| 目标不稳定，路径明确 | 先澄清目标，或委派可逆的信息收集 |
| 目标与路径都不稳定 | 多轮协作、可逆试探、阶段性委派；随证据调整 |

上述矩阵是本 Wiki 的分析工具，不是已验证的最优决策规则。目标不明确并不排除委派，关键是能否界定探索范围、风险和停止条件。

## 反馈与认知成本

反馈延迟可能使错误假设更晚暴露，产生返工或错误的用户心智模型；也可能降低无关中断。频率不能替代反馈质量。不存在本页证据支持的固定传播系数 k>1 或认知损失乘法定律。

设计时分别衡量：人工主动投入时间、墙钟时间、澄清次数、错误发现延迟、返工、结果质量、接管与恢复成本。若关注专业能力保持，还需独立的无 AI 迁移/保持测试，不能用任务成绩代替。

候选缓解措施：可核验的阶段状态、关键选择及其依据、可暂停/取消的执行点、事后溯因。模型自述不等于真实执行轨迹，停止也不等于撤销外部效果。

## 与组织权威及 Ambient UI 的关系

前提表达、编排和验收能力可能影响实际工作分配，但不自动改变正式授权或必然导致组织扁平化。参见 [[Flattening-as-Governance-Consequence]]。

主动通知（Ambient）是系统发起交互的方式，可与委派、对话共同存在。通知成本受时机、内容、任务相关性和可控性影响；尚无证据支持 N 次微打断必然比一次完整打断更昂贵。可忽略、可设频率、解释推送理由、退出是候选产品设计原则，不宣称为已确立或全球缺失的法律权利。

## 前提与局限性

- 委派并不意味着全程无人监督，须按影响范围、可逆性和授权安排检查点。
- 过程观察、结构化摘要和高频对话都可能提供有用反馈；不能先验规定谁拥有“全带宽”。
- 元操作能否支持独立判断力的形成和保持，需要明确测量目标并做经验检验；测量约定与技术可行性均重要。
- 不从模型圆桌推导学者背书、因果效应或普遍制度缺失。

## 关联概念

- [[Flattening-as-Governance-Consequence]] — 待检验的组织权力分配机制。
- [[Judgment-Degradation-Cascade]] — 需独立测试的专业能力风险假设。
- [[Permission-Ratchet-Mechanism]] — 委派授权的生命周期与撤销。
- [[Carbon-Silicon-Division]] — 人机任务分配。
- [[ACI-Agent-Computer-Interface]] — Agent 与工具/环境的接口，与人机交互互补。
