---
type: entity
title: Human Signal
aliases:
  - Human Signal
  - 人类信号
  - 人类方向信号
definition: "在多 Agent 高吞吐工作系统中，人类持续提供方向、品味、优先级、风险判断和反应-重定向反馈，而把主要执行交给 Agent 的分工角色"
created: 2026-06-04
updated: 2026-06-04
tags:
  - human-AI-collaboration
  - agentic-engineering
  - judgment
related_entities:
  - "[[Human-Governor-Agent-Operator]]"
  - "[[Judgment]]"
  - "[[Taste]]"
  - "[[Ownership]]"
  - "[[Plan-as-Agent-Checkpoint]]"
  - "[[Zero-Friction-Scope-Creep]]"
source_raw:
  - "[[Every Agentic Engineering Hack I Know (June 2026)]]"
---

# Human Signal（人类信号）

> [!definition] 定义
> **Human Signal** 是高吞吐 Agent 工作系统中的人类角色：不再亲手完成大部分执行，而是持续提供方向、品味、优先级、风险判断和反应-重定向反馈，使 Agent 产量收敛为有价值结果。

## 为什么会成为瓶颈

当多个 Agent 可以并行规划、构建、研究和修复时，执行供给迅速增加。新的稀缺资源变成：

- 哪件事值得做。
- 哪个方案更接近目标。
- 哪个风险必须先处理。
- 什么证据足以证明完成。
- 什么时候应停止、转向或拒绝。

可以把关系压缩为：

```text
有用结果 = Agent 执行量 x Human Signal 质量
```

执行量很高但信号弱，会产生更多无关功能、审查债务和 [[Zero-Friction-Scope-Creep|零摩擦范围蔓延]]。

## 信号如何进入系统

| 信号 | 典型动作 | 主要载体 |
|------|----------|----------|
| 方向 | 选择目标、约束范围、定义成功 | [[Plan-as-Agent-Checkpoint]] |
| 品味 | 比较方案、拒绝通用输出、调整表达 | [[Taste]] |
| 判断 | 处理不确定性、风险和例外 | [[Judgment]] |
| 反馈 | 对中间结果反应并重定向 | 评论、review、对话 |
| 责任 | 决定是否发布、合并或承担后果 | [[Ownership]] |

## 与 Human Governor 的关系

[[Human-Governor-Agent-Operator]] 描述组织级分工：人类设定目标和政策，Agent 运营流程。

Human Signal 描述更高频、更贴近工作台的交互：人在多个执行循环之间持续比较、纠偏和终止。前者强调治理结构，后者强调信号带宽和质量。

两者共同说明，人类退出执行层不等于退出系统。人的工作从“完成动作”迁移到“塑造动作空间并承担后果”。

## 关键数据点

- Matt Van Horn 同时运行四到六个 Agent 会话，让不同会话分别规划、构建、研究和修复。
- 作者将人的角色定义为 Human Signal：Agent 提供产量，人提供品味、方向和反应-重定向循环。
- 文章本身由语音输入、Agent 改写和 Proof 协作审阅完成，是该分工模式的自证案例。
- 作者同时承认高吞吐构建循环会带来沉迷、忽略用户和关系的风险，说明 Human Signal 也必须包含停止信号。

## 前提与局限性

- Human Signal 需要真实领域知识和结果反馈；没有用户、运行数据或业务指标时，所谓品味可能只是个人偏好。
- 多会话并行会提高信号负荷。人类无法有效审查时，增加 Agent 数量只会放大噪声。
- 只做方向判断、不理解约束和执行代价，会让 Human Signal 退化为随意指挥。
- 人类仍需承担关键验证和责任，不能用“我只提供信号”逃避审查。
- 信号本身会有偏差，需要通过评测、反例、用户反馈和复盘持续校正。

## 关联概念

- [[Human-Governor-Agent-Operator]] — 组织尺度的人类治理与 Agent 运营分工
- [[Judgment]] — 在不确定性中做取舍的核心能力
- [[Taste]] — 判断什么值得保留、什么过于通用
- [[Ownership]] — 为最终发布和后果负责
- [[Plan-as-Agent-Checkpoint]] — 将方向和验收信号持久化
- [[Zero-Friction-Scope-Creep]] — 信号不足时高吞吐系统的典型失败
