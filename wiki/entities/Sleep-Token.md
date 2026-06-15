---
type: entity
title: Sleep-Token
aliases:
  - Sleep-Token
  - 睡后 Token
definition: "让 Token 在人离线时持续产出候选结果的工作模式——把输入、边界、验证、回收提前设计好，第二天交给人做价值判断。核心指标是「有多少结果进入了判断流程」而非「烧了多少 Token」"
created: 2026-06-13
updated: 2026-06-16
evidence_level: medium
claim_type: mixed
tags:
  - agent-harness
  - workflow
  - coding-agent
related_entities:
  - "[[Agent-Harness]]"
  - "[[Coding-Agents]]"
  - "[[Agentic-Engineering]]"
  - "[[Agent-Verification]]"
source_raw:
  - "[[20260613-qoder-human-bottleneck]]"
---

# Sleep-Token（睡后 Token）

> [!definition] 定义
> 让 Token 在人离线时持续产出候选结果的工作模式——把输入、边界、验证、回收提前设计好，第二天交给人做价值判断。核心指标是「有多少结果进入了判断流程」而非「烧了多少 Token」。

## 关键数据点

- **核心洞察**: Token 产出的价值如果持续高于成本，凌晨三点跑和下午三点跑价值一样——Token 不需要等人在线
- **634 进 12 出**: QoderWork 的 issue 自动处理漏斗——634 个 issue → 190 有效缺陷 → 25 个 CR → 12 个合入。漏斗价值不在生成了 25 个 CR，在于 622 个没进主干
- **夜间批量任务**: 设计文档 review、跨仓库 API 一致性检查、大规模重构影响面分析——需要大量 Token 但不需要实时决策的工作，排在晚上 11 点后执行
- **杠杆率变化**: 从 1:N（N 受限于在线小时数）变成接近 1:24
- **前提条件**: 验收口设计足够严——Agent 生成的每个 CR 先按负债处理，只有通过测试、review 和业务判断才进资产池

## 工作进化路径

| 阶段 | 瓶颈 | 人角色 |
|------|------|--------|
| Cursor/Copilot | 打字速度 | 执行者（人停 Token 停） |
| CLI Agent | 单任务串行 | 执行者（等 Agent 跑完） |
| 并发 Agent | 注意力切换 | 调度器（等待→调度） |
| 三层委派 | 在线时长 | 决策者（提需求/审方案/验结果） |
| 睡后 Token | 无（离线产出） | 判断者（筛选候选结果） |

## 可靠运行的三个前提

- **Session 不怕断**: 会话是持久的事件流，和进程存活无关。状态落在事件流里，不藏在进程里
- **Sandbox 不怕换**: 执行环境可替换，失败重新 provision，无需手动恢复
- **Harness 不怕重启**: 无状态的大脑，随时用 wake(sessionId) 接管

## 前提与局限性

- **前提**: Token 产出价值稳定高于成本；验收口设计足够严格；可检测性内置在工作流中
- **风险三维度**: 概率、影响、可检测性——Böckeler 认为可检测性最关键（"你能不能发现它出了错"）
- **Harness 成本**: Agent 开发 70% 的成本不在模型推理，在 Harness（Token 编排、安全沙箱、可观测性、状态持久化、错误恢复）
- **个人 Harness 无法规模化**: SOTA 模型加速进化导致 Harness 加速过期，每个工程师自建无法传承

## 关联概念

- [[Agent-Harness]] — 睡后 Token 需要完整的 Harness 基础设施支撑
- [[Agent-Verification]] — 验收漏斗是睡后 Token 安全运行的核心保障
- [[Coding-Agents]] — 睡后 Token 是 Coding Agent 工作方式的终极演进阶段
- [[Agentic-Engineering]] — 从"更快打字"到"离线产出"的工程范式转变
