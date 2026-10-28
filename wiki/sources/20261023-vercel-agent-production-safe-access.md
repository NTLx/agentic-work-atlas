---
type: source-summary
title: "How Vercel Agent accesses production safely"
source_raw:
  - "[[20261023-vercel-agent-production-safe-access]]"
canonical_url: "https://vercel.com/blog/how-vercel-agent-accesses-production-safely"
canonical_key: "vercel-agent-production-safety"
promotion_id: "kp-20261026-vercel-prod"
work_id: "wiki_compile:vercel-agent-production-safety:20261026:recovery-v1"
correlation_id: "knowledge-promotion:week-of-2026-10-26"
raw_state: full
created: 2026-10-28
updated: 2026-10-28
tags:
  - source-summary
  - agent-security
  - verification
evidence_level: high
claim_type: mixed
source_locator:
  - "The plan determines the permissions: investigation/plan/scope boundary"
  - "Vercel Agent can only use permissions the user already has: authority ceiling, short-lived scoped tokens and API enforcement"
---

# How Vercel Agent accesses production safely

> Vercel 对其生产 Agent 权限架构的一手说明。它能证明设计与产品语义，但不能单独证明完整 action-surface coverage、漏洞抵抗力、撤销延迟或恢复效果。

## 编译摘要

### 1. 浓缩

#### 核心结论 1：先形成可审查的执行计划，再授予超出只读基线的能力

Vercel Agent 先用只读权限调查，再提出包含拟执行 work 与所需 scope 的 plan。需要写入或外部 side effect 的 plan 整体等待用户批准，而不是把 broad production credential 预先交给模型。

**判断**：权限请求的自然单位可以是“被用户理解的一组意图相关工作”，而不是每个 tool call，也不是整个 Agent session 的无限权限。

#### 核心结论 2：批准不能突破用户自己的 authority ceiling

Vercel Agent 作为应用代表用户执行，获得的权限受用户现有权限约束。OAuth 服务进一步换取更短生命周期、特定 scope 的 token，下游 API 在每次请求处执行 scope 检查。

这形成：`intent → proposed work → requested scope → human approval → short-lived credential → API enforcement`。

#### 核心结论 3：模型不是安全边界，plan 与 credential 也不是效果证明

文章明确把“模型提出动作”和“系统允许动作”分开。它也提醒只读访问仍可能暴露敏感数据，因此“read-only auto-approved”不等于无风险。

### 2. 质疑与边界

- 厂商一手架构说明可以支持“系统如何设计”，不能直接证明 adversarial robustness、错误授权率、完整中介率或事故恢复能力。
- plan scope 的安全性依赖任务分解与 scope mapping 是否正确；模型若遗漏真实 side effect，仍需要 API/action-boundary enforcement 兜底。
- 用户权限上限避免 Agent 自行扩权，但不能阻止用户本身拥有过宽权限。
- 短生命周期 credential 降低长期泄露窗口，却不能撤销已经提交的外部副作用。

### 3. 对标与约束

- 与 [[Agent-Security]]：为“授权 → 执行”接口补充一个生产架构样本，把用户 authority、plan scope、短期 token 与 API enforcement 串成同一链。
- 与 [[Least-Agency]]：least privilege 不只是工具数量少，也可以按 plan 动态授予时间/任务受限 scope。
- 与 [[Verifiable-Agent-Engineering]]：真正可验证的不是 prompt 里写了“不要改生产”，而是系统外部是否存在可观测、可拒绝的授权/执行边界。

## 重要判断

- **判断**：高影响 Agent 的权限控制应尽量绑定到“当前计划和当前用户 authority”，并由短生命周期 credential 与资源 API 在模型外强制执行；这比让模型长期持有 broad credential 更容易审计、撤销与限制 blast radius。
  - **证据**：[[20261023-vercel-agent-production-safe-access]]。
  - **边界**：当前是 Vercel 自述架构，不是独立安全实验；完整安全仍要求 action-surface coverage、撤销/恢复和生产事件证据。

### 关联概念
- [[Agent-Security]]
- [[Least-Agency]]
- [[Distinct-Principal-Identity]]
- [[Verifiable-Agent-Engineering]]
