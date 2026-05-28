---
title: "ITBench-AA: Frontier Models Score Below 50% on the First Benchmark for Agentic Enterprise IT Tasks — by Artificial Analysis and IBM"
source: "https://huggingface.co/blog/ibm-research/itbench-aa"
author:
  - "[[Ayhan Sebin]]"
  - "[[Saurabh Jha]]"
  - "[[Rohan Arora]]"
published: 2026-05-28
created: 2026-05-28
description: "A Blog post by IBM Research on Hugging Face"
tags:
  - "clippings"
---
Artificial Analysis and IBM Software Innovation Lab are launching ITBench-AA, the first in a new series of benchmarks evaluating models on agentic enterprise IT tasks, starting with Site Reliability Engineering tasks where frontier models score below 50% ITBench-AA’s SRE tasks benchmark model performance on Kubernetes incident response, where models and agents must diagnose live systems by reading logs, tracing dependencies, and identifying root-cause entities across complex infrastructure. The underlying ITBench dataset has been developed by IBM, leveraging deep expertise in enterprise IT operations. Artificial Analysis has worked closely with IBM over the last 6 months to develop an implementation of the dataset for frontier AI evaluation, beginning with Site Reliability Engineering (SRE) and expanding to Financial Operations (FinOps) and Chief Information Security Officer (CISO) tasks over time.

[![image](https://cdn-uploads.huggingface.co/production/uploads/64e8143f6de557454220921e/VLy6B6WYEMDqxEJL9KWNQ.png)](https://cdn-uploads.huggingface.co/production/uploads/64e8143f6de557454220921e/VLy6B6WYEMDqxEJL9KWNQ.png)

## Key findings:

1. Claude Opus 4.7 (Adaptive Reasoning, Max Effort) leads at 47%, followed by GPT-5.5 (xhigh) at 46% and Qwen3.7 Max at 42%.
2. All frontier models score below 50%, making ITBench-AA SRE one of the least saturated agentic benchmarks in our suite. For context, frontier models score considerably higher on Terminal-Bench.
3. Turn counts vary nearly 3x and longer trajectories do not translate to higher accuracy. GPT-5.5 (xhigh) averages 31 turns per task at 46%, while Gemini 3.1 Pro Preview averages 83 turns at 30%. Models that over-investigate tend to surface upstream fault-injection mechanisms or co-occurring symptoms as false positives.
4. GLM-5.1 (Reasoning) leads open weights models at 40%, effectively tied with Gemini 3.5 Flash (high). DeepSeek V4 Pro (Reasoning, Max Effort) follows at 38%, with Gemma 4 31B (Reasoning) at 37%, ahead of Gemini 3.1 Pro Preview at 30%.

## ITBench-AA SRE overview:

- 59 SRE tasks in total: 40 public tasks and 19 brand new, held-out tasks
- Each task provides a Kubernetes incident snapshot containing alerts, events, traces, metrics, logs, and application topology. The model must identify the minimal set of independent root-cause Kubernetes entities responsible for the incident.
- Faults span typical SRE failure modes including infrastructure, service, application, and chaos-injected incidents, such as resource quota exhaustion, rollout failures, connection pool exhaustion, and network partitions. Methodology details:
- Agentic harness: each task is solved by the model running in our open-source Stirrup reference harness, with shell access to a sandboxed file system containing the relevant logs and snapshots. 100-turn cap per task, 3 repeats per task.
- Models and agents submit a list of root-cause entities (Kubernetes Deployments, Services, Pods, etc.) they believe caused the incident. Each submission is compared against a ground-truth set of root causes provided by IBM.
- Scoring uses average precision at full recall: if a model misses any of the ground-truth root causes, it scores 0.0 for that repeat. If it identifies all of them, it is awarded a score equal to its precision - the share of its submitted entities that are actual root causes, i.e. true positives / (true positives + false positives). The headline score is the average across 59 tasks × 3 repeats.
- The harness (Stirrup) is held constant across all evaluated models, allowing an apples-to-apples comparison between models.

## Highlights

1. Tasks require agents to investigate Kubernetes incident snapshots through shell commands and submit a structured JSON diagnosis identifying the responsible root-cause entities. In one public SRE task, the agent sees user-facing failures in the frontend path. It uses shell commands to inspect the offline snapshot: reviewing alerts shows the incident window, then traces/logs narrow the failure to frontend traffic. Topology pins down the affected services, and Kubernetes manifests reveal a network policy blocking the frontend. The successful diagnosis identifies the responsible root-cause entity: otel-demo/NetworkPolicy/frontend-block-all-ports.2. More turns do not mean better answers. Models that submit additional contributing entities beyond the true root cause get penalized: identifying the correct root cause but adding upstream mechanisms (e.g., a chaos-mesh controller) or co-occurring symptoms counts as a false positive under recall-gated precision. This is why some models with long trajectories underperform terser ones: Gemini 3.1 Pro Preview averages 83 turns and scores 30%, while Gemma 4 31B (Reasoning) averages 58 turns and scores 37%.3. Open weights models sit on the cost frontier of ITBench-AA SRE. Gemma 4 31B (Reasoning) scores 37% at $0.14 per task, outperforming Gemini 3.1 Pro Preview ($2.23 per task, 30%) on both score and cost. GLM-5.1 (Reasoning) scores 40% at $1.23 per task, matching Gemini 3.5 Flash (high) ($1.70) on score at lower cost. Claude Opus 4.7 (Adaptive Reasoning, Max Effort) leads the leaderboard at 47% but is the most expensive at $5.38 per task.### ITBench-AA is built in partnership with @IBM based on their ITBench benchmark.

- For more information see: ITBench paper on arXiv: [https://arxiv.org/abs/2502.05352](https://arxiv.org/abs/2502.05352)
- GitHub: [https://github.com/itbench-hub/ITBench](https://github.com/itbench-hub/ITBench)
- ITBench-AA leaderboard: [https://artificialanalysis.ai/evaluations/itbench-aa](https://artificialanalysis.ai/evaluations/itbench-aa)
- ITBench-AA HuggingFace repo: [https://huggingface.co/datasets/ArtificialAnalysis/ITBench-AA/tree/main/sre](https://huggingface.co/datasets/ArtificialAnalysis/ITBench-AA/tree/main/sre)