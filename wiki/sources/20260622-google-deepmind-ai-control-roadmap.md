---
type: source-summary
title: "GDM AI Control Roadmap v0.1"
source_raw:
  - "[[20260622-google-deepmind-ai-control-roadmap]]"
canonical_url: "https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/securing-the-future-of-ai-agents/gdm-ai-control-roadmap.pdf"
raw_state: full
source_locator:
  - "async/sync coverage, recall and time-to-response definitions"
  - "R1–R3 risk-conditioned monitoring/response requirements"
  - "R2 >99% coverage targets are roadmap requirements, not deployment results"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - observability
  - agent-security
evidence_level: high
claim_type: mixed
---

# GDM AI Control Roadmap v0.1

## 编译摘要

### 1. 浓缩

- **coverage、recall、latency 是三个独立的 assurance 量**：看了多少、抓住多少、多久响应不能用一个“有监控”概括。
- **高风险 observability 必须接到 synchronous response**：路线图把 block/resample/escalate 等 action prevention 计入 response coverage。
- **roadmap 给出具体目标但不是实绩**：R2 的 coverage >99%、asynchronous response <24h 等属于 mitigation requirements。
- **CoT visibility 有能力边界**：随着 oversight awareness / opaque reasoning 增强，路线图主动从 CoT 转向 behavior-based monitoring，并考虑更高级内部监控。

### 2. 质疑

- 数值阈值属于目标/设计要求，并没有本轮公开的逐案部署实测支撑。
- proxy-untrusted-model red teaming 是否代表真实 production distribution 是额外假设。
- coverage denominator 若只统计已 instrument 流量，仍可能遗漏旁路 action surface。

### 3. 对标

- 对 CR-004：正式把 behavior layer 写成 coverage × recall × time-to-response，并补 synchronous response coverage。
- 对 [[Agent-Observability]]：观测必须连接 response，才能对高风险动作形成安全意义。
- 对 [[Agent-Security]]：observability 仍不等于 authorization/effect/recovery。

## 关联概念

- [[Agent-Observability]]
- [[Agent-Security]]
- [[Escalation-Based-Human-Oversight]]
