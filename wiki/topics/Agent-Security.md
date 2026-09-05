---
type: topic
title: Agent Security
description: "Agent 在不可信组件和跨信任域环境中行动时，从检测、判定、授权、执行到撤销与恢复的责任闭环"
created: 2026-09-05
updated: 2026-09-05
evidence_level: medium
claim_type: synthesized
tags:
  - AI-Agent
  - agent-security
  - governance
  - verification
related_entities:
  - "[[Agent-Observability]]"
  - "[[Agent-Containment]]"
  - "[[Least-Agency]]"
  - "[[Distinct-Principal-Identity]]"
  - "[[Policy-as-Code-for-Agent-Governance]]"
  - "[[Long-Lived-Credential-Risk]]"
  - "[[Alert-Closed-Loop]]"
  - "[[On-Call-Agent]]"
  - "[[Operational-Responsibility]]"
  - "[[Human-Governor-Agent-Operator]]"
source_raw:
  - "[[How we contain Claude across products]]"
  - "[[20260518-zero-trust-for-ai-agents]]"
  - "[[20260713-agentic-misalignment-summer-2026]]"
  - "[[20260727-hf-agent-intrusion-technical-timeline]]"
  - "[[20260801-tailscale-hugging-face-ai-agent-intrusion]]"
  - "[[20260819-anthropic-claude-tag-oncall]]"
---

# Agent Security（Agent 安全）

> [!summary] 当前边界
> Agent 安全研究的主问题不是“模型是否输出了正确答案”，而是：在 Agent 能调用工具、跨越信任域并产生外部后果时，谁能看见状态、谁能判定风险、谁能授权动作、哪一层能确定性执行，以及出事后谁能撤销、恢复并承担责任。
>
> 本页目前是一个**结构地图**，不是“完整安全已经得到证明”的定理。现有材料支持五阶段的对象与接口边界，但尚未闭合所有行动面、真实责任人、撤销时限和恢复效果。

## 五阶段安全闭环

| 阶段 | 它要回答的问题 | 当前稳定承载 | 可观察失败信号 | 候选责任角色 | 当前缺口 |
|---|---|---|---|---|---|
| **检测** | Agent 做了什么、经过了哪些路径、哪些状态已被看见？ | [[Agent-Observability|Agent 可观测性]]、[[Agent-Containment|Agent 隔离]] | 关键事件未记录、路径不完整、告警延迟、异常未被关联 | observability owner、SOC 或 incident detection owner | action-surface coverage、日志完整性、跨信任域可见性；意图不能直接当作观测事实 |
| **判定** | 这是什么风险，是否违反政策，是否应拒绝或升级？ | [[Policy-as-Code-for-Agent-Governance|治理策略即代码]]、[[Agent-Observability|Agent 可观测性]] | 错误严重度、误放行、误阻断、错误升级、评测/裁判共模漏报 | policy owner、风险裁决人、incident analyst | policy 与 evidence 的有效性、独立判定、reference/source lineage；“看见”不等于“判对” |
| **授权** | 谁以何种权限、在什么资源和时间范围内允许该动作？ | [[Distinct-Principal-Identity|独立主体身份]]、[[Least-Agency|最小代理权]]、[[Policy-as-Code-for-Agent-Governance|治理策略即代码]] | 凭证继承、权限过宽、过期权限仍有效、责任无法归因 | identity/IAM owner、policy author、委派的 human Governor | 授权人与撤销人是否分离、token TTL、范围与预算是否绑定到具体动作 |
| **执行** | 动作是否经过不可被模型自我改写的确定性边界？ | [[Agent-Containment|Agent 隔离]]、[[Long-Lived-Credential-Risk|长生命周期凭据风险]] | 未授权副作用、越过工具/网络/并发面、沙箱逃逸、凭据批量暴露 | runtime/platform security owner、tool owner | 完整 action-surface manifest、provenance substrate、out-of-band 绕过、允许范围内副作用 |
| **撤销 / 恢复** | 出事后能否立即停止、收回权限、回滚后果、交接责任并复盘？ | [[Alert-Closed-Loop|告警闭环]]、[[On-Call-Agent|On-Call Agent]]、[[Operational-Responsibility|运营责任制]] | 无人接收、转接失败、撤销过晚、不可逆损失、无法重建责任链 | revoke authority、resource owner、incident commander、reviewer | 撤销耗时、rollback success、MTTR、恢复 SLA、责任交接和信息型后果的止血边界 |

这五段不是五个独立产品，也不是每个 Agent 都必须配置相同强度的五层控制。它们是分析一条安全责任链的五个接口：前一段提供后一段的输入，后一段不能反过来证明前一段已经正确。

## 与可验证 Agent 工程的边界

[[Verifiable-Agent-Engineering|可验证 Agent 工程]]主要问：输出、路径、上下文和行为是否能够被验证、拒绝、重试或复现。Agent Security 在此基础上继续追问：**不可信组件已经行动时，权限和后果如何被约束，控制权如何被撤回，谁对结果负责。**

两者共享可观测性、确定性骨架和拒绝机制，但不是同一个判断：

- 结果正确，不代表动作被授权，也不代表责任可追溯。
- 告警被记录，不代表正确的人收到，也不代表其有权阻断或恢复。
- 策略被写成代码，不代表策略状态完整抵达执行边界。
- 动作被拒绝，不代表所有 action surface 都已被中介，也不代表已经可恢复。

