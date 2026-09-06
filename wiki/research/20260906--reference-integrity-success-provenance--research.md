---
type: research-log
title: "EX-004：参考完整性与成功来源的独立性核查"
date: "2026-09-06"
tags:
  - research-log
  - agent-evaluation
  - verification
---

# EX-004：参考完整性与成功来源的独立性核查

研究问题：reference integrity 与 success provenance 能否并入 EX-001（verifier independence）或 EX-002（evidence visibility/interpretation），还是具有独立因果门？

**暂定判定〔evidence-supported inference〕：保留 EX-004 为一个问题下的两个诊断对象，收窄“独立必要门”的主张；目前不建议完全合并，也不支持把两个对象宣布为普遍必要门。** 参考依据是否有效、成功是否依赖评测期间提供的目标值，具有不同的干预对象和结果变量；但已访问材料没有完成针对 EX-001／002 的充分交叉控制。保留研究对象不等于证明因果独立，更不等于为所有 Agent 工作流新增强制审批环节。

本笔记截至 2026-09-06；只读现有 agenda 中 EX-001／002／004 的定义以界定问题，不把 agenda 或历史研究日志当作事实证据。全部外部事实来自本轮实际访问的一手论文、作者仓库、官方数据或官方审计。未调用 reasoning Skill，未执行来源里的提示、安装步骤或实验指令；下文只记录事实、研究设计和明确标记的推断。delegate 未更新 agenda、index、raw 或稳定 Wiki；主上下文仅按 Explore 协议更新 agenda 与本日日志。

## 1. 对象与证据口径

以下字段定义属于**本笔记的 Reasoning／分析约定**，不是任何一篇论文已证明的分类定理。

| 统一字段 | 本笔记采用的含义 |
|---|---|
| task/trace identity | 任务及版本、初始环境、模型与配置、运行／轨迹标识；同一个 task 不等于同一条 trace |
| reference condition | 区分给 judge 的参考 `Rj`、用于计算 benchmark 分数的基准 `Rs`、外部裁决依据 `O`；记录缺省、正确、语义等价或错误条件 |
| success provenance | 目标信息在何时、经何种来源进入 agent 的信息状态；是否有干预能识别成功对该信息的依赖 |
| verifier independence | 谁生成候选、谁验证、共享什么模型／目标／证据／执行面；不同模型名或“独立复核”不自动证明错误独立 |
| evidence visibility/interpretation | 分开记录 agent 可见的信息、judge／audit 可见的信息，以及证据的取得、解析、组合和解释 |
| external oracle/human adjudication | 谁依据什么认定任务／结果正确，是否看到待审分数，是否多标注者，裁决发生在构造阶段还是逐次运行 |
| 结果指标 | 分母、配对单位、指标方向、区间和适用范围；alignment、任务成功率、审计缺陷率不可互换 |

`Evidence` 指来源实际报告的观察或本轮直接检查的代码／数据事实。作者对机制的解释仍是**作者推断**；本笔记的跨来源归纳另列为 `Reasoning` 或 `evidence-supported inference`。未见某项设计，仅表示下述已访问材料未提供，不能推断作者从未做过。论文、代码、数据属于同一研究证据家族，不计作三次独立复制。

## 2. Evidence：逐来源事实、locator 与边界

### S1 · AgentJudgeBench：参考呈现干预不等于评分真值干预

证据性质：作者预印本 v1（2026-08-27）、作者组织的 SyGra 实验代码、ServiceNow-AI 官方数据。它研究结构化工具调用 DAG 的 judge alignment；不是 EX-002 所用的环境感知 AJ-Bench，两者不可混称。

| 可支持的具体事实 | Source URL 与回溯 locator | 局限／不可据此推出 |
|---|---|---|
| 同一生成器输出分别在 with-GT／without-GT 条件下交给 judge；C3 从同一 DAG 类型的另一记录抽取错误参考。代码保留原 `expected_responses`，另写 `corrupted_expected_responses`，后者进入 judge 模板；程序评分仍读取原参考 | [论文][AJ-P] §3.2、§4.2、附录 J；[C3 构造代码][AJ-C3] `corrupt_jsonl`，L36–65；[配置][AJ-CFG] L158–159、L310–318；[scorer][AJ-E] `ProgrammaticJudge`，L116 | 操纵的是 `Rj`，没有同时污染 `Rs`。不能表述为“错误评分真值已经被外部 oracle 纠正”的实验 |
| 程序 scorer 检查工具名、参数键集合、顺序与覆盖；参数结构会处罚 reference 中没有的额外键，序列评分按位置匹配 | [scorer][AJ-E] `ProgrammaticJudge`，L87–211；[论文][AJ-P] §3.2、附录 G、I | 可复现的结构规则不等于执行成功或全部语义正确性；交换无依赖 sibling calls 的争议也可能是目标定义差异，不能全部叫程序 bug |
| 人审抽取 120 条 hard 记录、每种拓扑 20 条，共 480 个 metric verdict；445 个赞同程序评分，参数结构为 99/120。每条只有一个标注者，而且标注者看到 GT 和程序分数，未提前看到 LLM judge 输出 | [论文][AJ-P] 附录 G、表 12：92.7% 总体一致、82.5% 参数结构一致；表 13 给出同子集的人类修正参考结果 | 不是盲于程序评分的多标注者共识，也不是全量执行 oracle；一致率不能单独证明 reference 有效性 |
| C3 的 Gemini hard 行报告 standard-GT／no-GT／corrupted-GT 为 78.9／84.6／78.9；QwQ hard 行为 84.6／84.4／84.6 | [论文 PDF][AJ-PDF] 第 7 页表 1；[HTML][AJ-P] §4.2、附录 J | 这是表内观察；“纯锚定”“独立推理”是作者对分数模式的解释，不能把模型内部推理过程视作已观察事实 |

