---
type: entity
title: NLAH
aliases:
  - NLAH
  - Natural-Language Agent Harnesses
  - 自然语言智能体驾驭层
definition: "将 Agent 驾驭策略从代码中外置为可执行的自然语言文档，由智能驾驭运行时（IHR）解释执行，使驾驭模式可检视、可移植、可消融"
created: 2026-06-13
updated: 2026-06-13
tags:
  - agent-harness
  - research
related_entities:
  - "[[Agent-Harness]]"
  - "[[Harness-Engineering]]"
  - "[[Context-Rot]]"
  - "[[Multi-Layer-Memory]]"
  - "[[Thin-Harness-Fat-Skills]]"
source_raw:
  - "[[20260613-NLAH-natural-language-agent-harnesses]]"
---

# NLAH（Natural-Language Agent Harnesses）

> [!definition] 定义
> 将 Agent 驾驭策略从代码中外置为可执行的自然语言文档，由智能驾驭运行时（IHR）解释执行，使驾驭模式可检视、可移植、可消融。

## 关键数据点

- **核心论文**: 《Natural-Language Agent Harnesses》，提出 NLAH + IHR 双层架构
- **性能等效**: 在 SWE-bench Verified、Terminal-Bench 2.0、OSWorld 三类基准上，IHR 执行的 NLAH 取得与代码驾驭层相当的成绩
- **策略压缩**: Live-SWE 从 6.01 万 token 代码降到 2.9k token 的 NLAH（压缩约 20 倍）；MHTBA 从 1.05 万降到 0.8k
- **代价**: 当前原型运行时的 token/调用开销更高
- **消融发现**: 文件持久化状态是最稳正贡献（Δ 约 +2.6/+13.9）；多候选搜索和上下文压缩反而有害；自我进化模块提升性能但 token 消耗大幅上升

## 四层架构

| 层 | 职责 | 比喻 |
|---|------|------|
| 基础智能体 | 最小 agent 循环（LLM + 终端工具），不含任务逻辑 | 马 |
| 运行时策略（IHR） | 固定 NL 指令，读取 NLAH 文档、调度子 agent、管理状态 | 骑手 |
| NLAH 文档 | 可替换的自然语言驾驭策略（阶段、角色、状态、验收、恢复、停止） | 路线图 |
| 脚本与适配器 | 确定性硬逻辑（JSON schema 校验、diff 计算、格式转换） | 信号灯 |

## 三种驾驭方式谱系

从控制强到弱：
1. **代码驾驭层（Code Harness）**: 程序逻辑硬性控制，最强确定性但策略与实现交织
2. **NLAH + IHR**: 自然语言承载策略 + 运行时解释执行，放弃硬确定性但获得可编辑性和可消融性
3. **自驾驭（Self-Harnessing）**: 控制器模型直接驾驭其他模型，无外部驾驭层

## 前提与局限性

- **前提**: NLAH 假设驾驭策略可以被自然语言充分精确地表达，且 LLM 能忠实遵循
- **机制遵循不均**: 契约式、可即时验证的机制遵循度高；跨阶段、跨子 agent 协调的机制遵循度低
- **自然语言不精确性**: 语义约束可能被欠定义、被不同模型不同解读
- **安全风险**: 可移植的驾驭逻辑可能降低传播危险工作流的门槛；驾驭层中介工具使用，可能引入提示注入和供应链污染攻击面

## 关联概念

- [[Agent-Harness]] — NLAH 是 Harness 的一种新范式表达
- [[Harness-Engineering]] — NLAH 使 Harness 工程从代码层上升到策略层
- [[Context-Rot]] — 消融实验发现上下文压缩反而有害，与 Context Rot 研究方向一致
- [[Thin-Harness-Fat-Skills]] — NLAH 四层架构的关注点分离与此设计哲学相似
