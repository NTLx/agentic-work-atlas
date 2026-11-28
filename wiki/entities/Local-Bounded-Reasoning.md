---
type: entity
title: Local-Bounded Reasoning
aliases:
  - Local-Bounded Reasoning
  - local-bounded reasoning
  - 局部有界推理
definition: "通过工作流结构、图谱、程序分析和策略约束，把 LLM 的推理限制在局部相关状态空间内的 Agent 设计原则"
created: 2026-06-02
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - AI-Agent
  - reasoning
  - context-engineering
  - enterprise-ai
related_entities:
  - "[[Agent-Logic]]"
  - "[[Context-Engineering]]"
  - "[[Agentic-Workflow-Token-Efficiency]]"
  - "[[Verifiable-Agent-Engineering]]"
source_raw:
  - "[[20260602-ibm-agent-logic-scalable-ai-adoption]]"
---

# Local-Bounded Reasoning

> [!definition] 定义
> **Local-Bounded Reasoning** 是一种 Agent 设计原则：通过工作流结构、知识图谱、程序分析和策略约束，把 LLM 的推理限制在局部相关状态空间内，而不是让模型在整个企业上下文中自由搜索。

## 为什么需要它

企业系统的上下文空间很大：遗留代码、微服务依赖、监控指标、权限策略、合规规则、工单历史和业务流程都可能相关。无选择地扩展上下文可能增加成本、噪声与错误关联，但遗漏关键证据同样会降低质量。局部化是可验证的检索及推理策略，不是对真实因果范围的预先断言。

局部有界推理的目标不是让模型知道更多，而是让模型少看但看对。

## 典型机制

- 先用程序分析或图遍历找出相关模块、服务、事件或规则。
- 再把局部证据组织成模型可消费的上下文。
- 让模型在被约束的候选空间内解释、规划或生成。
- 用测试、规则、策略或证据链验证输出。

## 与 Context Engineering 的关系

[[Context-Engineering|Context engineering]] 关心“模型应该看到什么”。Local-bounded reasoning 进一步提出选择原则：上下文不只是压缩出来的，而是被工作流结构裁剪出来的。

这是用领域结构组织上下文，而非仅压缩Token。单次局部上下文较小不意味着累计输入Token、调用次数或总成本更低。

## 关键数据点

- IBM 主机代码理解案例显示，先用深度静态分析和预索引数据库缩小代码理解空间，作者报告在多个最高约百万行、千个程序的遗留系统应用理解任务上，相比 frontier LLM-only 基线保持略高表现、Token约为其1/30（IBM博客用例1）；非所有任务的因果效应或总成本比。
- Aster 测试生成通过程序分析和数据前后处理，把测试生成从开放式生成收缩为围绕代码结构和变更边界的局部任务。
- IT incident investigation 案例用知识图谱和 observability 信息引导调查，而不是让模型直接遍历全量日志和服务上下文。

## 局部推理与全局修正：EoG 研究实例

IBM关联论文 [Think Locally, Explain Globally (arXiv:2601.17915v1)](https://arxiv.org/html/2601.17915v1) §4、§5.2/Table 2（2026-11-28核对）：确定性Controller管理活跃节点、外部Ledger、消息与终止；Context Contract提供局部观测、相邻拓扑和传入消息；LLM执行溯因推理，提出局部判断与后续候选节点。新证据可以修订早先判断，证据缺失或无法识别时标记Defer；无明确根因则输出带不确定性的候选排序。

在35个ITBench场景、每个3次的论文实验中，GPT-5.1 ReAct→EoG的根因实体majority@3 F1为8.6→86.1，平均输入Token却由779K增至1837K（输出9.3K→1.7K）；Gemini 3 Flash的对应F1为74.3→92.1，输入5376K→3390K，输出21.2K→2.0K。Token不含reasoning tokens；不同实现工具集也不同。不能将局部化直接等同于全程降本，或把这些F1与ITBench-AA的precision-at-full-recall相混。

**综合判断**：局部窗口负责生成候选解释；全局状态负责证据覆盖、跨节点修订、预算及停止。验收需检查真实根因、证据遗漏、错误收敛、累计成本和无法判断时的升级；未复跑上述论文实验。

## 前提与局限性

如果局部边界切错，Agent 会错过真正原因。IT incident、复杂代码缺陷和跨部门流程问题都可能存在远距离依赖。因此 local-bounded reasoning 必须配合重新扩展搜索空间的机制，而不能把第一次裁剪当成真理。

这个原则更适合强结构任务。对战略判断、组织政治、创意探索等低结构任务，局部边界可能只能降低噪声，不能保证判断正确。

## 关联概念

- [[Agent-Logic]] — 产生局部边界的 harness 逻辑层。
- [[Agentic-Workflow-Token-Efficiency]] — 局部化可能降低累计Token，也可能因重复采样或传播增加总消耗，需实测。
- [[Verifiable-Agent-Engineering]] — 局部边界需要被验证和回退。
