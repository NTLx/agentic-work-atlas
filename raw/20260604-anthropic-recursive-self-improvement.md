---
type: raw
source: "https://www.anthropic.com/institute/recursive-self-improvement"
author:
  - "Marina Favaro"
  - "Jack Clark"
published: "2026-06-04"
created: "2026-06-05"
tags:
  - clippings
  - recursive-self-improvement
  - agentic-engineering
  - ai-development
---

# When AI builds itself

**Authors**: Marina Favaro, Jack Clark (editorial support from Santi Ruiz)
**Publisher**: Anthropic Institute
**Date**: June 4, 2026

---

The article examines Anthropic's progress toward recursive self-improvement—where AI systems autonomously design and develop their own successors. The authors argue this capability "could come sooner than most institutions are prepared for" and present internal and external evidence that AI is already accelerating AI development.

## Historical Timeline at Anthropic

The piece traces five phases:

1. **2021–2023**: Building the first Claude, with humans writing code on laptops
2. **2023–2025**: Chatbots assisting with short code snippets
3. **2025–2026**: Coding agents writing and editing entire files independently
4. **Today**: Autonomous agents running code and delegating work to other agents
5. **Future**: Agents potentially building and training models themselves

## External Evidence

Task completion horizons for AI models have been "doubling roughly every four months."

| Model | Date | Task Horizon |
|-------|------|-------------|
| Claude Opus 3 | March 2024 | 4-minute tasks |
| Claude Sonnet 3.7 | ~March 2025 | 90-minute tasks |
| Claude Opus 4.6 | ~March 2026 | 12-hour tasks |

Benchmarks like SWE-bench and CORE-Bench went from low single-digit scores to saturation in roughly two years and fifteen months, respectively.

## Internal Evidence from Anthropic

### Code production

As of May 2026, "more than 80% of the code we merge into Anthropic's codebase was authored by Claude." Engineers were "merging 8x as much code per day as they were in 2024."

### Code quality

"Claude-written code was still worse in quality than human-written code at Anthropic in late 2025, and is roughly at parity today." Success rates on open-ended tasks reached 76% by May 2026.

### Experiment execution

On optimization tasks:

| Model | Date | Speedup |
|-------|------|---------|
| Claude Opus 4 | May 2025 | ~3x |
| Claude Mythos Preview | April 2026 | ~52x |

A skilled human would need four to eight hours to reach 4x.

### Research judgment

| Model | Date | Beat human choices |
|-------|------|-------------------|
| Opus 4.5 | November 2025 | 51% |
| Mythos Preview | April 2026 | 64% |

### Productivity perception

A March 2026 poll of 130 employees found "the median respondent estimated that they produced around 4x as much output with Mythos Preview."

## The Narrowing Human Role

The authors argue "the human role is narrowing at each step in the AI development process." Human comparative advantage currently lies in "research taste and judgment, including choosing which problems matter."

## Three Possible Futures

### 1. Trend stalls

Exponential trajectories may be S-curves; compute or energy constraints could bind. Even frozen capabilities would produce major changes.

### 2. Compounding efficiency gains

AI development becomes substantially automated while humans set directions. "100-person companies could do the work of 10,000- or 100,000-person organizations."

### 3. Full recursive self-improvement

AI systems design their own successors; pace determined by compute availability. The authors note uncertainty about alignment: "the rare occurrences of misalignment present in today's models could compound as the models build their successors."

## Recommendations

The authors advocate building verification systems enabling credible slowdowns or pauses: "we expect that we would slow down or temporarily pause, if other developers at or near the frontier also did so in a verifiable manner." They acknowledge the coordination challenge, noting that "training runs are far easier to conceal than missile silos."

## Key Data Points Summary

| Metric | Value | Date |
|--------|-------|------|
| AI-authored code at Anthropic | >80% | May 2026 |
| Engineer productivity multiplier | 8x vs 2024 | May 2026 |
| Code quality parity | Reached | Late 2025 → mid 2026 |
| Task completion horizon doubling | ~4 months | Ongoing |
| Open-ended task success rate | 76% | May 2026 |
| Optimization speedup (Mythos) | 52x | April 2026 |
| Research judgment beat rate | 64% | April 2026 |
| Employee perceived productivity | 4x | March 2026 |

**Visual credits**: Shan Carter, Romello Goodman, and Nikki Makagiansar. Data collection by Brian Calvert and Jun Shern Chan.
