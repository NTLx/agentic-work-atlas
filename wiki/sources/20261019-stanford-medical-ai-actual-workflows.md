---
type: source-summary
title: "Measuring What Medical AI Can Actually Do"
canonical_url: "https://hai.stanford.edu/news/measuring-what-medical-ai-can-actually-do"
raw_state: index
original_raw_file: "20261019-stanford-medical-ai-actual-workflows.md"
original_body_sha256: "e4a9bd1f06e4fa4135ec77e1f850e1acf42a871dc7484abf719afe95e9903d24"
indexed_at: "2026-11-08T00:00:00+08:00"
created: 2026-11-07
updated: 2026-11-07
tags:
  - source-summary
  - agent-evaluation
  - healthcare
evidence_level: medium
claim_type: mixed
source_locator:
  - "Opening / clinical exams versus EHR chart, orders, documentation"
  - "MedHELM: Mapping the Whole Job / MedAlign 983 questions, 29 clinicians, 5/22/121 taxonomy"
  - "MedHELM: Mapping the Whole Job / 37 datasets, 9 models, calibrated LLM jury and five category pairwise win-rate ranges"
  - "Tasks Are Workflows / priors, EHR, payer portals, factual environment state"
  - "PhysicianBench and MedAgentBench / MedAgentBench 300 tasks and newer results belong to different benchmark"
  - "PhysicianBench and MedAgentBench / PhysicianBench 100 tasks, 21 specialties, 27 calls, 670 checks, 46% best single-run, 28% repeatability"
  - "PhysicianBench and MedAgentBench / 62% and 73% note-without-EHR-action among action-execution failures"
  - "HealthAdminBench / 100+ hours observation, 4 synthetic environments, 135 tasks, 1177 deterministic + 521 LLM verifiers"
  - "HealthAdminBench / 36.3% best end-to-end; GPT-5.4 82.8% subtask vs 26.7% whole"
  - "Reading the Benches Together / 46% and 36% not directly comparable"
  - "Primary abstracts: https://arxiv.org/abs/2605.02240 and https://arxiv.org/abs/2604.09937 / scope and publication difference"
---

# Measuring What Medical AI Can Actually Do

