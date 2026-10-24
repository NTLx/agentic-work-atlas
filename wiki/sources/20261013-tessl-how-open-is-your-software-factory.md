---
type: source-summary
title: "How Open Is Your Software Factory?"
canonical_url: "https://tessl.io/blog/how-open-is-your-software-factory"
original_raw_file: "20261013-tessl-how-open-is-your-software-factory.md"
body_sha256: "76bd1d9a8f73acd248746685c9acb94f27bdcfbf81220aaab89d127ef2d04e95"
indexed_at: "2026-10-24T23:52:29+08:00"
raw_state: index
created: 2026-10-24
updated: 2026-10-24
tags:
  - source-summary
  - knowledge-management
evidence_level: low
claim_type: mixed
---

# How Open Is Your Software Factory?

## 编译摘要

### 1. 浓缩
- **软件工厂会积累超出代码本身的组织知识**：架构决策、审查反馈、事故揭示的隐含约束和评测案例会在反复运行中形成；若这些知识只能留在单一平台，代码可迁移而组织理解仍被锁定（“The valuable output is more than code”）。
- **开放性需要以知识可迁移和可再用衡量**：多模型、外部 Agent、客户控制部署或开放接口各自有用，却不能单独证明生产中积累的 context/learning 可被检查、治理、导出并在其他 harness 中重新使用（“Open components are a starting point”; “Make openness observable”）。
- **纠错应被编译成可维护资产**：一次 Agent 绕过内部服务的错误可转化为有范围和理由的 architecture decision、skill、evaluation case 和自动检查；导出 transcript 不足以证明 lesson 的适用范围、权威性和可验证性（“Take your learning forward”）。
- **建议用一个工作流演练迁移**：选重复发生的有界任务，连接权威来源，沉淀少量 skills/evals，再在另一 Agent、harness 或团队中复用，检查适配成本和隐性依赖（“Start with one workflow—and rehearse the move”）。

### 2. 质疑
- **文章带有厂商定位**：作者销售 Tessl 软件工厂产品，开放性框架也服务于其产品叙事；论点可作为评估清单，不能作为其产品已经满足标准的证据。
- **“可导出”不等于可移植**：不同 Agent 的权限、记忆、工具语义和执行循环可能不同；文章承认适配和重测仍必要。真正的迁移性必须在目标环境实际跑通并通过 eval。
- **知识资产治理有持续成本**：skills、context、评测和集成会过时，且需要 owner；对商品化工作流，托管产品可能更经济。
- **保留知识需权限与范围治理**：跨团队共享可减少孤岛，但不意味着所有用户或 Agent 都应访问敏感上下文；临时 workaround 也不应未经判断晋升为政策。

### 3. 对标
- **与 Agent-Knowledge-Management 的关系**：把“记忆”从历史记录转成有来源、范围、状态、权限和验收条件的维护资产；可迁移性是复用质量的外部检验。
- **与 Enterprise AI Factory 的关系**：强调每次部署是否留下可复用 context、workflow、eval 和 owner，而非平台本身规模或部署位置；适合从轻量工作流验证开始。

### 证据定位
- “The valuable output is more than code”：代码所有权和 know-how 锁定的区分。
- “Take your learning forward”：错误经验转为 ADR、skill、eval、自动检查的示例。
- “Make openness observable”：透明度、可复现性、互操作性和生态复用四项观察标准。
- “Start with one workflow—and rehearse the move”：跨 Agent/harness 的迁移演练。

### 关联概念
- [[Agent-Knowledge-Management]]
- [[Enterprise-AI-Factory]]
