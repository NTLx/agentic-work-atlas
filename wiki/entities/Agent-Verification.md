---
type: entity
title: Agent Verification
aliases:
  - Agent 自主验证
  - Agentic Verification
definition: "Agent 能自主运行验证循环的能力——不是 lint/type check，而是 agent 能自己启动测试环境、执行操作、观察结果并判断是否通过"
created: 2026-06-12
updated: 2026-10-22
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
  - "[[20260917-tessl-ai-agent-evaluation-evidence]]"
  - "[[20260914-iouri-khramtsov-ai-code-quality]]"
  - "[[20260928-github-android-ai-security-agent]]"
  - "[[20260929-pragmatic-shopify-native-mobile]]"
  - "[[20260930-openrouter-agent-regression-testing]]"
  - "[[20261014-google-deep-review]]"
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

## 多信号证据环：coverage 不是 confidence

Tessl 的 S3-compatible storage 实践说明，测试只有在 oracle、风险选择和可观测性可信时才构成证据。追求 100% statement coverage 时，Agent 会生成能抬高数字却不增加信心的 trivial tests；相反，真实 S3 behavior、edge cases、flaky-test discipline、trace、security review 与 type constraints 共同缩小错误空间。

**判断**：生产级 Agent verification 应优化“证据组合的判别力”，而不是最大化某个容易被优化的代理指标。
- **证据**：[[20260917-tessl-ai-agent-evaluation-evidence]]；约 1,500 个 S3 behavior tests、约 5,000 tests/2 分钟，以及作者对 coverage gaming、rare-bug reproduction 和 type-enforced authorization 的复盘。
- **边界**：S3 复制任务天然拥有外部 reference behavior；原创产品、开放研究和不可观测状态没有同等强的 oracle，不能直接照搬这一验证结构。

## Verification 是证据组合，不是单一测试层（2026-10）

Iouri Khramtsov 的七层 AI coding 质量实践（[[20260914-iouri-khramtsov-ai-code-quality]]）提供了一个轻量但完整的工程视角：requirements review、unit tests、manual testing、E2E、专项 AI review、PR review 和 production monitoring 分别覆盖不同错误空间。

**判断**：当 Agent 生成成本下降时，verification 的正确扩展方向不是把某个 proxy（例如 coverage 或 reviewer 数量）推到极致，而是增加**异质证据层**，让同一个错误更难同时逃逸。

- **证据**：[[20260914-iouri-khramtsov-ai-code-quality]]；作者把质量防线从实现前的 requirements review 一直延伸到部署后的 monitoring / diagnosis。
- **边界**：流程层数不等于独立性。若 requirements、tests、implementation 和 review 全由同一错误假设驱动，它们仍可能共源失败；>95% coverage 也不能替代 risk-directed tests、manual exploration 与生产证据。

这与本页既有“保护 Oracle”“多信号证据环”形成同一结论：**coverage、CI green、AI review、人类 review、真实运行信号的价值来自互补，而不是数量本身**。对于简单且后果有限的变更，人类 review 可以按风险降级；对于权限、安全、数据、计费等高后果边界，即使 diff 很小也不能用“其他自动层都通过”替代责任判断。

## 双实现、共享 Oracle：把 shared code 迁成 shared contract（2026-10）

Shopify 从 React Native 转回 Swift/Kotlin 的公开案例（[[20260929-pragmatic-shopify-native-mobile]]）给“保护 Oracle”增加了一个架构层实例：Agent 可以把 feature 从 iOS port 到 Android、反向 port，也可以持续比较两套实现；但 Shopify 同时建立一套 shared test suite，让 Swift 与 Kotlin 的 business logic 必须通过同一个 behavioral contract，而且测试可 headless 在 desktop 快速运行。

~~~text
shared behavioral contract
       ↙       ↘
Swift impl     Kotlin impl
       ↘       ↙
 same headless tests
        ↓
release gate
~~~

**判断**：Agent 降低 duplicated implementation cost 后，系统未必还需要共享生产代码，但更需要共享、受保护的 correctness contract。换句话说，**AI 可以把 reuse boundary 从 implementation reuse 推向 specification / oracle reuse**。

