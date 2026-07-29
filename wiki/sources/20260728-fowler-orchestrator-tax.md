---
type: source-summary
title: "The Orchestrator's Tax"
source_raw:
  - "[[20260728-fowler-orchestrator-tax]]"
created: 2026-07-29
updated: 2026-07-29
tags:
  - source-summary
  - agentic-engineering
  - multi-agent
evidence_level: medium
claim_type: mixed
---

# The Orchestrator's Tax

> Rahul Garg（Thoughtworks Principal Engineer，发表于 martinfowler.com，2026-07-28）的探索性文章：subagent 通常以省时和并行来辩护，但在长时程多 agent 工作中最重要的不是这个——orchestrator 上下文中的每个 token 都在竞争它的注意力，**subagent 的真正价值是它把什么挡在那个上下文之外，而不是它跑得多快**。核心概念 cognitive locality（需要同一心智模型的任务应当待在一起）。来源：martinfowler.com。证据等级：medium（基于单一真实 incident 的探索性工作，作者自认"开放式问题多于定论"，成本排序是 orchestrator 自评而非实测；阈值针对 Claude Sonnet 5 校准）。

## 编译摘要

### 1. 浓缩

- **核心结论1**: 命题——subagent 是保护 orchestrator 工作记忆的工具，不是并行加速器。"The tax I went looking for was never on the subagents. It was on the orchestrator, in what it chose to carry forward."
  - 关键证据: orchestrator 是长会话中**唯一跨时间积累理解**的部分（记得设计决策的理由、携带架构约束、知道哪些取舍已讨论过）；subagent 本来就该是一次性的——探索、重复读文件、失败尝试、噪声中间推理都应留在 worker 上下文中，"never make the trip back to the main thread"。多 agent 设计的核心问题从"跑几个 agent"变成"什么配进入 orchestrator 的上下文"
- **核心结论2**: 两种成本不可混同——token 花一次就完，context 污染此后每轮都收租
  - 关键证据: 事件：orchestrator 建议"check on the agents"，工具拉回后台 agent 的完整原始 transcript（数万 token 的 JSONL）整体导入主线程，且发生两次。关键区分有二：① 留在上下文的污染对此后每一轮课税（"once polluted, keeps charging rent for the rest of the session"）；② 第二种机制与空间无关——上下文里挤的东西越多，模型越难挑出当下重要之物，**即使空间充裕**；更大的窗口不解决问题，只是给噪声更大的堆放空间
- **核心结论3**: cognitive locality + 永久规则 + 治理反模式
  - 关键证据:
    - **cognitive locality**: 两个 subagent 各自独立重建代码库的同一心智模型——因为工作按**任务**切分而非按**每个任务所需的知识**切分。"Tasks that need the same mental model should usually stay together"；文件所有权重叠是合并信号，不是 spawn 信号
    - **四条 CLAUDE.md 永久规则**: ① 一波 2-4 个 agent（≥5 先问共享文件/惯例的任务是否该合并）② 已知信息能回答时不轮询状态，不为轻量问题拉完整 transcript ③ 并发 agent prompt 中禁止仓库级 git 操作 ④ 文件所有权重叠视为整合信号。每条都在回答同一问题：这块信息（或这种切法）配不配进入 orchestrator 上下文
    - **治理反模式**："The next mistake would have been more governance"——发现 subagent 不继承父会话 skill 后，第一反应加 confirm-before-spawn 审批门，随即意识到解决错了问题（缺的是 skill 传播的**事实**，不是审批步骤）；审批门会给每个类似会话加往返，且很快会在 autopilot 上批准——"I wasn't really improving governance. I was just adding another ritual."。启发式：**加规则前问"一个称职的 orchestrator 知道那一个缺失事实后能做对吗"——能则规则只应陈述事实；开始规定决策程序（审批/检查点/强制步骤）通常是用流程编码替代了一句澄清**
    - **第四种 harness**（致谢节自陈）: Böckeler 的 Harness Engineering 列三种（maintainability / architecture fitness / behaviour），本文属于第四种——**编排过程本身**：前馈指南（CLAUDE.md 规则）遇反馈信号（orchestrator 自评 + 人类会话审查），由人类掌舵更新

