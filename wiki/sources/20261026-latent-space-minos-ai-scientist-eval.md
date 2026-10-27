---
type: source-summary
title: "An Eval for AI Scientists That Knows the Answer Key - Ian Quigley, Leash Bio"
source_raw:
  - "[[20261026-latent-space-minos-ai-scientist-eval]]"
canonical_url: "https://www.youtube.com/watch?v=vhPCo-8K78U"
raw_state: full
created: 2026-10-27
updated: 2026-10-27
tags:
  - source-summary
  - ai-for-science
  - scientific-discovery
  - evaluation
  - reinforcement-learning
evidence_level: medium
claim_type: mixed
source_locator:
  - "Transcript 00:01:16–00:03:15：Minos/预先测量世界、SAR 任务、100 molecule budget 与约 90,000 rollouts"
  - "Transcript 00:03:13–00:05:31：完整 measured landscape 作为 answer key；早停、重复测试、假设冲突、explore/exploit 与离开坏区域"
  - "Transcript 00:05:31–00:07:15：自然语言 SAR reasoning 的可读性、人类 medicinal chemist 的 plausibility 检查及人类基线限制"
  - "Transcript 00:07:14–00:09:02：模型排行的时点性描述；自动字幕中的模型名称存在转录歧义"
  - "Transcript 00:09:22–00:11:20：SMILES 能力变化、模型利用分子信息进行迭代决策的描述"
  - "Transcript 00:11:55–00:13:33：Minos 用于测量 scientific-agent decision making；lab-in-the-loop with amortized latency"
  - "Transcript 00:13:33–00:15:32：预测量环境的 action-space/coverage 限制、环境扩张计划与跨新 biology transfer 尚未知"
  - "Transcript 00:15:32–00:16:15：有限实验预算下的 stay/go 决策与结构化 tool calls"
---

# An Eval for AI Scientists That Knows the Answer Key - Ian Quigley, Leash Bio

> Latent Space 对 Leash Bio 联合创始人 Ian Quigley 的后续访谈。用户提供了视频元数据与完整自动生成英文 Transcript；本次以附件 Transcript 为主证据。原始附件文件 SHA256 为 `78dcf5998562998203b114356156d2dc635d0cb28339524cf602074bac2288b5`，时间轴结束于 00:16:35。由于是自动字幕，个别模型名、数字和专有名词可能误听；Leash 的规模、性能与路线图也主要属于公司一方陈述，因此按 `medium / mixed` 处理。

## 编译摘要

### 1. 浓缩

#### 核心结论 1：Minos 把“已完整测量的实验世界”从 replay 工具推进为可计算的科学决策评测环境

Leash 将此前的 replayable physical loop 进一步形式化为 Minos：先构造足够大、足够 counterfactually dense 的已测量实验环境，再把 scientific agent 放入其中，在固定实验预算下主动选择下一步实验。访谈中的 flagship 任务是结构活性关系（SAR）：Agent 只知道 target，从 catalog 中选择最多 100 个 molecule，目标是在有限预算内找到更强 binder，并用自然语言写出 SAR hypothesis、据实验结果更新后续选择（00:01:16–00:03:03）。Quigley 称这类 rollout 已达到约 90,000 次（00:03:00–00:03:15）。

**判断**：Minos 的关键不是把静态 dataset 换成聊天界面，而是保留 `state → choose experiment → observe measured result → revise hypothesis → choose next experiment` 的序贯决策结构，同时因为整个 landscape 预先测量过而拥有一个罕见的“answer key”。

#### 核心结论 2：完整 landscape 让评测从“最终得分”升级为对 scientific decision policy 的诊断

因为环境不仅知道 Agent 查询到的结果，也知道整个 measured world 的结果，Leash 可以判断 Agent 最终离全局更优区域有多远，并分析其决策轨迹。访谈列出的失败模式包括：过早放弃、发现与自身 hypothesis 不一致的 molecule、在有限预算下反复重测同一 molecule，以及 explore / exploit 分配不当（00:03:13–00:04:19）。

Quigley 报告更强模型更快离开低质量 neighborhood，而较弱模型会围绕低分 molecule 做大量细小变化、持续投入预算（00:04:17–00:05:31）。这不是关于“更聪明模型为何如此”的机制解释——他明确说团队还不知道原因——而是一个可由轨迹和完整环境共同观察到的行为差异。

**判断**：对科学 Agent，真正有价值的 eval 不只问“最后找到的答案多好”，还应测量**预算如何被花掉、何时 abandon、何时 exploit、是否重复无信息实验，以及新 evidence 是否真正改变 policy**。这比静态 benchmark 更接近实验设计能力本身。

#### 核心结论 3：Minos 将现实实验成本“摊销”为低延迟 rollout，但它仍不是实时实验室

Quigley 把这一形态称为 “lab in the loop with amortized latency”：真实实验先支付一次成本，随后同一个 measured world 可以被大量 Agent rollout 重复探索（00:12:32–00:13:33）。相比 conventional lab-in-the-loop 每一步都重新做实验，这种方法牺牲 action freedom，换取近乎软件速度的反馈和大量 counterfactual rollout。

