---
type: comparison
title: Agent-First vs Traditional Automation
created: 2026-04-09
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - comparison
  - AI-Agent
  - Enterprise-Transformation
related_entities:
  - '[[Agent-First-Enterprise]]'
  - '[[Human-Governor-Agent-Operator]]'
  - '[[Machine-Readable-Processes]]'
source_raw:
  - "[[Enabling agent-first process redesign]]"
  - "[[Forward deployed engineering at OpenAI]]"
---

# Agent-First vs Traditional Automation

> [!summary] 对比概述
> 传统自动化将执行逻辑显式编码；Agent-first 将部分解释、规划与工具选择委托给模型，并围绕可委托、可验收的工作单元设计流程。二者可以组合，不是从人工到自动化的固定成熟度阶梯。

## 核心维度对比

| 维度 | 传统自动化 | Agent-first |
|---|---|---|
| 执行逻辑 | 预定义程序、规则、工作流 | 部分路径由模型根据任务和上下文选择 |
| 自主程度 | 可无人值守，也可有人审批 | 可有界自治，也可逐步由人确认 |
| 适用输入 | 稳定接口、可枚举规则与异常 | 非结构化输入、开放问题、难以穷举的路径 |
| 验收 | 确定性断言、状态检查 | 同样需要终态检查，并处理模型判断的不确定性 |
| 失败代价 | 规则错误、接口漂移、异常未覆盖 | 上述风险加上错误推理、工具选择和权限滥用 |
| 经济性 | 比较开发、维护及执行成本 | 另计推理、监督、验证、返工和失败损失 |

## 详细分析

Agent-first 是一种运营设计选择，不意味着传统自动化必须由人逐步操作，也不要求人类退出所有常规决策。根据风险、可逆性与证据可得性选择委派深度；确定性控制流、权限检查、事务、幂等和验收可以继续由传统程序承担。模型根据上下文调整动作不等于在线训练或持续自我优化。

机器可读流程有助于表达边界，但 YAML/JSON 本身不保证规则正确、执行受控或结果可靠。应先定义 owner、真实结果、允许动作、异常升级与停止条件，再选择表达形式。

## 适用场景与选择指南

- 稳定、可枚举、可测试的流程：优先评估确定性自动化。
- 输入含糊、需要语义解释或动态检索的步骤：评估有界 Agent，并以确定性机制约束高影响动作。
- 混合流程：让模型处理不确定部分，让程序执行已知规则和可机械检查的操作；人类按责任和风险介入。
- 对照现有流程的真实交付质量、周期、总成本、异常率与接管成本，验证新增复杂性是否值得。非线性收益不是部署的必然结果。

## 证据边界

[[Enabling agent-first process redesign]] 是 MIT Technology Review Insights 的定制内容，引用 Deloitte 架构师关于 Agent-centric workflow 的倡议，而非传统自动化与 Agent-first 的随机对照试验。[[Forward deployed engineering at OpenAI]] 是厂商对其 FDE 方法与案例的描述，支持在真实约束下部署和回流产品能力的设计方向，不证明传统自动化会绕开治理或 Agent-first 普遍优越。

## 相关概念

- [[Agent-First-Enterprise]] — 可委托、可验收的运营单元。
- [[Human-Governor-Agent-Operator]] — 按责任和风险安排分工。
- [[Machine-Readable-Processes]] — 表达流程，不等同于强制执行。
- [[Agent-First-Process-Redesign]] — 流程重构与结果验证。
