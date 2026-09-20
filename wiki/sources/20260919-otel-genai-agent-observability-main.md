---
type: source-summary
title: "OpenTelemetry GenAI Agent and Framework Semantic Conventions — current main"
source_raw:
  - "[[20260919-otel-genai-agent-observability-main]]"
canonical_url: "https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md"
raw_state: full
source_locator:
  - "Development-status current main"
  - "create/invoke/workflow/plan/execute-tool plus retrieval/memory observability surface"
  - "no current normative authorization/post-state/revoke fields on cited span pages"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - observability
  - verification
evidence_level: high
claim_type: extracted
---

# OpenTelemetry GenAI Agent Observability — current main

## 编译摘要

### 1. 浓缩

- **结构层可枚举性显著增强**：current main 已把 agent creation/invocation、workflow、plan、tool execution，以及更广的 retrieval/memory 操作纳入通用 span vocabulary。
- **标准化 trace 仍是“被 instrument 的逻辑操作”视图**：它描述调用、父子关系、agent/version/conversation 等元数据，不等于真实 action surface 已闭合。
- **治理结果字段仍不是现行规范的一部分**：在本轮核对的 current agent/framework 与 GenAI span 页面中，没有 authorization decision、canonical external post-state、revoke/recovery 这样的 normative field。

### 2. 质疑

- Development status 意味着字段和边界仍可能演化。
- “没有标准字段”不等于厂商不能用自定义 span/event 记录。
- OTel 只能标准化被 instrumentation 捕获的路径；旁路调用、provider-side effect 与日志缺失仍需要其他证据。

### 3. 对标

- 对 CR-004：支持“结构层可枚举”的条件版本——只有已声明且被 instrumentation 覆盖的结构可枚举。
- 对 [[Agent-Observability]]：trace schema 是观测入口，不是 behavior coverage proof。
- 对 [[Agent-Security]]：authorization / effect / recovery 仍需额外事件谱系。

## 关联概念

- [[Agent-Observability]]
- [[Agent-Security]]
- [[Verifiable-Agent-Engineering]]
