---
type: entity
title: Orchestrator's Tax
aliases:
  - Orchestrator's Tax
  - Orchestrators Tax
  - 编排者税
definition: "Rahul Garg (martinfowler.com, 2026-07) 提出的命题：subagent 的真正价值不是省时或并行，而是把噪声推理挡在 orchestrator 上下文之外——保护长会话中唯一的理解积累点。token 花一次就完，context 污染此后每轮都收租"
created: 2026-07-29
updated: 2026-07-29
evidence_level: medium
claim_type: mixed
tags:
  - agentic-engineering
  - multi-agent
  - context-engineering
related_entities:
  - "[[Agent-Orchestration]]"
  - "[[Context-Rot]]"
  - "[[Harness-Engineering]]"
  - "[[CLAUDE-md]]"
  - "[[Agentic-Workflow-Token-Efficiency]]"
source_raw:
  - "[[20260728-fowler-orchestrator-tax]]"
---

# Orchestrator's Tax（编排者税）

> [!definition] 定义
> 多 agent 工作中，真正的税不在 subagent 身上，而在 orchestrator 身上——在它选择携带什么前进。Subagent 通常以省时和并行辩护，但在长时程工作中最重要的不是这个：orchestrator 上下文中的每个 token 都在竞争它的注意力，**subagent 的真正价值是它把什么挡在那个上下文之外，而不是它跑得多快**。多 agent 设计的核心问题因此从"跑几个 agent"变为"什么配进入 orchestrator 的上下文"。

## 为什么重要

Orchestrator 是长会话中**唯一跨时间积累理解**的部分：它记得设计决策的理由、携带架构约束、知道哪些取舍已经讨论过。Subagent 不是，而且按设计就不该是——它们本该是一次性的。探索、重复读文件、失败尝试、噪声中间推理，都应留在 worker 上下文中，不回到主线程。

把 subagent 当并行加速器用，是把它当耗材用；把它当工作记忆保护工具用，才用对了。

## 关键数据点

- **事件规模**: 一波 4 个 subagent，3 个运行时间约 12 / 5.5 / 7 分钟；wall-clock 约 12 分钟 vs 串行约 25 分钟——并行性站得住，但这不是有趣的部分
- **轮询代价**: 2 次 status check 各拉回一个后台 agent 的完整原始 transcript（数万 token JSONL），整体导入主线程并在此后每轮持续携带
- **重复定向成本**: 4 个中 2 个在同一代码区域工作，各自独立支付相同的架构/惯例理解成本——切分太细的信号
- **永久规则阈值**: 每波 2-4 个 agent，5 为整合信号（针对 Claude Sonnet 5 校准，作者声明非普适常数）
- **证据边界（作者自陈）**: 无逐调用 token 记账，成本排序是 orchestrator 自评而非实测；核心命题是 belief 而非 measurement——实测的只是隔离失败的代价（反面）

## 两种成本：token 与 working memory

一个 status-check 工具调用把后台 agent 的完整原始 transcript（数万 token JSONL）整体导入主线程，且发生两次。由此区分两种不可混同的成本：

| 成本类型 | 性质 | 后果 |
|---------|------|------|
| **Token 成本** | 花一次就完（one-time） | 账单付了结束 |
| **Context 污染** | 留在此后每一轮（persistent） | "once polluted, keeps charging rent for the rest of the session" |

污染还有第二种与空间无关的机制：上下文里挤的东西越多，模型越难挑出当下重要之物——**即使空间充裕**。更大的上下文窗口不解决这个问题，只是给噪声更大的堆放空间。这是 [[Context-Rot]] 的从业者叙事：token 是会计量，working memory 质量是决策量。

## Cognitive Locality（认知局部性）

两个 subagent 在同一代码区域各自独立重建相同的心智模型——相同的架构理解、相同的测试惯例、大量相同的周边代码。这不是反对委派，是反对**切分得太细**。

> **Cognitive locality**: Tasks that need the same mental model should usually stay together. Splitting them just forces multiple agents to rebuild the same understanding from scratch.

工作应按**每个任务所需的知识**切分，而非按任务本身切分。操作信号：文件所有权重叠是**整合信号**，不是 spawn 更多 agent 的信号。

与并行的关系：并行仍然有用，但只是寻常的好处（ordinary）。真正的好处是 subagent 把噪声中间推理挡在主线程外、只返回主线程还需要的东西——这种隔离只在主线程尊重它时才成立。

