---
type: source-summary
title: "Solving Open Research Problems Together"
canonical_url: "https://research.meta.ai/blog/solving-open-research-problems-together"
raw_state: index
original_raw_file: "20261002-meta-solving-open-research-problems-together.md"
original_body_sha256: "75a7d38cf76837ef8952d08cf26911c564ab628298eefe072721ee083a0f1e7b"
indexed_at: "2026-10-20T23:48:34+08:00"
created: 2026-10-20
updated: 2026-10-20
tags:
  - source-summary
  - ai-in-mathematics
  - scientific-discovery
  - human-ai-collaboration
  - research-verification
evidence_level: medium
claim_type: mixed
source_locator:
  - "开篇至 collaboration principles：Olympiad benchmark 与 open research 的区别；Muse Spark 1.1/1.2；无 custom research scaffold；研究者主导、第二组数学家复核、AI/人类撰写标记与 prior-work attribution"
  - "Probability：Gaussian ellipsoid fitting sharp threshold；三项 2026-08 concurrent independent work"
  - "Differential Equations：mass-critical biharmonic NLS radial negative-energy finite-time blow-up"
  - "Group Theory：order-384 counterexample；Muse Spark 生成 GAP 搜索程序；Nilradical concurrent counterexample"
  - "Optimization：probabilistic reframing、counterexample 与 proof strategy"
  - "Arithmetic Physics：number theory × p-adic string theory connection；candidate proofs 与 technical drafting"
  - "Non-Associative Algebra：three-dimensional counterexample、alternative characterization；independent Hu/Wen work"
  - "Building on this work：expert-AI collaboration、verification、production transparency 与 community communication"
---

# Solving Open Research Problems Together

> Meta AI Research 于 2026-10-02 发布的官方项目总结，报告数学家使用 Muse Spark 1.1/1.2 Thinking Mode 与常规 meta.ai 对话界面合作完成六篇论文，并称其中五篇回答了此前开放的研究问题。来源适合支持“Meta 如何组织这组人机数学研究、AI 在不同论文中承担了哪些工作、Meta 自己如何描述结果”的事实；对论文数学正确性、优先权和能力泛化的判断仍需分别回到论文与独立同行验证，因此按 mixed / medium evidence 处理。

## 编译摘要

### 1. 浓缩

- **核心结论 1：这次跨越的不是“更难 benchmark”，而是从有答案的竞赛题进入没有 answer key 的开放研究。**
  - Meta 明确把 Olympiad 任务与 open research 区分：竞赛题即使困难，也预先存在解；开放问题没有保证可解的方法，研究过程需要反复尝试、犯新错误、回退甚至重新开始。
  - 团队称数学家只通过常规 meta.ai chat 使用 Muse Spark 1.1/1.2 Thinking Mode，没有额外定制 research scaffold。这个事实如果按来源成立，说明至少在这组案例中，研究增量不依赖一个公开描述的复杂 Agent harness。

- **核心结论 2：最重要的系统边界不是“AI 独立研究”，而是一个有明确角色分工的人机 research production loop。**
  - Meta 给出的统一流程是：数学家选择/引导问题并与 Muse Spark 探索论证 → 第二组数学家复核 → 论文标注哪些段落主要由研究者或 AI 起草 → 明确引用先前工作。
  - 六个案例中 AI 的角色并不相同：有时帮助推导与修订 proof，有时生成 GAP 搜索程序找反例，有时把问题重构为概率表述，有时提出跨领域连接、candidate proofs 或 technical sections。更稳妥的抽象因此是 **AI 作为 research collaborator / search-and-draft substrate**，而不是单一“自动定理证明器”。

- **核心结论 3：Meta 声称六篇论文中五篇给出了此前开放问题的答案，但这一 headline 不能直接升级为“五个问题由 Muse Spark 独立解决”。**
  - 例如 differential-equation 案例中，Dinh 选择问题和关键 proof ideas，Muse Spark 帮助计算、测试论证和修订；group-theory 案例中，AI 生成 GAP 搜索程序找到 counterexample，随后由研究者验证并完成 argument；arithmetic-physics 案例中，AI 帮助识别连接并生成 candidate proofs/technical drafts，研究者检查、纠错和完善。
  - 因而成果归因应落在**协作轨迹**上：问题选择、假设/搜索、工具代码、proof construction、verification、writing 与 final responsibility 可能由不同主体承担。

- **核心结论 4：开放研究 benchmark 的另一个难点是 priority 与 independent rediscovery，而不仅是 correctness。**
  - Meta 主动披露：Gaussian ellipsoid fitting 在其工作完成后发现 2026-08 已有三组独立 concurrent work；semiabelian group conjecture 在 2026-09-16 有 Nilradical 报告不同 counterexample；evolution algebra 也有 Hu/Wen 独立 counterexamples。
  - 这说明当 AI 加速多个团队并行探索后，“是否正确”“是否独立得到”“谁先公开”“是否同一方法”“是否提供更一般结果”会成为不同的 provenance 维度。单纯统计 solved/open-problem count 会丢掉这些研究信用与知识增量差异。

