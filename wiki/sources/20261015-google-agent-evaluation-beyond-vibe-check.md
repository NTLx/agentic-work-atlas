---
type: source-summary
title: "Evaluating AI agents: moving past the vibe check"
canonical_url: "https://developers.googleblog.com/evaluating-ai-agents-moving-past-the-vibe-check/"
raw_state: index
original_raw_file: "20261015-google-agent-evaluation-beyond-vibe-check.md"
original_body_sha256: "4dc6e9b0be0fa4aba1dee320d3d0ca2eb8363060d67cd26aad8c594e518fe882"
indexed_at: "2026-11-06T08:59:07.828Z"
created: 2026-11-06
updated: 2026-11-06
tags:
  - source-summary
  - agent-evaluation
evidence_level: medium
claim_type: mixed
source_locator:
  - "Getting started: the high-level building blocks > Define success with critical user journeys"
  - "Start with simulated users, graduate to real traffic"
  - "Measure across the full stack"
  - "Four common traps to avoid > Trap 1–4"
  - "A practical Day 0 to Day 2 rollout > Day 0: Scenarios, simulations, and the red pen"
  - "Day 1: Cadence, signal, and the testing framework / The tuning loop"
  - "Day 2: Merge gates and shared dashboards"
---

# Evaluating AI agents: moving past the vibe check

> 一手来源：[Google Developers Blog（2026-10-15）](https://developers.googleblog.com/evaluating-ai-agents-moving-past-the-vibe-check/)，作者 Hugo Selbie、Dani Zamora、Jesse Carah、John DeMartino。2026-11-06 已阅读原文。本文为自撰编译及定位索引，未复制原文全文；具体引用应回到官方页面核验。作者所述示例与实践建议不自动构成通用实证结论。

**原文保留边界**：本来源按官方稳定链接结算为可恢复索引（raw_state: index）。临时 Raw 仅为注册用来源记录，original_body_sha256 是该记录的哈希而非原网页正文哈希；不可据此宣称保存或校验了全文。须按 canonical URL 与 source_locator 回查证据。

## 编译摘要

### 1. 浓缩

- **核心结论 1：Agent 评测先定义用户真正要完成的关键旅程（CUJ），再从它派生可观察的成功条件。**
  - **原文证据**：在 “Define success with critical user journeys” 中，金融运营分析员对交易差异邮件的处理被拆为核对正确交易、查询内部账簿、将内部 ID 转回券商用语等多项明确检查；作者建议依据 persona、目标、约束和验证条件建立场景。尚无真实日志时先模拟用户的错别字、信息不全和多轮交流，积累初始 traces；再用真实生产流量替换/扩展合成情景。
  - **可操作抽象**：以 business journey → scenario → expected state transitions → observable oracle 组织黄金测试集，而不是抽样问模型几个问题后凭手感批准。

- **核心结论 2：单项总分无法定位原因，评测应该同时约束过程、结果与资源消耗。**
  - **原文证据**：“Measure across the full stack” 提出 unit tests、deterministic metrics、LLM-as-a-judge rubrics、integration tests 四层；“Four common traps” 特别指出：不得为了好看频繁更换 golden dataset；将模糊 1–5 分尽可能改写为可以按事实核验的布尔问句；同时测 latency、tokens、API cost、tool-call counts；用 OpenTelemetry/OpenInference 约定让 LangGraph、ADK 等不同 Harness 的轨迹可比较。
  - **关键区分**：**布尔式 LLM Judge 仍是模型判定，不是确定性程序测试**。只有可通过代码或权威状态检查的 contract，才可升级为硬性确定性断言。

- **核心结论 3：从 Day 0 人工识别 failure mode，到 Day 1 固定回归，再到 Day 2 PR merge gate，逐步形成可审计反馈环。**
  - **原文证据**：Day 0 阅读并标注少量原始执行 Trace，找出工具误用、参数幻觉、重试与冗长动作；Day 1 用 agent-eval 等工具运行多轮场景，且用人工标注反向校准 judge，改模型、提示或工具描述时保持测试集不动；Day 2 将总通过率阈值（95% 是作者举例）与核心指标零回归作为两道 PR 门，并存 prompt hash、模型版本、Trace JSONL、时延与 token 账单。生产失败案例再经审阅提升为新测试。
  - **与已有知识衔接**：[[20261008-google-aqua-production-agent-quality]] 负责部署后的质量故障发现与聚类，本篇负责明确在上线前/每次变更时如何定义验收 oracle。

### 2. 质疑

- **Golden dataset 冻结 vs 真实案例持续沉淀**：二者并不冲突，但应给测试集版本、固定比较窗口、扩展测试集单独评估。若每次评测都暗改样本与权重，前后指标不可比较。
- **人工标注仍需质量控制**：20 条 Trace 可快速发现具体 bug，但可能漏掉稀有失败与长尾场景；标注者间分歧、真实生产分布漂移、泄漏到训练/提示的答案都可能使 Oracle 退化。
- **Judge 校准和独立性**：布尔化消除了部分评分歧义，但无法天然消除判定者共模错误、评价污染或奖励黑客；关键发布门应优先由权限、工具状态、业务数据等程序可核验事实支撑。
- **平台适用性**：原文展示 Google 的 agent-eval/Gemini 平台集成，是工程方法与样例，不是对所有框架或行业达到指定准确率的实证证明；“50–60 次调整”不是固定规律。

### 3. 对标与约束（跨来源综合，不作为原文事实）

| 层 | 本篇 Google 方法 | 对应既有知识 |
|---|---|---|
| 业务契约 | CUJ/角色/目标/约束/Success oracle | [[Verifiable-Agent-Engineering]]、[[Evaluation-Set]] |
| 判定器 | deterministic assertion + 校准的 boolean judge | [[Rubric-Based-Evaluation]]、[[Evaluator-Miscalibration]] |
| 过程证据 | OpenTelemetry/OpenInference、Trace、tool calls、成本 | [[Agent-Verification]] |
| 回归门禁 | 冻结数据集，逐改逐测，核心关键能力零回归 | [[Evaluation-Integrity]] |
| 生产外环 | 生产 traces 发现新 failure mode 回灌测试集 | [[20261008-google-aqua-production-agent-quality]] |

- **对 LLM WiKi/ChatGPT Worker 的综合推论**：把“队列返回 started / 工具返回成功 / Discord 已发出”分别对应不同的验证状态；每个 Worker 应有关键用户旅程、终态验收条件、故障回放语料和可解释的成功判据。是否引入 agent-eval 工具应先看现有 n8n traces 是否具备采集契约，不凭文章自动升级技术栈。
- **约束分类**：硬约束是可信外部状态与权限；软约束是团队选定的 release threshold 和预算；可调整假设是使用哪个 Agent 框架、哪个 judge、多少人工评测样本。

## 重要判断（Claim / Evidence / Boundary）

- **判断（综合）**：端到端 Agent 的可发布性须联合评价成功结果、执行路径、外部副作用与成本，并以未被同一变更静默修改的成功契约作比较。
- **证据**：本篇 “Four common traps to avoid”“Day 0 / Day 1 / Day 2”，以及独立的 [[20261008-google-aqua-production-agent-quality]] 生产故障诊断案例。
- **边界**：两篇均来自 Google 官方工程材料，构成互补方法而不是统计意义上独立验证的两份效果证据。

## 关联概念

- [[Verifiable-Agent-Engineering]]
- [[Evaluation-Integrity]]
- [[Evaluator-Miscalibration]]
- [[Agent-Verification]]