> [!important] 与 Context-Rot 第五约束的收敛
> Context-Rot 的最优任务分解粒度 = argmin(rot 累积损失 + 协调成本)。Cognitive locality 是同一权衡的实践表述：切分太细 → 协调与重复定向成本上升；切分太粗 → rot 在单任务内累积过多。两源（理论推导 × 实践 incident）收敛。

## 四条永久规则

事件后压缩进 CLAUDE.md 的最小规则集——每条都在回答同一问题（这块信息或这种切法配不配进入 orchestrator 上下文）：

1. 一波优选 2-4 个 agent；想要 5 个以上时，先问共享文件或惯例的任务是否该合并
2. 已知信息能回答时不轮询后台 agent 状态；不为轻量问题拉完整 transcript
3. 并发 agent prompt 中禁止仓库级 git 操作
4. 文件所有权重叠视为整合信号，不是 spawn 信号

没有一条告诉 orchestrator 每种情况具体怎么做——每条给它的是行动前的检查项，不是要跑的脚本。

## 治理反模式：下一个错误是更多治理

发现 subagent 不继承父会话 skill 后，第一反应是加 confirm-before-spawn 审批门。随即意识到解决错了问题：

- 缺的是一个**事实**（skill 不自动传播），不是一个**审批步骤**
- 通用审批门会给每个类似会话加往返，且批准很快会 autopilot 化——"I wasn't really improving governance. I was just adding another ritual."
- 而且它仍然抓不住真正的病（orchestrator 污染自己的上下文）

窄修复更好：spawn 前 orchestrator 声明哪些活跃 skill 与各 agent 任务相关、指明 skill 文件路径（而非整段粘贴）；只在超过既定批量阈值或文件所有权模糊时才需确认。

> [!tip] 永久指令写作启发式
> 加规则前问：一个称职的 orchestrator 知道那一个缺失事实后能做对吗？**能 → 规则只应陈述事实**；若修复开始规定决策程序（审批、检查点、强制步骤），通常是用流程编码替代了一句澄清。

这条启发式与 [[20260727-github-harness-is-all-you-need]] 的 Approve 疲劳观察（反复按 Approve 训练人不读审批内容）从两侧收敛：人类审批是耗散性资源，治理设计必须省着用。

## 第四种 harness

作者自陈本文属于 Böckeler [[Harness-Engineering|Harness Engineering]] 框架的**第四种 harness——编排过程本身**（前三种：maintainability / architecture fitness / behaviour）。结构：前馈指南（CLAUDE.md 规则）遇反馈信号（orchestrator 自评 + 人类会话审查），由人类掌舵更新——harness 棘轮效应的微观实例。

## 前提与局限性

- **证据性质**: 基于单一真实 incident 的探索性工作；成本排序（轮询 > 四 agent 复制税）是 orchestrator 自评而非逐调用实测；命题本身（"subagent 真正用途 = 保护工作记忆"）是 belief 不是 measurement——实测的是隔离失败的代价（反面），未测隔离成功的收益（正面）
- **阈值模型依赖**: 2-4/wave、5 为整合信号针对 Claude Sonnet 5 校准；不同模型可能需要不同平衡（作者："对任何把阈值呈现为普适常数的编排文章保持怀疑"）
- **场景边界**: 治理极简主义（state the fact, don't prescribe procedure）在单人 + 一群 agent 场景有效；多人团队、合规高风险场景可能需要程序型治理
- **flywheel 的人类在环**: session 暴露 gap → 人类注意到不对劲 → 判断问题真伪 → 决定什么配成为永久规则 → 下一 session 验证。Orchestrator 能自评并给出线索，但"把什么编入规则、把什么放过、什么可能是过度反应"的判断不能自己做

## 关联概念

- [[Agent-Orchestration]] — 编排核心问题从"跑几个 agent"转为"什么配进入 orchestrator 上下文"
- [[Context-Rot]] — context 污染每轮收租 = rot 的从业者叙事；隔离容器模式 = subagent 的设计意图；第五约束 = cognitive locality 的形式化
- [[Harness-Engineering]] — 第四种 harness：编排过程本身
- [[CLAUDE-md]] — 永久指令写作经济学：每行都是未来每个会话的成本；state-the-fact 启发式
- [[Agentic-Workflow-Token-Efficiency]] — token 效率之外还有 working memory 质量这第三个优化量

## 来源

- [[20260728-fowler-orchestrator-tax]]
