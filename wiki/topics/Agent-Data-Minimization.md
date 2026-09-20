---
type: topic
title: Agent Data Minimization
description: "Agent 数据最小化：把授权范围、实际读取范围、模型/上下文暴露与保留删除生命周期分开治理，避免用 least privilege 或 zero unauthorized writes 替代真实的数据最小化证据"
created: 2026-09-19
updated: 2026-09-19
evidence_level: high
claim_type: mixed
tags:
  - topic
  - privacy
  - agent-security
  - governance
related_entities:
  - "[[MosaicLeaks]]"
  - "[[PA-DR]]"
  - "[[Least-Agency]]"
  - "[[Agent-Security]]"
  - "[[Zero-PHI-Policy]]"
source_raw:
  - "[[20260618-mosaicleaks-privacy-agent]]"
  - "[[20260905-numezis-governed-business-agent-sme]]"
  - "[[20260614-decentralized-granular-access-control-agentic-ai]]"
  - "[[20260710-aws-ktern-agentcore-sap]]"
---

# Agent Data Minimization（Agent 数据最小化）

> [!summary] Topic 定位
> Agent 的隐私治理不能只问“有没有权限”或“有没有未经授权写入”。真正的数据最小化需要分别测量：**允许访问什么、任务实际读取什么、哪些数据进入模型/上下文、这些数据被保留多久以及如何删除。**

## 为什么这是一个独立问题

传统 least privilege 主要回答：

> 主体被允许访问哪些资源、执行哪些动作？

Agent 系统额外引入了检索、上下文拼装、长期 memory、tool trace 和模型调用，因此同一个“只读 Agent”也可能：

- 读取远超任务必要范围的数据；
- 把不必要字段放入 prompt / model context；
- 把项目历史长期保存在 memory；
- 把敏感内容写入日志、缓存或 trace；
- 在 provider、RAG store、本地 memory 和业务系统中形成不同保留周期。

因此：

~~~text
permission scope
      ≠
actual read scope
      ≠
context/model exposure
      ≠
retention / deletion
~~~

这四个轴不能互相替代。

## 1. Permission scope：允许做什么

[[20260614-decentralized-granular-access-control-agentic-ai]] 提供了一个生产级反例：20+ specialized agents、60+ deterministic playbooks、每日数千次操作，在 8 个月生产运行中自报零 unauthorized writes。

它说明：

- compound identity 可以把 agent authority 绑定到 delegated human authority；
- 权限可以细化到五级层次；
- 高风险写操作可以被隔离到 deterministic playbook / approval 路径；
- Agent 形态本身并不要求无限制写权限。

但这个案例并没有测量：

- 每个任务实际读取多少数据；
- 是否读取了任务不需要的字段；
- context 保留多少；
- 数据何时删除。

因此 **zero unauthorized writes 是 action-safety 指标，不是 data-minimization 指标。**

## 2. Read scope：实际读取了什么

[[20260905-numezis-governed-business-agent-sme]] 把控制推进到读取面：

- document retrieval 按法人隔离；
- 再按具体 client file 隔离；
- MCP connector 按 tool 单独授权；
- 每次 read、proposal、decision 都进入 audit log。

这证明任务 Agent 可以避免“默认全库可见”。

但该案例仍没有提供：

- 单任务读取记录数 / 文件数；
- 实际读取量相对最小必要量的比值；
- 被拒绝读取请求比例；
- 因检索扩大而额外暴露的字段量。

所以“按 client file 隔离”是**读取边界设计**，还不是“读取量已经最小”的直接测量。

## 3. Context / model exposure：读到的数据是否都应进入模型

[[MosaicLeaks]] 提醒了另一个独立层面：即使数据是合法读取的，Agent 为完成任务而构造外部 query 或模型上下文时，仍可能泄漏不必要的私密信息。

MosaicLeaks 的受控结果显示：

- 基线 Answer/Full-Information 泄漏率 34.0%；
- 只强化任务成功后升至 51.7%；
- [[PA-DR]] 把泄漏降到 9.9%，同时任务成功率保持接近 task-only 训练。

