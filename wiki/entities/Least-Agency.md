---
type: entity
title: "Least Agency"
aliases:
  - 最小代理权
  - least-agency
definition: "将Agent可用工具、功能、权限、操作对象、时间和累积行为限制到任务所需最小范围的安全原则；与Least Privilege互补，强调限制自主行动及工具组合的副作用。"
created: 2026-05-28
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
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
> Least Agency（最小代理权）强调将最小权限落实到Agent工具、功能、自主程度和委派链；OWASP在ASI02中明确使用该术语，不据此断言词源首创。Least Privilege本身也可以动态、细粒度及基于属性，并非只限制静态访问。实践中：数据库工具只获得只读查询权限，邮件摘要工具无发送/删除权限，API 仅获最小 CRUD 操作。

## 关键数据点

- 本库早期来源为Anthropic 2026-05-18《Zero Trust for AI Agents》；2026-11-28核对[OWASP ASI02](https://genai.owasp.org/agentic-applications-2026/asi02-tool-misuse-and-exploitation/) 与 [LLM03:2026 Excessive Agency](https://genai.owasp.org/llm2026/llm032026-excessive-agency/)，明确最小工具功能、权限、用户上下文、完整中介及高影响审批。
- 与 Least Privilege 的区分：Least Privilege是授权原则，RBAC只是实现之一；Least Agency把授权与可用能力、动作预算、状态、资源范围和自主审批结合
- Anthropic指南的三层权限作用域建议（非强制成熟度标准）：Foundation（静态 least-privilege roles）→ Enterprise（动态 privilege adjustment）→ Advanced（JIT/JEA + automatic expiration）
- "Impossible, not tedious" 设计测试：优先移除不必要能力；硬件绑定凭证和过期token只阻止特定滥用路径，并非所有攻击不可能。限速降低吞吐并争取响应时间；原子累计预算/拒绝门禁可约束总副作用，不等于普通限速。

## 前提与局限性

- **工具支持不成熟**: Least Agency 的实现需要细粒度的 tool capability scoping，不能从MCP协议或工具列表推断业务权限颗粒度；在实际资源服务端或完整中介的执行点核对身份、参数、资源及状态，工具发现/隐藏本身不是强制授权
- **与 Agent 能力的张力**: Agent 的价值在于自主行动能力，过度限制 agency 可能使 Agent 退化回传统软件。需要按风险与任务所需权限验证能力边界；最小权限也可减少无关工具和错误，不预设安全与效能必然冲突
- **JIT/JEA 的工程复杂度**: Just-In-Time / Just-Enough-Administration 在 multi-agent 系统中的实现成本依资源接口、身份与撤销语义而定；临时授权失效、任务恢复、已派生会话和未完成操作应独立测试

## 关联概念

- [[Agent-Containment]] — Least Agency 是 containment 策略的权限层实现
- [[Agent-Harness]] — Harness 是实施 Least Agency 约束的工程载体
- [[Verifiable-Agent-Engineering]] — Least Agency 的权限边界需要可验证机制保证
- [[Model-Context-Protocol-MCP]] — MCP 工具权限管理是 Least Agency 落地的关键场景
