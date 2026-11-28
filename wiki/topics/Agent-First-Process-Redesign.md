---
type: topic
title: Agent-First Process Redesign
created: 2026-04-09
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - AI-Agent
  - Enterprise-Transformation
  - Process-Design
related_entities:
  - '[[Agent-First-Enterprise]]'
  - '[[Human-Governor-Agent-Operator]]'
  - '[[Machine-Readable-Processes]]'
  - "[[AI-Ready-Organization]]"
  - "[[Integration-Wall]]"
  - "[[Alignment-Tax]]"
  - "[[Forward-Deployed-AI-Enablement]]"
  - "[[Escalation-Based-Human-Oversight]]"
  - "[[AI-Deployment-Valley-of-Death]]"
source_raw:
  - "[[20261119-latentspace-linear-cristina-cordova-gtm-100m-arr]]"
  - "[[20261113-anthropic-building-always-on-agents]]"
  - "[[20261110-latentspace-resend-designing-for-agents]]"
  - '[[Enabling agent-first process redesign]]'
  - '[[20260502-most-companies-arent-ready-for-ai]]'
  - '[[The layoffs will continue till we learn to use AI]]'
  - "[[20260601-stanford-enterprise-ai-playbook]]"
  - "[[20260825-enterprise-ai-workflow-redesign]]"
  - "[[20260911-github-marketing-ops-as-code]]"
---

# Agent-First Process Redesign（Agent-First 流程重构）

## Linear：Agent 创建 Issue 的指标不应替代实际完成结果（2026-11）

[[20261119-latentspace-linear-cristina-cordova-gtm-100m-arr]]（**20:00–23:39、36:14–42:23**）与本页原有「流程终态不能由文本声明替代」观点直接互证。Linear 披露 Agent 创建的 Issue 比例从约一年前的 3% 升至超过 50%，但该指标只说明**入站工作登记**发生变化，并不描述处理、审查、合并、上线、客户受益。对于外部客服，Linear 仍让 AI 生成答复草稿，**由真人审核和发送**，没有把自动生成消息等同于真正履约。

