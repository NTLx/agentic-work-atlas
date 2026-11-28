---
type: entity
title: Graph-Guided Agent Investigation
aliases:
  - Graph-Guided Agent Investigation
  - graph-guided agent investigation
  - 图引导 Agent 调查
definition: "用知识图谱、依赖图或 DAG 引导 Agent 调查复杂系统故障、证据链和根因路径的工程模式"
created: 2026-06-02
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - AI-Agent
  - observability
  - enterprise-ai
related_entities:
  - "[[Agent-Logic]]"
  - "[[Knowledge-Graph]]"
  - "[[Local-Bounded-Reasoning]]"
  - "[[ITBench]]"
  - "[[Verifiable-Agent-Engineering]]"
source_raw:
  - "[[20260602-ibm-agent-logic-scalable-ai-adoption]]"
---

# Graph-Guided Agent Investigation

> [!definition] 定义
> **Graph-Guided Agent Investigation** 是用知识图谱、依赖图或 DAG 引导 Agent 调查复杂系统故障、证据链和根因路径的工程模式。它让 Agent 沿结构化关系探索，而不是在日志、指标和文档中自由漫游。

## 核心问题

企业 IT、工业资产和代码系统的故障通常不是单点文本问题，而是网络问题：服务依赖、调用链、事件传播、配置变更、代码路径和资产状态共同决定结果。

大规模图遍历、去重和状态更新适合用可审计算法实现；模型的搜索与解释能力仍随任务、工具和预算变化。因此图引导调查把“找相关节点和路径”的工作交给图结构，把“解释这些证据意味着什么”的工作交给模型。

## 典型流程

```text
告警 / 问题
  -> 图结构定位相关节点
  -> 收集局部证据
  -> LLM 解释候选根因
  -> 验证 / 追加查询 / 升级
```

## 价值

- **缩小搜索空间**: 从全量日志和服务列表收缩到局部依赖子图。
- **保留证据链**: 调查路径可以回溯到节点、边和观测数据。
- **候选证据收益**：可减少无依据的关系猜测，但错误拓扑、遗漏观测及错误语义解释仍可导致误诊；图中边不自动构成因果证据。
- **支持复用**: 一次 incident 形成的路径和规则可反哺后续调查。

## 与 Knowledge Graph 的区别

[[Knowledge-Graph|Knowledge graph]] 是结构化事实层；graph-guided investigation 是使用这层事实指导 Agent 行动的工作流模式。

前者回答“系统里有什么关系”，后者回答“Agent 应该沿哪些关系调查”。

## 关键数据点

- IBM Instana I3 / IT incident investigation 使用知识图谱、程序分析和 observability 驱动 orchestration。
- IBM博客（用例3）自报I3对GPT-5.1 ReAct最高4倍；换Gemini 3 Flash ReAct后差距仅17%（后者Token多1.6倍）。这是IBM ITBench相关实验，不是ITBench-AA排行榜，也不是单独图结构的因果收益。
- IBM博客另报定位故障微服务及修复的特定增益；具体任务、模型与基线不同，不与I3混计。详见[[Agent-Logic]]及[原文](https://huggingface.co/blog/ibm-research/agent-logic-and-scalable-ai-adoption)用例3。
- Maximo Condition Insights 用 DAG、结构化证据和验证循环处理工业资产维护，内部 pilot 将资产分析时间从 15-20 分钟降到 15-30 秒。

## 两种图引导机制的直接证据（2026-11）

- [EoG](https://arxiv.org/html/2601.17915v1) §4、§5.2/Table 2：确定性调度与LLM局部溯因分离，消息传播允许非单调修订。35场景、3次运行；不同模型的根因实体F1和累计Token表现不同。见[[Local-Bounded-Reasoning]]。该研究使用LLM判定语义匹配；不能把图遍历完整性当作因果正确性保证。
- [Praxis](https://arxiv.org/html/2512.22113v1) §V–VI：服务依赖图SDG和程序依赖图PDG共同限定诊断范围。30个代码/配置相关及对照故障场景、6模型、3系统、每配置5次，共2700轨迹的主对照；作者报告最高3.1倍RCA准确性及3.8倍Token效率改善（摘要；Table V分别报告ATC和effective ATC，不能把按成功诊断归一化的开销当作每次运行的实际Token）。§VI-D报告观测稀疏的部署清单与资源类故障准确性接近零，且错误/不完整依赖图、节点粒度及代码不可用会限制效果。

**综合判断**：保留候选根因、支持与反驳证据、时间/版本、图覆盖范围及未观察区域。证据不足时扩大搜索或升级，不强制在已有子图中选根因。拓扑相关、故障传播路径和根因判定是不同对象；测试修复或复现条件提供更强证据，但不可擅自操作生产系统。本轮核对论文文本而非复跑，未把相关论文视为新增已编译Raw。

## 前提与局限性

图结构不会自动保证正确。依赖图可能过期，观测数据可能缺失，边权也可能无法表达真实因果。因此图引导调查需要与重新采样、人工升级和反事实验证配合。

该模式最适合依赖关系明确、观测数据足够、证据链可结构化的环境。如果图谱长期不维护，Agent 只是沿着过期地图更快地走错路。

## 关联概念

- [[Agent-Logic]] — 图遍历是 agent logic 的重要组成。
- [[Local-Bounded-Reasoning]] — 图结构提供局部推理边界。
- [[ITBench]] — 企业 IT Agent 能力评估场景。
- [[Verifiable-Agent-Engineering]] — 图路径让调查过程更可观察和可复现。
