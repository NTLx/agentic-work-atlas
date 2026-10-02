---
type: source-summary
title: "Academia is for Ambition — Alex Zhang, MIT"
canonical_url: "https://www.latent.space/p/rlm"
raw_state: index
original_raw_file: "20261002-latentspace-rlm-alex-zhang.md"
original_body_sha256: "6f36c1d515c4fbd5964ce3b10a94177a0ef3def617f3340021e71b5f88367fa6"
indexed_at: "2026-10-03T07:22:26+08:00"
created: 2026-10-03
updated: 2026-10-03
tags:
  - source-summary
  - recursive-language-model
  - agent-harness
  - context-engineering
  - agent-swarm
  - research-taste
evidence_level: medium
claim_type: mixed
source_locator:
  - "raw L50-L100：GPU kernel 自动化、verification、领域专家作为强 verifier、计算效率"
  - "raw L126-L190：学术研究的高风险押注、Jev 与非 text-to-text 模型空间、RLM 的模型/系统边界"
  - "raw L254-L372：Harness 作为任务程序、trajectory-as-a-prompt、RLM 定义、组合泛化与 locally in-distribution"
  - "raw L374-L470：RLM 训练方向、PrimeAgent、persistent subagents、swarm / scaffold 与模型边界"
  - "raw L472-L598：大规模 agent swarm、协调瓶颈、搜索浪费与收敛问题"
  - "raw L640-L736：jagged intelligence、capability overhang、continual learning、语言/表示对推理的约束"
---

# Academia is for Ambition — Alex Zhang, MIT

> Latent Space 对 Recursive Language Models（RLM）第一作者 Alex Zhang 的完整访谈。本文把受访者对自己工作的机制性说明作为一手证据，同时把对未来模型架构、Agent swarm 和学术研究方向的判断视为研究者观点，不当作已验证事实。

## 编译摘要

### 1. 浓缩

- **核心结论 1：RLM 的关键不是“递归调用模型”本身，而是把 Harness 重写成一种程序化计算结构：上下文外置、代码作为主要控制面、子 Agent 可递归调用。**
  - 关键证据：在 raw L340-L360，Zhang 将 RLM 定义为一种 harness design：唯一核心工具是代码，代码可以程序化调用 subagent，甚至调用自身；原始上下文可以外置到文件系统或 REPL 中，并在 compaction 后继续被访问。
  - PrimeAgent 是这一抽象的工程化实例：基于 Pi Mono，把 IPython 作为唯一显式工具，其余能力以 Python module / Bash script 形式进入；同时加入 persistent subagents 和 agent-to-agent communication（raw L408-L423）。
  - **判断**：RLM 改变的首先是 Agent 的“动作语言”——从逐 turn 调工具，变成让模型写一个可组合程序去读取、切分、调用和聚合外部上下文。

- **核心结论 2：Harness 可以承担“计算归纳偏置（inductive bias）”，让模型学习可跨长度、跨任务迁移的高层程序，而不只是提供工具和上下文。**
  - 关键证据：raw L274-L308 中，Zhang 描述了 RLM 训练时的观察：检索、聚合、数学、写作等表面不同任务，在 RLM 下可能收敛为相同的高层策略——切分问题、生成候选、调用 subagent、循环验证；模型在短任务上学到的策略可直接迁移到更长任务，他在访谈中举出“8–30× 更长”的例子（raw L288-L292）。
  - 他把现有 Claude Code / Codex / Pi 一类 harness 概括为 “trajectory as a prompt”：完整轨迹不断追加到主模型上下文；而 RLM 尝试让每次局部调用都只看到更小、更接近训练分布的问题（raw L320-L372）。
  - **判断**：如果一个 Harness 能把全局 OOD 问题分解成一组局部 in-distribution 调用，它的价值不只是“更好地使用模型”，还可能改变 post-training 的样本效率和泛化结构。

- **核心结论 3：大规模 Agent 系统的核心瓶颈不是“能不能并行”，而是怎样组合搜索、共享信息、验证结果并控制无效 token；领域知识和好的 Harness 可以显著减少暴力搜索。**
  - 关键证据：raw L50-L78 中，Zhang 用 GPU kernel optimization 说明：AI 已能生成很多高排名方案，但真正稳定的方案仍高度依赖懂问题的人作为 verifier；他明确指出，一个懂领域的人给出的方向可能消掉原本需要数千亿到万亿 token 才能探索出来的搜索空间。
  - raw L450-L498 中，他认为前沿 swarm 可以通过极长搜索解决困难问题，但大量分支可能完全无用；真正的问题是“什么设计适合什么任务”，以及 Agent 能否自己决定何时使用 swarm、何时使用更结构化的分解。
  - **判断**：test-time compute 的有效扩展需要 **search + communication + verifier + stopping rule**。没有这些结构，更多 Agent 只是把算力转成更大的搜索噪声。

