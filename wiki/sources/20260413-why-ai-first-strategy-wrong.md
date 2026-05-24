---
type: source-summary
title: "Why Your 'AI-First' Strategy Is Probably Wrong"
source_raw:
  - "[[20260413-why-ai-first-strategy-wrong]]"
created: 2026-05-24
updated: 2026-05-24
tags:
  - source-summary
  - AI-Agent
  - harness-engineering
  - engineering
---

# Why Your 'AI-First' Strategy Is Probably Wrong

## 编译摘要

### 1. 浓缩
- **核心结论1**: AI-First ≠ AI-Assisted — 差距是量级上的，不是线性的
  - 关键证据: AI-Assisted 只是把 AI 嫁接到现有流程（效率+10-20%）；AI-First 重新设计流程、架构和组织（从六周一版本到一天八部署）
- **核心结论2**: 工程团队的角色从"编写代码"转向"构建让 Agent 能有效工作的系统"
  - 关键证据: CREAO 实现 99% AI 编码，14 天内每天 3-8 次部署；OpenAI 2026.02 命名为"Harness Engineering"
- **核心结论3**: 适应能力 > 积累的技能 — 初级工程师比高级工程师适应更快
  - 关键证据: 没有十年习惯需要抛弃的工具放大了初级工程师影响力；高级工程师两月工作 AI 一小时完成

### 2. 质疑
- **关于"99% 生产代码由 AI 编写"的质疑**: CREAO 是 Agent 平台，用自家 Agent 重建自家——样本有选择偏差，非普适工业案例
- **关于"14 天内每天 3-8 次部署"的质疑**: 未披露部署粒度（是功能级还是微改动？）和回滚率（"糟糕功能当天淘汰"是否计入失败部署？）
- **关于数据可靠性的质疑**: 单一作者（CREAO CTO 第一人称），无第三方审计；用户参与度/付费转化率上升未提供基准线和具体数值
- **边界条件**: 25 人团队的系统，在 250 人或 2500 人组织中是否可扩展？复杂合规/安全领域的适用性未经验证

### 3. 对标
- **跨域关联1**: 现象类似 [[Constraint-Driven-Engineering]]——从"约束决定选择"到"Agent 能力决定架构"。Monorepo 统一不是技术偏好，而是 Agent 可见性的必要约束
- **跨域关联2**: "验证速度必须匹配实现速度"原则类似 [[Always-On-Economy]] 的 24/7 运营模式——流水线任何环节的速度不匹配都会成为整体制约
- **跨域关联3**: 从"代码产出到决策质量"的价值转移正是 [[Decision-Quality]] 和 [[Taste]] 的工程实践版本——架构师的核心能力是批评 AI 而非跟随它

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
