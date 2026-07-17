---
type: entity
title: Distinct Principal Identity
aliases:
  - Distinct Principal Identity
  - 独立主体身份
  - Agent Identity
  - Agent Principal
definition: "AI Agent 使用独立身份而非继承用户凭证，实现清晰归因、受限权限和组织级审计追踪。从技术安全模式（service account）到企业组织集成（目录条目、角色分配、邮箱）的完整光谱。"
created: 2026-07-13
updated: 2026-07-14
evidence_level: high
claim_type: mixed
tags:
  - agentic-engineering
  - security
  - enterprise
  - governance
related_entities:
  - "[[Agent-Containment]]"
  - "[[Agent-Harness]]"
  - "[[Plan-is-the-Permission]]"
  - "[[Policy-as-Code-for-Agent-Governance]]"
  - "[[Forward-Deployed-AI-Enablement]]"
source_raw:
  - "[[20260713-microsoft-ships-ai-agents-enterprise-scale]]"
  - "[[20260708-vercel-agent.md]]"
---

# Distinct Principal Identity

> [!definition] 定义
> **Distinct Principal Identity** 是 AI Agent 使用独立身份而非继承用户凭证来访问系统资源的架构模式。从技术安全层（service account、权限隔离）到企业组织集成层（目录条目、角色分配、邮箱、经理汇报线），形成完整光谱。

## 技术安全层：核心机制

- **归因清晰**: Agent 的所有操作在审计日志中以独立身份记录，不会与人类用户的操作混淆
- **权限隔离**: Agent 身份的权限上限由平台策略决定，即使触发 Agent 的用户拥有更高权限，Agent 也无法越权
- **凭证独立管理**: Agent 的凭证可独立吊销、轮换，不影响用户凭证

## 企业组织集成层：Microsoft 实现

行业共识是**扩展现有企业身份系统**将 Agent 作为新类型的 principal，而非发明平行系统。Microsoft 通过 Entra 扩展实现：

- Agent 拥有命名的目录条目
- 在组织架构中向经理汇报
- 拥有自己的邮箱
- 有独立的角色分配和审计追踪

> "A misbehaving agent gets bounded by the same access controls that bound a misbehaving employee."（Marco Casalaina, Microsoft）

### Action Surface：身份的意义在于行动

身份定义了 Agent **被允许触达什么**。Agent 还需要**行动面**来完成实际工作——读取收件箱、发送消息、安排会议、编辑共享文档。Microsoft 通过 Work IQ 提供行动面。

### Guardrails at Tool Boundary

Agent 比聊天机器人有更多防御面：不仅读取用户 prompt 和模型回复，还读取工具输出和检索文档。**间接 prompt 注入**攻击面更大。修复：将 guardrails 移到**工具边界**——在工具调用和工具响应级别运行分类器，配置一次即所有使用该工具的 Agent 继承。

## 实践案例

| 实现 | 范围 | 身份系统 |
|------|------|---------|
| **Vercel Agent** | 平台资源访问 | 独立 service account，权限由平台显式授予 |
| **Microsoft Foundry** | 企业组织集成 | Entra 扩展（目录条目、角色、邮箱、行动面） |

## 跨域类比

- **CI/CD deploy bot**: 使用独立 service account（如 GitHub Actions 的 `GITHUB_TOKEN`）而非开发者个人 PAT
- **Virtual employee**: Agent-as-employee 与 FDE 的对照——FDE 是嵌入客户的人类工程师，Agent 是嵌入组织的数字员工

## 关键数据点

- Vercel Agent 使用独立 principal identity，不继承用户凭证（2026-07-08）
- Microsoft Foundry 通过 Entra 扩展，使 Agent 拥有目录条目、经理汇报线和邮箱（2026-07-13）
- Microsoft 在工具调用和工具响应级别运行分类器，guardrails 配置一次即所有 Agent 继承（2026-07-13）

## 前提与局限性

- 企业身份集成依赖成熟的 IAM 系统（如 Entra/Active Directory）——初创公司可能缺乏
- Agent-as-employee 隐喻可能过度简化 Agent 的组织角色
- 工具边界 guardrails 增加每次工具调用的延迟
- 独立身份的实际安全收益取决于平台的权限隔离实现质量

## 关联概念

- [[Agent-Containment]] — Identity 是 containment 的访问控制层实现
- [[Agent-Harness]] — Identity 是生产 harness 五层架构的第四层
- [[Plan-is-the-Permission]] — 动态权限控制与身份结合形成完整安全体系
- [[Policy-as-Code-for-Agent-Governance]] — Identity 与 policy 结合形成治理体系
- [[Forward-Deployed-AI-Enablement]] — Agent-as-employee 与 FDE 的对照

## 治理三层模型中的位置（07-17 深度思考）

Distinct Principal Identity 处于 Agent 委派治理**三层保证模型**的 L1（表达保证层）。它回答了"谁在行动"——但单独的身份层不能构成治理。完整治理需要：

- **L0（机制保证/独立执行层）**：独立裁决者 + 不可篡改日志 + 独立撤销通道。身份只是 L1——如果撤销通道不独立于 agent runtime，身份再清晰也无法强制收回权限。
- **L+（意图保证/管理者委派决策）**：管理者声明委派范围和承担风险。身份让"谁的 agent 做了什么"可追溯——但追溯到的归因要有人负责，这个人就是 L+ 的管理者。

产业验证（07-17 联网）：Riptides 明确指出"SPIFFE by itself only solves issuance, not policy, posture, or credential lifecycle"——身份（L1）≠ 控制（L0）。Agat Software 正在商业化 agent 执行层 runtime enforcement——这是 L0 在产业中的形态。Stacklok 指出企业架构评审核心问题已从"用哪个 LLM"变成"如何知道 agent 被允许做什么 + 运行时证明 + 事后审计"。

详见：07-17 深度思考（roundtable 4人3轮+think 7层到底）→ 三层保证模型 + 数字主权不可外包残差定理
