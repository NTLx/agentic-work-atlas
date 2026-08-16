---
type: entity
title: Compaction
aliases:
  - Compaction
  - Context Compaction
  - Conversation Compaction
definition: "Coding agent 在长会话中当上下文逼近窗口上限时，把较老轮次通过一次独立的 LLM 调用序列化为结构化摘要（goal / progress / key decisions），保留最近 N 个消息不变，结果作为新 turn 前缀插入的工程机制；与 prompt cache 存在结构性张力"
created: 2026-08-16
updated: 2026-08-16
tags:
  - context-engineering
  - coding-agent
  - memory
evidence_level: high
claim_type: mixed
related_entities:
  - "[[Context-Engineering]]"
  - "[[Context-Rot]]"
  - "[[Ralph-Loops]]"
  - "[[Memory-Summary-Page]]"
  - "[[Agent-Harness]]"
  - "[[Coding-Agents]]"
  - "[[AGENTS-md]]"
source_raw:
  - "[[20260816-earendil-pi-compaction]]"
---

# Compaction

> [!definition] 定义
> **Compaction** 是 coding agent 在长会话中当上下文逼近窗口上限时，把较老轮次通过一次独立的 LLM 调用序列化为结构化摘要（goal / progress / key decisions），保留最近 N 个消息不变，结果作为新 turn 前缀插入的工程机制。由 Pi coding agent 团队在 2026-08 工程博客中详细描述，被 Claude Code、Codex 等同类 agent 普遍采用。

## 关键数据点

### 触发机制（三类）

| 触发类型 | 触发条件 | 时机 |
|---------|---------|------|
| **Auto-trigger** | 上下文逼近窗口上限 | turn 结束后检查（保留 cache 链）|
| **Manual-trigger** | 用户执行 `/compact` 命令 | 即时 |
| **Emergency-trigger** | mid-turn context overflow error | mid-turn |

### 摘要结构（Pi 工程实现）

```
before compaction: [system + tools][older turns][recent retained messages]
after compaction:  [system][tools][summary][recent retained messages][new user message]
```

- **system prompt**：独立 = "you are a context summarization assistant"
- **user message**：独立 = "structured summary of this conversation branch for context when returning later"
- **三段式输出**：goal / progress / key decisions
- **standalone request**：不嵌入常规对话，可用不同 LLM 模型

### 配置参数（Pi 默认）

| 参数 | 默认值 | 说明 |
|------|--------|------|
| Retained token budget | 20k tokens | 保留的最近消息总 token 数 |
| 折算 turn 数 | 5-20 turns | 取决于 turn 平均长度（tool call 多则 turn 短）|

### 与 Prompt Cache 的张力

```
cached before compaction:    [system][tools][older history][recent retained turns]  ← 全 cached
first request after compaction: [system][tools][summary][recent retained turns][new user message]
                              ^ retained turns 同样 tokens，但前缀变了 → cached prefix 作废
                              <-- reusable -->^ | 重新计算起点
```

- compaction 一次 = 一次 cache miss 链重置
- 之后请求重新建立 cache 链（warm-up 成本）
- **trigger 阈值选择** = cache 利用 vs overflow 风险的权衡

### 跨模型延续

- summary 存为 plain text（非结构化嵌入）
- 切换 LLM 模型时 summary 仍可读（session portability）
- **tradeoff**：portability 优于 structured embedding，但 loss of programmatic queryability

## 关键命题

### 命题 1：Compaction 是 [[Context-Engineering]] 的核心子机制

[[Context-Engineering]] 关注"Agent 看到什么、何时看到"；Compaction 关注"如何让 agent 在长会话中保留关键决策"——是 Context-Engineering 在"会话生命周期"维度的具体实现

### 命题 2：Compaction 对抗 [[Context-Rot]]

[[Context-Rot]] 主张"上下文填充越多，模型推理下降"——这是一个观察性现象。Compaction 提供**工程手段对抗**——通过定期压缩保持 high-signal token 比例。但**触发阈值 / 摘要质量上限决定对抗效果**

### 命题 3：Compaction 与 [[Ralph-Loops]] 是同一问题的两种解

| 机制 | Ralph-Loops | Compaction |
|------|-------------|------------|
| 对抗问题 | context 衰减 | context 衰减 |
| 路径 | 同一上下文无限循环 | 上下文定期压缩重置 |
| cache 利用 | 高（无 compaction 触发）| 中（每次 compaction 后 warm-up）|
| 信息保留 | 完整 | 摘要（信息有损）|

→ 适用场景不同：Ralph-Loops 适合结构化短任务；Compaction 适合长会话多任务

### 命题 4：独立 LLM 调用是核心设计选择

- **优势**：可用更小/更便宜的模型做摘要；不污染主对话上下文；可在不同模型间共享
- **代价**：compaction 本身消耗 token；摘要质量受模型能力限制
- **决策点**：Pi 未披露默认 compaction 模型选择策略（成本 vs 质量权衡）

## 前提与局限性

- **trigger 阈值未披露**——影响 user 反馈时间
- **20k tokens 默认值是经验值**——深度调试类任务可能不够
- **compaction 模型选择未披露**——小型模型做摘要可能遗漏关键决策点
- **摘要结构固定为三段式**——未必适用所有任务类型（数据探索 / 写作 / 调试需要不同模板）
- **compaction 成本未量化**——cache miss + LLM 调用合计开销
- **plain text 存储 vs structured embedding 的 tradeoff**——portability 优于 programmatic queryability
- **任务感知的摘要模板缺失**——Pi 没实现"任务类型感知 compaction"

## 时间线

- **2026-08** — Earendil Engineering 发布 Pi compaction 详细工程文档（GitHub 源码链接）
- **同期** — Claude Code、Codex 等同类 coding agent 普遍实现 compaction，但实现细节与 Pi 略有差异

## 关联概念

- [[Context-Engineering]] — 父概念；Compaction 是子机制
- [[Context-Rot]] — Compaction 对抗的现象
- [[Ralph-Loops]] — 同一问题的替代方案
- [[Memory-Summary-Page]] — Obsidian vault 轻量索引模式，同构的"摘要 + 按需加载"
- [[Agent-Harness]] — Compaction 是 harness 的子组件（context 管理维度）
- [[Coding-Agents]] — Claude Code / Codex / Pi 等同类 agent 普遍采用
- [[AGENTS-md]] — Coding agent 的初始配置；与 compaction summary 是两类不同 artifact