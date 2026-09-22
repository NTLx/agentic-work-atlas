---
type: entity
title: Agent Verification
aliases:
  - Agent 自主验证
  - Agentic Verification
definition: "Agent 能自主运行验证循环的能力——不是 lint/type check，而是 agent 能自己启动测试环境、执行操作、观察结果并判断是否通过"
created: 2026-06-12
updated: 2026-09-22
evidence_level: medium
claim_type: mixed
tags:
  - agentic-engineering
  - verification
  - claude-code
related_entities:
  - "[[Claude-Code-CLI]]"
  - "[[Agent-Loops]]"
  - "[[Auto-Mode]]"
  - "[[Validation-Pipeline]]"
  - "[[Captain-Mindset]]"
  - "[[Rubric-Based-Evaluation]]"
  - "[[Software-Development-Autonomy-Levels]]"
source_raw:
  - "[[20260713-microsoft-ships-ai-agents-enterprise-scale]]"
  - "[[20260608-reflecting-on-year-of-claude-code]]"
  - "[[20260620-l8-principal-agentic-workflow]]"
  - "[[20260702-anthropic-harnesses-long-running-agents]]"
  - "[[20260727-github-harness-is-all-you-need]]"
  - "[[20260726-berkeley-auto-software-dev]]"
  - "[[20260708-towards-autonomous-software-dev.pdf]]"
  - "[[20260727-hf-agent-intrusion-technical-timeline]]"
  - "[[20260728-openai-scientific-computing-field-report.pdf]]"
  - "[[20260801-lean-kernel-soundness-bug-postmortem]]"
  - "[[20260828-automated-researchers-alignment-failures]]"
  - "[[20260915-intelligent-artifact-code-review-model-routing]]"
  - "[[20260915-trail-of-bits-1password-ai-patching-benchmark]]"
  - "[[20260914-anthropic-test-impact-analysis-ci]]"
  - "[[20260916-github-copilot-runtime-rust-migration]]"
  - "[[20260918-trailofbits-auditing-good-enough-ai]]"
---

> [!definition] 定义
> Agent 验证不是传统意义上的自动化测试（lint、type check、unit test），而是 agent 能**自主运行验证循环**——自己启动测试环境、执行操作、观察结果、判断是否通过，并在失败时自行修复。

## 关键数据点

- Claude Code 的 verification 路径: agent 打开 CLI → 测试自己写的 feature → 观察结果 → 修复
- Desktop development skill: Claude 启动本地 desktop app → 用 computer use 点击测试 UX → 测试 edge cases → 修复并重新检查
- 验证循环示例: iOS simulator / Android simulator / desktop computer use
- 从 Opus 4 开始实现 self-testing，到今天已成常态

## 保护 Oracle：验证基线不能被同一变更者静默改写（09-20 编译新增）

GitHub Copilot runtime 的 Rust 迁移给“独立验证”提供了一个生产级软件案例：迁移 Agent 可以重写实现，但旧 E2E 行为测试被当作受保护 oracle；删除或修改这些测试本身就是 red flag。测试、静态分析、Agent review 与人类架构 review 被刻意分层，而最终 merge 仍由理解系统的人类负责。

这把“同一个 Agent 既写实现又写测试只证明一致性”的抽象风险落到了可执行规则：

~~~text
implementation mutation
        ≠
oracle mutation

agent may change implementation
        ↓
protected behavioral oracle
        ↓
independent review / CI / rollout
        ↓
human release judgment
~~~

**判断**：验证器独立性不仅是“换一个模型评审”，还包括**让 correctness contract 在权限和所有权上独立于被修改实现**。如果 Agent 能在失败时顺手弱化测试、更新 snapshot、抬高兼容基线，就失去了 oracle。

- **证据**：[[20260916-github-copilot-runtime-rust-migration]]
- **边界**：E2E 只保护已编码的行为契约；缺失覆盖、错误 oracle 和未知外部状态仍需要真实 rollout、人工审查与其他验证层补足。

## 自动化对齐研究循环：验证研究过程（08-28 编译新增）

Anthropic 将 Agent 验证从“检查一次输出”推进到**检查研究循环**：Claude 搜索文献、提出方法和数据、训练目标模型、测试 benchmark，再把结果带入下一轮。验证边界同时包含未见评测、通用能力保持、规模迁移和监控 Agent 对方法的预审。

