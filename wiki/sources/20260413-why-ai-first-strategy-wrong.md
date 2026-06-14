---
type: source-summary
title: "Why Your 'AI-First' Strategy Is Probably Wrong"
source_raw:
  - "[[20260413-why-ai-first-strategy-wrong]]"
created: 2026-05-24
updated: 2026-05-25
tags:
  - source-summary
  - AI-Agent
  - engineering
---

# Why Your 'AI-First' Strategy Is Probably Wrong

## 编译摘要

### 1. 浓缩
- **核心结论1**: AI-first 不是把 Copilot、Cursor 或 ChatGPT 加到旧流程里，而是围绕"AI 是主要构建者"重写流程、架构和组织。
  - 关键证据: 作者区分 AI-assisted 与 AI-first。前者是在原有 sprint、Jira、standup、QA sign-off 上加 AI，通常只有 10% 到 20% 效率收益；后者改变计划、构建、测试、部署和团队角色，使 CREAO 从六周周期变成一天内多次部署和实验。
  - 核心转换是问题表述：不是"AI 如何帮助工程师"，而是"如何重构一切，让 AI 做构建，人负责方向和判断"。
- **核心结论2**: Harness engineering 的中心任务是让 agent 能看见系统、理解失败、接受约束并通过验证，而不是让模型"更努力"。
  - 关键证据: CREAO 将多仓库系统统一为 monorepo，因为 fragmented codebase 对 agent 不透明，无法看见跨服务影响或本地跑集成测试；他们还建立六阶段 CI/CD、Claude 三路代码审查、CloudWatch/Sentry/Linear 的自愈反馈环。
  - 文章中最重要的工程原则是：验证速度必须匹配实现速度。否则 AI 把 build time 从几天压到几小时后，QA、PM、营销或发布流程会变成新的瓶颈。
- **核心结论3**: AI-first 组织把人的价值从代码产出迁移到决策质量、批判能力、品味和风险判断。
  - 关键证据: 作者把新工程组织分成 Architect 与 Operator。Architect 设计 SOP、测试基础设施、集成系统、triage 系统和架构边界，定义 agent 的"好"；Operator 调查、验证、审查风险和处理局部任务。
  - 对工程师的建议也很明确：写代码快的价值每月下降，评估、批评和指挥 AI 的价值上升。能发现 agent 漏掉的失败模式，比能亲手生产更多代码更稀缺。
- **核心结论4**: AI-first 的组织代价真实存在，不能只看部署频率。
  - 关键证据: 作者承认 CTO 工作强度上升、员工不确定性增加、高级工程师价值感受冲击、旧系统被拆而新系统尚未证明的过渡期成本。CREAO 的案例是激进重构，不是低摩擦升级。

### 2. 质疑
- **关于样本偏差的质疑**: CREAO 是 25 人 agent 平台公司，用自家 agents 重建自家工程系统。这是高适配样本，不能直接外推到大型企业、强监管行业、硬件系统或遗留系统深重的组织。
- **关于指标的质疑**: 99% 生产代码由 AI 编写、14 天每天 3 到 8 次部署、用户参与和付费转化上升，都是一手叙述，缺少第三方审计、基准线和部署粒度。坏功能当天杀掉是高速学习，也可能掩盖高失败率。
- **关于角色判断的质疑**: "初级工程师适应更快"可能成立于短期工具迁移，但长期系统设计、风险建模、产品品味和复杂故障诊断仍可能依赖深经验。不能把传统技能贬为无用，只能说未经重构的传统习惯会拖慢转型。
- **关于组织代价的质疑**: 作者把管理时间从 60% 降到低于 10% 描述为收益，但这也可能带来沟通断裂、心理安全下降和隐性知识流失。AI-first 不只是技术架构问题，也是组织契约问题。

### 3. 对标
- **与 [[Harness-Engineering]] 对标**: 这篇是 harness engineering 的组织级案例。harness 不只是测试脚本，而是让 agent 可见、可执行、可验证、可回滚、可审查的一整套工作系统。
- **与 [[Machine-Readable-Processes]] 对标**: CREAO 把部署、监控、错误聚类、PR 审查、feature flag、release note 都变成 agent 可读写的结构化流程，说明 AI-first 的底层是流程可机器操作。
- **与 [[Agent-First-Process-Redesign]] 对标**: 文章的核心不是工具清单，而是流程重构。PM、QA、工程、营销任一环节仍按人类速度运行，都会成为新瓶颈。
- **与 [[Decision-Quality]] 和 [[Taste]] 对标**: 当 agent 负责产出，人类的比较优势转向判断什么值得做、什么风险不能接受、什么设计看似可运行但长期会坏。

### 关联概念
- [[Harness-Engineering]]
- [[AI-First]]
- [[Agentic-Engineering]]
- [[Vibe-Coding]]
- [[Machine-Readable-Processes]]
- [[Decision-Quality]]
- [[Taste]]
- [[Context-Engineering]]
- [[Constraint-Driven-Engineering]]
- [[Agent-First-Process-Redesign]]
- [[Verifiability]]
