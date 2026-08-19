---
type: source-summary
title: "Claude on call: How Claude Tag serves as Anthropic's first responder for CI/CD failures"
source_raw:
  - "[[20260819-anthropic-claude-tag-oncall]]"
created: 2026-08-19
updated: 2026-08-19
tags:
  - source-summary
  - agentic-engineering
  - ci-cd
  - on-call
  - claude-tag
evidence_level: medium
claim_type: mixed
---

# Claude on call: How Claude Tag serves as Anthropic's first responder for CI/CD failures

## 编译摘要

### 1. 浓缩

- **核心结论1**: Anthropic 用 Claude Tag 把 CI/CD on-call 的 first responder 完全代理给 agent——首份 SITREP 15 分钟内、最快 4 分钟定位根因、revert 后 3 分钟内验证告警恢复
  - 关键证据: median 14 minutes first evidence-grounded analysis; fastest 4 minutes; 3-minute post-revert Slack ping; "Claude authored the first situation report in every recent incident that had one"
- **核心结论2**: 架构是 orchestrator + executor 双层 + MCP Connectors——orchestrator 起 dynamic workflow 派 executor subagents 并行查 Grafana/log store/PagerDuty/GitHub/K8s/Slack，executor 回 report 后 orchestrator 合成 SITREP
  - 关键证据: "orchestration agent spins up executor subagents to investigate each dependency and source of truth"; "Claude can chase multiple leads in parallel, helping to reduce MTTR"; 617-line investigation skill for shadow divergence bugs
- **核心结论3**: lessons.md 构成持续自我改进循环——每次事故 Claude 自动 append root cause/fix/gotcha；新事故开始先读 lessons.md 形成首假设；同一模式多次出现则被 promote 到 investigation skill
  - 关键证据: "Claude appends to it on its own automatically"; "If the same pattern shows up enough times, we promote it into the investigation skill itself"; 经典条目 "query the data first, then theorize"

### 2. 质疑

- **关于"15 分钟首份 SITREP"的可迁移性**: 这是 Anthropic CI 团队自身基础设施（Datadog/Grafana/GitHub/K8s + Claude Tag service account）下的指标，外部组织需要先打通这些 MCP connector。文中给出的 on-call-kit 模板可压缩搭建时间，但 connector 配置的真实成本未量化
- **关于"8x 代码量"叙事**: 与 recursive self improvement 那篇数据共享——"agentic coding 必须配 agentic CI"是因果主张但未给出对照实验。代码量增长是否真的让 CI 事故响应必须 agent 化，缺乏 A/B 证据
- **关于 lessons.md 自我改进循环的边界**: 技能膨胀会不会稀释 agent 表现？与 [[20260819-ibm-altk-evolve-memory-dosage]] 在 ALTK-Evolve 上的"饱和模型零增益"现象结构同构——lessons.md 与 investigation skill 是同一种 agentic memory，剂量问题在 CI 场景同样存在，本文未讨论
- **关于"deterministic alerting + agentic escalation"双路径**: 监控规则仍由人写，Claude 在新服务上线前几天的 alert tuning 阶段仍需要人类 review——意味着这套系统没有完全去除 alert engineering 的人工成本，只是分散到 service launch 时段

### 3. 对标与旁逸

- **跨域关联1**: *lessons.md 自动 append → promote to skill* 与 ALTK-Evolve 的 guideline distillation 同构——都是把 agent 自蒸馏的可复用知识沉淀为系统层资产。但 ALTK 用 8 模型评测发现 saturated 模型零增益，Anthropic 在 CI 域缺少类似系统性测量
- **跨域关联2**: *orchestrator + executor parallel investigation* 与 [[Agent-Orchestration]] 的 OpenClaw/Zoe 编排同构——但 Anthropic 模式更轻量（每个 executor 是单次 subagent，不持久），与 OpenClaw 长期 worker 模式不同
- **跨域关联3**: *on-call first responder* 是 [[Operational-Responsibility]] "first person paged = 最佳修复者"的延伸——AI 接管"被 paging"的部分，但责任链仍归人（"Either of us can steer the investigation or add a hypothesis in real-time, together"）。这是 Palantir 预言的 agent 责任路由问题的实证答案
- **跨域关联4**: *deterministic alerting + agentic escalation* 与 [[Alert-Closed-Loop]] 的"识别→通知→接收→评估→干预→复盘"六节点结构高度同构——本文闭环里 Claude 在"识别"和"评估"两个节点替代人类，"接收"与"干预"节点仍归人。差异在医疗场景闭环对应单条 RRT 激活，本文对应持续 incident stream

## 关联概念

- [[Claude-Tag]]（新建）— Anthropic 的 on-call agent 产品，本文核心承载物
- [[On-Call-Agent]]（新建）— agent 接管 first responder 角色，本文明确定义
- [[Lessons-MD-Self-Improvement]]（新建）— incident lessons 自动累积 + promote to skill 的自改进循环
- [[Agent-Harness]] — Claude Tag 本身就是 harness 实例；本文展示了面向 on-call 场景的具体配置
- [[Agent-Orchestration]] — orchestrator + executor 双层是编排层的实证形态
- [[Alert-Closed-Loop]] — CI 事故响应闭环是医疗 AI 闭环的工程变体
- [[Operational-Responsibility]] — "first paged = best fix" 原则被 agent 部分承担但责任仍归人
- [[Skills-as-Products]] — investigation skill 作为长期维护的产品，617-line shadow divergence skill 是实例
- [[Agent-Verification]] — verification 在 CI 域中表现为 SITREP + post-mortem + PR review 三件套
- [[Forward-Deployed-Engineer]] — on-call engineer 是 FDE 在生产维护阶段的角色延伸