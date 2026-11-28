---
type: source-summary
title: "AI Agent Traps"
canonical_url: "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6372438"
raw_state: index
original_raw_file: "20260707-ai-agent-traps.pdf"
original_body_sha256: "603f0cae8cd8ab944f3e700a169d325120db42239075350d07c8183da71a527c"
indexed_at: "2026-08-25T01:10:28+08:00"
created: 2026-07-07
updated: 2026-11-28
tags:
  - source-summary
  - agent-security
  - adversarial-attack
  - taxonomy
evidence_level: medium
claim_type: extracted
---

# AI Agent Traps

> Raw 生命周期：本地 PDF 已降级为可恢复索引；此页保留六类 taxonomy 的 evidence map，精确引用从 canonical URL 回到 SSRN 原文核验。

> 研究论文提出六类Agent陷阱分类；本轮仅能核对公开检索摘要，SSRN页面与PDF返回403，未核正文或作者机构；不主张首创。

## 证据边界（2026-11-28）

SSRN canonical及PDF均403，六类名称可从公开索引摘要确认；正文中每类例证、首创、引文与缓解方案仍待原文恢复。本轮仅对已读取的本库摘要作语义裁决并回核WASP/Verma原始摘要，不声称全文论文复核或实验复现。

## 编译摘要

### 1. 浓缩

- **核心结论 1**：信息环境本身可能构成Agent攻击面，并非排除模型、身份、工具、供应链或系统漏洞——攻击者不需要入侵模型，只需在 Agent 会访问的网页、邮件、文档中埋设针对机器解析逻辑的恶意内容。
  - 关键证据：[WASP](https://arxiv.org/abs/2504.18575)摘要报告所测配置开始执行对抗指令16%–86%，完整达到攻击目标0%–17%；不可将最大开始执行率当总体成功率。[Verma & Yadav v3](https://arxiv.org/abs/2509.05831v3)摘要：280页均分干净/注入；注入样本中Llama4 Scout超过29%、Gemma9B IT约15%摘要明显变化，非Agent真实外部动作成功率。
- **核心结论 2**：论文按 Agent 运行周期的六个环节，将陷阱分为六类：Content Injection（感知层）、Semantic Manipulation（推理层）、Cognitive State（记忆/学习层）、Behavioural Control（行动层）、Systemic（多 Agent 动态层）、Human-in-the-Loop（人类监督者层）。这个分类轴的价值在于——可用来组织防御和覆盖测试，但类别重叠且不证明一一对应关系。
  - 关键证据：六类陷阱各自引用大量实证工作支撑存在性，从间接 Prompt Injection 到 RAG 知识投毒到多 Agent 感染式越狱。
- **核心结论 3**："The web was built for human eyes; it is now being rebuilt for machine readers." 安全的思维必须从"守住模型"翻成"审计环境"——Agent 走过的每条信息路径都是潜在攻击面。
  - 关键证据：历史编译引用动态差异化内容与字体/文本表示差异作为威胁线索；本轮未重核Zychlinski、Xiong原始研究，不将其当作已确认普遍攻击效果。

### 2. 质疑

- **关于"六类分类的互斥性"**：论文自己承认实践中陷阱可能重叠。例如 Content Injection 中的 HTML 隐藏指令同时是感知层陷阱和行为控制层陷阱——同一攻击从不同角度看落入不同类别。分类轴的实用价值（能否引导差异化防御）尚未被实证检验。
- **关于"Systemic 和 HITL 类别的实证基础"**：这两类目前主要是理论威胁模型，缺乏真实世界中的攻击案例。分类学的长期价值取决于后续研究能否在这些类别中填上实证内容。
- **关于"防御策略的可行性"**：论文提出的缓解路径（训练时加固、推理时内容扫描、生态系统级信任协议）是方向性的，没有给出具体的技术方案或基准。检测和归因的难度可能被低估——语义操纵陷阱与"有说服力的正常内容"之间的边界是模糊的。

### 3. 对标

- **跨域关联 1 — OWASP Top 10**：这篇论文对 Agent 安全的贡献，类似于 OWASP Top 10 对 Web 安全的贡献——将攻击面组织为候选分类地图。OWASP已发布Agentic Applications Top 10（见[[Least-Agency]]）；分类清单不等于强制安全标准，也不证明这篇论文促成其发布。
- **跨域关联 2 — 自动驾驶中的对抗路标**：论文自引的类比准确——自治驾驶需要识别被篡改的路标，Agent 需要识别被篡改的网页。两者的共同结构是"感知层的输入不可信"。
- **跨域关联 3 — 多 Agent 系统病理**：Systemic Traps 与 [[Multi-Agent-System-Pathology]] 高度互补——前者从攻击者视角看多 Agent 脆弱性，后者从组织设计视角看多 Agent 失败模式，两者共享"同质性→同步崩溃"的底层逻辑。

### 关联概念

- [[Agent-Traps]] — 核心框架
- [[Persona-Hyperstition]] — 论文引入的新概念
- [[Agent-Perception-Gap]] — 感知差是部分内容注入利用条件，非必要条件
- [[Prompt-Injection-Risk]] — 已有的注入攻击概念
- [[Multi-Agent-System-Pathology]] — 多 Agent 病理（互补视角）
- [[Agent-Containment]] — 防御侧的核心概念
- [[Model-Safety-Divergence]] — 安全行为分歧
