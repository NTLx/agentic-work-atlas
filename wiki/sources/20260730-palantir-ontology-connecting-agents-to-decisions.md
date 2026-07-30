---
type: source-summary
title: "Connecting Agents to Decisions"
source_raw:
  - "[[20260730-palantir-ontology-connecting-agents-to-decisions]]"
created: 2026-07-30
updated: 2026-07-30
tags:
  - source-summary
  - palantir
  - ontology
  - decision-centric
  - enterprise-ai
evidence_level: low
claim_type: mixed
---

# Connecting Agents to Decisions — Palantir 决策中心架构总纲

> 来源：Palantir Blog（2026-04-28，约 15 分钟阅读），厂商官方。**证据定级 low**：Palantir 是 AIP/Ontology/FDE 的发明者与最大受益方，全文以 Ontology 为唯一答案，产品包装倾向明显；但可拆出四层可独立验证的机制（决策中心 ≠ 数据中心、ontology-as-tools、scenario staging、decision lineage 数据飞轮）。Onyx Incorporated 为虚构案例，不作事实引用。

## 编译摘要

### 1. 浓缩
- **核心结论1**：传统数据架构只描述数据、不描述"决策"，因此无法承载 AI；企业需要决策中心（decision-centric）架构，把 data / logic / action / security 四要素整合进单一系统
  - 关键证据: 数据侧的关键问题从 cleanliness 转向 relevance——必须捕获"决策数据"（决策上下文、候选选项、commit 后下游影响），并自动记录 end-to-end decision lineage（何时、基于哪个数据版本、通过哪个 app 做出决策）；这套 lineage 是 agentic memory（working/episodic/semantic/procedural）的燃料。
- **核心结论2**：Ontology 同时建模名词（data objects）与动词（actions），agent 与人类共用同一套 logic binding 接口和 action 原语，通过 tools 范式调用，而非只检索文本
  - 关键证据: logic 资产（业务逻辑、ML 预测、优化/仿真模型）统一为 agent 可调用的接口，tribal knowledge 通过持续生成新 functional encapsulation 沉淀；actions 可被 stage 为 scenarios（沙盒化 ontology 子集），人类 review 后 commit 写回 transactional systems/edge/custom apps；explore/stage/commit 权限分级原生建模。
- **核心结论3**：AI 自动闭环的范围是可外科手术式调节的治理变量——每个 agent 被视为"新员工"，置信度提升后逐步扩大 purview
  - 关键证据: 默认情况下 agent 的 action 只能 stage、必须人工 review；组织凭 granular logging 选择哪些"trusted, well-worn"流程可绕过人工；安全侧 marking/purpose/role 三类策略在每次交互动态计算，tool 调用受同一套安全架构约束（runtime validation + 显式 authorization grants）。decision lineage 事后可作 fine-tuning 数据与 agent prompting 原则。

### 2. 质疑
- **关于"结论1"的质疑**: "传统架构无法承载 AI"是全文论点前提，但反例未被讨论——大量 agentic 系统建立在数据仓库 + RAG 上也能运行；更准确的表述应是"无法承载需要审计与写回的操作型 AI"。decision lineage 自动捕获的工程代价（埋点、存储、隐私）全文未提。
- **关于"结论2"的质疑**: scenario staging 机制真实存在（等价于 git branch + PR review 的操作数据版本），但"nouns+verbs 组成 sentences"是修辞而非架构论证；把 actions 纳入 ontology 的代价是 action schema 治理成为新瓶颈，文中以"battle-tested modular architecture"一带而过。
- **关于"结论3"的质疑**: "agent 如新员工逐步授权"是好隐喻，但置信度如何度量、由谁裁决扩权、扩权后如何回滚，均无机制描述。fine-tuning 数据回流与 [[Alpha-Transfer|alpha 转移]] 风险直接冲突——decision lineage 既是资产也是最大的泄露面，本文完全回避了这一张力。
- **数据可靠性**: 全部案例为虚构（Onyx）或营销链接（AA/Novartis/Andretti），无一处可验证成效数字。当作"有结构的厂商架构主张"使用。

### 3. 对标
- **[[Organization-as-Agent-Harness]] 的企业数据层实现**: agent harness 理论讲"组织要变成 Agent 可运行的环境"，本文给出该命题在数据架构层的具体答卷——ontology 即企业级 harness 的 context/action/security 三件套。harness 侧（运行时）与 ontology 侧（企业语义层）此前在库中分属两条线索，本文是二者的接合点。
- **与 [[Reverse-Information-Paradox]] 的正面对撞**: Nadella 悖论指出买方为用智能必然泄露专有知识；本文的 decision lineage + fine-tuning 回流机制恰恰是泄露的制度化通道。区别在于：playbook 文献（[[20260727-palantir-ai-sovereignty-alpha-playbook]]）教买方堵漏，本文展示卖方如何把泄露设计成产品特性——两者应成对阅读。
- **scenario staging ≈ git 工作流的操作数据迁移**: explore/stage/commit 三级权限与 branch/PR/merge 同构；文中未明说的推论是——企业操作数据正在经历代码世界十年前的 Git 化，Global Branching（文末提及）即此隐喻的字面化。可迁移到一切"高风险写回需要人工 review"的 agent 部署场景。
- **[[Deployment-Product-Flywheel]] 的数据形态**: "decision lineage 沉淀为 fine-tuning 数据与 prompting 原则"是部署-产品飞轮在数据层的精确表述——FDE 回流的不再只是平台功能，还有决策语料。
- **约束分析（3c）**: 硬约束——决策必须锚定企业实时状态而非检索快照（操作型 AI 的写回本质决定）；软约束——explore/stage/commit 权限分级、动态安全策略（可设计的治理层）；自设约束——"必须单一系统整合四要素"是厂商架构偏好，多系统联邦架构（如 [[Secure-Paved-Path|SSCS]] 式的组件化思路）未必更差。

### 关联概念
- [[Decision-Centric-Architecture]]
- [[Ontology]]
- [[Ontology-Agent]]
- [[Forward-Deployed-Engineer]]
- [[Deployment-Product-Flywheel]]
- [[Organization-as-Agent-Harness]]
- [[Reverse-Information-Paradox]]
- [[Alpha-Transfer]]
