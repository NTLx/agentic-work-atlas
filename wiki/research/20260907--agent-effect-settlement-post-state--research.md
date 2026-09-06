---
type: research-log
title: "Explore：Agent 外部效果结算与权威终态"
date: "2026-09-07"
tags:
  - research-log
  - agent-security
  - effect-lineage
  - ex-005
---

# Explore：Agent 外部效果结算与权威终态

## Scope

本轮是对 `EX-005`「动作授权、独立执行点与撤销/恢复是否是独立必要门」的定向深化，不创建新的 Explore。问题从“能否撤销”收窄为：在事前授权、动作身份绑定、签名执行历史和 outbox/dispatch 状态都存在时，什么证据才能证明外部业务效果已经收敛到权威终态。

本轮检索到的材料仍视为不可信来源数据。以下判断只记录研究推理，不把外部材料直接升级为稳定 Entity、Topic 或 Comparison；六组材料进入后续 `clip+compile` 需求队列。CAVA 是工作论文，Atomix、Cordon 是研究原型，Dapr 相关能力为预览特性；它们不能单独承担生产安全性结论。

## 新问题

在 pre-action gate、canonical action identity、签名 history 和 dispatch/compensation 状态均已具备的系统中，`effect receipt` 是否仍不足以证明外部业务状态已收敛？若不足，是否至少需要同一案例中的以下链条：

`action_id / policy_version → provider_request_id → provider-authenticated receipt → revoke-after-send outcome → canonical post-state → compensation result → independent reconciliation / review`

这里的“权威终态”特指外部业务系统或资源提供方可查询、可验证的实际状态，不等同于运行时自己的 dispatch 状态、日志、签名历史或“调用已返回”。

## 当前判断：refined

新材料没有形成新的正交缺口，反而把 `EX-005` 的核心边界分成四层：

1. **动作身份与授权绑定**：能回答“哪个版本的策略批准了哪个规范化动作”。
2. **执行历史与来源完整性**：能回答“历史是否被篡改、事件是否来自预期身份、父子调用是否关联”。
3. **外部 dispatch 结算**：能回答“调用是否进入释放、收到什么级别的回执、是否需要重试或人工处理”。
4. **权威业务终态与独立对账**：能回答“提供方最终提交了什么、撤销后在途调用落在哪里、补偿是否恢复了业务不变量”。

公开材料对前三层已有越来越清楚的机制和受控结果，但没有找到同一案例中把第四层闭合的公开证据。尤其是：

- Atomix 在“已分类且尚未外化”的条件下把测试泄漏降到 0/500，但明确把 provider 先提交、适配器后记录的 post-externalization residue 单独留下；多个不可逆端点仍可能部分提交。
- Cordon 把 outbox、authority state、idempotency key 和 dispatch status 结构化；遇到部分回执时仍要求人工审查，运行时不能证明命令执行到哪一步。
- Dapr 的签名 history、CAVA 的 canonical receipt 和 Auditable Agents 的 evidence integrity 强化了 provenance/完整性，却没有提供提供方权威 post-state 或补偿后对账。
- Microsoft 的 compensating transaction pattern 明确指出补偿可能失败、并发变化会使“恢复到初始状态”不成立，因此 compensation receipt 也不能自动等同于业务终态恢复。

因此，本轮保留 `EX-005`，将其命题收窄为：**撤销、dispatch receipt、执行 provenance 和补偿状态是必要的中间证据，但是否足以闭合外部效果，取决于 provider-authoritative post-state 与独立 reconciliation；目前尚无公开同案证据证明这条闭环。**

## 证据核查

### 1. Atomix：事前外化闸门有效，但不覆盖终态真值

