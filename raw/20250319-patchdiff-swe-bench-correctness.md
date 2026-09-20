---
type: raw
title: "Are Solved Issues in SWE-bench Really Solved Correctly? An Empirical Study"
source: "https://arxiv.org/abs/2503.15223"
author:
  - "You Wang"
  - "Michael Pradel"
  - "Zhongxin Liu"
published: "2025-03-19"
created: "2026-09-20"
description: "ICSE 2026 PatchDiff study：SWE-bench Verified 上 plausible patches 中，7.8% 被基准计为正确却未通过开发者完整测试；29.6% 与 developer patch 存在行为差异，其中人工复核 28.6% 确认错误，最终使报告 resolution rate 高估 6.2 个百分点。"
tags:
  - clippings
  - verification
  - agent-evaluation
---

# Are Solved Issues in SWE-bench Really Solved Correctly?

> Canonical source: https://arxiv.org/abs/2503.15223
> ICSE 2026 Research Track.

## Source locator

- Authors: You Wang, Michael Pradel, Zhongxin Liu.
- Evaluates plausible patches produced by CodeStory, LearnByInteract and OpenHands on SWE-bench Verified.
- Introduces PatchDiff, a repository-level differential patch testing method that compares generated patches against human-written developer patches by probing behavioral differences.
- Reported findings:
  - 7.8% of all evaluated patches were counted as correct by the benchmark while failing the developer-written test suite;
  - 29.6% of plausible patches induced behavior different from the developer patch;
  - among behaviorally divergent patches, 46.8% reflected similar but divergent implementations;
  - 27.3% changed more behavior than the developer patch;
  - manual inspection judged 28.6% of behaviorally divergent patches as certainly incorrect;
  - combined weaknesses inflated reported resolution rates by 6.2 absolute percentage points.
- The replication package is publicly available in the PatchDiff repository.

## Evidence boundary

Passing the benchmark tests is not the same as behavioral equivalence. However, behavioral divergence from the developer patch is also not automatically incorrect, because the developer patch is not necessarily the unique valid implementation. PatchDiff is therefore best treated as a discrepancy detector followed by semantic/manual adjudication, not as a perfect oracle. The reported percentages apply to the studied tools and SWE-bench Verified version, not all coding agents or software tasks.
