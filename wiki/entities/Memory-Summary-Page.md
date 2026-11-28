---
type: entity
title: Memory Summary Page
aliases:
  - Memory Summary Page
  - 记忆摘要页
  - Memory Dashboard
definition: "记忆系统面向用户的高层可见与纠正界面；摘要不保证覆盖所有底层来源、状态或数据保留。"
created: 2026-06-06
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - memory-system
  - openai
related_entities:
  - "[[Dreaming]]"
  - "[[Memory-Architecture]]"
  - "[[Memory-Synthesis]]"
  - "[[Staleness-Problem]]"
  - "[[OpenAI]]"
  - "[[Personal-AI-Assistant]]"
source_raw:
  - "[[20260604-openai-dreaming-memory]]"
---

# Memory Summary Page（记忆摘要页）

> [!definition] 定义
> 面向用户展示综合记忆要点、支持纠正与个性化控制的界面。OpenAI Dreaming V3于2026-06发布时介绍该设计；它提升部分状态可见性，并不是把全部用户状态从黑盒变成白盒。

## 可见性与控制的不同层次

| 能力 | 应确认的真实效果 |
|---|---|
| 观察 | 查看摘要及可用来源；非完整数据清单 |
| 纠正 | 更新错误或过时信息，核验后续使用 |
| 行为约束 | 降低后续提及或指定偏好；不等于删除底层记录 |
| 删除 | 按实际信息所在的摘要及原始来源处理，注意传播延迟与保留政策 |
| 数据用途 | 个性化、服务存储、模型改进及安全用途独立治理 |

## 关键数据点

- [OpenAI 2026-06-04发布](https://openai.com/index/chatgpt-memory-dreaming/)：通过摘要浏览重点、添加或更新信息、提供何时提及主题的指导。
- [Memory in ChatGPT（2026-11-28回核）](https://help.openai.com/en/articles/8590148-memory-in-chatgpt)：摘要不是所有记忆或来源的完整视图；Sources也不保证显示影响回答的全部因素。完全移除需要处理摘要及所有含该信息的来源，删除与更新传播可能需要时间；仅要求不再提及不会删除来源。实际功能因套餐、地区、平台和工作区而异。个人账号的数据改进设置与记忆开关独立，Business/Enterprise/Edu等默认不用于训练。不能由用户纠正行为推出训练用途。
- 文章未公开用户查看率、完整性指标或纠正后回归通过率。原“信任=可观察性+可修改性+可撤回性”仅是历史启发式，不是可计算定律。

## 本库综合

知识状态的可观察性应结合来源、版本、适用范围和未解决问题；纠正操作需要真实状态验收，撤销应追踪衍生条目。摘要便利不等于来源可恢复或完整删除。设计评估需检查用户能否识别错误、修改实际状态并保留正常功能，同时遵守访问与隐私限制。未实施新UI。

## 前提与局限性

摘要可能失真、遗漏或过时；检查与修正可能带来用户成本，使用率及效果需实测。来源记录不自动证明信息真实，原始数据处理需遵守权限及保留规则。2026-11-28只核公开官方材料，未验证任何特定账号设置、后端算法或删除实际结果。

## 关联概念

- [[Dreaming]]、[[Memory-Synthesis]] — 综合结果。
- [[Memory-Architecture]]、[[Staleness-Problem]] — 状态管理与时效。
- [[Shared-Memory-Contamination]] — 纠正、撤销和来源。
- [[OpenAI]]、[[Personal-AI-Assistant]]、[[Memex]] — 产品与个人信息治理。
