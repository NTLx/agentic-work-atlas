---
type: raw
source: "https://www.lmsys.org/blog/2026-07-02-agent-assisted-sglang-development"
author:
  - "SGLang Team"
published: "2026-07-02"
created: "2026-07-03"
tags:
  - clippings
  - agentic-engineering
  - skill-engineering
  - perf-optimization
---

# Agent-Assisted SGLang Development: An Initial Exploration

SGLang Team, July 2, 2026

SGLang development increasingly goes beyond isolated code changes. The same repository now spans LLM serving, distributed runtime, GPU kernels, diffusion pipelines, model-specific execution paths, and production incident handling. In the past, many of these workflows depended on individual developer memory: how to launch a certain model, how to read a profile trace, which log to add first when debugging a CUDA crash, or which benchmarks a performance PR should include. As agent tools mature, this experience can be turned into executable `SKILL.md` files, scripts, benchmark contracts, and review loops.

Around SGLang agent development, a set of skills has already emerged for both LLM and diffusion work:

- SGLang `.claude/skills` is maintained inside the SGLang repository and captures repo-level development workflows such as CUDA crash debugging, kernel integration, tests, CI, profiling, production triage, and source-tree conventions.
- SGLang diffusion `.claude/skills` focuses on diffusion-specific workflows, including adding new diffusion models, benchmarking and profiling denoise paths, tuning performance options, and validating quantized pipelines.
- BBuf/AI-Infra-Auto-Driven-SKILLS covers cross-framework serving benchmarks, capacity planning, profile and pipeline analysis, model compute simulation, SGLang human-style review, production incident triage, SOTA loops for SGLang and other open-source inference frameworks, and model PR history.
- kernel-design-agents is the KDA project and the winning solution for the MLSys 2026 FlashInfer Kernel Contest.
- BBuf/KDA-Pilot applies KDA-style agent kernel workflows to SGLang. Its public B200 diffusion summary now tracks 10 SGLang kernel tasks.

Viewed together, these efforts point to the same direction: the value of agents comes from procedural engineering knowledge, including executable steps, reproducible experiments, and reviewable evidence.

## TL;DR

- Agents are most useful in SGLang when they can keep moving along a well-defined workflow. Benchmarking, profiling, kernel API logging, adding diffusion pipelines, production incident replay, and SOTA loops can all be encoded as skills.
- An SGLang skill is an executable development procedure. In `debug-cuda-crash`, `sglang-diffusion-benchmark-profile`, and `llm-torch-profiler-analysis`, the important content is preflight checks, hard failure gates, artifact contracts, reproduction commands, and result formats.
- Profile evidence is central to performance work. The SGLang profiler skills produce fixed kernel tables, overlap-opportunity tables, and fuse-pattern tables. KDA-Pilot extends this into same-ABI baseline/candidate comparison, real workloads, correctness gates, NCU evidence, and per-shape results.
- Long-running optimization has started to move into Loop Engineering. The SGLang SOTA Performance Loop decomposes "chasing SOTA" into fair benchmarking, gap decision, profiling, patching, and revalidation. Humanize/RLCR adds external review, while Codex Goal can run the same loop with lower coordination overhead.
- Review becomes more important. Agents can run more experiments, but they also generate more changes that look plausible and still need careful review.

## Why SGLang Is a Good Fit for Agent-Assisted Development

SGLang is a high-performance serving framework for LLMs and multimodal models. Several recurring problems show up in development:

- LLM paths are complex. A single performance issue may cross the Python runtime, scheduler, CUDA graph, Triton/CUDA kernels, FlashInfer/FlashAttention, distributed collectives, and model-specific wrappers.
- Diffusion paths are also complex. A slower denoise pass may involve pipeline/stage partitioning, DiT blocks, attention backends, `torch.compile` graph breaks, CFG/SP parallelism, VAE, or custom fused kernels.
- Validation is expensive. Many changes must be tested on real models and real workloads on H100, H200, B200, or RTX 5090.
- Profiles are hard to reuse manually. A single trace may contain hundreds of kernel launches. Reading Perfetto by hand can miss kernel-to-Python-source mappings.
- Performance conclusions depend heavily on context. GPU type, shape, batch size, parallelism, precision, backend, and compile state can all change the result.

The agent discussed here is therefore an executor constrained by engineering workflows. Repeated SGLang development procedures can be captured as skills, letting the agent handle repetitive execution, evidence collection, and state tracking. Developers remain responsible for defining goals, judging evidence, and reviewing whether a change belongs in the real serving path.

## From Prompt Engineering to SKILL: Protocols and Examples

A useful skill should answer: When to use, How to start, How to validate, How to decide, How to deliver.

### Current Skill Stack

