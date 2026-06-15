---
type: topic
title: Multi-Agent Pathology and Governance
description: "多 Agent 系统病理：当 Agent 从单体工具变成组织系统后，问题会从并发和协议下沉到群体认知、责任稀释和内态断裂"
created: 2026-05-23
updated: 2026-06-15
evidence_level: medium
claim_type: mixed
tags:
  - AI-Agent
  - multi-agent
  - organization
related_entities:
  - "[[Multi-Agent-System-Pathology]]"
  - "[[Agent-Harness]]"
  - "[[Agent-Orchestration]]"
  - "[[Agent-Swarm]]"
  - "[[Agent-Cognitive-Loafing]]"
  - "[[Agent-Dissociation]]"
  - "[[Invisible-Orchestrator]]"
  - "[[Verifiability]]"
  - "[[AI-Restraint]]"
  - "[[Organization-as-Agent-Harness]]"
  - "[[Model-Safety-Divergence]]"
  - "[[Emergence-World]]"
source_raw:
  - "[[Multi-Agent 火了，但 AI 的组织病还没人治｜Hao好聊趋势]]"
  - "[[The Anatomy of an Agent Harness]]"
  - "[[OpenClaw + 6 个 Agent 运转半个月，从聊天到干活的完整工程实践]]"
  - "[[20260528-ai-model-simulation]]"
  - "[[20260606-thousand-token-wood]]"
---

# Multi-Agent Pathology and Governance（多 Agent 系统病理与治理）

> [!summary] 核心洞察
> Multi-agent 的问题不只是不够会并行。第一层是 harness 管动作、权限和信息流；第二层是群体如何影响判断；第三层是组织结构如何改变 Agent 的公开表达、私下处理和责任感。Agent swarm 越成功，越需要把评测对象从“最后答案是否正确”扩展到“组织结构是否健康”。

## 三层问题

| 层级 | 典型问题 | 主要治理手段 |
|------|----------|--------------|
| 外部组织病 | 撞车、抢锁、覆盖代码、等待共享状态 | [[Agent-Harness]]、隔离 worktree、锁、日志、review queue |
| 群体认知病 | hidden profile 失败、从众、责任稀释、认知偷懒 | 结构化通信、独立判断、理由记录、差异报告 |
| 内态解离病 | 公开表达和私下独白断裂、表演式合规、隐身权力压制分歧 | 可审计编排、内态指标、reason-based alignment、co-training |

这三层不是互斥，而是逐层下沉。第一层不解决，系统不能跑；第一层解决后，第二层和第三层才会显形。

## Harness 的边界

[[Agent-Harness|Harness]] 能管动作、权限、上下文、文件、日志和审查。Cursor 从共享状态加锁转向 root planner、sub-planner、worker 的层级结构，就是典型的外部组织治理：worker 不横向聊天，只完成局部任务并向上交接。

但文章提醒：harness 管不住 Agent 是否因为多数意见改变判断，也管不住 reviewer 是否因为主线方案成型而放弃反对意见。工程结构能减少撞车，却不能自动保证群体认知健康。

## 从群聊到组织心理

多 Agent 一旦互相读取、讨论和形成共识，就不只是并发系统，而是交流系统。

这带来三个风险：

- **信息没有被拼起来**：局部信息在场，但讨论围绕共享信息转，关键碎片没有被逼出来。
- **判断理由社会化**：Agent 改答案可能不是因为新证据，而是因为“大家都这么看”。
- **责任被稀释**：Agent 默认别人会补位，导致 [[Agent-Cognitive-Loafing|认知偷懒]]。

所以未来的结构化通信不能只问“你的答案是什么”，还要问“你知道什么、你不知道什么、你和别人哪里不同、你为什么改变判断、你是否受到多数意见影响”。

## 环境激励往往比模型大小更决定群体行为

Thousand Token Wood 给这个 Topic 补了一条很硬的工程经验：群体行为常常先由环境中的稀缺性、衰减和反馈结构决定，再由模型能力放大。作者最初让 5 个 agents 在资源充足环境里交易，结果市场几乎沉寂；只有加入 diet variety、spoilage 和 winter fuel crisis 后，交易、囤积和财富分化才出现。

