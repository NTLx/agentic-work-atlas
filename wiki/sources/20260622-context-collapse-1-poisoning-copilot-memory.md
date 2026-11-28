---
type: source-summary
title: "Context Collapse, Part 1 - Poisoning Copilot Memory"
source_raw:
  - "[[20260622-context-collapse-1-poisoning-copilot-memory]]"
created: 2026-07-30
updated: 2026-11-28
tags:
  - source-summary
  - agent-security
  - prompt-injection
evidence_level: medium
claim_type: mixed
---

# Context Collapse, Part 1 - Poisoning Copilot Memory

> 来源：En Klype Salt（2026-06-22），Håkon Måløy；与MSRC协调披露的研究者报告；观察行为与缓解状态限定于披露及厂商说明。三部曲第一篇。

## 编译摘要

### 1. 浓缩
- **核心结论1**：作者在受控Copilot网页摘要测试中观察到未经用户授权的持久记忆写入及跨会话影响
  - 关键证据: 原文Security boundary and observed behavior、Impact报告特定语言偏好被持久写入，后续会话以及work/web上下文受到影响；不等于所有租户、所有会话必然复现，也非真实受害者事故。Disclosure status及Mitigating章节称具体向量已全租户缓解、客户无需为该漏洞额外操作；这是2026-06披露时状态。
- **核心结论2**：作者将此失败模式命名为 "context collapse"——来自不同信任域的内容被压扁进同一模型上下文，低信任数据被解释为高信任指令
  - 关键证据: 安全边界应是"不可信网页内容 vs 持久 Copilot Memory"；Copilot 必须读取页面才能摘要，但页面内容应被当作数据而非用户意图。模型能解释多样表达，固定语法匹配不足以单独构成权限边界。分类标签、检测与强制写入授权应分别验收，不断言所有过滤无效。
- **核心结论3**：作者建议对受配置和随机性影响的LLM安全行为采用重复试验
  - 关键证据: 作者建议报告具体版本、环境条件、预期/实际行为和重复试验结果；单次失败不足以排除其他条件下的风险。披露文章没有给出可普遍外推的成功率或生产发生率。

### 2. 质疑
- **关于"结论1"的质疑**: PoC 影响被刻意设为低危（语言偏好）；"攻击者可写入任意持久偏好"是合理外推但未演示高危载荷；记忆写入被缓解后，用户显式要求"记住 X"的流程与注入指令的边界如何划定，新闻未详述——缓解（记忆写入与用户实际 prompt 对齐）依赖"初始 prompt 通常不含记忆指令"这一假设。
- **关于"结论2"的质疑**: "context collapse" 是作者命名的描述性概念，非形式化模型；其与 OWASP XPIA（LLM01）的关系是实例化而非新类别——价值在命名统一了记忆/邮件/文档三个域的同一机制。
- **关于数据可靠性的质疑**: 研究者与厂商均有披露材料，属于一手观察及厂商控制说明；未独立复验真实租户，不能确认整个类别消失或泛化其他产品。

### 3. 对标
- **读取与持久写入的边界**: [[Shared-Memory-Contamination]] 从记忆系统视角指出"语义级注入使事实与推断失去区分度"；该受控PoC支持持久状态受不可信内容影响的风险；用户意图校验是写入授权措施，不等同于事实/推断分类或整个四层记忆治理得到验证。
- **[[Agent-Traps]] 的类别对应**: 本案例命中 Cognitive State Trap（记忆投毒）+ Content Injection Trap（页面隐藏指令），提供输入与持久状态相互影响的产品级PoC，不是六环完整实演。CVE-2026-55145属于系列Part 2，不将其归给Part 1。
- **概率性复现 ↔ 评估重复性**: 漏洞复现需要 repeated trials 与精确 prompt，与 agent 评估中 num_repetitions 的必要性同构（见 [[20260729-similarweb-langsmith-agent-report-evaluation]]）——概率性系统的验证都不能单次定论。
- **约束分析（3c）**: 硬约束——LLM 必须读取内容才能处理内容（"被检查的内容参与检查行为"，Part 3 展开）；软约束——记忆写入策略、信任域隔离（可设计、已缓解）；自设约束——不能把语法过滤当作强制授权。

### 证据边界与后续官方材料（2026-11-28）

回核本地Raw（Disclosure status、Security boundary、Mitigating、Lessons）与[研究者原文](https://enklypesalt.com/posts/context-collapse-part1-poisoning-copilot-memory/)。[Microsoft 2026-06-22 Guarding AI memory](https://www.microsoft.com/en-us/security/blog/2026/06/22/guarding-ai-memory/)明确提及多位研究者的协调披露，介绍Task Adherence、记忆操作审计、既有存储治理及用户控制，并提出五项设计原则：写入前意图/来源检查、模型外隔离、检索时重新评估、全生命周期可见性、用户控制。厂商区分已有能力与未来指导方向，功能受配置/许可/可用性限制。不是所有写入均有确定性的语义正确性保证，也不能把Måløy当作该类问题唯一发现者。

**本库综合**：将持久写入作为单独授权动作，记录来源、写入人/代理身份、目的、时间与版本；区分用户明确授权、系统业务规则、外部证据和模型推断。检索旧记忆时复核有效性及范围，支持撤销、过期和影响范围调查。不把外部内容或模型判断当作写权限来源。未复跑PoC或检查实际租户。

### 关联概念
- [[Context-Collapse]]
- [[Prompt-Injection-Risk]]
- [[Shared-Memory-Contamination]]
- [[Agent-Traps]]
- [[Agent-Perception-Gap]]
