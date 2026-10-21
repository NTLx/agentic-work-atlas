---
type: source-summary
title: "How Genie Ontology powers product development at Databricks"
canonical_url: "https://www.databricks.com/blog/how-genie-ontology-powers-product-development-databricks"
raw_state: index
original_raw_file: "raw/20261005-databricks-genie-ontology-product-development.md"
original_body_sha256: "8f112a1e40e1241f21118e131f16ace15c4758f05773dd22293a26118efc6761"
indexed_at: "2026-10-21T12:40:02+08:00"
created: 2026-10-21
updated: 2026-10-21
tags:
  - source-summary
  - ontology
  - enterprise-AI
  - product-development
evidence_level: low
claim_type: mixed
source_locator:
  - "Genie Ontology 与 OntoRank 机制：开篇第 3–4 段"
  - "资产选择、跨系统搜索、SQL 与权限：Genie finds the right data"
  - "引用与 ontology snippet provenance：Review Genie’s citations"
  - "定时任务与 Agent 分享：Schedule the workflow; Turn the conversation into a shareable agent"
  - "通用 Agent 时间/token 主张：Genie finds the right data 后半部分；无独立 benchmark"
---

# How Genie Ontology powers product development at Databricks

## 编译摘要

### 1. 浓缩

- **核心结论1**：Genie Ontology 在产品经理的实际工作流中，把 Unity Catalog 中人工治理、认证的核心语义，与从组织 dashboards、documents、queries、notebooks 和连接应用中学习的组织上下文组合起来；OntoRank 使用 certification、usage、authorship 等信号衡量权威性，产品演示称 Genie 优先采用 certified assets。
  - **关键证据**：原文开篇说明 curated context 与 learned knowledge 的组合及 OntoRank 信号；`Genie finds the right data` 描述先找数据资产和 curated Pages，再查看 ontology snippets，并举 certified weekly active users metric view 为例。
- **核心结论2**：该工作流把上下文检索与实时计算放在同一交互中：先跨受治理数据资产、Google Drive 与 Jira 搜索，再对 usage tables 执行 SQL；回答引用和可展开的 ontology snippets 展示定义、来源、作者及 authority score，使用户能检查上下文从何而来。上下文按用户权限过滤。
  - **关键证据**：`Genie finds the right data` 描述 MCP 搜索 live Google Drive/Jira 后运行 SQL；`Review Genie’s citations` 描述 metric views、Pages、snippet 定义/来源/作者/authority score；前文明确 permission-aware。
- **核心结论3**：一次产品分析交互可以延展为预测、定时任务和可分享的 Genie Agent，使临时分析成为团队可重复调用的工作流。
  - **关键证据**：`Ask a follow-up question and forecast the trend`、`Schedule the workflow`、`Turn the conversation into a shareable agent` 展示追问、forecast、schedule 和分享 Agent。

### 2. 质疑

- **关于治理语义与学习上下文的组合**：这是 Databricks 对自身产品机制的描述；文章展示了 PM 的单一内部用例，没有给出 ontology snippets 的准确率、错误率、覆盖率或权威排序校准结果。认证优先能约束已治理的核心指标，但不保证学习到的长尾上下文无误。
- **关于权限与 provenance**：文章说明访问会遵循 Unity Catalog 和连接来源权限，并展示 snippets 的出处和作者信息；未提供权限边界测试、跨连接器一致性或 provenance 信息完整率的独立审计结果。可见来源有助于检查，不等同于来源本身正确。
- **关于 general-purpose agent 的时间与 token**：作者称通用 Agent 可能需要爬 schema、采样表、读文档并重复查询来弥补业务语义缺失，因而消耗时间和 tokens；文章没有独立 benchmark、对照实验、任务分布或量化结果，不能据此断言 Genie Ontology 已被证明带来性能因果提升。
- **关于可调度和可分享工作流**：演示说明同一产品可把分析转成 schedule 或共享 Agent，但未评估后续维护、数据/定义漂移、Agent 行为一致性及团队复用效果。

### 3. 对标

- **相对既有 Ontology 编译**：与 [[20260901-databricks-genie-ontology-data-stack]] 已覆盖的语义资产和治理成熟度不同，本篇增量在于运行时产品体验：人工认证语义与自动学习的组织上下文共同参与检索，用户可见来源与 authority，并在一个对话里连接文档/工单搜索和 live SQL。
- **跨域关联（综合判断）**：这体现了“上下文准备”与“工作流执行”在产品交互中的合流：Ontology 给出组织可理解的候选资产和出处，搜索补充变化中的协作记录，SQL 提供当前数据计算，随后 schedule/分享把一次性问答变成可复用入口。它可作为企业 Agent 产品设计的机制假设；该单一厂商案例不能证明通用效果。

## 证据定位

- 治理与学习上下文、OntoRank 信号：原文开篇第 3–4 段（`Genie Ontology` / `OntoRank`）。
- 资产选择、搜索与 SQL、权限：`Genie finds the right data`。
- 引用、snippet provenance 与权威性：`Review Genie’s citations`。
- 工作流定时与分享：`Schedule the workflow`、`Turn the conversation into a shareable agent`。
- 时间/token 主张及其限制：`Genie finds the right data` 后半部分；文章未给独立 benchmark。

### 关联概念

- [[Enterprise-Ontology-Application]]
- [[Ontology]]
- [[20260901-databricks-genie-ontology-data-stack]]
