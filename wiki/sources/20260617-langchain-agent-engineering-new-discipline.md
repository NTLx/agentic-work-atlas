---
type: source-summary
title: "Agent Engineering: A New Discipline"
source_raw:
  - "[[20260617-langchain-agent-engineering-new-discipline]]"
created: 2026-06-17
updated: 2026-06-17
tags:
  - source-summary
  - agentic-engineering
  - agent-harness
  - production-engineering
evidence_level: medium
claim_type: mixed
---

# Agent Engineering: A New Discipline

## 编译摘要

### 1. 浓缩
- **核心结论1**: Agent 工程是将非确定性 LLM 系统迭代为可靠生产体验的新学科，核心循环是 build-test-ship-observe-refine-repeat
  - 关键证据: Clay、Vanta、LinkedIn、Cloudflare 等公司已在生产中部署 agent；ship 不是终点而是获取洞察的手段
- **核心结论2**: Agent 工程需要三技能组合——产品思维（prompt 编写、任务定义、eval 设计）、工程（工具开发、UI/UX、持久执行运行时）、数据科学（性能度量、错误分析）
  - 关键证据: 软件工程师写 prompt 和工具、PM 定义范围、数据科学家度量可靠性；团队快速迭代，角色间频繁交接
- **核心结论3**: Agent 的"每个输入都是边缘案例"和"工作不是二元的"特征使传统测试方法失效，生产环境是主要教师
  - 关键证据: 99.99% uptime 的 agent 可能仍然行为异常；小幅 prompt 调整可导致巨大行为偏移；成功团队将改进周期从季度缩短到天

### 2. 质疑
- **关于"三技能组合"的质疑**: 产品/工程/数据科学的划分是否过于理想化？大多数团队可能无法同时具备这三种能力；文中提到的公司（Clay、Vanta 等）均为资金充足的初创企业
- **关于"生产即教师"的质疑**: 在高风险领域（医疗、法律、金融），"ship to learn" 可能导致严重后果；文章未讨论如何在安全边界内进行生产学习
- **关于证据强度的质疑**: 文章主要是框架性描述，缺少量化数据（成功率、错误率、ROI）；案例以成功公司为主，缺乏失败案例分析

### 3. 对标
- **Agentic-Engineering**: 本文将 agentic engineering 定义为独立学科，与 [[Agentic-Engineering]] 概念一致但更侧重组织实践而非技术架构
- **Agent-Harness**: 三技能组合（产品/工程/数据科学）可视为构建 [[Agent-Harness]] 的组织能力框架
- **Compound-Engineering**: build-ship-observe-refine 循环是 [[Compound-Engineering]] 复利循环在 agent 领域的具体表现
- **Verifiable-Agent-Engineering**: 文章强调 eval 和 trace 的重要性，但未深入讨论可验证性标准，与 [[Verifiable-Agent-Engineering]] 形成互补

### 关联概念
- [[Agentic-Engineering]]
- [[Agent-Harness]]
- [[Compound-Engineering]]
- [[Verifiable-Agent-Engineering]]