这也是一种更强的异构验证：两份平台实现不是逐行相同，也不应要求相同；真正需要保持的是 externally observable business semantics。只要 oracle 独立于某一实现，Agent 就可以自由利用 Swift/Kotlin 各自的平台能力，而不把 parity 退化为人工 diff。

- **证据**：[[20260929-pragmatic-shopify-native-mobile]]，公开第 3 节 “Shared codebases more trivial with AI”；Shopify 第一方工程文章亦描述 shared specifications/tests/review checkpoints 与 agent-friendly headless business logic。
- **边界**：共享 tests 只验证已编码的语义，无法自动覆盖 accessibility、visual behavior、platform integration、performance 或未知 edge cases；同一套错误 specification 仍可能让两份实现一起“正确地错”。因此 shared oracle 是 parity foundation，不是完整质量证明。

## Agent 回归测试：锁定 behavioral contract，而不是字符串输出（2026-10）

OpenRouter 的 Agent regression 教程（[[20260930-openrouter-agent-regression-testing]]）把 verification 从“检查输出是否通过”推进到**控制一个 Agent behavior experiment**。Agent 的被测系统不是 prompt 一项，而是完整 execution envelope：

```text
Behavior
= f(prompt,
    concrete model/provider,
    tool schema + tool results,
    retrieval/context,
    harness + implicit instructions,
    inference parameters)
```

因此 prompt、model、tool definition、retrieval setting、conversation history 或 workspace instruction 任一变化，都可能使旧 pass 过期。

生产级回归证据的最小实验包更接近：

```text
locked cases
+ pinned prompt
+ concrete model/provider
+ fixed tools/schema/results
+ fixed retrieval/context
+ fixed judge
+ explicit inference params
+ disclosed implicit instructions
→ baseline vs candidate
```

### Baseline-before-candidate：验证器也要先做 health check

来源强调先在当前 harness 中 replay baseline，再评价 candidate。若 baseline 与 candidate 同时在同一个 case 失败，优先调查 case、judge、harness 或 environment，而不是自动归因给候选版本。教程自己的运行甚至没有找到候选模型问题，却暴露了 harness 问题。

**判断**：baseline replay 是 verifier 的廉价 self-test。它不能证明 verifier 绝对正确，但可以识别“测试系统自身刚坏了”这一类常见假回归。

### Structural assertion、outcome 与 hard invariant 必须分层

Agent 输出通常不能做字符串 diff。来源主张检查 tool call、arguments 和 policy boundaries；结合 [[Evaluation-Set]] 既有原则，更稳妥的 contract 是：

- **outcome/rubric**：最终任务结果是否满足目标；
- **structural assertion**：只有当 tool/path/order 本身属于需求时才锁定执行路径；
- **hard invariant**：退款上限、必须升级人工等绝不能突破的边界。

**判断**：hard invariant 不应被 aggregate pass rate 稀释。soft judge drift 可以 threshold / rerun / investigate；candidate-only invariant break 则应是零容忍 release defect。

### Hermeticity 还包括隐式 instruction sources

`AGENTS.md`、`CLAUDE.md`、skills 与 workspace instructions 都可能进入上下文，因此回归环境即使 API 参数完全相同，也可能因为运行目录变化而漂移。

**判断**：Agent test hermeticity 的对象必须包含隐式上下文来源。凡是能改变模型可见信息、工具定义或决策边界的东西，都属于 test fixture，而不是“环境杂音”。

- **证据**：[[20260930-openrouter-agent-regression-testing]]，locked case set、three kinds of change、model-swap、noise/invariant 与 conclusion 段落。
- **边界**：来源是 OpenRouter/Ori Eval 教程；具体模型和价格是时间敏感示例。baseline 通过只是 sanity check，无法发现 baseline 与 verifier 的共源错误；高风险系统仍需独立 oracle 与人工审查。

## 安全研究：finding confidence ≠ severity confidence（2026-10）

