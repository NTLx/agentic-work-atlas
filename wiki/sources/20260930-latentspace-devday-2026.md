---
type: source-summary
title: "Why Dwarkesh is Wrong about Computer Use + How OpenAI shipped its Jev competitor in 1 Week"
canonical_url: "https://www.latent.space/p/devday-2026"
raw_state: index
original_raw_file: "20260930-latentspace-devday-2026.md"
original_body_sha256: "c4c123093cb6e32516b2c73a0cbdc42ff0f11aa896762b75714bed095610e3d0"
indexed_at: "2026-10-01T21:58:51+08:00"
created: 2026-10-01
updated: 2026-10-01
tags:
  - source-summary
  - computer-use
  - agent-harness
  - api-platform
  - context-engineering
  - decision-models
evidence_level: high
claim_type: mixed
source_locator:
  - "00:05:20–00:12:02 — Computer Use capability changes; debugging, generated code, accessibility/DOM/Playwright, App Shots"
  - "00:12:32–00:19:06 — latency bottlenecks, event-driven operation, safety/consent, Computer Use as software verification"
  - "00:19:34–00:23:21 — async function calling, mid-turn steering, WebSockets, UltraFast"
  - "00:23:38–00:31:13 — Decisions API / Jev inspiration / constrained parallel low-latency decision path"
  - "00:32:35–00:36:57 — prompt caching, pre-warming, long-lived cache, compaction"
  - "00:37:13–00:38:56 — higher-level agent primitives and AI cloud boundary"
---

# Why Dwarkesh is Wrong about Computer Use + How OpenAI shipped its Jev competitor in 1 Week

## 编译摘要

### 1. 浓缩

- **核心结论 1：Computer Use 的能力增量已经不能只归因于模型；representation 与 harness 正成为同等重要的性能变量。**
  - Ari Weinstein 将近几个月的变化同时归因于模型更会重试/调试，以及 Computer Use harness 开始混合截图、accessibility、DOM、Playwright 和模型生成代码；代码还能一次完成多步操作，而不是逐点击推进。
  - **判断**：Computer Use 的有效能力来自 model × representation × action substrate × recovery loop 的乘积。截图只是最低层输入；结构化 accessibility/DOM 提供更完整状态，代码执行则把动作粒度从“单步 GUI 操作”提升到“程序化批处理”。

- **核心结论 2：当 Agent 变快后，瓶颈会从推理迁移到软件与工具本身；因此运行时需要异步、事件驱动和可中途干预。**
  - 访谈明确提到页面加载和外部响应开始占据可观延迟；在可行场景下，应在真实事件发生后立即触发下一步，而不是固定等待。
  - API 侧同步提供 async function calling、mid-turn steering 与 WebSockets，让模型不必因长工具调用完全暂停，并允许工具结果或用户指令在 turn 中途进入。
  - **判断**：Agent loop 正从“模型调用—等待工具—再调用模型”的串行 RPC，演化为并发、双向、事件驱动的 runtime。

- **核心结论 3：Decision Model 可以被理解为一种独立平台 primitive：用较弱但更快、更受约束的推理承担高频局部决策。**
  - Nikunj Handa 说明 Decisions API 初版并没有新训练权重，而是在 Luna 上叠加 structured constraints、并行问题和针对 time-to-first-decision 的 inference 优化。
  - 这说明“decision model”第一阶段的差异未必来自新 foundation model，而可能来自任务表面、解码约束、并行化和 serving stack。
  - **判断**：复杂 Agent 不必让同一个 frontier model 处理所有 decision。高频分类、路由、tool selection 等局部判断可以拆成低延迟 decision path；长程 planning 再由高能力模型承担。

