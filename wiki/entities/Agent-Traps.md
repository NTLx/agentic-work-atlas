---
type: entity
title: "Agent Traps"
aliases:
  - Agent Traps
  - Agent 陷阱
  - AI Agent 陷阱
  - 网页陷阱
definition: "嵌入在网页、邮件、文档等数字资源中，专门针对 AI Agent 的解析逻辑设计、用以操纵或利用其行为的恶意内容分类框架——按 Agent 运行周期的六个环节（感知→推理→记忆→行动→多Agent→人类）系统化"
created: 2026-07-07
updated: 2026-07-07
tags:
  - agent-security
  - adversarial-attack
  - taxonomy
evidence_level: high
claim_type: extracted
related_entities:
  - "[[Prompt-Injection-Risk]]"
  - "[[Persona-Hyperstition]]"
  - "[[Agent-Perception-Gap]]"
  - "[[Multi-Agent-System-Pathology]]"
  - "[[Agent-Containment]]"
  - "[[Model-Safety-Divergence]]"
source_raw:
  - "[[20260707-ai-agent-traps.pdf]]"
---

# Agent Traps（Agent 陷阱）

> [!definition] 定义
> **Agent Traps** 是任何嵌入在 Agent 会消费的数字资源（网页、邮件、文档、图片、API 响应等）中的内容元素——其设计目标不是让人看到，而是让解析它的 AI Agent 照做，结果是攻击者获益。这是 Google DeepMind（Franklin, Tomašev, Jacobs, Leibo & Osindero）提出的首个系统性分类框架。

## 六类陷阱框架

按 Agent 运行周期的六个环节排列——每一类针对一个可被攻击的环节，每一类暗示一类差异化的防御策略：

| 陷阱类别 | 攻击目标 | 核心机制 | 实证成熟度 | 典型防御 |
|----------|----------|----------|-----------|----------|
| **Content Injection Traps** | 感知层 | 利用人机解析差异（CSS 隐藏、HTML 注释、隐写编码、动态披风）嵌入不可见指令 | 高 | 内容消毒层、输入剥离 |
| **Semantic Manipulation Traps** | 推理层 | 利用框架效应、锚定偏差、情感语言操纵 Agent 的推理输出，不直接下指令 | 高 | 输出监控、偏差检测 |
| **Cognitive State Traps** | 记忆/学习层 | 污染 RAG 知识库、潜伏记忆投毒、毒化上下文学习示范 | 中 | 知识库审计、来源校验 |
| **Behavioural Control Traps** | 行动层 | 嵌入式越狱序列、数据窃取诱导、子 Agent 劫持生成 | 高 | 输出消毒、网络出口控制 |
| **Systemic Traps** | 多 Agent 动态 | 拥堵信号、级联崩溃、隐性共谋、片段组合、女巫攻击 | 低（理论为主） | 异质性设计、反协同监控 |
| **Human-in-the-Loop Traps** | 人类监督者 | 利用自动化偏差、审批疲劳、社会工程学攻击人类审批者 | 低（早期探索） | 审批节奏设计、偏差培训 |

## 框架的核心洞察

1. **感知差是所有陷阱的入口**：Agent 解析 HTML 源码树、像素数组、元数据标签——和人类消费渲染后的视觉页面是完全不同的路径。这个不可消除的差异是 Content Injection 的基础。

2. **六环可以连锁**：攻击者可以在感知层埋指令 → 推理层把它合理化 → 记忆层固化 → 行动层执行 → 多 Agent 层放大 → 人类监督者批准。防住一环不等于安全。

3. **对齐解决不了环境攻击**：模型层面的对齐训练对语义操纵、记忆投毒、多 Agent 级联几乎无效——因为这些攻击不直接对模型"下命令"。

## 关键数据点

- WASP 基准：简单 Prompt Injection 在 86% 场景中部分劫持 Agent（Evtimov et al., 2025）
- HTML 隐藏指令改写 AI 摘要：15–29% 成功率（Verma & Yadav, 2025）
- AgentPoison：记忆/知识库投毒，攻击成功率 > 80%，仅需 < 0.1% 数据投毒（Chen et al., 2024）
- Web-use Agent 数据窃取：5 个不同 Agent 中攻击成功率 > 80%（Shapira et al., 2025）
- M365 Copilot Echoleak：单封邮件绕过分类器外泄特权上下文（Reddy & Gujral, 2025）
- Android 通知注入：多模态 Agent 攻击成功率最高 93%（Chen et al., 2025）
- 多 Agent 感染式越狱：一张图在所有 Agent Pairwise 交互后几乎全部感染（Gu et al., 2024）

## 前提与局限性

- **分类互斥性不足**：论文自认实践中陷阱可能重叠——同一攻击可能同时属于多个类别；分类的实用价值（能否引导差异化防御）尚未被实证检验
- **Systemic 和 HITL 类别的实证缺口**：目前主要是理论威胁模型，缺乏真实攻击案例
- **防御策略是方向性的**：论文提出的缓解路径（训练加固、内容扫描、生态信任协议）没有给出具体技术方案或基准
- **前提**：论文假设六类分类对防御策略设计有意义——这个假设需要后续研究来验证

## 关联概念

- [[Prompt-Injection-Risk]] — Agent Traps 是 Prompt Injection 的超级；注入只是六类中的两种（Content Injection + Behavioural Control）的核心机制
- [[Multi-Agent-System-Pathology]] — Systemic Traps 是从攻击者视角看多 Agent 脆弱性，与多 Agent 病理学互补
- [[Agent-Containment]] — Containment 是主要的防御架构；Agent Traps 告诉你 Containment 要防"什么"
- [[Persona-Hyperstition]] — 六类中最新颖的子概念，独立成 Entity
- [[Agent-Perception-Gap]] — 感知差是所有 Content Injection 的共同入口，独立成 Entity
- [[Model-Safety-Divergence]] — Agent Traps 解释了安全行为分歧的"环境侧"原因
