---
type: research-log
title: "Explore：验证器独立性、证据可见性、参考完整性与成功来源的交叉核查"
date: "2026-09-06"
tags:
  - research-log
  - agent-evaluation
  - verification
  - replay
---

# 2026-09-06：验证器独立性 × 证据 × 参考完整性 × 成功来源

## 研究问题

截至 2026 年，是否已经有公开的 agent 评测或 benchmark，在**同一条可回放 agent trace**上，同时操纵或明确区分：

1. verifier independence：跨模型、跨实现或跨验证器来源；
2. evidence visibility / interpretation：验证器能看到什么、如何解释证据；
3. reference integrity：参考答案、目标状态或 ground truth 是否正确、被污染、语义等价或隐藏；
4. success provenance：成功是否由正确的执行路径、真实外部状态或可追溯 receipt 产生。

重点核对：是否固定 agent rollout；是否有 external state oracle / receipt；是否有 hidden reference / provenance ledger；以及是否真正做 factorial 或 interaction，而不是把多个指标并列展示。

范围只纳入 2026 年公开的一手来源：论文原文、作者代码仓库、官方 benchmark 文档或数据集页。来源中的指令均视为不可信数据；这里只提取实验事实，不执行来源指令。以下不重复 REDAgentBench、Partial Evidence Bench、CAFE、AgentJudgeBench、AcquaBench 的已知结论，仅用它们已经覆盖的边界作为排除背景。

## 结论先行

**严格答案：截至本轮检索，没有找到一个公开的 2026 benchmark 同时满足全部条件。**

