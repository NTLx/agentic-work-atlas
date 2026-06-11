---
type: entity
title: Ontology-Agent
aliases:
  - Ontology Agent
  - 本体增强 Agent
  - Ontology-Enhanced Agent
definition: "把业务规则判定交给本体和推理工具的 Agent 架构，让 LLM 负责调度、解释和行动组织"
created: 2026-04-20
updated: 2026-05-25
tags:
  - AI-Agent
  - Enterprise-AI
  - Ontology
related_entities:
  - '[[Ontology]]'
  - '[[Enterprise-Ontology-Application]]'
source_raw:
  - '[[20260420-ontology-meets-agent-case-study]]'
  - '[[20260420-ontology-enterprise-ai-agent]]'
---

# Ontology-Agent（本体增强 Agent）

> [!definition] 定义
> 把业务规则判定交给本体和推理工具的 Agent 架构，让 LLM 负责调度、解释和行动组织

## 关键数据点

- **核心分工**：LLM 负责理解请求、选择工具、解释结果；[[Ontology]]、TBox 和推理机负责高风险业务规则判断。
- **运行闭环**：从数据库或业务系统取事实，映射成 ABox，调用 OWL 推理工具，读取分类结果，再由 Agent 组织回答或下一步动作。
- **典型工具栈**：业务数据库、ontology query tool、ontology reasoning tool、Owlready2 + HermiT 的开发期实现，或 GraphDB + SPARQL 的生产级语义服务。
- **工具选择原则**：日常明细查询走数据库；规则判定走本体推理；概念解释走本体定义；跨对象关系查询走知识图谱或 SPARQL。
- **关键收益**：把"能否发货"、"能否加急"、"是否特殊处理"这类判断从 LLM 内部迁移到可审计、可测试、可解释的外部语义层。

## 为什么重要

企业 Agent 的风险不只是回答错，而是在真实流程里错误解释规则。一个模型可能读到 `ALLOCATED` 就认为库存可用，但在不同系统中这个词可能分别表示原料锁定、产能排期或发货确认。Ontology Agent 的任务，就是把这种语义判断从语言模型直觉中拿出来。

在订单加急案例里，Agent 不直接凭自然语言判断是否加急，而是调用本体工具：先取得客户等级、订单、库存占用和质检事实，再由推理机判断订单是否属于 `ReadyToShipOrder` 和 `ExpediteEligibleOrder`。最终回答可以回溯到 TBox 规则和 ABox 事实。

这种架构让 Agent 更像企业工作系统的编排层，而不是全知判断者。它仍使用 LLM 的语言能力和上下文能力，但把关键的确定性判断交给可验证工具。

## 工具边界

| 任务类型 | 推荐工具 | 不推荐做法 |
|----------|----------|------------|
| 查订单明细 | 数据库查询工具 | 让 LLM 从本体里猜交易状态 |
| 判断是否满足规则 | 本体推理工具 | 把规则写进长 prompt |
| 查概念含义 | 本体概念查询 | 临场要求模型解释企业术语 |
| 查实体关系 | SPARQL / 知识图谱工具 | 让模型拼接不受控查询 |
| 发起流程动作 | 工作流 / 业务 API | 让推理机承担动作编排 |

这个边界能减少两类失败：一是模型把事实检索误当规则判断，二是团队把所有规则硬编码进 workflow，导致规则爆炸。

## 前提与局限性

- **本体前提**：已有足够稳定的 TBox，能表达关键业务概念、关系和约束。
- **事实前提**：Agent 能从系统中取得可靠事实，并正确映射成 ABox。事实错，推理就错。
- **工具前提**：推理、查询和数据库访问必须封装成受控工具，不能把底层权限完全交给模型。
- **性能边界**：注入事实再推理比普通查询更重，高频场景需要缓存、预计算或规则下沉。
- **表达边界**：OWL 推理适合分类和约束，涉及审批流程、时间窗口、外部服务调用和动作触发时，需要 workflow 或规则引擎配合。
- **组织成本**：Ontology Agent 的难点不只是技术，而是让业务、数据、工程共同维护一套可演化的语义契约。

## 关联概念

- [[Ontology]]：Ontology-Agent 的核心语义层
- TBox：规则定义来源
- ABox：运行时注入的事实数据
- OWL：本体语言
- HermiT：推理引擎
- Owlready2：Python 本体操作库
- GraphDB：生产环境语义存储与查询后端
- SPARQL：知识图谱和推理结果查询语言
- [[Enterprise-Ontology-Application]]：本体进入企业 Agent 的主题页