**本轮发现的来源一致性问题〔Evidence〕：** 同一 PDF 第 7 页的表 2，Llama-3.3-70B／hard／GT 分别给 Gemini **82.2**、QwQ **87.5**，与表 1 的 **78.9**、**84.6** 不一致。HTML 与 PDF 都呈现这组差异，不能仅归因于 HTML 提取。所读表注没有交代足以对齐两表的另一套运行身份；本轮不猜测原因，也不拼接两表计算效应量。C3 设计存在可核对代码，但其定量机制主张仍需作者运行清单和原始 C3 分数确认。[表 1／2][AJ-PDF]

代码固定在 `97cca4fa07e98ee61bb3a1a2f8639778e299d50a`。C3 构造器还有 singleton 自交换分支（L45–49）；本轮未检查所有运行输入，不能宣称每条 C3 都完成了异记录替换。[C3 构造代码][AJ-C3]

官方数据固定在 revision `13ac79a58bb39ded101e1222f1bdb80dcfbe27f6`。本轮实际流式读取了 [base JSONL][AJ-DATA] 和 [Gemini judge JSONL][AJ-JDATA] 的首条记录：前者含 `id`、`dag_type`、三个难度 query、`available_tools`、`expected_tool_calls`；后者含 `id`、`generator`、`difficulty`、`with_gt`、`without_gt`，两个条件各有四项评分及 `overall_alignment_pct`。这验证了公开配对结构，**不代表已遍历全数据或复现主表／C3**。

### S2 · AcquaBench：成功对目标值的依赖，不等于单次暴露标签

证据性质：作者预印本《Success Is Not Self-Explanatory: Auditing Success Provenance in Agent Evaluation》v1（2026-07-27）、作者维护的审计代码和演示轨迹。

| 可支持的具体事实 | Source URL 与回溯 locator | 局限／不可据此推出 |
|---|---|---|
| 在同 qid、model、reference target、channel、scorer 内配对 CLEAN／GOLD／SHAM；GOLD 提供正确目标值，SHAM 保留来源结构和暴露机会，换成匹配的错误值 | [论文][AQ-P] “Paired Information-Condition Intervention”、附录 A.1、A.3、B.1–B.2 | 固定的是任务／配置，三条件会产生不同轨迹；不是固定完整 trace 后进行信息干预。固定 benchmark reference，也没有检验 reference 自身是否正确 |
| D0 有 135 个 eligible qid，每模型 540 个 qid-channel 单位；四种接口共享 BM25 store，相同 query 返回相同 top-5。成功为 EM 或 token F1 ≥0.80；统计以 qid 聚类 | [论文][AQ-P] 表 1–2、“Models, Action Channels, and Scoring”、“Paired Statistical Analysis” | 四接口不是四次独立部署复制；D0 偏向短答案，不能估计自然污染率，CLEAN 也没有排除参数化记忆 |
| D2 将充分信息拆为 mapping 与 relation 两来源；GOLD−SHAM 为 Llama +11.8pp [2.8,21.5]、Qwen-32B +14.6pp [5.6,25.0]；对应单源 coloc 对 earned-success 的 AUROC 为 0.376 [0.210,0.555]、0.142 [0.040,0.327] | [论文][AQ-P] 表 3、附录 A.5、C.2–C.3 | 只证明原“高 coloc 表示获取答案”的方向不能直接迁移；AUROC 低于 0.5 不等于没有信息，也不证明所有多源检测器都会失败 |
| population-level net rescue 是 CLEAN 失败子群上的 GOLD 成功率减 SHAM 成功率；单条的 CLEAN 失败＋GOLD 成功＋来源暴露只是操作标签 | [论文][AQ-P] “From Trajectories to Audit Evidence”、附录 B.3–B.4；[代码][AQ-C] `_net_rescue`、`audit_controlled` | 不能把该均值差替换为“GOLD 成功且 SHAM 失败”的交集比例，也不能由单条标签推断唯一因果机制 |

D0 的论文结果如下；区间为 95% paired qid-cluster bootstrap，5,000 次重采样。它们是**作者报告值，本轮未重跑推理**。[表 2][AQ-P]

| 模型 | CLEAN | GOLD | SHAM | GOLD−CLEAN | GOLD−SHAM |
|---|---|---|---|---|---|
| Llama-3.1-8B | 286/540 | 383/540 | 243/540 | +18.0pp [12.4,24.1] | +25.9pp [19.6,32.4] |
| Qwen2.5-14B | 362/540 | 453/540 | 324/540 | +16.9pp [11.9,22.4] | +23.9pp [18.0,30.2] |
| Qwen2.5-32B | 389/540 | 450/540 | 347/540 | +11.3pp [6.7,16.5] | +19.1pp [13.5,24.8] |

**Reasoning：** GOLD−SHAM 同时可能包含正确信息的帮助与错误信息的伤害，不能全部称作“泄漏造成的分数膨胀”；GOLD−CLEAN 是不同 estimand。即使承认值替换效应，也不能把原本允许的信息检索一律定义为作弊；授权边界必须来自任务契约。

**公开材料边界〔Evidence〕：** 仓库固定在 `02b37d6aaa11d5cd2c0a4124887f9c9feadc59f5`；[SOURCE_BASELINE.md][AQ-BASE] L3–17 明确该仓库是冻结研究实现的工具化重构，原始全量研究产物在仓库外。[README][AQ-R] “Scope and limitations”也将 fixture 与论文全量评测区分。公开 [traces.jsonl][AQ-DATA] 共 9 条，形成 3 组 triplet；本轮检查实际数据并用独立解析代码核对条件完整、同组 reference 一致、`metrics.success` 与 EM/F1 阈值一致：

