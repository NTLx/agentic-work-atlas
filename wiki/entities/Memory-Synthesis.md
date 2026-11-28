---
type: entity
title: Memory Synthesis
aliases:
  - Memory Synthesis
  - 记忆合成
  - 记忆综合
  - Background Memory Curation
definition: "从获授权的历史与其他来源提炼、合并、校正和更新跨任务记忆的过程，可后台或按需执行；不等于模型训练。"
created: 2026-06-06
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - memory-system
  - context-engineering
  - openai
related_entities:
  - "[[Dreaming]]"
  - "[[Memory-Architecture]]"
  - "[[Staleness-Problem]]"
  - "[[Memory-Summary-Page]]"
  - "[[Multi-Layer-Memory]]"
  - "[[OpenAI]]"
  - "[[Personal-AI-Assistant]]"
source_raw:
  - "[[20260604-openai-dreaming-memory]]"
---

# Memory Synthesis（记忆合成）

> [!definition] 定义
> 从获授权的历史、用户输入及其他可用来源提取、合并和更新持久记忆。OpenAI Dreaming为后台综合实例；合成不是所有记忆更新的唯一方式，也不意味着模型参数改变。

## 与显式记忆的关系

| 维度 | 显式记录 | 综合 |
|---|---|---|
| 触发 | 用户请求或业务写入规则 | 后台、任务结束或按需触发 |
| 输入 | 具体授权的信息 | 获准访问的多个来源 |
| 更新 | 增删改与版本控制 | 提取、冲突核验、归并及更正 |
| 代价 | 需适当记录与验证 | 额外处理、误合并及错误传播风险 |

二者可组合，不将显式记录定性为无时间感知或高成本。OpenAI官方未披露具体LLM-as-judge、索引、去重算法与更新调度；原先积分式只是类比，不能描述真实实现。

## 候选合成合同

1. 提取：保留来源、身份、事件时间与语义类型，区分事实、偏好、推断与待验证。
2. 核验：检查授权、来源版本、相互独立性、冲突和实际状态；计划时间已过不能自动变成已完成事件。
3. 合成：在适用范围内去重或记录替代关系；不同结论、条件或证据不应机械合并。
4. 更新：按风险更正、撤销、过期或重新验证；保留必要的合法历史与恢复路径。
5. 验收：确认新状态及下游复用，检查正确内容是否保留；不是只看摘要更短。

## 关键数据点

- [OpenAI Dreaming（2026-06-04）](https://openai.com/index/chatgpt-memory-dreaming/)记载2024-04 Saved memories、2025-04首版dreaming及2026-06 V3，三个评测目标为连续性、偏好/约束、时效。Free用户dreaming所需计算约降至原先1/5，厂商自报，非所有综合流程成本。
- [当前Memory帮助中心](https://help.openai.com/en/articles/8590148-memory-in-chatgpt)说明摘要并非全部记忆，敏感信息可进入记忆，纠正、不再提及和删除来源有不同效果；训练使用依数据控制，不把用户纠正等同训练标签。
- [[20260729-memsecbench-memory-lifecycle]]：受控研究中移除目标语义与保留正常记忆的成功率不同，支持将两项分别验收。

## 前提与局限性

合成需要适用、可访问且获授权的来源。相同模型或原始证据可能重复错误，摘要可能省略条件或丢失细节；持续后台运行的频率及成本未披露。删除、保留、撤销、同步和训练分别治理。2026-11-28回核官方发布、帮助中心和相关研究，未复现内部算法或评测。本库上述合同是候选设计，不是OpenAI已公开实现或新增Schema。

## 关联概念

- [[Dreaming]] — 后台综合的产品实例。
- [[Memory-Architecture]]、[[Multi-Layer-Memory]] — 架构和分层。
- [[Staleness-Problem]]、[[Shared-Memory-Contamination]] — 时效、冲突、纠错与安全。
- [[Memory-Summary-Page]] — 用户可见与可控的摘要。
- [[OpenAI]]、[[Personal-AI-Assistant]] — 产品场景。
