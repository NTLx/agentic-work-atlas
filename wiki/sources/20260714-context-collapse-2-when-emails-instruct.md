---
type: source-summary
title: "Context Collapse, Part 2 - When Emails Instruct"
source_raw:
  - "[[20260714-context-collapse-2-when-emails-instruct]]"
created: 2026-07-30
updated: 2026-11-28
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
- **核心结论1**：作者报告三种受控Outlook Copilot行为，涉及回答完整性与潜在机密性损害
  - 关键证据: 原文Observed behavior与Impact分别报告日程摘要中的时间误报（未证明日历事件本身被修改）、错误 operational alert，以及内部信息进入外发回复草稿。第三例依赖可访问数据、产品配置及用户发送动作；草稿生成与实际泄露不同。外部发件是威胁模型，不等于仅知邮箱即可无条件造成影响。
- **核心结论2**：据研究者报告，厂商针对邮件正文引入受限处理路径，再将摘要交给主会话；属于分层缓解，不是所有字段、动作及输出都已强制隔离
  - 关键证据: CVE-2026-55145（2026-07-14，七月 Patch Tuesday 周期）；缓解依赖客户启用 Exchange Online 外部发件人标记（采纳缺口）；作者在当时观察到邮件主题和显示名残余风险（可靠性较低）；不能直接断言2026-11仍未修复。
- **核心结论3**：三条结构性含义
  - 关键证据: (a) 仅依赖主模型判断外部内容是否有指令权威存在风险；来源及实际权限可在模型外强制；(b) 单一注入点派生多种利用能力——同一注入方法因 LLM 通用能力与暴露工具不同而表现为截然不同的行为，因此漏洞范围评估必须包含底层系统与工具，不只是攻击向量；(c) 信息完整性损害易被低估——Copilot 对被注入内容的响应是短暂的，但用户据之采取的行动持久存在。

### 2. 质疑
- **关于"结论1"的质疑**: Variant 1/2 是按会话短暂的，实际影响依赖用户采信并行动（作者自认 PoC 低危）；Variant 3 有人类最后一道门（Copilot 不能自动发送），但审批者可能无法充分看见或理解完整草稿。应验收用户看到的实际内容、收件人及提交的最终状态，而不是只检查有无发送按钮。
- **关于"结论2"的质疑**: 双 LLM 缓解的有效性依赖外部发件人标记被启用——这是技术设计、配置覆盖和组织采纳共同决定的有效性问题；应验证所有参与授权/风险判断的输入及实际动作路径，不能只验正文。
- **关于数据可靠性的质疑**: 一手协调披露与公开漏洞记录支持特定产品风险；不能据此判定任意助手均可利用。MSRC页面本轮仅返回JS壳，NVD页面无可读正文；通过公开CNA记录及Microsoft 10月说明交叉核对CVE编号、类型与配置要求，不做现行全租户修复确认。

### 3. 对标
- **伪造工具结果 = 攻击 agent 的"内部世界"**: Variant 2 不是让模型"做坏事"，而是让它相信自己的工具返回了某事——这命中 [[Agent-Traps]] 的 Content Injection（格式伪装）与 Behavioural Control（诱导操作）连锁，需要区分工具框架提供的真实调用结果与文本对工具结果的叙述；本轮无不同注入类型识别难度对照。
- **双 LLM 缓解 ↔ "LLMs all the way down" 预告**: 本篇的缓解模式（低权限 agent 先摘要）正是 Part 3 架构论证将要审视的对象——作者讨论前置模型同样存在检测盲区（见 [[20260728-context-collapse-3-ai-worming-through-word]] 摘要）。受限路径可能降低风险，具体覆盖与误拒绝需测量；前置模型并非唯一可用控制，来源分类、能力限制与资源端授权可以独立实现。
- **潜在数据披露模式**: Variant 3 涉及助手生成包含内部摘要的外发草稿，与 [[MosaicLeaks]]/[[Mosaic-Effect]] 的"碎片聚合成敏感整体"结构一致，但此PoC只自动形成草稿，最终发送仍依赖人类动作；不将潜在披露写成已观测数据外泄。
- **约束分析（3c）**: 硬约束——助手要回复邮件就必须读邮件（处理即暴露）；软约束——外部发件人标记、权限分离架构（可部署）；自设约束——"模型会识别恶意指令"被 Variant 2 反例（模型把伪造工具结果当权威内部数据）。

### 后续官方说明与证据边界（2026-11-28）

回核[研究者原文](https://enklypesalt.com/posts/context-collapse-part2-when-emails-instruct/)及本地Raw的Disclosure status、Observed behavior、Impact、Mitigating。Microsoft在[2026-10-12 Trust-Aware Controls](https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/building-trust-aware-controls-for-ai-differentiated-handling-of-untrusted-conten/4562160)说明：确定性来源信号、受限内容处理、来源标记、结构化交接及主模型综合；它强调风险降低而非全类别消除，初期覆盖外部通信等高风险内容，其他来源仍在探索，要求启用相应Outlook发件人标记并参考CVE配置，功能随发布与租户环境变化。[CNA记录镜像](https://app.opencve.io/cve/CVE-2026-55145)列明该漏洞为Outlook Copilot Tampering（2026-07-14发布），厂商评分与其他评估口径不可混用；未核实际租户配置或运行效果。

**本库综合**：在检索层标记来源，在工具框架保留真实结构化结果，在提交层检查用户授权、目的地、内容与敏感数据范围；不让低权限摘要获得原本没有的权限。源可信度、数据访问权限、动作授权与批准后的真实副作用是不同判定。未复跑PoC。

### 关联概念
- [[Context-Collapse]]
- [[Prompt-Injection-Risk]]
- [[Agent-Traps]]
- [[Agent-Perception-Gap]]
- [[MosaicLeaks]]
