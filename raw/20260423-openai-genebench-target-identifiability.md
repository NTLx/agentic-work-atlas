---
type: raw
title: "GeneBench: Assessing AI Agents for Multi-Stage Inference Problems in Genomics and Quantitative Biology"
source: "https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf"
author:
  - "Jeremy Li"
  - "Andrew Ho"
published: "2026-04-23"
created: "2026-09-20"
description: "OpenAI GeneBench：103 个多阶段基因组/定量生物学任务；graded target 选择为 agent-visible data 可恢复的 realized-data quantity，并进行 scientific/methodological/target-identifiability review、trace/leakage/shortcut/prompt-grader mismatch audit。"
tags:
  - clippings
  - verification
  - agent-evaluation
---

# GeneBench

> Canonical source: https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf
> Report date: 2026-04-23.
> Accessed report: 31 pages.

## Source locator

- GeneBench contains 103 evaluations across 10 domains.
- Problems start from realistic staged data and require multi-step iterative analysis.
- The graded endpoint is designed around a target that can be recovered from agent-visible data rather than an unrecoverable hidden data-generating parameter.
- Construction constraints include target identifiability, robustness to reasonable analysis variants, distinguishability of plausible-but-wrong paths, scientific/methodological review, independent target-identifiability review, model trial runs and trace audit, leakage and shortcut checks, and prompt-grader mismatch checks.
- Grading uses a verifiable answer with tolerance rather than requiring one exact implementation path.
- Reported benchmark-wide results use 103 tasks and aggregate unweighted per-problem pass rates.
- Example problems explicitly distinguish acceptable analysis variants from ablations that omit necessary correction or use the wrong phenotype/estimand.

## Evidence boundary

GeneBench is a constructed scientific benchmark. Its design shows how to make a target recoverable and auditable, but does not prove real scientific questions always admit a single defensible answer. Independent review during benchmark construction is not the same as an external oracle adjudicating every model run. It does not experimentally randomize reference quality or success provenance.
