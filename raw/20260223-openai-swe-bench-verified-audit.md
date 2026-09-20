---
type: raw
title: "Why SWE-bench Verified no longer measures frontier coding capabilities"
source: "https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/"
author:
  - "OpenAI"
published: "2026-02-23"
created: "2026-09-20"
description: "OpenAI 对 SWE-bench Verified 的官方复审：对 o3 在 64 次运行中不能稳定解决的 138 题进行至少 6 名工程师独立审查，59.4% 在该审计子集中存在测试或题面实质问题；同时报告 gold patch/题面污染风险。"
tags:
  - clippings
  - verification
  - agent-evaluation
---

# Why SWE-bench Verified no longer measures frontier coding capabilities

> Canonical source: https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/
> Published: 2026-02-23.

## Source locator

- SWE-bench Verified was originally created by reviewing 1,699 SWE-bench problems with three independent expert reviews and filtering to 500 tasks.
- The 2026 audit selected 138 tasks that OpenAI o3 did not solve consistently across 64 independent runs.
- Each selected task was reviewed independently by at least six experienced software engineers; flagged issues were re-verified by an additional team.
- OpenAI reports that 59.4% of those 138 audited tasks had material issues in test design and/or problem description.
- The post separates overly narrow/strict tests, underspecified prompts and environment-dependent failures.
- It also reports contamination evidence: tested frontier models could reproduce original human gold-patch content or specific problem-statement details for some tasks.

## Evidence boundary

The 59.4% figure applies to a deliberately selected hard subset of 138 tasks, not the full 500-task benchmark. Expert review is benchmark-quality adjudication, not a per-run external oracle. The contamination conclusion is based on behavioral evidence of reproducing benchmark content; this source does not expose model training corpora directly.
