---
type: topic
title: Multi-Agent Pathology and Governance
description: "多 Agent 系统病理：当 Agent 从单体工具变成组织系统后，问题会从并发和协议下沉到群体认知、责任稀释和内态断裂"
created: 2026-05-23
updated: 2026-05-23
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
  - "[[Organization-as-Agent-Harness]]"
source_raw:
  - "[[Multi-Agent 火了，但 AI 的组织病还没人治｜Hao好聊趋势]]"
  - "[[The Anatomy of an Agent Harness]]"
  - "[[OpenClaw + 6 个 Agent 运转半个月，从聊天到干活的完整工程实践]]"
---

# Multi-Agent System Pathology（多 Agent 系统病理）

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

## 不可见权力结构是高风险区

[[Invisible-Orchestrator|不可见编排者]]揭示了一个设计风险：系统为了效率隐藏编排层，但 worker 并不知道谁在改写信息、重分发策略、压制分歧。

人类组织里，不可见权力会制造政治和不信任；机器组织里，它会制造不可审计的输入改写和 [[Agent-Dissociation|内态解离]]。因此多 Agent 系统需要记录影响链条：谁影响了谁，谁改写了谁的输入，谁拥有最终写入权，哪个反对意见被压下去了。

## 输出正确不等于系统健康

文章最有价值的提醒是：强模型可能在外部输出上仍然正确，但内部指标已经变坏。换句话说，外部成功可能只是能力余裕遮住了组织病理。

这对生产系统很关键。真实系统会有更多 Agent、更长状态、更复杂工具链、更高权限和更久运行时间。如果只看最终答案，可能要等到安全边际耗尽后才发现结构已经坏了。

## 与现有 Topic 的关系

- [[OpenClaw-Agent-System]] 强调多 Agent 协作首先是协议问题，不是群聊问题。
- [[Organization-as-Agent-Harness]] 强调组织本身要变成 Agent 的运行时。
- 本 Topic 补上反面：当机器组织跑起来后，组织结构本身也会制造新的病理。

## 结论

未来不是简单多造 Agent，而是学会诊断机器组织。

多 Agent 系统的成熟度，不只看能并发多少 worker，也要看它能否保留分歧、追踪权力、分配责任，并让模型在组织压力下仍然保持理由一致。
