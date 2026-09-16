---
type: entity
title: Memory Architecture
aliases:
  - Memory Architecture
  - 记忆架构
  - Memory System
  - 记忆系统
definition: "LLM 应用中长期记忆的工程架构——解决 staleness（过时）/ correctness（错误）/ scalability（亿级用户 × 多年）三大挑战的子系统设计"
created: 2026-06-06
updated: 2026-09-16
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
> **Memory Architecture** 是 LLM 应用中长期记忆的工程架构——解决 staleness（过时）/ correctness（错误）/ scalability（亿级用户 × 多年）三大挑战的子系统设计。代表实现：OpenAI ChatGPT Dreaming V3（2026-06）、三层 Agent 记忆 L1/L2/L3（2026-05）、Obsidian + Claude Code 脑（2026-05）。

## 三大核心挑战

| 挑战 | 含义 | 典型失败 |
|------|------|----------|
| **Staleness** | 记忆内容随时间过时 | "用户 7 月去新加坡"→ 8 月应自动改写为"用户 7 月去了新加坡" |
| **Correctness** | 记忆内容错误或无中生有 | 虚构用户偏好、把临时决定当长期判断 |
| **Scalability** | 亿级用户 × 多年时间窗口 | 算力成本爆炸、检索延迟、隐私合规 |

## 代表实现对比

| 架构 | 运营方 | 触发方式 | 评审界面 | 解决重点 |
|------|--------|----------|----------|----------|
| Saved memories | OpenAI | 用户显式触发 | 列表 | correctness |
| Dreaming V3 | OpenAI | 后台持续综合 | Memory summary page | staleness + scalability |
| Three-Layer Agent Memory | 社区/个人 | 主动分层写入 | 各自文件 | 防止记忆腐化 |
| Memex-style 个人数据 | 历史范式 | 用户主动管理 | 完全用户控制 | 数据主权 |

## 与系统设计的关系

- **OS daemon 类比** — 后台进程在用户不在时整理，对用户不可见但持续
- **数据库类比** — 记忆是用户状态，记忆架构是 schema + index + transaction
- **缓存类比** — 记忆 = L1/L2/L3 cache，按需加载控制 prompt 成本

## 关键设计模式

| 模式 | 说明 | 应用 |
|------|------|------|
| 后台综合 | 用户不在时跑整理进程 | OpenAI Dreaming |
| 三层分离 | L1 画像 / L2 程序性 / L3 历史 | Three-Layer Agent Memory |
| 摘要降维 | 巨量记忆通过 summary 暴露给用户 | Memory summary page |
| 按需加载 | prompt 中只装当前相关记忆 | 所有 LLM 应用 |
| 时间戳版本化 | 记忆带时间戳 + 自动更新 | Dreaming V3 |
| 职能分层 | working / episodic / semantic / procedural 分开读写 | CoALA-inspired playbook |
| 遗忘与冲突治理 | 过期、替代、标记矛盾，而不是无限追加 | memory maintenance |

## 从“存得下”到“能维护”的五层管线

这份 playbook 对现有架构图的增量，不是再增加一个数据库，而是把记忆的行为契约拆开：当前上下文负责工作，episodic 记录经历，semantic 保存可复用事实，procedural 保存经重复验证的方法，forgetting 负责跨层清理和冲突治理。

**判断**：生产记忆系统的关键边界在“写入什么、何时召回、何时晋升、何时失效”，而不在某一种向量库或文件格式。

- **证据**：[[Agent Memory _ The 5-Layer Playbook.pdf]] 第 2–8 页；第 4 页给出技能晋升门槛，第 5–6 页给出 expiration / supersession / contradiction resolution，第 7–8 页把流程串成 agent loop。
- **边界**：该 PDF 是低证据等级的独立汇编，阈值与效果数字不是通用默认值；高风险领域仍需更长保留、人工复核、权限隔离和可审计 provenance。

## 前提与局限性
- **持续 compute cost** — 后台进程算力开销大
- **summary 失真** — summary 本身有信息损失
- **隐私合规** — 记忆属用户数据，监管严
- **训练回授** — 用户修改 = 标注员行为

## 关联概念
| 本库主题 | Memory Architecture 的连接 |
|---------|------------------------|
| [[Dreaming]] | OpenAI 的具体实现 |
| [[Multi-Layer-Memory]] | 平行概念（按 token 加载） |
| [[Three-Layer-Agent-Memory]] | 三层分层实现 |
| [[Context-Engineering]] | 持续记忆是 context engineering 核心场景 |
| [[Agent-Harness]] | 记忆架构是 harness 组件 |
| [[Memex]] | 历史范式参考 |
| [[Personal-AI-Assistant]] | 记忆架构是个人 AI 助理的标志能力 |
| [[Staleness-Problem]] | 三大挑战之一 |
| [[Memory-Synthesis]] | Dreaming 核心动作 |
| [[Memory-Summary-Page]] | Dreaming V3 用户界面 |

- [[OpenAI]] — Dreaming V3 开发方

## 关键数据点

（关键事实、统计、时间线从原 raw 源沉淀，见 source_raw 字段）
