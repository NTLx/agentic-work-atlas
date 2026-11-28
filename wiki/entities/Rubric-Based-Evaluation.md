---
type: entity
title: Rubric-Based Evaluation
aliases:
  - rubric-based evaluation
  - rubric evaluation
definition: "用明确、可审查的任务相关判据评价Agent行为及产物，并与泛化质量指标互补的方法。rubric 可由二元、分级或其他判据组成，需与实际用例需求、参考标准及测量目标对齐。Microsoft 的 Agent Optimizer 可基于 rubric 失败自动生成候选修复。"
created: 2026-07-14
updated: 2026-11-28
evidence_level: high
claim_type: mixed
tags:
  - evaluation
  - production-agents
related_entities:
  - "[[Agent-Verification]]"
  - "[[Agent-Harness]]"
  - "[[Harness-Engineering]]"
  - "[[LLM-as-a-Judge]]"
  - "[[Evaluator-Miscalibration]]"
  - "[[Goodharts-Law]]"
source_raw:
  - "[[20261109-latentspace-handshake-frontier-labs-data]]"
  - "[[20260713-microsoft-ships-ai-agents-enterprise-scale]]"
  - "[[20260729-similarweb-langsmith-agent-report-evaluation]]"
  - "[[20260819-google-ai-evals-inspect-skill]]"
  - "[[20260901-google-ai-evaluations-trust]]"
---

# Rubric-Based Evaluation

## 分数与现实价值的断裂：专业依赖门禁及专家偏好（2026-11）

