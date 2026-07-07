---
type: source-summary
title: "AI Agent Traps"
source_raw:
  - "[[20260707-ai-agent-traps.pdf]]"
created: 2026-07-07
updated: 2026-07-07
tags:
  - source-summary
  - agent-security
  - adversarial-attack
  - taxonomy
evidence_level: high
claim_type: extracted
---

# AI Agent Traps

> Google DeepMind 研究论文，首次系统性提出 AI Agent 陷阱的六类分类框架。

## 编译摘要

### 1. 浓缩

- **核心结论 1**：AI Agent 的安全威胁本质不是模型被攻破，而是信息环境本身可以被人为构造成陷阱——攻击者不需要入侵模型，只需在 Agent 会访问的网页、邮件、文档中埋设针对机器解析逻辑的恶意内容。
  - 关键证据：WASP 基准测试显示人类手写 Prompt Injection 在 86% 的场景中能部分劫持 Agent（Evtimov et al., 2025）；CSS 隐藏文本改写 AI 摘要输出的比例在 15–29% 之间（Verma & Yadav, 2025）。
- **核心结论 2**：论文按 Agent 运行周期的六个环节，将陷阱分为六类：Content Injection（感知层）、Semantic Manipulation（推理层）、Cognitive State（记忆/学习层）、Behavioural Control（行动层）、Systemic（多 Agent 动态层）、Human-in-the-Loop（人类监督者层）。这个分类轴的价值在于——每一层对应一类差异化的防御策略。
  - 关键证据：六类陷阱各自引用大量实证工作支撑存在性，从间接 Prompt Injection 到 RAG 知识投毒到多 Agent 感染式越狱。
- **核心结论 3**："The web was built for human eyes; it is now being rebuilt for machine readers." 安全的思维必须从"守住模型"翻成"审计环境"——Agent 走过的每条信息路径都是潜在攻击面。
  - 关键证据：动态 Cloaking 技术已能检测 AI Agent 访问并专门推送陷阱内容（Zychlinski, 2025）；字体文件可被人为修改来对 Agent 隐藏恶意指令（Xiong et al., 2025）。

### 2. 质疑

- **关于"六类分类的互斥性"**：论文自己承认实践中陷阱可能重叠。例如 Content Injection 中的 HTML 隐藏指令同时是感知层陷阱和行为控制层陷阱——同一攻击从不同角度看落入不同类别。分类轴的实用价值（能否引导差异化防御）尚未被实证检验。
- **关于"Systemic 和 HITL 类别的实证基础"**：这两类目前主要是理论威胁模型，缺乏真实世界中的攻击案例。分类学的长期价值取决于后续研究能否在这些类别中填上实证内容。
- **关于"防御策略的可行性"**：论文提出的缓解路径（训练时加固、推理时内容扫描、生态系统级信任协议）是方向性的，没有给出具体的技术方案或基准。检测和归因的难度可能被低估——语义操纵陷阱与"有说服力的正常内容"之间的边界是模糊的。

### 3. 对标

- **跨域关联 1 — OWASP Top 10**：这篇论文对 Agent 安全的贡献，类似于 OWASP Top 10 对 Web 安全的贡献——第一次把分散的攻击手段画成了统一的地图。如果这个类比成立，接下来应该看到一个"OWASP for AI Agents"标准的出现。
- **跨域关联 2 — 自动驾驶中的对抗路标**：论文自引的类比准确——自治驾驶需要识别被篡改的路标，Agent 需要识别被篡改的网页。两者的共同结构是"感知层的输入不可信"。
- **跨域关联 3 — 多 Agent 系统病理**：Systemic Traps 与 [[Multi-Agent-System-Pathology]] 高度互补——前者从攻击者视角看多 Agent 脆弱性，后者从组织设计视角看多 Agent 失败模式，两者共享"同质性→同步崩溃"的底层逻辑。

### 关联概念

- [[Agent-Traps]] — 核心框架
- [[Persona-Hyperstition]] — 论文引入的新概念
- [[Agent-Perception-Gap]] — 感知差，所有 Content Injection 的入口
- [[Prompt-Injection-Risk]] — 已有的注入攻击概念
- [[Multi-Agent-System-Pathology]] — 多 Agent 病理（互补视角）
- [[Agent-Containment]] — 防御侧的核心概念
- [[Model-Safety-Divergence]] — 安全行为分歧
