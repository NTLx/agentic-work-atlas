---
type: entity
title: "Least Agency"
aliases:
  - 最小代理权
  - least-agency
definition: "OWASP 提出的概念，将 Least Privilege 从'限制访问什么'扩展到'限制 Agent 工具能做什么、做多少次、在哪里做'——约束 Agent 的行动能力而非仅约束访问权限。"
created: 2026-05-28
updated: 2026-05-28
tags:
  - agent-security
  - zero-trust
  - enterprise
related_entities:
  - "[[Agent-Containment]]"
  - "[[Agent-Harness]]"
  - "[[Verifiable-Agent-Engineering]]"
source_raw:
  - "[[20260518-zero-trust-for-ai-agents]]"
---

# Least Agency

> [!definition] 定义
> Least Agency（最小代理权）由 OWASP 提出，是 Least Privilege（最小权限）在 agentic 应用中的扩展。Least Privilege 约束"谁能访问什么"，Least Agency 进一步约束"Agent 工具能做什么、做多少次、在哪里做"。实践中：数据库工具只获得只读查询权限，邮件摘要工具无发送/删除权限，API 仅获最小 CRUD 操作。

## 关键数据点

- 概念出自 Anthropic 2026-05 发布的《Zero Trust for AI Agents》电子书，引用 OWASP 定义
- 与 Least Privilege 的区分：Least Privilege 是静态权限约束（RBAC），Least Agency 涵盖工具能力约束（tool capability scoping）、操作频率限制（rate limiting）和作用域限制（domain/resource scoping）
- 三层实现：Foundation（静态 least-privilege roles）→ Enterprise（动态 privilege adjustment）→ Advanced（JIT/JEA + automatic expiration）
- "Impossible, not tedious" 设计测试：控制措施应使攻击在结构上不可能（如硬件绑定凭证、过期 token），而非仅增加摩擦（如 rate limits、SMS MFA）

## 前提与局限性

- **工具支持不成熟**: Least Agency 的实现需要细粒度的 tool capability scoping，当前多数 Agent 框架（包括 MCP）的工具权限模型仍是粗粒度的 allow/deny
- **与 Agent 能力的张力**: Agent 的价值在于自主行动能力，过度限制 agency 可能使 Agent 退化回传统软件。需要在安全约束和 Agent 效能之间找到平衡点
- **JIT/JEA 的工程复杂度**: Just-In-Time / Just-Enough-Administration 在 multi-agent 系统中的实现复杂度极高，尤其是动态权限回收可能在多步骤任务中导致中断

## 关联概念

- [[Agent-Containment]] — Least Agency 是 containment 策略的权限层实现
- [[Agent-Harness]] — Harness 是实施 Least Agency 约束的工程载体
- [[Verifiable-Agent-Engineering]] — Least Agency 的权限边界需要可验证机制保证
- [[Model-Context-Protocol-MCP]] — MCP 工具权限管理是 Least Agency 落地的关键场景
