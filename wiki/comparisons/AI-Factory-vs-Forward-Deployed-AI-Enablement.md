---
type: comparison
title: "AI Factory vs Forward Deployed AI Enablement"
entity_a: "[[AI-Factory]]"
entity_b: "[[Forward-Deployed-AI-Enablement]]"
created: 2026-05-24
updated: 2026-05-24
tags:
  - comparison
  - AI-deployment
  - organization
related_entities:
  - "[[AI-Factory]]"
  - "[[Forward-Deployed-Engineer]]"
  - "[[Deployment-Product-Flywheel]]"
  - "[[Integration-Wall]]"
  - "[[Golden-Case]]"
  - "[[Business-Embedded-AI-Organization]]"
  - "[[Organization-as-Agent-Harness]]"
source_raw:
  - "[[How Procter & Gamble Uses AI to Unlock New Insights From Data  Thomas H. Davenport and Randy Bean]]"
  - "[[Inside PG AI Factory and the Push to Operationalize AI at Scale]]"
  - "[[Building an AI Factory at Procter & Gamble - Case - Faculty & Research - Harvard Business School]]"
  - "[[Forward deployed engineering at OpenAI]]"
  - "[[The Return of the Deployment Company]]"
  - "[[当我们谈论 FDE 时，我们在谈论什么？]]"
---

# AI Factory vs Forward Deployed AI Enablement

> [!summary] 对比概述
> AI Factory 是把 AI 生产能力平台化、标准化、可运维化的内部能力层；Forward Deployed AI Enablement 是进入真实业务现场，发现黄金用例、穿越集成之墙，并把一次性部署回流为平台或组织能力的现场机制。前者解决“如何规模化生产”，后者解决“如何找到并接入真实工作”。

## 核心维度对比

| 维度 | AI Factory | Forward Deployed AI Enablement |
|------|------------|--------------------------------|
| 核心问题 | 如何规模化构建、测试、部署和监控 AI 能力 | 如何把 AI 接进真实组织流程并产生可度量结果 |
| 主要场域 | 企业内部平台、数据、模型、工具和运维体系 | 客户现场或业务现场 |
| 价值起点 | 重复用例足够多，需要统一生产系统 | 真实流程复杂，demo 无法自然进入生产 |
| 关键产物 | 平台能力、数据接入、模型运维、治理标准、agent 注册和监控 | 问题地图、约束清单、原型、评测集、流程模板、部署 playbook |
| 组织角色 | 平台团队 + 业务嵌入团队 | FDE、业务 owner、产品、研究、安全、GTM 或内部赋能团队 |
| 主要风险 | 过早平台化、脱离业务、变成技术中台自转 | 退化为咨询、外包或供应商锁定 |
| 复利机制 | 用例经验沉淀为平台标准，后续部署更快 | 现场方案回流为产品能力或组织能力，下一次赋能更省力 |

## 本质区别

AI Factory 是**生产系统**。它把数据源、模型、工具、安全协议、监控和运维能力打包成可重复使用的企业级 AI 生产线。P&G 案例中的核心信号是：当企业已经有足够多 AI 用例时，单个项目式交付会拖慢规模化，必须建设统一能力层。

Forward Deployed AI Enablement 是**发现与接入系统**。它面对的是另一类问题：企业往往不知道真正高价值的 AI 用例在哪里，即使知道，也会被遗留系统、权限、合规、工作流和组织采纳卡住。FDE 式赋能通过嵌入现场，把模糊需求变成可运行系统，再抽象出可复用能力。

简单说：

- AI Factory 关注“能力如何被稳定生产”。
- FDE 式赋能关注“能力如何进入真实工作”。

## 互补关系

两者真正有效时会形成闭环。

```text
业务现场发现黄金用例
  -> FDE 构建可运行方案
  -> 真实工作流验证
  -> 抽象为平台能力、评测集或模板
  -> AI Factory 标准化生产和运维
  -> 下一次现场部署更快
```

没有 FDE 式现场机制，AI Factory 容易不知道该生产什么，或者生产出业务不采纳的通用能力。

没有 AI Factory，FDE 容易停留在一次性项目，每次都从零处理接入、权限、监控、评测和运维。