### 2. 质疑

- **关于证据性质的质疑**: 单一 incident + orchestrator 自评（"the orchestrator grading its own mistake"）。作者明确声明无逐调用 token 记账，"轮询成本 > 四 agent 复制税"的排序是 orchestrator 自己的说法而非测量事实；可信部分更窄：transcript dump 真实、wall-clock 计时真实、status-check 路径引入了大而可避免的成本——是否单一最大成本仍是假设
- **关于命题方向的质疑**: "subagent 真正用途 = 保护工作记忆"是 belief 不是 measurement（作者原话："That's a belief, though, not a measurement"）。作者实测的是隔离失败的代价（反面），未测隔离成功的收益（正面）——命题由反面证据支撑
- **关于阈值模型依赖的质疑**: 2-4/wave、5 为整合信号——针对 Claude Sonnet 5 校准，作者自认其他模型可能需要不同平衡，且"对任何把阈值呈现为普适常数的编排文章保持怀疑"。自我辩护同时标定了迁移边界
- **关于治理极简主义的边界质疑**: "state the fact, don't prescribe procedure" 在单人 + 一群 agent 的场景有效；多人团队、合规高风险场景可能需要程序型治理（审批/检查点）。文章场景不覆盖这些，启发式的适用域未论证

### 3. 对标

- **两种成本 ↔ [[Context-Rot]]**: "context 污染每轮收租"是 Context-Rot 的从业者叙事；Context-Rot 第五约束"最优任务分解粒度 = argmin(rot 累积损失 + 协调成本)"是 cognitive locality 的形式化——两源（理论推导 × 实践 incident）收敛于同一分解权衡。Anti-rot 五模式的"隔离容器"模式（rot 局限在可丢弃上下文中）= subagent 隔离的设计意图；"新鲜审查者"模式解释为何 orchestrator 不该继承 worker 上下文（综合判断）
- **治理反模式 ↔ 同周 GitHub 文章的 Approve 疲劳**: [[20260727-github-harness-is-all-you-need]] 说"反复按 Approve 训练人不读审批内容"（审批过多），本文说审批门会退化为 autopilot 仪式（审批仪式化）——两篇从不同角度收敛于同一命题：**人类审批是耗散性资源，治理设计必须省着用**。[[Auto-Mode]] 命题由此获得治理成本叙事（综合判断）
- **第四种 harness ↔ [[Harness-Engineering]]**: Böckeler 三种 + 本文编排过程型。"feedforward 规则 + feedback 自评 + 人类掌舵更新"= harness 棘轮效应（每个错误变永久约束）的微观实例；flywheel（session 暴露 gap → 人类注意到 → 判断 → 永久规则 → 下一 session 验证）是棘轮的人类在环版本
- **永久规则经济学 ↔ [[CLAUDE-md]]**: "every extra line in a standing instruction file is a cost paid again on every future session" = CLAUDE.md 的写作经济学；state-the-fact 启发式（陈述事实而非规定程序）可作永久指令文件的第一写作原则
- **跨域类比: 空管工作记忆**: orchestrator ≈ 空中交通管制员——管制员的价值不在于并行指挥更多飞机，而在于**什么不该进入他的注意力**；cognitive locality ≈ 康威定律的认知版（系统分解应遵循心智模型边界而非任务列表）（综合判断）

### 关联概念

- [[Orchestrators-Tax]] — 本文核心命题，新建 entity
- [[Context-Rot]] — "context 污染每轮收租" = rot 的从业者叙事；cognitive locality = 最优分解粒度约束的实践版
- [[Agent-Orchestration]] — 编排设计核心问题从"跑几个 agent"转为"什么配进入 orchestrator 上下文"
- [[Harness-Engineering]] — 第四种 harness：编排过程本身（feedforward 规则 + feedback 自评 + 人类掌舵）
- [[CLAUDE-md]] — 永久指令文件写作经济学：每行都是未来每个会话的成本