> 来源：[Stanford HAI，2026-10-19](https://hai.stanford.edu/news/measuring-what-medical-ai-can-actually-do)，Nigam Shah、Jonathan Chen；2026-11-07 已读取原文，并查阅文章所链接的 PhysicianBench（[arXiv:2605.02240](https://arxiv.org/abs/2605.02240)）与 HealthAdminBench（[arXiv:2604.09937](https://arxiv.org/abs/2604.09937)）**论文摘要**作交叉核对。尚未逐页审阅两篇论文的全部方法、统计表或开源仓库，数据和解释主要归于 Stanford 作者。官网是研究传播与整合文章而不是单独新 benchmark 论文。

**来源保留边界**：官方原文通过 canonical URL 和章节定位可回查；Wiki 保存原创分析，不复制外部全文。临时 Raw 只用于 Registry 来源登记，original_body_sha256 **只对应此登记记录，不是官方原文正文的哈希**；不能将本页视为全文镜像或独立 Evidence。

## 编译摘要

### 1. 浓缩

#### 核心结论 1：医疗 AI 从「知道医学答案」到「可在系统里完成临床任务」存在一个独立的执行能力鸿沟。

- **证据（opening / MedHELM）**：Licensing exam 只要求正确选项；临床任务需在 EHR 找到过往超声检查、合并本次化验、制定计划、**实际下达医嘱并记录**。2023 年 MedAlign 使用 15 位临床医生的 983 条 EHR 问题，原文称当时 GPT-4 约 35% 回答有误；在此基础上 MedHELM 请 29 位临床医生整理 **5 大类、22 子类、121 种实际任务**，并以 37 个 benchmark dataset 覆盖全部子类，评价 9 个 frontier model。
- **测量语义**：MedHELM 按医生定义准则由 LLM jury 比较，其报告的范围是 **pairwise win rate**，不是临床任务完成率或准确率。例如 administration/workflow 为 **0.53–0.63**，clinical decision support **0.63–0.77**；clinical note generation **0.74–0.85**，patient communication **0.76–0.89**。较弱的正是对真实医疗组织很重要的流程类工作，但不能将 win rate 数字与后面的端到端成功率直接比较。
- **核心判断（综合）**：医学知识、临床推理、工具权限、工作流记忆、执行确认、终态文书是不同能力；知道应该下什么医嘱不代表已经下达。构建医疗 Agent eval 必须冻结成功判据：**最终环境中到底发生了什么**。

#### 核心结论 2：PhysicianBench 暴露「写下正确医嘱计划，却未提交医嘱」的执行鸿沟；单次成功和重复成功差距明显。

- **证据（PhysicianBench and MedAgentBench）**：MedAgentBench 原有 300 个基于 100 个患者档案的单体任务（10 类），2025 年 best 小于 70%，2026 年作者称较新模型可超过 90%；这是另一套任务定义，不能拿它证明长期临床任务完成。
- **PhysicianBench 设计**：**100 个长程复合任务、21 个专科**，从医生间真实会诊转化而来，医生专家单独审核；每任务平均 **27 次工具调用**，共 **670 个 checkpoint**，检查资料检索、临床推理、EHR 动作执行和文书记录。重要操作由脚本在环境中检验实际医嘱/订单是否存在，推理与病历文字使用 LLM 判断。
- **结果（以 Stanford HAI 文为准）**：文章称在 12 个模型中 GPT-5.5 单次最优完成 **46%**，开源 DeepSeek V4-Pro **19%**；同一 GPT-5.5 只有 **28%** 的任务能在三次独立运行中均完成。稿件并称在**动作执行失败的子集**，GPT-5.5 的 **62%**、Claude Opus 4.6 的 **73%** 属于写对病历记载/行动计划却未在 EHR 真正执行。62/73% **不是所有任务失败率，也不是临床错误率**。
- **关键推论**：`documented_action` 与 `persisted_EHR_action` 必须拆开验证，并保留跨运行的一致性；不能以一篇“漂亮病历”或模型自报完成作为真值。

#### 核心结论 3：HealthAdminBench 量化了「各步看似正确，但整段流程失败」的可靠性塌缩。

- **证据（HealthAdminBench）**：研究团队称观察 Stanford Health Care 行政人员超过 **100 小时**，构造 4 个可操纵网页模拟系统（一个 EHR、两个 payer portal、一个 fax system），涵盖 **135 个完整任务**（60 prior authorization、60 appeals/denials、15 durable medical equipment），按 3 级难度安排。
- 评估包含 **1,698 个 verifier**：**1,177 个确定性检查 + 521 个 LLM Judge rubric**，全部使用合成患者数据；最佳 Claude Opus 4.6 computer-use 模式完整任务成功率 **36.3%**，最佳开放权重 Kimi K2.5 **15.6%**。**GPT-5.4 computer-use 的子任务通过率 82.8%，整项任务成功率仅 26.7%**。
- **失败类型**：跨页面/跨系统保留资料失败、遗漏附件下载上传、没有回退修复前序错误、运行预算耗尽。单步成功不可直接相乘推断整体完成，因为多个错误具有相依性和难度分布；真实 end-to-end 需查看最后确实提交到正确对象并有可检查的记录。
- **关键判断（综合）**：在多系统 Agent 中，核心质量指标应区分 `step_success`、`workflow_success`、`action_receipt`、`multi_run_consistency`、`risk_class`；界面操作步骤成功不是跨系统事务完成。

### 2. 质疑、冲突与限制

1. **不同 benchmark 的分母不可互换**：MedHELM 的成对胜率、MedAgentBench 的相对简单任务、PhysicianBench 的长程会诊、HealthAdminBench 的行政 GUI 是不同的对象。原文明确指出 **46% 和 36.3% 不能直接比较**，因为环境、接口、判定器和参与模型不同；不应用这两项排名某一个模型的通用临床能力。
2. **与原始论文摘要存在细节不一致**：Stanford HAI 文称 PhysicianBench 测了 **12 models**、测试于 **synthetically reconstructed patient records**；[PhysicianBench arXiv 摘要](https://arxiv.org/abs/2605.02240) 则写 **13 agents**、EHR 环境中的 **real patient records**。可能源于模型与 agent 配置计数、版本或描述差异，但**本次没有阅读全文核实原因，不自行调和，也不把“real records”当作已确认隐私边界**。两边的核心任务数 100、平均 27 次工具调用和 46% single-run 一致。
3. **Benchmark 的临床真实性 ≠ 临床部署安全**：PhysicianBench 任务来源于真实临床会诊并经医生审核，不等于临床试验中真实病患接受 Agent 决策；HealthAdminBench 由合成患者和模拟系统构成，更不涉及真实付款人或真实患者结果。外推仍需真实系统权限治理、隐私保护、human oversight、异地验证和 prospective outcome 研究。
4. **测量器组合不天然准确**：脚本能可靠检查订单存在与否，但不一定证明医学上应该开该医嘱；LLM Judge 评估推理/病历则可能与临床专家有误差。MedHELM 报告校准了 LLM jury 与医生间一致性，不能替代对其他两项研究各自 Judge 的独立审计。
5. **重复运行样本与稳定性**：28% 三次全成功不能直接与 46% single-attempt 推导独立重试成功率；模型输出、环境状态、tool budget 和错误相关性需要在实验设计中核对。
6. **错误严重程度混合**：一次遗漏转诊可能与病历格式问题一样在 aggregate task score 中被计为失败；做临床决策还需对错误严重性和可逆性分层，而不只是追求 pass@1。
7. **案例结果有时间与版本边界**：数字只是原文在 2026-10-19 报告的模型/环境/配置快照，不是“截至今天最新版模型”的结论。

### 3. 对标与应用约束（跨来源综合判断）

| 评测层 | 本文贡献 | 已有知识 | 最小验收证据 |
|---|---|---|---|
| 分类任务地图 | MedHELM 的 5/22/121 taxonomy | [[Evaluation-Integrity]]、[[Rubric-Based-Evaluation]] | 确认业务实际任务分母/类别 |
| 真实工作流 | PhysicianBench 100 例 × 平均 27 tool calls | [[Verifiable-Agent-Engineering]]、[[Agent-Harness]] | EHR 中持久化的实际动作和病历 |
| 行政 GUI | 135 tasks / 1,698 verifiers | [[20261019-langchain-numan-eval-first-health-coach]] | 跨系统/附件/提交回执和终态 |
| 评分装置 | scripts + LLM judgment，按对象各司其职 | [[Evaluator-Miscalibration]]、[[Evaluation-Integrity]] | 临床评审确认判据、证据链可重查 |
| 多次稳定性 | 46% single run 与 28% all-three | [[Agent-Verification]] | 预先规定的多次运行条件与一致性 |

**对医疗/生信 Agent 的启示（综合，未实施）**：真实生产验收应明确将“分析报告正确”“授权动作允许”“外部对象状态实际改变”“修改已被持久化”“可撤销/纠错”分为独立状态；临床范围必须由专业负责人批准，工具交互日志与真实回执不能被模型自然语言宣告替代。生信领域若要外推，需另定适当的实验/分析可验证终态，不能移植医疗具体任务通过率。

**对 n8n/LLM WiKi 自进化的类比（非原文结论）**：Queue Claim 返回 `started`、Worker 输出 `completed` 或发布消息说已成功，若无数据库读回和交付 ACK，仍是可能的执行失败；需用状态机持久化和目标端回执验证最终完成，而非把“模型知道应做什么”视为任务已做完。本次仅知识沉淀，不自动改造生产平台。

## 重要判断（Claim / Evidence / Boundary）

- **判断（综合）**：高风险多步骤 Agent 评测必须从答案质量转向执行效果，控制单步评分与整项完成之间的错误激励，验证真实外部状态并进行多次独立重复。
  - **证据**：Stanford HAI 原文「Tasks Are Workflows」「PhysicianBench and MedAgentBench」「HealthAdminBench」「Reading the Benches Together」，辅以两篇 arXiv 摘要交叉确认样本规模和主要结果。
  - **边界**：这些结果是模拟/重建环境下的研究评测，不是已被证明可自治执行临床医嘱或支付等不可逆行动的现实许可。

## 关联概念

- [[Evaluation-Integrity]]
- [[Verifiable-Agent-Engineering]]
- [[Evaluator-Miscalibration]]
- [[Agent-Verification]]
- [[Rubric-Based-Evaluation]]
