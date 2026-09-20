---
type: raw
title: "AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling"
source: "https://arxiv.org/abs/2608.26623"
author:
  - "Abhigya Verma"
  - "Amit Kumar Saha"
  - "Seganrasan Subramanian"
  - "Sai Harshitha Aluru"
published: "2026-08-27"
created: "2026-09-19"
description: "3,808 instances / 6 DAG topologies / 3 difficulty tiers；同一 judge 在 with-ground-truth 与 without-ground-truth 条件下成对比较。"
tags:
  - clippings
  - verification
  - agent-evaluation
---

# AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling

> Canonical source: https://arxiv.org/abs/2608.26623
> Dataset: https://huggingface.co/datasets/ServiceNow-AI/AgentJudgeBench

## Source locator

- 3,808 benchmark instances spanning six workflow-DAG topologies and three difficulty tiers.
- Five generators and six judges, from 20B scale to frontier models.
- Paired conditions with and without ground-truth exposure.
- Judge alignment degrades monotonically with task difficulty and 1.5× faster without ground truth.
- On hard no-ground-truth queries, all six judges cluster around 77–82% alignment.
- Ground-truth exposure reduces alignment for GPT-5.4 by 1.5 pp and Gemini-2.5-Pro by 3.9 pp in the reported setup.
- Structured rubrics improve alignment by up to 6.5 pp, while chain-of-thought and temperature changes have negligible reported effect.

## Evidence boundary

Ground-truth exposure is a strong paired manipulation, but the benchmark still depends on a programmatic reference and the reported human validation uses a different yardstick. The paper demonstrates that reference availability can help, fail to help, or over-anchor a judge; it does not prove that withholding reference is generally safer.
