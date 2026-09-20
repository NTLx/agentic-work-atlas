---
type: entity
title: Recursive Self-Improvement
aliases:
  - Recursive Self-Improvement
  - 递归自我改进
  - RSI
  - AI 改 AI
definition: "AI 系统设计、训练或验证其下一代或同代继任者的能力；当这一回路达到某临界点，AI 进步速度由机器而非人类决定"
created: 2026-06-06
updated: 2026-09-20
evidence_level: medium
claim_type: mixed
tags:
  - AI-frontier
  - ai-capability
  - AI-policy
  - AI-safety
related_entities:
  - "[[Anthropic]]"
  - "[[Anthropic-Institute]]"
  - "[[Task-Horizon]]"
  - "[[Verifiability]]"
  - "[[AI-Capability-Gap]]"
  - "[[AI-Psychosis]]"
  - "[[Coding-Agents]]"
  - "[[Agentic-Engineering]]"
  - "[[Meta-Harness-Optimization]]"
  - "[[Context-Engineering]]"
  - "[[Agent-Verification]]"
  - "[[Verifiable-Agent-Engineering]]"
source_raw:
  - "[[20260604-anthropic-recursive-self-improvement]]"
  - "[[20260815-autodesign-meta-harness-optimization]]"
  - "[[20260730-jeff-dean-1-rule-building-ai]]"
  - "[[20260911-dwarkesh-recursive-self-improvement-debate]]"
  - "[[20260901-harnessevolve-reference-trajectories]]"
  - "[[20260809-hsi-hierarchical-self-improvement]]"
  - "[[20260528-harness-updating-not-harness-benefit]]"
  - "[[20260827-rethinking-harness-evolution-evaluation]]"
  - "[[20260917-dwarkesh-noam-brown-agent-swarms-rsi]]"
---

# Recursive Self-Improvement（递归自我改进）

> [!definition] 定义
> **递归自我改进 (Recursive Self-Improvement, RSI)** 指 AI 系统设计、训练或验证其下一代或同代继任者的能力。当这一回路达到某临界点，AI 进步速度由机器而非人类决定，Anthropic 在 2026-06 用 frontier 实验室一手数据公开宣告这一进程"已经发生"。

## 关键数据点

Anthropic 2026-05 一手数据：

| 指标 | 数值 | 含义 |
|------|------|------|
| Anthropic 合并代码由 Claude 写的比例 | 80%+ | AI 在改 AI 自身的代码 |
| 工程师人均合并量 vs 2024 | 8x | AI 加速 AI 工程师产出 |
| Code quality parity | 2025 末"差于人类" → 2026 中"对齐" | AI 写的代码质量进入可生产区间 |
| 任务视野（4 月翻倍） | 4 分钟 (Opus 3, 2024-03) → 12 小时 (Opus 4.6, 2026-03) | AI 能独立完成的工作块涨 180 倍 |
| 实验执行加速 | Mythos 52x vs 人类 baseline | AI 优化 AI 训练 pipeline |
| 研究判断胜率 | Mythos 64% | AI 选"哪个问题值得做"开始反超人类 |
| 员工自评生产率 | 4x | 主观体感一致 |

## 演化阶段（Anthropic 自述）

| 阶段 | 时间 | 特征 |
|------|------|------|
| 1 | 2021-2023 | 人类在笔记本上手写代码，AI 不参与 |
| 2 | 2023-2025 | Chatbot 辅助短代码片段 |
| 3 | 2025-2026 | Coding agent 独立读写整文件 |
| 4 | 今天 | Agent 跑代码、互相委派 |
| 5 | 未来 | Agent 训练下一模型（recursive 闭环） |

## 三种未来（Anthropic 框架）

1. **Stall** — 指数轨迹变成 S 曲线，算力/能量约束先到。即使能力冻在 2026 水平也已足以颠覆
2. **Compounding efficiency** — AI 开发高度自动化，人类设方向，100 人公司干 10 万人活
3. **Full recursive** — AI 设计自己的继任者，节奏由算力决定

公共子集：无论哪个 case，"verification 必须现在做"。

## 实验回路是递归改进的中间层（2026-07）

Jeff Dean 将 AlphaChip、AlphaEvolve 和模型改进归结为同一套科学方法：提出实验、实现运行实验所需的东西、评估结果，再把有效结果整合回更高层系统（42:08）。当高层目标能够被拆成子问题，而每个子问题都有足够快、可测量的评估器时，系统就能从少量人工实验转向大量自动实验。

