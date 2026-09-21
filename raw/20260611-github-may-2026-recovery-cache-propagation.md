---
type: raw
title: "GitHub availability report: May 2026 — account recovery and cache propagation"
source: "https://github.blog/news-insights/company-news/github-availability-report-may-2026/"
author:
  - "Jakub Oleksy"
published: "2026-06-11"
created: "2026-09-20"
description: "GitHub May 2026 availability report 中 5 月 26 日事故：服务账号误暂停后，账号恢复、豁免、缓存刷新和完全恢复分阶段发生，提供非 Agent 但真实生产环境的 recovery verification 时间线。"
tags:
  - clippings
  - agent-security
  - incident-response
---

# GitHub availability report: May 2026 — account recovery and cache propagation

> Canonical source: https://github.blog/news-insights/company-news/github-availability-report-may-2026/

## Source locator

- May 26 incident window: 10:40–12:56 UTC; GitHub Actions jobs were degraded and dependent services were also affected.
- Root cause: an automated account-review system incorrectly suspended the service account used by GitHub Actions.
- Recovery steps were staged: account restored at 12:16 UTC; exemption added at 12:20; related service redeployed at 12:48 to flush cached account state; full recovery confirmed at 12:56.
- A small number of issues, pull requests, comments and discussions were hidden while the service account was disabled; GitHub reported no data loss and restored affected content/search state.
- Follow-up included allowlisting protected service accounts and reducing cache propagation delay.

## Evidence boundary

This is a production reliability incident, not an autonomous-Agent security experiment. It is valuable as a counterexample to atomic recovery: restoring authority, preventing recurrence, refreshing dependent caches and confirming service/business state occurred at different times. It does not provide an Agent action-surface denominator, revoke-after-send trace or rollback-success rate.
