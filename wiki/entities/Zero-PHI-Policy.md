---
type: entity
title: Zero-PHI Policy
aliases:
  - 零 PHI 策略
  - Zero-PHI
definition: "一种数据隐私保护策略，在任何文本到达 LLM 之前，先通过确定性规则识别并替换所有受保护健康信息（PHI），确保敏感数据永远不会进入模型推理流程。"
created: 2026-05-10
updated: 2026-05-10
tags:
  - Privacy
  - AI-Safety
  - Healthcare-AI
related_entities:
  - "[[Agent-Orchestration]]"
  - "[[Agentic-Engineering]]"
source_raw:
  - "[[OncoAgent A Dual-Tier Multi-Agent Framework for Privacy-Preserving Oncology Clinical Decision Support]]"
---

> [!definition] 定义
> Zero-PHI 策略是一种"设计即合规"的数据隐私保护模式：在处理管道的最前端（Ingestion 节点）运行专用脱敏节点，用确定性规则识别并替换患者姓名、出生日期、病历号、地址、机构标识等受保护健康信息，脱敏后的表示存入状态，原始文本立即丢弃，确保 PHI 永远不会到达任何下游 LLM 调用。

## 关键数据点

- **执行位置**: 作为 Ingestion 节点的第一个处理步骤，在任何文本到达 LLM 之前
- **脱敏范围**: 患者姓名、出生日期、MRN 号码、地址、机构标识符
- **替换方式**: 用临床中性占位符替换
- **合规标准**: 满足 HIPAA 去标识化要求（设计层面，非策略层面）
- **架构保障**: 脱敏后的表示存入 AgentState，原始文本丢弃

## 前提与局限性

- **前提**: 需要可靠的 PHI 识别规则（正则表达式或 NER 模型）
- **前提**: 脱敏不能损害临床语义，占位符需要保持上下文可理解性
- **局限性**: 确定性规则可能遗漏非标准格式的 PHI
- **局限性**: 仅覆盖健康信息领域，其他敏感数据类型需要类似但不同的策略

## 关联概念

- [[Agent-Orchestration]] — Zero-PHI 节点是 Agent 编排中的数据预处理环节
- [[Agentic-Engineering]] — 隐私前置是 Agentic 工程中处理敏感数据的最佳实践
