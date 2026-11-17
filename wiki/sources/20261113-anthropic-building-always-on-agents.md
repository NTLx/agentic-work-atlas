---
type: source-summary
title: "Building always-on agents — William Hu (Anthropic)"
canonical_url: "https://claude.com/resources/articles/building-always-on-agents"
raw_state: index
original_raw_file: "20261113-anthropic-building-always-on-agents.md"
original_body_sha256: "7333a0811230bddb01b46029f1e8b741221dafedec874486d5ad4503fe13b3ba"
indexed_at: "2026-11-17T15:07:25+08:00"
created: 2026-11-17
updated: 2026-11-17
tags:
  - source-summary
  - agent-harness
  - agent-orchestration
  - automation
evidence_level: medium
claim_type: mixed
source_locator:
  - "2026-11-13 / The cycle behind the always-on agent: sleep, event, run, session, writeback"
  - "The core primitives / Event inbox: durable inbox, event handler, worker; dedupe, quick ACK, worker concurrency, batching"
  - "The core primitives / Timers: follow-up vs recurring schedule; durable separate timer store; due event inserted into inbox"
  - "The core primitives / Memory: four categories; pointer vs duplicate; durable files and optional dreaming"
  - "The core primitives / Inside the context window: startup overhead, session continuation, compaction loss"
  - "The core primitives / Permissions: credential proxy, risk classifier auto mode, deferred tool call and resume"
  - "The core primitives / Outbox: delivery lifecycle, quiet runs, dispatcher, notification frequency"
  - "How everything fits together: inbox → run/session → memory/permission → outbox, then event feedback"
  - "Opening paragraphs: Opus 5.5 vs Opus 5 on an Anthropic-mentioned coding benchmark; task-cost statistic is not runtime reliability benchmark"
---

# Building always-on agents：事件驱动的长期 Agent，五个可独立治理的运行时组件

