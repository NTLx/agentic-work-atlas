---
type: source-summary
title: "Before the Tool Call: Deterministic Pre-Action Authorization for Autonomous AI Agents"
source_raw:
  - "[[20260321-oap-pre-action-authorization]]"
canonical_url: "https://arxiv.org/abs/2603.20953"
raw_state: full
source_locator:
  - "synchronous pre-tool-call ALLOW / DENY / ESCALATE authorization with signed decision receipt"
  - "1,151 sessions / 4,437 decisions; restrictive tier 0/879 breaches in author-reported CTF"
  - "cloud authorization p50 ≈53 ms; ESCALATE unimplemented; tool-boundary and platform-trust limits"
created: 2026-09-20
updated: 2026-09-20
tags:
  - source-summary
  - agent-security
  - verification
evidence_level: medium
claim_type: mixed
---

# Before the Tool Call: Deterministic Pre-Action Authorization for Autonomous AI Agents

## 编译摘要

### 1. 浓缩

- **核心结论 1：动作可以在模型推理之外被同步拒绝。**
  - OAP 在每个 tool call 前验证 agent passport、capability scope、参数与 policy，并返回 ALLOW / DENY / ESCALATE，随后生成签名决策记录。
- **核心结论 2：作者的 CTF 把“模型被说服”与“动作是否被执行”分开。**
  - 报告包含 1,151 sessions、4,437 次授权决定；在 restrictive 最高等级中记录 879 次尝试、0 次成功突破，而 permissive 条件报告 74.6% success。
- **核心结论 3：同步 gate 的成本可以单独测量。**
  - 云端 API 授权 benchmark 的 p50 约 53 ms；该数字不含客户端网络 RTT，且只是当前实现与规模下的作者测量。

### 2. 质疑

- permissive 与 restrictive CTF 不是随机对照，且仅为单一银行/授权场景；不能外推成通用攻击成功率差异。
- ESCALATE 只在规范中定义，参考实现尚未完成；需要人审的部署仍由应用层自行处理。
- OAP 逐 tool call 检查，可能遗漏多个单独允许动作组合成的越权结果；direct output、retrieval、side channel 等也不在其 action surface 内。
- 平台/runtime hook 被假定可信；若执行环境本身被攻陷，pre-action hook 可以被绕过。

### 3. 对标

- 对 EX-005：提供 **pre-action authorization / permission stop** 的直接实现与测量证据，证明“模型决定调用”与“系统允许执行”可由独立组件分离。
- 对 [[Agent-Security]]：应记录 policy/version、capability、decision、signed receipt 和 fail-closed outcome；但这条链仍停在 dispatch 前，不能替代 in-flight cancellation 或 effect recovery。
- 对 EX-006：OAP 依赖签名身份与可信 runtime，但没有证明所有控制状态都必须用该 passport 载体；其平台信任假设应保留为边界。

## 关联概念

- [[Agent-Security]]
- [[Least-Agency]]
- [[Distinct-Principal-Identity]]
- [[Long-Lived-Credential-Risk]]
