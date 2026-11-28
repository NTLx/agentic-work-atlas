---
type: entity
title: "Agent Traps"
aliases:
  - Agent Traps
  - Agent 陷阱
  - AI Agent 陷阱
  - 网页陷阱
definition: "面向AI Agent环境侧风险的六类候选分类，覆盖内容注入、语义操纵、认知状态、行为控制、系统性及人类监督；类别可重叠，不限于隐藏指令"
created: 2026-07-07
updated: 2026-11-28
tags:
  - agent-security
  - adversarial-attack
  - taxonomy
evidence_level: medium
claim_type: extracted
related_entities:
  - "[[Prompt-Injection-Risk]]"
  - "[[Persona-Hyperstition]]"
  - "[[Agent-Perception-Gap]]"
  - "[[Multi-Agent-System-Pathology]]"
  - "[[Agent-Containment]]"
  - "[[Model-Safety-Divergence]]"
  - "[[Context-Collapse]]"
  - "[[AI-Worm]]"
source_raw:
  - "[[20260707-ai-agent-traps.pdf]]"
  - "[[20260622-context-collapse-1-poisoning-copilot-memory]]"
  - "[[20260714-context-collapse-2-when-emails-instruct]]"
  - "[[20260728-context-collapse-3-ai-worming-through-word]]"
---

# Agent Traps（Agent 陷阱）

> [!definition] 定义
> **Agent Traps** 是任何嵌入在 Agent 会消费的数字资源（网页、邮件、文档、图片、API 响应等）中的内容元素——可利用模型对信息的解释、状态更新、行动或人类监督的弱点；也可能使用人类可见内容。分类来自《AI Agent Traps》历史编译；上一轮SSRN正文及PDF返回403，仅核到公开摘要，首创、机构与完整分类论证未重核，不作确定断言。

## 六类陷阱框架

六类用于组织风险面与候选控制；不代表固定顺序、互斥类别或一一对应防御。下表是历史分类的工程解释，不是原论文经验证的成熟度评分。

| 陷阱类别 | 关注对象 | 候选防御/验收 |
|---|---|---|
| Content Injection Traps | 不可信输入及指令解释 | 来源标签、最小必要表示、独立授权 |
| Semantic Manipulation Traps | 事实与判断受不可信证据影响 | 权威来源、独立核验、冲突处理 |
| Cognitive State Traps | 持久状态、记忆与知识 | 写入合同、provenance、撤销及回归 |
| Behavioural Control Traps | 工具与外部副作用 | 资源端权限、完整中介、实际终态 |
| Systemic Traps | 多组件或多Agent传播 | 隔离、委派授权、跨组件监测 |
| Human-in-the-Loop Traps | 人类监督与决策 | 可见证据、明确动作授权、可拒绝与追溯 |

## 框架的核心洞察

1. **感知差是 Content Injection 的重要入口**：Agent 解析 HTML 源码树、像素数组、元数据标签时，可能消费人类界面未直接呈现的信息层。这个差异为隐藏内容攻击提供了条件，但 Semantic Manipulation、Cognitive State 等其他陷阱并不都依赖感知差。

2. **类别可能连锁**：输入、状态、行动与监督风险可能相互影响，但不是每次都经过六类。需针对实际系统验证控制与传播边界。

3. **模型对齐不能单独覆盖环境攻击**：语义操纵、记忆投毒、多 Agent 级联和证据污染涉及输入来源、状态写入与系统权限等模型外因素，因此仅依赖模型层对齐无法构成完整防御。

## 关键数据点

- [WASP v3摘要](https://arxiv.org/abs/2504.18575)：报告部分成功最高86%，完整目标完成较困难；非完整成功率。
- [Verma & Yadav v3摘要](https://arxiv.org/abs/2509.05831v3)：280页均分干净与注入样本，所测两模型的注入样本摘要明显变化比例超过29%及约15%；非真实外部行动成功率。
- 其他历史论文的精确攻击比例、样本量和阈值本轮未重新核对，撤出确定量化结论，保留历史Git及源索引。
- Context Collapse三篇协调披露描述M365 Copilot的持久记忆、邮件处理与文档传播风险；部分机制与六类重叠，是不同受控演示，不证明在单次真实事故中完整走通六环，也不证明全体用户受影响或跨组织实际传播。2026-11-28定向回看本库三篇摘要；尚需逐篇重核原披露、缓解条件及当前状态。详见[[Context-Collapse]]、[[AI-Worm]]。

## 前提与局限性

- **分类互斥性不足**：分类可能重叠；未核完整论文或系统综述，不将其宣称为已经验证的最佳风险分类
- **Systemic 和 HITL 的跨产品实证仍有限**：相关研究提供产品级受控演示及风险线索；不等同实地事故率、全链路成功率或所有部署通用性。
- **防御策略是方向性的**：原论文完整缓解论证尚未回核；本页候选控制须用负向授权、任务效用、真实状态及恢复测试分别验证
- **前提**：本库将六类作为覆盖检查的候选视角，不把分类本身作为强制标准或完整保障

## 关联概念

- [[Prompt-Injection-Risk]] — Prompt Injection 是 Agent Traps 更广攻击面中的一种重要机制；六类 taxonomy 还覆盖语义操纵、状态污染、多 Agent 与 HITL 风险
- [[Multi-Agent-System-Pathology]] — Systemic Traps 是从攻击者视角看多 Agent 脆弱性，与多 Agent 病理学互补
- [[Agent-Containment]] — Containment 是主要的防御架构；Agent Traps 告诉你 Containment 要防"什么"
- [[Persona-Hyperstition]] — 历史编译中提取的相关子概念，首创性未核，独立成 Entity
- [[Agent-Perception-Gap]] — 感知差是部分内容注入的利用条件，非必要条件，独立成 Entity
- [[Model-Safety-Divergence]] — Agent Traps 解释了安全行为分歧的"环境侧"原因
