---
type: source-summary
title: "HarnessEvolve: Learning from Reference Trajectories for Reliable Agent Self-Evolution"
source_raw:
  - "[[20260901-harnessevolve-reference-trajectories]]"
canonical_url: "https://arxiv.org/abs/2609.00829"
raw_state: full
source_locator:
  - "execution/evaluation/optimization/gating four-module architecture"
  - "reference-trajectory diagnosis plus leakage/bloat quality gate"
  - "recent-batch performance gate plus held-out validation snapshot selection"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - verification
  - agent-evaluation
evidence_level: high
claim_type: mixed
---

# HarnessEvolve: Learning from Reference Trajectories for Reliable Agent Self-Evolution

## 编译摘要

### 1. 浓缩

- **核心结论 1：自演化首先需要把“执行、评估、修改、接受修改”拆成可归因对象。**
  - 关键证据：HarnessEvolve 用 execution / evaluation / optimization / gating 四模块处理完整 harness，而不是让一个循环既改自己又给自己打分。
- **核心结论 2：terminal score 不足以进行可靠 credit assignment。**
  - 关键证据：系统用已知 ground-truth answer 生成 reference trajectory，再核验其路径合法性，并定位 failed trajectory 的 first divergence。
- **核心结论 3：性能晋级至少需要防 shortcut 与防 forgetting 两类 gate。**
  - 关键证据：quality gate 检查 data leakage / prompt bloat；performance gate 要求当前 batch 提升且近期 batch 不明显退化；epoch 结束再从 snapshot pool 用 validation set 选择版本。

### 2. 质疑

- reference trajectory 来自同一个 execution agent 在已知答案条件下运行，即便另有 evaluation agent 核验，也不能自动视为外部独立真值。
- gate 的“结构解耦”不等于 gate 具有不可修改的独立安全权限。
- validation snapshot selection 是实验内版本选择，不等于 production canary / rollback。

### 3. 对标

- 对 EX-007：补齐 **change surface → diagnosis → candidate → quality gate → regression gate → snapshot selection** 链。
- 对 [[Verifiable-Agent-Engineering]]：验证对象从单次 Agent 行为扩展到“Agent 自己产生的下一版行为系统”。
- 对 [[Recursive-Self-Improvement]]：这是 harness-layer self-improvement，而不是模型权重层 RSI。

## 关联概念

- [[Recursive-Self-Improvement]]
- [[Meta-Harness-Optimization]]
- [[Agent-Harness]]
- [[Verifiable-Agent-Engineering]]
