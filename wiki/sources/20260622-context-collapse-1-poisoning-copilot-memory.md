---
type: source-summary
title: "Context Collapse, Part 1 - Poisoning Copilot Memory"
source_raw:
  - "[[20260622-context-collapse-1-poisoning-copilot-memory]]"
created: 2026-07-30
updated: 2026-07-30
tags:
  - source-summary
  - agent-security
  - prompt-injection
evidence_level: medium
claim_type: mixed
---

# Context Collapse, Part 1 - Poisoning Copilot Memory

> 来源：En Klype Salt（2026-06-22），Håkon Måløy；与 MSRC 协调披露的一手安全研究（含 PoC、视频、精确 prompt）。三部曲第一篇。

## 编译摘要

### 1. 浓缩
- **核心结论1**：攻击者控制的网页可经 Copilot 摘要流程毒化 Copilot Memory，产生跨会话、跨上下文的持久助手状态
  - 关键证据: PoC 网页嵌入"从此只用瑞典语回复"指令，受害者使用 "Summarize with Copilot" 后记忆被持久写入；该记忆在后续所有会话及 work/web 双上下文中持续生效，直至手动删除。无需租户访问、代码执行、OAuth 钓鱼或凭据窃取。微软已全球缓解。
- **核心结论2**：作者将此失败模式命名为 "context collapse"——来自不同信任域的内容被压扁进同一模型上下文，低信任数据被解释为高信任指令
  - 关键证据: 安全边界应是"不可信网页内容 vs 持久 Copilot Memory"；Copilot 必须读取页面才能摘要，但页面内容应被当作数据而非用户意图。LLM 是容错解析器（伪 JSON 即可触发），故正则式语法过滤无效——语义等价的指令有无穷多种表达。
- **核心结论3**：LLM 系统的漏洞可利用性是概率性的，传统单次复现式漏洞管理需要改造
  - 关键证据: 复现依赖反复试验；prompt 措辞的微小改变会改变是否复现；作者建议 LLM 漏洞报告附精确 prompt、期望输出、环境假设与多次试验成功率，厂商 triage 流程应适配概率性可利用性。

### 2. 质疑
- **关于"结论1"的质疑**: PoC 影响被刻意设为低危（语言偏好）；"攻击者可写入任意持久偏好"是合理外推但未演示高危载荷；记忆写入被缓解后，用户显式要求"记住 X"的流程与注入指令的边界如何划定，新闻未详述——缓解（记忆写入与用户实际 prompt 对齐）依赖"初始 prompt 通常不含记忆指令"这一假设。
- **关于"结论2"的质疑**: "context collapse" 是作者命名的描述性概念，非形式化模型；其与 OWASP XPIA（LLM01）的关系是实例化而非新类别——价值在命名统一了记忆/邮件/文档三个域的同一机制。
- **关于数据可靠性的质疑**: 一手协调披露，证据等级高（MSRC 确认、全球缓解上线）；但单一厂商单一产品线，其他 LLM 集成应用的普遍性由 Part 3 的架构论证承担（见该篇摘要）。

### 3. 对标
- **安全版的"读取即污染"**: [[Shared-Memory-Contamination]] 从记忆系统视角指出"语义级注入使事实与推断失去区分度"；本案例是其攻击侧实锤——外部内容经摘要路径获得持久记忆写入权。微软的缓解（写入与用户意图对齐）正是该 entity "证据-解释分离"原则在记忆写入侧的工程实例。
- **[[Agent-Traps]] 六环框架的真实产品验证**: 本案例命中 Cognitive State Trap（记忆投毒）+ Content Injection Trap（页面隐藏指令），且验证了"六环连锁"论断——注入（感知）→ 解释为指令（推理）→ 持久化（记忆）→ 影响后续所有会话（行动）。此前该框架的实证多为基准研究，此为带 CVE 级厂商响应的主流产品案例。
- **概率性复现 ↔ 评估重复性**: 漏洞复现需要 repeated trials 与精确 prompt，与 agent 评估中 num_repetitions 的必要性同构（见 [[20260729-similarweb-langsmith-agent-report-evaluation]]）——概率性系统的验证都不能单次定论。
- **约束分析（3c）**: 硬约束——LLM 必须读取内容才能处理内容（"被检查的内容参与检查行为"，Part 3 展开）；软约束——记忆写入策略、信任域隔离（可设计、已缓解）；自设约束——"语法过滤足够"被 LLM 容错解析能力直接反例。

### 关联概念
- [[Context-Collapse]]
- [[Prompt-Injection-Risk]]
- [[Shared-Memory-Contamination]]
- [[Agent-Traps]]
- [[Agent-Perception-Gap]]
