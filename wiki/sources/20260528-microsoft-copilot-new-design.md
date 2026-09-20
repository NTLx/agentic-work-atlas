---
type: source-summary
title: "Introducing a new design for Microsoft 365 Copilot"
source_raw:
  - "[[20260528-microsoft-copilot-new-design]]"
canonical_url: "https://www.microsoft.com/en-us/copilot/blog/2026/05/28/introducing-a-new-design-for-microsoft-365-copilot/"
raw_state: full
source_locator:
  - "Jon Friedman / Microsoft 365 Chief Design Officer"
  - "output quality + task-aware workspace + in-app agentic interaction"
  - "rollout metrics: >50% load reduction, ~10% p95 response improvement, usage lifts across apps"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - design
  - ai-era
evidence_level: high
claim_type: mixed
---

# Microsoft 365 Copilot redesign

## 编译摘要

### 1. 设计对象明确越过界面

Jon Friedman 直接把 AI 时代最重要的 UX 对象从单纯 interface 扩展到 output quality：

- tone；
- structure；
- readability；
- usefulness；
- trustworthiness。

这与 Anthropic 的 system-state / executable-prototype 路径不同，但指向同一稳定变化：AI 产品设计对象不再只是 screen。

### 2. interaction model 从 prompt box 转向 task-aware workspace

Copilot 被重新设计成：

- app 内一致入口；
- 直接理解文档上下文；
- 在 canvas / side pane / agentic mode 间流动；
- 能建议或执行修改，并给用户明确状态信号。

这使 design 同时覆盖 interaction、context visibility、agent action 与 control surface。

### 3. 有真实 rollout 指标

与多数设计访谈不同，这篇给出了部署数据：

- load time 降低超过 50%；
- complex-prompt p95 first-token latency 改善约 10%；
- Word / Excel / PowerPoint / Outlook usage 分别增加 27% / 33% / 43% / 30%。

但这些是短期 rollout 指标，不能自动解释为长期满意度、质量或留存。

### 4. 对标

- 对 [[AI-Era-Designer-Role]]：补齐“output 本身是设计对象”和 deployment metric。
- 对 [[Agent-Observability]]：可见状态与可控 intelligence layer 是体验设计问题，但不替代系统级 effect trace。

## 关联概念

- [[AI-Era-Designer-Role]]
- [[Agent-Observability]]
