---
type: entity
title: "能力地图"
aliases:
  - Capability Map
  - 能力地图反向索引
  - reference_local_capabilities
definition: "按'我要做什么'（场景）而非工具名组织本地工具链的反向索引表，让 Agent 查表即用而非摸索式探索，将工具调用从 5000+ token 降到 200 token"
created: 2026-05-29
updated: 2026-05-29
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

> [!definition] 定义
> 按"我要做什么"（场景）而非工具名组织本地工具链的反向索引表，让 Agent 查表即用而非摸索式探索，将工具调用从 5000+ token 降到 200 token。

## 核心设计

能力地图的组织方式不是"我有什么工具"（正向索引），而是"我要做什么 → 用哪个工具最省事"（反向索引）。

| 我要做什么 | 用哪个工具 |
|-----------|----------|
| 飞书群消息 | `lark-cli im +messages-send --chat <id> --text "..."` |
| 搜索 Vault 笔记 | `obsidian_bridge.py search query="..." limit=10` |
| 生成图片 | `seedream "prompt"` |
| 发公众号到飞书 | `lark-cli` + 两阶段图片处理 |

## 对比：有无能力地图

|  | 没有能力地图 | 有能力地图 |
|---|------------|----------|
| 耗时 | 5 分钟 | 2 秒 |
| Token | 5000+ | 200 |
| 过程 | which → pip list → 翻目录 → 找 OpenAPI → 写代码 | 翻到对应行，直接抄命令 |
| 结果 | 可能还要调签名 | 消息已发 |

这个差距乘以一天几十次工具调用，乘以一个月，就是几十万 token 和几个小时的等待。

## 更深层价值：保住注意力预算

省下来的不只是 token，还有 Agent 的"判断力质量"。一个被反复在底层细节上消耗的 Agent，到了真正需要它动脑子的时候已经没劲儿了。能力地图保住的是它的注意力预算。

## 活地图

能力地图本身是活的。Agent 每次发现地图里没有但又用上了的工具，或发现命令已过时，会主动提"能力地图需要更新这条"。

CLAUDE.md 规则：执行任务前必查能力地图；发现地图缺失或过时，当场更新。

作者实测从最初 20+ 行增长到 200+ 行，每多一行，下一次类似任务就少烧一次摸索的 token。

## 关键数据点

- 发飞书群消息：无能力地图 5 分钟 5000+ token → 有能力地图 2 秒 200 token（25x 提速，25x 省 token）
- 作者实测能力地图从最初 20+ 行增长到 200+ 行
- 工具链覆盖：飞书 CLI、obsidian_bridge.py、seedream、lark-cli、defuddle、web-access、whisper、vault-gardener、cc-health 等上百个命令行入口
- 能力地图组织方式：按场景（"我要做什么"）反向索引到工具链（"用哪个工具最省事"）

## 前提与局限性

- 能力地图假设工具集相对稳定；频繁更换工具链时维护成本上升
- 反向索引需要使用者持续维护，否则过时条目比没有更危险（Agent 会信任旧命令）
- 适用个人开发者场景；团队共享能力地图需要解决权限、环境差异等问题

## 关联概念

- [[Agent-Harness]] — 能力地图是 Harness 工具层的一种优化策略
- [[Tool-Use-Architecture]] — 能力地图是工具使用架构在实践中的落地
- [[Agentic-Workflow-Token-Efficiency]] — 能力地图通过减少摸索直接降低 token 消耗
- [[Three-Layer-Agent-Memory]] — 能力地图与三层记忆互补：记忆管"知道什么"，能力地图管"用什么"
