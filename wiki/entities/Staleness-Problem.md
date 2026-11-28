---
type: entity
title: Staleness Problem
aliases:
  - Staleness Problem
  - 记忆过时
  - Memory Staleness
definition: "已保存事实、偏好、规则或状态与当前任务所需时点或适用范围不一致的风险；需区分实际变化、过期、纠正、时间查询和未知状态。"
created: 2026-06-06
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - memory-system
  - context-engineering
related_entities:
  - "[[Dreaming]]"
  - "[[Memory-Architecture]]"
  - "[[Memory-Synthesis]]"
  - "[[Memory-Summary-Page]]"
  - "[[Multi-Layer-Memory]]"
  - "[[OpenAI]]"
source_raw:
  - "[[20260604-openai-dreaming-memory]]"
---

# Staleness Problem（记忆过时问题）

> [!definition] 定义
> 持久记忆与目标任务所需时点或适用范围不一致，导致错误召回或应用。信息陈旧不必然错误，历史事实可能仍真实但不适用于当前问题；当前结论也可能从首次写入就不正确。OpenAI将staleness列为记忆架构的三项挑战之一，并未证明不可解决。

## 时间与状态的区别

| 情况 | 应如何处理 |
|---|---|
| 计划日期已过去 | 不自动改成已完成；核实完成、取消、延期或未知 |
| 当前角色或偏好改变 | 新证据支持时更新适用范围，保留必要历史 |
| 规则或接口版本改变 | 核对实际版本及生效状态；旧规则不得默认继续执行 |
| 同一时点证据冲突 | 区分来源权威、独立性和条件，必要时保留分歧 |
| 查询过去某时点 | 使用当时有效的事实，不机械选最新记录 |
| 未获得结果 | 区分已查范围内无证据、范围外及未完成查询；不得补造事实 |

## 候选治理策略

区分事件时间、有效时间、记录时间、最后核验时间与来源版本。高风险或易变状态按实际权威来源复核，无法确认时表达不确定性；稳定事实不因更新时间旧就删除。新记录可能更正历史而非替代当前状态，过期与撤销也不同。对于权限受限信息，不应借缺失状态向未授权者暴露其存在。

## 关键数据点

- [OpenAI Dreaming 2026-06-04](https://openai.com/index/chatgpt-memory-dreaming/)将时间影响正确回答纳入评测；旅行计划示例说明需要时间感知，不是实际出行完成证据。未披露通用过期算法。
- [[20261020-tessl-claim-based-agent-memory]]关联作者[VarOps报告](https://raw.githubusercontent.com/varops/acropolis-research/main/paper/methodology.md) A.11：LongMemEval-S 500问的禁止拒答探针，总准确率88.0→87.2%，30个不可答题中正确拒答29→0，470可答题准确率87.4→92.8%。显示只看总分可能掩盖缺失处理的变化；特定厂商试验非普适效果。正文“30次原有诚实拒答”的说法与表中29次不一致，以表为依据，未复跑。
- [[20260729-memsecbench-memory-lifecycle]]：修复需同时检查目标错误去除与正确记忆保留，不将陈旧条目数量下降当作正确性提升。

## 前提与局限性

时间戳不能替代实际事实核验；用户明确纠正是授权的重要来源，但与客观状态、外部事实和其他权限主体需区分。更新策略依风险、业务有效期和保留政策；用户询问成本与错误影响需平衡，不断言用户不会查看或主动询问必定不合适。2026-11-28回核OpenAI官方发布、VarOps作者技术报告与已校准来源，未执行生产时效评测。本库不设普适TTL或新Schema。

## 关联概念

- [[Dreaming]]、[[Memory-Architecture]]、[[Memory-Synthesis]] — 持久状态维护。
- [[Memory-Summary-Page]]、[[Shared-Memory-Contamination]] — 纠错、撤销与来源。
- [[Multi-Layer-Memory]] — 不同记忆类型的更新策略。
- [[Structured-Agent-Memory]] — 适用条件及版本。
- [[Continual-Learning]]、[[OpenAI]] — 模型学习与外置记忆的不同机制。
