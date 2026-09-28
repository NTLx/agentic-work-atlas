---
type: source-summary
title: "Coding sessions are longer and use more context. Claude Opus 5.5 is built with that in mind."
canonical_url: "https://claude.com/blog/claude-opus-5-5-built-for-coding-sessions-that-use-more-context"
raw_state: index
original_raw_file: "20260924-claude-opus-5-5-context-cost.md"
original_body_sha256: "c1b2657689fdc0b1cdaff1cc56ae7bc49a66429a402069ace4c737da5d9d4939"
indexed_at: "2026-09-28T16:34:38+08:00"
created: 2026-09-28
updated: 2026-09-28
tags:
  - source-summary
  - claude-code
  - context-engineering
  - token-economics
  - prompt-cache
evidence_level: high
claim_type: mixed
source_locator:
  - "Claude Code trends"
  - "What makes Opus 5.5 cost effective for long, context heavy sessions"
  - "Cache is cheap"
  - "Claude Code is better at using the cache"
  - "The same task, but with fewer turns"
  - "Protect your cached reads"
---

# Coding sessions are longer and use more context

## 1. 浓缩

- **核心结论 1：coding-agent 成本结构正在从“生成多少”转向“反复读多少上下文”。**
  - Anthropic 的 2026-03→09 Claude Code 聚合数据中，prompts/session 基本稳定，但每 prompt 工作时间约 3.3×、model calls/prompt 增长 >40%、中断减少 68%，context/request 增长约 2.6×，input:output 从 189:1 变为 324:1。
  - **判断**：长程 coding agent 的主要经济变量不再只是 output token，而是**重复上下文读取 × session 长度 × turn 数**。Context Engineering 因此同时是质量工程和 FinOps。
- **核心结论 2：Prompt Cache 已从实现优化升级为 Agent Harness 的成本架构。**
  - Anthropic 把缓存读价、cache invalidation、TTL、effort 切换与 subagent cache inheritance 放在同一篇成本分析里，说明 cache 命中率由 harness 行为共同决定。
  - **判断**：对长程 Agent，cache locality 是一等设计目标。改变模型、工具、instructions、compaction 时，不仅影响行为，也可能改变整个 session 的成本曲线。
- **核心结论 3：应以“完成任务成本”而不是“单 token 价格”评估模型。**
  - 强模型若在开放任务上少走错误路径、减少 turns/tool calls，节约可能大于单 token 价差；但文章明确说简单机械任务未必存在该优势。
  - **判断**：模型选择应按 workload 分层：短机械任务偏单位价格，长开放任务要同时测 turns、cache reuse、成功率和 wall-clock。

## 2. 质疑

- 数据是 Anthropic 自身产品 telemetry，不是跨 coding-agent 市场样本。
- Opus 5.5 成本与竞品比较同时受价格政策、Claude Code harness、任务分布和模型质量影响，无法把收益单独归因于模型。
- “输入 miss 减半”等变化来自多个 Claude Code 改动叠加，文章没有给出逐项消融。
- Zeta Labs 案例属于客户自报；文章自己也提醒不同 codebase 应实测。

## 3. 对标与约束

- **与 [[Agentic-Workflow-Token-Efficiency]]**：补上“重复 context read 成为主成本项”的直接产品 telemetry，并把 cache hit rate 从局部技巧提升为 task economics。
- **与 [[Context-Engineering]]**：既有框架强调最小高信号 token；本文补充一个经济约束——即使上下文都“有用”，反复读取也有持续成本，因此上下文生命周期和 cache stability 同样重要。
- **与 [[Compaction]]**：compaction 能释放窗口，但会改变 prefix；因此 compaction 时机必须同时考虑 context rot 与 cache invalidation。
- **与 [[Agent-Harness]]**：模型成本并非模型自身属性；TTL、subagent inheritance、tool loading、effort switching 等 harness 决策会重塑有效成本。

## 证据边界

- 第一方 Anthropic telemetry，适合作为 Claude Code 工作负载变化的一手证据。
- 价格和性能比较是厂商陈述，不升级为跨模型通用基准。
- Raw 为公开页面 evidence snapshot；canonical 页面可恢复。

## 关联概念

- [[Agentic-Workflow-Token-Efficiency]]
- [[Context-Engineering]]
- [[Compaction]]
- [[Agent-Harness]]
