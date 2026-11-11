---
type: source-summary
title: "The five components of building a company harness"
canonical_url: "https://www.langchain.com/blog/components-building-company-harness"
canonical_key: "company-harness-control-plane"
promotion_id: "kp-20261026-company-harness"
work_id: "wiki_compile:company-harness-control-plane:20261026:recovery-v1"
correlation_id: "knowledge-promotion:week-of-2026-10-26"
raw_state: index
original_raw_file: "20261024-langchain-company-harness.md"
original_body_sha256: "8cb83f6987a5415608ae8e34e5ce0178bcdbb5c9ecdd8bfb6239839b2850f444"
indexed_at: "2026-11-11T14:18:00.656+08:00"
created: 2026-10-28
updated: 2026-11-11
tags:
  - source-summary
  - agent-harness
  - enterprise-ai
evidence_level: medium
claim_type: mixed
source_locator:
  - "Opening list: five recurring company-harness primitives"
  - "Problem: User Experience: Slack DM/channel, breakout thread, batch email review dedicated UI"
  - "Problem: Identity: OpenSWE foreground/background, GTM DM-only email, Content Studio Twitter whitelist"
  - "Problem: Identity: OBO vs fixed identity and context-dependent tool availability"
  - "Problem: Memory: global and per-user scopes"
  - "Problem: Code Execution: sandbox plus authenticated service access"
  - "Problem: Scheduled Runs: background/event-triggered execution"
---

# The five components of building a company harness

> **来源生命周期与证据边界**：公开全文稳定可由 canonical URL 的 Opening list / Problem: User Experience / Identity / Memory / Code Execution / Scheduled Runs 等章节恢复。此前 Raw 仅是约 2.5 KB 的 bounded evidence clipping，并非原文全文；本页 `original_body_sha256` 代表这份摘录的哈希，而不是网页原文正文校验值。2026-11-11 已将错误的 `raw_state: full` 修正为 `index`，没有制造或声称拥有完整离线全文。
>
> LangChain 对 GTM Agent、OpenSWE、Content Studio 三类内部 Agent 的一手经验总结。它提供的是公司级 Agent runtime primitives 的案例证据，不是跨企业比较或最优架构证明。

## 编译摘要

### 1. 浓缩

#### 核心结论 1：company harness 的共性正在从“prompt 规范”转向运行时 primitives

LangChain 将三类内部 Agent 的共同基础归纳为五项：工作发生处的交互界面、identity、分层 memory、sandboxed code execution + authenticated service access、scheduled/background runs。

**判断**：当 Agent 进入多人、多系统、长期运行场景后，真正稳定复用的架构单元更多是 identity/memory/execution/scheduling 等 runtime primitive，而不是某个具体 prompt。

#### 核心结论 2：identity 不是单一 service account，而是按动作与上下文选择 delegation model

文章同时使用 on-behalf-of 与 fixed identity；同一个 Agent 甚至会按工具、DM/shared channel、foreground/background execution 切换身份模式。

**判断**：企业 Agent 的 identity contract 至少需要回答“谁触发、以谁身份、在什么上下文、哪些工具可见、谁承担结果”，不能把 authentication 简化为一个长期 token。

#### 核心结论 3：ambient work 是 harness 的一等能力

大量运行来自 schedule/event，而不是用户主动发消息。这意味着 company harness 必须把 background identity、权限、context、memory 与观察/通知一起设计，不能只优化同步对话体验。

#### 核心结论 4：多人协作的 UX 需要同时支持「共享可见性」与「任务独立性」

- **原文证据（Problem: User Experience）**：三个内部 Agent 以 Slack 作为主要工作入口，各自注册应用，可 DM 也可在频道里 @。频道中旁观者能学习 Agent 的用法；但 Agent 介入一段人类正在进行的讨论会污染原 Thread，LangChain 为此开发了把 Agent 对话从原线程 **break out** 到独立线程的交互。另一个反例是 GTM Agent 需要人工审核多封待发送邮件：单条 Slack 消息适合临时批准，大量积压不适合用 Thread 逐一管理，因此另建专用 UI。
- **判断（综合）**：交互入口要根据任务状态密度而选——**聊天适合低频请求和协作发现，队列式审批/大量待办需要结构化工作台**；在协作频道保留可见性不等于允许所有成员访问同一用户的数据。
- **边界**：原文描述的是 LangChain 的 Slack 工作流，并没有提供「独立线程提高生产力」或「定制 UI 降低处理时间」的 A/B 测试。

#### 核心结论 5：身份应绑定「调用方式 × 服务 × 动作」，不能只给 Agent 一把万能钥匙

