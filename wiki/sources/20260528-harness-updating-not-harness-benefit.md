---
type: source-summary
title: "Harness Updating Is Not Harness Benefit: Disentangling Evolution Capabilities in Self-Evolving LLM Agents"
source_raw:
  - "[[20260528-harness-updating-not-harness-benefit]]"
canonical_url: "https://arxiv.org/abs/2605.30621"
raw_state: full
source_locator:
  - "harness-updating vs harness-benefit capability decomposition"
  - "crossed evolver × task-solving-agent evaluation"
  - "activation/adherence failure analysis"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - verification
  - agent-evaluation
evidence_level: high
claim_type: mixed
---

# Harness Updating Is Not Harness Benefit

## 编译摘要

### 1. 浓缩

- **核心结论 1：会改 harness 和会用 harness 是两个能力。**
  - 关键证据：论文独立定义 harness-updating 与 harness-benefit，并交叉改变 evolver 与 task-solving agent。
- **核心结论 2：端到端 gain 不能直接归因给 evolver。**
  - 关键证据：作者报告不同能力层 evolver 写出的更新收益差距较小，而最终受益更强地依赖执行 Agent 是否能激活并遵循 harness。
- **核心结论 3：变更“存在”还不够，需要记录 runtime activation / adherence。**
  - 关键证据：SkillsBench 将低收益拆成没加载 relevant artifact 与加载后没持续遵循两种失败。

### 2. 质疑

- activation/adherence 是 benchmark 内部行为指标，不自动代表线上真正调用了正确版本。
- 更新可用性与更新安全性是两个独立维度。
- 论文限制写评估脚本/权重有助于可审计，但不等于不可绕过的 production control plane。

### 3. 对标

- 对 EX-007：强制把 **change producer → artifact → runtime activation → adherence → outcome** 分开记录。
- 对 [[Skill-Internalization]]：沉淀为 skill 并不等于运行时会稳定激活和遵循它。
- 对 [[Recursive-Self-Improvement]]：不能用“系统写出了下一版”直接证明下一版实际拥有更高能力。

## 关联概念

- [[Recursive-Self-Improvement]]
- [[Skill-Internalization]]
- [[Agent-Harness]]
- [[Verifiable-Agent-Engineering]]