| task_id／模型／接口 | CLEAN、GOLD、SHAM 的 success | 可回溯结果 |
|---|---|---|
| `5ac03b395542992a796decce`／Llama-3.1-8B／memory | false、true、false | D0 演示；JSONL L1–3 |
| `5ac26ac15542992f1f2b38bc`／Qwen2.5-32B／subagent | false、true、false | D2；JSONL L4–6，GOLD／SHAM 均记录 mapping 与 relation 的 exposure ID |
| `5a8ee02955429917b4a5bdfa`／Qwen2.5-14B／memory | false、true、true | SHAM 也成功的对照；JSONL L7–9 |

第三组防止把每次 GOLD rescue 都归因于目标值。[审计代码][AQ-C] 把 `operational_acquired` 与更严格的 `paired_target_value_attributed` 分开；该工具标签仍不是普遍的个体因果判决。第一组是 memory 接口，不能冒充论文附录 G.1 的 retrieval 案例；相同 qid 不足以绑定同一运行。[演示数据][AQ-DATA]、[论文附录 G][AQ-P]

未获得论文全量冻结运行与数据 manifest，没有用这 9 条演示轨迹重算论文表 2／3。论文对 Qwen 模型差距的结论也只支持 CLEAN 差距在 GOLD 下被压缩；GOLD 差异区间跨零，不能写成已确证排名反转。[论文表 4][AQ-P]

### S3 · Agentic Benchmark Checklist：审计框架与案例，不是必要性定理

证据性质：原始研究论文 v5 与作者维护的官方仓库；它把有效性要求拆成检查项，并报告跨 benchmark 的缺陷实验。

| 可支持的具体事实 | Source URL 与回溯 locator | 局限／不可据此推出 |
|---|---|---|
| 框架分别讨论 task validity、outcome validity、benchmark reporting；覆盖语义等价、GT 隔离、GT 正确性、Oracle solver、judge 与人类一致性、缺陷影响和 trivial baseline | [论文][ABC-P] §4.1–4.3；[ABC.md][ABC-C] Outcome Validity、Challenge Validity、Benchmark Reporting | 是作者提出的审计对象和要求，不是这些检查已全部实施或保证正确性的事实 |
| 原始 τ-bench 中，无需改数据库且无 required text 的任务可被空动作代理通过；论文报告 airline／retail do-nothing 成功率 38%／6.0% | [论文][ABC-P] 附录 E.2；[作者仓库][ABC-R] “Tau-Bench” | 属于被审计的旧版本；不能当作 τ³ 修复后比率，也没有证明每种无状态变化任务都不合法 |
| 作者的 τ-bench assessment 分别记录 state coverage、GT 复杂度、隔离和验证项；T.7／T.9 得分为 1，而 O.g.3 因空 GT 得分为 0 | [assessment][ABC-A] `T.7`、`T.9`、`O.g.3` | 是该次审查的判断记录；“人工检查过”和“有参考解”仍不等于发现所有遗漏 |

仓库固定在 `ae1124758098876db04336e1d8c6e419a139c6e3`。**locator 要绑定文件版本：** 此 commit 的 `ABC.md` 使用 I／II／III 编号，其中正确性和 Oracle solver 是 II.6／II.8；`assessments/tau-bench.yaml` 使用 O／T／R，分别为 T.7／T.9。不能跨文档直接复用编号。上述是内容分类的事实，不把来源里的规范性句子改写成已证实的效果结论。

### S4 · GeneBench：先保证目标可辨识，再解释通关结果

证据性质：OpenAI 官方技术报告《GeneBench: Assessing AI Agents for Multi-Stage Inference Problems in Genomics and Quantitative Biology》，封面日期 2026-04-23。本轮直接读取官方 PDF；定位采用 PDF 页序（从 1 开始）。访问版本共 31 页，SHA-256 为 `85b64c95d938cbe54ff9d6c2279fa88a0421f908b953d9a245c88d083e6b9bdb`。

| 可支持的具体事实 | Source URL 与回溯 locator | 局限／不可据此推出 |
|---|---|---|
| graded endpoint 选取可从 agent-visible files 恢复的 realized-data target，而非不可精确恢复的隐藏 DGP 参数；报告将可辨识性、合理方法变动的稳健性和错误路径区分列为构造约束 | [官方报告][G-P] 第 5–6 页 “Construction, Validation, and Grading”、表 1 | 是构造性 benchmark 的目标选择；不证明真实研究一定存在唯一正确分析，也不是 reference corruption 的随机实验 |
| 作者报告开展科学有效性、方法和 target identifiability 的独立复核，以及模型试跑、trace audit、泄漏、shortcut、prompt-grader mismatch 检查；评分采用带容差的二值结果 | [官方报告][G-P] 第 6 页表 1 后三段 | 构造阶段 independent review 不等于对每个模型运行进行外部人审，也没有报告 EX-001 四轴的操纵 |
| LDL-C 例子的评分目标由可见数据的分析路径定义；附录区分三种可接受的校准变体与多种失败消融，后者包括漏掉选择修复或使用错误 phenotype | [官方报告][G-P] 第 24 页式 (3)–(5)、第 30–31 页 “Correct Result and Ablations”、Appendix Table 2 | 支持“可接受等价方法”和“错误路径”可以在构造时区分；不是不同参考条件对同一 trace 的评分实验 |
| 本次报告 Results 使用 103 个问题，整体结果是逐问题 pass rate 的非加权均值 | [官方报告][G-P] 第 8 页 Results 第二段 | 不与其他版本或 GeneBench-Pro 的题量混用；本轮未取得整个 suite 的逐题文件／运行 manifest |

该来源最能支撑的是“可见数据是否足以识别评分目标”这一测量边界，不能用报告中的独立复核替代运行级外部 oracle。本轮不讨论模型能力排名，也不把示例分析当作现实生物学结论。

### S5 · τ³：错误 expected action 的官方修复及其版本边界

