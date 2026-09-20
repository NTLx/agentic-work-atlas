---
type: source-summary
title: "Hierarchical Self-Improvement: A Framework for Task-Specific Evolvable Agent Harnesses"
source_raw:
  - "[[20260809-hsi-hierarchical-self-improvement]]"
canonical_url: "https://arxiv.org/abs/2608.08466"
raw_state: full
source_locator:
  - "task harness → evolver strategy → frozen outer anchor"
  - "scope-isolated write permissions and thinking-on/off confound control"
  - "held-out task split plus backbone-capability-bound negative result"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - verification
  - agent-evaluation
evidence_level: medium
claim_type: mixed
---

# Hierarchical Self-Improvement: A Framework for Task-Specific Evolvable Agent Harnesses

## 编译摘要

### 1. 浓缩

- **核心结论 1：自修改系统可以把“谁能改谁”编码成层级权限。**
  - 关键证据：task harness、evolver strategy 与 frozen outer anchor 属于不同可编辑作用域，越界修改被拒绝。
- **核心结论 2：冻结外层能提高变更归因，但不是外部独立监督。**
  - 关键证据：task harness 与 evolver strategy 可以演化，而执行 meta-evolution 的外层逻辑冻结；但三个作用域仍由同一个 frozen LLM 驱动。
- **核心结论 3：harness evolution 受 feedback fidelity 与 backbone capability 双重上界约束。**
  - 关键证据：多个 BALROG 任务有明显提升，但 NLE 无改善；held-out 子任务间泛化也不均匀。

### 2. 质疑

- frozen outer anchor 是实现内边界，不等于组织或安全上的独立 authority。
- thinking-on/off 能减少 task-time reasoning 混淆，但仍不能消除任务选择、reward 和 selector 的评测偏差。
- held-out split 证明的是一定程度泛化，不是线上安全晋级。

### 3. 对标

- 对 EX-007：提供 **behavior surface / evolution strategy / outer control anchor** 的分层变更模型。
- 对 [[Recursive-Self-Improvement]]：说明系统层自改进可以在模型参数冻结时持续发生。
- 对 [[Agent-Security]]：scope isolation 与 authority separation 相邻，但不能把二者视为同义。

## 关联概念

- [[Recursive-Self-Improvement]]
- [[Meta-Harness-Optimization]]
- [[Agent-Harness]]
- [[Agent-Security]]
