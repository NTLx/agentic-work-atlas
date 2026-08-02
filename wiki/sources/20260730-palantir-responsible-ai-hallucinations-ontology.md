---
type: source-summary
title: "Reducing Hallucinations with the Ontology in Palantir AIP (Engineering Responsible AI, #1)"
source_raw:
  - "[[20260730-palantir-responsible-ai-hallucinations-ontology]]"
created: 2026-08-02
updated: 2026-08-02
tags:
  - source-summary
  - palantir
  - responsible-ai
  - hallucination
  - ontology
  - agentic-engineering
evidence_level: medium
claim_type: mixed
---

# Reducing Hallucinations with the Ontology in Palantir AIP — 三层防御：Grounding / Handoff / HITL

> 来源：Palantir Blog（2024-07-09，约 11 分钟阅读，Engineering Responsible AI 系列 #1）。**证据定级 medium**：核心论点（next-token 预测 ≠ 真相检索；幻觉是生成能力的内禀副产品而非可训练消除）属于 LLM 本质属性共识，不依赖 Palantir 产品；产品包装集中在 AIP Logic 的三种缓解机制。案例为虚构（Titan Industries），无 benchmark / 失效率数据，编译定位为 "vendor pattern extraction" 而非 "empirical validation"。注 [1] 主动去拟人化（responding/replying/reasoning 皆为隐喻），是负责任叙事的工程姿态。

## 编译摘要

### 1. 浓缩
- **核心结论1**：幻觉是 LLM 生成能力的**结构性副产品**，不可靠 retrain 消除——训练目标是预测"统计上最像的下一个 token"，而非返回 truthful/accurate 答案；使文本流畅有创造力的特性与产生幻觉的特性是同一特性
  - 关键证据: "the job of an LLM is to just produce text that is statistically likely to *look* plausible"；"aspects of hallucinations are part and parcel of the generative capability"；且即使相关信息在训练数据中，模型仍可能预测不出正确答案——grounding 因此是必需而非可选。
- **核心结论2**：架构答案是**按幻觉机制分层的三层防御**，每层对应一类幻觉成因：(a) **Query Ontology grounding**——企业私有数据不在训练集中 → 让 LLM 经 search-query 间接访问 Ontology（Palantir 命名为 OAG，Ontology-Augmented Generation，RAG 的领域特化）；(b) **Tool handoff to trusted logic**——next-token 预测是错误的计算类型（用算术模拟距离）→ handoff 给确定性函数（Haversine）；(c) **Human-in-the-loop review**——前两层仍可能漏 → AI 提案 "queue up" 等待 domain expert approve/reject，不直接写回外部系统
  - 关键证据: Titan Industries 三组递进演示：(a) 询问分销中心城市 → 凭空列出错误城市 → 加 Query Ontology 工具后正确；(b) 卡车抛锚最近中心 → 返回 Albany（应为 Providence）→ 加 Haversine Function 后正确；(c) 库存短缺工单 → 提取 → 检索 → 提议补货/调拨 → 入审核队列。
- **核心结论3**：三层防御的隐含前提是"承认模型一定会幻觉"——因此最后一层不是技术层而是**组织层**（human review + ledger-style audit），且三层都建在同一个 Ontology 的 data / logic / action 三要素上
  - 关键证据: "no matter how well we design our use of LLMs, hallucinations are a potential side-effect"；Human-AI teaming 被定位为同时解决 accountability、outcome 可解释与 human-centric 三个问题的设计模式，不止是防幻觉。

### 2. 质疑
- **关于"结论1"的质疑**: "幻觉不可训练消除"在 2024-07 是合理立场，但表述偏绝对——RLHF/Constitutional AI 等后训练手段已能显著降低特定类型幻觉（虽未消除）。准确的弱表述应为"不可仅靠 retrain 解决"，文中"not feasible"的框架 conveniently 把解决方案导向了 Palantir 的产品层。
- **关于"结论2"的质疑**: 三组演示都是虚构公司 Titan Industries 的玩具场景，无失效率、无消融、无对照——"OAG 减少幻觉"是机制论证而非实证论证。且 grounding 层有效性完全依赖 Ontology 建模质量与数据新鲜度（见 [[Ontology]] 前提与局限性）：ABox 事实延迟或缺失时，grounding 只会给出"有据可查的错误"。
- **关于"结论3"的质疑**: 文章把 human review 当作兜底灵药，但库内已有反向证据：[[Human-Governor-Agent-Operator]] 记录的 Anthropic 数据显示 93% 权限提示被批准，CUA Oversight 论文显示高风险任务成功阻止率仅 12.8%——**审批在安全需求最高的场景中表现最差**。vendor 展示了 queue 的理想形态，未讨论 queue 的退化形态（橡皮图章化）。
- **数据可靠性**: 无学术引用支撑机制主张（注 [1] 仅为拟人化警告 + 综述链接）；核心机制可独立验证，产品效果声明不可。

### 3. 对标
- **系列互补结构**：本篇（#1）处理*事实正确性*，[[20260730-palantir-responsible-ai-black-box-explainability|#2]] 处理*推理路径透明性*，[[20260730-palantir-responsible-ai-evals-prototype-to-production|#3]] 处理*开发期评测*——三篇共用同一个 Titan 分销中心案例但取三个截面：#1 用 Haversine handoff 修**正确性**，#2 用同案例演示 LLM Debugger 的**可解释性**，构成 "correctness + transparency + evals" 三脚架。
- **与 [[Deterministic-Retrieval]] 同族**：OAG 与确定性检索、DoorDash "RAG 倒置"（LLM 从检索列表选取而非生成）属于同一设计家族——"把 LLM 关进无聊可靠的空间"；差异在于 OAG 的检索对象是企业 Ontology 的对象/属性元数据，而非领域数据库隧道。
- **HITL queue 与 Governor 模式的对偶**：AIP 的 "queue up for approval" 是 [[Human-Governor-Agent-Operator]] 的 vendor 正面实现，而库内该条目记录的四层根因模型（tempo 错配 / 偏差正常化 / System 1 接管 / 有限理性）正是其退化路径——正面模式与失败模式应在同一视图内对照，见 [[Escalation-Based-Human-Oversight]]。
- **约束分析（3c）**：硬约束——LLM 输出是概率性的，私有数据不在训练集中（世界规律）；软约束——Ontology 建模完备性、tool 接口设计、queue 审批粒度（工程选择）；自设约束——"幻觉只能靠模型改进解决"被本文证伪，但"加了 human review 就安全"在高风险高频场景中是自设安慰。

### 关联概念
- [[Ontology]]
- [[Transparent-Tool-Handoff]]
- [[Human-Governor-Agent-Operator]]
- [[Deterministic-Retrieval]]
- [[Escalation-Based-Human-Oversight]]
- [[Decision-Centric-Architecture]]