- **核心结论 4：Prompt Cache、pre-warming 与 compaction 已经成为长寿命 Agent API 的基本运行时机制。**
  - OpenAI API 团队把长线程 cache guarantee、cache pre-warming、cache diagnostics 与 compaction 放在同一 performance 路线中；Agents API 将部分 compaction 封装进 harness，Responses API 则保留 server-side / manual control。
  - **判断**：长寿命 Agent 的“状态”不能等同于无限增长的 prompt。平台必须在 cache reuse、context compression、storage/memory 与 developer control 之间建立分层。

- **核心结论 5：Agent API 的产品边界仍在形成，且模型与官方 harness 可能存在训练耦合。**
  - Ari 明确表示 OpenAI 的 Computer Use 模型会在其 harness 上训练，因此使用发行中的 harness 可能存在速度、成本或准确性优势。
  - Nikunj 也把“哪些能力应该进入高层 API，哪些留给开发者 harness”描述为持续开放问题。
  - **判断**：Agent 平台不会简单收敛为“模型 API + 一组工具”。未来竞争点之一是：哪些 runtime primitive 被标准化进平台，哪些仍保持可替换的开发者控制面。

### 2. 质疑

- **Computer Use 性能**：关于“多数任务比平均人更快”、成本倍数和 benchmark 提升均为 OpenAI 受访者自述，Transcript 没有提供独立实验设计，不能当作跨产品客观排名。
- **Harness 优势**：官方 harness 与模型共同训练可能形成真实协同，也可能带来平台锁定；来源没有比较同模型在独立第三方 harness 下的系统性结果。
- **Decision Model 定义**：初版 Decisions API 仍基于 Luna 权重，因此当前证据支持的是“decision-serving primitive”，还不足以证明已出现独立的模型范式；calibration 也被明确留作开放问题。
- **Computer Use 的 universality**：能操作任意人类软件不等于稳定完成任意业务流程。身份验证、权限、支付、反自动化机制和 prompt injection 仍会约束实际可用性。
- **高层 API 边界**：访谈只说明 OpenAI 正在探索 memory / storage / harness 等抽象，并未形成稳定设计结论。

### 3. 对标与约束

- **与 [[Agent-Harness]]**：本来源把“harness 影响能力”推进为更强命题——模型可能直接在特定 harness 上训练，因此模型能力和 runtime interface 形成协同设计，而不是两个完全可交换的层。
- **与 [[ACI-Agent-Computer-Interface]]**：Computer Use 证明 ACI 不应被理解为纯 GUI 自动化。更强接口同时暴露 pixels、accessibility tree、DOM 和 programmatic execution，并允许模型按任务选择最合适的表示/动作层。
- **与 [[Tool-Latency-Bottleneck]]**：来源提供新的 2026 一手实例：当 Computer Use 本身加速，网页加载、远端响应和操作完成事件开始占总时延更大比例，异步与 event-driven scheduling 因而成为架构问题。
- **与 [[Context-Engineering]] / [[Compaction]]**：cache guarantee、pre-warming 与 compaction 说明 context 生命周期已经成为 API 层 primitive，而不再只是单个 coding agent 的内部技巧。
- **与 [[Local-Bounded-Reasoning]]**：Decisions API 的 constrained / parallel / fast-decision 路线，是把局部判断从大模型长程 reasoning 中拆出的工程实例。

## 证据边界

- 来源为 Latent Space 在 2026-09-30 发布的完整时间戳访谈，嘉宾 Ari Weinstein 与 Nikunj Handa 分别代表 OpenAI Computer Use 与 API 产品侧。
- 产品结构、实现选择和内部开发时间属于直接参与者的一手陈述；性能、成本、可靠性和未来能力属于第一方报告或前瞻判断。
- Raw 保存可恢复的时间戳证据地图；canonical 页面可重新取得完整 Transcript。

## 关联概念

- [[Agent-Harness]]
- [[ACI-Agent-Computer-Interface]]
- [[Tool-Latency-Bottleneck]]
- [[Context-Engineering]]
- [[Compaction]]
- [[Local-Bounded-Reasoning]]