### 2. 质疑

- **关于 RLM 泛化结果的质疑**：访谈给出了“短任务训练后泛化到 8–30× 更长任务”等结论，但没有同时提供实验设计、基线、方差、失败样本或完整 benchmark。它可以作为第一作者对其工作的机制性说明，不能单靠本访谈量化优势。
- **关于“多数 Harness 都一样”的质疑**：Zhang 多次把 Claude Code、Codex、Pi 等归入 trajectory-as-a-prompt 家族，并引用近期 Harness Tax 工作支持“很多 harness choice 不重要”。这是有启发性的分类，但不同产品在权限、安全、状态、工具协议、并行调度、训练耦合等方面仍可能形成实质差异。
- **关于 locally in-distribution 的质疑**：把一个全局 OOD 任务切成局部 ID 子任务是理想性质，不代表分解本身总能正确，也不保证 subagent 输出可以无损组合。错误的 decomposition、共享状态或聚合逻辑会把局部正确变成全局错误。
- **关于 code-only abstraction 的质疑**：RLM 依赖当前模型很强的代码能力，把 code 作为统一动作语言；在代码表达自然、可验证的任务中这很有优势，但对感知、物理交互或强实时任务，代码可能只是上层控制表示，仍需专门的数据通道与执行 substrate。
- **关于 Agent Swarm 的质疑**：受访者对 OpenAI、Kimi、Gemini 等系统的多处评论明确属于外部观察或推测；除公开事实外，不能把“他们一定这样训练/这样组织”当作已证实实现。
- **关于 Jev / 新模型形态的质疑**：访谈最重要的点是“输出空间不必永远是 autoregressive text-to-text”，但 Jev 的具体训练目标、架构和校准方法在本访谈里并未公开，不能由讨论反推出实现。

### 3. 对标与约束

- **与 [[Agent-Harness]] 对标**：传统定义把 Harness 看成围绕模型的运行时与基础设施；RLM 提供了更强的一层：Harness 还可以规定“模型如何计算”。因此设计轴应从工具数量扩展到 **state representation、decomposition language、subagent topology、aggregation program**。
- **与 [[Context-Engineering]] 对标**：RLM 不是继续把更多文本塞入上下文，而是把上下文本身外置为可寻址状态，再让模型通过代码读取、切分和聚合。它把 long-context 问题从“prompt 如何压缩”转换成“外部状态如何被程序化访问”。
- **与 [[Agent-Swarm]] 对标**：RLM 与 swarm 都在增加 test-time compute，但组织方式不同。Swarm 更强调多个主体并行搜索；RLM 更强调共享上下文上的程序化分解与递归调用。两者可以组合，但都需要 verifier 与通信结构来抑制无效搜索。
- **与软件系统中的中间表示对标**：代码在 RLM 中类似一种 IR（intermediate representation）：它把高层意图压成可执行、可组合、可循环的结构，再由模型或 subagent 填充局部计算。此类 IR 的价值来自可验证性与复用，而不只是表达力。
- **硬约束**：RLM 仍需要强代码生成模型、可执行环境、状态隔离、错误处理和可验证的子任务；递归调用会带来显著 latency / token 成本。
- **研究边界**：把 RLM 行为进一步“编译进模型 forward pass”、获得更好的 post-training scaling law，当前在访谈中仍是研究方向，不是已经建立的工程结论。
- **组织层旁逸**：Zhang 对 PhD 的核心判断是“资源劣势要用探索自由来换”——学术研究的比较优势不是复制 frontier lab 的当前路线，而是押注那些今天看起来太简单、太怪或尚无规模回报的问题（raw L134-L160）。这与 Agent 系统设计中的同一原则相呼应：当算力无法竞争时，应该改变问题表示与搜索空间，而不是在同一轴上硬拼规模。

## 证据边界

- 证据主体是 RLM 第一作者 Alex Zhang 对自己工作、PrimeAgent 合作和研究判断的一手访谈；对 RLM 定义、设计动机和本人参与的实现具有较强 provenance。
- Transcript 为公开页面转录文本，已通过 transcript-enabled canonical 页面确认可恢复，存在自动转录误差，例如人名和模型名偶有识别偏差；本摘要只采用上下文可明确还原的概念与机制。
- 关于未公开内部结果、第三方实验室训练方式、未来 scaling law、前沿 swarm 实现细节等内容，只作为受访者判断记录，不升级为确定事实。

## 关联概念

- [[Recursive-Language-Model]]
- [[Agent-Harness]]
- [[Context-Engineering]]
- [[Agent-Swarm]]
- [[Agent-Verification]]