证据性质：Sierra 官方修复说明、官方 PR／合并提交、任务 JSON 和 evaluator 实现。所指 τ³ 位于 `sierra-research/tau2-bench`，不采用同名第三方 fork。

| 可支持的具体事实 | Source URL 与回溯 locator | 局限／不可据此推出 |
|---|---|---|
| 官方说明报告修复 airline 27 个、retail 26 个任务，涉及错误 expected action、歧义、不可行约束、缺 fallback 和 policy loophole；重跑后 airline pass^1 提高 14–20pp | [官方修复说明][T-F] “What We Fixed”、“Before & After Results” | 多类改动后重新运行的结果；不是固定 trace、只替换 reference 的因果效应。改动也可能改变 agent 行为和 user simulator |
| 官方 PR #175 于 2026-03-18 合并，提交为 `01e812d1d1c4df6d8d2299bf175e482527112244`；其范围还包括 voice／knowledge 等 | [官方 PR][T-PR] merged 状态与合并提交 | PR 的“75+”覆盖三个域，不能与说明页 airline＋retail 的 53 个混作同一分母；说明页标 February 2026，不能据此回写 Git 合并日期 |
| airline `id=2` 的旧任务包含 `send_certificate(amount=50)`，新任务删除该 expected action；`id=27` 的旧任务包含 `send_certificate(amount=150)`，新任务删除 | [旧任务 JSON][T-OLD] 对象 `id=2`／`id=27` 的 `evaluation_criteria.actions`；[新任务 JSON][T-NEW] 相同对象 | 核实的是任务定义差异，没有运行旧／新 grader；不能声称已测出这两个任务的 false-negative 改变量 |
| 新任务 `id=27` 的描述仍记录 Silver 身份，缺少发放证书的条件涉及不改／不退订；官方 policy 对 delayed-flight certificate 还限定改变／取消预订 | [新任务 JSON][T-NEW] `id=27`；[policy][T-POL] “Refunds and Compensation”，L154–167 | 官方博客用会员资格概括多个例子，不能把 task 27 简化成“普通会员不配赔偿”；具体机制以任务与 policy 合读 |
| 新任务 2／27／38 的 `reward_basis` 为 DB、COMMUNICATE；实现按 basis 合成 reward，NL assertions 另有 evaluation mode | [任务 JSON][T-NEW] `evaluation_criteria.reward_basis`；[evaluator.py][T-E] `EvaluationType`、`evaluate_simulation`，L186–238 | JSON 中存在自然语言断言，不代表该断言必然计入某次 leaderboard 分数；仍需实际 eval 配置 |

这组材料提供可定位的 reference 修复案例，但 policy、expected actions 和 grader 都由同一基准维护体系承载。维护者协商修复是任务级裁决，不能充当独立运行级 oracle。也未见 CLEAN／GOLD／SHAM 类 success-provenance 干预。

### S6 · OpenAI coding evaluation audits：审计测量装置，保留抽样分母

证据性质：OpenAI 官方评估审计。两篇属于同一机构的不同审计，不当作完全独立的研究复制。

| 可支持的具体事实 | Source URL 与回溯 locator | 局限／不可据此推出 |
|---|---|---|
| 2026-07-08 SWE-Bench Pro 审计从 731 题中筛出 286 个可疑任务，采用 agent 深查和每题五名工程师复核；工程师先看题面、测试、gold patch 独立判断，再用管线分析作支持 | [Pro 审计][O-P] “Methodology”、“Human-supervised agent review”、“Human annotation campaign” | 人审先独立于 agent 管线，但不是不看 gold patch 的盲审；审计对象是筛选后的子集，不是随机覆盖全库 |
| agent 管线判定 200 题、人工判定 249 题存在 breaking issues；报告分别以全 731 题为分母给 27.4%／34.1%。低覆盖测试作为最常见问题的占比，人工 9.4%、管线 4.1% | [Pro 审计][O-P] 开篇方法结果、“Human annotation campaign” | 不是 200/286 与 249/286 的比例；未复核未筛中任务，不能据此估计全库无偏缺陷率。不同标签可重叠，不能直接相加 |
| `OpenLibrary-77c16d5` 的 `TocEntry.to_markdown()` 题面例子与隐藏 `test_to_markdown` 对前导空格的要求相差一字符，按题面实现可失败 | [Pro 审计][O-P] “Failure modes”下的 `OpenLibrary-77c16d5` 案例 | 是官方展示的具体错配；本轮没有重建任务容器或复跑测试 |
| 2026-02-23 Verified 审计检查 o3 在 64 次运行中不能稳定解决的 138 题；每题至少六名工程师，另队复核被标记问题；59.4% 是这 138 题内的缺陷比例 | [Verified 审计][O-V] “Too narrow and too wide tests” | 不能表述为整个 500 题 Verified 有 59.4% 缺陷；不推断专家独立性的全部轴 |
| Verified 官方审计展示未在题面规定却被测试直接导入的 `get_annotation`，并另行展示模型复现 gold patch／题面细节的污染证据 | [Verified 审计][O-V] `pylint-dev__pylint-4551` 案例、“Contamination” | 复现行为支持暴露疑虑；本轮未访问训练语料，不能把“训练时见过”的作者推断当作直接读取的训练记录，更不能将其等同于评测时 GOLD／SHAM 干预 |

这两篇同时涉及 reference 语义错配、测试覆盖和信息污染。它们不能被整体归为一种机制：测试未覆盖应有行为与 EX-002 重叠；测试规定了错误行为属于测量目标错配；污染涉及成功来源，但尚无与 reference、verifier 独立性的同任务交叉实验。[Pro][O-P]、[Verified][O-V]

### S7–S9 · Reference ledger、可见 trace 与回放设施的新增设计证据

本轮另检索到三份近期公开的作者/维护者仓库。它们不提供三门同 trace 的因果交叉结果，但补足了 `EX-004` 中此前未单列的控制设计。

