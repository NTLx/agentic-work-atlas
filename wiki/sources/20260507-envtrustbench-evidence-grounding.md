---
type: source-summary
title: "EnvTrustBench: Evaluating LLM Agents' Evidence-Grounding Robustness"
source_raw:
  - "[[20260507-envtrustbench-evidence-grounding]]"
canonical_url: "https://github.com/EnvTrustBench/EnvTrustBench"
raw_state: full
source_locator:
  - "public paper-basics: W0 / E0 / q / Omega framework and five evidence-grounding patterns"
  - "final aggregate matrix: 55 cases / 14 model-scaffold stacks / 3,850 accepted runs"
  - "release boundary: manuscript PDF and raw traces withheld"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - verification
  - agent-evaluation
evidence_level: medium
claim_type: mixed
---

# EnvTrustBench: Evaluating LLM Agents' Evidence-Grounding Robustness

## 编译摘要

### 1. 浓缩

- **核心结论 1：环境“给出的证据”与环境“真实状态”必须分开建模。**
  - 关键证据：EnvTrustBench 显式区分 W0、E0、任务 q 与 validation oracle Omega，并为每个 case 定义 true state、correct path、false path 和 verification opportunity。
- **核心结论 2：Agent 会把日志、文档、API 输出、记忆或可执行 artifact 当成事实权威；这种错误跨多种入口发生。**
  - 关键证据：公开框架覆盖五种 evidence-grounding pattern，而不是只测 prompt injection。
- **核心结论 3：model 与 scaffold 必须作为组合系统评估。**
  - 关键证据：公开 final matrix 中不同 model-scaffold stack 的 FPCR 差异很大；作者据此强调不能只把失效归因于模型。

### 2. 质疑

- 当前公开稿没有 manuscript PDF 与 raw traces，独立复核能力受限，因此不能把 83.3% 当作外部世界的风险基准率。
- 55 个 machine-scoreable cases 覆盖的是作者定义的典型失败模式，不代表完整 action surface。
- oracle 本身仍由 benchmark author 定义；reference correctness 与 environment truth 没有被完全独立操纵。

### 3. 对标

- 对 EX-004：把 **environment truth** 从 reference truth 和 transcript truth 中单独拆出。
- 对 EX-002：即使 evidence physically visible，agent 仍可能把非权威 observation 错当成权威事实，因此 coverage 之外还有 authority/interpretation 门。
- 对 [[Agent-Observability]]：记录 observation 不等于知道 canonical post-state；observability 必须包含权威状态来源。

## 关联概念

- [[Verifiable-Agent-Engineering]]
- [[Agent-Observability]]
- [[Agent-Verification]]
- [[Context-Collapse]]
