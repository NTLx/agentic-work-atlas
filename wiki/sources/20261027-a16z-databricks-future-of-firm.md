---
type: source-summary
title: Databricks & the Future of the Firm
canonical_url: https://www.a16z.news/p/databricks-and-the-future-of-the
raw_state: index
original_raw_file: "20261027-a16z-databricks-future-of-firm.md"
original_body_sha256: "61385594619b086404b8559104ad8d4fdb0cf34fde688e6e282784218029819e"
indexed_at: "2026-11-26T12:31:43+08:00"
author: Ben Horowitz, Michael McGuiness
published: '2026-10-27'
created: '2026-11-26'
updated: '2026-11-26'
tags:
- source-summary
- organization
- AI
- knowledge-management
evidence_level: low
claim_type: mixed
source_locator:
- From Spark to Agents
- A System of Record for Agents
- The Nature of the Firm
- The Sovereign Firm
---

# Databricks & the Future of the Firm

> **原文保留边界**：来源为公开网页，按 canonical URL 与章节定位结算为可恢复索引（raw_state: index）。Registry 哈希对应临时来源登记摘录（非全文），不是原网页正文或全文哈希；原文需按来源链接回查。读取与结算日期：2026-11-26。

## 编译摘要

### 1. 浓缩

- **基础设施与组织边界的关联。** 作者从 Spark、Lakehouse、Lakebase 到 Agents 解释数据平台如何支持分析和操作状态。Lakebase 的分支能力与计算/存储分离被用于说明 Agent 可隔离试验；文中宣称 Databricks 超过 70 亿美元 revenue run rate、同比 80%，每天 Agent 启动超过 1700 万数据库。这些是投资机构文章中的经营叙述，非独立审计，也不等于生产任务完成数量。定位：From Spark to Agents / opening。
- **Agent System of Record 不只是一张业务表。** 文中提出企业需为 Agent 提供对象语义、关系、权威数据来源、执行权限、预算、trace 及任务评测。用 Coase 的交易成本和 Simon 的共享记录解释状态集中如何支持分布式决策。定位：A System of Record / The Nature of the Firm。
- **企业的学习资产应可跨模型保留。** 两家银行的假设案例对比仅保存最终决策与同时保存依据、人工覆盖、成败结果和修正策略。作者主张模型可替换，企业的定义、权限、评测、例外与历史应保有。随着执行自动化，更多专业人员承担任务定义、委托、审查及流程改进，而不必都成为传统人员经理。定位：The Sovereign Firm。

### 2. 质疑

作者为早期投资人，Databricks 为被投企业；厂商架构、客户案例和商业数据不可视为独立证明。数据库分支能力不等于隔离所有应用副作用，也不保证跨系统事务一致。共享记录的语义可能不正确、不及时或受权限限制；分布式执行仍需要冲突控制与审计。减少信息转发不等于管理职能整体消失。关于 AGI、未来劳动力和任务长度的预测不当作确定事实。记录知识也不必然成为护城河，关键在于后续决策收益与复用质量。

### 3. 对标

- [[Organization-as-Agent-Harness]]、[[Enterprise-Ontology-Application]]：以既有权威系统为基础区分语义定义、交易状态、授权、结果回执和历史评价；共享状态支持分散行动，不默认给每个 Agent 全部数据权限。
- [[Agent-Knowledge-Management]]：将业务经验、评测和例外作为模型无关的长期资产；不让 Wiki 取代 CRM、LIMS、ERP 或 Broker 的权威业务状态。事实源指针与知识推断分离。
- [[AI-Labor-Bottleneck-Shift]]：测信息等待与协调成本、错误决策率、独立审查成本、最终业务结果；不以查询量、数据库数、Agent 数或层级裁撤为价值指标。

## 前提与局限性

此为投资机构战略文章而非独立的 Databricks 产品测试或经济学实证研究。商业数据、客户案例、技术能力均以原文报告时点为限；未独立复核厂商财务和技术实现。

## 关联概念

- [[Organization-as-Agent-Harness]]
- [[Enterprise-Ontology-Application]]
- [[AI-Labor-Bottleneck-Shift]]
- [[Agent-Knowledge-Management]]
