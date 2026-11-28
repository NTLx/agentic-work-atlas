---
type: entity
title: Memory Architecture
aliases:
  - Memory Architecture
  - 记忆架构
  - Memory System
  - 记忆系统
definition: "管理LLM跨任务记忆的存储、检索、更新、授权与生命周期的工程架构；目标包括时效、正确性、可扩展性与安全。"
created: 2026-06-06
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - memory-system
  - context-engineering
  - architecture
related_entities:
  - "[[Dreaming]]"
  - "[[Memory-Synthesis]]"
  - "[[Memory-Summary-Page]]"
  - "[[Staleness-Problem]]"
  - "[[Multi-Layer-Memory]]"
  - "[[Three-Layer-Agent-Memory]]"
  - "[[Context-Engineering]]"
  - "[[OpenAI]]"
  - "[[Personal-AI-Assistant]]"
  - "[[Structured-Agent-Memory]]"
source_raw:
  - "[[20260604-openai-dreaming-memory]]"
  - "[[Agent Memory _ The 5-Layer Playbook.pdf]]"
---

# Memory Architecture（记忆架构）

> [!definition] 定义
> 管理LLM跨任务状态的存储、检索、更新、授权和生命周期的工程架构。OpenAI 2026-06发布将staleness、correctness、scalability作为设计挑战，不能认为这些问题已被解决。任务效用、隐私与安全恢复亦须独立验收。

## 核心设计维度

| 维度 | 问题与验收 |
|---|---|
| 信息类型 | 区分事实、偏好、事件、程序、推断和待办；避免把计划日期已过当成事件已发生 |
| 存储与组织 | 文件、结构化记录、向量索引、图及数据库可组合；按实际规模、成本、权限与查找需求选型 |
| 召回 | 按需加载、核验相关性、有效时间、来源与覆盖；活动上下文不是全部状态 |
| 生命周期 | 写入、合成、晋升、冲突处理、撤销、过期与修复；版本和访问权限分别管理 |
| 评估 | 测量任务正确性、约束遵循、时效、延迟、成本、正常知识保留与实际副作用 |

## 代表实现与证据

- Saved memories（2024历史形态）：会话内通过显式请求或强信号记录，跨会话使用。
- Dreaming V3（2026-06）：后台综合并提供记忆摘要；未公开内部索引、时间字段、调度或事务实现。摘要非完整状态，个性化设置也不同于数据训练授权。
- [[Three-Layer-Agent-Memory]]：个人Vault按画像、程序性经验、历史分层，按需加载；个人报告非普适架构或收益保证。
- [[Structured-Agent-Memory]]：按任务属性、适用条件及来源组织经验；与信息类型、生命周期及实际存储相互独立。
- [[Multi-Layer-Memory]]：其他分层视角；不要求与三层或五层一一映射。

## 从“存得下”到“能维护”

《[[Agent Memory _ The 5-Layer Playbook.pdf]]》按working/episodic/semantic/procedural/forgetting组织记忆。此前编译定位第2–8页，其中第4页晋升、第5–6页过期/替代/冲突、第7–8页agent loop；遗忘可作为横切生命周期控制，而非独立存储层。本轮仅回看已有Source Summary，未重开原PDF。独立汇编的TTL、晋升次数与效果数字不是通用默认值。高风险任务按风险、法规和保留策略确定验证与删除范围，不一律保留更久。

## 关键数据点

- [OpenAI 2026-06-04官方发布](https://openai.com/index/chatgpt-memory-dreaming/)评价跨会话相关信息、偏好/约束与时效，报告Free用户dreaming计算需求约降至原先1/5，非整体服务成本或全部套餐收益。未估算图表分数。
- [[20260729-memsecbench-memory-lifecycle]]：成功污染条件下，修复目标语义86.3%、保留所需正常记忆62.5%、同时满足56.1%（各配置宏平均，Forget独立分支）。受控实验非生产风险率。
- [[20260610-smsr-runtime-memory-provenance]]：认证来源不等于内容真实或授权；论文采样证书存在待核的聚合条件缺口，见来源页复核。
- [[20261014-langchain-deep-agents-context-memory]]：外置状态、可回查压缩、按需加载是厂商设计实例，需验收原文可访问性与恢复质量。

## 前提与局限性

以上为跨来源工程综合，不是统一标准或已实施架构。后台综合可能增加成本、产生摘要失真或过期判断；按需检索可能漏召回。不同模型、来源和访问范围影响结果。敏感信息仍可能进入记忆；依据实际权限、用途、删除与保留政策治理。2026-11-28回核OpenAI发布和帮助中心、相关论文关键章节及本地实践材料，未运行系统或独立评估效用。

**本库综合**：LLM WiKi现有Raw/Source Summary/Entity等层次已提供证据与解释分离的基础。应检验写入授权、来源独立性、真实召回、晋升与纠错传播，而不是先增加数据库、模型或层级。

## 关联概念

- [[Dreaming]]、[[Memory-Synthesis]]、[[Memory-Summary-Page]] — 综合与用户可见性。
- [[Staleness-Problem]] — 时间与实际状态。
- [[Three-Layer-Agent-Memory]]、[[Multi-Layer-Memory]]、[[Structured-Agent-Memory]] — 不同组织视角。
- [[Shared-Memory-Contamination]] — 记忆生命周期安全。
- [[Context-Engineering]]、[[Agent-Harness]] — 上下文与执行合同。
- [[Memex]]、[[Personal-AI-Assistant]]、[[OpenAI]] — 历史范式、产品场景和发布者。