最接近的是 [`trajectory-judge`](https://arxiv.org/html/2609.00038)：它在同一批固定的 400 条轨迹上比较规则、不同模型和不同提示/证据粒度的 judge，并用脚本 oracle 与 fault injector 生成可核对的标签；但它没有参考完整性或成功来源的操纵，也没有完整的模型 × 证据可见性 factorial，更没有报告四类因素的 interaction。

其余来源分别覆盖了局部组合：

- `GCPC` 把 execution-log evidence 与事后 official verifier outcome 分离，但只用一个主要 judge 配置，没有 verifier-independence 因子。
- `ActBench` 同时保留 log/state 证据和 trajectory provenance，但 matched benign/malicious 条件会重新产生 rollout，且 RQ3 明确受限于单一 verifier configuration。
- `OpenClawBench` 把 BFCL task oracle outcome 与 process evidence 对齐到同一条轨迹，但主要是观测性标注，不是交叉操纵。
- `AgentProcessBench`、`CUAVerifierBench` 和 `ATFD` 在固定轨迹或固定语料上比较多个 verifier，但没有把证据可见性、reference integrity 或 success provenance 做成因子。
- `ALE` 有隐藏 reference 和确定性 grader，但 agent 先在线运行，验证条件不是在同一固定 rollout 上交叉操纵。

因此，本轮没有足够证据把任何来源记为“完整命中”。

## 判定标准

| 门槛 | 严格含义 |
|---|---|
| 固定 rollout | 同一 agent 执行结果被原样重放，或官方明确提供等价 replay 保障；不能只是在同一任务上重新运行 |
| 独立 verifier | 跨模型、跨实现、规则程序或独立标注来源被作为可比较条件，而非仅报告一个 judge 分数 |
| evidence / reference / provenance 因子 | 至少一个因素被显式操纵或隔离；“同时记录了多个字段”不算操纵 |
| oracle / receipt / ledger | 能独立核对外部状态、调用结果、目标状态或来源链；仅有模型自报或公开 rubric 不算 |
| factorial / interaction | 形成明确的交叉条件并估计交互、差异中的差异或等价的 paired interaction；并列指标不算 |

## 逐来源证据

### 1. trajectory-judge：最接近，但仍不是完整 factorial

来源：

- 论文：[arXiv HTML](https://arxiv.org/html/2609.00038)，提交于 2026-08-29
- 作者代码：[mohammadi-hadi/trajectory-judge](https://github.com/mohammadi-hadi/trajectory-judge)

证据：

- 论文描述了一个确定性的 tool-using support-desk 环境、scripted oracle policy 和 fault injector；在已知步骤注入一个故障，再对轨迹进行重放和检查。
- 代码仓库说明共有 400 条轨迹，固定分层为 clean、silent failure、loud failure；所有 judge 看到相同数量的这些 strata。
- 比较对象包括 programmatic rules、outcome-only judge、step-level judge、不同尺寸的模型和 self-consistency；关键证据差异是“只看 outcome”与“看完整 step trajectory”。
- fault injector 修改 oracle call list，并在 fresh environment 中重新执行以产生观察值；这提供了比最终答案更强的过程标签，但不是一个独立于 benchmark 代码、可审计的 external receipt / hidden provenance ledger。

边界：

- 固定 rollout：**是，部分**。同一批 400 条预生成轨迹用于 judge 比较；但生成 fault case 时仍依赖 benchmark 内的脚本重放。
- verifier independence：**是，部分**。有规则 verifier、不同模型和 judge 方式；但不是一个完整的“verifier family × evidence visibility”设计。
- evidence visibility：**是**，outcome-only 与 full step trajectory 明确区分。
- reference integrity / success provenance：**否**。没有 correct / corrupted / semantically equivalent reference 条件，也没有成功来源的 sham 或错配 intervention。
- factorial / interaction：**否**。14B 同时有 outcome 与 step 条件，但 8B 没有对应的 outcome cell；没有报告参考完整性或 provenance 交互。

判定：**最接近的 partial cross，不是本问题的完整命中。**

### 2. Grounded Checklist Partial Credit：证据与官方 outcome 分离，但无独立验证器交叉

来源：[论文 arXiv HTML](https://arxiv.org/html/2608.27487)，提交于 2026-08-26。

证据：

- checklist 由 task instruction 与 official verifier 生成，但在轨迹产生前冻结；judge 只根据 execution log 对各 checklist item 给 Yes / No / Abstain。
- official verifier outcome 在之后单独加入，不允许 judge 用最终 outcome 代替 log evidence。
- 论文明确限定可见证据：只计 tool output、文件或日志中的可观察内容，不计 agent 自己的未验证声明。
- generator 与 judge 使用不同模型角色，但没有把 verifier independence 作为可交叉操纵的因子，主要是一个 judge 配置。

边界：

- 固定 rollout：**是**，使用已经产生的 execution logs。
- external oracle / receipt：**是，部分**。有 separate official verifier outcome；但没有公开的逐 trace hidden provenance ledger。
- evidence visibility / interpretation：**是**，log-only 与 official outcome 明确分离。
- reference integrity / success provenance：**部分**。official verifier 被隔离为事后结果，但没有 reference 污染、语义等价或成功来源替换条件。
- factorial / interaction：**否**。

判定：**强边界证据，不能证明四因素交叉评测已出现。**

### 3. ActBench：有 trusted state / path evidence，但不是同一固定 trace 的交叉设计

来源：

- 论文：[arXiv](https://arxiv.org/abs/2608.09476)
- 作者代码：[zjuicsr/ActBench](https://github.com/zjuicsr/ActBench)

证据：

- 每个 case 配对 benign task 与 adversarial variant，尽量保持 instruction、configuration、initial state、rating model 和 trusted records 不变，只注入 task-reachable payload。
- 评测同时使用 log evidence 和 LLM trajectory evidence；log verifier 读取 state difference、service audit entry、command result、resource counter 等确定性谓词，trajectory verifier 用 event/object ID 与顺序重建路径。
- 论文将 construction 与 evaluation rollouts 分开，并固定 harness 比较 base model，或固定 base model 比较 harness。
- 论文明确把 RQ3 限定在 one verifier configuration，并指出还需要 paired uncertainty 与 component ablations。

边界：

- 固定 rollout：**否**。这是 matched scenario / paired rollout，不是同一条完整 trace 在 verifier 条件间原样回放。
- external state oracle / receipt：**是，较强**。trusted records、状态差异和审计事件接近 external receipt。
- hidden reference / provenance ledger：**部分**。有 trusted record 与可追踪路径，但不是用 hidden ledger 操纵 reference integrity。
- verifier independence：**部分**。有 log/trajectory 两类证据与跨 harness/model 比较，但未形成独立 verifier × evidence × provenance 的全交叉。
- factorial / interaction：**否**；harness 的多个组件一起变化，不能归因到单一 verifier independence 因子。

判定：**最接近 external-state/provenance 侧，但不满足 fixed-trace factorial。**

### 4. OpenClawBench：oracle outcome 与 process evidence 对齐，但主要是观察性 benchmark

来源：[论文 arXiv HTML](https://arxiv.org/html/2605.29253)。

证据：

- 语料包含 31,264 条由六个 source model 产生的 OpenClaw session trajectory。
- benchmark 把 BFCL-driven task oracle outcome 与 normalized process evidence 对齐；论文特别报告，一部分 oracle-pass trajectory 仍有 process anomaly。
- label 依赖轨迹中可见的 normalized steps、事件描述和 oracle pass/fail context；oracle outcome 是任务上下文，不是 anomaly label 本身。

边界：

- 固定 rollout：**是，作为已收集语料**；但没有在同一 trace 上重新应用不同 evidence/reference 条件。
- external oracle / receipt：**是，部分**，有 task oracle outcome；没有看到独立 provenance ledger 或 receipt 版本化条件。
- verifier independence：**部分**，source model 多样，但不是验证器独立性的操纵。
- evidence visibility / interpretation：**否，作为实验因子**；只是以可见 process evidence 做标签。
- reference integrity / success provenance：**否，作为实验因子**。
- factorial / interaction：**否**。

判定：**证明“成功 outcome 不等于过程正确”这一边界，但不是本问题的交叉 benchmark。**

### 5. AgentProcessBench：固定轨迹、多模型 verifier，reference 只是标注辅助

来源：

- 论文：[arXiv HTML](https://arxiv.org/html/2603.14465)
- 作者代码：[RUCBM/AgentProcessBench](https://github.com/RUCBM/AgentProcessBench)

证据：

- 论文使用 1,000 条预收集 tool trajectories，由五个 policy model 产生，并让 20 个 LLM 进行 step-level evaluation。
- 同一 task 保留多个 policy model 的 trajectory 以支持横向比较；人类标注员独立标注，official solution 与三个 LLM 生成的 reference annotation 只作为辅助材料。
- 论文报告了 human label 与 reference model 的一致性，但没有把 reference 正确性、可见性或污染作为实验条件。

边界：

- 固定 rollout：**是**，对 verifier 来说是固定输入轨迹。
- verifier independence：**是，部分**，有多模型评估；但主要是模型横比，不是跨实现 × evidence 的 factorial。
- evidence visibility：**否，作为因子**，没有同一轨迹的 masked / outcome-only / interpretation 条件。
- oracle / hidden ledger：**否/未报告**；reference annotation 是辅助材料，不是外部状态 receipt 或隐藏 provenance ledger。
- factorial / interaction：**否**。

判定：**固定 trace 上多 verifier 的清晰负边界。**

### 6. CUAVerifierBench / Universal Verifier：固定语料与 blind/informed reviewer，但不是证据可见性 factorial

来源：

- 论文：[arXiv](https://arxiv.org/abs/2604.06240)
- 作者仓库：[microsoft/fara](https://github.com/microsoft/fara)
- 数据集页：[microsoft/CUAVerifierBench](https://huggingface.co/datasets/microsoft/CUAVerifierBench)

证据：

- Fara 仓库公开了 CUAVerifierBench 的 fixed corpus；其中一个 split 有 106 条 trajectory、约两名 reviewer，并提供 UV-blind 与 UV-informed labels；另一个 split 有 154 条 trajectory，仅有 UV-blind label。
- 同一条 Fara trajectory 配有 human reviewer verdict、Universal Verifier 与 legacy verifier 输出，用于比较 agreement。
- 论文与仓库强调 process reward、outcome reward、controllable/uncontrollable failure，以及完整 screenshot context。

边界：

- 固定 rollout：**是**。
- verifier independence：**是，部分**，有 Universal/legacy verifier 与人类标签。
- evidence visibility：**未形成所需因子**。UV-blind / UV-informed 主要是 reviewer 是否知道 UV，不是同一 trace 的 evidence mask 或 interpretation manipulation。
- reference integrity / success provenance：**否/未报告**；没有 hidden reference corruption 或 provenance ledger intervention。
- factorial / interaction：**否**。

判定：**fixed-trace verifier comparison，不是四因素交叉。**

### 7. ATFD：多种监控实现与共识 ground truth，但未操纵证据或来源

来源：作者代码仓库 [Galea-foo/atfd](https://github.com/Galea-foo/atfd)。

证据：

- README 将任务定义为：给定完整 trajectory，包括 tool calls、中间状态和最终输出，评估 monitoring tool 的 detection、classification 与 cost。
- 数据集包含来自多个 agent benchmark 的 2,577 条 trajectory；ground truth 由 programmatic verifiers 与三个独立 LLM annotator 的多数意见生成。
- 被比较的系统包括 GPT-5、Claude、Llama、LangSmith、Braintrust 等模型或监控实现。

边界：

- 固定 rollout：**是**，监控器接收固定完整 trace。
- verifier independence：**是，部分**，实现与模型来源多样；但这些不是与 evidence/reference 因子正交的操纵。
- external oracle / reference integrity：**部分/未报告**。programmatic verifier 与 annotator consensus 是标签来源，但没有 hidden reference 或外部 receipt 的交叉条件。
- evidence visibility / success provenance：**否，作为因子**。
- factorial / interaction：**否**。

判定：**多监控器基线，不是同一 trace 上的交叉因果评测。**

### 8. Agents’ Last Exam：有 hidden reference 和确定性 grader，但 rollout 不是固定后再交叉

来源：

- 论文：[arXiv](https://arxiv.org/abs/2606.05405)
- 作者仓库：[MaxIntelligenceAgency/ALE-Benchmark](https://github.com/MaxIntelligenceAgency/ALE-Benchmark)

证据：

- 仓库描述的固定 loop 是：provision environment、stage inputs、运行 agent 至完成、之后才 stage hidden reference、grade、score，并收集统一 trace/log/artifacts。
- hidden reference 在 agent 完成后才注入，以避免 reference leakage；grader 是确定性的，整个运行可审计。

边界：

- hidden reference：**是**。
- external oracle / receipt：**是，部分**，有环境与 deterministic grader。
- 固定 rollout：**否，按本问题的严格定义**；它固定的是运行协议，不是同一 agent rollout 在 verifier/reference 条件之间回放。
- verifier independence、evidence visibility、reference corruption、success provenance：**未形成交叉因子**。
- factorial / interaction：**否**。

判定：**hidden-reference 设计的强边界，但不回答同一 trace 的交叉操纵问题。**

### 9. Agent-Safety Evaluations as Load-Bearing Evidence：把 replayability 本身变成测量对象

来源：[论文 arXiv](https://arxiv.org/abs/2607.12469)，复现包链接见论文给出的 [Zenodo DOI](https://doi.org/10.5281/zenodo.21055696)。

证据：

- 论文提出 evidence sufficiency / reconstructability metric，覆盖多个 decision-property 类别，并用 counterfactual-replay intervention 与 replayability-precondition probe 检查公开 trace 是否足以支持判断。
- 论文摘要说明其 release-gate pair 使用 raw 与 instrumented trace，且不重新运行模型。

边界：

- 这是 replayability / evidence integrity 的元评测工具，不是同时操纵 verifier independence、reference integrity 与 success provenance 的 benchmark。
- 它没有提供本问题所需的完整 cross-factor interaction；其价值在于指出“同一 trace 可被回放”必须先成为可证伪的前置条件，而不能只由日志存在推断。

判定：**方法学边界，不是命中来源。**

### 10. The Replay Gap：模型切换会破坏“同一 trace 代表同一世界”的假设

来源：

- 论文：[arXiv HTML](https://arxiv.org/html/2608.08239)
- 作者代码：[AshrithaG/replay-gap](https://github.com/AshrithaG/replay-gap)
- 数据集：[replay-gap-trajectories](https://huggingface.co/datasets/ashritha0907/replay-gap-trajectories)

证据：

- 该工作从真实 SWE-bench trajectory 的受控点分叉，用不同模型继续执行，并设置 same-model paired control。
- 论文报告 prefix replay 的 return code agreement 很高，但 model swap 仍会让后续成功结果翻转；因此静态 replay evaluator 可能给出错误的世界判断。

边界：

- 它操纵的是 agent model switching，不是 verifier independence。
- 它没有 evidence visibility、reference integrity 或 success provenance 的 factorial。
- 它对本问题的直接贡献是：固定前缀、重建环境和 live continuation 不是同一个实验对象；若 verifier 条件改变了 agent 可见信息或执行路径，必须验证 trace 的 counterfactual validity。

判定：**非 benchmark 命中，但直接暴露 replay-validity 的关键边界。**

## 横向判定矩阵

| 来源 | 固定 rollout | oracle / receipt | hidden reference / ledger | verifier independence | evidence 因子 | reference / provenance 因子 | 真 factorial / interaction | 总判定 |
|---|---|---|---|---|---|---|---|---|
| trajectory-judge | 是，固定 400 条 | 部分，脚本 oracle/fault replay | 否 | 部分 | 是，outcome-only/full trace | 否 | 否 | 最接近，但未命中 |
| GCPC | 是 | 部分，official outcome | 未报告 | 否/部分 | 是，log-only vs outcome 分离 | 部分 | 否 | 强边界 |
| ActBench | 否，paired rerun | 是，trusted state/audit evidence | 部分 | 部分 | 是，log vs trajectory | 部分，path provenance | 否 | provenance 侧近邻 |
| OpenClawBench | 是，已收集语料 | 部分，BFCL oracle | 否 | 部分，source model 多样 | 否，主要是标签证据 | 否 | 否 | 观察性边界 |
| AgentProcessBench | 是 | 部分，human/reference aid | 否 | 是，模型横比 | 否 | 否 | 否 | fixed-trace 负边界 |
| CUAVerifierBench | 是 | 部分，human verdict | 否 | 是，UV/legacy/human | 未形成 mask 因子 | 否 | 否 | fixed-trace 负边界 |
| ATFD | 是 | 部分，多 verifier/annotator 共识 | 否 | 部分 | 否 | 否 | 否 | 监控器基线 |
| ALE | 否，在线运行 | 是，deterministic grader | 是 | 否 | 否 | 否 | 否 | hidden-reference 边界 |
| Load-Bearing Evidence | 静态 trace / replay probe | replay precondition | 否 | 否 | 是，reconstructability | 否 | 否 | 方法学工具 |
| Replay Gap | 只固定 prefix | 环境重建有检查 | 否 | 操纵 agent model 而非 verifier | 否 | 否 | 否 | replay-validity 边界 |

## 边界与不确定性

1. **“跨模型”不自动等于 verifier independence。** AgentProcessBench、OpenClawBench 和 ATFD 有多个模型来源，但只有在同一输入、同一判定任务和明确的 verifier 角色下，才能解释为 verifier independence；policy model 多样本身不够。
2. **“有 oracle”不自动等于 external state receipt。** trajectory-judge 的 scripted oracle、OpenClawBench 的 BFCL outcome 和 ALE 的 deterministic grader 都提供比最终答案更强的标签，但只有带版本化状态、调用结果或审计事件的记录，才接近可审计 receipt；本轮没有找到它们与 reference corruption 交叉的公开实验。
3. **“盲/知情”不自动等于 evidence visibility。** CUAVerifierBench 的 UV-blind / UV-informed 主要操纵 reviewer 对 verifier 的知识，不等于同一 trace 的 evidence mask、字段可见性或 interpretation protocol 被操纵。
4. **匹配任务不等于固定 trace。** ActBench 的 paired benign/malicious cases 和 Replay Gap 的 model-switch branches 都说明：只保持任务、初始状态或 prefix 相同，不能推出完整 rollout 相同。
5. **当前结论是公开材料边界，不是“不存在”的证明。** 特别是作者内部 benchmark、未公开附录或尚未发布的代码可能包含更完整的 design；本轮未将二手综述或搜索目录当作证据。

## 是否出现 new bottleneck

**出现了一个被进一步明确的新瓶颈：`replay-validity / provenance binding`。**

它不是一个与 EX-001/EX-002/EX-004 完全无关的新主题；那些队列已经要求固定 trace、receipt 和 provenance。但本轮把约束 sharpen 成了一个可检验的门：

> 在比较 verifier independence 或 evidence visibility 之前，必须证明同一条 trace 在该反事实条件下仍代表同一个外部世界，并能由 receipt / state hash / event ledger 绑定到该世界；否则“同一 trace 上的交叉效应”可能只是回放失真。

这使得真正的瓶颈不是再找一个“多 judge benchmark”，而是同时拥有：

- 不变的 agent rollout；
- 可独立核验的外部状态与调用 receipt；
- 对 verifier 不可见或不可篡改的 reference / provenance ledger；
- evidence mask、reference integrity、verifier independence 的正交条件；
- 明确的 interaction 估计，而非多个主效应表格。

## Explore 产出：下一步研究单元

### 新问题

能否在一个小型确定性 tool environment 中构造公开的 2 × 2 × 2 设计：

- verifier：同实现 / 跨实现或跨模型；
- evidence：outcome-only / full trace 或可控字段 mask；
- reference/provenance：正确 ledger / corrupted 或 sham ledger；

并在同一条冻结 rollout 上，用 external receipt 估计 verifier × evidence、verifier × reference 以及 evidence × provenance interaction？

### 可证伪方向

- 若后续找到来源同时公开了固定 trace、hidden reference、receipt/ledger、至少两个独立 verifier，并报告 interaction，应撤回“没有完整命中”的结论。
- 若同一 trace 在不同 verifier 可见性下无法由 state hash、tool result 和 event ID 重建，则“固定 trace”门槛应判为不成立，不能把结果记作 factorial evidence。
- 若 verifier 之间的差异在 evidence mask 或 reference integrity 变化后不显著，说明所谓 independence 可能只是模型能力主效应，而不是交互机制。

### 继续寻找的 source 需求

优先查找：作者发布的 replay harness、benchmark data card、hidden-reference grader 和 provenance/receipt schema；搜索时要求代码或官方文档能定位到逐条件数据，而不是只给 aggregate score。

### 最小实验建议

复用 trajectory-judge 类型的确定性 support-desk 环境：先固定一批 clean / silent / loud traces，保存 state hash、tool-call receipt 和不可见 reference ledger；再把同一 trace 交给 rule verifier、独立模型 verifier，并按 outcome-only / full trace 与 correct / sham ledger 交叉评分。只有当每个 cell 都有同一 trace、同一 receipt 绑定且预先定义 interaction contrast，才把结果计为本问题的正例。
