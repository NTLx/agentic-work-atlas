---
type: entity
title: Integration Wall
aliases:
  - Integration Wall
  - 集成之墙
  - AI 集成之墙
definition: "AI 项目从 demo 到生产落地时遇到的遗留系统、权限、SSO、数据驻留、合规、流程改造和组织采纳约束"
created: 2026-05-22
updated: 2026-05-22
tags:
  - AI-deployment
  - enterprise
  - systems-integration
related_entities:
  - "[[Forward-Deployed-Engineer]]"
  - "[[AI-Ready-Organization]]"
  - "[[Machine-Readable-Processes]]"
  - "[[Deployment-Product-Flywheel]]"
  - "[[Hardware-Sovereignty]]"
source_raw:
  - "[[当我们谈论 FDE 时，我们在谈论什么？]]"
  - "[[Forward Deployed Engineer：AI 时代的新宠岗位，到底干什么？]]"
---

# Integration Wall（集成之墙）

> [!definition] 定义
> **Integration Wall（集成之墙）** 是 AI 项目从演示进入生产时遇到的真实企业约束：遗留系统、权限模型、SSO、数据驻留、合规、业务流程、人际协作和组织采纳。FDE 的大量价值就在于穿越这堵墙。

## 关键数据点

- yan5xu 文章指出，许多 AI 项目失败不是因为模型不够强，而是因为无法接入客户的遗留系统、认证、数据驻留和工作流。
- 文章将沙盒 demo 与企业现实区分开：让 demo 跑起来只是一小部分工作，大量工作发生在生产环境约束中。
- 宝玉文章也强调，FDE 的核心不是写模型，而是把模型真正接进企业业务：调接口、现场 debug、处理客户环境中的复杂要求。
- OpenAI、Anthropic 和 Google 对 FDE 的投入，反映了 AI 行业从“模型竞赛”转向“落地竞赛”的结构性变化。

## 前提与局限性

- 集成之墙不是单纯技术问题。许多阻力来自组织目标不清、权限不明、流程未建模和用户不采纳。
- FDE 可以穿墙，但不能替代客户组织自身能力建设；如果每次都依赖外部 FDE，产生的是依赖而非能力。
- 集成之墙会随平台成熟而部分降低，但不会完全消失，因为企业环境、监管和组织政治本身持续变化。

## 关联概念

- [[Forward-Deployed-Engineer]] — 穿越集成之墙的关键角色
- [[AI-Ready-Organization]] — 组织越不清晰，集成之墙越厚
- [[Machine-Readable-Processes]] — 将流程变成 Agent 可执行结构，是降低集成摩擦的路径
- [[Deployment-Product-Flywheel]] — 对集成问题的抽象回流能让下一次部署更容易
- [[Hardware-Sovereignty]] — 临床、金融等场景中，本地部署和数据主权是集成之墙的一部分
