---
type: raw
title: "Separating signal from noise in coding evaluations"
source: "https://openai.com/index/separating-signal-from-noise-coding-evaluations/"
author:
  - "OpenAI"
published: "2026-07-08"
created: "2026-09-20"
description: "OpenAI 对 SWE-Bench Pro 的官方审计：731 题中自动管线筛出 286 个可疑任务，agent 深查判 200 题、五名工程师复核判 249 题存在 breaking issues；公开百分比分母是全部 731 题，且未筛中任务并未同样人工复核。"
tags:
  - clippings
  - verification
  - agent-evaluation
---

# Separating signal from noise in coding evaluations

> Canonical source: https://openai.com/index/separating-signal-from-noise-coding-evaluations/
> Published: 2026-07-08.

## Source locator

- Benchmark size in the reported audit: 731 SWE-Bench Pro tasks.
- Initial automated pipeline flagged 286 potentially broken/problematic tasks.
- Deeper audit used human-supervised investigator agents with repository/environment access and a human annotation campaign with experienced software engineers.
- Each flagged task in the human campaign was reviewed by five engineers.
- Reviewers first formed judgments from the visible problem statement, tests and gold patch, then used pipeline analysis/transcripts as supporting context.
- Reported findings:
  - agent-assisted audit identified 200 tasks with breaking issues;
  - human campaign identified 249;
  - the post reports these as 27.4% and 34.1% of all 731 tasks.
- Main failure classes:
  - overly strict tests;
  - underspecified prompts;
  - low-coverage tests;
  - misleading prompts.
- Human reviewers selected low-coverage tests more often than the agent pipeline, 9.4% versus 4.1%.

## Evidence boundary

The 286 flagged tasks were selected by an automated screen; the remaining tasks were not subjected to the same deep human review. Therefore 27.4%/34.1% are reported benchmark-level fractions derived from findings in a selected audit path, not an unbiased random-sample prevalence estimate. Labels can overlap and should not be added. Gold patch remains part of the review evidence and is not itself an unquestioned oracle.
