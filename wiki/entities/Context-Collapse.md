---
type: entity
title: Context Collapse
aliases:
  - Context Collapse
  - context collapse
  - 上下文坍缩
  - 信任域坍缩
definition: "LLM集成系统中不同来源与信任等级的内容共同参与语义处理，不可信数据可能被误解释为授权指令或污染持久状态的描述性失败模式；不等于信任标签必然失效"
created: 2026-07-30
updated: 2026-11-28
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
  - "[[20260714-context-collapse-2-when-emails-instruct]]"
  - "[[20260728-context-collapse-3-ai-worming-through-word]]"
evidence_level: medium
claim_type: mixed
---

# Context Collapse（上下文坍缩）

> [!definition] 定义
> Håkon Måløy在2026年Microsoft 365 Copilot协调披露系列中使用的描述性概念：外部网页、邮件、文档等不可信信息与可信请求共同进入语义处理，可能影响模型理解任务、生成内容或更新状态。属于跨域提示注入（XPIA）及相关信任边界风险的分析视角，不是数学定理、首创声明或独立标准。

## 核心机制

1. **来源与授权混淆**：可读取不等于有权指挥模型；信息来自内部账号也不自动取得用户授权。
2. **语义判断风险**：同一模型处理可信请求及不可信数据时，可能误判内容的角色。来源标签、规则与模型检测可降低风险，但不宜作为唯一授权机制。
3. **持久状态放大**：记忆、文档或知识库写入可使错误与不可信内容影响后续任务；再次传播依赖实际复用与权限。
4. **副作用不同**：错误回答、生成草稿、持久化写入、实际发送及外部状态改变是不同安全事件，需核对最终状态。

## 关键数据点

| 研究者披露 | 观察及边界 | 当时缓解状态 |
|---|---|---|
| [[20260622-context-collapse-1-poisoning-copilot-memory|Part 1]]（2026-06-22） | 未经授权的偏好进入持久记忆并影响后续会话；受控PoC | 披露者称具体记忆向量已全租户缓解 |
| [[20260714-context-collapse-2-when-emails-instruct|Part 2]]（2026-07-14） | 日程摘要误报、错误告警、潜在敏感信息进入外发草稿；不等于真实日历改写或实际外泄 | CVE-2026-55145；正文路径缓解依赖外部发件人标记，披露时存在元数据残余风险 |
| [[20260728-context-collapse-3-ai-worming-through-word|Part 3]]（2026-07-28） | 受控文档生成与复用传播演示；非真实跨组织感染统计 | 原始载荷及特定变体得到缓解，作者称类别在披露时仍可复现 |

## 架构论证及工程边界

Part 3提出，外部内容参与模型的语义检查，因此单纯依赖模型判断恶意意图存在盲区；将内容交给前置模型也需要关注该模型的风险。此论证支持分层防御，不证明所有检测器必然失败、不证明所有LLM工作流存在固定非零失败率，也不能把本库早期Gödel类比提升为形式证明。可以在模型外限制可执行动作、访问资源、持久写入和最终提交。

Microsoft [Guarding AI memory（2026-06-22）](https://www.microsoft.com/en-us/security/blog/2026/06/22/guarding-ai-memory/)提出意图/来源、模型外隔离、检索风险、生命周期审计和用户控制五项原则；[Trust-Aware Controls（2026-10-12）](https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/building-trust-aware-controls-for-ai-differentiated-handling-of-untrusted-conten/4562160)描述确定性来源分类、受限处理路径、结构化交接和来源标记。确定性的是来源规则和路由/约束，不等于语义转换一定安全。官方明确实际功能取决于配置、许可、发布与租户；未证实所有Word、记忆或元数据向量当前状态。

## 本库综合：跨信任域的最小控制合同

- **读取**：标明来源及数据范围，区分真实工具返回与文本叙述；可访问不代表可信事实或授权。
- **解释**：允许模型提炼信息，保留证据和不确定性；不要把外部内容转换成新的授权要求。
- **写入及提交**：在实际执行点检查身份、任务、资源、目的地、内容及权限；持久记忆、文件、外发等使用与风险相符的独立授权。
- **复用及恢复**：保存受保护的来源、版本、编辑和传播关系，复核有效性，支持更正、撤销及影响范围调查。正常效用与安全效果分别验收。

对LLM WiKi同样适用：Raw是原始证据，不是工作指令；Source Summary是解释而非独立证据；编译层不得仅因多页转引一致而把不可信内容升级为事实或行动权限。

## 前提与局限性

2026-11-28回核三篇本地Raw关键章节、研究者网页及Microsoft官方材料；未运行PoC、未验证真实租户、未独立核查后续全部修复。报告支持特定产品及版本条件下风险可行性；不同输入、模型、配置、权限与任务影响可复现性。重复测试必须注明测试对象、配置、成功判据与实际终态，不能以单次失败宣告无风险。溯源记录只能辅助调查，不保证事实真实性或自动消除已传播内容。

## 关联概念

- [[Prompt-Injection-Risk]] — 指令授权风险与证据污染的不同边界。
- [[Agent-Traps]] — 候选风险覆盖分类，非六阶段固定攻击路径。
- [[Shared-Memory-Contamination]] — 记忆写入、检索与撤销的治理。
- [[Agent-Perception-Gap]] — 人机表示差异是部分风险条件，非必要条件。
- [[AI-Worm]] — 生成物及后续复用造成的传播风险。
- [[Policy-as-Code-for-Agent-Governance]] — 在模型之外约束实际副作用。
