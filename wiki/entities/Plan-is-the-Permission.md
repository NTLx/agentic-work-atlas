---
type: entity
title: Plan is the Permission
aliases:
  - Plan is the Permission
  - 计划即权限
definition: "Agent 保持只读状态，仅在明确授权时获得临时受限执行权限，执行后恢复受限"
created: 2026-07-13
updated: 2026-07-13
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

Agent 默认以只读模式运行。当需要执行变更时，Agent 先制定明确的执行计划，用户审批后 Agent 获得临时的、有范围的执行权限，完成操作后立即恢复只读状态。权限不是持久授予的——计划本身就是权限的边界。

## 核心机制

- **默认只读**: Agent 始终处于受限状态，可观察、分析、建议，但不能直接执行变更
- **计划驱动授权**: 用户审批的不是一个笼统的"允许写操作"，而是针对具体计划的逐项授权。计划定义了权限的范围和时限
- **即时回退**: 执行完成后，权限立即回收，Agent 恢复到只读模式。不存在持久提权

## 实践案例

Vercel Agent 的权限框架将此作为第二原则。典型流程：Agent 发现生产环境 500 错误 -> 追溯到最近部署 -> 制定回滚计划 -> 用户批准 -> Agent 执行回滚 -> 恢复只读。整个过程权限生命周期随计划闭合。

## 设计优势

- **爆炸半径可控**: 每次执行的权限范围由计划定义，不会出现权限蔓延
- **人类保持回路**: 关键操作必须经过人类审批，避免完全自主执行
- **审计友好**: 计划、审批、执行、回退形成完整的审计链

## 局限与质疑

该模型假设用户有能力判断计划的安全性。在高压力场景（如凌晨故障）中，工程师可能草率批准。需要配合沙箱执行（[[Agent-Containment]]）作为兜底。

## 跨域类比

类似 Kubernetes 中的 RBAC + Admission Controller：默认拒绝所有操作，每个变更需要明确的 Policy 审批，审批结果仅对该次操作有效。

## 关键数据点

- Vercel Agent 默认只读，仅在用户批准具体计划后获得临时执行权限（2026-07-08，Vercel 官方博客）
- 执行完成后权限立即回退至只读状态

## 前提与局限性

- 当前证据仅来自 Vercel 单篇博客，缺乏实际用户案例或安全审计报告
- 模型假设用户能准确判断计划安全性，在高压力场景（如凌晨故障）中该假设可能失效
- 计划的粒度定义不明——是整批授权还是逐操作授权，博客未说明

## 关联概念

- [[Distinct-Principal-Identity]]
- [[Agent-Containment]]
- [[Agent-Harness]]
