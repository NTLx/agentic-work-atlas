---
type: entity
title: Evaluation Set
aliases:
  - Evaluation Set
  - 评测集
  - AI 评测集
definition: "把真实业务判断、边界案例和验收规则显式化为可复用测试样本，用来评估、迭代和迁移 AI 系统行为的关键资产"
created: 2026-05-23
updated: 2026-10-12
tags:
  - AI-evaluation
  - AI-deployment
  - enterprise
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[Forward-Deployed-Engineer]]"
  - "[[Tacit-Knowledge-Lock-In]]"
  - "[[Integration-Wall]]"
  - "[[Hardware-Sovereignty]]"
  - "[[Distributional-Alignment]]"
  - "[[Specialized-Small-Models]]"
  - "[[Transparent-Tool-Handoff]]"
source_raw:
  - "[[The Return of the Deployment Company]]"
  - "[[Specialization Beats Scale A Strategic Variable Most AI Procurement Decisions Overlook]]"
  - "[[20260730-palantir-responsible-ai-evals-prototype-to-production]]"
  - "[[20260730-lenny-anthropic-first-technical-pm-dianne-penn]]"
  - "[[20260901-google-ai-evaluations-trust]]"
  - "[[20260901-databricks-genie-ontology-data-stack]]"
  - "[[20260930-openrouter-golden-eval-production-traffic]]"
  - "[[20260930-openrouter-agent-regression-testing]]"
---

# Evaluation Set（评测集）

> [!definition] 定义
> **Evaluation Set（评测集）** 是把真实业务判断、边界案例和验收规则显式化为可复用测试样本的资产。它不只是模型评分工具，也是企业工作流知识的载体：谁有权访问、导出和复用评测集，谁就掌握了 AI 系统持续迭代的关键控制点。

## 关键数据点

- Caffein Chen 文章将 FDE 的共同假设概括为：AI 商业化不能只靠 SaaS 式自助上手，需要有人进入客户现场，把客户隐性知识编码进评测集。
- 保险理赔例子说明，真正的业务规则常常不在 SOP 里，而在资深员工对例外、争议、客户等级和签核习惯的判断中。
- 文章建议企业在签 FDE 合同时明确评测集 IP、合同终止后的删除或移交、导出格式、是否可被供应商用于同业客户。
- 在 on-prem 或内部能力建设场景中，评测集、提示配置和交互日志留在企业内部，是保持数据主权和模型迁移能力的基础。
- DharmaOCR 案例说明，评测集也是模型采购的判别器：只有在真实任务 benchmark 上比较质量、成本和稳定性，企业才能发现专门化小模型是否优于更大的通用模型。

## 运行时生命周期：评测集作为迭代引擎

Palantir AIP Evals 文（2024-10）把评测集从"资产"升级为"迭代引擎"，给出单元测试范式的完整生命周期：

1. **构建 Test Bench**：用 ontology 历史数据生成 Object Set-backed Test Cases（如用专家标注的历史召回决策作 ground truth）。
2. **定义 Evaluators**：内置 no-code 比较器（如 Exact Boolean Match）/ 自定义 Python/TypeScript / LLM-as-judge。
3. **重复运行**：每个 test case 默认跑 3 次以应对 LLM 非确定性。
4. **Drill-down 迭代**：aggregate 指标定位失败案例 → 检查 inputs/intermediate outputs/final response → 三种修复路径（改 prompt / 补数据 / 加 tool handoff）→ re-run 防回归。

示范曲线：产品召回系统准确率 41.3% → 修 prompt（补充 expert review 触发条件）→ 93.3% → 剩余失败定位为 LLM 数学错误（1.865 vs 正确 1.864）→ handoff 给 Calculator tool（[[Transparent-Tool-Handoff]]）→ 通过。

Anthropic 产品团队的 "evals are the new PRDs"（[[20260730-lenny-anthropic-first-technical-pm-dianne-penn]]）从 PM 工作流侧确认同一趋势：用户反馈 → 读失败轨迹 → 凝结为 eval set → 可度量改进，evals 取代 PRD 承担需求定义功能。两条线索（平台基础设施视角 + PM 工作流视角）互为验证。

⚠️ 边界：ground truth 来自人类历史决策时，evals 只能收敛到人类历史判断，不能超越它；3x 重复是朴素处理，pass@k 阈值与分布偏差校正才是真正的工程难点（参见 [[Evaluator-Miscalibration]]）。

## 评测题目设计的信号质量

Google Developer Relations（2026-09）补充了评测集的题目设计约束：题目必须足够难以越过 baseline ceiling，每个 prompt 测试独立能力，grader 只评分 prompt 明确要求的结果；除非路径本身是需求，否则应评估最终目的而不是固定工具调用轨迹。[[Rubric-Based-Evaluation|基于评价标准的评估]] 因而不只是写 scorer，还要先保证测试题目产生可区分、低重叠的信号。

**判断**：评测集的信号质量首先取决于题目是否能区分工具增量、覆盖独立能力并避免把未声明的要求偷偷交给 grader。
- **证据**：[[20260901-google-ai-evaluations-trust]]
- **边界**：这些规则来自实践指南，不是带对照组和置信区间的因果研究；多轮交互、审批顺序或安全停机只有在被明确写入需求时，才应进入路径 rubric。

## 评测集的业务语义治理

Databricks Genie Ontology（2026-09）把评测集推进到业务语义治理：每个优先业务域要维护代表性问题、expected answer、authoritative source、ground truth、acceptance criteria、人工 review 和阈值。回答失败后，修复应回到真正承载错误的 Page、Metric View、元数据、权限、认证状态或 Agent instructions，而不是盲目改 prompt。

