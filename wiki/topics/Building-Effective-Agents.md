---
type: topic
title: Building Effective Agents
description: "Anthropic 的 Agent 构建指南：从简单模式到自主 Agent 的架构设计"
created: 2026-04-10
updated: 2026-05-23
tags:
  - AI-Agent
  - architecture
  - best-practices
related_entities:
  - '[[ACI-Agent-Computer-Interface]]'
  - '[[Agent-Workflow-Patterns]]'
  - '[[Agent-Harness]]'
  - '[[Barry-Zhang]]'
  - '[[Coding-Agents]]'
  - '[[Erik-Schluntz]]'
  - '[[MIT-Technology-Review-Insights]]'
  - "[[Verifiability]]"
  - "[[Bias-to-Action-LLM]]"
source_raw:
  - '[[building-effective-agents]]'
  - '[[The Anatomy of an Agent Harness]]'
  - '[[Validating agentic behavior when “correct” isn’t deterministic]]'
---

# Building Effective Agents

> **来源**：Anthropic, "Building Effective AI Agents" (2024-12-19)
> **作者**：Erik Schluntz, Barry Zhang

## 核心原则

> [!important] 关键洞察
> 成功的 Agent 系统通常不是最复杂的框架，而是最小可行的可观察循环：任务能被拆分，工具接口清楚，错误能反馈，结果能验证。

### 三大原则

1. **Simplicity** - 保持设计简单
2. **Transparency** - 明确展示规划步骤
3. **Well-crafted ACI** - 精心设计 Agent-Computer Interface

---

## 架构定义

### Workflows vs Agents

| 类型 | 定义 |
|------|------|
| **Workflows** | LLM 和工具通过预定义代码路径编排 |
| **Agents** | LLM 动态指导自己的过程和工具使用 |

选择的第一原则不是“哪个更先进”，而是任务的不确定性在哪里。可预测任务优先 workflow；开放任务才需要 agent。把可预测任务交给自主 agent，通常只是把可控复杂性变成不可控复杂性。

---

## 何时使用 Agent

### 不需要 Agent

- 单次 LLM 调用 + 检索 + 示例足够
- 可预测的任务
- 对延迟/成本敏感

### 需要 Workflow

- 任务可清晰分解
- 需要一致性和可预测性
- 有明确的评估标准

### 需要 Agent

- 开放性问题
- 无法预测步数
- 需要灵活决策

## 从模式到 Harness

Anthropic 文章给的是模式层，[[Agent-Harness|Agent Harness]]补上运行时层。一个生产 Agent 至少需要把五件事显式化：

| 层 | 问题 | 典型机制 |
|----|------|----------|
| 编排 | 什么时候调用模型和工具 | ReAct / TAO loop |
| 工具 | Agent 能做什么 | schema、沙箱、权限 |
| 上下文 | Agent 看到什么 | 检索、压缩、懒加载 |
| 状态 | 过程如何保存 | checkpoint、日志、git |
| 验证 | 什么时候相信输出 | 测试、规则、评审、拒绝 |

这说明“简单”不是没有结构，而是只保留能提高成功概率或降低风险的结构。

---

## Workflow Patterns 详解

### 1. Prompt Chaining

**适用**：任务可分解为固定子任务

```
步骤1 → 步骤2 → 步骤3 → 输出
```

### 2. Routing

**适用**：不同类别需要不同处理

```
分类 → 路由到专门处理流程
```

### 3. Parallelization

**适用**：速度优化、多视角验证

```
并行执行 → 聚合结果
```

### 4. Orchestrator-Workers

**适用**：动态子任务分解

```
Orchestrator 分解 → Workers 执行 → 合成结果
```

### 5. Evaluator-Optimizer

**适用**：迭代改进有价值

```
生成 → 评估 → 反馈 → 改进 → 循环
```

Evaluator-Optimizer 是最接近生产价值的模式，因为它把模型输出放进反馈回路。但反馈必须具体可执行：测试失败、schema 不合格、截图不符合、引用缺失，都比“再好一点”更适合 Agent 消费。

---

## ACI 设计

### 核心类比

> 在 HCI 上投入多少努力，就在 ACI 上投入多少。

### 设计检查清单

1. **模型视角** - 使用方式是否明显？
2. **命名清晰** - 参数名是否让事情更明显？
3. **测试迭代** - 在 workbench 测试错误模式
4. **Poka-yoke** - 防错设计

### 格式选择

| 格式 | Agent 难度 |
|------|-----------|
| Markdown 代码块 | 低 |
| 整个文件重写 | 低 |
| Diff 格式 | 高（需计算行号） |
| JSON 内嵌代码 | 高（需转义） |

---

## 框架使用建议

### 推荐框架

- Claude Agent SDK
- Strands Agents SDK (AWS)
- Rivet (GUI workflow builder)
- Vellum (GUI workflow tool)

### 注意事项

> [!warning] 框架陷阱
> 框架增加抽象层，可能掩盖底层 prompt/response。
> 
> **建议**：
> 1. 先用 LLM API 直接实现简单模式
> 2. 使用框架时理解底层代码
> 3. 不要因框架添加不必要复杂性

## 反模式：把 Agent 当万能脑

本主题与 [[Verifiable-Agent-Engineering]] 的交集在于：不要把确定性工作交给 LLM。解析文件、读取 diff、权限判断、格式校验、成本记录，这些都应尽量由代码或规则完成。LLM 的价值在于模糊分解、语义判断和异常处理，不在于替代一切控制流。

同时要防 [[Bias-to-Action-LLM|行动偏差]]。生产 Agent 不只是会做事，也要会在信息不足、高风险或不可验证时停止。

---

## Agent 应用场景

### 客户支持

- 自然对话 + 工具集成
- 成功可清晰衡量
- 人类监督机制

### 编码 Agent

- 代码可通过测试验证
- Agent 可用测试结果迭代
- 问题空间结构化

---

## 相关主题

- [[Agent-Workflow-Patterns]] - 详细模式说明
- [[Agentic-Engineering-Patterns]] - Simon Willison 的工程视角
- [[ACI-Agent-Computer-Interface]] - 接口设计详解
- [[Verifiable-Agent-Engineering]] - 验证边界与拒绝机制
- [[Agent-Harness]] - 生产级 Agent 运行时结构

## 参见

- [[Barry-Zhang]] - Building Effective Agents 合著者
- [[Erik-Schluntz]] - Building Effective Agents 合著者
- [[MIT-Technology-Review-Insights]] - Agent 报告研究部门

---

## 结论

构建有效 Agent 的第一性原理是先缩小问题，再扩大自主性。

如果一个任务能用 workflow 稳定完成，就不要把它交给 agent；如果必须使用 agent，就给它清楚工具、可观察状态和可验证反馈。
