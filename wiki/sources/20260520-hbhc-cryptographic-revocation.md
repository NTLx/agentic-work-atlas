---
type: source-summary
title: "Heartbeat-Bound Hierarchical Credentials: Cryptographic Revocation for AI Agent Swarms"
source_raw:
  - "[[20260520-hbhc-cryptographic-revocation]]"
canonical_url: "https://arxiv.org/abs/2605.20704"
raw_state: full
source_locator:
  - "deterministic zombie-window bound and local heartbeat verification"
  - "90x OAuth comparison / 0.26 ms auth / 18,000+ verifications per second"
  - "49-agent four-level cascading revocation and zero tested post-revocation tool calls"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - agent-security
  - verification
evidence_level: medium
claim_type: mixed
---

# Heartbeat-Bound Hierarchical Credentials: Cryptographic Revocation for AI Agent Swarms

## 编译摘要

### 1. 浓缩

- **核心结论 1：Agent shutdown 与权限失效可以被拆成可测量的时间窗口。**
  - 关键证据：HBHC 以 parent heartbeat freshness 约束后代凭据，并给出确定性 zombie-window 上界。
- **核心结论 2：撤销可以放到模型/应用上下文之外执行。**
  - 关键证据：verifier 只需缓存的公钥与本地时钟即可检查 freshness，不依赖 Agent 是否遵守 prompt。
- **核心结论 3：层级授权需要层级撤销。**
  - 关键证据：作者在 49-agent、四层层级中测试级联失效，并报告测试条件下撤销后零工具调用。

### 2. 质疑

- HBHC 解决的是**未来调用权**，不是已提交副作用的 rollback；不能把“零 post-revocation call”解释为外部状态已经恢复。
- 安全上界依赖 clock skew、父密钥保护和所有目标 verifier 都实施协议。
- 与 OAuth 的 90x 比较是作者设定的协议/TTL 条件下结果，不是所有生产 OAuth 部署的统一倍数。

### 3. 对标

- 对 EX-005：提供“permission stop”层的强证据，同时反向证明它与 effect reconciliation 不是同一对象。
- 对 EX-006：这是 out-of-band authority carrier 的正例：权限存活依赖独立 heartbeat，而不是 Agent 对上下文规则的记忆。
- 对 [[Agent-Security]]：撤销链至少要区分 credential invalidation、in-flight stop 与 committed-effect recovery。

## 关联概念

- [[Agent-Security]]
- [[Distinct-Principal-Identity]]
- [[Long-Lived-Credential-Risk]]
- [[Least-Agency]]
