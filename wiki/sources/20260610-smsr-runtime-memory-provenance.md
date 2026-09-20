---
type: source-summary
title: "SMSR: Certified Defence Against Runtime Memory Poisoning in Persistent LLM Agent Systems"
source_raw:
  - "[[20260610-smsr-runtime-memory-provenance]]"
canonical_url: "https://arxiv.org/abs/2606.12703"
raw_state: full
source_locator:
  - "HMAC-SHA256 write provenance and randomized retrieval defence"
  - "3,150 trials; unsigned injection 93–100% to 0%"
  - "authenticated injection 8.0%; live-stack query-only attack 65.3% to 5.3%"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - agent-security
  - verification
evidence_level: medium
claim_type: mixed
---

# SMSR: Certified Defence Against Runtime Memory Poisoning in Persistent LLM Agent Systems

## 编译摘要

### 1. 浓缩

- **核心结论 1：runtime memory 的写入来源可以成为独立安全边界。**
  - 关键证据：HMAC write provenance 在作者测试中把 unsigned injection 的 attack success 从 93–100% 降至 0%。
- **核心结论 2：来源合法仍不等于内容可信。**
  - 关键证据：对 authenticated adversary 还需要 randomized ablation + verdict voting；单次 authenticated injection 成功率仍为 8.0%。
- **核心结论 3：provenance 与 retrieval robustness 可以组合，但存在 utility trade-off。**
  - 关键证据：组合防御 clean-query utility 报告为 85%。

### 2. 质疑

- HMAC 证明“谁写的”，不证明写入内容语义正确。
- authenticated writer 的权限变更、撤销与历史 memory 是否继续有效，是论文没有闭合的时间绑定问题。
- memory 安全结果不直接证明高影响 tool action 的 post-state 安全。

### 3. 对标

- 对 EX-006：补强 issuer/provenance binding，并把 unsigned 与 authenticated injection 明确拆开。
- 对 EX-005：当 authority 被撤销后，过去签名的 memory 如何处理仍需要 recovery/reconciliation 规则。
- 对 [[Agent-Attack-Surface]]：memory poisoning 是状态入口；SMSR 则是写路径 provenance 控制。

## 关联概念

- [[Agent-Security]]
- [[Agent-Attack-Surface]]
- [[Shared-Memory-Contamination]]
- [[Distinct-Principal-Identity]]