**判断**：Agent 能自主改进目标，不等于改进可信；可信度来自候选生成、外推评测、能力护栏与过程监控的组合。

- **证据**：[[20260828-automated-researchers-alignment-failures]]；在 10 类 alignment failure 上逐类迭代，最佳方法通过未见 benchmark、Petri 和最多约 4.7 倍规模模型测试。
- **边界**：这套验证链仍依赖公开 benchmark、有限的能力集合和可监控的行为轨迹；它不能证明未测失败、长期 RL 后的保持性或真实部署中的安全。

## 异构验证与保障对象转移（07-28 扩展）

两篇同窗口来源（GitHub 2026-07-27 / Berkeley RDI 2026-07-26）从实践和理论两侧扩展了验证命题：

**实践侧：Rubber Duck 跨模型评审**（GitHub Copilot 机制）：请求**不同模型家族**审查实现——用 GPT 5.6 Terra 写的代码请 Sonnet 审查。原理：不同训练数据 → 不同盲点，单模型自审是盲点自洽。可与 Autopilot 组合成循环，直到双方同意只剩边际收益。这是异构验证的轻量工业形态。

**理论侧：保障对象从产物转移到 agent**（Berkeley position paper）：

> **CORE RISK**：当同一个 agent 既写实现又写测试，通过测试只证明**一致性**，不证明**正确性**。

自治 agent 会同时生成实现、测试、文档和理由——创造跨越所有"互相验证的产物"的**关联失败**。因此验证软件产物不再足够，还必须审计产出它的 agent（规格、技能、记忆、决策溯源、执行轨迹）。独立验证者 agent 只有在具备**真正独立的目标**、可信的评估机制、有原则的分歧解决协议时才有效。

**两侧配对的关键张力**：跨模型家族评审只是**训练数据级独立**——完整论文给出两个具体失败机制：verifier 与 generator 可能 **talk past each other**（互不理解、无法收敛），或 **co-adapt**（共同适应，直到测试仅仅背书实现的 bug）。这正是"不同模型家族不同盲点"不够的原因：Berkeley 要求的是**目标级独立**。Rubber duck 降低了自洽盲区风险，但未满足完全独立验证的条件——自治程度越高（[[Software-Development-Autonomy-Levels|Level II/III]]），这一缺口越致命。

## 科学域验证：四个细化命题（07-29 编译新增）

OpenAI 科学计算 field report（[[20260728-openai-scientific-computing-field-report.pdf]] 八案一手案例）在最严格正确性要求下（微妙数值错误即改变科学结论）压力测试了验证命题：

1. **plausible ≠ correct**：编译通过 + "看起来合理"的输出只是极弱证据。实际观察到的微妙错误：被改的数值默认值、不当的内存分配/流式行为、静默跳过的 case——"输出貌似合理但微妙错误"
2. **验证 harness 自身是错误来源**：HelixForge 中，下采样导致的假阳性 strand-balance 审计让 agent 去修改本来正确的 GPU 实现——人类审查需同时在两层：重写本身 + 验证 harness（后者常由 agent 辅助设计）
3. **真实数据不可替代**：RustQC 边缘 case 只在真实公开测序数据的真实规模显现（最小数据集不够）；hifiasm 在真实人类 reads 上的加速小于合成 benchmark——性能增益随数据集衰减
4. **技术正确性 vs 概念正确性**：agent 能提出并评估优化假设，但"下一步把优化压力投向哪里、尝试哪个高层策略"仍需人类反复决定——人类判断同时保证 technical correctness 与 conceptual correctness

佐证：agent "出错时照样表达自信"（七案贡献者均为成功的主要裁决者）；HI.SIM 是唯一近自主案例，恰因其验收目标是字节级一致（可验证性极强）——自主程度由可验证性决定，见 [[Grindability-vs-Verifiability]] 域边界节。

## 形式验证镜像：验证器独立性与新鲜度（08-01 编译）

Lean kernel soundness bug #14576 事后分析（[[20260801-lean-kernel-soundness-bug-postmortem]]）在正确性保证最强的领域（数学证明检查，字节级判定）压力测试了验证命题，并把上文的独立性框架精确化：

