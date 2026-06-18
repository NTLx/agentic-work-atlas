---
type: raw
source: "https://openai.com/index/introducing-life-sci-bench/"
author:
  - "OpenAI"
published: "2026-06-17"
created: "2026-06-18"
tags:
  - clippings
  - benchmark
  - life-science
  - evaluation
  - frontier-model
---

# Introducing LifeSciBench

OpenAI released LifeSciBench, a 750-task benchmark grading AI models on real life-science research with expert-written rubric.

## Key facts

- 750 expert-authored tasks spanning 7 workflows and 7 biological domains
- Built by 173 PhD scientists with 19,020 rubric criteria
- Grades reasoning and decisions, not just recall
- Best model (GPT-Rosalind) passes 36.1%, leaving large headroom

## What is LifeSciBench

Most biology benchmarks ask narrow, fact-based questions with clean answers. Scientists weigh imperfect evidence and make decisions. LifeSciBench targets that gap directly.

The seven workflows cover evidence handling and analysis, design and optimization, scientific reasoning, validation and operations, translation, and scientific communication.

The seven domains run from genomics and medicinal chemistry to clinical and translational science.

Tasks are written as a scientist would brief a colleague. They are free-response, not multiple-choice. Around 79% require multiple reasoning or decision-making steps, averaging four steps each.

## How the Benchmark was Built

A cohort of 173 expert scientists wrote the tasks. Each held a Ph.D. and had biotechnology or pharmaceutical experience. Accepted tasks averaged six automated review cycles and at least two expert reviews.

Many tasks ship with artifacts. The benchmark includes 1,062 attached artifacts in total. About 53% of tasks require at least one artifact. Types include sequences, figures, tables, PDFs, and chemical structures.

A separate cohort validated quality. There were 453 reviewers, and 97% held doctorates. Overall agreement exceeded 96% on relevance, reasoning, grounding, and usefulness.

## The Rubric System

Rubrics are the core mechanic. They contain 19,020 criteria across the benchmark. That is roughly 25 criteria per task.

Each criterion rewards one concrete property. Examples include a specific fact, a reasoning step, or a numeric answer within tolerance. Grading runs against the rubric, not a single reference string.

Two metrics summarize performance. Normalized rubric score divides awarded points by total points. Task pass rate counts tasks scoring at or above 70%.

## How the Models Performed

| Model | Normalized score | Task pass rate |
|-------|-----------------|----------------|
| GPT-Rosalind | 0.576 | 36.1% |
| GPT-5.5 | 0.519 | 25.7% |
| Gemini 3.1 Pro | 0.515 | 23.6% |
| GPT-5.4 | 0.479 | 20.7% |
| Grok 4.3 | 0.399 | 13.0% |

GPT-Rosalind, OpenAI's domain-specialized model, led overall. It had the highest per-task mean on 386 of 750 tasks. Gemini 3.1 Pro uniquely led on 214 tasks.

## Where Models Win, and Where They Fall Short

Models were strongest on structured judgment. GPT-Rosalind reached a 0.712 mean score on Translation. Scientific Communication scored 0.718.

Two workflows stayed hard. Design, Optimization, and Prediction was among the toughest, with GPT-Rosalind passing 30.7%. Analysis was close behind at 30.3%.

Artifact use was a clear bottleneck. GPT-Rosalind dropped from 45.1% on text-only tasks to 28.1% on artifact tasks.

Exact outputs were hardest of all. Sequence and structure criterion success ranged from 46.9% to 18.0% across models.

Headroom remains large. No model passed 171 tasks (22.8%). And 261 tasks (34.8%) had a best-model pass rate below 20%.

## Strengths and Weaknesses

Strengths:
- Broad coverage across seven workflows and seven biological domains
- Expert-authored rubrics with 19,020 atomic, gradeable criteria
- Realistic artifacts: sequences, figures, tables, PDFs, and structures
- Independent validation by 453 expert reviewers, 97% with doctorates

Weaknesses:
- Single-turn only; real research is iterative and multi-turn
- Built by OpenAI, which also supplies most evaluated models
- Public release may be limited by safety and licensing constraints
- 750 tasks cannot cover every scientific specialty