| 内部 Agent | 代表用户执行（OBO） | 固定身份或后台执行（按场景） | 来源特定边界 |
|---|---|---|---|
| **OpenSWE** | 以调用者 GitHub 身份创建 PR | 自动审查 PR 时使用 GitHub App 自身身份 | **前台 OBO / 后台独立主体** |
| **GTM Agent** | 邮件工具 OBO 调用者；Salesforce 部分工具使用固定身份 | 每日简报/线索追踪等可后台触发 | **邮件工具仅限私信 DM，在共享频道不可用** |
| **Content Studio** | Notion 工具 OBO 调用者 | 企业 Twitter/X 使用固定企业凭据 | **仅白名单用户可发布，其他用户可只读或拟稿** |

- **原文证据（Problem: Identity）**：作者直接称 identity 是最棘手的问题，上述三种内部产品的 on-behalf-of 和 fixed credentials 均依服务而不同；不能把「在 Slack 频道被 @ 的用户」默认为所有后续动作的授权主体。
- **判断（综合）**：至少记录 `trigger actor / execution principal / delegated authority / channel context / service/resource / allowed operation / audit owner`。定时任务即使最初由某用户要求创建，也需要明确定义后续运行使用哪种身份、如何失效/撤回，而不是永久继承聊天权限。
- **边界**：LangChain 原文没有发布完整 RBAC matrix、token lifecycle、revocation 测试或跨租户审计结果；上述 contract 字段属于可迁移设计建议，不是其公开的现成 API。

#### 核心结论 6：两级记忆、沙箱与后台任务是独立治理对象

- **原文证据（Problem: Memory）**：三个 Agent 使用 **global memory** 和 **user memory**，由 Agent 决定将知识写入哪一层。作者明确承认这是“探索最少”的部分，存在大量待解决问题。**分两层存储不自动解决来源真实性、数据敏感度、跨用户信息泄漏或过期删除。**
- **原文证据（Problem: Code Execution）**：Agent 控制循环在 sandbox 之外，代码运行发生在各自不同基镜像的隔离环境中。OpenSWE 按 channel/user 选择基镜像；sandbox 中需要认证的服务通过 LangSmith Sandbox 的 **secret proxy** 访问。**secret proxy 是公司自述的设计模式，不是本轮独立验证的隔离有效性或权限零泄漏保证。**
- **原文证据（Problem: Scheduled Runs）**：后台执行包括开发者配置的 OpenSWE 新 PR 自动审查，也包括用户要求 GTM Agent 发送日报并由 Agent 创建 cron。二者说明同一后台框架承载**事件触发**与**用户请求的周期计划**。
- **判断（综合）**：区分 `global vs per-user memory scope`、`execution isolation vs credential delegation`、`event trigger vs user-defined schedule`；另外补足实际运行需要的任务所有权、幂等、取消、过期、日志和终态回执。
- **边界**：这些额外的权限/运行保障是企业级综合设计建议，不能倒写为本文已经验证的 LangChain 产品能力。

### 2. 质疑与边界

- 三个样本都来自 LangChain 自己的产品/内部运行环境，不能据此证明五项 primitives 对所有企业都充分或必要。
- memory 仍被作者称为探索较少的区域；“global + user memory”是当前实现形态，不等于已经解决 memory governance/provenance。
- sandbox + secret proxy 说明执行与凭据需要隔离，但没有给出独立攻击测试或完整 side-effect control 证据。
- scheduled/background run 增加 autonomy，也增加 stale context、权限生命周期、重复执行、预算与观测责任；文章主要讲能力，不是完整治理模型。

### 3. 对标与约束

- 与 [[Organization-as-Agent-Harness]]：该 Topic 的目标/流程/权限/学习是组织层抽象；LangChain 五项更像其下的运行时实现 primitives，两者互补而不是替代。
- 与 [[Agent-Harness]]：补充 company/multiplayer 语境中的 identity、memory、sandbox、scheduling 组合。
- 与 [[Agent-Security]]：OBO/fixed identity、context-dependent tool availability 与 secret mediation 都直接落到授权和执行边界。
- 与自动化控制面：scheduled/background work 说明企业 Agent 不只是交互产品，还需要 durable state、幂等、重试、通知和可观测的控制面。

## 重要判断

- **判断**：公司级 Agent harness 可以被拆成组织抽象层与 runtime primitive 层：组织层定义目标/流程/权限/学习，runtime 层提供 interaction surface、identity、memory、sandboxed execution 与 background scheduling。把两层混成“一个更好的 prompt”会同时丢失治理和执行边界。
  - **证据**：[[20261024-langchain-company-harness]]；现有 [[Organization-as-Agent-Harness]] 的跨案例综合。
  - **边界**：LangChain 的五项是内部经验归纳，不是普适必要条件；不同组织仍需按 action surface、监管、数据与运营模式裁剪。

### 关联概念
- [[Organization-as-Agent-Harness]]
- [[Agent-Harness]]
- [[Agent-Security]]