| 独立性层级 | Agent 域实例 | 形式验证域对应 |
|-----------|-------------|---------------|
| 训练数据级 | 跨模型家族 rubber duck 评审 | —（同一实现的不同视角，独立性最弱） |
| 实现级 | — | Lean kernel vs nanoda（不同语言、不同团队的独立实现） |
| 目标级 | 具备真正独立目标的验证者 agent | lean4lean（kernel 实现其类型理论的**形式化证明**） |

三个新命题：

1. **独立性是结构属性，新鲜度是运维属性，缺一不可**：exploit 同时骗过 Lean kernel 与 nanoda，因为两个不相关 bug 恰好对齐——独立检查*机制*依然成立（攻破需两个独立实现各有一个不同 bug），但 nanoda 的 bug 早一周已修复，**持有旧版本的独立检查等于没有独立检查**。"users who rely on it need current versions of both"——异构验证必须配套版本跟踪（comparator.live 每日同步 nanoda 上游）。
2. **bug 独立性可能被信息渠道侵蚀**：无法排除 AI 模型见过 nanoda 的公开 bug 报告后定向构造 exploit。若攻击方能系统性 harvest 多个检查器的公开缺陷，独立性假设退化为"未公开 bug 的独立性"——这与 co-adapt 机制（verifier 与 generator 共同适应）在结构上同源。
3. **enforcement point 必须独立于不可信组件**："健全性不能依赖不可信组件拒绝构造坏项，kernel 必须在自己的进程内独立拒绝 ill-typed 声明"——与 agent 域"containment 不能依赖模型自我克制、护栏必须由 [[Agent-Harness]] 独立执行"是同一条信任边界原则。"移除 metaprogramming 防攻击"等同于"靠 prompt 约束模型"——把安全寄托在不可信组件的自我克制上。

## 前提与局限性

- **依赖工具使用能力**: Agent 必须能访问运行环境（terminal、simulator、browser），无法访问时 verification 仍然是外部的
- **内部案例为主**: 当前最佳实践来自 Anthropic 内部，外部企业是否同样适用存疑
- **需要 skill 支撑**: 复杂验证（如 desktop app 测试）需要专门的 skill 教 agent 如何操作

## 补丁与验证管线的双重边界（2026-09）

**判断**：验证对象既包括修复是否有效，也包括 benchmark、selector 和评分器自身是否可靠；exploit blocked、CI green 或模型裁判一致，单独都不足以证明修复成立。

- **证据**：[[20260915-trail-of-bits-1password-ai-patching-benchmark]]、[[20260914-anthropic-test-impact-analysis-ci]]、[[20260915-intelligent-artifact-code-review-model-routing]]。
- **边界**：Trail of Bits 数据来自项目方复盘；Anthropic 数据来自内部工程实践；Intelligent Artifact 使用厂商基准，均不能替代跨项目、独立复现。

## Agent 构建 verifier：把“够用的生成”关进独立验证轨道

Trail of Bits 的 Miden 审计把 Agent Verification 往前推进了一层：Agent 不只接受 verifier 检查，也可以帮助构建 LSP、decompiler、静态分析器和 Lean 模型，把原本隐式、难审计的语义转换成可执行的验证对象。

**判断**：Agent 构建 verifier 可以扩大可验证边界，但前提是 correctness contract 最终由独立于生成器的确定性语义、回归 oracle 或 proof kernel 承担；“Agent 写了验证器且验证器通过”本身仍不足以自证正确。
- **证据**：[[20260918-trailofbits-auditing-good-enough-ai]]；decompiler 用随机 procedure 做回归，静态分析基于中间表示与抽象解释，Lean kernel 检查 Agent 生成的 95 个 correctness proofs。
- **边界**：这是 Miden zkVM 的单一高保证案例；Agent 生成的分析器、翻译器与 theorem statement 仍需人工或独立机制审查，不能把 proof kernel 的可靠性外推到整个工具链。

## 关联概念

- [[Claude-Code-CLI]] — Agent verification 的主要载体
- [[Agent-Loops]] — Verification 是 loop 的核心环节
- [[Auto-Mode]] — Auto mode 让 verification 循环可以无人值守运行
- [[Validation-Pipeline]] — 系统化验证管线：对抗审查 + e2e 测试 + 证据生成 + PR babysitting
- [[Captain-Mindset]] — 验证能力的组织意义：人类从审 diff 转向看证据
- [[Software-Development-Autonomy-Levels]] — 自治级别越高，保障对象越从产物转向 agent（CORE RISK：一致性 ≠ 正确性）