- **综合判断**：工作流 KPI 明确分开 `created → triaged → claimed → acted → verified → accepted/released`；客户沟通则分开 `drafted → approved → sent → delivered → resolved`。将自动化覆盖率与准确性/用户受益、人工监督成本和异常回滚一起观察。
- **证据**：[[20261119-latentspace-linear-cristina-cordova-gtm-100m-arr]]（20:00–23:39、36:14–42:23）；[Linear CEO 2026-08-26 公告](https://linear.app/now/sharing-growth-with-the-people-building-linear)。
- **边界**：Linear 原始指标中的 Agent Issue 创建量不能直接与 n8n Broker 的任务完成数类比；必须先对齐采样窗口、分母与任务定义。



## Inbox 不接收未来定时，Outbox 也不是业务终态（2026-11）

[[20261113-anthropic-building-always-on-agents]]（「Event inbox / Timers / Outbox」）将三个容易混淆的工作流分离：未来提醒/周期计划位于独立 Timer store；到期后 scheduler 创建 Inbox event；worker 处理事件，完成 run 后可以发消息、**静默结束**或以 deferred tool call 暂停等待批准。发送回执由 dispatcher 管理，与实际工作成功状态分离。

- **判断（综合）**：`source_event → durable inbox → claimed work/run → completion receipt` 与 `schedule/follow-up → due occurrence → inbox`、`notification intent → outbox → provider ack` 应是独立状态机。Inbox 的快速 ACK 不代表外部副作用已经成功，worker 在 crash 后可重试也不代表已天然 Exactly-once。
- **对现有 n8n Broker 的候选检验**：检验原本的 Claim/CAS/lease 在同一任务重复入队和多个 Worker 竞争时是否只允许一次业务动作；对 timer fire/写事件的故障边界、通知失败及幂等回执作独立试验，而不引入第二套调度/队列系统。
- **边界**：作者建议每用户 inbox 同时一个 active worker，并非要求整个调度系统只有一个消费者；静默通知是用户体验策略，不能吞掉任务结算/必须通知的业务要求。
- **证据**：[[20261113-anthropic-building-always-on-agents]]（Event inbox、Timers、Outbox）。



## Resend：别将「接口成功」误认为业务交付成功（2026-11）

[[20261110-latentspace-resend-designing-for-agents]]（**06:54–23:55、50:29–57:26**）以邮件送达为反例：提交发送请求后仍有队列、Gmail 等收件方限流、IP/域名信誉、退信投诉、共享 tracking 域的恶意邻居污染，最终是否进入收件箱/真正被阅读更是不同层级的状态。Resend 通过 Domain Connect 降低 DNS 配置门槛，支持工程团队的 Git 模板和市场团队的协作编辑器，说明 **面向 Agent 的自动化入口与人类协作/审批入口可共享同一业务规则而非互相取代**。

- **判断（综合）**：企业工作流至少区分 `command submitted → provider accepted → queued → external acknowledgment → completed/failed → reconciled`，为不同层级记录回执、重试、事故与补偿；减少用户/Agent 需要手工掌握的低层操作，但对 DNS/身份/账单等状态变更保留权限校验。
- **证据**：[[20261110-latentspace-resend-designing-for-agents]]。
- **边界**：送达外部邮箱并不保证真人读信；邮件域名信誉与数据/权限隔离经验不能直接转成其它行业的性能数值。



> [!summary] 核心洞察
> Agent-First 不是把 Agent 接到旧流程上，而是重新设计流程，让机器能读取目标、执行常规路径、暴露异常，并让人类从流程节点上移到治理节点。

## 旧流程为什么不能直接接 Agent

传统流程假设人类是默认执行者：人知道例外、会问同事、会在系统之间手工搬运信息，也会用组织默契补上文档缺口。Agent 没有这些默契。把 Agent 插到这种流程中，只会把隐藏混乱放大。

[[AI-Ready-Organization|AI 就绪组织]]的前提正是组织自我描述能力：目标、项目、负责人、数据、成本和成功标准能否被清楚说出。若组织无法描述自己，Agent 只能在局部任务上显得聪明，无法稳定改变运营系统。

## 三层重构

| 层级 | 旧问题 | Agent-First 处理方式 |
|------|--------|----------------------|
| 目标层 | 目标写在会议和个人理解里 | 目标、指标、拒绝条件显式化 |
| 流程层 | 人在系统之间补缝 | [[Machine-Readable-Processes]]（机器可读流程）、结构化输入输出 |
| 治理层 | 异常靠资深员工临场判断 | [[Human-Governor-Agent-Operator]]（人类治理、Agent 执行）、升级路径 |

重构的核心不是“减少人”，而是重新分配人类工作：人类定义目标、约束、例外和价值判断；Agent 处理可重复执行、可观察、可回滚的路径。

## 例外升级式监督

Stanford 51 个成功部署案例补充了一个重要细节：人类监督不是越多越安全，也不是越少越高效。[[Escalation-Based-Human-Oversight|例外升级式监督]] 是候选模式，而非普遍最优。

在这种模式里，Agent 处理常规路径，人类处理例外、边界、高风险判断和清障。[Stanford 原报告](https://digitaleconomy.stanford.edu/publication/enterprise-ai-playbook/) p.30 图6：在选择的成功案例中，例外升级（80%+自动处理）中位/平均收益71%/63%，逐项审批30%/44%，协作30%/43%。观察性分组非随机监督干预，任务风险、类型和成熟度可能混杂；80%是分类口径而非推荐比例，71%不是预期收益。

这把 Agent-First 的治理原则具体化了：流程重构要同时设计“自动完成路径”和“升级给人的路径”。没有升级路径，自动化会放大错误；没有常规自动路径，人类仍被困在流程节点上。

## 三类人-AI 交接的操作参数（08-26 补充）

[[20260825-enterprise-ai-workflow-redesign|Workflow Redesign（2026-07）]]把「例外升级式监督」细化为三类 handoff，每类带准确率阈值、风险与度量：

| 交接类型 | AI 角色 | 人角色 | 适用条件（经验值） | 关键风险 | 度量 |
|---------|--------|--------|-------------------|---------|------|
| **AI 优先** | 产首稿/推荐/分类 | 验证、批准或纠正 | 按任务错误损失、可纠正性与审查能力校准；85%仅原作者经验值 | 审查走过场 → 错误累积 | 必须定义"审查要检查什么"而非只定义"要审查" |
| **人优先** | 实时建议/检索上下文/标记问题 | 主导工作 | 需判断与创造力，AI 无法复制 | AI 频繁打断/经常错 → 被关闭 | 建议接受率（非功能激活率） |
| **全自动** | 端到端处理，仅超标升级 | 只处理例外 | 高量、风险有界；按误放行/误拒绝及真实结果确定门槛，95%非通用标准 | 例外队列被忽略 | "自动化前先构建例外工作流" |

**AI 改写率（override rate）作为诊断信号**：更改/拒绝率需结合原输出质量、审核正确性、错误严重度、漏改、误改与复核时间。撤回 <5%必为橡皮图章、>40%必无效、10–25%为理想区间的无出处通用门槛；低改写可源于高质量，高改写可源于合理个性化。

**Deloitte 量化背景**：[AI Pulse Check 2026](https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/blogs/pulse-check-series-latest-ai-developments/ai-transformation-predictions-2026.html) 约3700专业人士，48%受访者称引入AI未改工作流或角色，12%称以新运营模式规模化重构；不是项目失败率、代表性企业分布或本库成熟度等级的实测。

## GitHub APAC：把营销运营写成可审查的执行系统（2026-09）

GitHub APAC marketing team 提供了一个非工程职能的具体样本：把“一个活动”建模为一个 Issue，用 Issue form 收集结构化输入，用 label 触发 Actions，再由 API/CLI 适配器创建落地页、UTM 链接、邀请文档、项目板和会后摘要。Issue 不只是待办清单，还提供状态历史、可见性、审查入口和稳定 URL。

这里的 Agent-First 分工不是让 Copilot 独自操作：团队先把命名、财季、时区和邮件规则写入 `AGENTS.md`，让 Copilot 根据对话起草；人决定是否采用并 sign off。市场差异放入 `SKILL.md`，通过 PR 和 CODEOWNERS 进入组织治理。`DRY_RUN`、测试、代码审查、secret scanning 和数据政策构成护栏，而每日 cron 的失败必须能被发现——文章记录了一次晨间筛选 workflow 静默失败五天的反例。

> **判断（综合判断）**：流程重构的最小可复用单元不是“一个更聪明的 Agent”，而是“结构化状态对象 + 明确事件 + 确定性执行器 + 人类决策点 + 可观测失败”。
>
> **证据**：GitHub 案例把 Issue form、label、Actions、runbook、Skills、dry-run 和审批串成一条从计划到跟进的链路（见 [[20260911-github-marketing-ops-as-code]]）。
>
> **边界**：该模式依赖可用的 API/CLI 和可写清楚的业务规则；高判断密度、强合规或不可逆流程仍需更深的权限、数据和升级设计。

## 经济驱动：不要做漂亮试点

MIT Technology Review Insights 的文章提醒，Agent-first 的判断标准不是试点是否炫目，而是是否改变服务成本、交易成本和决策速度。一个 demo 能跑，不等于流程被重构。

最小判断问题是：

- 这个流程的输入输出是否能结构化？
- 成功与失败是否可判定？
- Agent 犯错时是否有清楚的停止和升级路径？
- 如果第 10 次运行仍需同样多人工解释，是否说明没有形成复用能力？

## 对齐税会被流程重构放大

[[Alignment-Tax|对齐税]]解释了一个反直觉问题：AI 让产出更快，可能让组织冲突更快暴露。以前一个团队要花几周才能做出错误方向的原型；现在 Agent 可以一天内做出多个互相冲突的版本。

所以 Agent-First 流程重构必须先处理目标、权限和验收标准。没有人类对齐，所谓人机对齐只是在把分歧自动化。

## 与 FDE 的关系

[[Forward-Deployed-AI-Enablement|FDE 式 AI 赋能]]是 Agent-First 流程重构的现场方法。很多企业不是缺少 Agent API，而是不知道哪条真实流程值得重构，也不知道遗留系统、权限、合规和采用阻力在哪里。

FDE 的现场工作把流程问题暴露出来；Agent-First 的设计原则把现场发现变成可复用流程。两者合起来，才能从一次性项目变成组织能力。

## 与 Organization-as-Agent-Harness 的区分

[[Organization-as-Agent-Harness]] 和 Agent-First Process Redesign 都讨论如何让组织适配 Agent，但切入层次不同：

| 维度 | Organization-as-Agent-Harness | Agent-First Process Redesign |
|------|------------------------------|------------------------------|
| 焦点 | 组织整体作为 Agent 运行环境 | 具体流程的改造方法 |
| 层次 | 目标层、流程层、权限层、学习层 | 目标层、流程层、治理层 |
| 核心问题 | 组织如何成为 Agent 的 Harness | 旧流程如何被重新设计 |
| 典型输出 | 组织架构设计原则 | Machine-Readable Processes |

两者的关系是：Organization-as-Agent-Harness 提供了”组织应该长什么样”的愿景，Agent-First Process Redesign 提供了”如何从旧流程走到那里”的路径。

## 反例与边界

**反例 1：不适合 Agent-First 的流程**。并非所有流程都适合 Agent-First 重构。高风险、强监管、低容错的流程（如医疗诊断、金融合规审查、核设施控制）可能需要人类始终在回路中，而不是”Agent 执行、人类治理”。[[Enabling agent-first process redesign]] 本身也承认，legacy process 不是为 autonomous systems 建的，但没有讨论哪些流程根本不应该 autonomous。

**反例 2：组织自我认知缺失**。[[20260502-most-companies-arent-ready-for-ai]] 指出，大多数公司无法清晰描述自己在解决什么问题、策略是什么、工作流如何运作。这种组织自我认知缺失是 Agent-First 的前置障碍——如果组织不知道自己是什么，就无法设计机器可读的流程。这不是技术问题，而是管理问题。

**反例 3：Flashy Pilots 陷阱**。[[Enabling agent-first process redesign]] 警告，很多组织不了解完整经济驱动因素（如 cost to serve、per-transaction costs），因此容易优先做 flashy pilots 而不是最有价值的 agent 用例。Demo 能跑不等于流程被重构；试点成功不等于可以规模化。Agent-First 的判断标准应该是”是否改变了服务成本、交易成本和决策速度”，而不是”是否看起来很炫”。

## 跨来源综合：Agent-First 的四层成熟度模型

综合 [[Enabling agent-first process redesign]]、[[20260502-most-companies-arent-ready-for-ai]] 和 [[The layoffs will continue till we learn to use AI]] 三个来源，可以构建 Agent-First 的四层成熟度模型：

| 成熟度 | 特征 | 典型表现 | 来源 |
|--------|------|---------|------|
| Level 0: 混乱 | 无法描述自己的目标和流程 | “大多数公司是混乱的黑箱” | Most companies aren't ready |
| Level 1: Copilot | 把 Agent 插入旧流程做辅助 | Flashy pilots，增量收益 | Enabling agent-first |
| Level 2: Agent-First | 围绕 Agent 重新设计流程 | Machine-Readable Processes，人类治理 | Enabling agent-first |
| Level 3: 组织学习 | Agent 使用过程成为组织学习资产 | Public-only，渗透学习，Skills 沉淀 | Layoffs will continue |

四层为本库诊断启发，不是经过验证的顺序、总体分布或晋升量表。各流程可采用不同自动化程度；保留人主导的高价值流程不意味着组织不成熟。

## 与现有 Topic 的关系

- [[Organization-as-Agent-Harness]]讲组织作为 Agent 运行时需要目标、流程、权限和学习层。
- [[AI-Labor-Bottleneck-Shift]]讲 AI 让瓶颈从生成迁移到对齐、集成和结果。
- [[AI-Apprenticeship-and-Lehrwerkstatt]]讲 Agent 使用过程如何成为组织学习资产。
- 本 Topic 聚焦流程层：如何把旧工作流改造成 Agent 可以稳定运行的系统。

## 结论

Agent-First 的第一性原理不是”让 Agent 做更多事”，而是让流程变得可读、可控、可验证。

如果流程只能靠人类默契运行，Agent 只能做助手；如果流程被重新设计成机器可读系统，Agent 才能成为运营层。
