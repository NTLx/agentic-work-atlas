---
type: entity
title: Agentic Speculation
aliases:
  - Agentic Speculation
  - Agent 投机探索
  - Agentic Query Speculation
definition: "Agent 与数据系统交互的典型模式：高吞吐、异构的查询流，涵盖 schema 探索、列级试探、部分到完整的查询构造。BAIR 报告特定 text-to-SQL 实验子计划高度重叠，增加尝试与成功率改善同时出现；不代表所有冗余有益。"
created: 2026-07-08
updated: 2026-11-28
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
> **Agentic Speculation** 是 agent 与数据系统交互的典型模式：一个高吞吐、异构的查询流，涵盖 schema 自省、列级探索、从部分到完整的查询构造。多个 agent 各自探索假设空间的一部分，作者提出某些多 Agent 场景单请求可能触发数千 SQL，非普遍观测分布。

## 核心特征

### 候选工作负载差异（非人机固定属性）

| 维度 | 人类/BI 工具 | Agent |
|------|-------------|-------|
| 查询模式 | 目标导向、逐个查询 | 假设空间探索、组合搜索 |
| 单次请求查询量 | 依工作负载 | 作者举例可能数千；无代表性分布 |
| 子计划重复率 | 低（有意设计） | 80-90%（并行探索的副产品） |
| 容错能力 | 依任务精度 | 探索阶段可容许经标注近似；终态验收另定 |
| 反馈形式 | 结构化表格 | 任何文本形式 |

### 冗余的二重性

在 text-to-SQL 基准测试中，多 agent 尝试同一任务时：
- 只有 **10-20%** 的子计划是不同的
- **80-90%** 的子查询执行重复工作
- 作者报告更多尝试对应较高成功率；原文未披露该实验的样本、详细协议或效应量

> [!important] 区分有价值的探索与重复计算
> 类比生物系统的冗余探索（免疫系统的多克隆筛选、神经可塑性的突触冗余）：并行探索可能提高成功率，重复计算本身未必有价值。设计候选是保留有价值的探索分支、合并可安全复用的计算；不能推导重复执行本身造成成功。

## 数据系统的优化方向

Berkeley AI Research 提出五个方向，将 agentic speculation 的"浪费"转化为效率：

### 1. 子计划复用（Sub-plan Reuse）

借鉴数十年历史的 multi-query optimization 和 shared scans 文献，在重叠子计划间复用结果。但关键区别：传统 MQO 优化的是人类有意设计的查询重叠，agentic speculation 的重叠是 agent 并行探索的随机副产品。

### 2. 近似查询处理（Satisficing）

返回对 agent "足够好"的近似答案（Approximate Query Processing），让 agent 基于近似结果决定是否深入。AQP 仅适合误差可接受且有界的探索，不替代最终精确查询或高风险决策。

### 3. 流式中间结果

将中间算子的结果流式传送给 agent，让其决定是否继续查看完整结果。这利用了 agent 的推理能力来做"早停"判断——人类工具也可利用流式反馈和早停，收益需实测。

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
| 单次用户请求触发查询量 | 作者举例可能数千，非一般分布 |
| 子计划不同比例 | 10-20%（text-to-SQL 基准） |
| 子查询重复率 | 80-90% |
| 成功率与尝试次数关系 | 作者报告尝试次数增加对应成功率改善，因果未隔离 |
| 推理成本下降速度 | BAIR 转述历史能力匹配价格估算，非当前价格或总成本预测 |

## 前提与局限性

- 原文未给出该实验的详细可复核方法；80-90% 重复率报告来自 text-to-SQL 基准，复杂分析任务（根因分析、队列分析）的重复模式可能不同
- "消化冗余"的优化策略（MQO、AQP）假设冗余可被高效识别——在语法不同但语义等价的查询间，识别成本可能很高；复用须匹配参数、数据版本、权限、事务快照及精度要求，禁止把有副作用的操作视为可重复只读查询
- 主动数据系统需要数据系统理解 agent 的意图——这本身是一个未解决的问题

## 关联概念

- [[Agent-Infra]] — agentic speculation 要求数据系统作为 agent infra 的新组件
- [[Agent-Harness]] — harness 需要管理 agent 与数据系统的交互模式
- [[Agentic-Workflow-Token-Efficiency]] — 减少冗余查询可直接降低 token 消费
- [[Agent-Ergonomics]] — 数据系统的接口设计应以 agent 为中心
