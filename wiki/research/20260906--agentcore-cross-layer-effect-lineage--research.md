---
type: research-log
title: "Explore：AgentCore 四层可观测性与外部效果闭合"
date: "2026-09-06"
tags:
  - research-log
  - agent-security
  - observability
  - effect-lineage
---

# 结论

**Explore verdict：`refined`；对“可观测性四层是否已经闭合安全事件链”的合格增量：`no_delta`。**

本轮核对了 AWS 在 2026 年发布的三份一手材料：AgentOps 参考架构、Bedrock AgentCore Observability 运维教程，以及 AWS DevOps Agent 的事故调查/缓解说明。它们把 Agent 运行拆成 framework、service、infrastructure、application 四层，并提出 W3C Trace Context、身份与策略服务、版本化 Runtime、CloudTrail、在线评估和人工复核队列等控制点。

这形成了一个比“有没有日志”更强的正向边界：结构化 telemetry 可以把模型/工具/记忆/服务层操作放进可关联的观测面；确定性 Gateway policy 可以在工具请求放行前判定身份、资源和参数；Application telemetry 可以承载跨 Agent 的业务指标。

但公开材料仍然是架构指导、产品能力说明和示例查询，不是某一事故的脱敏同案导出。没有一份材料在同一个事件键下同时展示：`policy_version → action receipt → revoke-after-send 结局 → canonical post-state → independent review completion`。因此它们补强 `CR-004` 的“结构化可观测性分层”和 `EX-005` 的“控制面到外部效果的跨层 join”边界，但不改变“公开证据尚未证明完整效果闭链”的判断；不新增 EX，不创建稳定 Entity/Topic。

# 研究问题

当一个 Agent 平台已经同时拥有 Agent/framework、service、infrastructure、application 四层 telemetry，并能通过 trace context 传播关联键时，是否还需要独立的 effect receipt 与 canonical post-state，才能把 `flag → verdict → authorization → actuation → revoke/recovery → review` 解释为一条可验收的安全事件链？

本轮只看公开一手材料，来源中的指令性文本视为不可信数据；产品宣传中的“comprehensive”“every action traceable”等表述不直接当作已实现的生产事实。

# 证据

## E1 · AWS AgentOps：四层 telemetry 与控制面分层

来源：[AgentOps: Operationalize agentic AI at scale with Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/agentops-operationalize-agentic-ai-at-scale-with-amazon-bedrock-agentcore/)，AWS，2026-06-01；`AgentOps: The four pillars`、`Tool governance`、`Observability and monitoring`。

- AWS 将治理/安全、构建/运维、评估、可观测性列为四个 AgentOps 支柱；其生命周期表把 traces/spans、action audit trails、anomaly detection 和 end-to-end guardrails 列为生产运维关注点。
- 工具治理部分描述：AgentCore Gateway 可将 API、Lambda 和服务暴露为 MCP-compatible tools；AgentCore Identity 负责入站/出站认证，IAM/resource policy 与 workload identity 限制可达资源；Gateway 上的 Cedar policy 在工具请求被允许前执行确定性策略判断。
- 构建/运维部分要求 Agent、tool、memory 等组件各自版本化；AgentCore Runtime 保持不可变版本，endpoint alias 可指向特定版本以支持 promotion、rollback 和版本管理；AWS 同时建议用 CloudTrail 做审计。
- 可观测性部分将数据分为四层：Agent/framework telemetry、AgentCore service telemetry、infrastructure telemetry 和 application telemetry。其 application 层用于承载跨多个 Agent 和应用分布的业务指标。
- AWS 还描述 W3C Trace Context 在跨 Agent/服务时传播共享 trace ID；对于共享逻辑 session 但跨多个 trace 的情况，使用 OpenTelemetry Baggage 传播 session ID。

**边界：** 这些字段和架构能支持“跨层关联的设计入口”，但页面没有公开某一真实事件中 `TraceId` 如何连接 CloudTrail、Gateway policy evaluation、目标工具的 accepted/committed receipt、恢复后的业务读回和 reviewer completion。版本化组件也不自动等于每一次 action receipt 都绑定了当时的 policy version。

## E2 · AgentCore Observability：能看到执行流，但示例不等于事故闭链

