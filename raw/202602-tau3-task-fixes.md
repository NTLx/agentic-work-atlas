---
type: raw
title: "τ³-Bench: Fixing Airline + Retail"
source: "https://taubench.com/blog/tau3-task-fixes.html"
author:
  - "Victor Barres"
  - "Ben Shi"
created: "2026-09-20"
description: "τ³ 官方 task audit：airline 27 个、retail 26 个任务修复错误 expected actions、歧义、不可行约束、missing fallback 和 policy loopholes；修复后 airline pass^1 按模型提高 14–20pp，GPT-5.2 high 的 pass^4 从 50% 到 72%。"
tags:
  - clippings
  - verification
  - agent-evaluation
---

# τ³-Bench: Fixing Airline + Retail

> Canonical source: https://taubench.com/blog/tau3-task-fixes.html
> Published by τ-bench, February 2026.

## Source locator

- Official audit reports 27 airline tasks fixed and 26 retail tasks fixed.
- Fix categories include incorrect expected actions, ambiguous user instructions, impossible/contradictory constraints, missing fallback behaviors, policy-loophole prevention, plus data/tool fixes in the detailed list.
- Examples include removing compensation/cancellation actions that contradicted policy, fixing unsupported refund methods, resolving impossible payment constraints and clarifying ambiguous exchange requests.
- After fixes:
  - airline pass^1 increased by 14.0–20.0 percentage points depending on model;
  - retail pass^1 changes ranged from -0.4 to +5.5 points;
  - GPT-5.2 high airline pass^4 rose from 50.0% to 72.0%.
- Updated tasks are reported as live on the leaderboard and trajectories available in the visualizer.

## Evidence boundary

This is a multi-change benchmark repair: task text, expected actions, constraints, fallback behavior and loopholes can all change model/user behavior as well as scoring. Therefore before/after score changes are not a fixed-trace reference-only causal experiment. Policy, task definition and evaluator remain in the same benchmark-maintainer ecosystem.
