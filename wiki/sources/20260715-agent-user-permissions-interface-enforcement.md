---
type: source-summary
title: "How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement"
source_raw:
  - "[[20260715-agent-user-permissions-interface-enforcement]]"
canonical_url: "https://arxiv.org/abs/2607.13718"
raw_state: full
source_locator:
  - "21-system permissions survey plus five commercial-agent walkthroughs"
  - "taxonomy: specification → derivation → runtime enforcement"
  - "12/21 deterministic enforcement; six systems clearly support post-specification change/revocation"
created: 2026-09-20
updated: 2026-09-20
tags:
  - source-summary
  - agent-security
  - verification
evidence_level: medium
claim_type: mixed
---

# How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement

## 编译摘要

### 1. 浓缩

- **核心结论 1：权限不是一个按钮，而是一条链。**
  - 论文把 Agent 权限拆成 user-facing/internal specification、从用户输入到内部策略的 derivation，以及 runtime enforcement；这三层可以由不同机制承担。
- **核心结论 2：形式化、低用户负担和确定性执行目前没有在同一方案中同时闭合。**
  - 对 21 个系统的调查中，12 个采用确定性非 AI enforcement，但作者没有发现同时实现低用户负担、形式化策略和确定性执行的方案。
- **核心结论 3：持续控制/撤销是独立设计维度。**
  - 只有 6 个系统明确支持在初始授权后修改或撤销权限；部分方案只支持会话间修改。商业产品 walkthrough 则显示频繁确认与低透明度 auto-review 之间的现实权衡。

### 2. 质疑

- 这是文献调查与 closed-source walkthrough，不是统一任务上的安全因果实验。
- 商业产品观察发生在 2026 年 5 月下旬至 6 月上旬，产品行为会变化；不能把当时 UI/审批行为当作长期实现事实。
- “确定性 enforcement”只回答策略是否按规则执行，不证明策略本身正确，也不覆盖已提交副作用的恢复。

### 3. 对标

- 对 EX-005：把 **policy specification → derivation/binding → runtime enforcement → continued revoke/update** 明确拆开，避免把“有权限 UI”误写成“动作边界已被独立执行”。
- 对 [[Agent-Security]]：authorization 必须记录 policy owner/version、derivation path、enforcement point 与 revoke/update semantics；用户确认负担本身也是可观测的运行成本。
- 对 EX-006：策略能否到达 action boundary 与策略是否来自可信 authority 是不同问题；本调查主要覆盖前者的系统形态，不证明 provenance 完整性。

## 关联概念

- [[Agent-Security]]
- [[Least-Agency]]
- [[Distinct-Principal-Identity]]
- [[Verifiable-Agent-Engineering]]
