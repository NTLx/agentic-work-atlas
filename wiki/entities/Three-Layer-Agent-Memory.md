---
type: entity
title: "三层 Agent 记忆"
aliases:
  - Three-Layer Agent Memory
  - L1 L2 L3 记忆
  - 三层记忆架构
definition: "个人Agent记忆按持久画像、程序性经验及历史事件组织，并按需加载的实践模式；有助降低混杂风险但不保证消除记忆错误或固定成本收益。"
created: 2026-05-29
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - agent-memory
  - context-engineering
  - claude-code
related_entities:
  - "[[Multi-Layer-Memory]]"
  - "[[Context-Engineering]]"
  - "[[CLAUDE-md]]"
  - "[[Agent-Harness]]"
  - "[[Capability-Map]]"
source_raw:
  - "[[20260526-obsidian-claude-code-brain]]"
---

# 三层 Agent 记忆

> [!definition] 定义
> 李祥瑞2026-05-26 Obsidian/Claude Code实践中将Agent记忆区分为L1持久画像、L2程序性经验、L3历史检索，以便控制工作集和分离不同信息类型。作者称受到hermes-agent启发，未在本轮核查Hermes原版架构或术语来源，不将三层划分当作其正式规范。

## 三层结构（作者案例）

| 层级 | 目的 | 存储及加载 |
|---|---|---|
| L1 持久画像 | 用户是谁、稳定背景 | user.md，按需读取；更新节奏视实际变化 |
| L2 程序性经验 | 可复用方法、约束与经验 | memory.md索引及主题文件；命中后读取 |
| L3 历史检索 | 过去发生的事 | 日志、归档和检索；作者还在开班时按当前话题召回，不是仅用户主动请求才读取 |

事实、偏好、方法及事件混杂可能导致错误更新；分层本身不能消除错误、越权、过期及错误晋升。遵循[[Shared-Memory-Contamination]]的写入、核验、撤销与正常知识保留边界。

## 关键数据点

- 作者Raw §01自报：单文件3000余行，改造前读取memory.md约3万Token；改造后启动真正读入内容不到3000 Token。是个人使用环境下的自述，非同模型任务匹配的计费或总体成本测试；不外推10倍普适收益。
- L2按标题和一句话提示索引；L3使用OpenViking语义索引。未复查工具发布日期与完整实现。
- §02开班包含文件监听和按话题记忆召回；收班五步包括经验记录、事实流水、知识编译、文件统计与交接自检。作者描述一次历史操作经验在三周后复用成功，未提供对照或总体成功率。
- 语义去重区分同义、补充及新判断；需保护条件、来源和版本，误合并可能丢失有效知识。保留可回滚记录。

## 工程综合

任务历史是证据，不是自动授权；只有明确适用、可核实、经必要回归的经验才可晋升为操作规则。历史交接记录应区分已完成、待办、决定、证据与未解决事项；按风险验证新的会话是否能恢复正确状态。不能仅凭成功次数、读入Token少或完成交接步骤认定效果。与LLM WiKi已有分层及行动台账相容，不新增文件结构或强制自动结束协议。

## 前提与局限性

2026-11-28回读本地Raw L1–160的入口结构、三层及交班部分（原文后续章节留后轮完整消化），未复查微信原网页、Hermes实现、作者脚本或复现成本。个人Vault不等于企业多人、权限、多租户架构；长期画像及程序可能变化，需来源、实际授权、版本及风险重验。

## 关联概念

- [[Multi-Layer-Memory]] — 不同层级分类。
- [[Memory-Architecture]]、[[Context-Engineering]] — 存储、生命周期及工作集。
- [[CLAUDE-md]]、[[Agent-Harness]]、[[Capability-Map]] — 规则和工具的按需发现。
- [[Knowledge-Compilation]] — 经验提炼与验证。
- [[Shared-Memory-Contamination]] — 事实纠正与持久状态治理。
