---
type: entity
title: UModel
aliases:
  - UModel
  - 统一可观测模型
definition: "阿里云可观测团队基于本体论思想构建的 IT 世界统一建模框架，以实体为中心、以图为核心，推动可观测体系从面向数据转向面向对象"
created: 2026-06-13
updated: 2026-06-13
tags:
  - ontology
  - observability
  - aiops
related_entities:
  - "[[Ontology]]"
  - "[[Knowledge-Graph]]"
  - "[[Agent-Harness]]"
source_raw:
  - "[[20260613-ontology-for-agent-optimization]]"
  - "[[20260613-ontology-tokenmaxxing]]"
  - "[[20260613-aliyun-agent-infra-constraint-infrastructure]]"
---

# UModel（统一可观测模型）

> [!definition] 定义
> 阿里云可观测团队基于本体论思想构建的 IT 世界统一建模框架，以实体为中心、以图为核心，推动可观测体系从面向数据转向面向对象。

## 关键数据点

- **发布时间**: 2025 年发布，已上线云监控 2.0 并开源
- **发展历程**: 2019 年开始可观测数据建模，历经数据标准化、实体与关联、知识表达、行动能力四个阶段
- **核心转变**: 从"我有哪些数据"（日志、指标、链路、事件各自独立）转向"我有哪些实体"（数据绑定在实体上，关系显式定义在图谱中）
- **Token 效率**: 提供 Ontology 可避免多轮元数据查询、字段映射推断、查询语法纠错三类 Token 开销

## 建模体系

以图为中心，定义三种核心节点和四种核心关系：

**核心节点**:
- EntitySet — 可观测实体集合（主键、属性、状态）
- TelemetryDataSet — 可观测数据通用表示（LogSet、MetricSet、TraceSet、EventSet）
- Storage — 存储抽象
- Explorer — 可视化抽象

**核心关系**:
- EntitySetLink — 实体间关系（调用、部署、依赖、包含、运行在）
- DataLink — 数据与实体的关联
- StorageLink — 建模抽象与存储的关联
- ExplorerLink — 数据与可视化的关联

## 知识分层设计

| 层次 | 内容 | 特点 |
|------|------|------|
| 通用知识库 | 跨实体的文档和 FAQ | 通用但缺乏上下文 |
| Agent Rules | 告诉 Agent"如何做"的指令 | 行为偏好 |
| UModel Knowledge | 与实体强耦合的 SOP、Runbook | 情景化，精确上下文 |

关键洞察：运维知识的价值高度依赖它所描述的实体是谁。"数据库慢查询排查指南"绑定到具体实体时，从普通文档变成精确行动指南。

## 前提与局限性

- **前提**: 依赖阿里云生态的数据模型和查询语言（PromQL、SPL 等）
- **生态绑定**: 迁移到其他云或混合环境时本体层适配成本未讨论
- **维护成本**: 实体拓扑每天变化，绑定到实体的知识如何保持同步是开放问题

## 关联概念

- [[Ontology]] — UModel 是本体论在运维领域的具体实现
- [[Knowledge-Graph]] — UModel 以图为中心的建模与知识图谱技术密切相关
- [[Agent-Harness]] — UModel 为 AIOps Agent 提供结构化上下文，是 Harness 的知识基础设施
- [[Constraint-Infrastructure]] — 约束基建的效果观测层依赖 UModel 提供拓扑感知的根因定位能力