因此：

~~~text
authorized read
≠
authorized disclosure
~~~

数据进入本地 Agent，并不意味着它应该进入外部搜索 query、模型 prompt、第三方 tool 参数或下游协作者上下文。

## 4. Retention / deletion：最小权限并不决定记忆寿命

[[20260710-aws-ktern-agentcore-sap]] 是最清楚的反例。

同一个生产架构同时具备：

- per-agent least privilege；
- customer session isolation；
- private VPC / PrivateLink path；
- tool/model observability；

但又明确使用 persistent AgentCore Memory，把 process decisions、code patterns 与 accumulated insights 跨 session 保留。SAP transformation 项目持续 12–18 个月，这种长期记忆是设计目标。

这并不自动构成“过度收集”——长期项目可能确实需要长期状态。

它证明的是：

> **least privilege 与 minimum retention 是正交问题。**

权限可以很窄，而保留可以很长；保留可以很短，而单次读取仍可能过宽。

因此 retention 需要自己的治理字段：

- retention owner；
- retention purpose；
- TTL / expiry；
- project-close deletion；
- selective forgetting / correction；
- legal hold / audit exceptions；
- downstream cache / trace / provider retention。

## 5. Provider no-retention 也不是全栈无保留

Numezis 披露模型调用使用 no retention，并且不以客户数据训练。

这是有价值的 provider-side control，但不能被外推成：

~~~text
model provider no-retention
        ⇒
agent system no-retention
~~~

因为数据仍可能存在于：

- retrieval store；
- local cache；
- Agent memory；
- tool execution log；
- audit trace；
- business source system；
- backup / observability pipeline。

因此每个 retention claim 都必须带上 **retention surface**。

## CR-002 的稳定收窄

原命题“Agent 的数据过度收集来自任务代理架构，而不是单一产品或单一厂商实现失误”过强。

当前更符合证据的版本是：

> **Agentic workflow 对广权限、广检索、上下文累积和长期记忆存在结构性压力；但这些风险不是 Agent 架构不可避免的属性。通过外部身份授权、按资源/客户隔离、tool-level permissions、provider no-retention、human approval 和审计，可以显著收窄边界。真正仍缺的是对 actual read volume 与 retention/deletion 生命周期的长期量化。**

生产反例已经足以否定：

~~~text
agentic architecture
      ⇒ necessarily
over-broad permission / unlimited retention
~~~

但还不足以证明：

~~~text
least privilege
      ⇒
long-term data minimization
~~~

## 最小可审计字段

更可靠的生产审计应至少记录：

~~~text
task / purpose
  → authorized resources
  → actual resources read
  → fields / chunks exposed to model
  → external disclosures / tool arguments
  → memory / cache / log writes
  → retention owner + TTL
  → correction / deletion event
~~~

其中任意一段缺失，都可能让“最小权限”形成隐私上的虚假安全感。

## 与相邻概念的边界

- [[Least-Agency]]：控制 Agent 能做哪些动作；不直接证明数据读取/保留最小。
- [[MosaicLeaks]]：测量任务过程中向外泄露的信息；不覆盖企业生产系统的完整 retention lifecycle。
- [[PA-DR]]：训练层缓解信息泄露；不替代身份、检索隔离和删除策略。
- [[Agent-Security]]：覆盖 authorization / actuation / recovery；数据最小化专注 information lifecycle。
- [[Zero-PHI-Policy]]：是高度敏感数据“完全不进入模型”的强约束特例。

## 当前开放缺口

CR-002 后续只需要真正能改变边界的生产证据：

1. 任务级 actual read denominator；
2. read scope 与最小必要数据的比较；
3. context / model exposure 量化；
4. retention TTL 与项目结束删除；
5. correction / erasure 是否传播到 memory、cache、trace；
6. 至少数月的 drift / permission-creep / retention-creep 纵向结果。

没有这些字段时，不再把“零未授权写入”“least privilege”或“有审计日志”当作长期数据最小化反例。
