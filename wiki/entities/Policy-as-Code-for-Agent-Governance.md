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
updated: 2026-11-28
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
  - "[[20260930-databricks-agentic-apps-ai-sprawl]]"
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
- IBM博客自报CUGA healthcare用例多模型族准确率改善15%–26%（未明确百分比或百分点），非通用安全或合规保证。
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

## Delegation-time down-scoping：调用者权限 ≠ Agent 权限（2026-10）

Databricks 的 refund 示例（[[20260930-databricks-agentic-apps-ai-sprawl]]）补充了 policy-as-code 的一个关键授权语义：发起请求的员工可以拥有广泛客户账户权限，但执行单笔退款的 Agent 只需要该订单、相关 policy，以及完成当前交易的有限 action authority。

因此生产 Agent 的有效权限更接近：

```text
effective delegated authority
⊆ delegator's delegable authority
∩ agent identity grants
∩ task scope
∩ resource/action policy
```

而不是：

```text
agent authority = principal authority
```

**判断**：委派场景须在授予及执行时核对有效权限与任务范围；已有足够窄、可撤销的权限不必人为反复签发。服务独立授权、人工升级与代理委派需显式区分，不能一律等于调用者权限。任务上下文本身应参与权限计算：本次需要哪些数据、哪几个工具、什么金额/次数边界、何时必须升级。

这也要求 control plane 同时保留执行证据。一个最终答案“看起来正确”不足以证明治理生效；按风险记录最少必要identity/context、检索及版本、动作/授权决定和实际结果；敏感数据、完整上下文或秘密不应因审计而无条件留存。否则发生异常时无法区分模型错误、检索错误、工具错误和 policy enforcement 缺口。

- **证据**：[[20260930-databricks-agentic-apps-ai-sprawl]]，`Control has to follow every action` 与 `Control also requires visibility into what happened`。
- **边界**：来源描述的是 Databricks 平台设计。centralized traces 证明可见性，不自动证明所有 action surface 都被强制拦截；**observability ≠ enforcement coverage**。

## 治理三层模型中的位置（07-17 深度思考）

Policy-as-Code 处于 Agent 委派治理**三层保证模型**的 L5（表达保证层——规则被写清楚）。但 07-17 深度思考揭示：**表达 ≠ 执行**。

关键发现：
- 规则表达和执行应分别验证。运行时、工具中介或目标资源本身均可承载强制执行；关键是完整中介、信任边界和防绕过能力，而非仅凭厂商身份断定失效。利益冲突是待治理风险，不是必然事实。
- **L0（机制保证）** 表示规则得到强制执行的机制层，而非所有Policy-as-Code实现必然缺失的层。L0在高风险场景需要独立于不可信模型的强制执行、可信审计与撤销；可由资源端、受保护中间件或隔离运行时实现。与整个runtime物理分离不是普适必要条件；日志宜防篡改/可验证，不承诺绝对不可篡改。
- **适应式治理的 L5 角色**：在预防→适应范式转换下，L5 的功能不再是"穷尽所有违规规则"（不可能，表达性上限）——而是"将从 L0+L4 检测→L+ 管理者识别的异常模式形式化为可自动执行的规则"。L5 是学习循环的终点和下一轮循环的起点。

历史商业产品线索（07-17联网）：Agat Software宣称工具执行前治理；本轮未重新核实产品或部署证据，不将宣称等同独立执行层已验证。Policy-as-Code 的规则是输入——独立执行层是执行这些规则的引擎。

与权限棘轮闭合（07-16）：L5 的策略 + L2（临时权限）+ L0（独立撤销）是缓解权限累积的候选组合，需验证撤销范围、派生凭据和未完成副作用。策略定义了"什么算越权"→ L2 限制了时间窗口→ L0 独立执行撤销。

详见：07-17 深度思考（roundtable 4人3轮+think 7层到底）

## 供应链 transaction policy：把业务授权包络写进执行层（2026-10）

[[20260921-ai-news-multi-agent-supply-chain-execution]] 把 policy-as-code 从抽象权限规则落到具体 transaction constraint：运输改道的成本/SLA 边界、库存变动的金额/数量阈值，以及供应商账户的 draft-only 信任级别，是报道建议部署前设置的约束，不能推断列名企业均已采用；可作为执行规则候选。

**判断**：面向真实企业交易的 Agent policy 至少应同时约束 **who/what can act、how far it may act、when it must stop、who must authorize the exception**。这类规则的价值在于把“谨慎一点”从 prompt 语言变成确定性的 action envelope。

- **证据**：[[20260921-ai-news-multi-agent-supply-chain-execution]]，供应链 guardrail 段落列出 cost ceiling、SLA delta、inventory threshold 与 draft-only supplier communication。
- **边界**：报道没有证明这些规则由独立 policy engine 实施，也没有给出 bypass、rollback 或 enforcement coverage 数据；因此这里吸收的是规则形状，不把其执行强度外推为已验证的 L0 机制保证。

这一案例也进一步说明 **Policy-as-Code 与 Escalation 是同一执行链的两侧**：policy 先判断动作是否处于包络内，越界后再由 [[Escalation-Based-Human-Oversight]] 决定接收者、上下文包和人工动作。只有二者闭合，multi-agent 的“自主执行”才不是把审批隐性地塞回 prompt。

## 运行时语义治理的增量（2026-09）

**判断**：Policy-as-Code 从静态表达进入工具执行点后，需区分“规则被写清楚”与“每个 action surface 都被拦截、记录、撤销”。

- **证据**：[[20260914-microsoft-ai-code-of-conduct]]、[[20260915-google-zero-trust-intent-governance]]。
- **边界**：Google的语义策略是厂商架构与示例；Microsoft的2026-09-14文档是未来MAI模型的咨询草案（不是法律权限层级或部署验证），不证明全部行动面被完整中介。

## 执行合同：从语义判断到不可越过的业务状态

**综合判断（2026-11-28）**：将硬约束与语义风险判断分离。确定性PEP/资源端以真实身份、任务授权、当前资源状态及事务内预算判断能否提交；语义策略用于难以编码的意图/分类候选判断，低可信结果可拒绝或升级。需避免检查与提交之间的竞态，按版本或事务原子核对累计金额/次数、幂等及撤销，并验证直接接口、替代工具、子Agent调用等路径不会绕过约束。失败关闭策略与例外权限按业务风险确定，不能只依赖模型自觉。

Google退款demo的异常识别在已发生超额退款之后，动态政策拦截后续调用并不撤销已写账；应由账务系统在提交时检查订单累计可退余额、去重与并发一致性，跨会话检测是补充，不是额度正确性的oracle。Databricks委派案例提供按任务缩小权限的设计动机，非完整执行证据。[OWASP完整中介指南](https://genai.owasp.org/llm2026/llm032026-excessive-agency/)允许工具、独立中介或下游系统实施授权，并非必须新增中央代理。上述事务、幂等和失效检查为本库工程综合，不是厂商已验证成效。
