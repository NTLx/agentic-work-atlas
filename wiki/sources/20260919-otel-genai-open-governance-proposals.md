---
type: source-summary
title: "OpenTelemetry GenAI open governance and orchestration proposals — 2026-09-19 snapshot"
source_raw:
  - "[[20260919-otel-genai-open-governance-proposals]]"
canonical_url: "https://github.com/open-telemetry/semantic-conventions-genai/issues/204"
raw_state: full
source_locator:
  - "open PR dashboard snapshot"
  - "authorization #291 / guardrail #427 / handoff #447 / action gate #457"
  - "governance semantics remain proposal-layer"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - observability
  - governance
evidence_level: medium
claim_type: extracted
---

# OpenTelemetry GenAI open governance proposals

## 编译摘要

### 1. 浓缩

- authorization、handoff、guardrail/security finding、action gate/ledger 等字段已经进入 OTel GenAI SIG 的设计讨论。
- 但截至本轮快照，这些仍是 open proposal，不能和 current-main normative semantics 混写。
- 这反过来提供了一个清晰边界：OTel 当前擅长表达“发生了哪些被 instrument 的 operation”，治理决策与效果闭环仍在演进。

### 2. 质疑

- Dashboard 自动生成且自身声明 grouping 可能有误；这里只用它核对 PR 存在/开放状态，不从 reviewer grouping 推导事实。
- proposal 的字段不能被当作已经可跨厂商依赖的 schema。
- 旧 agenda 中 PR #483 本轮未核实，因此移除其事实地位。

### 3. 对标

- 对 CR-004：区分 current observable surface 与 proposed governance surface。
- 对 [[Agent-Observability]]：观测标准的演化方向本身显示 authorization/effect lineage 尚未闭合。
- 对 [[Agent-Security]]：action gate 与 ledger 仍不能假定为标准 trace 默认能力。

## 关联概念

- [[Agent-Observability]]
- [[Agent-Security]]
