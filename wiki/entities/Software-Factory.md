---
type: entity
title: Software-Factory
aliases:
  - Software Factory
  - 软件工厂
definition: "Agent 驱动的自动化软件生产系统——接受生产错误、bug 报告或 feature 想法作为输入，由 agent 链自主完成 build、improve、deploy、manage 全流程，人类只保留灵感、品味与判断（inspiration/taste/judgment）"
created: 2026-08-13
updated: 2026-08-13
evidence_level: medium
claim_type: mixed
tags:
  - agentic-engineering
  - organization
  - automation
related_entities:
  - "[[Agent-Development-Lifecycle]]"
  - "[[Agent-Orchestration]]"
  - "[[Agent-Verification]]"
  - "[[Agent-Unit-of-Work]]"
  - "[[Machine-Readable-Processes]]"
  - "[[Agent-Legibility]]"
source_raw:
  - "[[20260804-agent-development-lifecycle-adlc]]"
  - "[[20260804-astro-software-factory-issue-triage]]"
  - "[[20260805-how-we-use-ai-cloudflare-os]]"
---

# Software-Factory（软件工厂）

> [!definition] 定义
> **Software Factory** 是 agent 驱动的软件生产系统：输入一个生产错误、客户 bug report 或新 feature 想法，委托给 agent 链自主完成 build、improve、deploy、manage，人类只在需要 inspiration、taste、judgement 的地方介入。与 [[Agent-Development-Lifecycle|ADLC]] 互为表里——ADLC 是生命周期范式，Software Factory 是建立在该范式之上的生产架构。

## 关键机制

### 输入输出全链委托
- 输入：production error / customer bug report / feature idea
- 输出：已修复、已预览、已部署、已维护的软件
- 关键：不是"人管每步、只把单步委托给 agent"，而是把整个流程的钥匙交给 agent（"hand over the keys"）

### 平台七项硬需求（Cloudflare, 2026-08-04）
1. **Programmatic**——ClickOps 对 agent 是 non-starter，一切操作要有 API
2. **Horizontally scalable**——每个 agent 有与生产一致的独立 preview
3. **Reproducible**——4G 模拟 / 地理 IP 类 bug 需能复现
4. **Real-time, push-based**——事件触发 agent 而非等人盯 dashboard
5. **Atomic**——每个变更独立可测/可发布/可观察/可回滚
6. **Permissioned**——agent 能 escalte 获得更多权限以完成工作
7. **Self-improving**——agent 从经验中学习（像人从 on-call 中学习）

### 实证：Astro 的 issue triage 工厂（2026-08-04）
- 隔离子代理串行（reproduce → diagnose → verify → fix），通过 `report.md` 传递
- 状态由 issue labels 驱动（`triage needed` → `fix verified`），pipeline 本身无状态
- 效果：open issues 200+ → ~30（85% 缩减），5+ 年首次接近清零
- 失败归因：agent 解不出 → 不透明抽象 / 缺文档 / 测试不足（代码库可读性信号）

## 关键数据点

- Astro：200+ → ~30 open issues；Cloudflare OS：25 万问题 / 1.6 万 merges / 4000 apps（[[20260805-how-we-use-ai-cloudflare-os]]）
- Cloudflare：SDLC 七阶段全映射到自家栈（Vite/Rolldown → Browser Run/Vitest → Flagship/Gradual Deployments → Logs/Agent Traces/MCP/Analytics）

## 前提与局限性

- **可复现性前提**：工厂管线只能处理可复现的输入——依赖真实环境（4G/地理/第三方）的 bug 不在其能力范围
- **vendor 叙事**：Cloudflare 的七项需求与栈映射来自平台发布文，自家狗粮=自家卖点，复制需剥离
- **80%→99% 鸿沟**：软件工厂与自驾车同病——从"工作 80% 时间"到"可交钥匙的 n nines"之间缺少已证实的机制路径
- **社区副作用**：客服式 bot 回复可能制造"维护者与用户的新隔阂"，Astro 自评"更多但更有用的对话"未经独立验证

## 关联概念

- [[Agent-Development-Lifecycle]] — 工厂的生命周期范式（SDLC 的 agent 版）
- [[Agent-Orchestration]] — 工厂的编排层（Workflow / Flue 状态机 / 隔离子代理）
- [[Agent-Verification]] — 工厂的验证环节（isolated subagents 反 LLM 偏见）
- [[Agent-Unit-of-Work]] — 工厂的任务粒度控制参数
- [[Machine-Readable-Processes]] — 标签驱动状态机是流程显式化的最小实现
- [[Agent-Legibility]] — "agent 失败 = 代码库不可读"把可读性变成工厂输入指标