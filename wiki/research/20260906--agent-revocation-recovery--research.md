---
type: research-log
title: "研究日志 2026-09-06：Agent 授权撤销后的恢复边界"
date: "2026-09-06"
tags:
  - research-log
  - agent-security
  - revocation
  - ex-005
---

# 结论摘要

本轮新增的一手材料支持把撤销后的结果至少拆成三个不同语义：

1. **authority stop**：授权服务、任务服务或策略门不再放行新的调用；
2. **in-flight stop**：已经发出、已排队、已建立连接或已被 Worker 接收的动作是否真的停止；
3. **effect reconciliation**：外部副作用已经提交后，是否通过幂等识别、补偿、回滚和 post-state verification 收敛。

官方材料并没有用同一套术语统一这三层，但其行为契约反复把它们分开：MCP Tasks 的稳定版规范甚至允许任务已经是 `cancelled` 而底层执行仍继续；MCP Tasks Extension 草案把取消定义成最终不保证生效的合作式意图；A2A 只保证尝试取消并返回任务状态；Temporal 将工作流取消、Activity 取消、强制终止和应用自行执行的 Saga compensation 分开；OAuth 把令牌失效与传播/缓存窗口分开；AWS Step Functions 把 `StopExecution` 的成功响应与最终状态查询的 eventual consistency 分开。

本轮新增材料没有提供部署级的撤销传播延迟、在途完成率、补偿成功率或 rollback MTTR。它们提供的是规范声明、状态字段、时间字段、超时配置和示例代码，不是实测数据。2026-09-05 日志中的 HBHC、ACRFence 和 GitHub 事故报告仍是本研究中已有的实测/生产时间锚点，本轮不重复计入新材料。

# 去重范围与材料清单

访问日期：2026-09-06。以下按五个“材料族”计数，满足本轮 3–5 个新增材料的范围；同一材料族内的多个官方页面是为了核对同一系统的不同语义面。