访谈也明确承认限制：Agent 只能选择预先测过的那些实验，不能任意合成或测量全新 molecule；live loop 更自由，而 replay 环境受已测 action space 限制（00:13:33–00:14:04）。Leash 称目前大约能构造 2 个新环境/天，并计划尝试提升到约 20 个/天，但这是未来运营目标，不是已实现能力（00:14:02–00:14:34）。

#### 核心结论 4：科学 Agent 的潜在训练目标正在从“懂化学”转向“会在有限预算下做决策”

访谈强调的能力不仅是 molecule representation。Quigley 回顾，较早模型连 SMILES 转换都很弱，而后来模型开始能在 chemistry 信息上做有意义的迭代选择；当去掉 molecule 信息时，决策表现会明显下降（00:09:22–00:11:20）。但更重要的开放问题是：在有限 experimental budget 下，模型是否知道什么时候继续局部搜索、什么时候跳走，以及这种 decision skill 能否迁移到其他 scientific problems（00:15:32–00:16:01）。

**判断**：Minos 更像是把 scientific reasoning 拆成一个 budgeted sequential decision problem。若后续 RL 有价值，训练对象未必只是领域知识，而可能是 `information acquisition policy`：如何花实验预算、如何根据反馈调整搜索、如何避免把 plausibility 当成 evidence。

### 2. 质疑与证据边界

- **这是公司一手访谈，不是独立 benchmark audit。** 约 90,000 rollouts、模型间 separation、当前环境生成速度和未来 20/day 目标均来自 Quigley 的陈述；附件描述虽指向 preprint、blog、data/transcripts，但本次编译没有把这些外部材料当作额外独立证据。
- **“answer key” 只覆盖已测量世界。** Minos 可以知道 measured landscape 内的最佳/较优选择，却不能回答未测 chemical space 中是否存在更好的 molecule；因此 global optimum 是环境内 optimum，不是现实世界完整最优。
- **模型排行不宜固化。** Transcript 在 00:07:14–00:09:02 给出若干 frontier/open model 的当时表现，但自动字幕对模型名存在明显误听，而且访谈自己强调 frontier model 迭代很快。稳定知识应保留“模型族存在可分离行为差异”这一点，而不是把具体冠军作为长期结论。
- **人类 medicinal chemist 仅做有限 plausibility 检查。** 受访者称少量 chemist 看过 hypothesis，认为推理在药化上“plausible”，但没有系统的人类基准、同预算 head-to-head 或统计比较（00:05:31–00:07:15）。不能据此断言 Agent 已达到或超过专业药化师。
- **高吞吐 replay 不等于跨域 generalization。** Quigley 明确说团队尚不知道能否把这些环境中的 reinforcement-learning progress 迁移到新的 biology（00:14:52–00:15:32）。这是核心研究问题，而不是已证实结果。
- **当前任务只覆盖 binding 优化。** 访谈明确说本轮 SAR eval 暂不覆盖 metabolism 等其他 drug-like properties（00:02:00–00:02:20）；因此不能把结果外推为完整 medicinal chemistry 或 drug discovery 能力。

### 3. 对标与约束

- **与 [[20261014-latentspace-leash-bio-lab-in-the-loop]]：从环境架构推进到 evaluation contract。** 前一篇主要建立“预支付 reality cost → replayable physical experience”的机制；本篇新增的是如何利用完整 measured world 作为 answer key，诊断 Agent 的实验预算分配、exploration/exploitation、重复测试和 abandon behavior。
- **与 [[Evaluation-Set]]：从固定 case scoring 扩展为 trajectory-aware evaluation。** 普通 eval 只观察最终回答；Minos 同时记录 action sequence 和每步现实反馈，并知道环境中未被 Agent 选择的 counterfactual outcomes，因此可以评价决策过程而不只评价终点。
- **与 [[Lab-in-the-Loop]]：amortized latency 是 replayable loop 的时间经济学。** 真实实验一次性构造世界后，可以进行大量低延迟 rollout；代价是 action space 被历史 measurement coverage 限定。更完整系统仍需要 replay 与 live experiment 之间的 frontier-expansion 回路。
- **与 [[Scientific-Discovery-AI]]：scientific-agent capability 的单位可从“知识问答正确率”转向“有限预算下的信息获取与决策质量”。** 这为 AI scientist 提供了更接近真实科研资源约束的 eval 方向，但跨任务/跨 biology 的 transfer 尚未证明。

## 重要判断（Claim / Evidence / Boundary）

- **判断**：对可预先高密度测量的科学问题，最有信息量的 Agent eval 之一，是把完整 measured landscape 包装成有限预算的 sequential decision world；这样既能给 Agent 真实反馈，也能用未选择的已知结果构造反事实“answer key”，诊断其搜索策略而不只看最终分数。
  - **证据**：[[20261026-latent-space-minos-ai-scientist-eval]]（00:01:16–00:05:31；00:11:55–00:13:33）。
  - **边界**：answer key 只对已测 world 完整；环境 coverage、assay bias 与 action restriction 仍存在，且访谈未证明这种策略能力能迁移到新的 biology。

### 关联概念

- [[Lab-in-the-Loop]]
- [[Scientific-Discovery-AI]]
- [[Evaluation-Set]]
- [[Agent-Verification]]