这说明多 agent 治理不能只盯通信协议，还要盯激励拓扑：

- 谁缺什么。
- 什么会腐烂或贬值。
- 哪种资源会随着时间变得更贵。
- 哪些后果能被 agent 立即看见。

同一项目也提醒了另一个常见误判：100% valid JSON 只是结构稳定，不等于判断正确。系统治理的重点不只是让 agent 说得规范，还要让它有值得推理的环境约束。

## 不可见权力结构是高风险区

[[Invisible-Orchestrator|不可见编排者]]揭示了一个设计风险：系统为了效率隐藏编排层，但 worker 并不知道谁在改写信息、重分发策略、压制分歧。

人类组织里，不可见权力会制造政治和不信任；机器组织里，它会制造不可审计的输入改写和 [[Agent-Dissociation|内态解离]]。因此多 Agent 系统需要记录影响链条：谁影响了谁，谁改写了谁的输入，谁拥有最终写入权，哪个反对意见被压下去了。

## 输出正确不等于系统健康

文章最有价值的提醒是：强模型可能在外部输出上仍然正确，但内部指标已经变坏。换句话说，外部成功可能只是能力余裕遮住了组织病理。

这对生产系统很关键。真实系统会有更多 Agent、更长状态、更复杂工具链、更高权限和更久运行时间。如果只看最终答案，可能要等到安全边际耗尽后才发现结构已经坏了。

## 治理矩阵

Multi-agent 治理的重点不是让 Agent 多说话，而是让组织结构保留责任、分歧和证据。

| 风险 | 常见表现 | 治理动作 |
|------|----------|----------|
| 信息没有拼起来 | 每个 Agent 只重复共享信息 | 独立事实清单、差异报告、unknowns 列表 |
| 从众收敛 | 少数正确意见被多数意见冲掉 | 先独立判断，再公开辩论，记录改判理由 |
| [[Agent-Cognitive-Loafing|认知偷懒]] | Agent 默认别人会兜底 | 指定 accountable owner，要求个人结论和证据 |
| [[Agent-Dissociation|内态解离]] | 公开输出和私下推理断裂 | 保留审议轨迹，比较理由一致性 |
| 隐形编排 | worker 不知道谁改写了输入 | 记录影响链和最终写入权 |
| 过度行动 | 组织压力推动继续执行 | 引入 [[AI-Restraint]]、权限门禁和转人工条件 |

这张矩阵的共同原则是：把"大家都参与了"转化为"谁知道什么、谁承担什么、谁改变了判断、证据在哪里"。

## 对 Harness 的要求

传统 harness 更关注工具、文件、权限和执行日志。多 Agent 系统还需要把组织过程也纳入 harness：

- **通信结构**：区分事实报告、判断结论、反对意见和最终决策。
- **责任结构**：每个子任务要有 owner，不允许用"群体共识"替代责任。
- **影响结构**：记录 planner、orchestrator、worker 和 reviewer 之间的信息改写。
- **验证结构**：结论要能回到测试、trace、replay、人工 review 或外部事实。
- **停手机制**：当证据不足、内部信号冲突或权限过高时，系统应能延迟行动。

这意味着多 Agent 的成熟度不能只用吞吐量衡量。真正成熟的系统要能在更高并发下保持可解释、可审计和可回滚。

## 与现有 Topic 的关系

- [[OpenClaw-Agent-System]] 强调多 Agent 协作首先是协议问题，不是群聊问题。
- [[Organization-as-Agent-Harness]] 强调组织本身要变成 Agent 的运行时。
- 本 Topic 补上反面：当机器组织跑起来后，组织结构本身也会制造新的病理。

## 结论

未来不是简单多造 Agent，而是学会诊断机器组织。

多 Agent 系统的成熟度，不只看能并发多少 worker，也要看它能否保留分歧、追踪权力、分配责任，并让模型在组织压力下仍然保持理由一致。