**判断**：评测集不仅定义题目测什么，还要定义在什么业务语义、权限上下文和权威来源下算对。
- **证据**：[[20260901-databricks-genie-ontology-data-stack]]
- **边界**：Databricks 的闭环来自厂商产品材料，没有独立证明每个治理动作在不同企业中的因果效果；同一问题因权限不同而有不同答案时，评测集需记录权限上下文。

## Golden Set：把生产分布变成版本化回归契约（2026-10）

OpenRouter 的 production-derived golden eval 教程（[[20260930-openrouter-golden-eval-production-traffic]]）补上了评测集从“业务资产”变成“可复现部署契约”的完整构造路径。关键不是随机抽一批线上请求，而是同时保存**真实分布**与**高风险尾部**：

```text
Golden eval contract
= production-distribution sample
+ risk-weighted tail
+ reviewed expected behavior
+ rubric / evaluator
+ provenance metadata
+ frozen baseline
```

生产流量给出真实用户频率与失败模式，但纯频率采样会让低频、高损失 case 被 head traffic 淹没。因此评测集既要忠实表示 observed distribution，又要主动 overweight critical tail；synthetic case 更适合作为有 provenance 的补洞层，而不是静默混入真实流量。

**第一轮 eval 也在验证 oracle 本身。** 来源要求 domain expert 标注 expected behavior，并用 reviewer disagreement 暴露 rubric ambiguity；baseline 失败应继续区分真实系统失败、错误/含糊的 expected answer、以及 evaluator defect。也就是说，评测文件并不会因为被命名为 golden 就自动成为 ground truth。

另一个重要增量是版本治理：

```text
Eval Result
= f(dataset version,
    rubric/evaluator version,
    baseline version,
    system configuration)
```

**判断**：dataset、rubric 与 baseline 应被视为同一个 provenance unit。若三者在不同时间静默漂移，分数变化就无法归因。真实流量进入评测集时的 PII scrub、截断、重写等 transformation 也应记录，因为它们可能改变 case 难度与语义。

最后要区分两个时间尺度：**跨 product epoch 要 refresh golden set；单次 candidate comparison 内必须冻结 set/rubric/baseline。** 前者适应分布漂移，后者保证实验可比性，并不矛盾。

- **证据**：[[20260930-openrouter-golden-eval-production-traffic]]，production sampling、dedup/cluster、expected outputs、first evaluation、Git/CI 与 cross-model benchmarking 段落。
- **边界**：来源是平台教程；20–50、100–1000 等样本规模和刷新周期是经验建议，不是普适阈值。生产流量也会继承历史偏差和既有盲区，真实分布不等于完整分布。

## Locked case set：可比性本身是一等资产（2026-10）

[[20260930-openrouter-agent-regression-testing]] 把评测集的版本治理进一步精确化：**评测集可以长期演化，但在一次 regression comparison 内必须被冻结。** 如果测试过程中顺便重写 case，candidate 与 baseline 的 measurement condition 已经不同，历史结果不再可比。

```text
长期生命周期：
production drift
  → refresh / add cases
  → new eval-set version

单次实验：
exact eval-set version
  → freeze
  → baseline run
  → candidate run
  → compare
```

**判断**：case-set edit 应视为 experiment/schema boundary，而不是无害的测试维护。只有在新版本明确建立新 baseline 后，才能继续做纵向回归比较。

这条规则与上一节 Golden Set 的 refresh 要求构成两个时间尺度：

- **between epochs**：根据生产分布、新失败和产品行为更新 Evaluation Set；
- **within an epoch/comparison**：冻结 case、rubric 与 execution envelope，避免 treatment 与 measurement 同时变化。

来源还补充一个重要的 evaluation provenance 边界：Agent 的 execution fixture 不只包含题目本身，也包含 concrete model、tool schema/results、retrieval/context、judge、inference parameters，以及 `AGENTS.md` / `CLAUDE.md` / skills 等隐式 instruction source。若这些变量未记录，所谓“同一评测集”也未必是在测试同一个系统条件。

- **证据**：[[20260930-openrouter-agent-regression-testing]]，locked case set、three kinds of change、model-swap 与 hermetic run 讨论。
- **边界**：structural path 不应因为容易断言就被写进所有 case；只有路径本身属于业务契约时才应成为 oracle，否则会把实现细节误写成产品要求。

## 前提与局限性

- 评测集的价值取决于样本是否覆盖真实工作流、边界案例和失败模式；只收集 demo 成功案例会制造虚假的可靠性。
- 评测集不是中立资产。它可能间接包含客户数据、商业规则和敏感决策逻辑，因此也会成为合规和商业秘密问题。
- 评测集可导出并不等于可迁移。若格式、标注规范、业务语义和运行环境都绑定在单一供应商平台上，迁移成本仍然很高。

## 关联概念

- [[Forward-Deployed-Engineer]] — FDE 在现场提取和维护评测集
- [[Tacit-Knowledge-Lock-In]] — 评测集如果不可导出，会成为新的供应商锁定机制
- [[Integration-Wall]] — 评测集必须覆盖真实生产约束，而不是只验证沙盒能力
- [[Hardware-Sovereignty]] — 本地部署让评测集和推理日志保留在企业控制范围内
- [[Distributional-Alignment]] — 评测集把训练历史是否贴近部署任务变成可观察证据
- [[Specialized-Small-Models]] — 小模型是否足以进入生产，取决于评测集上的质量、稳定性和成本表现
