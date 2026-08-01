---
type: entity
title: Decision-Centric-Architecture
aliases:
  - Decision-Centric Architecture
  - 决策中心架构
  - Decision-Centric Ontology
definition: "把企业的'决策'（而非仅数据）作为建模对象的软件架构：数据、逻辑、行动、安全四要素统一进单一语义系统，使 agent 与人类在同一套原语上探索、暂存、提交并审计决策"
created: 2026-07-30
updated: 2026-07-30
tags:
  - enterprise-ai
  - ontology
  - agentic-ai
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[Ontology]]"
  - "[[Ontology-Agent]]"
  - "[[Organization-as-Agent-Harness]]"
  - "[[Forward-Deployed-Engineer]]"
  - "[[Deployment-Product-Flywheel]]"
  - "[[Transparent-Tool-Handoff]]"
  - "[[Integration-Wall]]"
topics:
  - "[[Enterprise-Ontology-Application]]"
source_raw:
  - "[[20260730-palantir-ontology-connecting-agents-to-decisions]]"
  - "[[20260730-palantir-industry-ai-unified-namespace]]"
---

# Decision-Centric-Architecture（决策中心架构）

> [!definition] 定义
> **决策中心架构**主张传统数据架构只描述数据、不描述"决策"——不记录决策的上下文、候选选项与下游影响——因此无法承载需要学习与写回的操作型 AI。它要求把决策的四要素（data / logic / action / security）整合进单一语义系统，使 agent 与人类共用同一套决策原语。

## 与数据中心架构的区别

| 维度 | 数据中心架构 | 决策中心架构 |
|------|------------|------------|
| 建模对象 | 实体与事实（golden tables） | 实体 + 决策事件（含上下文、选项、commit） |
| 关键数据品质 | cleanliness（干净） | relevance（相关性，含决策数据） |
| 行动 | 在系统外部执行 | 作为 ontology 动词原生建模（nouns + verbs） |
| 学习燃料 | 历史事实 | end-to-end decision lineage |
| Agent 接口 | 检索文本（RAG） | 调用 data/logic/action 原语（tools 范式） |

## 四要素模型

- **Data**：所有模态统一为 objects/properties/links 的实时语义表示；额外捕获"决策数据"——决策上下文、被评估的选项、commit 后的下游影响。decision lineage 自动记录"何时、基于哪个数据版本、通过哪个 app"做出决策，是 agentic memory（working/episodic/semantic/procedural）的燃料。
- **Logic**：业务逻辑、ML 预测、优化与仿真模型统一为 logic binding 接口，agent 与人类以同一方式调用；tribal knowledge 通过持续生成新 functional encapsulation 沉淀。
- **Action**：actions 是 ontology 的"动词"，可被 stage 为 scenarios（沙盒化的 ontology 子集）供人类 review，commit 后写回 transactional systems/edge/custom apps；explore/stage/commit 三级权限原生建模，冲突决策与协作权限分级内置。
- **Security**：marking/purpose/role 三类策略叠加，在每次交互动态计算；tool 调用受同一套安全架构约束（runtime validation + 显式 authorization grants），日志访问由相同 primitives 治理。

## 关键机制

- **Scenario staging ≈ 操作数据的 Git 化**：explore/stage/commit 与 branch/PR/merge 同构——企业操作数据正在经历代码世界十年前的版本化革命（Palantir 的 Global Branching 即此隐喻的字面化）。
- **AI 闭环范围是可调刻度**：每个 agent 被视为"新员工"，默认只能 stage、须人工 review；凭 granular logging 选择哪些 trusted 流程可自动闭环，授权范围可外科手术式扩大/收缩。制造业版本将同一思想表述为五级自治标尺（manual → assisted → semi-automated → highly automated → fully autonomous）。
- **Decision lineage 数据飞轮**：全部决策事后可作 fine-tuning 数据与 agent prompting 原则——这是 [[Deployment-Product-Flywheel|部署-产品飞轮]] 在数据层的形态：FDE 回流的不仅是平台功能，还有决策语料。

## 关键数据点

- 四要素模型：data / logic / action / security 整合进单一语义系统（Palantir 提出）
- explore/stage/commit 三级权限原生建模，类比代码世界的 Git branching/PR/merge
- 制造业版本将自治分为五级：manual → assisted → semi-automated → highly automated → fully autonomous

## 前提与局限性

- **厂商立场**：该架构由 Palantir 提出并与其 AIP/Ontology 产品绑定，"必须单一系统整合四要素"含架构偏好；多系统联邦方案未必更差。
- **lineage 的双刃性**：decision lineage 既是学习资产也是最大的专有知识泄露面——与 [[Reverse-Information-Paradox|反向信息悖论]] 直接冲突，供应商托管的 lineage 等于制度化的 [[Alpha-Transfer|alpha 转移]]通道。
- **治理成本未定价**：action schema 治理、lineage 埋点与存储、动态安全策略的计算开销，在原始论述中均被略过。
- **适用域**：最适合高风险写回、强审计、多系统联动的操作型场景；纯分析型工作负载不需要决策中心架构。

## 关联概念

- [[Ontology]] — 决策中心架构的语义层载体；本概念为其"为何而建"的架构论证
- [[Ontology-Agent]] — 在决策原语上运行的 agent 形态
- [[Organization-as-Agent-Harness]] — 决策中心架构是该命题在企业数据层的实现
- [[Transparent-Tool-Handoff]] — logic binding 的工具化使系统级可解释性成为可能
- [[Forward-Deployed-Engineer]] — 将客户数据源/逻辑资产/行动系统接入 ontology 的角色
- [[Integration-Wall]] — 决策中心架构要穿越的工程约束
