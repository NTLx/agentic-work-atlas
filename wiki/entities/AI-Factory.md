---
type: entity
title: AI Factory
aliases:
  - "AI Factory"
  - "AI 工厂"
  - "企业 AI 工厂"
  - "P&G AI Factory"
definition: "企业为规模化构建、测试、部署、监控 AI 算法而建立的平台化能力层，把数据、模型、工具、安全协议和运维标准打包成可复用生产系统"
created: 2026-05-23
updated: 2026-05-23
tags:
  - enterprise-AI
  - AI-deployment
  - platform
related_entities:
  - "[[Business-Embedded-AI-Organization]]"
  - "[[Organization-as-Agent-Harness]]"
  - "[[Integration-Wall]]"
  - "[[Deployment-Product-Flywheel]]"
  - "[[Model-Context-Protocol-MCP]]"
  - "[[Golden-Case]]"
source_raw:
  - "[[How Procter & Gamble Uses AI to Unlock New Insights From Data  Thomas H. Davenport and Randy Bean]]"
  - "[[Inside PG AI Factory and the Push to Operationalize AI at Scale]]"
  - "[[Building an AI Factory at Procter & Gamble - Case - Faculty & Research - Harvard Business School]]"
---

# AI Factory（企业 AI 工厂）

> [!definition] 定义
> **AI Factory** 是企业为规模化构建、测试、部署、监控 AI 算法而建立的平台化能力层。它不是单个模型或工具库，而是把数据源、软件工具、方法、安全协议、生产运维和集成标准合成一个可重复使用的 AI 生产系统。

## 关键数据点

- P&G 从 2021 年左右提出 AI factory，原因是算法复杂度上升、原型到规模化部署的延迟产生了实质财务影响。
- P&G 的 AI factory 提供数据源、软件工具、方法和安全协议，用于快速开发、测试、部署和监控生产算法。
- Jeff Goldman 表示，AI factory 将模型部署时间大约缩短六个月，并且现在已纳入 agentic AI 的监控、agent 注册、Agent2Agent Protocol 与 [[Model-Context-Protocol-MCP|MCP]] 连接能力。
- P&G 的组织分工是两侧并行：一侧持续建设和更新 factory，另一侧负责扩展和运营 factory 内开发出来的算法。
- 典型业务结果包括 Pampers My Perfect Fit 漏尿预防推荐准确率 90%、巴西订单拆分和排车系统让缺货减少 15%、香水开发数字套件让新香型开发速度提高 5 倍。

## 前提与局限性

- AI factory 的前提是企业已经有足够多的 AI 用例和数据资产。若用例稀少，先建设重平台容易过早复杂化。
- 它解决的是规模化生产问题，不自动解决业务问题选择。P&G 通过业务嵌入、业务出资和产品团队合作来防止 factory 变成纯技术项目。
- HBS case 的公开页面只提供元数据和引用信息，不能单独支撑具体运营细节；细节主要来自 MIT SMR 文章和 CDO Magazine 访谈。
- AI factory 降低部署摩擦，但不会消除 [[Integration-Wall|集成之墙]]；遗留系统、权限、合规和组织采纳仍需要业务现场工作。

## 关联概念

- [[Business-Embedded-AI-Organization]] — AI factory 需要与业务嵌入式组织结构配套，否则平台能力无法转成业务结果。
- [[Organization-as-Agent-Harness]] — AI factory 是企业把自己变成 Agent 运行环境的一种具体实现。
- [[Integration-Wall]] — factory 标准化了一部分集成和运维问题，但核心工作流仍要穿越企业现场约束。
- [[Deployment-Product-Flywheel]] — P&G 内部 factory 是企业内部版的部署复利机制：一次用例经验回流为下一次部署能力。
- [[Golden-Case]] — Pampers、巴西供应链和香水研发案例都是 AI factory 找到并规模化的业务用例。
