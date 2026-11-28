---
type: entity
title: Plan is the Permission
aliases:
  - Plan is the Permission
  - 计划即权限
definition: "Agent 保持只读状态，仅在明确授权时获得临时受限执行权限，执行后恢复受限"
created: 2026-07-13
updated: 2026-11-28
tags:
  - agentic-engineering
  - security
evidence_level: medium
claim_type: extracted
related_entities:
  - "[[Agent-Containment]]"
  - "[[Distinct-Principal-Identity]]"
source_raw:
  - "[[20260708-vercel-agent.md]]"
---

# Plan is the Permission

## 定义

Agent 默认以只读模式运行。当需要执行变更时，Agent 先制定明确的执行计划，用户审批后 Agent 获得临时的、有范围的执行权限，完成操作后立即恢复只读状态。“计划即权限”是产品设计名称，不是自然语言计划本身能强制限制动作。Vercel 官方网页（2026-11-28 核验）明确描述：批准后生成短期 capability，每次调用同时检查该 capability、token scope 和团队现有权限；检查发生在平台而非模型内。

## 核心机制

- **默认只读**: Agent 始终处于受限状态，可观察、分析、建议，但不能直接执行变更
- **计划驱动授权**: 用户批准特定计划，平台据此授予范围受限的临时 capability。原文未说明逐项审批的粒度、精确 TTL 或参数绑定方式
- **即时回退**: 执行完成后，按产品描述在计划完成后恢复只读。异常退出、并发、撤销及已启动任务的语义尚未独立核验

## 实践案例

Vercel Agent 的权限框架将此作为第二原则。典型流程：Agent 发现生产环境 500 错误 -> 追溯到最近部署 -> 制定回滚计划 -> 用户批准 -> Agent 执行回滚 -> 恢复只读。整个过程权限生命周期随计划闭合。

## 设计优势

- **爆炸半径可控**: 若平台逐次强制检查真实请求及派生权限，可缩小暴露面；计划文字本身不能排除越权
- **人类保持回路**: 关键操作必须经过人类审批，避免完全自主执行
- **审计友好**: 应将计划版本、审批、实际执行、撤销及终态回执关联；原文未证明审计覆盖完整性

## 局限与质疑

该模型假设用户有能力判断计划的安全性。在高压力场景（如凌晨故障）中，工程师可能草率批准。需要配合沙箱执行（[[Agent-Containment]]）作为兜底。

## 跨域类比

与 Kubernetes 的请求授权及 admission 分层可作类比，但不是同一授权模式。[Kubernetes 官方 Authorization](https://kubernetes.io/docs/reference/access-authn-authz/authorization/) 说明授权通过后才进入 admission；并非每次变更需要人审批，也不自动授予一次性 capability。

## 关键数据点

- Vercel Agent 默认只读，仅在用户批准具体计划后获得临时执行权限（2026-07-08，Vercel 官方博客）
- 执行完成后权限立即回退至只读状态

## 前提与局限性

- 当前证据仅来自 Vercel 单篇博客，缺乏实际用户案例或安全审计报告
- 模型假设用户能准确判断计划安全性，在高压力场景（如凌晨故障）中该假设可能失效
- [Vercel 原文](https://vercel.com/blog/vercel-agent) 明确每次调用执行三重检查；具体动作/资源绑定、计划版本、失效时钟、重放保护、撤销和外部效果回执尚待实测。读权限仍有敏感数据暴露风险；撤销未来权限不等于撤销已发生的副作用。

## 关联概念

- [[Distinct-Principal-Identity]]
- [[Agent-Containment]]
- [[Agent-Harness]]