> **原始来源**：Anthropic / Claude 官方文章 [Building always-on agents](https://claude.com/resources/articles/building-always-on-agents)，**William Hu，2026-11-13**。本次已直接读取官方公开正文及各节。该文是官方的**工程设计指导**，不是正式标准或跨厂商对照试验。正文给出五种 primitive、说明其组合方式，但不是可直接运行的完整生产实现。来源可由 `canonical_url` 和上方章节定位回查，故完成编译后按 schema 保留 `index`，不在仓库复制受版权保护的全文。**证据说明**：原先短期创建的 Raw 仅是来源定位摘录；`original_body_sha256` 是该摘录的校验值，**不是**原网页 HTML 或全文校验值，全文始终以官方稳定 URL 与章节定位为准。

## 编译摘要

### 1. 浓缩

#### 核心结论一：“始终在线”并不是进程持续推理，而是可无限重复的休眠—唤醒—执行—记账周期

- **原文（The cycle behind the always-on agent）**：Always-on 是用户体验形容。Agent **多数时间在睡眠**；事件抵达后进入一次 **run**，在包含消息和工具调用 transcript 的 **session** 中工作，结束时写入可持久存储的状态，再休眠。后来的 run 可以新建 session，也可以恢复同一 session。模型核心仍是通用 Agent loop；变化在 loop 外部的架构。
- **原文（opening）**：Anthropic 将近期实用性归因于模型判断力改善和成本下降，并举例称某个**长程编码 Benchmark** 中 Opus 5.5 对比 Opus 5 每个成功任务成本下降 **78%**，而常规负载下降 **40%**。这是**特定基准、模型比较**，不能解读为所有 Always-on Agent 的成本节省或五组件的因果效果。
- **判断（综合）**：统一基本单位 `event → claimed run → session execution → durable state/receipt → sleep`。核心设计对象是**一次可重试的工作及其跨 run 的可审计连续性**，而不是让一个 LLM 永不停机。
- **边界**：该文没有给出长时生产吞吐、可用性、失败重放率或并发多租户基准；不能凭“模型更便宜”就推导不需要预算、配额和守护逻辑。

#### 核心结论二：Event Inbox 是入站事实源，触发器不能直接在外部事件上并发启动 Agent

- **原文（Event inbox）**：最简 Event Inbox 包含 **数据库中的持久事件列表**、**快速写入的 HTTP handler**、**读取事件的 worker**。可用来源事件 ID 去重；建议最初**每用户一个 inbox**，若需要更高并行度再拆。事件到达 → Handler 持久写入并尽快 ACK → Worker 醒来先从 inbox 拉取待处理事件 → 根据新事件或续接事件开启/恢复 session → 完成后更新事件状态。
- **原文注意事项**：一次事件的同步 webhook 响应要快，深入内容检查（例如 prompt injection 检查）可以进入 run；若 worker 运行中崩溃，inbox 仍保留未完成事件；**一个 inbox 同时仅有一个 active worker**，防止重复运行/状态覆盖。运行中进入新事件可推迟到下一轮、纳入当前轮，或中断重启；可**批量合并**多条连续消息，减少不必要重复回复。
- **判断（综合）**：`source_event_id / inbox_partition / event_state / claim_owner / lease_until / run_id / correlation_id / retry_count / terminal_receipt` 构成可实现的最小审计契约。这些字段是**针对可靠执行的延伸设计**，不是作者逐项公布的数据库 schema。
- **边界**：**一 inbox 一 active worker 不等于整个平台只能一个 Worker**。多用户/多工作分区可并行，但必须防止对同一拥有者与同一状态对象双写；Claim/CAS、lease、atomic transitions、幂等副作用和死信/恢复等仍须靠明确实现与测试保证，原文没有给出可照搬的事务 SQL。

#### 核心结论三：Timers 是未来意图的存储，Inbox 只存已经可执行的事件

- **原文（Timers）**：两个类型：**follow-up**（Agent 为自己设定的一次性提醒，如检查对方是否回复）和 **schedule**（固定频率的重复任务）。Timer 放在**独立、持久的存储表**，不混作 Event Inbox 的 pending 队列；scheduler 扫描到期，更新一次性状态或算出下一次 recurring due，然后把一条新事件写入 Inbox，由同一个 Worker 执行。可以自己搭 scheduler，亦可使用 durable execution engine。
- **判断（综合）**：`schedule definition ≠ due occurrence ≠ claimed work item`。一个 recurring schedule 可以产生多个不同日期的 event，每次发火必须有确定 occurrence key；对 user-created follow-up，应保存取消和过期权限。原文没有要求采用 Cron 节点以外的新平台。
- **边界**：计时表独立不自动避免跨表 crash window（定时器标记已发火但事件未写入、或者重复写入）；实现应通过事务/唯一键/outbox 式协调做故障注入验证。时区、DST、迟到触发、停机补偿等是**工程补充**，并非文章已验证的机制。

#### 核心结论四：长期 Memory 不等于历史聊天；只存不能再次查询的事实、指令和进度

- **原文（Memory / Inside the context window）**：Anthropic 将长期记忆类比为可持久的文件目录（实际可由 DB 或 object store 支撑），明确分四类：① **User instructions**（每 run 都加载的行为规则）；② **User notes**（偏好与纠正，可以按主题拆小文件、按需读）；③ **Past messages**（避免重复报告）；④ **Task progress**（长任务的已做/未做和可恢复进度）。**若另一系统是权威事实源，存指针不复制内容**。
- **原文（上下文成本）**：每次运行启动时都有 system prompt + tool definitions + memory files 的固定上下文开销。建议初始上下文保持轻量，并通过 prompt caching 优化成本。续接 session 会带入旧消息与 tool calls，长了需 compact 或新建 session，均会丢细节；真正必须保留的进度要及时写入 Memory。
- **原文（dreaming）**：可以选用跨 session 定期整理记忆的 dreaming，清理过时内容与发现模式；**它是可选能力**，不是持久化或继续工作所必需的核心闭环。
- **判断（综合）**：`context window ≠ durable memory ≠ source-of-truth business state`。知识/用户偏好之外，处理中的队列状态应留在权威状态机；run 可以用只读指针访问它，避免 Agent Memory 与数据库并行宣称真相。对长期记忆补充 scope、provenance、TTL、修正/撤销和信息最小化。
- **边界**：四类记忆是建议分类，不保证已经解决隐私/权限、跨用户污染、过时 Claim 和记忆改写误差。Prompt caching 仅降低特定缓存条件下费用，不能保证内存无界。

#### 核心结论五：Permissions 的核心是可持久化的人工延期决策，而不只是“自动批准/自动拒绝”

- **原文（Permissions）**：Always-on run 通常持有用户权限而没有人实时观察。对每个工具调用，可自动执行、阻止，或**延期等待用户批准**。敏感凭据不直接放在 agent sandbox，而由环境外的 proxy 在发往目标系统时注入。Auto mode 通过 classifier 审查较高风险动作；文章强调**重大决定仍需要用户审核**。
- **原文（deferred tool calls）**：工具 hook 将某次操作延期，**中止 run 并将 session 保存在等待中间状态**；向用户展示请求，等其回复作为 **Event Inbox 新事件** 回到系统后，恢复先前 session 并继续工具调用。期间 Worker 仍可处理其它事件。
- **判断（综合）**：`requested action → policy/risk gate → pending approval (durable checkpoint) → user decision event → revalidation → execute once → verified receipt`。将权限审批建模为**状态机中的暂停点**而不是聊天输出中一句“是否同意”，审批的对象需包含 action hash、主体/权限、有效期和状态，批准后要重新校验权限及目标环境。
- **边界**：分类器无法证明高风险行为安全。Proxy 减少明文凭据暴露并不自动限制越权/外传，需审计实际发出的请求与资源范围；延期审批必须处理超时、拒绝、重复点击、任务过期和二次授权等文章未展开的情形。

#### 核心结论六：Outbox 解决“该告诉用户什么、何时告诉、是否送达”，不是每次都发一条消息

- **原文（Outbox）**：一次 run 有三个结局：①发一条出站消息；②认为无需通知、安静结束；③请求用户授权/澄清的延期工具调用。简单 Agent 可使用直接 send tool；**只有要做发送节奏控制或错误恢复时才需要正式 Outbox**。后者用待发送消息表 + dispatcher，读取待发项目并推送到用户界面/消息渠道。
- **原文（Attention）**：过多消息造成噪声，过少消息会错过用户真正需要的信息。建议构建评测量化这项取舍，**默认少打扰，再逐渐赢得用户注意力**。
- **判断（综合）**：区分 `task_done / report_necessary / delivery_queued / provider_ack / user_notified`。AI 应负责判断摘要价值与升级理由，Dispatcher 负责确定性路由、速率、幂等和失败恢复。业务完成与用户收到通知是**不同终态**。
- **边界**：原文没有提供通用发送阈值、具体用户注意力成本、出站跨渠道幂等事务。若系统需要“每次任务都必须输出结果”的业务规则，quiet-run 必须有显式规则例外，不可机械套用此建议。

#### 核心结论七：五组件形成一条循环，不要求五个新微服务

- **原文（How everything fits together）**：各来源把事件写入 inbox；worker 在 new/existing session 运行 agent；run 读取 memory、受 permission 限制采取动作、写回 memory、必要时写入 outbox 由 dispatcher 发送；用户的回复再作为 inbound event，timer 也能安排下次 run。多次短 run 连接起来，产生 always-on 体验。
- **判断（综合）**：核心设计是不变量和职责隔离，不是部署形态。Inbox、Timer、Memory、Permissions、Outbox 可以由现有工作流引擎和同一数据库中不同逻辑实体实现；不必为每个名词新增一项微服务。最小化方案要以失效后可恢复性、实际副作用和权限独立性为准。

### 2. 质疑、边界与未证明的命题

1. **文章是 Anthropic 的架构指导，而不是第三方实测。** 能支持这些组件的工程理由和推荐关系，但没有提供 5-primitive 与其它架构的对照成功率、实测事故密度和系统成本。
2. **“一个 inbox 一个 Worker”是分区并发模型。** 不应写成“整个部署只能运行一个 Agent”。若采用通用任务队列与四个 consumer，只要 Claim/CAS、租约及写入隔离真实保证不重复执行，便可以并发处理独立任务；独立共享状态仍要串行或版本检查。
3. **Webhook 立即 ACK ≠ 业务完成。** 入站处理在持久化成功后才给来源成功回执，异步后续审核不能替代网络边界的鉴权、数据大小约束或输入防护。
4. **Worker Crash 后重试 ≠ Exactly-once 副作用。** Inbox 持久性只能确保机会重试，网络侧可能已发生付款、邮件发送或工单变更。幂等键/外部回执/补偿和最终状态回读仍需设计。
5. **Timer 更新再写 Inbox 存在跨表失效窗口。** 如果非原子，重放、漏发和重复触发仍然可能；原文没有承诺已解决。
6. **Memory file 是模型可读上下文，不是授权数据库。** 不可允许 Agent 修改自身安全策略、他人的 user memory、审批结果或完整性审计；Dreaming 的自动整理需证明不会误删关键证据。
7. **长期 session 会压缩丢失重要上下文。** 关键 Claim 和工作进度应经校验后保存，不能只依赖压缩摘要。
8. **自动风险 classifier 有漏报和误报。** 对资金、隐私、生产修改等高影响操作须有外部权限控制，人类确认与可复审回执。
9. **Deferred approval 无法靠简单提问解决。** 要避免被拒绝后执行、用户授权过期、同一批准多次消费，以及在休眠期目标对象变化造成 time-of-check/time-of-use 问题。
10. **Outbox 的静默原则依业务不同。** 用户体验层适合优先减少噪声，但审计记录/系统终态不应静默；高优先级告警和明确要求每日回报的任务也不能因为 Agent“觉得不重要”而跳过。
11. **收益数字仅为特定模型比较。** Opus 5.5 的 78%/40% 为文中引用 Benchmark，不是 Inbox/Timers 架构降低运营成本的独立实验。
12. **用户与租户边界不由本文完全展开。** 每用户 Inbox 是起步建议；跨组织协作、账号迁移、多租户/跨渠道审计和数据删除仍须另行治理。

### 3. 与现有 LLM WiKi 和 n8n 架构对标（建议，非实施报告）

| 原文原语 | 现有相关知识 | 最小可验证设计 | 不应引入的复杂度 |
|---|---|---|---|
| **Event Inbox** | [[Agent-Harness]]、[[Agent-Workflow-Patterns]] | n8n durable task/event 的消息 ID、Claim/CAS、租约回收、唯一工作完成回执，验证同时触发时无双消费 | 不因文章有 inbox 就另造第二套队列 |
| **Timers** | [[Agent-First-Process-Redesign]] | schedule definition 与具体 due occurrence 分离；同一个 Broker 接收 timer 产生的任务，失效可补偿 | 不让 ChatGPT Worker 自己维护第二份 cron 队列 |
| **Memory** | [[Agent-Knowledge-Management]]、[[Organization-as-Agent-Harness]] | instruction/notes/reported/progress 四类内容；任务状态留在 n8n source of truth，LLM WiKi 仅存可回溯知识/指针，保留所有权与授权边界 | 不复制业务表为记忆文件，不把 Dreaming 强行放入任务闭环 |
| **Permissions** | [[Agent-Security]]、[[Agent-Data-Minimization]] | 独立的授权、敏感工具代理、审批暂停/恢复事件、权限过期和拒绝可验收 | 不让模型自身决定是否越权或伪造用户同意 |
| **Outbox** | [[Agent-First-Process-Redesign]]、[[Agent-Knowledge-Management]] | 区分业务完成、消息生成、Discord/email 发送回执；节流、分级通知和可回读失败记录 | 不让每个 AI Worker 自己独立负责通知与重试 |

#### 可验证的候选试验（提出而未执行）

- **事件一致性**：对同一 `source_event_id` 重复发送 20 次并并发触发不同 worker，确认最终一次业务行为/可审计去重记录；再模拟 Claim 后 crash。
- **Timer 补偿**：故障注入“到期但未入 inbox / 入 inbox 但未确认”，验证事件不丢失、不重复产生实际业务副作用。
- **跨 Run 延期授权**：先暂停敏感工具调用，再测试批准/拒绝/过期/同一批准重复点击，以及重启 worker 后的终态。
- **Memory 最小化**：强制 worker 仅携带任务最小 context 及指针，比较成功率、成本、用户/租户上下文泄露测试。
- **通知质量**：固定 20 个包含噪声事件、必须通知、必须静默、明确需要日报的样例，分别验证 `event → work result → notification decision → delivered receipt`。

## 前提与局限性

- 本文五组件是作者在 Anthropic 生态下给出的**建议架构**，并非新发布的产品强制 API、不可变行业标准或经过第三方审计的系统性能证明。
- 本 Source Summary 使用一手技术文章形成可追溯证据地图；跨系统应用属于综合设计判断，不能写作作者对现有 n8n 系统的诊断或已经完成的生产整改。
- 对长期记忆、细粒度数据最小化、事件 exactly-once、跨表事务、审批超时与外部系统 ACK 的补充属于**工程扩展**，不是原文逐条实现的事实。
- `canonical_url` 能恢复原文；暂时登记的 Raw 仅有来源摘要，不是原文全文，索引状态中的原始摘录哈希也不应冒充文章正文哈希。

## 关联概念

- [[Agent-Harness]]
- [[Agent-Workflow-Patterns]]
- [[Agent-Unit-of-Work]]
- [[Organization-as-Agent-Harness]]
- [[Agent-First-Process-Redesign]]
- [[Agent-Knowledge-Management]]
- [[Agent-Security]]
- [[Agent-Data-Minimization]]
