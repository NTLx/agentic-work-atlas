---
type: source-summary
title: "GitHub availability report: May 2026 — account recovery and cache propagation"
source_raw:
  - "[[20260611-github-may-2026-recovery-cache-propagation]]"
canonical_url: "https://github.blog/news-insights/company-news/github-availability-report-may-2026/"
raw_state: full
source_locator:
  - "May 26 service-account suspension incident"
  - "12:16 restore → 12:20 exemption → 12:48 cache-flush redeploy → 12:56 full recovery"
  - "temporary hidden content restored; no data loss reported"
created: 2026-09-20
updated: 2026-09-20
tags:
  - source-summary
  - agent-security
  - incident-response
evidence_level: high
claim_type: extracted
---

# GitHub availability report: May 2026 — account recovery and cache propagation

## 编译摘要

### 1. 浓缩

- **核心结论 1：authority recovery 与 full recovery 不是同一时间点。**
  - GitHub 在 12:16 UTC 恢复服务账号，但直到 12:48 才通过 redeploy 刷新缓存状态，12:56 才确认完全恢复。
- **核心结论 2：防止再次触发与恢复当前状态也是两个动作。**
  - 12:20 加入 automated review exemption 解决 recurrence path，但它没有自动刷新此前已缓存的 account state。
- **核心结论 3：恢复验证需要检查业务可见后果。**
  - 事故期间少量 issue、PR、comment、discussion 被隐藏；GitHub随后恢复内容和 search index，并报告无数据丢失。

### 2. 质疑

- 这是 GitHub Actions/账号系统事故，不是 Agent dangerous-action rollback 实验。
- 时间线说明 recovery 有中间态，但不能给出 Agent revoke latency 或外部 compensation 成功率。
- “无数据丢失”与内容恢复是该事故的具体结果，不能外推为一般缓存/权限事故。

### 3. 对标

- 对 EX-005：提供 production anchor，证明 authority state、policy exemption、cache refresh 与 full recovery confirmation 可以分步发生。
- 对 [[Agent-Security]]：recovery 事件链至少应区分 authority restored/denied、dependent-state refresh、business-state verification 与 final close。
- 对 CR-004：只有服务 status 或账户状态不足以证明 recovery；应能关联依赖缓存和业务对象状态。

## 关联概念

- [[Agent-Security]]
- [[Operational-Responsibility]]
- [[Alert-Closed-Loop]]
- [[Agent-Observability]]
