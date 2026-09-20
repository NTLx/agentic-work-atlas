---
type: source-summary
title: "AGENTOPS01-BP02: Design multi-agent handoff procedures with human-in-the-loop escalation"
source_raw:
  - "[[20260610-aws-agentic-handoff-contract]]"
canonical_url: "https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops01-bp02.html"
raw_state: full
source_locator:
  - "handoff as versioned data contract"
  - "task/completed-work/memory-artifacts/handoff-reason package schema"
  - "receiver capability/availability plus handoff latency/completeness/success telemetry"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - governance
  - verification
evidence_level: high
claim_type: extracted
---

# AGENTOPS01-BP02: Design multi-agent handoff procedures with human-in-the-loop escalation

## 编译摘要

### 1. 浓缩

- **核心结论 1：handoff 应该被当成版本化 data contract。**
  - 关键证据：AWS 要求 context package 包含 task description、completed work、memory artifacts 与 handoff reason，并建议 version schema。
- **核心结论 2：receiver 是运行时变量，不是固定的人名。**
  - 关键证据：路由需要 capability、availability、acceptance criteria；receiver 不可用时必须有重新分配/通知路径。
- **核心结论 3：agent-to-agent routing 与 agent-to-human judgment escalation 必须分开。**
  - 关键证据：前者由 capability mismatch 触发，后者由低置信、高风险或 retry budget exhaustion 触发。
- **核心结论 4：handoff quality 必须可观测。**
  - 关键证据：AWS 明确要求监控 success rate、handoff latency、context-transfer completeness。

### 2. 质疑

- 这是规范性 best practice，不是效果实证。
- 指标“可记录”不等于这些指标已经被证明能预测最终人类正确率。
- AWS 没有在固定 receiver / queue 下做 packet schema 的随机消融。

### 3. 对标

- 对 EX-003：把 **receiver / packet / acceptance / telemetry** 明确成可操作字段层。
- 对 [[Escalation-Based-Human-Oversight]]：例外升级不能只定义 trigger，还要定义交接契约与接收失败语义。
- 对 [[Alert-Closed-Loop]]：handoff success 必须继续追踪到 receiver 接收和处置，而不是在 sender 发出后结束。

## 关联概念

- [[Escalation-Based-Human-Oversight]]
- [[Alert-Closed-Loop]]
- [[Agent-Security]]