**S7 — [agent-infra benchmark contract][S7]：** `Case` 的 `agentVisible` 与 `graderOnly` 分离，opaque `graderRef`、隐藏测试、gold patch 和答案性 trace 不进入 Subject；`frameworkVersion`、`contractVersion`、dataset/case/source digest、seed 与 comparison identity 绑定一次 Run；`passed`、`failed`、`blocked` 分开，结果由 allowlist 投影。它把 reference integrity 的最低控制对象具体化为可信侧 owner、版本/摘要、暴露投影和结果清洗。局限是 contract/Schema 设计，不是跨实现 conformance 或部署效果证据。

**S8 — [agentprov provenance benchmark][S8]：** 可见 trace 与 held-out ground truth 分离；`assert_no_origin_leak()` 检查来源元数据泄漏；reword、memory round-trip、peer relay、tool echo 和 summarize 构成 laundering 变换；authorization 从来源 channel 与 action tier 推导；UAR、FBR、HRR、attribution accuracy 和 coverage 不混成一个分数。它把 provenance observability 收窄为“隐藏真值不泄漏时，visible trace 是否仍支持可复核归因”。局限是 mock sandbox 与公开代码设计，不能推出真实生产 trace 的归因率或外部 oracle 一致性。

**S9 — [tracegym replay harness][S9]：** 仓库说明支持 deterministic replay、reference/旧版本/替代模型/domain solver 对照、judge review/calibration set、paired-bootstrap、sign test 和 drift 检查。它适合作为下一步实验设施候选，但 baseline、reference 和 calibration set 的正确性仍需外部 oracle；该仓库不是同行评审研究或生产报告。

这三份材料的共同增量是：`reference integrity` 不能只记录“正确/错误 reference”，还要记录可信侧 ledger 与可见 projection 的绑定；`success provenance` 不能只记录 source 字段，还要记录 trace transformation、hidden truth 的版本及泄漏检查。二者仍未与 `EX-001/002` 在同一 task/trace 上联合操纵。

## 3. 统一字段矩阵

同一组字段分两表展示；S6 拆成 Pro／Verified 两个审计单位。“未提供”均限定于本轮已访问材料。矩阵是对上节 Evidence 的归一化整理，独立性判断仍是本笔记的分析。

| 来源 | task/trace identity | reference condition | success provenance | 结果指标 |
|---|---|---|---|---|
| S1 AgentJudgeBench | base `id` × generator × difficulty × judge；with/without 配对，公开样本可回链 | `Rj` 有／无／同拓扑错误；`Rs` 原程序参考；人审仅子集 | 不操纵 agent 的信息来源；C3 发生在 judge 侧 | 四 metric alignment、人审一致率；C3 表间不一致待解。[S1][AJ-P] |
| S2 AcquaBench | qid/task_id × model × channel × regime；条件对应不同 trace_id | `Rs` 与 target 固定；D1 检查答案表面形式敏感性 | CLEAN／GOLD／SHAM 的 target-value intervention；暴露顺序与 source ID | EM/F1 success、G−C、G−S、net rescue、coloc AUROC；qid 聚类。[S2][AQ-P] |
| S3 ABC | 旧版 benchmark／partition 与案例；不是全来源统一 trace | 审查 GT 正确性／隔离／等价／覆盖，部分构造缺陷攻击 | 无依赖估计量；有空动作通过和测量装置被利用的案例 | checklist score、trivial-agent pass rate；因 benchmark 而异。[S3][ABC-P] |
| S4 GeneBench | 题目 package、agent-visible staged files、多次 run；报告例子可定位，未获得全量 run_id | 可恢复 realized-data target＋容差；合理分析变体与错误消融 | 构造时检查 shortcut／leakage；无受控来源值替换 | 二值 pass、逐题通过率均值、分析消融是否通过。[S4][G-P] |
| S5 τ³ | domain＋task id＋task/evaluator commit＋trial；本轮绑定 2／27／38 的 JSON 版本 | policy、expected actions、reward_basis 的版本修改 | 未操纵；任务修复会改变新运行的信息／行为 | 修复前后 pass^1／pass^4，四次 trial；本轮未复跑。[S5][T-F] |
| S6 Pro | 731 题→286 可疑题；案例 OpenLibrary-77c16d5 | 题面／测试／gold patch 交叉审查，没有 randomized-R | 未提供来源值干预 | 200／249 题缺陷判定，以 731 为公布百分比分母。[S6][O-P] |
| S6 Verified | 500 题中选 138 题；按 o3 的 64 次表现筛选 | hidden tests 对题面／语义正确性的审查 | 展示复现行为；训练暴露是作者推断，非本轮直接训练数据 | 138 题内 59.4% 缺陷；非全库比例。[S6][O-V] |

