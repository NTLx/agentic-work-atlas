---
type: source-summary
title: "How Anthropic teams use Claude Code — Product Design"
source_raw:
  - "[[20250724-anthropic-product-design-claude-code]]"
canonical_url: "https://claude.com/blog/how-anthropic-teams-use-claude-code"
raw_state: full
source_locator:
  - "Anthropic official internal Product Design case study"
  - "direct code/state changes + interactive prototypes + edge-case/system-status mapping"
  - "self-reported 2–3x execution speed / weeks-to-hours coordination examples"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - design
  - ai-era
evidence_level: medium
claim_type: mixed
---

# Anthropic Product Design × Claude Code

## 编译摘要

### 1. 工作对象扩展

设计交付不再只停在 Figma/mock/spec：

- 直接前端 polish；
- state-management 修改；
- executable prototype；
- error / logic / system-status 枚举；
- codebase-wide copy/compliance change。

这支持“AI 产品设计对象扩展到可执行系统状态”，而不是“UI 设计消失”。

### 2. 协作边界变化

设计师更靠近代码，因此减少一部分 design→engineering 翻译成本；functional prototype 也让工程师更快理解和继续实现。

### 3. 速度证据的边界

2–3x 与 weeks-to-hours 都是 Anthropic 内部自报案例，不是 cross-company benchmark，也没有同口径质量/返工/事故分母。

### 4. 对标

- 对 [[AI-Era-Designer-Role]]：提供“代码化原型 + state/system reasoning”的团队级实证。
- 与负责人访谈配合后，可把“design-object expansion”与“judgment/decision responsibility”分开，不用从速度数据推断责任迁移。

## 关联概念

- [[AI-Era-Designer-Role]]
- [[Agent-Observability]]
