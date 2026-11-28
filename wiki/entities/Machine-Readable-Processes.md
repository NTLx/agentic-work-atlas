---
type: entity
title: Machine-Readable Processes
aliases:
  - Machine Readable Processes
definition: "结构化表达流程状态、输入输出、决策条件和规则，使受授权的 Agent 或确定性运行时可解释、执行并验证适合委派的工作流"
created: 2026-04-09
updated: 2026-11-28
tags:
  - AI-Agent
  - Process-Design
  - architecture
evidence_level: medium
claim_type: mixed
related_entities:
  - '[[Agent-First-Enterprise]]'
  - '[[Human-Governor-Agent-Operator]]'
  - '[[Harness-Engineering]]'
source_raw:
  - '[[Enabling agent-first process redesign]]'
  - '[[20260413-why-ai-first-strategy-wrong]]'
---

# Machine-Readable Processes

> [!definition] 定义
> Machine-Readable Processes 是指结构化、显式的流程定义，支持 AI Agent 读取流程并在受控执行层中运行；是否能自主优化取决于权限、效果测量、审批和变更治理。这是 Agent-First Enterprise 的技术基础设施。

## 核心要点

### 三大要素

| 要素 | 说明 | 示例 |
|-----|------|-----|
| **流程定义** | 机器可理解的工作流程描述 | YAML/JSON 格式的流程配置 |
| **政策约束** | 明确的边界和规则约束 | "审批金额上限"、"数据访问权限" |
| **结构化数据流** | 标准化的数据输入输出 | API 接口定义、数据 Schema |

### 与遗留流程的区别

| 维度 | 遗留流程 | Machine-Readable 流程 |
|-----|---------|----------------------|
| 表达形式 | 文档、手册、隐性知识 | 代码、配置、显式定义 |
| 执行方式 | 人工或既有自动化 | Agent/确定性执行器按合同操作 |
| 优化能力 | 人工分析或既有反馈控制 | 可自动提出优化；变更须受验证与授权 |

### 为什么 Agent 需要它
- Legacy processes 不是为自主系统设计的
- Agent 需要明确的规则边界来安全运营
- 结构化数据流支持实时决策

## 关键数据点

- 来源是2026-04-07的 MIT Technology Review Insights 咨询型内容，预算预测未在公开正文给出样本与基线；不作为流程有效性证据。
- Machine-Readable 流程的三大要素：流程定义（YAML/JSON）、政策约束（金额上限/权限）、结构化数据流（API/Schema）
- 遗留流程以文档、手册、隐性知识表达；Machine-Readable 流程以代码、配置、显式定义表达
- 结构化表达不是执行保证：须有实际状态、前置/终止条件、失败恢复、审计与资源侧权限控制。

## 前提与局限性

- 探索任务也可结构化目标、预算、验收和停止条件，不必预先规定所有推理步骤。
- 需要先有明确的 policy constraints，否则 Agent 缺乏安全运营边界
- 遗留系统的迁移成本可能很高——不是所有企业都能快速转换
- 机器可读流程假设数据流标准化，但现实中很多组织的数据流是碎片化的

## 关联概念

- [[Agent-First-Enterprise]] - Machine-Readable Processes 是其技术基础
- [[Human-Governor-Agent-Operator]] - 政策约束由人类 Governor 定义

## 来源

- Raw Source: [[Enabling agent-first process redesign]]
- Original URL: https://www.technologyreview.com/2026/04/07/1134966/enabling-agent-first-process-redesign/
