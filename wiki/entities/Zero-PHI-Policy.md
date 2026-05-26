---
type: entity
title: Zero-PHI Policy
aliases:
  - 零 PHI 策略
  - Zero-PHI
definition: "在任何 LLM 调用前先用确定性管道移除受保护健康信息的隐私架构模式"
created: 2026-05-10
updated: 2026-05-25
tags:
  - Privacy
  - AI-Safety
  - Healthcare-AI
related_entities:
  - "[[Agent-Orchestration]]"
  - "[[Agentic-Engineering]]"
  - "[[Hardware-Sovereignty]]"
  - "[[Corrective-RAG]]"
  - "[[Reflexion]]"
  - "[[Verifiable-Agent-Engineering]]"
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
- **OncoAgent 位置**: Zero-PHI 位于 Router 和 RAG 之前，确保 Specialist、Critic、Formatter 等下游 LLM 节点只能看到去标识化文本
- **状态管理**: 系统使用 thread_id 关联 PatientMemoryStore，而不是把患者原始文本作为可传递上下文

## 为什么它不是普通脱敏

普通脱敏常发生在日志、导出或人工审查阶段，默认系统内部仍能看见原始数据。Zero-PHI 的差异在于把隐私边界前移到 Agent 执行图的入口：任何模型调用、检索查询、批评者校验和最终格式化都只能处理去标识化后的表示。

这会改变系统设计：

- 隐私不再依赖 prompt 约束，而依赖确定性预处理。
- LLM 不被要求“不要泄露 PHI”，因为它从未获得 PHI。
- 日志、trace、RAG query 和失败重试天然更容易审计。
- 人工接管仍可通过受控系统查看原始病历，而不是让模型上下文携带原文。

因此 Zero-PHI 是 [[Verifiable-Agent-Engineering]] 的一个数据边界模式：先减少 Agent 能犯错的空间，再谈模型安全。

## 前提与局限性

- **前提**: 需要可靠的 PHI 识别规则（正则表达式或 NER 模型）
- **前提**: 脱敏不能损害临床语义，占位符需要保持上下文可理解性
- **局限性**: 确定性规则可能遗漏非标准格式的 PHI
- **局限性**: 仅覆盖健康信息领域，其他敏感数据类型需要类似但不同的策略
- **局限性**: 如果脱敏破坏关键临床上下文，例如年龄、时间线、病灶位置或家族史，系统可能降低医疗推理质量
- **局限性**: Zero-PHI 不能替代访问控制、审计、数据驻留和医生责任，它只是防止 PHI 进入模型上下文的一层

## 关联概念

- [[Agent-Orchestration]] — Zero-PHI 节点是 Agent 编排中的数据预处理环节
- [[Agentic-Engineering]] — 隐私前置是 Agentic 工程中处理敏感数据的最佳实践
- [[Hardware-Sovereignty]] — 本地部署降低数据出域风险，Zero-PHI 降低模型上下文风险
- [[Corrective-RAG]] — 去标识化后的查询进入检索与评分流程
- [[Reflexion]] — Critic 只能验证去标识化输出，不能接触原始 PHI
- [[Verifiable-Agent-Engineering]] — Zero-PHI 是把隐私约束变成可验证工程边界的例子