访谈还给出一个评估器加速的案例：用神经网络近似昂贵的量子化学模拟器，声称在近似准确的前提下把验证速度提高约 300,000 倍；这让原本只能筛选少量候选的流程变成可以批量探索的实验回路。

**判断**：递归自我改进能否从愿景变成可运行能力，关键不只是模型能否生成候选，而是候选能否进入足够快、可验证、可组合的实验回路。

- **证据**：[[20260730-jeff-dean-1-rule-building-ai]]
- **边界**：300,000 倍是访谈中的案例数字，不是本文独立验证的 benchmark；评估器近似误差、分布外可靠性和人工复核成本未披露。

## 从“自动做实验”到“自动决定研究方向”（Dwarkesh 圆桌，2026-09）

Dwarkesh Patel 与 John Schulman、Beren Millidge、Charlie O’Neill 的圆桌把 RSI 的关键断点说得更具体：有清晰目标和验证器的 autoresearch 可以进入自动实验回路，但开放式研究还要求系统判断“什么问题值得做”、选择下一步实验，并在结果看似成功时检查自己。Beren 将持续的 sim-to-real gap、泛化和 continual learning 视为可能的停滞原因；John 则强调较弱的判断和 self-checking 会限制研究/工程生产率，即使模型能写出远多于人的代码。

嘉宾讨论的自动化研究员路径包括把人类研究品味蒸馏进训练、使用多步且可验证的环境、吸收部署轨迹，再用回归 benchmark 判断新模型是否真的进步。这里的验证器不是附属评测，而是把候选改动接入下一轮的入口条件。

> **判断（综合判断）**：RSI 不是单一能力开关，而是“候选生成 → 环境执行 → 验证 → 选择下一目标”的闭环。闭环越接近开放式研究，目标定义、研究品味和现实迁移越成为瓶颈。
>
> **证据**：圆桌 00:00:00–00:45:24 讨论失败情景、研究目标、自动化研究员训练、长程 RL 与 sim-to-real（见 [[20260911-dwarkesh-recursive-self-improvement-debate]]）。
>
> **边界**：这是对研究者讨论的机制归纳；圆桌没有证明某条训练路线、时间表或能力跃迁必然发生。

## 并行 test-time compute 与评估 horizon 的新约束（2026-09-17）

Noam Brown 的后续访谈补了两条与 RSI 闭环直接相关、但方向相反的约束：

1. **并行化可以加速候选搜索**：multi-agent 把原本串行的 test-time compute 分散到大量 Agent 上，以更高总 token/协调成本换取更短 wall-clock。对可分解的研究问题，这会加速“生成候选”这一段。
2. **任务 horizon 变长会拖慢可信评估**：如果 Agent 能可靠执行数周乃至数月任务，而模型发布/训练周期仍以月计，完整 horizon 的 safety/product evaluation 可能来不及在下一代系统到来前结束。

这意味着 RSI 速度不能只看 capability loop：

~~~text
candidate generation speed ↑
        ×
experiment / compute throughput
        ×
verification horizon
        ×
alignment / deployment gate
~~~

**判断**：并行 Agent 可能让“做更多实验”更快，却同时扩大“我们是否有足够时间观察完整行为”的验证债务。越接近长程自治，evaluation horizon 本身越可能成为 RSI 的限制变量。

- **证据**：[[20260917-dwarkesh-noam-brown-agent-swarms-rsi]]
- **边界**：关于未来月级任务 horizon 与发布节奏的部分是 Brown 的前瞻讨论，不是已实现生产数据；应作为风险模型而非时间预测。

## Harness 层 RSI：变更晋级不能由自身得分自证

2026 年的 harness-evolution 研究让“AI 改 AI”出现一个比模型权重更新更容易观察的中间层：模型参数保持冻结，但 prompts、skills、tools、memory、execution logic 以及负责修改这些对象的 evolver 可以持续变化。[[20260901-harnessevolve-reference-trajectories]]、[[20260809-hsi-hierarchical-self-improvement]]、[[20260528-harness-updating-not-harness-benefit]] 与 [[20260827-rethinking-harness-evolution-evaluation]] 共同说明，**“系统能写出下一版”不能直接证明“下一版拥有更高、可复用且可安全部署的能力”。**

### 两个不可互相替代的晋级边界

