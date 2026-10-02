---
type: entity
title: Recursive Language Model
aliases:
  - Recursive Language Model
  - RLM
  - Recursive Language Models
definition: "一种把上下文外置为可寻址状态、以代码作为主要控制面，并允许模型程序化调用自身或子 Agent 的 Harness 设计；目标是把全局复杂任务分解为可组合、局部分布内的模型调用。"
created: 2026-10-03
updated: 2026-10-03
evidence_level: medium
claim_type: mixed
tags:
  - AI-Agent
  - agent-harness
  - context-engineering
  - architecture
related_entities:
  - "[[Agent-Harness]]"
  - "[[Context-Engineering]]"
  - "[[Agent-Swarm]]"
  - "[[Agent-Verification]]"
source_raw:
  - "[[20261002-latentspace-rlm-alex-zhang]]"
---

# Recursive Language Model

> [!definition] 定义
> **Recursive Language Model（RLM）** 是一种 Harness 设计：把原始上下文外置到文件系统、REPL 或其他可寻址状态中，让模型通过代码读取、切分、处理这些状态，并程序化调用 subagent 或再次调用自身。它不是一种新的 Transformer 基础架构；重点是改变模型执行复杂任务时的计算结构。

## 核心机制

RLM 可以压缩为四个相互依赖的设计选择：

1. **Context offloading**：长上下文不要求始终驻留在主模型 prompt 中，而是外置保存，模型按需访问。
2. **Code as control language**：代码不是普通工具之一，而是主要动作语言；读取、过滤、循环、聚合和 subagent 调用都可以写成程序。
3. **Recursive subagent calling**：模型可以把局部问题交给另一个模型调用，必要时递归展开。
4. **Shared addressable state**：主 Agent 与子 Agent 围绕同一个外部上下文工作，而不是只依赖不断增长的聊天轨迹。

PrimeAgent 是这一思路的工程化实现之一：它建立在 Pi Mono 上，把 IPython 设为唯一显式工具，其余能力通过 Python module 或 Bash script 暴露；同时加入 persistent subagents 与 agent-to-agent communication（[[20261002-latentspace-rlm-alex-zhang]]，transcript 00:52:01–00:57:40，“Prime Agent and Persistent Subagents”）。

## 从长上下文到组合泛化

RLM 最初针对长上下文问题，但 Alex Zhang 在后续工作中把它的核心价值推进到 **compositional generalization**。

传统 coding-agent harness 往往采用 **trajectory as a prompt**：工具调用、观察结果、subagent 返回都持续追加到主模型轨迹，接近上限时再 compact。RLM 则尝试让主模型学习一个高层程序，把任务拆成多个更小的局部调用。

访谈中的关键观察是：表面完全不同的任务，可能共享同一套高层程序，例如：

~~~text
读取外部状态
    ↓
切分问题 / 生成候选
    ↓
调用 subagent 处理局部子问题
    ↓
程序化聚合与验证
    ↓
继续迭代或结束
~~~

Zhang 报告，在部分实验中，模型在短任务上学到的策略可以迁移到 **8–30× 更长**的任务；数学、写作、检索和聚合等不同任务之间，也可能因为共享相同 meta-strategy 而出现迁移（[[20261002-latentspace-rlm-alex-zhang]]，transcript 00:36:38–00:44:23，“Harnesses as Compositional Generalizers”）。

> **判断**：RLM 的稳定价值不应概括成“让 LLM 自己调用自己”，而应理解为：**用代码和外部状态为模型提供一种可组合的计算中间表示，使重复出现的任务结构能够被学习和复用。**
>
> **证据**：[[20261002-latentspace-rlm-alex-zhang]] 对 RLM 定义、短→长任务迁移和跨任务策略复用的第一作者说明。
>
> **边界**：访谈没有给出完整实验表、基线、方差和失败分布；“8–30×”应视为作者报告的特定实验结果，而不是所有 RLM 任务的通用 scaling law。

## Locally In-Distribution

Zhang 用 **locally in-distribution** 描述 RLM 希望获得的性质：

- 整个任务可以是模型从未见过的、全局 OOD 的问题；
- Harness 先把它分解成多个局部问题；
- 每一个局部模型调用都尽量保持在模型熟悉的分布内；
- 全局能力来自这些局部调用的组合。

