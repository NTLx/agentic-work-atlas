---
type: source-summary
title: "The layoffs will continue till we learn to use AI"
source_raw:
  - "[[The layoffs will continue till we learn to use AI]]"
created: 2026-05-24
updated: 2026-05-25
tags:
  - source-summary
  - layoffs
  - organizational-alignment
  - outcome-economics
---

# The layoffs will continue till we learn to use AI

## 编译摘要

### 1. 浓缩

- **核心结论1**: 所谓 AI layoffs 的核心不是“AI 直接替代某个员工”，而是企业已经增加了 AI 输入成本，却还没有把这些输入稳定转化为业务 outcome。
  - 关键证据: 作者用 Input、Output、Outcome 区分代码、功能和用户付费。AI 让代码输入暴增，PR/diff 数量可以上升 2 到 5 倍，但如果产品体验、收入和用户价值几乎不变，公司只是买了更多输入。
  - 成本证据: 文中估算部分工程师每天消耗约 `$100` Claude Code tokens，折合每年约 `$30`k；当 AI 预算快速增长而收入没有同步增长，裁员就成为抵消新增输入成本的粗暴办法。
- **核心结论2**: AI 暴露了大型组织长期隐藏的 alignment tax：代码变便宜后，真正卡住的是方向筛选、跨团队协调和共同假设。
  - 关键证据: 过去工程带宽有限，CEO 或 PM 的 10 个想法会被迫筛到 2 个；当 coding 变快，坏想法也更容易被做成 MVP。不同团队还可能各自生成互相冲突的版本，然后继续让 Claude 按自己的假设重写对方部分。
  - 关键机制: 写代码变快并不会自动让组织对齐变快。相反，它可能绕过早期辩论和筛选，让更多错误方向进入实现阶段。
- **核心结论3**: 裁员短期能同时减少 AI 支出和协调人数，但不解决组织债务；如果组织不会把 AI tokens 转成 outcome，裁员会周期性重演。
  - 关键证据: 作者承认大型组织天然存在 slack、冗余和 org debt，裁掉 10% 到 20% 的人可能短期让事情变快，因为阻塞者更少；但冗余会重新积累，alignment tax 也会在新结构中再生。
  - 对本库的意义: 这篇文章把 AI 裁员从“替代人力”问题改写为“输入成本、输出质量、组织对齐和 outcome 转换率”问题，适合接入 [[Input-Output-Outcome]] 与 [[Organizational-Shape-Moat]]。

### 2. 质疑

- **关于成本数据的质疑**: `$100`/天和 `$30`k/年的 token 成本是作者估算，未给出公司级账单、角色分布或模型使用结构。应把它当作单位经济提醒，而非稳定行业数据。
- **关于“代码是 input”的质疑**: 对大多数产品公司成立，但对开源库、代码平台、开发者工具或内部自动化系统，代码本身有时更接近 output。仍需根据交付物类型判断。
- **关于裁员效果的质疑**: 裁员可以减少协调节点，但也会移除上下文、系统记忆和备份能力。短期速度提升可能换来长期脆弱性。
- **关于 AI 使用能力的质疑**: 作者把问题归结为“还没学会用 AI”，但这不只是个人技能问题，也包括产品战略、组织结构、预算治理、评价指标和工作流重设计。

### 3. 对标

- **对标 [[Input-Output-Outcome]]**: 本文是该框架在 AI 成本问题上的清晰案例。AI 增加 input 不等于增加 outcome，组织必须测量从 tokens 到收入、留存、质量或客户价值的转换率。
- **对标 [[AI-Capability-Gap]]**: 模型能力与组织吸收能力之间的缺口，会表现为代码量上升、会议更多、方向更乱、产出没有被用户感知。
- **对标 [[Organizational-Shape-Moat]]**: AI 时代真正的护城河不是谁生成代码更多，而是谁能更快筛掉坏想法、对齐假设、把好方向转成结果。
- **可迁移场景**: coding agent 预算治理、AI 工具采购 ROI、组织重组、团队绩效评估、软件交付指标设计。关键问题应从“用了多少 AI”改成“AI 是否改变了 outcome”。

### 关联概念

- [[Input-Output-Outcome]]
- [[AI-Capability-Gap]]
- [[Organizational-Shape-Moat]]
- [[Alignment-Tax]]
- [[Allocation-Economy]]
- [[AI-Ready-Organization]]
