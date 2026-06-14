---
type: entity
title: Plan as Agent Checkpoint
aliases:
  - Plan as Agent Checkpoint
  - 计划即 Agent 检查点
  - Agent 可读计划
  - plan.md
definition: "用结构化计划文件把目标、上下文、方案、目标文件和验收标准外化为可跨会话恢复、可供 Agent 执行和人类审查的持久检查点"
created: 2026-06-04
updated: 2026-06-04
tags:
  - agentic-engineering
  - context-engineering
related_entities:
  - "[[Agentic-Engineering]]"
  - "[[Compound-Engineering]]"
  - "[[Human-Signal]]"
  - "[[Context-Engineering]]"
  - "[[Machine-Readable-Processes]]"
  - "[[Verifiability]]"
source_raw:
  - "[[Every Agentic Engineering Hack I Know (June 2026)]]"
---

# Plan as Agent Checkpoint（计划即 Agent 检查点）

> [!definition] 定义
> **Plan as Agent Checkpoint** 是把任务思考和执行状态写入结构化计划文件，使 Agent 能在上下文耗尽、会话切换、模型切换或人机交接后继续工作。计划不是一次性说明，而是可恢复、可审查、可执行的任务状态。

## 核心机制

```text
模糊输入
  -> 并行读取代码库、历史经验和外部资料
  -> 形成结构化计划
  -> Agent 按计划执行
  -> 用验收标准验证
  -> 将新经验沉淀回计划、规则或 Skill
```

一个有效的 Agent 计划至少应包含：

| 组成 | 作用 |
|------|------|
| 问题与目标 | 防止 Agent 只解决表面请求 |
| 代码库或工作环境模式 | 让方案服从本地约定，而不是生成通用建议 |
| 实施路径与目标文件 | 限定执行范围，降低无关修改 |
| 验收标准 | 把“完成”转成可验证条件 |
| 风险与边界 | 提前暴露需要人类判断的部分 |
| 状态与下一步 | 支持跨会话恢复和交接 |

## 为什么是检查点

LLM 上下文是易失的。长任务中，Agent 会遗忘早期判断、重新探索已知信息，或在会话切换后失去执行方向。

计划文件把易失上下文变成持久状态：

- 新会话可以直接读取计划继续工作。
- 不同模型可以围绕同一目标分工。
- 人类可以只审查目标、风险和验收标准，不必跟踪每个执行步骤。
- 团队成员可以对计划评论，再把反馈送回 Agent 循环。

这使计划同时连接 [[Context-Engineering|上下文工程]]、[[Machine-Readable-Processes|机器可读流程]] 和 [[Verifiability|可验证性]]。

## 与普通计划文档的区别

普通计划主要用于沟通意图；Agent 检查点还必须能驱动执行和恢复。

| 维度 | 普通计划文档 | Agent 检查点 |
|------|--------------|--------------|
| 主要读者 | 人类 | Agent + 人类 |
| 粒度 | 方向和里程碑 | 方向、文件、约束、验收和状态 |
| 生命周期 | 启动时撰写，执行中可能失效 | 执行中持续校正 |
| 核心价值 | 对齐认知 | 对齐认知 + 恢复执行 |

## 关键数据点

- Matt Van Horn 的规则是：除非变更只有一行，否则先生成 `plan.md`。
- 他的规划流程会并行读取代码库模式、过去方案和必要的外部资料，再合并为目标文件、实施路径和验收清单。
- 作者明确把计划作为上下文耗尽后的恢复点：新会话读取计划后可以继续执行。
- 计划也可以成为团队协作接口；作者使用 Proof 让非终端同事阅读、评论计划，再把反馈送回 Agent 循环。

## 前提与局限性

- 计划只能外化已识别的问题；错误假设被写进计划后，也会被 Agent 更稳定地执行。
- “有计划”不等于“计划正确”。人类仍需审查目标、风险、权限和验收标准。
- 开放探索、研究发现和创意任务可能无法提前列出完整实施路径，计划应允许更新，而不是变成僵硬脚本。
- 计划过长或过细会增加维护成本，使 Agent 把更新文档当成工作本身。
- 计划不能替代测试、运行证据、代码审查和责任承担。

## 关联概念

- [[Agentic-Engineering]] — 计划让 Agent 生成进入可验证工程流程
- [[Compound-Engineering]] — 计划中的有效模式可沉淀为规则和 Skill
- [[Human-Signal]] — 人类通过计划输入方向、风险和验收信号
- [[Context-Engineering]] — 计划是高密度、持久化上下文
- [[Machine-Readable-Processes]] — 计划把任务流程变成 Agent 可执行结构
- [[Verifiability]] — 验收标准决定计划能否闭环