- **核心结论 5：Meta 的协作协议把 verification 与 production transparency 放在能力展示本身旁边。**
  - 第二组数学家独立检查、论文级 AI/human drafting attribution、prior-work citation 与 concurrent-work acknowledgment，都是让产物进入研究共同体而不是停留在模型 demo 的治理机制。
  - 这与本库已有的数学 AI 证据形成连续链：形式或数学正确性是必要门槛，但学术价值还包括能否被检查、解释、归因和继续构建。

### 2. 质疑与边界

- **这是 Meta 对自身合作项目的一手公告，不是六篇论文正确性的独立 meta-review。** “五篇回答此前开放问题”应保留为发行方 claim；如果要把单篇结论升级为稳定数学事实，应分别检查论文、proof、review status 与后续社区反馈。
- **“无 custom research scaffold”不能推出“scaffold 对开放研究不重要”。** 页面只说明这些具体合作通过常规 meta.ai chat 完成；数学家在对话外如何保存状态、筛选分支、调用数学软件、整理文献或人工推进没有被系统量化。
- **参与者筛选与问题选择高度重要。** 页面没有给出失败项目总数、尝试过但未成文的问题、interaction count、token/compute、研究者投入工时或相对 human-only baseline，因此无法估计真实 success rate 或 productivity multiplier。
- **第二组数学家复核不等于正式同行评审。** 它提升可信度，但不能替代期刊/会议审稿、社区复现或长时间错误发现。
- **concurrent solution 使“开放问题求解数量”成为不稳定指标。** 同一问题可能在相近时间被多个团队独立解决，而且结果的普适性、方法价值与公开时间不同；能力评价需要区分 rediscovery、first public solution、independent confirmation 与 stronger theorem。
- **从数学外推到一般 science 需谨慎。** 数学对象具有强可验证结构，很多中间产物能由 proof checking、symbolic tools 或专家 inspection 复核；物理/生物研究还要面对测量噪声、实验成本与真实世界反馈延迟。

### 3. 对标与约束

- **与 [[AI-in-Mathematics]]：从竞赛成绩进入开放问题，但能力单位从“单模型解题”变成“human-AI research system”。** 早期能力讨论更关注 Olympiad、反例发现和自动证明；这批案例新增的是 multi-stage research contribution：reframing、program synthesis、counterexample search、proof revision、cross-domain connection 与 technical drafting。评价对象应从 final answer 扩展到完整 provenance trace。
- **与 [[20260918-terence-tao-if-math-more-than-proof]]：proof production 与 mathematical understanding 仍需分开。** Sanderson/Tao 线索强调 AI proof 之后还有 motivation、exposition、canonicalization 的工作；Meta 这次也把目标写成帮助研究者发展“others can understand and build on”的 insight，并通过研究者复核和标注主要起草主体来保留解释与责任链。两者共同反对把“生成一个 proof artifact”直接等价为“共同体已经吸收了新数学”。
- **与 [[Human-Curation]]：人类角色不只是最后点击 accept。** 问题选择、关键 proof idea、检查错误、修订 argument、确认 prior art、决定如何写进论文，都属于高价值 judgment；来源没有证据表明这些环节已被模型替代。
- **与 [[Scientific-Discovery-AI]]：数学展示了低物理反馈成本的 open-research 路线。** 与 [[Lab-in-the-Loop]] 的真实实验环境不同，数学中的候选 idea/proof 可以通过专家推导、软件搜索与 proof checking 快速迭代，因此更接近“开放式 computational research + human verification”。这说明 Scientific Discovery AI 不必只有 laboratory loop，也可以在可形式化/可审计的符号领域先形成高带宽研究闭环。

## 当前稳定判断

**判断**：Meta 这批 Muse Spark 合作最有价值的信号，不是一个新的“AI solved N open problems”排行榜，而是**开放研究正在出现可审计的人机共同生产协议**：专家负责问题 framing 与科学责任，模型扩大 search / derivation / coding / drafting surface，独立专家复核正确性，论文保留 AI-human attribution 与 prior-art provenance。

- **证据**：Meta AI Research《Solving Open Research Problems Together》，尤其是开篇 collaboration principles 与六个案例中的具体角色描述。
- **边界**：来源未公开 denominator、human-only baseline、interaction/compute cost，也不是独立 correctness audit；因此它支持“这种协作机制已产出论文级结果”，但不足以证明 Muse Spark 已具备自主开放数学研究能力或相对数学家的净 productivity multiplier。

## 关联概念

- [[AI-in-Mathematics]]
- [[Scientific-Discovery-AI]]
- [[Human-Curation]]
- [[Proof-Indigestion]]
- [[Mathematical-Canonicalization]]
- [[Agent-Verification]]
