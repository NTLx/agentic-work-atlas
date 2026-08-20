---
type: entity
title: Claude Tag
aliases:
  - Claude Tag
  - Anthropic Claude Tag
  - Claude On-Call
definition: "Anthropic 出品的 Slack-resident AI agent 产品——Claude 拥有独立 service account，作为常驻成员加入 on-call Slack 频道，跨事故保有记忆、能调用 MCP Connectors 工具、按 markdown skill 文件执行 on-call 流程"
created: 2026-08-19
updated: 2026-08-19
tags:
  - agentic-engineering
  - on-call
  - mcp
  - claude-tag
  - product-page
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[Agent-Harness]]"
  - "[[Model-Context-Protocol-MCP]]"
  - "[[Distinct-Principal-Identity]]"
  - "[[On-Call-Agent]]"
  - "[[Lessons-MD-Self-Improvement]]"
  - "[[Skills-as-Products]]"
source_raw:
  - "[[20260819-anthropic-claude-tag-oncall]]"
---

# Claude Tag

> [!definition] 定义
> **Claude Tag** 是 Anthropic 出品的 Slack-resident AI agent 产品：Claude 拥有独立 service account，作为常驻成员加入团队 on-call Slack 频道，跨事故保有记忆、能通过 MCP Connectors 调用工具（如 Datadog/Grafana/GitHub/K8s/PagerDuty）、按 GitHub 仓库中的 markdown skill 文件执行 on-call 流程，并通过 `claude.com/product/tag` 公开给 Claude Team/Enterprise 客户。

## 关键能力

- **独立身份**：Claude Tag 自带 service account（参考 [[Distinct-Principal-Identity]]），由组织 owner 一次性配置；不需要为每个 incident 创建临时身份
- **跨事故持久记忆**：Claude Tag 持有 on-call channel 的记忆，新事故开始时读取 lessons.md 与最近 incident 上下文
- **工具调用**：通过 MCP Connectors 连接 Datadog/Grafana/GitHub/K8s/PagerDuty/Slack 等基础设施；MCP 是工具接入标准（[[Model-Context-Protocol-MCP]]）
- **自然语言调度**：以 "run CI handoff every Monday at 9:00am EST" 这种自然语言触发定时任务，无需配置 cron
- **Skill 文件驱动**：所有 standing instructions 以 markdown 文件存在 GitHub 仓库，多人协作迭代

## 架构要素

| 要素 | 实现 |
|------|------|
| 记忆 | Slack channel + lessons.md |
| 工具 | MCP Connectors 到 Datadog/Grafana/GitHub/K8s/PagerDuty |
| 调度 | 自然语言 prompts 在 on-call channel |
| 指令 | GitHub 仓库中的 markdown skill（oncall.md / investigation skill / triage/） |

## 关键数据点

- Anthropic CI 团队用 Claude Tag 跑了"几个月"成为 CI/CD 事故 first responder
- 首份 evidence-grounded SITREP 中位数 14 分钟、最快 4 分钟、revert 后 3 分钟验证
- investigation skill 单条 617 行（如 shadow divergence bugs）

## 前提与局限性

- **依赖企业版许可**：需要 Claude Team 或 Claude Enterprise 计划
- **依赖 MCP 生态成熟度**：Datadog/Grafana/GitHub/K8s 等必须已有 MCP server 实现，否则 Claude Tag 的工具能力空载
- **Slack-bound**：当前形态以 Slack 频道为前端；其他 IM 平台需要适配
- **运营责任仍归人**：Claude Tag 不能完全无人监督——文中明示 multi-player 模式，"Either of us can steer the investigation or add a hypothesis in real-time, together"
- **Anthropic 自报数据**：所有指标来自自家 CI 团队；外部组织的 MTTR 改善幅度未公开

## 关联概念

- [[Agent-Harness]] — Claude Tag 是面向 on-call 场景的 harness 实例，包装 Claude 模型 + Slack + MCP + skill 仓库
- [[Model-Context-Protocol-MCP]] — 工具接入协议，Claude Tag 通过 MCP 联通外部系统
- [[Distinct-Principal-Identity]] — Claude Tag 的 service account 是 agent 独立身份的产品化形态
- [[On-Call-Agent]] — Claude Tag 的目标用例：让 agent 成为 on-call first responder
- [[Lessons-MD-Self-Improvement]] — Claude Tag 跨事故累积 lessons.md 的自改进模式
- [[Skills-as-Products]] — Claude Tag 的指令系统是 skills-as-products 治理的产品化实例
- [[Agent-Orchestration]] — Claude Tag 启用的 orchestrator + executor 双层动态工作流是编排层的实证