| Layer | Representative skill | Problem it solves |
|-------|---------------------|-------------------|
| CUDA crash | `debug-cuda-crash` | Records inputs, exceptions, and dumps around custom op/kernel API boundaries |
| LLM benchmark | `llm-serving-auto-benchmark` | Runs fair, bounded, resumable serving benchmark search |
| Capacity planning | `llm-serving-capacity-planner` | Parses startup logs to explain weight memory, KV cache budget, CUDA graph overhead |
| Trace triage | `llm-torch-profiler-analysis` | Produces fixed kernel, overlap-opportunity, and fuse-pattern tables |
| Pipeline/layer analysis | `llm-pipeline-analysis` | Slices torch profiler traces into forward passes, layers, and kernel flows |
| Model compute simulation | `model-compute-simulation` | Builds operator-level compute templates, estimates FLOPs, MFU |
| Diffusion benchmark/profile | `sglang-diffusion-benchmark-profile` | Captures denoise latency, perf dumps, and torch profiler traces |
| Add diffusion model | `sglang-diffusion-add-model` | Adds new diffusion model into SGLang pipeline structure |
| Diffusion performance tuning | `sglang-diffusion-performance` | Chooses performance settings: torch.compile, warmup, SP/CFG parallelism |
| Production triage | `sglang-prod-incident-triage` | Collects live-server bundles, saves failing requests, replays them |
| SGLang review / PR history | `sglang-humanize-review` | Reviews patches against real maintainer discussion patterns |
| SOTA Performance Loop | `sglang-sota-humanize-loop` | Fair benchmarking → gap decision → profiling → patching → revalidation loop |

### Recent Optimization Examples

| Case | Result | Key point |
|------|--------|-----------|
| Router long-context tokenization dedup (#28744) | TTFT dropped 29%-49% | Agent handled cache-aware routing, chat-encoder parity together |
| Qwen3-Next FlashInfer allreduce fusion (#22664) | Throughput +71.4%, TTFT dropped from 456ms to 168ms | Profile-driven collective optimization with accuracy checks |
| Cohere2Moe NVFP4 fused-MoE (#27401) | +26% chat, +21% summarization | Completed routing semantics for existing kernel |
| Kimi Delta Attention CuteDSL prefill on SM100 (#27488) | 1.08x-1.52x faster than Triton | Kernel task covered gate distribution, numerical overflow, real-model accuracy |
| Spectral Progressive Diffusion (#27524) | 1.63x-2.32x denoising speedup | System optimization: early denoise at lower latent resolution |
| LTX-2 VAE decode channels-last-3d (#27431) | 1.41x decode speedup, saved 9.7 GiB memory | Profile pointed to Conv3d and layout conversion |

## Profiling, Review, and Loop Engineering

Two profiler skills are used together. `llm-torch-profiler-analysis` produces kernel tables, overlap-opportunity tables, and fuse-pattern tables. `llm-pipeline-analysis` grounds the problem in steady-state forward passes, representative layers, and concrete kernel flows.

### Humanize/RLCR: Adding External Review

Humanize splits long-running tasks into two stages:
1. Run gen-plan first → structured `plan.md` with goal, acceptance criteria, milestones
2. Run RLCR loop → Claude Code implements, commits, writes summary; Codex Review checks evidence, state, and risk

### SGLang SOTA Performance Loop

Full loop stages:
1. Define target boundary (model, hardware, precision, workload)
2. Run fair search for SGLang and competing frameworks
3. Decide the gap
4. Use profiles to explain the gap (do not rush into code changes)
5. Patch only evidence-supported paths
6. Revalidate on the same workload

### Codex Goal: Lower-Cost Loop

Single Codex Goal carries execution, self-checking, and revalidation without two-role setup. Same benchmark/profile/accuracy requirements, less orchestration overhead.

## KDA-Based CUDA Kernel Optimization

KDA-Pilot separates kernel optimization into isolated tasks:
- Workloads from real SGLang diffusion models
- Baseline copied from upstream with source lineage
- Same ABI and build/export path for baseline and candidate
- Fixed production rows, A/B interleaving, CUDA event timing
- Correctness: production rows, regression grid, NaN/Inf checks, poison output checks

As of June 27, 2026, three KDA-Pilot-derived optimizations landed upstream:
- #27392: Qwen-Image norm-scale-shift, 1.279x kernel improvement
- #29281: Cosmos3 Conv3D cat/pad, 2.03x kernel improvement
- #29361: LTX-2.3 residual-gate, 1.108x-1.130x improvement

## Practice Rules

1. Define task boundary before starting agent
2. Fix benchmark before reading profiles
3. Interpret NCU results according to kernel compute characteristics
4. Check backend and fallback gates before trusting a profile
5. Kernel optimization must use same ABI, wrapper, and compile flags
6. Review matters more than before — agents create more plausible mistakes

Agent-era SGLang development will not remove developers from the system. The more realistic change is to write developer experience into workflows, hand repetitive execution to agents, and leave judgment, design, and review to people.