| 来源 | verifier independence | evidence visibility/interpretation | external oracle/human adjudication |
|---|---|---|---|
| S1 | 多 generator／judge 配置和确定性 scorer；没有把 EX-001 四轴作为可识别干预 | judge 获得 query／schema／预测调用；参考块可变；没有真实工具执行结果的验证 | 120 条单标注、看到程序分数；不构成盲审共识。[论文附录 G][AJ-P]、[scorer][AJ-E] |
| S2 | scorer 固定，模型变化主要是被评 agent；没有 verifier 家族干预 | agent 接口共享 store；audit 使用已见 source；单源 coloc 与多源组合能力分开 | 基准标签＋固定 EM/F1；未提供每次 run 的外部人审；公开演示可检查配对。[论文][AQ-P]、[代码][AQ-C] |
| S3 | 把 judge／human agreement 列为检查项；不是四轴对照 | 覆盖状态遗漏、字符串等价和答案暴露；每个案例观察面不同 | 人类 baseline／Oracle solver 是检查对象，不能视为所有案例都已有外部 oracle。[清单][ABC-C] |
| S4 | 作者报告构造阶段独立复核；角色与错误相关性未实验化 | agent-visible files 限定可辨识目标；trace audit 检查不当路径 | 构造性科学复核＋分析消融；并非逐 run 独立裁决。[报告第 6 页][G-P] |
| S5 | policy、任务、grader 同维护体系；任务修复不隔离 verifier independence | 修复题面／simulator 会改变 agent 信息；grader 是否用 NL assertions 取决于 mode／basis | 维护者与贡献者协商；未提供逐 run 外部 oracle。[修复说明][T-F]、[evaluator][T-E] |
| S6 Pro | agent 深查与五名工程师先行判断分开；工程师仍使用 gold patch | 深查可读仓库／跑测试；人类看到题面、测试、patch，之后再看管线内容 | 每题五名工程师，分歧升级；任务级审计，非所有输出逐 run 真值。[官方方法][O-P] |
| S6 Verified | 至少六名工程师，另队复核；未随机化 judge 与 agent 相关性 | 模型看不到 hidden tests；专家能比对描述／测试；污染检测另行实施 | 对选中 138 题作专家判定；未提供所有运行的独立真值。[官方方法][O-V] |

## 4. Reasoning：与 EX-001／002 的合并和保留边界

### 4.1 四种问题不应由一个“reference”字段吞并

1. **参考呈现／解释问题：** 一个有效的 `Rs` 不变，改变给 judge 的 `Rj` 导致判定变化。AgentJudgeBench C3 主要位于此处；共享参考造成的锚定可与 EX-001 的共享证据依赖、EX-002 的解释失败合并研究。不能仅凭 C3 宣布一个新的上游真值门。
2. **评分目标完整性问题：** `Rs` 对任务契约的映射有误，更多独立 judge 或更完整的 trace 仍可能共同服从错误评分标准。OpenAI 题面／测试错配、τ³ expected-action 修复、GeneBench 的可恢复目标选择为这一问题提供机制案例，但没有完成统一的正交实验。
3. **覆盖／解释问题：** 判断依据正确，但验证器遗漏应检查的状态、只看到部分证据或误解证据。这部分应归 EX-002，不宜因为它发生在 benchmark 中就全部转交 EX-004。
4. **成功来源归因问题：** 固定有效 `Rs` 后，评测中获得的目标值是否改变 agent 成功概率？AcquaBench 在 eligible population 上提供直接干预；这是不同于“答案对不对”的 estimand。但 D2 的单源检测失败本身属于 EX-002 的观测单位边界，不能单独证明 provenance 独立于一切 evidence interpretation。

### 4.2 哪些可以合并，哪些暂不应合并

| 对象 | 与 EX-001／002 的可合并部分 | 暂不能完全合并的理由 | 会迫使收窄／合并的证据 |
|---|---|---|---|
| reference integrity | shared-GT 锚定纳入 EX-001；有正确目标但未取得／误读证据纳入 EX-002；低覆盖测试也属于覆盖问题 | “依据是否忠实表达任务”与“谁独立检查、检查了什么”是不同错误位置；检验错误标准不能由多次忠实执行自动修复 | 所有可重复 reference 效应都来自呈现／覆盖；在明确契约和完整证据下，既有独立验证方案已能检测全部目标错配，额外 reference 审计没有预先定义的实质增益 |
| success provenance | 单源／多源检测与信息恢复纳入 EX-002；共享训练来源或参考来源的共同偏差纳入 EX-001 | outcome 与 exposure 不直接识别反事实依赖；AcquaBench 值替换有自己的干预与指标，即使 outcome scorer 固定仍可测量 | 在非构造任务和语义稳健 scorer 下，预先定义的完整证据审计可同样可靠识别该依赖，额外 provenance 实验无决策增量；或实际任务只要求合法终态，不声称测量未借助目标答案的能力 |

上述最后一列是**研究证伪标准，不是本轮已观察结果**。若把 EX-002 定义为“一切能知道真相的推理”，当然可以吞并其他问题，但这个宽定义无法形成可检验比较；反过来，仅把原本遗漏的变量改名为新门也没有价值。

### 4.3 暂定判定的强度

- **Evidence-supported inference：** 当前材料足以支持两个可操作对象：`Rs` 对任务的有效映射，以及成功对评测期间 target-value intervention 的依赖。两者可共享记录格式，不宜把“修复参考”与“取得正确目标值”混为一种干预。
- **Evidence-supported inference：** 不建议把 EX-004 整体并入 EX-001。不同生成／验证实现仍可能共享一个错误 reference；但来源中的多模型对照并没有直接测出四轴独立性之后的剩余效应。
- **Reasoning／仍待证伪：** reference integrity 可作为“分数能否解释为任务正确性”的有效性前提；success provenance 只在需要把分数解释为特定能力、合规路径或信息边界下的成功时成为审计需要。二者不是保证任务成功的充分条件，也不要求每次工作都由外部人类判定。
- **尚不支持：** 两个门在所有领域都必要、彼此统计独立、独立于 EX-001／002，或者任意一门失效必然导致错误。良好 verifier 可能拒用坏参考；错误参考偶尔也可能给出正确判决；被暴露的答案未必被依赖。

因此本笔记的建议 delta 是 **refined**：保留同一 EX 内两个对象，合并重复的锚定／覆盖机制；优先补运行身份、参考版本和独立裁决证据。本笔记不执行 agenda 状态变更，也不新建 Claim。

S7–S9 的字段补充如下：

