---
type: entity
title: "碳基-硅基分工"
aliases:
  - Carbon-Silicon Division
  - 碳基定义硅基执行
  - 碳基定义者硅基执行者
definition: "作者提出的人机任务分配隐喻：部分任务由人定义、授权与验收，Agent执行；实际分工及责任取决于任务、权限和风险。"
created: 2026-05-29
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - agentic-ai
related_entities:
  - "[[Coding-Agents]]"
  - "[[Agentic-Engineering]]"
  - "[[Human-Governor-Agent-Operator]]"
  - "[[Agent-Infra]]"
source_raw:
  - "[[20260528-agentic-ai-2026-landscape]]"
---

> [!definition] 定义
> 人可在部分任务中委托Agent执行，并定义目标、约束、验证与责任；非普遍职业转型或固定人机能力边界。

## 核心命题

**能力扩大可能扩大授权范围和监督负担，但责任由制度和实际行动确定。**

- 当工具只能补全一行代码时，人只需要判断这一行
- 当工具能改几十个文件、跑测试、开 PR、回应 review 时，人要设计边界、写清验收标准、管理权限、检查结果、处理失败，并为最终合并负责

部分开发任务可重新分配；是否替代岗位、增加监督或保留执行需独立测量。过去的核心能力是把需求翻译成代码；现在的核心能力，是把模糊目标翻译成 Agent 能执行、能验证、能回滚的任务系统。

## 开发者日常手感变化

过去写代码像砌墙，现在越来越多工作像带一个不稳定但学习很快的同事：

1. 先把任务讲清楚
2. 给它足够上下文
3. 告诉它哪些地方不能碰
4. 让它提出方案
5. 再看它改出的 diff

好的开发者会更在意 prompt 之外的东西：仓库结构是否清晰、测试是否可靠、错误信息是否可读、文档是否告诉 Agent 怎么运行、review 标准是否能被机器理解。

## 组织推论

- 没有测试、文档、清晰边界的团队，Agent 可能放大错误，也可能帮助发现问题
- 有良好模块化、可运行验证链路和明确贡献规范的团队，Agent 可能改善交付，仍需质量与成本验收
- 未来最稀缺的不是"会不会使用某个 AI 工具"，而是能否把模糊目标变成可执行任务、能否把成功交互沉淀为可复用规则、能否在 AI 方案里看出真正的风险

## 关键数据点

- Top 开发者画像包含独立工具作者、开源维护者、AI startup 创始人、云厂商/模型厂商工程师、研究者、工具作者和社区型项目维护者
- Agentic AI 226 个项目中，Coding Agent 相关 78 个、历史累计Star386万、2026年4月参与者14,019（可能重复或含自动化账号，非工作量/实际AI使用率）
- Coding Agent 三条路线: CLI-first（Claude Code、Codex）、IDE-first（Cursor）、cowork/cloud worker（Devin、OpenHands）

## 前提与局限性

- 框架假设开发者能清晰地将任务定义为 Agent 可执行的形式，但大量软件工作涉及模糊需求沟通、政治协商、隐性判断
- "定义层"工作本身难以完全形式化
- 分工模式在 coding 领域最清晰，迁移到其他知识工作领域需要更多验证

## 关联概念

- [[Human-Governor-Agent-Operator]] — 企业场景中的碳基-硅基分工
- [[Agentic-Engineering]] — 碳基定义者的核心工程实践
- [[Coding-Agents]] — 硅基执行者的具体形态
- [[Taste]] — 碳基定义者需要的核心能力
- [[Judgment]] — 在 AI 方案中识别风险的能力
- [[Agent-Infra]] — 支撑碳基-硅基分工的基础设施层
