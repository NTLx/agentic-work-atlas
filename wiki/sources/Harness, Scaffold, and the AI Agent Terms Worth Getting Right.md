---
type: source-summary
title: "Harness, Scaffold, and the AI Agent Terms Worth Getting Right"
source_raw:
  - "[[Harness, Scaffold, and the AI Agent Terms Worth Getting Right]]"
created: 2026-05-27
updated: 2026-05-27
tags:
  - source-summary
  - AI-Agent
  - architecture
---

# Harness, Scaffold, and the AI Agent Terms Worth Getting Right

## 编译摘要

### 1. 浓缩

- **核心结论1**: Agent 术语体系尚未收敛——Harness 和 Scaffold 在不同语境下含义不同，需要区分"广义"和"细粒度"两种用法
  - 关键证据: ICLR 2026 后 Arnav Gupta 发帖称"听了太多 harness/scaffold 解释但无法收敛到单一定义"；HuggingFace 撰写本文作为术语锚定
- **核心结论2**: Scaffold 是行为定义层，Harness 是执行层——区分在训练管线中尤为重要
  - 关键证据: Scaffold = 系统提示 + 工具描述 + 解析 + 上下文管理；Harness = 调用模型 + 处理工具调用 + 决定何时停止。Claude Code 官方文档自称"harness"（广义用法）
- **核心结论3**: 同一底层模型 + 不同 Harness = 完全不同的产品体验——Model、Harness、Product 是三件不同的事
  - 关键证据: Cursor 博客"Continually improving our agent harness"展示了 harness 作为产品迭代的独立性

### 2. 质疑

- **关于术语收敛的假设**: 文章目标是"锚定术语"，但领域演化速度可能快于术语标准化——Agent 定义已从 RL 函数扩展到 LLM 全系统
- **关于训练与推理对称性**: 文章声称 Scaffold/Harness 区分在训练管线中尤为重要，但大部分内容聚焦推理侧，训练侧的具体差异未充分展开
- **关于 Policy 概念的引入**: Policy 作为 RL 术语被引入 Agent 讨论，但 LLM Agent 的 Policy 部分由权重学习、部分由 harness 定义——这种混合性质是否使术语更清晰而非更混乱？

### 3. 对标

- **跨域关联1**: 类似编程语言的语法/语义/运行时三层分离——Scaffold 类似语法（定义表达形式），Harness 类似运行时（执行并管理生命周期）
- **跨域关联2**: 与 Anthropic 的 [[Agent-Harness]] 定义形成互补——Anthropic 聚焦组件和功能，HuggingFace 聚焦术语标准化和训练/推理对称性
- **跨域关联3**: Skills vs Tools vs Sub-agents 的区分类似微服务架构中 API（工具）、SDK（技能）、独立服务（子 Agent）的区别

### 关联概念

- [[Agent-Harness]]
- [[Harness-Engineering]]
- [[Context-Engineering]]
- [[Agent-Orchestration]]