## 何时优先建设 AI Factory

优先建设 AI Factory，当：

- 企业已经有大量 AI 用例，且重复建设、重复接入、重复监控成本很高。
- 数据、模型、权限、安全和部署流程需要统一治理。
- 多个业务单元都需要类似的 AI 能力，但缺少标准生产系统。
- 组织已经有稳定的业务 owner 和平台团队，可以共同维护能力层。

P&G 的 AI Factory 更接近这一类：它不是从单个 demo 开始，而是在算法复杂度和规模化部署延迟已经造成明显业务影响后，把 AI 开发、测试、部署和监控纳入平台化体系。

## 何时优先采用 FDE 式赋能

优先采用 FDE 式赋能，当：

- 企业还不清楚哪些工作流最值得 AI 改写。
- 现有 AI 尝试停留在培训、试点或工具试用，缺少生产采用。
- 核心阻力来自 [[Integration-Wall|集成之墙]]：遗留系统、权限、审计、合规、数据驻留和组织采纳。
- 需要把一线隐性知识转成评测集、流程规范、模板或内部 playbook。

此时先建重平台可能过早。更好的路径是先通过现场工作发现 [[Golden-Case|黄金用例]]，再决定哪些能力值得平台化。

## 共同的成败标准

两者最终都要回答同一个问题：第 10 次是否比第 1 次更省力、更清晰、更可复用？

| 成败标准 | AI Factory 视角 | FDE 式赋能视角 |
|----------|----------------|----------------|
| 复用率 | 平台组件是否被多个业务持续使用 | 现场经验是否回流成模板、评测集和 playbook |
| 结果度量 | 算法是否在生产中被监控并产生业务结果 | 工作流是否被真实改变，而非只完成试点 |
| 组织学习 | 平台团队是否吸收业务需求并更新能力层 | 业务团队是否获得自主迭代能力 |
| 集成成本 | 标准接口是否降低后续部署摩擦 | 每次穿越集成之墙后是否留下可复用路径 |
| 治理边界 | 安全、权限、监控是否标准化 | 客户或业务侧是否保有评测集和流程知识主权 |

## 反模式

### 没有用例密度就建设 AI Factory

如果组织还没有足够多高价值用例，AI Factory 会变成技术团队自转：平台很完整，但业务不知道如何使用，也没有足够真实反馈推动演化。

### 没有平台回流就声称 FDE

如果 FDE 每次只是驻场解决一次性问题，没有把经验回流为产品、模板、评测、数据接入规范或组织记忆，它更接近咨询或外包，不是 FDE 式赋能。

### 把集成之墙误认为工程细节

AI Factory 和 FDE 都可能低估集成之墙。真实难点不只是 API，也包括权限、审计、数据边界、员工习惯、部门政治和治理权重新分配。

### 忽略买方知识主权

FDE 的现场经验回流对供应商是飞轮，对客户也可能是锁定。评测集、提示配置、流程规则和边界案例必须明确归属、导出和退出机制。

## 选择指南

选择 AI Factory，当你要解决的是：

- 多业务重复交付。
- 统一安全、监控、部署和治理。
- 把 AI 能力变成企业内部生产系统。
- 降低规模化运维成本。

选择 FDE 式赋能，当你要解决的是：

- 找不到真正高价值工作流。
- demo 进不了生产。
- 组织流程和权限阻力比模型能力更大。
- 需要把现场知识显式化为可迁移资产。

成熟路径通常不是二选一，而是先用 FDE 式赋能找到和验证黄金用例，再把高复用部分纳入 AI Factory。

## 相关概念

- [[AI-Factory]] — 企业 AI 平台化生产能力层。
- [[Forward-Deployed-Engineer]] — 执行现场发现、构建和回流的角色。
- [[Deployment-Product-Flywheel]] — 两种模式共享的复利机制。
- [[Integration-Wall]] — AI 从 demo 到生产的主要阻力。
- [[Golden-Case]] — 现场发现后值得平台化和推广的高价值用例。
- [[Business-Embedded-AI-Organization]] — AI Factory 需要与业务嵌入结构配套。
- [[Organization-as-Agent-Harness]] — 两者共同指向的组织能力形态。