| 来源 | reference trust/control | provenance observability | external adjudication / result boundary |
|---|---|---|---|
| S7 agent-infra | trusted-side `graderRef`、version/digest、agentVisible/graderOnly、sanitized result | 不测 source-value 依赖；只规定哪些数据不得进入 Subject | Provider/Grader/Reporter 是角色设计；`blocked` 与 `failed` 分开，不证明 grader 真值 |
| S8 agentprov | 不操纵 benchmark reference；ground truth 单独保存 | lossy visible trace、laundering、origin-leak floor、coverage | held-out truth 是评分基准，不是独立人类 run-level oracle；安全/成本/归因分开 |
| S9 tracegym | reference/baseline 可回放对照；正确性未外部确认 | tool/LLM spans 和 replay 增加可见性，不证明解释正确 | review/calibration 是工程流程，不是外部真值 |

因此新增材料只改变字段设计与实验设施候选，不改变“尚无联合因果证据”的裁决。

## 5. 新问题、证伪方向与 Source 需求

| 新问题／证伪方向 | 所需一手材料 | 下一步可改变什么判断 |
|---|---|---|
| AgentJudgeBench 表 1／2 的同名 GT 为什么不同？是否因配置、子集或版本不同？ | 作者 C3 run manifest、同一 record 的三条件 verdict、生成输出 hash、scorer／prompt commit；另需多标注者且盲于程序分数的人审 | 先决定 C3 的定量比较能否接受，再判断参考内容效应是否只是解释／锚定问题 |
| AcquaBench 的整体值替换效应能否由公开数据复算？有多少 G−S 来自 SHAM 伤害？ | 作者冻结全量 trace、artifact、eligibility 清单、scorer hash、paper-to-run 映射；材料名称可从 SOURCE_BASELINE 回溯，但本轮未取得归档 | 复算 G−C、G−S、net rescue 和聚类区间；防止把 9 条演示或单条标签当作总体因果证据 |
| 如果用多源语义审计替换 coloc，EX-004 的 provenance 是否还有额外诊断价值？ | 作者／官方发布的 full-source replay、明确的授权信息契约、经独立裁决的多源任务 | 若增强证据审计已能达到预注册等价标准，provenance 可并入 EX-002 的操作子项；仅修复单源 detector 不等于完成归因 |
| τ³ 得分提高中，reference-only 修复占多少，题面与模拟器变化占多少？ | 官方旧／新 task 与 evaluator 组合、同 trace 重评分、原始 trial 配置及修复分类 | 区分测量变动与 agent 行为变动；不从版本级 +14–20pp 反推纯 reference 效应 |
| 开放科学／代码任务是否存在独立而不过度狭窄的 oracle？ | GeneBench 全题目标说明／消融／独立复核记录；OpenAI 逐题审计标签和可重放 harness | 判断“纠正参考”是恢复契约，还是用另一套偏好替换原偏好；检查合理多解与 oracle 分歧 |
| hidden ledger 与 visible trace 的实现是否能通过跨实现 conformance？ | `agent-infra` contract、`agentprov` origin-leak checks、`tracegym` replay/gate；需要固定版本运行清单和泄漏测试 | 判断身份/暴露控制是可执行门，还是仅停留在仓库设计 |

这些是本笔记中的 Source 需求，未写入 research agenda。现有六类材料已足以定位设计缺口，本轮没有再扩展 PatchDiff、ELT-Bench-Verified 或 SWE-bench Verified 原始论文；Verified 仅使用用户指定的 OpenAI 官方审计。

## 6. Reasoning：下一步最小实验

**先修正实验单位：不能既固定完整 trace，又声称测量改变 agent 信息来源后的行为效应。** reference 的 judge-side 干预发生在运行之后；success-provenance 的干预发生在运行之前或中途。两者应分阶段交叉，且把 agent 的可见信息与 verifier 的可见证据分别记录。

### 阶段 A：固定 trace 的 reference 重评分

先从一个可重放任务族选 8 个任务作为设计试验：4 个明确唯一结果，4 个允许语义等价方法／调用顺序。数量只是低成本排查实验是否成立的建议，不作有统计功效的必要性检验。预先由两名不接触候选评分的审查者依据任务契约与执行状态裁决，分歧另行裁定或标作 unknown；外部 `O`、task、trace 和工具／预算被冻结。

同一条 trace 分别给予 judge `Rj = none / correct / semantic-equivalent / wrong`；保持 reference 块结构尽量匹配。固定 `Rs`，用 `O` 计算 judge 的 false accept／false reject；再单独对有明确历史修复的任务使用旧／修复 `Rs` 重评分，避免把 `Rj` 和 `Rs` 一起改动。每次判定均是 fresh context，防止条件间泄漏。

先在一个固定 verifier 和完整 evidence packet 上定位差异，再对出现差异的配对增加一个不同实现的 verifier、一个删减后的 evidence packet，形成最小的跨条件复查。不同实现只代表一个独立性操作因子，不能声称覆盖 EX-001 全四轴。即使局部差异仍存在，也只支持局部反例，不证明普遍必要性。

### 阶段 B：相同初始状态的 provenance 重运行

只选其中 4 个适合可控信息获取的任务；冻结初始环境、授权信息、agent 配置、scorer 和外部 `O`，分别运行 CLEAN／GOLD／SHAM，至少 3 个配对种子，得到 36 条运行。这是机制 pilot；正式规模按 pilot 方差、最小实质效应和预注册功效确定。

GOLD／SHAM 的来源位置、格式、长度与访问机会尽量一致，仅替换目标值；允许下游动作和 trace 改变。保留未暴露、失败、截断等所有预注册有效运行，按分配条件计算 G−C／G−S；实际 exposure 是中间变量，不在主分析中事后筛选它来伪造配对。重新运行可能出现模型端非确定性，故 seed 相同不是确定性保证。

将每条已生成 trace 再送入阶段 A 的 reference／verifier／evidence 配置。由此区分：来源干预对 agent 结果的影响、reference 对 judge verdict 的影响、证据删减对审计的影响。以 task 聚类报告配对差异与不确定性；报告 outcome 及归因两种指标，不把主观合理的解释转为事实标签。