[[20261109-latentspace-handshake-frontier-labs-data]]（**10:03–11:37、27:38–31:30、1:31:18–1:48:52**）描述长期专业任务的评分逻辑：对数值结果采用确定性检查，辅以结构、交付和业务推理标准；遇到错误的税务前提、关键路径或违规行为，设置 **dependency gate / penalty trap** 避免在其后续污染的 100 多项子指标仍得分。对无法充分写成标准的专业 `taste`，在环境内增加专家 preference ranking。ATLAS 访谈口述平均约 146 项标准，而[官方 Benchmark 页面](https://joinhandshake.com/research/benchmarks/atlas-finance/)报告中位数 124.5；统计量不同，不能混用。

- **判断（综合）**：判据分成 `hard prohibitions`、`critical dependency gates`、`verifiable checks`、`professional preference` 和 `delivery quality`；对可辩护的两种行业假设，必须在任务输入明确指定适用原则，不能由 rubric 事后偷偷加条件。
- **证据**：[[20261109-latentspace-handshake-frontier-labs-data]]；[ATLAS-Finance 开源数据与环境](https://huggingface.co/datasets/handshake-ai-research/ATLAS-Finance)。
- **边界**：某个公司的分数权重及 grader 不构成跨金融/生信通用的阈值。专家偏好可能彼此冲突，需要多专家一致性校准。



> [!definition] 定义
> **Rubric-Based Evaluation** 是用具体任务相关判据评价Agent行为与产物的方法；与通用指标互补。rubric 是一组针对特定用例的评价标准；Microsoft 案例采用 yes/no 检查，但二元形式不是定义的必要条件。"Generic metrics tell you whether the agent works. They don't tell you whether the agent works right."（Marco Casalaina）

## 泛化指标的天花板

通用评估指标（groundedness、coherence、task completion）有用但有上限：
- groundedness/coherence 本身并不检查实际工具调用或全部路径；工具调用与中间步骤须有单独的轨迹证据及合同判据。

例：餐厅预订 Agent 成功创建了预订，但没有询问用户偏好的时间、没有确认可用性——技术上成功，用户体验失败。

## Rubric 设计

以下是 Microsoft 案例中的 yes/no 行为检查示例：

- 当用户给出部分请求时，Agent 是否询问缺失信息？
- 在声称预订可用前，Agent 是否验证了系统可用性？
- 完成预订后，Agent 是否向用户确认了详情？

关键特征：**由拥有 Agent 的团队编写**，因此反映实际期望行为而非抽象指标。

## 评测题目与评分对象的对齐

Google Developer Relations（2026-09）从评测设计侧补充了三个边界：

- **先制造区分度**：如果不带 skill 的 baseline 已经高分，题目可能过易，无法显示工具增量；应提高真实任务的复杂度，或重新审视工具范围。
- **只评分已声明的任务合同**：除prompt外，明确适用的安全政策、系统约束与验收合同也可构成判据。不能事后惩罚未声明的实现偏好。
- **目的优先于固定路径**：Agent 绕过自定义工具却得到正确结果，是工具设计的反馈，不应被自动判错。只有当工具调用、审批顺序或审计轨迹本身是需求时，才把它们显式写入 rubric。

这把 rubric 的工作边界从“检查行为”扩展为“保证被检查的行为确实是需求”：题目定义测试空间，rubric 定义验收边界，二者错位时分数会制造假信号。

## 分级锚点 vs yes/no 检查（SimilarWeb 2026 补充）

Microsoft 的 rubric 是 yes/no 行为检查，回答"行为有没有做"；SimilarWeb Data Studio 案例（`[[20260729-similarweb-langsmith-agent-report-evaluation]]`）把 rubric 扩展为**分级评分锚点**，回答"做得有多好"——开放式长文可结合多个二元判据与分级锚点；单一二元总判通常丢失细粒度信息：

- 每个质量维度独立 rubric，带显式锚点（如 `source_integration` 的 0.0/0.3/0.8/1.0 四档描述），裁判返回每维度分数而非单一总判。
- 每个标准返回三件套：score + gap（差距摘要）+ detail（一句话理由）——低分永远附带可检查的理由。
- rubric 之外叠加 faithfulness 检查（每条论断是否由检索数据支持，捕捉"自信但无根据"陈述）与 A/B 基线裁判（新版本与已接受历史版本并排比较）。

关键失效模式：锚点措辞即激励结构。奖励"来源数量"的锚点会被"堆模糊引用"游戏化（[[Goodharts-Law]] 的评估层形态）；两个标准互相拉扯时聚合分数掩盖冲突——详见 [[Evaluator-Miscalibration]]。修复方式是把锚点改为奖励真正想要的东西（命名、可验证、绑定具体论断的来源），同一份报告的分数从 0.7 落到 0.3，与评语一致。

## Self-Improving Loop（Agent Optimizer）

Microsoft 的 Agent Optimizer 将 rubric 评估与自动改进结合：

1. 运行 Agent 对抗测试交互集
2. 对每个 rubric 评分
3. 当 rubric 失败时，自动生成多个候选修复（改写 system prompt、调整工具使用、切换模型、调优 skills）
4. 并行评分各候选
5. 选择候选版本，是否晋升还需独立回归、真实终态及安全门禁；高分不自动证明实际改进

**同一循环既度量 Agent 也改进 Agent。**

Foundry 还可以从 Agent 配置和生产 traces 自动草拟 rubric——从真实流量而非空白页出发。

## 与 Continuous Evaluation 的配合

| 评估类型 | 回答的问题 | 时机 |
|---------|-----------|------|
| Continuous Evaluation | 行为是否变化了？ | 实时流量采样 |
| Rubric-Based Evaluation | 行为是否正确？ | 测试交互集 |
| Agent Optimizer | 如何自动修复？ | rubric 失败时 |

三者构成一种生产评估与候选改进流程，而非完整充分的发布安全保证。还需保护 reference/holdout，校准评估器并核对实际外部效果。

## 前提与局限性

- **聚合与否决**：分级质量得分、关键依赖门禁、禁止行为与过程证据应分别报告。AutoDesign PosterBench以加权七维得分再取适用上限的最小值（§5, 式7–8），是非补偿约束的一种例子，不代表对所有安全违规只需降分；生产系统可能要求直接拒绝发布。参见[[PosterBench]]。Agent Optimizer为特定产品功能，不是rubric评估的同义词。

- Rubric 质量取决于团队对 Agent 期望行为的理解深度
- 自动草拟的 rubric 仍需人工审核
- Optimizer 自动改写 prompt 有失控风险——如果 rubric 有缺陷，可能收敛到错误行为
- 主要来源是 Microsoft Foundry 的产品叙事，独立验证有限
- [[20260819-google-ai-evals-inspect-skill]] 的代码核验表明确定性 reducer 仍聚合可能误判的 LLM 二元结果。保留逐项错误、总体效果与成本；对关键禁止行为采用非补偿门禁，不能以平均分抵消。
- **锚点即激励**：rubric 锚点写错会被 game（模糊引用刷广度分），且标准间冲突会被聚合分数掩盖——错误校准可能带来错误优化或发布判断，严重性需按实际风险衡量（[[Evaluator-Miscalibration]]）；rubric 需要像代码一样接受迭代验证

## 关联概念

- [[Agent-Verification]] — Rubric 是 verification 的一种结构化形式
- [[Agent-Harness]] — 评估是 harness 的关键层
- [[Harness-Engineering]] — rubric 设计是 harness engineering 的实践之一
- [[Validation-Pipeline]] — rubric 可集成到验证管线中

## 关键数据点

- Microsoft Agent Optimizer (2026-07): 基于 rubric 失败自动生成候选修复——改写 prompt、调整工具、切换模型、调优 skills，并行评分后选最优
- Foundry 可从 Agent 配置和生产 traces 自动草拟 rubric，从真实流量而非空白页出发
- 生产评估管线三件套：Continuous Evaluation（检测漂移）→ Rubric（定位问题）→ Optimizer（生成修复）