这与单纯扩大 context window 不同。后者仍要求一个模型直接处理完整轨迹；RLM 更接近“把一个大程序编译成很多局部可执行步骤”。

> **判断**：Harness 可以成为一种 **计算归纳偏置（inductive bias）**。好的 Harness 不只是给模型更多工具，而是约束它采用更容易训练、验证和迁移的计算结构。
>
> **证据**：[[20261002-latentspace-rlm-alex-zhang]]，transcript 00:47:46–00:49:15，“Long Context, Composition, and Locally In-Distribution Tasks”。
>
> **边界**：局部调用处于训练分布内，并不保证 decomposition、共享状态和最终 aggregation 正确；局部正确仍可能组合成全局错误。

## RLM 与 Agent Swarm

RLM 与 [[Agent-Swarm]] 都能扩展 test-time compute，但主要组织方式不同：

| 维度 | RLM | Agent Swarm |
|---|---|---|
| 核心结构 | 程序化分解 + 递归调用 | 多主体并行搜索 / 协作 |
| 共享状态 | 外置、可寻址上下文 | message board、共享上下文或消息网络 |
| 主要优势 | 组合性、策略复用、上下文外置 | wall-clock 并行、搜索宽度 |
| 主要风险 | decomposition / aggregation 错误、递归成本 | 无效分支、协调成本、收敛与验证 |
| 共同要求 | verifier、停止条件、状态与通信设计 | verifier、停止条件、状态与通信设计 |

RLM 并不排斥 swarm。一个 RLM 程序完全可以生成多个并行 subagent；区别在于，RLM 把“如何生成、调用和聚合这些 Agent”也交给程序表示。

## Model / Harness 边界

Zhang 进一步提出一个尚未验证但重要的研究方向：如果 RLM 中反复出现的高层程序足够稳定，是否可以直接训练模型在 forward pass 内隐式实现这些行为，而不再把每个步骤都暴露为外部 Harness？

这与“能力先在 Harness 中出现，再被模型训练吸收”的更广泛趋势相呼应，但两者需要严格区分：

- **可能内化**：分解策略、搜索模式、局部路由、某些 aggregation pattern。
- **仍应外置**：权限、审计、真实工具执行、持久状态、成本控制、安全边界、确定性验证。

因此，RLM 并不意味着 Harness 最终消失，而是提供了一种研究 **哪些计算应该留在系统层、哪些可以编译进模型** 的实验平台。

## 关键数据点

- RLM 第一作者在访谈中给出的简洁定义：**context offloading + code + programmatic subagent/self-calling**。
- PrimeAgent 将 IPython 作为唯一显式工具，其余工具通过代码模块进入，并支持 persistent subagents。
- 作者报告部分训练实验可从短任务泛化到 **8–30× 更长**任务。
- 作者认为当前主流 coding harness 多属于 trajectory-as-a-prompt 家族，而 RLM 代表结构上不同的 harness class。
- 当前 frontier models 尚未针对 RLM workflow 系统优化；多次模型调用带来的 latency / token 成本仍是主要限制。

## 前提与局限性

- RLM 强依赖模型已有的代码生成与程序理解能力；如果代码不是该领域自然的控制表示，收益可能下降。
- 外置上下文解决的是“如何访问状态”，不是自动保证“访问到正确证据”；检索、切分和聚合仍需要验证。
- 递归调用会快速增加 latency、token 与并发资源，因此需要任务级停止条件和成本控制。
- “locally in-distribution” 是有用的设计目标，不是充分正确性条件。
- 作者关于更好的 post-training scaling、把 RLM 编译进 forward pass 等判断仍属于研究方向。
- 本页目前主要依赖一份第一作者访谈；后续应加入 RLM 论文、Compositional Generalizers 原文及第三方复现，才能把证据等级进一步提高。

## 关联概念

- [[Agent-Harness]] — RLM 属于结构上不同于 trajectory-as-a-prompt 的 Harness 设计。
- [[Context-Engineering]] — 将上下文从 prompt 内存转为外部可寻址状态。
- [[Agent-Swarm]] — 可以作为 RLM 内部的并行计算形式，但需要程序化协调与聚合。
- [[Agent-Verification]] — 局部调用与递归搜索都需要外部 verifier 与停止条件。
