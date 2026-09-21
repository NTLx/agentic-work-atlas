---
type: raw
title: "Omission Constraints Decay While Commission Constraints Persist in Long-Context LLM Agents"
source: "https://arxiv.org/abs/2604.20911"
author:
  - "Yeran Gamage"
published: "2026-04-22"
created: "2026-09-20"
description: "Security-Recall Divergence：4,416-trial、12-model、8-provider 的长上下文实验中，禁止型 omission constraints 会随上下文压力衰减，而要求型 commission constraints 可保持正常；但测试约束是可字符串匹配的格式代理。"
tags:
  - clippings
  - agent-security
  - verification
---

# Omission Constraints Decay While Commission Constraints Persist in Long-Context LLM Agents

> Canonical source: https://arxiv.org/abs/2604.20911
> Accessed: 2026-09-20.

## Source locator

- Three-arm study: 4,416 trials, 12 models, 8 providers, six conversation depths.
- Eight behavioral constraints are delivered through a policy file: three commission rules and five omission rules; all eight are formatting constraints with deterministic string/regex grading.
- Mistral Large 3 example: omission compliance falls from 73% at turn 5 to 33% at turn 16 while commission compliance remains 100%.
- Token-matched padding Arm C was run on Gemini 2.5 Flash and Llama 3.3 70B; schema semantic content accounts for 62–100% of the measured dilution effect in those two models.
- Safe Turn Depth and periodic constraint re-injection are proposed as operational mitigations; re-injection before the per-model threshold restores measured compliance without retraining.

## Evidence boundary

The experiment uses a fully synthetic DevOps sandbox and formatting/style constraints selected for deterministic measurement. The paper explicitly states that whether semantically meaningful security constraints, such as credential or data-exfiltration prohibitions, decay at the same rates remains untested. Arm C covers only two models and therefore does not causally isolate the semantic-dilution mechanism for the full SRD-susceptible model cluster.