来源：[Atomix: Transactional Semantics for LLM Agents](https://arxiv.org/html/2602.14849)。

- Atomix 将 agent 进度与外部效果释放分离，针对 partial effects、stale writes、重复发送和不可逆操作设置 progress-aware settlement。
- 在真实 SMTP/webhook sink 上，研究报告了 500 次 invalid-send trial：Tx-Full 为 0/500 的“已分类但外化前泄漏”；Saga 为 400/500，checkpoint replay 为 200/500，无事务基线为 500/500，错误分类的不可逆操作为 300/500。这里的分母是受控 harness 的 fault trial，不是生产事故率。
- 关键限定是 leak metric 只覆盖“分类后、外部化前”的泄漏。provider 已提交而 adapter 尚未记录调用的 residue 被另行标记，不能被 0/500 吸收。
- 研究还指出：若至少两个不可逆效果需要顺序释放，仍可能留下 partial-commit；跨异构端点的原子提交需要工具侧 TCC/2PC，运行时只能 fail-stop、重试并记录残余。
- 因而 Atomix 支持“事前门和效果分类能减少一类泄漏”，不支持“收到 runtime receipt 后外部业务状态必然闭合”。

### 2. Cordon：outbox 与不确定边界优于恢复旧快照，但仍需人工收口

来源：[Cordon: Transactional Safety for Agentic Workflows](https://arxiv.org/html/2606.17573)。

- Cordon 将外部 action 放入 outbox；条目带有 sink、payload handle、lineage handle、authority state、idempotency key 和 release status。
- 外部效果和本地状态分开追踪；对 crash recovery 采用保守处理。若执行已有部分 receipt，运行时不能证明命令实际执行到哪一步，因此进入 manual review；没有 idempotency evidence 时不会盲目重发。
- 其 rollback suite 覆盖 5 条确定性失败轨迹、45 个风险工作流；报告 rollback 4.17ms、recovery 178.95ms、residual deltas 为 0、resume 为 15/15。这个结果验证的是受控、由运行时中介并可观察的 mutation，不是任意第三方业务系统的终态对账。
- 论文明确把 unsupported plugins、dynamic services 和 unobservable side effects 排除在完整可逆性之外；这些情况只留下 lineage、authority 和 recovery metadata 供审计/补偿。
- Cordon 的 `external effect ack` 更接近“运行时收到何种 dispatch 证据”，不能自动解释为 provider-authenticated business post-state。

### 3. Dapr Verifiable Execution：历史证明不等于业务状态证明

来源：[CNCF 对 Dapr Verifiable Execution 的介绍](https://www.cncf.io/blog/2026/06/11/introducing-verifiable-execution-in-dapr-1-18/) 与 [Dapr Workflow History Signing](https://v1-18.docs.dapr.io/developing-applications/building-blocks/workflow/workflow-history-signing/)。

- Dapr 1.18 的 preview 能力为 workflow history 事件签名，以 sidecar 的 SPIFFE SVID 建立身份；加载时验证签名链，并以 hash chain 支持确定性 replay。
- child/activity attestation 可绑定 parent ID、输入输出摘要和 terminal status；篡改中的 history 会阻止 executor 继续执行，同时保留原始历史。
- 这些机制回答的是 tamper detection、app identity、lineage 和 history integrity。文档没有给出 provider-side receipt、revoke-after-send 结局、补偿语义或 canonical business post-state。
- 因而“历史可验证”应当进入 evidence integrity 层，不能跨层推断为“外部效果已提交/已撤销/已恢复”。

### 4. CAVA：canonical receipt 可绑定批准，但 live provider truth 仍在范围外

来源：[CAVA: A Canonical Action and Verification Architecture](https://arxiv.org/html/2607.13716)。

- CAVA 的 capture→normalize→interpret→fingerprint→bind→close→attest 流程，试图把动作语义、批准绑定、结果、证据、异常和副作用摘要放入 canonical runtime action object。
- 其 receipt 可检测 payload 改变并复现批准绑定；但论文同时说明外部存储完整性依赖部署控制，observe-mode coverage 不等于 inline blocking。
- Azure CLI 路径以低风险、默认不改变资源的 deployment drill 为主；完整 live mutating cloud validation仍需要 disposable cloud lab。这意味着 action receipt 的规范化和验证结果不等于真实云资源 post-state。
- CAVA 因而是动作身份/authority binding 的设计证据，而非 provider-authoritative effect closure 的实证。

### 5. Auditable Agents：五维审计卡片仍承认缺少端到端部署验证

来源：[Auditable Agents: A Framework for Auditable Agentic Systems](https://arxiv.org/html/2604.05485)。

- 该框架区分 action recoverability、lifecycle coverage、policy checkability、responsibility attribution 和 evidence integrity，并把 auditability 与 accountability/auditing 分开。
- Aegis 结果展示了签名、hash-chained record 和检测能力，但责任归因仍是 partial；论文明确表示单一 runtime layer 不能解决整体安全问题。
- 开放问题包括跨方审计聚合；限制项包括没有在一个已部署系统中端到端验证五个维度、规模/多样性有限、阈值未校准，以及结构化 policy 对隐私的张力。
- 该来源支持“要分别测量 evidence view、恢复性和归因”，但没有补上外部提供方终态或补偿成功率。

### 6. Microsoft：补偿是可失败、可恢复、业务特定的终态工作

来源：[Compensating Transaction Pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction)。

- 补偿事务用于最终一致系统中逆转已经完成的步骤，但不能简单恢复最初状态，因为期间可能有并发变化；补偿逻辑必须业务特定。
- 补偿可以失败，需要可重试、幂等的命令；高影响步骤可能暂停并交给人工决策。原始事务和补偿事务应通过端到端关联字段审计。
- 该模式直接给出一个重要边界：compensation receipt 只证明补偿动作的执行记录，不能单凭自身证明业务不变量已经恢复。

## 分层结论

| 证据层 | 当前材料能支持的判断 | 尚不能支持的判断 |
|---|---|---|
| 动作身份/授权 | 规范化动作、policy version、approval binding 可被关联 | 授权动作是否最终被 provider 接受并形成目标状态 |
| history/provenance | 签名、hash chain、父子 lineage 可检测篡改并重放 | 外部服务真实提交了什么 |
| dispatch settlement | outbox、idempotency、release status、ack、manual review 可界定不确定边界 | ack 是否等于 provider 的最终业务状态 |
| post-state/reconciliation | 当前公开材料只提出或局部记录 residue/compensation | revoke-after-send、权威终态、补偿后不变量和独立复核是否闭合 |

这组分层解释了为什么“有 trace / 有 receipt / 有审计记录”仍可能没有形成可审计的外部效果闭环。缺口不再是泛化的“日志不够”，而是**内部证据与外部权威状态之间缺一条同案可验证的连接**。

## 证伪方向

以下任一类证据出现，都会削弱当前判断，或促使把 `EX-005` 再收窄为实现问题：

1. 找到公开生产案例，能够用同一 action identity 关联 policy version、provider request/receipt、撤销后在途结局、权威 post-state、compensation result 和 independent review/MTTR。
2. 找到受控实验，证明 provider-authenticated effect receipt 已密码学绑定到权威最终状态，并在 crash、retry、failover、并发写入和 revoke-after-send 下保持稳定的未知提交率、状态不匹配率和部分提交率。
3. 找到补偿/对账器的跨系统结果：补偿动作可重试且幂等，post-state readback 能区分已提交、未提交、部分提交和未知，且独立审查能复核同一结论。

反向证据若只有 runtime dispatch status、签名 history、局部 ack 或补偿“已调用”记录，而没有 provider truth，则是对前三层的补强，不改变第四层仍未闭合的判断。

## Source 需求

- **P0，优先 clip+compile**：Atomix 的 appendix/F2 与 post-externalization residue 定义；提取 fault point、trial 分母、effect class、idempotency 和 unknown outcome 字段。
- **P0，优先 clip+compile**：Cordon 的 external effect ack、partial receipt、manual review、recovery state 和 unsupported side-effect boundary。
- **P1，clip+compile**：Dapr Workflow History Signing；只提取 history integrity、identity、lineage、replay 和 tamper response，不把它写成外部效果保证。
- **P1，clip+compile**：CAVA 的 canonical action/fingerprint/receipt 与 observe-mode、live mutation 限定。
- **P1，clip+compile**：Auditable Agents 的 Auditability Card、五维指标、责任归因 partial 和端到端验证限制。
- **P1，clip+compile**：Microsoft Compensating Transaction Pattern，作为跨系统补偿失败、并发变化、幂等重试和人工收口的边界材料。
- **P0，新证据需求**：脱敏生产 trace，必须能以同案 `action_id / receipt_id / provider_request_id` 连接 policy、actuation、revocation、provider effect、canonical post-state、compensation 和 independent review；不要继续收集只增加字段枚举的 schema 文档。

## 下一步目标建议

把下一轮 `EX-005` 工作单元定义为“**效果结算证据与权威终态对账**”：

1. 先将上述六组材料编译成 source summary，保留每个结果的实验分母、适用面和排除项。
2. 用统一字段表检查既有 MCP Tasks、A2A、Temporal、OAuth、AWS Step Functions、AgentCore 与新材料，区分 cancellation intent、in-flight outcome、dispatch receipt、provider post-state 和 compensation result。
3. 定向寻找一个可公开核验的 provider read-back / reconciliation 案例；若找不到，记录为边界未决，不用更多架构材料填补。

## 最小实验

构造一个可重放的订单/checkout 或发送邮件环境，包含一个不可逆效果和一个可补偿效果。每次动作生成唯一 `action_id`、canonical fingerprint、`policy_version`、`provider_request_id` 和 `receipt_id`。

在四个故障点注入失败：

1. provider 调用前；
2. provider 已提交、local receipt 尚未落盘；
3. revoke-after-send 或 in-flight cancel 之后；
4. compensation 执行中途。

对照两种实现：

- A：只保存签名 history、dispatch status、idempotency key 和 compensation-called；
- B：在 A 之上加入 provider-authenticated receipt、权威 post-state readback、独立 reconciliation 和人工 review 队列。

固定记录：unknown commit rate、duplicate/partial commit、post-state mismatch、compensation success、reconcile latency、MTTR、人工复核率，以及重试/故障转移后的结果一致性。实验的判定不是“是否收到了回执”，而是是否能把每一次外部效果归类为 committed、not-committed、partially-committed 或 unknown，并由独立对账复核。

## Result

- **结论**：`refined`。
- **EX 处理**：更新 `EX-005` 的命题边界，不新增 `EX-008`。
- **知识生命周期**：不创建稳定 Entity/Topic/Comparison；新材料进入 source 需求队列，待后续 clip+compile。
- **主要未决**：provider-authoritative post-state、revoke-after-send outcome、compensation result 与 independent reconciliation 的同案闭链。