最小记录包含 `task_version / initial_state_hash / trace_id / model_config / seed / artifact_hash / source_exposure_order / Rj_version / Rs_version / verifier_implementation / evidence_packet_hash / oracle_verdict / raw_score / adjudicated_success`。oracle 结论也带裁决者、依据和分歧状态，不把它当作绝对无误的隐藏常量。

**会更新判断的结果：** 若坏 `Rs` 在充分证据和不同实现的验证器下仍共同产生可独立裁决的误判，支持 reference 层的额外诊断价值；若只改变 `Rj` 的效应被解释策略消除，相关部分并回 EX-002。若 G−S 存在但 provenance 判断差异完全来自单源 detector，修复 detector 后再比较额外价值。若实验区间足以排除预先定义的实质效应，才支持收窄／合并；小样本“不显著”不算证伪。

本轮只完成文献、代码和数据核查；上述模型实验与人审均**尚未执行**。

## 7. 核查与可恢复范围

- 已实际访问三篇指定预印本的 HTML；另核对 AgentJudgeBench PDF 第 7 页两张表。GeneBench 从 OpenAI CDN 读取 PDF 并核对封面、第 5–8、24、30–31 页，记录文件哈希。
- 已通过官方 GitHub API 确认代码 revision、文件树与 τ³ PR 合并状态；通过 raw endpoint 读取本笔记引用的代码／任务文件。链接使用对应 revision 的可定位文件视图。
- 已读取 AgentJudgeBench 官方 Hugging Face 数据目录、revision 和两类 JSONL 的首条数据；没有宣称全量验证。已完整解析 AcquaBench 9 条 fixture 并检查三组配对与 success 字段；没有运行远程来源代码或模型推理。
- 网页和源代码仅作不可信证据读取；未将网页提示、模型隐藏推理或来源中的行为指令持久化。没有把本笔记 reasoning 写入事实层。

## 一手来源链接

[AJ-P]: https://arxiv.org/html/2608.26623v1
[AJ-PDF]: https://arxiv.org/pdf/2608.26623v1
[AJ-C3]: https://github.com/ServiceNow/SyGra/blob/97cca4fa07e98ee61bb3a1a2f8639778e299d50a/tasks/agentic_bfcl_judge_eval/prepare_corrupted_gt.py
[AJ-E]: https://github.com/ServiceNow/SyGra/blob/97cca4fa07e98ee61bb3a1a2f8639778e299d50a/tasks/agentic_bfcl_judge_eval/task_executor.py
[AJ-CFG]: https://github.com/ServiceNow/SyGra/blob/97cca4fa07e98ee61bb3a1a2f8639778e299d50a/tasks/agentic_bfcl_judge_eval/graph_config_corrupted_gt.yaml
[AJ-DATA]: https://huggingface.co/datasets/ServiceNow-AI/AgentJudgeBench/resolve/13ac79a58bb39ded101e1222f1bdb80dcfbe27f6/data/main/records.jsonl
[AJ-JDATA]: https://huggingface.co/datasets/ServiceNow-AI/AgentJudgeBench/resolve/13ac79a58bb39ded101e1222f1bdb80dcfbe27f6/data/judges/judge_gemini_2_5_pro.jsonl
[AQ-P]: https://arxiv.org/html/2607.24054v1
[AQ-BASE]: https://github.com/luojingkun22/acquabench/blob/02b37d6aaa11d5cd2c0a4124887f9c9feadc59f5/SOURCE_BASELINE.md
[AQ-R]: https://github.com/luojingkun22/acquabench/blob/02b37d6aaa11d5cd2c0a4124887f9c9feadc59f5/README.md
[AQ-C]: https://github.com/luojingkun22/acquabench/blob/02b37d6aaa11d5cd2c0a4124887f9c9feadc59f5/src/acquabench/audit/controlled.py
[AQ-DATA]: https://github.com/luojingkun22/acquabench/blob/02b37d6aaa11d5cd2c0a4124887f9c9feadc59f5/src/acquabench/demo_data/traces.jsonl
[ABC-P]: https://arxiv.org/html/2507.02825v5
[ABC-C]: https://github.com/uiuc-kang-lab/agentic-benchmarks/blob/ae1124758098876db04336e1d8c6e419a139c6e3/ABC.md
[ABC-A]: https://github.com/uiuc-kang-lab/agentic-benchmarks/blob/ae1124758098876db04336e1d8c6e419a139c6e3/assessments/tau-bench.yaml
[ABC-R]: https://github.com/uiuc-kang-lab/agentic-benchmarks/blob/ae1124758098876db04336e1d8c6e419a139c6e3/README.md
[G-P]: https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf
[T-F]: https://taubench.com/blog/tau3-task-fixes.html
[T-PR]: https://github.com/sierra-research/tau2-bench/pull/175
[T-OLD]: https://github.com/sierra-research/tau2-bench/blob/37199f36924c8896f5e048360691f8476cd89ba1/data/tau2/domains/airline/tasks.json
[T-NEW]: https://github.com/sierra-research/tau2-bench/blob/01e812d1d1c4df6d8d2299bf175e482527112244/data/tau2/domains/airline/tasks.json
[T-POL]: https://github.com/sierra-research/tau2-bench/blob/01e812d1d1c4df6d8d2299bf175e482527112244/data/tau2/domains/airline/policy.md
[T-E]: https://github.com/sierra-research/tau2-bench/blob/01e812d1d1c4df6d8d2299bf175e482527112244/src/tau2/evaluator/evaluator.py
[O-P]: https://openai.com/index/separating-signal-from-noise-coding-evaluations/
[O-V]: https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/
[S7]: https://github.com/fitlab-ai/agent-infra/blob/main/docs/en/benchmark.md
[S8]: https://github.com/webpro255/agentprov
[S9]: https://github.com/hoomanesteki/tracegym-ai-agent-evaluation
