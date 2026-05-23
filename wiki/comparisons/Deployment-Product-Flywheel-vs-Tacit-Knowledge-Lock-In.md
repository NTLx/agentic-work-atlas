---
type: comparison
title: "Deployment-Product Flywheel vs Tacit Knowledge Lock-In"
entity_a: "[[Deployment-Product-Flywheel]]"
entity_b: "[[Tacit-Knowledge-Lock-In]]"
created: 2026-05-24
updated: 2026-05-24
tags:
  - comparison
  - AI-deployment
  - FDE
related_entities:
  - "[[Deployment-Product-Flywheel]]"
  - "[[Tacit-Knowledge-Lock-In]]"
  - "[[Forward-Deployed-AI-Enablement]]"
  - "[[Evaluation-Set]]"
  - "[[Layered-AI-Sourcing]]"
  - "[[Integration-Wall]]"
  - "[[Forward-Deployed-Engineer]]"
source_raw:
  - "[[The Return of the Deployment Company]]"
  - "[[Forward deployed engineering at OpenAI]]"
  - "[[当我们谈论 FDE 时，我们在谈论什么？]]"
  - "[[Forward Deployed Engineer：AI 时代的新宠岗位，到底干什么？]]"
---

# Deployment-Product Flywheel vs Tacit Knowledge Lock-In

> [!summary] 对比概述
> Deployment-Product Flywheel 和 Tacit Knowledge Lock-In 描述的是同一类现场部署机制的两面：从供应商视角，客户现场经验回流为平台能力；从客户视角，隐性规则、评测集和流程调优经验若沉淀在供应商侧，就会形成新的迁移成本。

## 核心维度对比

| 维度 | Deployment-Product Flywheel | Tacit Knowledge Lock-In |
|------|-----------------------------|-------------------------|
| 视角 | 供应商、平台团队、FDE 团队 | 客户、买方组织、内部能力建设 |
| 核心问题 | 如何把一次性部署变成可复用产品能力 | 如何避免业务隐性知识被供应商锁住 |
| 关键资产 | 模板、评测集、集成规范、工具链、playbook | 业务规则、边界案例、验收标准、流程习惯 |
| 成功信号 | 第 10 次部署比第 1 次更快、更稳、更标准 | 客户能理解、导出、接管或迁移关键知识资产 |
| 主要风险 | 退化为咨询或外包，无法回流产品 | 替换供应商时要重新学习业务语义和流程 |
| 治理重点 | 抽象、产品化、平台复用 | 归属、可移植性、退出机制、分层 sourcing |

## 本质区别

[[Deployment-Product-Flywheel|部署-产品飞轮]]强调现场经验如何变成复利。FDE 在客户现场解决集成、权限、流程和采用问题后，如果能把方案抽象为产品能力、模板、评测集或部署 playbook，下一次部署成本就会下降。

[[Tacit-Knowledge-Lock-In|隐性知识锁定]]强调同一过程的买方风险。现场部署会暴露大量客户隐性知识：真实业务规则、异常处理、评测样例、员工习惯、审批边界和流程口径。如果这些知识主要留在供应商侧，客户会越来越依赖供应商。

简单说：

- 飞轮是供应商的复利。
- 锁定是客户的代价。

## 同一机制的两面

```text
客户现场部署
  -> 暴露隐性业务规则
  -> 写入提示、评测集、流程配置和集成代码
  -> 供应商抽象为平台能力
  -> 后续部署更快
  -> 客户迁移成本也可能上升
```

这不是说部署-产品飞轮不好，而是说飞轮必须配套知识主权设计。否则供应商越成功，客户越难退出。

## Evaluation Set 是关键分界

[[Evaluation-Set|评测集]]是两者的分水岭。

从飞轮视角看，评测集让供应商把客户现场判断转成可复用测试资产。  
从锁定视角看，评测集也可能承载客户最核心的隐性业务判断。

因此需要明确：

- 评测集由谁拥有？
- 客户能否导出？
- 是否包含敏感业务规则？
- 供应商能否跨客户复用？
- 内部团队能否用它接管系统？

## 反模式

### 只看交付成功，不看知识归属

一个 AI 部署项目短期跑起来，不代表长期健康。若客户不知道系统为什么这样判断，也无法导出评测和配置，项目成功可能同时制造锁定。

### 把所有现场经验都产品化

不是所有客户知识都适合进入供应商平台。有些规则高度敏感、特定、合规相关，应留在客户侧或以明确边界进入分层 sourcing。

### 把锁定误认为护城河

供应商可以从部署飞轮中获得护城河，但如果护城河来自客户无法退出，而不是产品能力持续提高，长期会损害信任和扩散。

## 选择指南

对供应商或 FDE 团队：

- 必须证明现场经验能回流为产品能力，而不只是一次性人力交付。
- 应明确哪些客户知识可泛化，哪些必须留在客户隔离层。
- 应提供客户可理解、可审计、可导出的交付资产。

对客户或买方组织：

- 关键评测集、验收标准和流程规则应保留副本和解释权。
- 高频、高敏感、核心流程能力应逐步内部化。
- 前沿、低频、探索性能力可以借助外部 FDE。
- 退出机制应在部署初期设计，而不是供应商关系恶化后补救。

## 相关概念

- [[Deployment-Product-Flywheel]] — 现场方案回流为平台能力的复利机制。
- [[Tacit-Knowledge-Lock-In]] — 供应商掌握客户隐性规则和流程经验形成的锁定。
- [[Forward-Deployed-AI-Enablement]] — 嵌入真实组织现场的 AI 赋能模式。
- [[Evaluation-Set]] — 把业务判断转成可验证样本的关键资产。
- [[Layered-AI-Sourcing]] — 按敏感度、频率和能力需求分层配置 AI 来源。
- [[Integration-Wall]] — AI 从 demo 进入生产时面对的集成约束。