GitHub Security Lab 的 Android Taskflow 实践（[[20260928-github-android-ai-security-agent]]）给 verification 增加了一个很清晰的分层反例：模型能找到真实代码弱点，甚至能组合出高影响逻辑漏洞，但它对实际 severity 的判断经常不可靠。决定漏洞是否真正成立的，可能是静态代码之外的 runtime state、storage precedence、mitigation、调用链和受影响资产。

因此安全 finding 的验证链不能压成一个“vulnerable / not vulnerable”标签：

~~~text
candidate code pattern
    ↓
reachable behavior
    ↓
working PoC / runtime evidence
    ↓
real-world impact
    ↓
severity adjudication
~~~

**判断**：生成器对前一层有较高置信度，不应自动把置信度传递给后一层。尤其是 severity，本质上是系统级 impact claim；如果只根据代码 pattern 评分，很容易把“看起来可控”误判成“现实中可利用”。

作者的补救方法是显式要求模型构造 PoC，必要时给 debugger 去运行 PoC 与原始代码，再由熟悉 mobile security 的研究者复核。这里 PoC 的作用可以抽象成 **evidence escalation primitive**：把文本推断推进到可执行反证环境。

- **证据**：[[20260928-github-android-ai-security-agent]]，“LLMs are good at finding vulnerabilities but struggle at estimating severity”。
- **边界**：PoC 仍只覆盖特定路径，测试环境也可能与真实设备/部署状态不同；成功 exploitability 证据不自动给出完整 CVSS 或业务影响。因此 human review 在这里不是礼仪性 approval，而是补足环境状态与 impact semantics 的最后 oracle。

## 长文档验证：把 review 本身做成分层 Agent pipeline（2026-10）

Google Deep Review（[[20261014-google-deep-review]]）把 Agent Verification 从软件 artifact 扩展到 knowledge artifact。它明确针对一个同构问题：生成技术内容的吞吐提高，而专家 verification capacity 没有同比增长，因此 review 成为独立的 **validation bottleneck**。

Deep Review 没有把整篇长文档交给一次 single-prompt judge，而是把验证拆成四层：

~~~text
document segmentation
      ↓
adaptive reasoning budget
      ↓
parallel section verification
      ↓
global synthesis + grounding
~~~

其中每个 specialised reviewer 聚焦一个 target segment，但仍能访问 full-document context 来处理 cross-reference；最后 synthesis agent 重新检查跨段一致性，并调用外部工具做 grounding。

**判断**：长上下文验证的核心扩展策略不是“让一个 reviewer 看更多”，而是**把验证预算显式调度到不同风险区域，同时保留全局一致性恢复层**。这与测试分片/异构证据的思路同构，但对象从 executable behavior 变成 claims、proofs、citations 和 document-level consistency。

Google 同时把 automation boundary 说得很清楚：系统承担 logical consistency、mathematical checking、fact grounding、prior-work comparison 等高认知成本检查，而 higher-level judgement 留给人类。换言之，**扩大 verification coverage 不等于转移 decision authority**。

- **证据**：[[20261014-google-deep-review]]；16,000+ opt-in pre-submission manuscripts、四阶段 pipeline、design/legal/finance 扩展与 higher-level judgement 边界。
- **边界**：16,000+ 是部署覆盖而非 correctness benchmark；PAT feedback 与正式 conference review 明确解耦。产品方没有在本文给出跨领域误报/漏报曲线，因此不能把“可规模运行”直接等同于“可独立裁决”。

## 关联概念

- [[Claude-Code-CLI]] — Agent verification 的主要载体
- [[Agent-Loops]] — Verification 是 loop 的核心环节
- [[Auto-Mode]] — Auto mode 让 verification 循环可以无人值守运行
- [[Validation-Pipeline]] — 系统化验证管线：对抗审查 + e2e 测试 + 证据生成 + PR babysitting
- [[Captain-Mindset]] — 验证能力的组织意义：人类从审 diff 转向看证据
- [[Software-Development-Autonomy-Levels]] — 自治级别越高，保障对象越从产物转向 agent（CORE RISK：一致性 ≠ 正确性）
