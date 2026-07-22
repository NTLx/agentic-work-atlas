---
type: entity
title: MCP Registry (MCP 注册表)
aliases:
  - MCP 注册表
  - MCP Registry
definition: "MCP 生态中的中心治理组件，负责批准 server、暴露工具目录、校验权限、记录安全姿态和支撑生产级工具发现"
created: 2026-05-13
updated: 2026-07-22
evidence_level: medium
claim_type: mixed
tags:
  - AI-Agent
  - governance
  - infrastructure
related_entities:
  - "[[Model-Context-Protocol-MCP]]"
  - "[[Pinterest-Engineering]]"
  - "[[Harness-Engineering]]"
  - "[[Context-Engineering]]"
source_raw:
  - "[[Building an MCP Ecosystem at Pinterest]]"
  - "[[20260617-huggingface-agentic-resource-discovery]]"
---

# MCP Registry

> **核心洞察**：没有治理的工具集只是乱堆的积木，注册表是 Agent 工具生态的“交通指挥中心”。

> [!definition] 定义
> MCP Registry 是 MCP 生态中的中心治理组件，负责批准 server、暴露工具目录、校验权限、记录安全姿态和支撑生产级工具发现。

## 为什么重要

没有 registry，MCP 生态很容易退化成“每个团队都暴露一点工具”的碎片化集成。Agent 看见的工具越多，误用、越权、上下文拥挤和责任不清的风险越高。Registry 把工具生态从个人效率工具升级为组织治理系统。

在 Pinterest 案例中，registry 同时服务人和 AI client：人类通过 Web UI 查看 server owner、support channel、安全姿态、在线状态和可见工具；AI client 通过 API 发现、验证和连接 server；内部服务还能询问某个用户是否允许使用某个 server。

## 核心功能

1. **服务发现 (Discovery)**：展示或返回 MCP server、owner、support channel、live status 和可见 tools。
2. **安全与准入 (Governance)**：只有进入 registry 的 server 才被视为 production approved；非实验 server 需要 owning team 和 Security、Legal/Privacy、GenAI review。
3. **权限校验 (AuthZ)**：在 Agent 调用工具前，确认当前用户、业务组或服务身份是否允许使用该 server 和具体 tool。
4. **上下文控制**：让 client 按需选择领域特定 server，避免把所有工具一次性塞进上下文窗口。
5. **运营可观测**：记录 server 数、tool 数、调用量、异常和 owner 元数据，为平台演进和价值评估提供依据。

## Pinterest 的双层鉴权模型

1. **JWT 令牌 (End-user JWTs)**：在 Web Chat、IDE、内部聊天机器人等前端捕获用户身份，确保 Agent 操作具有用户归属和可审计性。
2. **网格身份 (Mesh Identities / SPIFFE)**：对于低风险、只读、无人在场的服务间场景，基于服务网格身份进行机器间验证。

这套模型的关键不是“登录一次”，而是让 Agent 的工具能力继承真实组织权限。即使 Presto MCP server 技术上可从广泛 surface 触达，只有被批准的业务组才能建立 session 并调用高权限工具。

---

## 关键数据点

- 注册表是所有非一次性实验的 MCP 服务器必须注册的地方。
- 通过注册表，Pinterest 实现了基于**业务组（Business Group）**的权限隔离，例如只有财务组能访问包含敏感收入指标的 Presto 服务器。
- Registry 同时面向人类 Web UI 和 AI client API，因此它既是目录，也是运行时授权和生产准入门。
- Registry 把 MCP server 的安全 review、live status、visible tools、support channel 和 owner 统一到一个可查询表面。

## Registry = 宪法级权力（07-22 圆桌）

Registry 的治理地位被低估了（synthesized/medium，来源：[[2026-07-22]] 研究日志）：

- **定义"合法 server" = 宪法条款**：谁能上架、谁为谁担保、什么算合法 server——这不是治理的一个环节，是治理本身（Lessig "Code is Law"：架构即法律）。Registry 是 agent 生态"圈外资源"入口的边境检查站：守门人不只控制进出，还**定义异质能以什么形态存在**。
- **信任锚 = 谢林点**：registry 的网络效应是协调均衡而非质量胜出——"每个人预期每个人信任既有锚，所以每个人信任它"。默认侧拥有举证特权（继续信任既有锚不需理由，切换信任锚需证明），举证成本本身加固默认侧。
- **fork registry 不可行 = 可信威胁缺失**：fork 规范容易，fork 信任锚的网络效应不可行（新锚冷启动无历史信任可压缩——信任=压缩过的过去，不可伪造）。因此对 registry 治理者的纪律机制（"退出可能性"）经验性地不可兑现——这是 MCP 治理比规范治理更脆弱的结构性原因。
- ** Pinterest 双层鉴权是操作层雏形**：身份/权限验证属制度堆栈的操作层；缺失的是集体选择层（分级责任）与宪法层（可插拔信任模型的不可单方修改性）。

## 前提与局限性

- **前提**：所有 Agent 客户端必须集成了对注册表的 API 调用流程。
- **局限性**：注册表本身成为单点故障风险（SPOF），需要高可用的架构保障。
- **局限性**：Registry 只能记录和执行治理规则，不能替代工具设计质量；错误的 tool schema、模糊描述和不稳定后端仍会让 Agent 误用。
- **组织风险**：Registry 也可能成为审批瓶颈。随着 server 数量增长，需要清晰 owner、审查 SLA、废弃机制和质量评分。

## 关联概念

- [[Model-Context-Protocol-MCP]] - 协议基础
- [[Pinterest-Engineering]] - 生产级 MCP registry 的案例来源
- [[Harness-Engineering]] - 注册表是驾驭系统的关键治理组件
- [[Context-Engineering]] - 决定 Agent 看到哪些工具
