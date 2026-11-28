---
type: entity
title: "能力地图"
aliases:
  - Capability Map
  - 能力地图反向索引
  - reference_local_capabilities
definition: "以任务场景为入口组织工具、能力、适用环境与调用约束的可维护索引；用于减少重复发现成本，不替代权限、版本及实际效果核验。"
created: 2026-05-29
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - tool-use
  - context-engineering
  - claude-code
related_entities:
  - "[[Agent-Harness]]"
  - "[[Three-Layer-Agent-Memory]]"
  - "[[Tool-Use-Architecture]]"
  - "[[Agentic-Workflow-Token-Efficiency]]"
source_raw:
  - "[[20260526-obsidian-claude-code-brain]]"
---

# 能力地图

> [!definition] 定义
> 按任务场景反向索引工具或工作流。李祥瑞2026-05-26个人Vault实践将其作为发现本地工具的入口；与原生工具发现、按需文档、技能及权限控制可组合。

## 核心设计

每项能力应能回答：任务匹配什么工具、在哪个环境可用、依赖/版本与权限是什么、如何验收成功。优先原生工具及现成合同，只有能力确实缺失或不匹配时再探索其他方案；索引不是授权凭证，也不能取代实际工具描述或当前环境检查。

| 场景 | 索引用途 |
|---|---|
| 检索知识 | 指向适用的查询入口和范围 |
| 执行重复任务 | 指向已验证的工具或技能 |
| 调用外部系统 | 指向真实接口、身份和权限条件 |
| 结果验收 | 指向实际终态、日志或回读方法 |

## 关键数据点

- 本地Raw [[20260526-obsidian-claude-code-brain]] §04作者自述：发送飞书群消息的探索式流程约5分钟、5000+ Token，查表式约2秒、200 Token。若直接按其数字比较，时间约150倍、Token约25倍或更多；不同于旧条目将两者均称25倍。单一作者的轶事，没有匹配对照、计费详情或实际日志，本轮不将其作为可复现性能数据。
- 原文描述reference_local_capabilities.md按场景组织，发现遗漏时提示更新；不包含旧条目所称20→200行或上百个命令行入口的可核依据，撤出量化断言。
- 原文的禁止which/--help是特定环境规则；实际不确定命令时核对帮助、版本及官方文档更可靠。

## 前提与局限性

工具变化可能导致索引失效；更新需验证真实可用性，不能仅复制命令。静态索引不等于自动获得能力、权限或成功结果。多环境需明确作用域，维护成本应与避免的发现成本比较。2026-11-28回读本地Raw全部246行，未复查原始公众号页面、运行脚本或重现计费。

**本库综合**：先查原生工具能力及现有适用索引；若需要共享索引，保留真实接口和验收条件，避免再建与实际注册工具重复的管理层。本轮不新增系统。

## 关联概念

- [[Agent-Harness]]、[[Tool-Use-Architecture]] — 工具发现及执行合同。
- [[Agentic-Workflow-Token-Efficiency]] — 重复发现成本和效用。
- [[Three-Layer-Agent-Memory]]、[[Skill-Internalization]] — 经验与工作流复用。
