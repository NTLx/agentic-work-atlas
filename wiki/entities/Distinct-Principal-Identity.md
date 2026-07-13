---
type: entity
title: Distinct Principal Identity
aliases:
  - Distinct Principal Identity
  - 独立主体身份
definition: "AI Agent 使用独立身份而非继承用户凭证，实现清晰归因与受限权限"
created: 2026-07-13
updated: 2026-07-13
tags:
  - agentic-engineering
  - security
evidence_level: medium
claim_type: extracted
related_entities:
  - "[[Agent-Containment]]"
  - "[[Agent-Harness]]"
source_raw:
  - "[[20260708-vercel-agent.md]]"
---

# Distinct Principal Identity

## 定义

AI Agent 使用独立身份（distinct principal identity）而非继承用户凭证来访问系统资源。该身份拥有独立的服务账号，其权限范围由平台显式授予，而非从用户 session 中派生。

## 核心机制

- **归因清晰**: Agent 的所有操作在审计日志中以独立身份记录，不会与人类用户的操作混淆
- **权限隔离**: Agent 身份的权限上限由平台策略决定，即使触发 Agent 的用户拥有更高权限，Agent 也无法越权
- **凭证独立管理**: Agent 的凭证可独立吊销、轮换，不影响用户凭证；用户账号泄露不会波及 Agent

## 实践案例

Vercel Agent 使用独立 principal identity 而非继承用户凭证访问 Vercel 平台资源。这是其权限框架三原则之首，与 [[Plan-is-the-Permission]]（动态权限控制）和沙箱执行共同构成安全体系。

## 跨域类比

类似 CI/CD 系统中 deploy bot 使用独立 service account（如 GitHub Actions 的 `GITHUB_TOKEN`）而非开发者个人 PAT 的实践。核心逻辑一致：操作归因可追溯、凭证可独立管理、权限边界独立于触发者。

## 关键数据点

- Vercel Agent 使用独立 principal identity，不继承用户凭证（2026-07-08，Vercel 官方博客）
- 该身份拥有独立服务账号，权限由平台显式授予

## 前提与局限性

- 当前证据仅来自 Vercel 单篇博客，缺乏独立安全审计或第三方验证
- 博客属产品宣传材料，未披露权限粒度、IAM scope 细节或凭证管理具体实现
- 独立身份的实际安全收益取决于平台的权限隔离实现质量，而非概念本身

## 关联概念

- [[Agent-Containment]]
- [[Agent-Harness]]
- [[Plan-is-the-Permission]]
