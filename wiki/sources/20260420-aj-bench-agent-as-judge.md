---
type: source-summary
title: "AJ-Bench: Benchmarking Agent-as-a-Judge for Environment-Aware Evaluation"
source_raw:
  - "[[20260420-aj-bench-agent-as-judge]]"
canonical_url: "https://arxiv.org/abs/2604.18240"
raw_state: full
source_locator:
  - "benchmark overview: 155 tasks / 516 trajectories across Search, DS, GUI"
  - "three capabilities: information acquisition, state verification, process verification"
  - "official repository aggregate comparison with LLM-as-a-Judge"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - verification
  - agent-evaluation
evidence_level: high
claim_type: mixed
---

# AJ-Bench: Benchmarking Agent-as-a-Judge for Environment-Aware Evaluation

## 编译摘要

### 1. 浓缩

- **核心结论 1：验证复杂 Agent 行为时，judge 需要获取环境证据，而不只是阅读最终回答或静态 transcript。**
  - 关键证据：AJ-Bench 把评测拆成 information acquisition、state verification、process verification，并覆盖 Search、Data Systems、GUI 三个环境域。
- **核心结论 2：可交互 Agent-as-a-Judge 在该 benchmark 上优于静态 LLM-as-a-Judge，但仍存在明显开放问题。**
  - 关键证据：155 tasks、516 trajectories；官方仓库报告总体 F1 最多提升 13.41 个百分点。
- **核心结论 3：证据“可见”与证据“被主动检查”是两个不同能力。**
  - 关键证据：judge 必须使用工具检查文件/数据库/GUI 状态及关键过程，而不是只消费已有文本。

### 2. 质疑

- benchmark 的 ground-truth annotation 自身仍是 reference；AJ-Bench 没有同时研究 reference 被污染或错误时 judge 会怎样。
- Agent-as-a-Judge 的提升同时包含更多工具、更多环境访问和不同推理流程，不能把效果全部归因于“证据覆盖”单一变量。
- 结果是在特定任务构造与 judge 配置上得到，不等价于生产系统中可观察性的完整闭包。

### 3. 对标

- 对 EX-002：直接支持把 **physical visibility / active inspection / evidence interpretation** 拆开。
- 对 EX-001：它不能替代 verifier independence；一个证据访问更强但与 generator 高度相关的 judge 仍可能共错。
- 对 EX-004：AJ-Bench 的 ground truth 主要承担 reference 角色，尚未把 reference truth、environment truth、execution truth 三层同时交叉。

## 关联概念

- [[Verifiable-Agent-Engineering]]
- [[LLM-as-a-Judge]]
- [[Agent-Observability]]
- [[Agent-Verification]]
