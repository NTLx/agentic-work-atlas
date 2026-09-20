---
type: raw
title: "SkillTV-Bench: Benchmarking How Well Judges Perform on Skill-Augmented Agentic Execution"
source: "https://arxiv.org/abs/2608.05573"
author:
  - "Zhi Han"
  - "Chenxi Zeng"
  - "Liuhaichen Yang"
  - "Zihan Guo"
  - "Ming Zhou"
  - "Yang Li"
published: "2026-08-06"
created: "2026-09-19"
description: "681 条真实 agent trajectories / 50 tasks / 11 domains；把 task-time skills、可检查 artifacts、环境与 verifier-side hidden labels 组合到同一 judge benchmark。"
tags:
  - clippings
  - verification
  - agent-evaluation
---

# SkillTV-Bench: Benchmarking How Well Judges Perform on Skill-Augmented Agentic Execution

> Canonical source: https://arxiv.org/abs/2608.05573
> Code/data: https://github.com/HanZhi306/SkillTV-Bench

## Source locator

- 681 real agent trajectories from 50 source tasks across 11 domains.
- Evaluation split: 203 cases from 14 source tasks; evolution split: 478 cases from 36 source tasks; source-task disjoint.
- Each case packages instruction, normalized trajectory, 1–6 task-time skills, final artifacts, an inspectable environment, and a verifier-side hidden source label.
- JudgeSkill directs an agent judge to build an inspection plan, perform artifact/process checks, record an inspection log, and issue an evidence-grounded PASS/FAIL verdict.
- Refined JudgeSkill improves the same agent judge from 43.8% to 58.6% accuracy (+14.8 pp); balanced accuracy 56.8% to 63.4%.
- In offline rollout-pool selection, selected-trajectory success rises from 33.9% to 45.5% at 10 rollouts with the refined JudgeSkill.

## Evidence boundary

The benchmark shows that task-time procedural knowledge can improve where and how a judge inspects evidence. It does not isolate whether gains come from knowledge content, inspection ordering, additional effective compute, or benchmark-specific verifier alignment, and it does not establish the same gains outside the released task families.
