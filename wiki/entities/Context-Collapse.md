---
type: entity
title: Context Collapse
aliases:
  - Context Collapse
  - context collapse
  - 上下文坍缩
  - 信任域坍缩
definition: "LLM 集成应用的失败模式：来自不同信任域的内容被压扁进同一模型上下文，低信任数据被解释为高信任指令"
created: 2026-07-30
updated: 2026-07-30
tags:
  - agent-security
  - prompt-injection
related_entities:
  - "[[Prompt-Injection-Risk]]"
  - "[[Agent-Traps]]"
  - "[[Shared-Memory-Contamination]]"
  - "[[Agent-Perception-Gap]]"
source_raw:
  - "[[20260622-context-collapse-1-poisoning-copilot-memory]]"
evidence_level: medium
claim_type: mixed
---

# Context Collapse（上下文坍缩）

> [!definition] 定义
> **Context Collapse（上下文坍缩）** 是 Håkon Måløy（2026）在 Microsoft 365 Copilot 协调披露系列中命名的失败模式：来自不同信任域（网页、邮件、文档、工具输出）的内容被压扁进同一个模型上下文，使低信任数据被解释为高信任指令。它是跨域提示注入（XPIA, OWASP LLM01）的统一描述——三个域（记忆、邮件、文档）的三种攻击共享同一机制。

## 核心机制

1. **信任域压扁**：助手要处理外部内容就必须把它读入上下文；一旦进入上下文，外部内容与系统指令、用户请求参与同一计算，来源标签在语义层失效。
2. **LLM 成为唯一仲裁者**：内容有效性的判断落在模型身上，而模型是容错解析器——伪 JSON、近似结构都能被推断为"权威格式"，因此正则/语法过滤无法防御语义等价的无穷变体。
3. **持久化放大**：若坍缩发生在有写权限的路径上（记忆、文档、草稿），一次性注入会变成持久状态或新载体，影响远超当前会话。

## 关键数据点

- **记忆域**（Part 1, 2026-06-22）：攻击者网页经 "Summarize with Copilot" 使 Copilot 持久写入非用户意图的偏好（PoC：瑞典语回复），跨会话、跨 work/web 上下文存活。微软全球缓解：记忆写入与用户实际 prompt/intent 对齐，而非与被摘要内容中的指令对齐。
- **缓解模式的可迁移结构**：微软的修复本质是"写入决策锚定用户意图而非上下文内容"——与 [[Shared-Memory-Contamination]] 的证据-解释分离原则同构。

## 前提与局限性

- **概率性**：XPIA 可利用性是概率性的（上下文、温度、措辞都影响成功率），单次复现失败不能否定漏洞；防御评估同样需要重复试验。
- **命名边界**：context collapse 是描述性统一命名，不是新漏洞类别；其理论深度（为何原则上难解）由系列 Part 3 的架构论证承担——见 [[20260728-context-collapse-3-ai-worming-through-word]]（待编译回填：解释器悖论与 intention/interpretation 分离）。
- **缓解不终结问题**：Part 1/2 的具体向量被缓解，但邮件主题、发件人显示名等元数据字段仍是残余面（Part 2 证据）——信任域隔离必须覆盖全部进入上下文的字段。

## 关联概念

- [[Prompt-Injection-Risk]] — context collapse 是提示注入在"多信任域助手"形态下的结构化表述。
- [[Agent-Traps]] — 六环陷阱框架（感知→推理→记忆→行动）是本机制的攻击分类学视图。
- [[Shared-Memory-Contamination]] — 记忆域坍缩 = 共享记忆污染的攻击侧实例。
- [[Agent-Perception-Gap]] — 人机解析差异（格式剥离后隐藏文本仍可读）是注入得以隐藏的前提。
