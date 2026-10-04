---
type: entity
title: Policy-as-Code for Agent Governance
aliases:
  - Policy-as-Code for Agent Governance
  - policy-as-code for agent governance
  - Agent Governance Policy-as-Code
  - Agent 治理策略即代码
definition: "把 Agent 权限、披露、合规规则和人工升级路径写成可执行策略，在运行时约束模型行动的治理方法"
created: 2026-06-02
updated: 2026-10-05
evidence_level: medium
claim_type: mixed
tags:
  - AI-Agent
  - governance
  - enterprise-ai
related_entities:
  - "[[Agent-Logic]]"
  - "[[Least-Agency]]"
  - "[[Escalation-Based-Human-Oversight]]"
  - "[[Agent-Containment]]"
  - "[[Verifiable-Agent-Engineering]]"
source_raw:
  - "[[20260602-ibm-agent-logic-scalable-ai-adoption]]"
  - "[[20260914-microsoft-ai-code-of-conduct]]"
  - "[[20260915-google-zero-trust-intent-governance]]"
  - "[[20260921-ai-news-multi-agent-supply-chain-execution]]"
---

# Policy-as-Code for Agent Governance

> [!definition] 定义
> **Policy-as-Code for Agent Governance** 是把 Agent 权限、信息披露、合规规则和人工升级路径写成可执行策略，并在运行时约束模型行动的治理方法。

## 核心问题

高风险 Agent 的治理不能只靠 prompt 提醒。Prompt 可以告诉模型“不要泄露敏感信息”或“必要时升级给人类”，但真正的生产约束需要在模型外执行。

Policy-as-code 把这些约束变成 harness 可以检查、拒绝、记录和审计的规则。

## 它约束什么

| 约束对象 | 典型问题 |
|----------|----------|
| 信息披露 | 当前用户是否有权看到这类信息 |
| 工具权限 | Agent 是否可以调用某个系统或执行某个动作 |
| 决策边界 | 哪些情况必须升级给人类 |
| 合规规则 | 输出或动作是否违反行业、公司或监管要求 |
| 审计记录 | 哪条策略允许或拒绝了这次动作 |

## 与 Least Agency 的关系

[[Least-Agency|Least Agency]] 强调限制 Agent 能做什么、做多少次、在哪里做。Policy-as-code 是把这条原则落成运行时机制：不是相信模型会克制，而是让工具和策略层强制执行克制。

## 价值

- 让治理规则可测试、可版本化、可审计。
- 减少模型在合规场景中凭语义猜测边界。
- 把人工升级路径从建议变成执行规则。
- 让同一套治理策略可以跨模型族复用。

## 关键数据点

- IBM 在 CUGA healthcare benchmark 中使用 policy-as-code 做运行时 agent governance，不依赖 prompt 或 fine-tuning。
- 该方法在多个模型族上将任务正确率提高 15% 到 26%。
- 文章强调 least-privilege disclosure、人类升级路径和显式合规规则应作为运行时策略执行，而不是只写进 prompt。

## 前提与局限性

策略即代码只能执行已经被表达出来的规则。真实组织中的政策常常含糊、冲突或依赖情境判断，因此 policy-as-code 的前置工作是把组织治理语言澄清到可执行程度。

如果组织本身没有清楚的权限、责任和升级规则，Agent 治理代码只会把混乱自动化。

Policy-as-code 也不能替代人工责任。它适合拦截、记录、升级和约束动作，但复杂合规判断仍可能需要人类负责人承担最终判断。

## 关联概念

- [[Agent-Logic]] — policy-as-code 是 agent logic 在治理层的形态。
- [[Least-Agency]] — 策略执行的核心原则。
- [[Escalation-Based-Human-Oversight]] — 策略中必须显式表达的人工接管路径。
- [[Agent-Containment]] — 工具与环境层隔离提供确定性边界。

## 治理三层模型中的位置（07-17 深度思考）

Policy-as-Code 处于 Agent 委派治理**三层保证模型**的 L5（表达保证层——规则被写清楚）。但 07-17 深度思考揭示：**表达 ≠ 执行**。

关键发现：
- Policy-as-Code 是"表达保证"——规则被编码了，但代码不能自己强制执行自己。谁阻断违规？如果阻断者是 agent runtime（厂商产品），厂商的利益（不想阻断太多影响体验）和治理目标（该阻断就阻断）之间存在结构性冲突。
- **L0（机制保证）** = Policy-as-Code 所缺失的执行层。L0 需要独立于 agent runtime 的裁决者、不可篡改的审计日志、独立撤销通道。
- **适应式治理的 L5 角色**：在预防→适应范式转换下，L5 的功能不再是"穷尽所有违规规则"（不可能，表达性上限）——而是"将从 L0+L4 检测→L+ 管理者识别的异常模式形式化为可自动执行的规则"。L5 是学习循环的终点和下一轮循环的起点。

产业验证（07-17 联网）：Agat Software 正在商业化"runtime enforcement at the tool invocation layer before execution happens"——这正是 L0 的独立执行层。Policy-as-Code 的规则是输入——独立执行层是执行这些规则的引擎。

与权限棘轮闭合（07-16）：L5 的策略 + L2（临时权限）+ L0（独立撤销）= 权限棘轮破解条件。策略定义了"什么算越权"→ L2 限制了时间窗口→ L0 独立执行撤销。

详见：07-17 深度思考（roundtable 4人3轮+think 7层到底）

## 供应链 transaction policy：把业务授权包络写进执行层（2026-10）

[[20260921-ai-news-multi-agent-supply-chain-execution]] 把 policy-as-code 从抽象权限规则落到具体 transaction constraint：运输改道的成本/SLA 边界、库存变动的金额/数量阈值，以及供应商账户的 draft-only 信任级别，都可以被表达为 tool call 前的可执行规则。

**判断**：面向真实企业交易的 Agent policy 至少应同时约束 **who/what can act、how far it may act、when it must stop、who must authorize the exception**。这类规则的价值在于把“谨慎一点”从 prompt 语言变成确定性的 action envelope。

- **证据**：[[20260921-ai-news-multi-agent-supply-chain-execution]]，供应链 guardrail 段落列出 cost ceiling、SLA delta、inventory threshold 与 draft-only supplier communication。
- **边界**：报道没有证明这些规则由独立 policy engine 实施，也没有给出 bypass、rollback 或 enforcement coverage 数据；因此这里吸收的是规则形状，不把其执行强度外推为已验证的 L0 机制保证。

这一案例也进一步说明 **Policy-as-Code 与 Escalation 是同一执行链的两侧**：policy 先判断动作是否处于包络内，越界后再由 [[Escalation-Based-Human-Oversight]] 决定接收者、上下文包和人工动作。只有二者闭合，multi-agent 的“自主执行”才不是把审批隐性地塞回 prompt。

## 运行时语义治理的增量（2026-09）

**判断**：Policy-as-Code 从静态表达进入工具执行点后，需区分“规则被写清楚”与“每个 action surface 都被拦截、记录、撤销”。

- **证据**：[[20260914-microsoft-ai-code-of-conduct]]、[[20260915-google-zero-trust-intent-governance]]。
- **边界**：Google 的语义策略是厂商架构与示例指标；Microsoft 文档是面向未来模型的公开咨询草案；两者都不能单独证明独立执行已经覆盖生产中的全部行动面。
