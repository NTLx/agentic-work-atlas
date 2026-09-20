---
type: source-summary
title: "Partial Evidence Bench: Benchmarking Authorization-Limited Evidence in Agentic Systems"
source_raw:
  - "[[20260506-partial-evidence-bench]]"
canonical_url: "https://arxiv.org/abs/2605.05379"
raw_state: full
source_locator:
  - "72 tasks / three scenario families / ACL-partitioned corpora"
  - "complete-answer, authorized-view, completeness and gap-report oracles"
  - "four evaluation surfaces and fail-and-report baseline"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - verification
  - agent-evaluation
evidence_level: medium
claim_type: mixed
---

# Partial Evidence Bench: Benchmarking Authorization-Limited Evidence in Agentic Systems

## 编译摘要

### 1. 浓缩

- **核心结论 1：权限控制正确，不代表回答的证据完整性正确。**
  - 关键证据：benchmark 明确把 complete answer、authorized-view answer、completeness judgment 和 gap report 分成不同 oracle。
- **核心结论 2：验证系统必须判断“我看不到什么”，而不只是判断“我看到的内容是否一致”。**
  - 关键证据：72 个任务覆盖 due diligence、compliance audit、security incident response，并单独评分 completeness awareness 与 unsafe completeness。
- **核心结论 3：fail-and-report 是一种可测量的安全退化策略。**
  - 关键证据：作者的 deterministic baseline 中，silent filtering 会产生危险的完整性错觉；显式报告缺口能消除该类 unsafe completeness，而不是一律拒答。

### 2. 质疑

- 主要 benchmark 是合成且确定性的，现实系统中的 ACL、搜索排序、文档新鲜度和工具失败会引入额外混杂。
- “看不到证据”与“看到但没检查/没理解”在实际系统里会同时发生，本 benchmark 主要隔离前者。
- 初步 real-model 结果不足以证明跨模型、跨组织的统一失败率。

### 3. 对标

- 对 EX-002：把 evidence coverage 从抽象概念具体化为 **授权可见范围 + 完整性意识 + gap reporting**。
- 对 [[Sufficient-Context]]：相关证据存在并不等于当前授权视图已经足以支持完整回答。
- 对 EX-004：它提供 reference oracle，但没有同时操纵 verifier independence 与执行 post-state。

## 关联概念

- [[Verifiable-Agent-Engineering]]
- [[Sufficient-Context]]
- [[Agent-Verification]]
- [[Least-Agency]]
