---
type: source-summary
title: "Build real agentic apps using CUGA: IBM's lightweight agent harness"
source_raw:
  - "[[20260623-ibm-cuga-agent-harness]]"
created: 2026-07-05
updated: 2026-07-05
tags:
  - source-summary
  - agent-harness
  - agentic-engineering
  - enterprise-ai
evidence_level: medium
claim_type: extracted
---

# Build real agentic apps using CUGA: IBM's lightweight agent harness

## 编译摘要

### 1. 浓缩
- **核心结论1**: CUGA 代表了 "governed by construction" 的 harness 设计——六种策略类型（Intent Guard/Tool Approval/Output Formatter/Tool Guide/Rate Limiter/CustomPolicy）在运行时内置，治理路径是默认路径而非附加层
  - 关键证据: IBM Research 开源项目，pip install cuga，策略系统使用 sqlite-vec 进行语义匹配，策略文件版本化在 .cuga 文件夹中
- **核心结论2**: CUGA 的轻量 API 设计（`CugaAgent` = 工具列表 + prompt → `await agent.invoke(...)`）体现了 "Harness carries the load" 理念——planning、reflection、variable-tracking 由 harness 承担，使较小的开源模型也能在 AppWorld 和 WebArena 等 benchmark 上领先
  - 关键证据: 三个推理模式（Fast/Balanced/Accurate）、三种沙箱（local/Docker/E2B cloud）、模型无关的一键切换
- **核心结论3**: CUGA Supervisor 的多 Agent 架构（Ouroboros 七 Agent 线索生成系统）和 Agent Skills（SKILL.md + ALTK-Evolve 自进化）展示了从单 Agent 到多 Agent 的平滑扩展路径
  - 关键证据: 两个打单文件应用示例 + Sovereign Core 生产部署（gpt-oss-120b 完全离线运行，OpenTelemetry 追踪）

### 2. 质疑
- **关于"governed by construction"的质疑**: 六种策略类型覆盖了常见场景，但策略本身仍需人工定义——"governed by construction"指的是治理机制内置，而非治理规则自动生成
- **关于 benchmark 领先的质疑**: AppWorld 和 WebArena 的领先可能部分归因于 harness 设计，也可能部分归因于模型选择——需要更严格的 ablation 研究
- **关于 ALTK-Evolve 的质疑**: Agent 从自身运行中改进 Skill 存在自我强化偏差的风险——如果初始 Skill 有缺陷，自我进化可能放大而非修正

### 3. 对标
- **跨域关联1**: CUGA 的 "governed by construction" 与 [[Constraint-Infrastructure]] 理念完全一致——将约束嵌入运行时而非事后附加
- **跨域关联2**: CUGA 的轻量 API + 策略系统与 [[HaaS-Harness-as-a-Service]] 的 "从构建 API 到构建 Harness 运行时" 对应——CUGA 是 HaaS 的开源实现
- **跨域关联3**: Agent Skills 的按需加载模式与 [[Context-Engineering]] 中的 "Just in Time" 检索和 [[Skill-Chains]] 形成呼应

### 关联概念
- [[Agent-Harness]]
- [[HaaS-Harness-as-a-Service]]
- [[Constraint-Infrastructure]]
- [[Context-Engineering]]
- [[Skill-Chains]]
- [[Agent-Orchestration]]