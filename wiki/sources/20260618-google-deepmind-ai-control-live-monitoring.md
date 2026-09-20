---
type: source-summary
title: "Securing the future of AI agents"
source_raw:
  - "[[20260618-google-deepmind-ai-control-live-monitoring]]"
canonical_url: "https://deepmind.google/blog/securing-the-future-of-ai-agents/"
raw_state: full
source_locator:
  - "coverage / recall / time-to-response"
  - "asynchronous vs synchronous response by risk"
  - "about one million coding-agent tasks analyzed; Gemini Spark live monitor"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - observability
  - agent-security
evidence_level: high
claim_type: mixed
---

# Google DeepMind AI Control live monitoring

## 编译摘要

### 1. 浓缩

- **可观测性必须和识别能力分开**：coverage 说明“看了多少流量”，recall 说明“异常被抓住多少”，二者不可互代。
- **行为监控还必须带时间维度**：高风险动作若在事后才发现，即使 trace 完整也可能已经无安全价值。
- **Google 已披露大规模 operational prototype**：约一百万 coding-agent tasks 被异步监控系统分析，并用于建设 Gemini Spark live monitor。
- **行为信号不是意图真值**：Google 明确说多数 flagged events 来自误解/过度积极，而非 adversarial intent。

### 2. 质疑

- 一百万任务是规模，不是 recall/precision 证明。
- 页面没有给出逐案 synchronous block、false positive 或 containment latency。
- “live monitor”存在不等于 action surface 全覆盖。

### 3. 对标

- 对 CR-004：把 behavior observability 收窄成 coverage × recall × response latency。
- 对 [[Agent-Observability]]：trace visibility 和 behavioral assurance 必须分开。
- 对 [[Escalation-Based-Human-Oversight]]：flag 只是 handoff chain 起点。

## 关联概念

- [[Agent-Observability]]
- [[Agent-Security]]
- [[Escalation-Based-Human-Oversight]]
