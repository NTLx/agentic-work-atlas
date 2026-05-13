---
type: entity
title: Progressive-Disclosure
aliases:
  - 渐进式披露
  - Skillify
definition: "一种知识组织策略——根据上下文动态决定加载哪部分知识，而非一次性全部注入 Context Window，是 LLM Wiki 和 GBrain 的核心检索机制"
created: 2026-05-13
updated: 2026-05-13
tags:
  - knowledge-management
  - AI
  - agent
related_entities:
  - "[[LLM-Wiki]]"
  - "[[GBrain]]"
  - "[[Obsidian-Wiki]]"
  - "[[Thin-Harness-Fat-Skills]]"
source_raw:
  - "[[深度解析LLM Wiki  Obsidian-Wiki  GBrain：Agent时代知识的"自组织"与"自进化"]]"
---

# Progressive-Disclosure（渐进式披露）

> [!definition] 定义
> **渐进式披露（Progressive Disclosure）** 是一种知识组织策略：通过定义清晰的元数据（Metadata）或 Schema，描述"在什么场景下应该调用哪些文件"，由大模型根据上下文动态决定加载哪部分知识，而非一次性将所有相关内容全部注入 Context Window。Garry Tan 用 "Skillify" 来描述这种将知识像 Skill 一样组织和加载的机制。

## 关键数据点

- **与传统 Skill 的区别**: 传统 Skill 固化为特定 `SKILL.md` 文件或指令集；Skillify 将 Skill 泛化为知识组织形态——任何 Markdown 文件、文档片段甚至零散笔记都可以是 Skill
- **GBrain 的三层检索流程**: "Chunk 确认 → 整页加载 → 分层呈现"——先以极低成本确认页面相关性（2KB chunk），再加载完整页面，最后按优先级分层喂给模型（先结论、后证据）
- **Token 效率**: 分层呈现避免将无关搜索结果一股脑塞进 Context Window，显著降低 Token 消耗
- **认知路径**: 引导模型遵循"先结论、后证据"的认知路径，避免陷入细节噪音而忽略全局脉络

## 前提与局限性

- 渐进式披露增加了工具调用和文档读取的时间开销，整体响应速度比 RAG 慢
- 在企业级生产环境中，这种延迟可能不可接受，需要混合架构（向量初筛 + 大模型精读）
- 渐进式披露的效果依赖 Schema/Metadata 的定义质量——如果分类不准确，可能导致遗漏关键知识
- 在实时性要求高的场景中，需要预加载热点知识作为补充

## 关联概念

- [[LLM-Wiki]] — 渐进式披露是 LLM Wiki 的核心知识组织机制
- [[GBrain]] — GBrain 的 Layered Feeding 是渐进式披露在检索环节的具体实现
- [[Obsidian-Wiki]] — Obsidian-Wiki 通过 20+ Skills 实现渐进式披露
- [[Thin-Harness-Fat-Skills]] — Skillify 理念的架构表达
- [[Knowledge-Compilation]] — 编译后的结构化知识是渐进式披露的前提
- [[Context-Engineering]] — 渐进式披露是 Context Engineering 在知识管理领域的应用
