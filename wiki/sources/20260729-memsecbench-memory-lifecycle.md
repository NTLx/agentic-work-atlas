---
type: source-summary
title: "MemSecBench: Tracking Agent Memory Poisoning from Persistence to Consequence and Repair"
source_raw:
  - "[[20260729-memsecbench-memory-lifecycle]]"
canonical_url: "https://arxiv.org/abs/2607.27080"
raw_state: full
source_locator:
  - "310 cases / 48 contexts / 24 stack configurations"
  - "Write–Execute–Forget lifecycle and seven checkpoint adjudication"
  - "84.2% persistence / 50.3% full Write–Execute / 56.1% selective repair among poisoned cases"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - agent-security
  - verification
evidence_level: high
claim_type: mixed
---

# MemSecBench: Tracking Agent Memory Poisoning from Persistence to Consequence and Repair

## 编译摘要

### 1. 浓缩

- **核心结论 1：memory 安全必须按生命周期测，而不能只测是否“写进去了”。**
  - 关键证据：Write→Execute→Forget 协议把 persistence、实际下游 consequence 和 repair 连在同一 case。
- **核心结论 2：memory backend / harness / model 的组合会显著改变传播与修复。**
  - 关键证据：24 种 stack 配置中，作者报告 matched configuration 的 end-to-end attack success 与 selective repair 存在明显绝对差异。
- **核心结论 3：删除恶意 memory 与恢复所有后果是不同问题。**
  - 关键证据：selective repair 只在部分成功污染 case 中完成，且 benchmark 的 repair 对象仍主要位于 memory 生命周期。

### 2. 质疑

- isolated runtime 与现实 SaaS/API 的 provider-authoritative post-state 仍有距离。
- judge-model checkpoint + programmatic gates 是 benchmark adjudication，不是独立生产审计。
- Forget 成功并不意味着已经发出的消息、已提交交易或传播工件被撤销。

### 3. 对标

- 对 EX-006：提供 carrier lifecycle 的 Write→Execute→Forget 联动证据。
- 对 EX-005：明确显示 repair 应继续追踪到 external effect，而不能在 memory 删除处提前结束。
- 对 [[Agent-Security]]：恢复链需要区分 state repair、effect compensation 和 canonical post-state verification。

## 关联概念

- [[Agent-Security]]
- [[Agent-Attack-Surface]]
- [[Shared-Memory-Contamination]]
- [[Alert-Closed-Loop]]