| 材料族 | 官方材料 | 相对 2026-09-05 日志 | 材料类型与边界 |
|---|---|---|---|
| MCP Tasks | [MCP 2025-11-25 Tasks](https://modelcontextprotocol.io/specification/2025-11-25/basic/utilities/tasks)、[MCP 2025-11-25 Cancellation](https://modelcontextprotocol.io/specification/2025-11-25/basic/utilities/cancellation)、[Tasks Extension 草案](https://tasks.extensions.modelcontextprotocol.io/specification/draft/tasks) | **新增语义材料**。日志已有 MCP 2026-07-28 传输层、公告和安全实践，但没有 Tasks/cancel 语义 | 核心规范与 2026-07-28 草案；草案不能当作已发布核心规范或部署效果 |
| A2A | [A2A Protocol Specification，latest released version 1.0.0](https://a2a-protocol.org/latest/specification/) | **新增**。日志中 OTel PR #447 只引用 A2A 拓扑参考，不是 A2A 取消规范 | 官方协议规范；定义任务状态、CancelTask、幂等和时间字段，不定义业务回滚 |
| Temporal | [Java Workflow cancellation](https://docs.temporal.io/develop/java/workflows/cancellation)、[Activity Execution](https://github.com/temporalio/documentation/blob/main/docs/encyclopedia/activities/activity-execution.mdx)、[事件参考](https://github.com/temporalio/documentation/blob/main/docs/references/events.mdx)、[官方 HelloSaga 示例](https://github.com/temporalio/samples-java/blob/main/core/src/main/java/io/temporal/samples/hello/HelloSaga.java) | **新增** | 官方产品文档、官方文档仓库和官方 SDK 示例；示例展示机制，不是运行遥测 |
| OAuth | [RFC 7009 Token Revocation](https://datatracker.ietf.org/doc/html/rfc7009)、[RFC 7662 Token Introspection](https://datatracker.ietf.org/doc/html/rfc7662) | **新增** | IETF Standards Track 规范；定义令牌失效、active 查询和缓存边界，不定义在途请求或业务副作用 |
| AWS Step Functions | [StopExecution API](https://docs.aws.amazon.com/step-functions/latest/apireference/API_StopExecution.html)、[DescribeExecution API](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DescribeExecution.html) | **新增**。日志已有 AWS Agentic AI Lens、Security Incident Response 和 DevOps Agent 文档，但没有 Step Functions API | 官方 API 契约；给出 stopDate/status 和 eventual-consistency 声明，不给出下游 effect 或 rollback 数据 |

明确的已有重复/背景材料：2026-09-05 日志已核对 [ACRFence](https://arxiv.org/html/2603.20625)、[HBHC](https://arxiv.org/html/2605.20704)、[AWS Agentic AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec07-bp04.html)、[AWS Security Incident Response Contain](https://docs.aws.amazon.com/security-ir/latest/userguide/contain.html)、[AWS DevOps Agent token revocation](https://docs.aws.amazon.com/devopsagent/latest/userguide/accessing-devops-agent-connect-to-devops-agent-remote-servers.html)、[Google IAM access propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation?hl=en)、[Microsoft Entra emergency revocation](https://learn.microsoft.com/en-us/entra/identity/users/users-revoke-access) 和 [GitHub May 2026 availability report](https://github.blog/news-insights/company-news/github-availability-report-may-2026/)。这些材料继续作为本轮的对照，而不被再次算作新增。

# 逐条证据

## 1. MCP：任务状态可以与真实停止脱钩

**E1 — [核心 Tasks 规范](https://modelcontextprotocol.io/specification/2025-11-25/basic/utilities/tasks)（规范声明，强度：高；局限：仅适用于该版本和已声明 Tasks capability 的实现）。**

- 任务对象强制包含 `createdAt`、`lastUpdatedAt`，并带有 `ttl`、可选 `pollInterval` 和 `working / input_required / completed / failed / cancelled` 状态。
- 有效的 `tasks/cancel` 请求要求接收方尝试停止执行，并在发送响应前把任务转成 `cancelled`；但规范又明确：任务一旦是 `cancelled`，即使底层执行后来继续到完成或失败，任务仍保持 `cancelled`。
- 状态通知是可选的，客户端不能依赖收到通知；客户端应通过 `tasks/get` 轮询，`tasks/result` 在非终态时阻塞到终态。

因此，MCP 核心规范把“任务控制平面的状态确认”与“底层工作是否真的停止”明确拆开。`cancelled` 不是外部副作用已经逆转的证明，也不是所有 action surface 都已经被 authority stop 覆盖的证明。

**E2 — [MCP 基础请求取消](https://modelcontextprotocol.io/specification/2025-11-25/basic/utilities/cancellation)（规范声明，强度：中高；局限：是请求级取消而非凭据撤销）。**

`notifications/cancelled` 只适用于发送方认为仍在进行中的请求；接收方应停止处理、释放资源且不再回复，但可以因为请求未知、已经完成或不可取消而忽略。规范还承认取消通知可能因网络延迟在响应已经发送后才到达。对任务增强请求必须使用 `tasks/cancel`，不能把请求通知当成任务终态确认。

**E3 — [MCP Tasks Extension 草案](https://tasks.extensions.modelcontextprotocol.io/specification/draft/tasks)（草案规范，强度：中；局限：截至访问日仍标记 Draft，不能与已发布核心规范混作同一实现契约）。**

草案把语义写得更弱、更接近分布式取消：服务器成功返回空确认即可；确认之后，任务的可观察状态仍可能是 `working` 或其他非终态，也可能因为工作先完成而最终到达 `completed`/`failed` 而非 `cancelled`。取消是合作式意图，服务器不被要求真的停止工作，最终转成 `cancelled` 也不保证。

这与核心 2025-11-25 页面形成**版本/层级差异**：核心页面要求在响应前转成 `cancelled`，草案则明确允许 ack 先于可观察状态更新。两者都没有 effect ledger、幂等键、补偿或业务 post-state 语义。

## 2. A2A：返回取消状态不等于外部效果已收敛

**E4 — [CancelTask 和任务状态](https://a2a-protocol.org/latest/specification/)（规范声明，强度：高；局限：协议规范，不是跨实现测量）。**

A2A 1.0 的 `CancelTask` 只表述为“请求取消 ongoing task”；服务器会尝试取消，但成功不保证，例如任务已经完成/失败，或当前阶段不支持取消。操作返回更新后的 `Task`；不可取消和不存在分别有明确错误。规范另行规定 Cancel Task 是幂等的，多次取消应有相同效果，但任务已经取消且被清除时，重复请求可以返回 `TaskNotFoundError`。

**E5 — [状态、时间和交付物](https://a2a-protocol.org/latest/specification/)（规范声明，强度：高；局限：字段是协议可见性，不是业务事实）。**

A2A `TaskStatus` 定义了当前 `state`、可选的 status message 和 ISO 8601 `timestamp`；`Task` 还可携带 artifacts。订阅流在任务进入终态时必须结束，并且订阅开始时先返回当时的 Task 快照。由此可以确认“协议任务状态在何时被记录、客户端何时看到任务级终态”，但不能确认工具调用是否在途、下游服务是否已经提交、artifact 是否代表外部业务对象的正确 post-state，或是否需要补偿。

## 3. Temporal：取消、终止和补偿是不同机制

**E6 — [Workflow cancel vs. terminate](https://docs.temporal.io/develop/java/workflows/cancellation)（官方产品文档，强度：高；局限：文档契约，不是运行分布）。**

Temporal Java 文档把取消描述为 graceful stop：事件历史记录 `WorkflowExecutionCancelRequested`，随后调度 Workflow Task，由 Workflow 代码处理取消并执行 cleanup；系统不会强制停止 Workflow。`terminate` 则记录 `WorkflowExecutionTerminated`，强制、立即停止 Workflow，代码没有处理终止的机会，也不会再调度 Workflow Task。

这已经把“停止编排层”与“让应用完成清理”分开。文档没有声称 terminate 会撤销已经发给外部服务的请求，也没有声称 Workflow cancel 会回滚外部业务对象。

**E7 — [Activity 的在途取消](https://github.com/temporalio/documentation/blob/main/docs/encyclopedia/activities/activity-execution.mdx)（官方产品文档，强度：高；局限：依赖 Worker/SDK 行为和 Activity 的合作）。**

Activity 只有在发送 heartbeat 且设置 Heartbeat Timeout 时才能从 Temporal Service 收到取消；不 heartbeat 会使取消通知延迟。收到取消时，Activity 在下一次可用机会抛出错误；实现可以让取消错误继续传播，也可以捕获并继续执行。Workflow 可以等待 Activity 接受取消，也可以不等待继续走后续逻辑。事件参考进一步区分 `ActivityTaskCancelRequested` 与 `ActivityTaskCanceled`，后者带有 Activity 确认取消时报告的 details。

这提供了 `cancel requested` 与 `cancel observed/recorded` 的状态差异，但 heartbeat timeout、SDK delivery 和 Activity 代码都不是外部副作用的完成确认。

**E8 — [Saga compensation](https://github.com/temporalio/samples-java/blob/main/core/src/main/java/io/temporal/samples/hello/HelloSaga.java)（官方代码示例，强度：中高；局限：示例机制，不是成功率或生产保证）。**

Temporal 官方 `HelloSaga` 示例明确把“已成功完成的工作”与“补偿动作”分成两个 Activity，并说明补偿仅在显式调用 `saga.compensate()` 时执行；补偿可以在异常处理路径中按注册顺序的反向逻辑执行。这个示例证明 Temporal 提供应用层补偿编排能力，不证明取消会自动触发补偿，也不证明补偿成功后业务 post-state 已被独立验证。

## 4. OAuth：authority stop 也有传播和缓存窗口

**E9 — [RFC 7009](https://datatracker.ietf.org/doc/html/rfc7009)（IETF 规范声明，强度：高；局限：规范没有部署级时延分布）。**

OAuth 令牌撤销端点的语义是令牌失效；RFC 7009 写明失效在授权服务器上立即发生，撤销后的令牌不能再次使用，但同时承认传播延迟：某些服务器可能已经知道失效，其他服务器尚不知道，规范要求实现尽量缩短窗口但没有给出上界。撤销响应的 HTTP 200 既可能表示成功撤销，也可能表示客户端提交的是无效令牌，因此 200 不能作为“一个此前有效的动作已经被所有资源服务器拒绝”的完成证明。

RFC 7009 还允许撤销相关 access token、refresh token 和 authorization grant，但级联范围取决于授权服务器策略；如果服务器不支持 access-token revocation，撤销 refresh token 不会立即使对应 access token 失效。

**E10 — [RFC 7662](https://datatracker.ietf.org/doc/html/rfc7662)（IETF 规范声明，强度：高；局限：`active` 由实现决定，缓存仍可能陈旧）。**

Introspection 的 `active` 是令牌当前是否活跃的布尔指标，但“active”的具体含义取决于授权服务器保存的状态。受保护资源可以缓存 introspection 响应；RFC 7662 明确指出，令牌可能在缓存有效期内被撤销，而资源服务器继续依据旧缓存做授权决定，形成撤销令牌仍被使用的窗口。若响应包含 `exp`，缓存不得超过该时间；规范没有给出从 revoke request 到各资源点 deny-effective 的实测数据。

OAuth 因而主要覆盖 authority stop：令牌/授权状态变为不可用。它不定义已发送 HTTP 请求是否被终止，也不定义已经提交的数据库、支付或文件副作用如何回滚。

## 5. AWS Step Functions：停止调用有时间戳，但查询本身可能滞后

**E11 — [StopExecution API](https://docs.aws.amazon.com/step-functions/latest/apireference/API_StopExecution.html)（官方 API 契约，强度：高；局限：没有下游 effect 语义）。**

`StopExecution` 成功时返回 HTTP 200 和 `stopDate`，其含义是执行停止的日期。该 API 页面只规定“Stops an execution”，没有说明已经启动的 Lambda、HTTP、消息或其他外部系统动作是否会被撤销、终止或补偿，也没有幂等键或业务 post-state 验证要求。

**E12 — [DescribeExecution API](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DescribeExecution.html)（官方 API 契约，强度：高；局限：明确不是实时观测）。**

`DescribeExecution` 提供 `startDate`、`stopDate` 和 `status`；状态包括 `RUNNING`、`SUCCEEDED`、`FAILED`、`TIMED_OUT`、`ABORTED` 和 `PENDING_REDRIVE`。但页面明确写出该操作 eventual consistent，结果是 best effort，可能不反映最近的更新。因而 `StopExecution` 的响应、`DescribeExecution` 看到的 `ABORTED`、以及下游外部 effect 的终止/回滚，至少是三个不同的观测对象。

# 三层语义矩阵

| 材料族 | authority stop | in-flight stop | effect reconciliation | 可观测状态/时间 | 证据性质 |
|---|---|---|---|---|---|
| MCP Tasks 核心 | 任务级取消，不是凭据撤销 | 应尝试停止；任务可先变 `cancelled` 而执行继续 | 未定义 | `createdAt`、`lastUpdatedAt`、TTL、轮询；通知可选 | 规范声明/示例 |
| MCP Tasks Extension 草案 | 取消意图 ack，不保证最终取消 | 服务器不被要求真的停止 | 未定义 | ack 与可观察状态可暂时不一致 | 草案规范 |
| A2A 1.0 | 任务状态控制，不是 token authority | “attempts to cancel”，成功不保证 | artifacts 不是 post-state/rollback 证明 | Task status、可选 timestamp、stream terminal | 规范声明 |
| Temporal | Workflow cancel/terminate 改变编排执行状态 | Activity 需 heartbeat，代码可延迟、忽略或继续；可选择等待 | 显式 Saga/compensation，由应用调用和验证 | Event History、heartbeat、timeout；无实测延迟分布 | 产品文档/官方示例 |
| OAuth RFC 7009/7662 | 令牌/授权失效；传播和缓存可能延迟 | 不覆盖已发请求 | 未定义 | `active`、`exp` 等状态/时间；无撤销时延数据 | IETF 规范 |
| AWS Step Functions | `StopExecution` 停止编排执行 | API 页面未定义下游动作是否停止 | API 页面未定义回滚/补偿 | `stopDate`、status；Describe eventual consistent | API 契约 |

# 时间、状态与完成确认：哪些是真实数据，哪些只是能力

## 本轮新增材料实际提供了什么

- **可用来记录状态/时间，但不是实测数据**：MCP 核心要求任务有创建和最后更新时间；MCP 草案有 TTL 和轮询间隔；A2A 定义 status timestamp、Task 快照和流终止；Temporal 定义事件、heartbeat 与 timeout；AWS 定义 `startDate`、`stopDate`、status。它们给出了未来实验的事件字段或查询接口。
- **提供任务级/编排级完成确认，但不是副作用完成确认**：MCP `cancelled`、A2A `TASK_STATE_CANCELED`、Temporal 的取消/终止事件、AWS `ABORTED` 都是其控制面对象的状态。它们没有共同定义“外部 effect 已停止”“副作用没有提交”或“业务不变量已恢复”。
- **真正的撤销传播窗口声明**：RFC 7009 直接承认跨服务器 propagation delay；RFC 7662 直接承认缓存导致 revoked token 仍可被使用。MCP Extension 也直接承认 ack 与可观察状态可不一致。以上是规范对可能窗口的声明，不是测得的 p50/p95/p99。
- **本轮没有新的实测数据**：没有材料报告一组真实 Agent 请求的 `revoke_requested_at → deny_effective_at` 分布、`request_sent_at → terminated_at` 分布、已提交 effect 的数量、补偿成功率或 MTTR。Temporal 的 HelloSaga 是可运行代码样例，A2A/MCP 的带时间 JSON 是协议示例，不能充当观测样本。

## 与已有材料的区别

2026-09-05 日志中的材料才提供了有限的实测/生产锚点：HBHC 报告 49-agent 受控实验中的零 post-revocation tool calls，并给出基于 heartbeat、时钟偏差和窗口的界；ACRFence 报告小规模 checkpoint-restore 重复 commit 与 token reuse 结果；GitHub availability report 是一个非 Agent 的生产事故，按 12:16 恢复账号、12:20 加豁免、12:48 刷新缓存、12:56 确认完全恢复记录了多步恢复时间线。它们分别更接近 authority stop、effect duplication 和生产 recovery verification，但已有日志已经核对，本轮不重复计数，也不能把其中任何一个推广成所有 Agent 系统的保证。

# 对 EX-005 的影响

本轮结论为 **refined，不新增 EX，不晋升稳定页**。

1. `EX-005` 的三层划分获得跨系统/协议的独立支持：OAuth 把令牌失效与传播/缓存分开；MCP/A2A 把 cancel request/ack/status 与真实 task stop 分开；Temporal 把 Workflow cancel、Activity cancellation、terminate 和 compensation 分开；AWS 把 stop API、状态查询和 eventual consistency 分开。
2. 需要把“撤销成功”的判定从单一布尔值改为带作用域的事件链：`revoke_requested`、`authority_denied`、`request_sent`、`inflight_terminated_or_completed`、`external_effect_committed`、`compensation_started`、`compensation_succeeded`、`post_state_verified`。其中 `cancelled`、`ABORTED`、`active=false` 只能填充部分控制面字段，不能自动填充后面的业务事实。
3. effect reconciliation 目前没有被通用协议闭合。Temporal 是新增材料中最明确提供补偿编排能力的系统，但其官方示例也把补偿写成应用显式调用；它不表示取消会自动补偿，更不表示补偿后的外部状态已验证。
4. 时间指标必须按对象和分母分别计算，而不能从状态字段差值直接宣称恢复成功：
   - `T_authority = deny_effective_at - revoke_requested_at`，分母是每个 action surface 上实际发出的 revoke 请求；
   - `T_inflight = terminal_or_commit_at - revoke_requested_at`，分母是撤销前已经 sent/accepted 的在途动作；
   - `T_reconcile = post_state_verified_at - effect_committed_at`，分母是已产生且需要对账的外部 effects；
   - 另报撤销后仍完成的在途比例、重复 effect 比例、补偿成功比例和 post-state 不变量恢复比例。
5. 本轮还强化了 `EX-005` 与 `CR-004` 的接口：trace 中有 task ID、status timestamp 或 stopDate，只能证明控制面事件可见；要证明 effect reconciliation，仍需同一 `event_id/trace_id` 关联外部提交、幂等键、补偿和 post-state 读回。与 `EX-006` 的关系是：policy state 抵达动作门之后，仍可能有在途和已提交副作用残差。

# 新问题

在同一 action-surface manifest、相同 policy/verdict 和相同任务 trace 下，**“任务已进入 cancelled/ABORTED”是否应被视为一种仅限编排层的状态，还是协议应进一步要求一个外部 effect ledger 与 post-state confirmation？** 更具体地说：当 MCP/A2A/Temporal 的控制面已经报告取消时，能否用同一 `event_id` 唯一回答“是否已发出”“是否已提交”“是否仍可重试”“是否已补偿”“业务不变量是否恢复”？

当前未知点是：这些协议设计上的弱取消语义，在接入带幂等键、服务端消费记录和可读 post-state 的下游后，是否会被下游语义完全吸收；还是仍会留下跨协议、跨区域、长连接和异步队列共同存在的独立安全残差。

# 证伪方向

- 在固定任务、Agent trace、policy、verdict 和 action-surface 后，若 MCP/A2A/Temporal 的取消适配器都能通过下游 fence 在固定上界内阻止所有撤销后的新调用和在途提交，且所有已提交 effects 都能用同一幂等键唯一重放或补偿，并由 post-state 读回证明不变量恢复，则三层边界应收窄为一个由下游事务语义吸收的统一 revoke transition。
- 若在固定 `deny_effective_at` 后，所有真实完成请求都能在控制面状态中被唯一枚举，且 `cancelled`/`ABORTED` 与外部 commit/compensation 之间不存在遗漏或延迟差异，则“控制面终态不等于 effect 终态”的判断应收窄为当前实现缺口。
- 反过来，若令牌撤销在可控缓存 TTL 内只改变后续 introspection 结果，而已建立连接、消息队列消费或下游重试仍可产生 effect，则 authority stop 与 in-flight/effect 三分法继续成立。
- 若 Temporal 的显式 Saga compensation 在故障、重试和 Worker 重启下仍能无重复地完成，并且官方事件能与外部 post-state 唯一关联，则应把它作为 effect reconciliation 的强反例；若补偿失败、重复或无法验证，则不能从“存在 compensation API”推出恢复保证。

# 最小实验建议

做一个单一可回放 mock tool，具有四个可观察动作：`authorize(token)`、延迟的 `commit(event_id, idempotency_key)`、`query_post_state(event_id)` 和显式 `compensate(event_id)`。在 MCP Tasks、A2A Task、Temporal Activity 三个适配器中执行同一任务；OAuth 只作为 authority/cache 对照，不需要引入真实支付或生产系统。

随机化四个取消时点中的前三个即可保持最小：

1. `revoke/cancel-before-send`；
2. `revoke/cancel-after-send-before-commit`；
3. `revoke/cancel-after-commit-before-retry`。

每次记录：`revoke_requested_at`、`deny_effective_at`、`request_sent_at`、`cancel_ack_at`、`status_observed_at`、`inflight_completed_at`、`external_commit_at`、`compensation_at`、`post_state_verified_at`、`event_id`、`idempotency_key`、`action_surface`、`policy_version` 和 `result`。至少比较四个结果：新调用放行率、撤销后仍完成的在途比例、重复/越权 effect 比例、post-state 不变量恢复率；另报告 `T_authority`、`T_inflight`、`T_reconcile` 的分布及其明确分母。

最小判定规则：若三种适配器都只改变 task/status 而不改变在途完成或外部提交，三层边界得到直接支持；若服务端幂等/fence 在固定上界内吸收所有差异，则把 `EX-005` 收窄为“跨协议控制面如何接入下游事务语义”，而不是宣称通用 Agent recovery gap 已独立存在。

# 来源索引与证据等级

- **高：规范/API 契约**：[MCP Tasks](https://modelcontextprotocol.io/specification/2025-11-25/basic/utilities/tasks)、[MCP Cancellation](https://modelcontextprotocol.io/specification/2025-11-25/basic/utilities/cancellation)、[A2A Specification](https://a2a-protocol.org/latest/specification/)、[RFC 7009](https://datatracker.ietf.org/doc/html/rfc7009)、[RFC 7662](https://datatracker.ietf.org/doc/html/rfc7662)、[AWS StopExecution](https://docs.aws.amazon.com/step-functions/latest/apireference/API_StopExecution.html)、[AWS DescribeExecution](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DescribeExecution.html)。这些可支持语义和字段存在，不支持部署效果。
- **高但版本受限：草案**：[MCP Tasks Extension Draft](https://tasks.extensions.modelcontextprotocol.io/specification/draft/tasks)。它对 eventual consistency 和 cooperative cancellation 的描述很直接，但截至 2026-09-06 是 Draft，不能当作稳定互操作保证。
- **中高：官方产品文档与代码示例**：[Temporal cancellation](https://docs.temporal.io/develop/java/workflows/cancellation)、[Temporal Activity Execution](https://github.com/temporalio/documentation/blob/main/docs/encyclopedia/activities/activity-execution.mdx)、[Temporal Events](https://github.com/temporalio/documentation/blob/main/docs/references/events.mdx)、[Temporal HelloSaga](https://github.com/temporalio/samples-java/blob/main/core/src/main/java/io/temporal/samples/hello/HelloSaga.java)。这些可支持实现机制、事件名和补偿调用方式，不支持成功率或恢复时限。
- **重复但用于校准**：[HBHC](https://arxiv.org/html/2605.20704)、[ACRFence](https://arxiv.org/html/2603.20625)、[GitHub May 2026 availability report](https://github.blog/news-insights/company-news/github-availability-report-may-2026/)。它们已在 2026-09-05 日志核对，本轮不计入新增材料。

未使用原始网页中的提示、指令性文本或与本问题无关的内容；来源只作为事实和规范语义的证据。
