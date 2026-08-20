---
type: entity
title: On-Call Agent
aliases:
  - On-Call Agent
  - On-Call First Responder
  - agent on-call
  - CI/CD on-call agent
definition: "agent 作为事故 first responder 直接承担 production incident 的检测/分诊/响应——以 Slack-resident 身份常驻 on-call channel、独立查询监控/日志/工单系统、按 markdown skill 执行流程，并与人协同验证与修复"
created: 2026-08-19
updated: 2026-08-19
tags:
  - agentic-engineering
  - sre
  - ci-cd
  - on-call
  - incident-response
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[Claude-Tag]]"
  - "[[Alert-Closed-Loop]]"
  - "[[Operational-Responsibility]]"
  - "[[Agent-Harness]]"
  - "[[Lessons-MD-Self-Improvement]]"
  - "[[Skills-as-Products]]"
source_raw:
  - "[[20260819-anthropic-claude-tag-oncall]]"
---

# On-Call Agent

> [!definition] 定义
> **On-Call Agent** 是 agent 担任事故 first responder 的运维形态：常驻 on-call 频道，跨事故保有记忆，能并行查询 Datadog/Grafana/GitHub/K8s/PagerDuty 等 source of truth，按 markdown skill 文件执行分诊/调查/修复，并以 SITREP 形式回写给人。Anthropic CI 团队的 Claude Tag 是当前公开最完整的实例。

## 核心能力

| 能力 | 描述 | Anthropic 实例 |
|------|------|----------------|
| 检测 | 分析 alerts，按 standing rule 决定 page 或 defer | Claude 监控每个 alert channel，按 oncall.md criteria 判断 |
| 分诊 | 启动 dynamic workflow，并行查多个 source of truth | orchestrator + executor 子 agent 模式 |
| 调查 | 按 investigation skill 顺序提假设、查数据、合成 SITREP | 617-line shadow divergence skill 编码完整流程 |
| 修复 | 提 PR 由人 review 合并；或在 feature flag 场景渐进式 ramp | Claude Code 子 agent 操作部署 |
| 验证 | 复用 MCP tools 验证 fix 生效 | revert 后 3 分钟内 Slack 验证告警恢复 |
| 复盘 | 写 post-mortem 到 lessons.md | 自动 append root cause/fix/gotcha |
| 通信 | 多事故聚合给团队"what's wrong with CI?" | ci-weather agent 新闻室风格报告 |
| 交接 | 每日/每周 summary 让轮班者接力 | "run CI handoff every Monday at 9:00am EST" |

## 关键设计决策

- **deterministic alerting + agentic escalation 双路径**：alert rule 仍由人写（确定性），但 page 还是 defer 由 agent 判断（agentic）。这避免"AI 完全决定谁被叫醒"的失控风险
- **multi-player 模式**：人和 agent 共享 Slack 频道，可实时 steer 或加假设。不是"agent 独自完成 + 通知人"，而是"agent 和人一起"
- **skill-driven workflow**：所有 standing instructions 在 markdown 文件中，commit 到 GitHub 仓库，多人协作迭代
- **lessons.md 跨事故累积**：每个事故自动 append，新事故先读 lessons.md，形成首假设；多次出现的模式 promote 到 investigation skill
- **服务账号身份**：agent 用自己的 service account 操作工具，独立审计与权限边界（[[Distinct-Principal-Identity]]）

## 关键数据点

- Anthropic CI 团队 Claude Tag 几个月运行
- 首份 SITREP 中位 14 分钟、最快 4 分钟定位根因
- Revert 后 3 分钟验证告警恢复
- 单条 investigation skill 617 行（shadow divergence bugs）
- 8x 代码量增长推动 on-call agent 化（与 Anthropic 自身 recursive self-improvement 数据共享）

## 前提与局限性

- **基础设施依赖**：MCP server 必须覆盖团队的监控/工单/部署工具集；缺失 connector 等于空载
- **skill 维护成本**：investigation skill 需要由熟悉该类 bug 的工程师持续维护（参考 [[Skills-as-Products]] 的 ownership 责任）
- **责任仍归人**：multi-player 模式意味着 engineer 仍需在场 override 与判断；agent 不能完全替代 on-call rotation
- **alert tuning 仍需人工**：新服务上线前几天 Claude 协助分析数据建议阈值，但最终规则由人 review
- **业务范围有限**：当前公开实例限定 CI/CD 事故；通用 incident response 是否可同形态扩展未验证

## 与 Operational Responsibility 的边界

[[Operational-Responsibility]] 是 Palantir 的生产所有权文化（"first paged = best fix"）；on-call agent 不是替代 OR，而是**承担 OR 流程中被 paging 后的 agentic 部分**——alert 仍要路由到正确的团队或人，但人在收到 page 后由 agent 协助分诊/调查/写 PR。责任主体清晰度不下降，但工作量分布改变。

## 关联概念

- [[Claude-Tag]] — Anthropic 的产品实现，是 on-call agent 当前最公开的实例
- [[Alert-Closed-Loop]] — 医疗 AI 闭环六节点结构在 CI 场景的工程变体
- [[Operational-Responsibility]] — "first paged = best fix" 在 on-call agent 时代的延伸
- [[Agent-Harness]] — on-call agent 是 harness 在 SRE 域的应用形态
- [[Lessons-MD-Self-Improvement]] — on-call agent 的跨事故自改进机制
- [[Skills-as-Products]] — investigation skill 是 skill 治理的产品化实例
- [[Forward-Deployed-Engineer]] — on-call engineer 是 FDE 在生产维护阶段的角色延伸
- [[Agent-Verification]] — on-call agent 的 SITREP + PR review 是 verification 在 CI 域的体现