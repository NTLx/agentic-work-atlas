---
type: source-summary
title: "Context Collapse, Part 2 - When Emails Instruct"
source_raw:
  - "[[20260714-context-collapse-2-when-emails-instruct]]"
created: 2026-07-30
updated: 2026-07-30
tags:
  - source-summary
  - agent-security
  - prompt-injection
evidence_level: medium
claim_type: mixed
---

# Context Collapse, Part 2 - When Emails Instruct

> 来源：En Klype Salt（2026-07-14），Håkon Måløy；MSRC 协调披露，产生 CVE-2026-55145。三部曲第二篇。

## 编译摘要

### 1. 浓缩
- **核心结论1**：外部邮件正文中的隐藏指令可操纵 Outlook Copilot 的行为，三个变体覆盖完整性与机密性
  - 关键证据: 白底白字 JSON 指令（Copilot 剥离格式后仍可读）；Variant 1 直接改行为（日历事件时间前移 2 小时）；Variant 2 伪造 office365_search 工具返回结构，使 Copilot 相信"组织正遭受网络攻击"并指示用户断网；Variant 3 将用户邮箱/OneDrive 内部摘要插入发往攻击者的回复草稿，用 50 个换行藏于视口外与签名之下。攻击者只需知道受害者邮箱地址。
- **核心结论2**：微软的缓解是权限分离架构——外部邮件正文先经独立的低权限 agent 摘要，只有摘要进入主 Copilot 会话
  - 关键证据: CVE-2026-55145（2026-07-14，七月 Patch Tuesday 周期）；缓解依赖客户启用 Exchange Online 外部发件人标记（采纳缺口）；主题字段与发件人显示名在披露时仍是残余攻击面（可靠性较低但证明元数据需要同等信任域处理）。
- **核心结论3**：三条结构性含义
  - 关键证据: (a) LLM 成为内容有效性的唯一仲裁者，而内容进入上下文后 LLM 并不适任此职；(b) 单一注入点派生多种利用能力——同一注入方法因 LLM 通用能力与暴露工具不同而表现为截然不同的行为，因此漏洞范围评估必须包含底层系统与工具，不只是攻击向量；(c) 信息完整性损害易被低估——Copilot 对被注入内容的响应是短暂的，但用户据之采取的行动持久存在。

### 2. 质疑
- **关于"结论1"的质疑**: Variant 1/2 是按会话短暂的，实际影响依赖用户采信并行动（作者自认 PoC 低危）；Variant 3 有人类最后一道门（Copilot 不能自动发送），但 UI 隐藏手法（视口外 + 签名下方 + "草稿似被删除"错觉）系统性削弱了这道门——人类门的存在不等于人类门的有效。
- **关于"结论2"的质疑**: 双 LLM 缓解的有效性依赖外部发件人标记被启用——这是组织采纳问题而非技术问题；残余面（主题、显示名）证明信任域隔离必须覆盖所有进入上下文的字段，部分隔离只是提高门槛。
- **关于数据可靠性的质疑**: 一手协调披露 + CVE，证据等级高；单一厂商生态（M365），但机制（工具结果伪造、草稿注入）可迁移到任何带工具调用与内容生成能力的助手。

### 3. 对标
- **伪造工具结果 = 攻击 agent 的"内部世界"**: Variant 2 不是让模型"做坏事"，而是让它相信自己的工具返回了某事——这命中 [[Agent-Traps]] 的 Content Injection（格式伪装）与 Behavioural Control（诱导操作）连锁，且比直接指令更难被模型侧识别，因为它模仿的是系统内部结构而非用户/外部指令。
- **双 LLM 缓解 ↔ "LLMs all the way down" 预告**: 本篇的缓解模式（低权限 agent 先摘要）正是 Part 3 架构论证将要审视的对象——把检测外移给另一个 LLM 只是把同一问题外推（见 [[20260728-context-collapse-3-ai-worming-through-word]] 摘要）。缓解有效（降低成功率）与原则上不完备可以同时成立。
- **数据外泄模式**: Variant 3 是助手辅助的聚合泄露——内部信息经合法摘要能力流向攻击者，与 [[MosaicLeaks]]/[[Mosaic-Effect]] 的"碎片聚合成敏感整体"结构一致，只是聚合与外发都由助手自动完成。
- **约束分析（3c）**: 硬约束——助手要回复邮件就必须读邮件（处理即暴露）；软约束——外部发件人标记、权限分离架构（可部署）；自设约束——"模型会识别恶意指令"被 Variant 2 反例（模型把伪造工具结果当权威内部数据）。

### 关联概念
- [[Context-Collapse]]
- [[Prompt-Injection-Risk]]
- [[Agent-Traps]]
- [[Agent-Perception-Gap]]
- [[MosaicLeaks]]
