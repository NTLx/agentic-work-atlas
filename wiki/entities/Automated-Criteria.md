---
type: entity
title: Automated Criteria
aliases:
  - 自动化判据
definition: "在 Agent 工作流中，用于客观判定 Agent 执行结果是否成功的机器可读标准，包括编排层状态、产物存在性验证以及预定义协议码（如 ANALYZE_RESULT: PASS）。"
created: 2026-06-10
updated: 2026-09-20
evidence_level: medium
claim_type: mixed
tags:
  - verification
  - agentic-engineering
related_entities:
  - "[[Constraint-Driven-Engineering]]"
  - "[[Verifiability]]"
source_raw:
  - "[[20260610-qwen-constraint-driven-engineering-experiment]]"
  - "[[2026-ai-agent-evaluation-pipeline-methodology]]"
  - "[[20260626-llm-as-judge-healthcare]]"
---

# Automated Criteria（自动化判据）

> [!definition] 定义
> **Automated Criteria** 是闭环控制系统的核心节点。它解决了“模型返回一段话，我们如何知道它到底做完没有”的工程挑战。

## 关键数据点
- **三层判定体系**:
  1. **编排层 (Orchestration Layer)**: 监控退出码（Exit Code）、轮数上限（Max Turns）。
  2. **产物层 (Artifact Layer)**: 实地检查文件系统（如 APK 是否生成）。
  3. **协议层 (Protocol Layer)**: 文本暗号协议（如 `VALIDATION_RESULT: PASS`）。
- **证据边界**: Qwen 单案例显示分层判据与“带错纠正”共同构成长期闭环；独立评测方法材料也把 deterministic grader、校准后的 LLM judge 与 CI gate 作为生产管线组件。但现有来源没有提供可支持“成功率数量级提升”这一跨项目强结论的统一对照分母。

## 前提与局限性
- **前提**: 需要 Harness 具备感知运行环境（文件系统、终端状态）的能力。
- **判据类型边界**: deterministic check、规则 rubric 与 LLM-as-a-Judge 的可靠性条件不同，不能因为都可自动执行就视为同等强度的 oracle。
- **局限**: 过严的判据可能导致 Agent 陷入死循环，过松则导致“伪交付”；LLM judge 还需要独立校准与 reference/evidence 边界。

## 关联概念
- [[Constraint-Driven-Engineering]]
- [[Verifiability]]
- [[Convergence-vs-Generation]]
- [[Agent-Harness]]
