---
type: entity
title: Integration Wall
aliases:
  - Integration Wall
  - 集成之墙
  - AI 集成之墙
definition: "AI 项目从 demo 到生产落地时遇到的遗留系统、权限、SSO、数据驻留、合规、流程改造和组织采纳约束"
created: 2026-05-22
updated: 2026-11-03
evidence_level: high
claim_type: mixed
tags:
  - AI-deployment
  - enterprise
related_entities:
  - "[[Forward-Deployed-Engineer]]"
  - "[[AI-Ready-Organization]]"
  - "[[Machine-Readable-Processes]]"
  - "[[Deployment-Product-Flywheel]]"
  - "[[Hardware-Sovereignty]]"
  - "[[Evaluation-Set]]"
  - "[[Layered-AI-Sourcing]]"
  - "[[Open-Source-Operational-AI-Framework]]"
  - "[[Alert-Closed-Loop]]"
source_raw:
  - "[[当我们谈论 FDE 时，我们在谈论什么？]]"
  - "[[Forward Deployed Engineer：AI 时代的新宠岗位，到底干什么？]]"
  - "[[The Return of the Deployment Company]]"
  - "[[Open and closed models are on different exponentials]]"
  - "[[20260729-nejm-ai-triggered-rapid-response-mortality]]"
  - "[[20261102-latent-space-legora-legal-agents]]"
---

# Integration Wall（集成之墙）

> [!definition] 定义
> **Integration Wall（集成之墙）** 是 AI 项目从演示进入生产时遇到的真实企业约束：遗留系统、权限模型、SSO、数据驻留、合规、业务流程、人际协作和组织采纳。FDE 的大量价值就在于穿越这堵墙。

## 关键数据点

- yan5xu 文章指出，许多 AI 项目失败不是因为模型不够强，而是因为无法接入客户的遗留系统、认证、数据驻留和工作流。
- 文章将沙盒 demo 与企业现实区分开：让 demo 跑起来只是一小部分工作，大量工作发生在生产环境约束中。
- 宝玉文章也强调，FDE 的核心不是写模型，而是把模型真正接进企业业务：调接口、现场 debug、处理客户环境中的复杂要求。
- OpenAI、Anthropic 和 Google 对 FDE 的投入，反映了 AI 行业从“模型竞赛”转向“落地竞赛”的结构性变化。
- Caffein Chen 文章把集成之墙扩展到治理层：FDE 进入客户现场后，数据、提示、评测集、员工经验和业务规则都会重新划定边界，传统 DLP 和审计流程未必能覆盖。
- Google Research 的水文框架说明，开源也不会自动越过集成之墙。真正让模型进入运营的是 CHMI 开发 Delft-FEWS 适配器，使模型能在水文机构的标准工作流中运行。
- NEJM AI（2026）临床案例给出集成之墙的时间尺度：RWJBarnabas 先在一家学术医疗中心把 Epic Deterioration Index 集成进 EHR，打磨告警送达、自动通知和培训数年，评估后才快速铺向其余 10 家医院——穿墙是持续工程，不是一次性切换；墙后真正运转的是 [[Alert-Closed-Loop]] 而非模型本身。

## 受监管行业的 Vendor Graph：每个新 API 都是一条新的数据处理路径（2026-11）

[[20261102-latent-space-legora-legal-agents]] 把 Integration Wall 的“合规”进一步落到供应商拓扑。Legora CTO Jacob Lauritzen 回顾，早期律所已经完成 Microsoft 365 的安全与供应商审查，因此 Azure 是容易被接受的既有 trust boundary；当时新增 AWS/Google 等云边界会遇到更大阻力。这个具体偏好后来发生变化，但机制没有消失：企业采购不是在真空中选择技术，而是在既有 approved-vendor graph 上增加或减少数据处理路径（28:42–29:36）。

DPA 约束更直接。访谈称 Legora 刻意让 data processing agreement 中的 vendors 保持很少；某个专用模型或语音 API 即使单项能力更强，也会新增数据处理方、合同和治理面。相反，已批准的大型平台如果能覆盖多个任务，即使不是每项都绝对 SOTA，也可能在整体系统上更优（31:15–32:24）。

可以把企业 Agent 的集成成本扩展为：

```text
Integration Cost
= system/API integration
+ identity & permission mapping
+ data residency / retention
+ vendor review & DPA
+ audit / revocation path
+ operational fragmentation
```

**判断**：受监管 Agent 的架构优化目标不是简单的 `best model per task`，而是**在能力增益与 vendor graph 扩张之间做多目标优化**。每引入一个新的模型、MCP server、语音服务或数据处理器，都应视为新增 trust edge；它带来的能力收益要覆盖额外的 DPA、安全审查、数据流向、撤销和故障责任成本。

这也解释了为什么“mostly good enough but already governed”的平台能力有时会战胜 best-of-breed point solution。它不是模型能力判断，而是 Integration Wall 在组织/合规层对技术 Pareto frontier 的重新排序。

- **证据**：[[20261102-latent-space-legora-legal-agents]]（28:42–32:24）。
- **边界**：Azure/Microsoft 的客户接受度来自 Legora 的客户经验，不代表所有律所或司法辖区；减少 vendors 也会提高 concentration risk、平台锁定和共享故障域，本来源没有系统比较这些反作用。

## 前提与局限性

- 集成之墙不是单纯技术问题。许多阻力来自组织目标不清、权限不明、流程未建模和用户不采纳。
- FDE 可以穿墙，但不能替代客户组织自身能力建设；如果每次都依赖外部 FDE，产生的是依赖而非能力。
- 开源框架可以把更多控制权交给本地机构，但也把集成、评测、维护和值班责任交给本地机构；开放代码只改变穿墙方式，不会让墙消失。
- 集成之墙会随平台成熟而部分降低，但不会完全消失，因为企业环境、监管和组织政治本身持续变化。
- 对受监管行业来说，集成之墙还包括评测集归属、推理位置、数据驻留、跨境传输和供应商能否把现场知识复用于同业客户。

## 关联概念

- [[Forward-Deployed-Engineer]] — 穿越集成之墙的关键角色
- [[AI-Ready-Organization]] — 组织越不清晰，集成之墙越厚
- [[Machine-Readable-Processes]] — 将流程变成 Agent 可执行结构，是降低集成摩擦的路径
- [[Deployment-Product-Flywheel]] — 对集成问题的抽象回流能让下一次部署更容易
- [[Hardware-Sovereignty]] — 临床、金融等场景中，本地部署和数据主权是集成之墙的一部分
- [[Evaluation-Set]] — 集成约束必须进入评测集，才能被系统性验证
- [[Layered-AI-Sourcing]] — 根据集成厚度和数据敏感度决定本地化、FDE 或 cloud API
- [[Open-Source-Operational-AI-Framework]] — 通过开放训练管线、文档和适配接口，让本地机构穿越集成之墙
- [[Alert-Closed-Loop]] — 穿墙穿的不是模型接口，而是告警通知、责任人接收与复盘节点的嵌入