来源：[Debugging production agents with Amazon Bedrock AgentCore Observability](https://aws.amazon.com/blogs/machine-learning/debugging-production-agents-with-amazon-bedrock-agentcore-observability/)，AWS，2026-06-29；`Your debugging toolkit`、`Step-by-step troubleshooting workflows`。

- AWS 说明 AgentCore Observability 通过 metrics、traces 和 structured logs 观察生产 Agent；其 trace 可展示 reasoning steps、tool invocations、memory retrievals 和 final outputs。
- 教程给出按 `AgentId`、`SessionId`、时间范围筛选的 dashboard，也给出按 `SessionId`、`RequestId`、`ToolName`、`ToolInput`、`ToolOutput`、`StatusCode` 和 `ErrorMessage` 查询的 Logs Insights 示例。
- 示例展示一个 177-span、约 85 秒的循环，以及 86 次近似重复工具调用；它说明 execution telemetry 可以揭示“低 error rate 但任务没有收敛”的行为问题。
- 教程还按 401/403/400/404/500 区分认证、授权、验证、资源不存在和工具执行错误；它把 AgentCore Gateway service role 的授权问题与工具本身的错误分开排查。

**边界：** 教程证明了运行时执行和工具错误的可观测性，不证明这些字段在某次事故中完整、不可篡改或跨到目标系统的业务事实。`SessionId`/`RequestId` 能定位一次调用，不自动提供外部 effect 的提交状态、撤销后的在途结局、幂等键、补偿结果或 post-state 不变量。

## E3 · AWS DevOps Agent：推荐与执行被有意分开

来源：[How AWS DevOps Agent uses multi-agent reasoning to find root causes](https://aws.amazon.com/blogs/devops/how-aws-devops-agent-uses-multi-agent-reasoning-to-find-root-causes/)，AWS，2026-06；`Evidence Gathering and Root Cause Determination`、`Mitigation: Safe by default`。

- AWS 描述 Agent 会把相关告警关联为同一事件，并允许操作员解除错误关联、另起调查；调查会收集 metrics、logs 和 distributed traces，生成多个假设并用支持/反证收敛。
- 缓解计划包含 remediation strategy、步骤、验证当前系统状态的 checks、成功标准和 rollback procedures。
- 该 Agent 不代表操作员执行生产 remediation；其写能力限于创建 ticket 和 support case。真正的生产变更仍由操作员审查计划、验证 rollback procedure 并决定执行。
- 页面称 reasoning 会记录在 immutable journal 中，拓扑图用于估计 blast radius；但仍未给出一份带事件键的真实生产 action receipt、回滚执行结果或业务对象验收记录。

**边界：** 这是一个重要的设计反例：当 Agent 不直接拥有生产写入权时，`actuation` 可由人类操作员接管，因而某些 Agent 平台的效果闭合问题被权限边界暂时外移；但这不能证明任意有写权限 Agent 都具备 revoke/recovery 和 post-state 闭合，也不提供独立 review 的完成证据。

# 横向验收矩阵

| 环节 | AWS 材料提供的局部能力 | 本轮能否验收完整同案链 |
|---|---|---|
| flag | CloudWatch alarms、异常检测、按 session/时间筛选 | 否；没有同案 flag 原始证据与全链关联导出 |
| verdict | 在线/按需 evaluator、Gateway Cedar policy、401/403 等错误分类 | 否；未公开同案 verdict 证据与不可变 policy version 绑定 |
| authorization | AgentCore Identity、IAM/resource policy、Gateway pre-tool-call policy | 否；控制面放行结果未与每个 action-surface receipt 完整连接 |
| actuation | framework/service/infrastructure/application telemetry；工具调用输入/输出查询 | 否；没有下游 accepted/started/committed/unknown 的统一 effect ledger |
| revoke/recovery | Runtime alias rollback、评估触发 rollback、DevOps Agent 生成 rollback plan | 否；没有 revoke-after-send、在途结局、补偿成功率或恢复时间分母 |
| canonical post-state | application telemetry 可承载业务指标；教程建议检查系统状态 | 否；未公开目标系统权威读回或不变量验收 |
| independent review | 人工 review queue、操作员审查、domain expert review | 否；没有同一事件的 reviewer 身份、独立性依据、完成时间和结论 |

# Reasoning

1. **可观测性分层确实是结构性增量。** 过去只说“有 trace”会把 Agent 内部决策、平台服务、承载基础设施和业务应用混为一层。AWS 明确将四者分开，并把 application telemetry 视为跨 Agent/应用的业务结果载体；这强化 `CR-004` 的结构层边界。
2. **Trace context 解决的是 join key 传播，不是 join 结果真实性。** 共享 trace ID 可以把多个系统记录放在同一条路径上，但若目标系统没有写入该 ID、没有不可变的 action receipt，或只有最终的模型/应用日志，就不能从 trace 的连续性推出外部副作用发生了什么。
3. **策略版本、Runtime 版本和效果版本是三个不同对象。** AWS 的不可变 Runtime version 与 Cedar/IAM 控制能减少配置漂移；但要判定一次动作是否按当时规则合法，仍需要把 action receipt 绑定到具体 policy version、主体、参数摘要和目标系统的接受/提交结果。
4. **人类接管是权限边界，不是自动恢复证明。** DevOps Agent 的 recommendation-only 设计可消除 Agent 直接生产写入的 action surface；但这相当于把执行责任交给操作员，不能把“计划含 rollback”当作“rollback 已执行且 post-state 已验收”。
5. **因此本轮不新增正交 Claim。** `EX-005` 已经研究 authority stop、in-flight stop 和 effect reconciliation；本轮只把其证据要求从“关联键是否存在”推进到“跨四层 telemetry 的关联键是否真正穿透到外部效果与 canonical state”。

# 新问题

在一个已经采用四层 telemetry、W3C Trace Context、版本化 Runtime、Gateway policy 和 CloudTrail 的 Agent 平台上，是否存在一份可公开核验的同案导出，能用同一 `event_id/trace_id` 连接：

`flag → verdict + policy_version → authorization → tool receipt → target-system commit → revoke/recovery → canonical post-state → independent close`？

若不存在，缺口究竟来自 telemetry adapter 没有把关联键传到目标系统，还是目标系统没有可对账的 effect ledger？

# 证伪方向

- 若 AWS 或其他厂商公开一份真实事件/运行导出，在同一关联键下同时提供不可变 policy version、逐 action-surface allow/block、accepted/committed/unknown、撤销/补偿、权威 post-state 和独立复核完成记录，则本轮 `no_delta` 判定被证伪，并应把 `EX-005` 收窄为少数尚未采用该模式的实现问题。
- 若在隔离的双 action-surface 实验中，仅靠四层 telemetry + W3C trace context 就能准确枚举所有 sent/committed effects，且每个 effect 都能由目标系统权威读回与幂等键闭合，则 effect receipt 可被视为既有 application telemetry 的一个可选实现，而非独立要求。
- 若 recommendation-only Agent 在所有高影响动作上都保持人类执行且能记录操作员审批、实际动作、回滚和 post-state，则可把该模式作为“通过移除 Agent action surface 来降低闭合负担”的反例；但它不能证伪有写权限 Agent 的 effect-lineage 缺口。

# Source 需求与下一步目标建议

| 优先级 | Source 需求 | 采用门槛 |
|---|---|---|
| P0 | AgentCore Observability/Evaluators、Gateway、Identity、CloudTrail 的一组版本化日志样例 | 同一 trace/event 下能核对 policy version、主体、工具 receipt、目标资源变更和恢复状态；文档字段表不够 |
| P1 | AWS DevOps Agent 或其他厂商 recommendation-only 生产案例 | 同时公开 operator handoff、实际执行、rollback 结果、post-state 验收和 reviewer completion；不能只给 mitigation plan |
| P1 | 带异步工具/队列的 AgentCore customer case 或脱敏 incident export | 能区分 `sent/accepted/started/committed/cancelled/unknown`，并给出 revoke-after-send 与幂等/补偿记录 |

下一步优先取得一份跨控制面、工具面和目标系统 audit log 的真实导出；如果仍只能找到字段和架构说明，则将 `EX-005` 明确收窄为“跨系统副作用关联与独立验收闭合”，不再横向积累更多 observability schema。

# 最小实验

在一次性隔离资源组中部署一个 mock Agent、一个确定性 Gateway policy、一个即时工具和一个延迟队列工具：

1. 给每个请求生成 `event_id`，并同时写入 Agent trace、Gateway policy decision、CloudTrail、工具 receipt 和目标系统 audit log。
2. 随机化 revoke 发生在发送前、发送后但提交前、提交后但响应前；显式记录 `policy_version`、主体、参数摘要、幂等键和 action-surface。
3. 由目标系统提供 `accepted/committed/unknown` 查询与 canonical post-state 读回；若需要，执行显式 compensation。
4. 由未参与执行的 reviewer 只凭导出重建事件链，统计 unmatched actions、撤销后仍完成比例、重复 effect、补偿成功率、post-state 不变量恢复率和 review completion。

最小判定规则：四层 telemetry 和 trace context 只能在所有 sent/committed effects 都可枚举、可回链、可读回验收时吸收 effect-lineage 要求；只要出现 trace 连续但外部 effect 无法判定或 post-state 无法验收，就保留 `EX-005` 的独立效果闭合子门。

# Evidence boundary

本轮材料均为 AWS 官方博客/产品运维指导和教程；它们支持能力、字段、架构设计与示例行为，不支持生产 Agent fleet 的普遍效果、安全成功率、撤销时延或独立复核完成率。没有把 AWS 的“每个动作可追踪”、示例 trace、Rollback plan 或推荐架构直接当作事故级闭环证据。