1. **变更归因**
   - 必须区分 change producer、被修改 artifact、实际 runtime activation、adherence 与最终 outcome。
   - HarnessEvolve 将 execution / evaluation / optimization / gating 拆开；HSI 将 task harness / evolver strategy / frozen outer anchor 分层；Harness Updating Is Not Harness Benefit 则直接证明“会产生有用更新”与“执行 Agent 能从更新获益”是两个不同能力。
   - 因此版本存在不等于版本被实际使用，版本被加载也不等于 Agent 持续遵循。

2. **反馈与控制不对称**
   - 被改对象不能同时自由定义自己的 reference、reward、selector 和安全通过条件。
   - Rethinking the Evaluation 在 matched feedback / inference budget 下加入 parallel sampling、sequential refinement 等搜索基线，并使用 disjoint held-out tasks；其结果表明，部分 benchmark 提升可以由额外搜索和同 benchmark 选择解释，而不是持久 harness 能力。
   - HarnessEvolve 的质量门、近期 batch 回归门和 validation snapshot，HSI 的 frozen outer anchor 与 held-out split 都提高了归因质量，但仍不是不可改写的独立安全控制面。

### 三个结果必须分开

~~~text
candidate score ↑
      ≠
reusable capability ↑
      ≠
safe deployment ↑
~~~

- **candidate score**：首先要排除额外 search budget / 多次采样 / benchmark reuse 的贡献。
- **reusable capability**：需要 disjoint held-out tasks，并追踪 artifact activation / adherence，而不是只看最终分数。
- **safe deployment**：还需要独立安全复评、policy freeze、canary、rollback 与 rollback 后行为验证；当前四篇研究都没有闭合这一生产级链条。

因此 EX-007 当前最小审计链可写成：

~~~text
change hash / owner
  → feedback provenance
  → independent acceptance
  → matched-search delta
  → held-out behavior
  → safety canary
  → rollback / recovery result
~~~

**判断（综合）**：harness 层 RSI 的关键不是“是否允许系统自改”，而是每次自改能否在**不让被测对象同时控制反馈和晋级标准**的条件下，被归因、复验、部署和撤回。这里的“不对称”是工程治理条件，不是新的独立安全定理。

- **证据**：[[20260901-harnessevolve-reference-trajectories]]；[[20260809-hsi-hierarchical-self-improvement]]；[[20260528-harness-updating-not-harness-benefit]]；[[20260827-rethinking-harness-evolution-evaluation]]
- **边界**：上述来源主要是 benchmark / experimental self-evolution。当前仍缺生产 Agent fleet 上将 change hash、evaluator version、全部反馈查询、canary、线上行为、rollback 与 post-rollback verification 绑定到同一版本的纵向证据。

## 前提与局限性
- **80% ≠ 100%** — 80% 是 commit-level 不是 deploy-level；merge 不等于 production
- **Code quality parity 是评估侧** — 内部评审打分，主观度未披露
- **任务视野是软件类任务** — 不能直接外推到物理实验、销售谈判
- **Mythos Preview 是未公开** — 公开复现性缺
- **Verifiable pause 难** — 作者自承 training run 比导弹井更易隐藏

## 关联概念
| 本库主题 | RSI 的连接 |
|---------|------------|
| [[Task-Horizon]] | 4 分钟 → 12 小时可作为长程执行能力变化的一项外显指标 |
| [[Verifiability]] | "verifiable pause" 是 RSI 时代的协调机制提议 |
| [[AI-Capability-Gap]] | 80% / 8x / parity 数据校准能力感知 |
| [[AI-Psychosis]] | 一手数据可校准深度用户与外行的认知鸿沟 |
| [[Allocation-Economy]] | 工程师 8x 但团队规模不变 → R&D 成本结构重写 |
| [[AI-Labor-Bottleneck-Shift]] | 瓶颈从"生产代码"迁到"验证 + 集成 + 部署" |

## 前提与局限性
1. **数据来自单一机构** — Anthropic 是工具链、人才、评测集都在极端右尾的 frontier lab；外推到中位公司前必须打折
2. **作者把对齐放在脚注** — "机构克制"是有意为之，让监管者读起来觉得"他们在自我反思"，让算力扩张派读出来"反正还是要扩"
3. **代际对齐漂移** — 当 AI 输出被用来训练下一代，对齐问题从"单代"变成"代际 compounding"；脚注低估了这个放大

## 关联概念
- [[Anthropic]] — 一手数据提供方
- [[Anthropic-Institute]] — 政策发布平台
- Marina-Favaro — 主笔
- Jack-Clark — 联合署名 + 编辑支持