因此，现有研究候选的接口可以暂时这样放置：

| 研究线 | 在五阶段中的位置 | 不应偷换成什么 |
|---|---|---|
| `CR-004` Agent observability | 检测，以及判定的证据输入 | 不能由日志存在推出完整覆盖或正确理解 |
| `EX-004` reference integrity / success provenance | 判定的真值、来源和成功归因条件 | 不能由 reference 可用推出动作安全 |
| `EX-005` authorization / actuation | 授权到执行的确定性边界 | 不能由 Allow/Deny 结果推出撤销和恢复已解决 |
| `EX-006` policy carriage / control-plane integrity | 策略从 owner 到决策和执行边界的承载 | 不能由上下文中出现 policy 文本推出其稳定绑定和失败关闭 |
| `EX-003` facilitator / handoff | 判定后的升级、接收面和人类处置 | 不能由“已升级”推出人类确实接住并完成闭环 |

## 现有证据能支持什么

### 1. 检测不是单纯的日志数量

[[Agent-Observability|Agent 可观测性]]已经把 Agent trace、数据流、工具调用、终止条件和跨信任域审计放在同一问题中；Hugging Face 入侵时间线则显示，防御方即使能把大量动作聚类成攻击链，也可能错误判断告警级别而没有及时触发 on-call。这里的稳定边界是：**记录、关联和触发是不同能力**。

### 2. 判定依赖独立的证据与政策

[[Policy-as-Code-for-Agent-Governance|治理策略即代码]]把权限、披露、升级和合规规则放到模型外；Agent misalignment 材料同时说明，同质裁判或共享激励会让监督链误标。这里的稳定边界是：**政策可执行性与判定正确性相互依赖，但不能互相充当证据**。

### 3. 授权与执行必须分开看

[[Distinct-Principal-Identity|独立主体身份]]解决归因、权限上限和凭证生命周期，[[Least-Agency|最小代理权]]进一步限制工具能力、操作次数和作用域；[[Agent-Containment|Agent 隔离]]把最坏情况限制在环境边界内。它们共同支持一个结构判断：**模型提出动作，不等于系统必须放行动作**。

### 4. 恢复是闭环的一部分，不是事后附录

[[Alert-Closed-Loop|告警闭环]]要求通知、接收、评估、干预和复盘形成责任链；[[On-Call-Agent|On-Call Agent]]显示 Agent 可以承担检测、分诊和 SITREP，但人仍需接手高影响修复；[[Long-Lived-Credential-Risk|长生命周期凭据风险]]进一步区分了可撤销、可止血和不可恢复的后果。这里的稳定边界是：**撤销一个凭证不等于撤销已经被第三方系统接纳的后果**。

## 不能从现有材料推出什么

- 五阶段在所有 Agent 部署中具有相同的必要性或最佳控制强度。
- 某个厂商的架构描述等同于部署级安全效果。
- 事前授权已经覆盖所有工具、网络、消息、stdio、并发和合法权限内的副作用。
- 有独立身份就必然有可执行的撤销权；身份、权限、执行点和撤销通道仍可能属于不同 owner。
- 告警、SITREP 或结构化摘要被生成，就等于人类收到了足够上下文并完成了正确处置。

## 当前证据缺口

下一步优先补四类可回溯材料：

1. **动作面清单**：同一 Agent 的工具、HTTP、消息、文件、进程、并发和外部 side effect 是否都经过可验证中介。
2. **责任与控制权**：policy author、identity owner、executor、revoke authority、incident commander 和 reviewer 是否由不同角色承担，冲突如何处理。
3. **恢复实测**：token TTL、time-to-block、revoke latency、rollback success、MTTR 和不可逆后果的止血方式。
4. **完整事件时间线**：`flag → owner → allow/deny → actuation → revoke → rollback/recovery → review` 是否能在同一生产任务中逐事件重建。

这些缺口对应 `EX-003`、`EX-004`、`EX-005`、`EX-006` 的相邻研究线；本页只提供导航，不把候选问题改写成已验证结论。

## 最小验证实验

在同一可回放 incident 上固定任务、模型、原始 trace、policy、verdict、工具 schema 和负载，依次检查：

1. 用五阶段字段表重建一条 `detection → verdict → authorization → actuation → revocation/recovery` 事件链。
2. 对每个阶段记录唯一 owner、权限边界、可观察失败信号和证据定位；缺失项保持为 `gap`。
3. 注入未授权参数、过期 token、多个单独合法但合计越界的调用、out-of-band 通道和授权范围内的错误副作用。
4. 比较 `action-surface coverage`、误放行、误阻断、阻断延迟、撤销成功率、回滚成功率、MTTR 和责任谱系重建率。

如果某阶段只有架构描述而没有可观察事件或责任主体，就只能把它保留为设计接口，不能把它当作闭环已经成立的证据。

## 研究状态

这是一个由现有安全 Entity 和 Source summary 支持的最小 Topic 骨架。结构边界暂定为“安全责任闭环”，而不是把 [[Verifiable-Agent-Engineering|可验证 Agent 工程]]的安全章节复制一遍。`owner`、`action-surface`、`revoke` 和 `recovery` 仍标记为未闭合，后续需用一手材料逐格核验。
