---
type: source-summary
title: "Effective Context Engineering for AI Agents (Anthropic)"
source_raw:
  - "[[20260702-anthropic-context-engineering]]"
created: 2026-07-05
updated: 2026-11-28
tags:
  - source-summary
  - context-engineering
  - agent-engineering
  - AI-Agent
evidence_level: medium
claim_type: mixed
---

# Effective Context Engineering for AI Agents (Anthropic)

## 编译摘要

### 1. 浓缩
- **核心结论1**: Context Engineering 是 Prompt Engineering 的自然演进——不再是"找对措辞"，而是"在有限的注意力预算下，找到最小的高信号 token 集合来最大化期望行为"
  - 关键证据: Anthropic Applied AI 团队的工程实践总结。Context = 推理时输入 LLM 的所有 token 集合（系统指令、工具、MCP、外部数据、消息历史等）。作者以全注意力的成对关系及有限注意力作解释；计算复杂度与归一化不证明每 token 信息必减或任务表现单调下降（[[Context-Rot]]）。
- **核心结论2**: 作者介绍三种长周期 context 管理技术——Compaction（摘要压缩后重启 context window）、Structured Note-Taking（Agent 主动写笔记持久化到 context 外）、Sub-Agent 架构（专业化子 Agent 在清洁 context 中执行深度工作，返回压缩摘要）
  - 关键证据: Claude Code 的 compaction 实践（保留架构决策/未解决 bug/实现细节，丢弃冗余工具输出）；Claude 玩 Pokemon 的笔记系统（精确计数、探索地图、策略笔记跨 context reset 持久化）；Sub-Agent 在复杂研究任务上显著优于单 Agent
- **核心结论3**: "Just in Time" context 检索可与预处理混合——Agent 持有轻量标识符（文件路径、查询、链接），运行时动态加载数据，配合 Progressive Disclosure 逐层发现。但这与 pre-computed retrieval 存在 trade-off：运行时探索更慢但更灵活
  - 关键证据: Claude Code 使用此模式——写入定向查询，用 `head`/`tail` 分析大数据而不加载完整对象到 context

### 2. 质疑
- **关于"最小高信号 token 集合"的质疑**: "最小"和"高信号"是方向性指导，缺乏可操作的量化标准。实际工程中如何判断某个 token 是否"高信号"？Anthropic 未给出度量方法，主要依赖经验
- **关于 Compaction 的质疑**: 有损摘要可能丢失关键内容；不等于所有压缩都不可恢复。Anthropic 建议"先最大化召回率，再迭代提升精确率"，但召回率本身在 context 压缩场景下也难以精确衡量。哪些信息被丢弃可能在多轮后才暴露为关键缺失
- **关于 Sub-Agent 架构的质疑**: 子 Agent 返回 1,000-2,000 token 的压缩摘要，这个压缩比本身可能丢失关键上下文。文中提到"substantial improvement"但未给出定量数据

### 3. 对标
- **跨域关联1**: Context Engineering 的理念与 [[Context-Minimalism]] 高度一致——都是在有限注意力预算下做信息策展。Anthropic 这篇从工程实现角度提供了具体技术方案（Compaction/Note-Taking/Sub-Agent）
- **跨域关联2**: "Just in Time" context 检索 + Progressive Disclosure 的模式与人类认知高度相似——人类不记忆完整语料库，而是维护外部索引系统（文件系统、书签、inbox）按需检索。这与 [[Knowledge-Compilation]] 中的"编译 vs 索引"权衡直接对应
- **跨域关联3**: System Prompt 的"right altitude"（Goldilocks zone）——既不过度硬编码（脆性），也不过度模糊（无信号）——与 [[Ubiquitous-Language]] 和 [[Bounded-Context]] 的设计原则对应

### 证据边界

2026-11-28 本地80行摘录及官方原文复核：原网页现显示 Published Sep 29, 2025，与 Raw 的 published 2026-06-01 不一致；保留历史 Raw 元数据，引用原网页日期。原文明确允许混合预取与按需检索、指出探索延迟和摘要遗漏风险。三种机制为设计建议，案例非通用阈值或独立对照；不核当前产品合同。

### 关联概念
- [[Context-Engineering]]
- [[Context-Rot]]
- [[Context-Minimalism]]
- [[Progressive-Disclosure]]
- [[Knowledge-Compilation]]
- [[Agent-Loops]]
- [[Memory-Architecture]]