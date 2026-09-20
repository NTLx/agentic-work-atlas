---
type: raw
title: "REDAgentBench: Executable Red Teaming and Faithful Measurement of LLM Agent Systems"
source: "https://arxiv.org/abs/2608.10669"
author:
  - "Zixing Chen"
  - "Xingyuan Liu"
  - "Jie Zhu"
  - "Huaixia Dou"
  - "Shuo Jiang"
  - "Junhui Li"
  - "Lifan Guo"
  - "Feng Chen"
  - "Chi Zhang"
published: "2026-08-11"
created: "2026-09-19"
description: "1,661-case executable red-team benchmark；从 service receipt 与 final-state change 验证实际副作用，并区分 exposure/execution/observation/adjudication。"
tags:
  - clippings
  - verification
  - agent-safety
---

# REDAgentBench: Executable Red Teaming and Faithful Measurement of LLM Agent Systems

> Canonical source: https://arxiv.org/abs/2608.10669

## Source locator

- 1,661 cases across five service surfaces.
- Evaluation spans six models and three agent harnesses.
- Macro-average attack success rate reported as 65.69%.
- Harmful effects are verified from service receipts and final-state changes rather than transcript narration alone.
- In the state-grounded diagnostic cohort, almost one in five confirmed violations with resolved action anchors occurs after the agent states the relevant constraint or risk.
- A training-free policy reminder reduces confirmed violations by more than 70 percentage points in matched replay.

## Evidence boundary

This is a benchmark/preprint built by the same team that designed the cases and measurement framework. Its executable state-grounding is directly relevant to success provenance, but attack prevalence and intervention effect should not be generalized outside the benchmark without replication.
