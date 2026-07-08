---
type: entity
title: Agentic Speculation
aliases:
  - Agentic Speculation
  - Agent 投机探索
  - Agentic Query Speculation
definition: "Agent 与数据系统交互的典型模式：高吞吐、异构的查询流，涵盖 schema 探索、列级试探、部分到完整的查询构造。多 agent 并发时 80-90% 的子计划重复，但冗余提升成功率。"
created: 2026-07-08
updated: 2026-07-08
tags:
  - agentic-engineering
  - data-systems
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[Agent-Infra]]"
  - "[[Agent-Harness]]"
  - "[[Agentic-Workflow-Token-Efficiency]]"
  - "[[Agent-Ergonomics]]"
source_raw:
  - "[[20260707-intelligence-is-free-data-systems-for-of-by-agents]]"
---

# Agentic-Speculation（Agent 投机探索）

> [!definition] 定义
> **Agentic Speculation** 是 agent 与数据系统交互的典型模式：一个高吞吐、异构的查询流，涵盖 schema 自省、列级探索、从部分到完整的查询构造。多个 agent 各自探索假设空间的一部分，单个用户请求可触发数千条 SQL 查询。

## 核心特征

### 与人类查询的本质区别

| 维度 | 人类/BI 工具 | Agent |
|------|-------------|-------|
| 查询模式 | 目标导向、逐个查询 | 假设空间探索、组合搜索 |
| 单次请求查询量 | 1-10 | 数百到数千 |
| 子计划重复率 | 低（有意设计） | 80-90%（并行探索的副产品） |
| 容错能力 | 期望精确结果 | 可接受近似结果 |
| 反馈形式 | 结构化表格 | 任何文本形式 |

### 冗余的二重性

在 text-to-SQL 基准测试中，多 agent 尝试同一任务时：
- 只有 **10-20%** 的子计划是不同的
- **80-90%** 的子查询执行重复工作
- 但任务成功率**随尝试次数显著增加**

> [!important] 冗余是探索策略，不是浪费
> 类比生物系统的冗余探索（免疫系统的多克隆筛选、神经可塑性的突触冗余）：表面的"浪费"实际上是提高成功率的并行搜索策略。数据系统需要**消化冗余**而非**消除冗余**。

## 数据系统的优化方向

Berkeley AI Research 提出五个方向，将 agentic speculation 的"浪费"转化为效率：

### 1. 子计划复用（Sub-plan Reuse）

借鉴数十年历史的 multi-query optimization 和 shared scans 文献，在重叠子计划间复用结果。但关键区别：传统 MQO 优化的是人类有意设计的查询重叠，agentic speculation 的重叠是 agent 并行探索的随机副产品。

### 2. 近似查询处理（Satisficing）

返回对 agent "足够好"的近似答案（Approximate Query Processing），让 agent 基于近似结果决定是否深入。Agent 的容错能力使 AQP 从"可接受的妥协"变成"最优策略"。

### 3. 流式中间结果

将中间算子的结果流式传送给 agent，让其决定是否继续查看完整结果。这利用了 agent 的推理能力来做"早停"判断——人类 BI 工具不具备这种能力。

### 4. 批量查询 + Jinja 宏接口

Agent 不再逐条发 SQL，而是提交带近似要求的查询批次。使用 DBT 风格的 Jinja 宏提供循环原语，让 agent 描述搜索空间而非枚举每条查询。

### 5. 主动数据系统（Proactive Data Systems）

数据系统从被动执行器变为主动引导者：
- 提供相关查询的结果（agent 没问但可能有用的）
- 在执行昂贵查询前先提供延迟估计
- 预先准备物化视图和虚拟视图作为 agent 上下文
- 利用 agent 能接受任意文本反馈的能力（不限于 SQL 结果格式）

## 关键数据点

| 指标 | 数据 |
|------|------|
| 单次用户请求触发查询量 | 数百到数千条 SQL |
| 子计划不同比例 | 10-20%（text-to-SQL 基准） |
| 子查询重复率 | 80-90% |
| 成功率与尝试次数关系 | 正相关（冗余有益） |
| 推理成本下降速度 | 9x-900x/年（中位数 50x） |

## 前提与局限性

- 80-90% 重复率数据来自 text-to-SQL 基准，复杂分析任务（根因分析、队列分析）的重复模式可能不同
- "消化冗余"的优化策略（MQO、AQP）假设冗余可被高效识别——在语法不同但语义等价的查询间，识别成本可能很高
- 主动数据系统需要数据系统理解 agent 的意图——这本身是一个未解决的问题

## 关联概念

- [[Agent-Infra]] — agentic speculation 要求数据系统作为 agent infra 的新组件
- [[Agent-Harness]] — harness 需要管理 agent 与数据系统的交互模式
- [[Agentic-Workflow-Token-Efficiency]] — 减少冗余查询可直接降低 token 消费
- [[Agent-Ergonomics]] — 数据系统的接口设计应以 agent 为中心
