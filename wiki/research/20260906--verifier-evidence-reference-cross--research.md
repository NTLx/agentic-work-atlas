---
type: research-log
title: "验证器独立性、证据可见性与参考完整性的交叉核查"
date: "2026-09-06"
tags:
  - research-log
  - agent-evaluation
  - verification
---

# 验证器独立性、证据可见性与参考完整性的交叉核查

## 研究问题

是否已有一手 benchmark 在同一条可回放 Agent trace 上，同时操纵 `verifier independence`、`evidence visibility/interpretation` 与 `reference integrity/success provenance`？本页只记录一手论文、作者仓库和官方 benchmark 文档；Research 结论不进入稳定知识层。

## Evidence

### S1 · trajectory-judge

- 来源：[论文](https://arxiv.org/abs/2609.00038)、[作者仓库](https://github.com/mohammadi-hadi/trajectory-judge)。
- 固定一个确定性的 support-desk 环境、脚本化正确策略和单故障注入；每条回放轨迹带有故障类型、发生步骤，以及 customer-visible outcome 是否存活的构造标签。论文和仓库报告 400 条轨迹、六类故障、100 条 clean、175 条 silent fault、125 条 loud fault。
- 在同一批 trace 上比较 programmatic rules、outcome-only judge、step-rubric judge（两种模型规模）和 self-consistency judge。outcome-only judge 的 silent-fault recall 为 0.451，step judge 为 0.766；self-consistency 三倍成本且没有稳定质量收益。
- 它补足了 `evidence view → judge error` 的固定 trace 入口：outcome-only 与 step-rubric 的差别不是 Agent 重跑造成的。但 8B judge 几乎把全部轨迹判为 faulty，说明不同模型名、较高 recall 与 verifier independence 不能互换。
- 边界：只有一个合成领域；故障是单点注入而非自然级联；只使用本地模型；没有 `none/correct/semantic-equivalent/corrupted reference`、success-provenance 干预或生产 post-state。

### S2 · BabelJudge

- 来源：[论文](https://arxiv.org/abs/2606.22329)、[作者仓库](https://github.com/Shreyaskc/BabelJudge)。
- 方法从高质量 reference response 施加受控降级，构造无需人工标注的 pairwise gold；Agent 扩展包含参数破坏、工具替换、虚构调用、缺失步骤等九类轨迹扰动，并定义工具准确率、幻觉检测和轨迹长度偏差等指标。
- 框架提供 11 个 judge backend 的适配器，但论文主体实验只报告一个 judge 模型；Agentic 数据是手工合成 demo，尚未形成跨 verifier、hidden reference ledger、外部 post-state 的联合实验。
- 因此它支持“可控扰动能审计 judge 的机械可靠性”，不支持“不同 verifier 的错误独立”，也不支持 reference 本身有效或 success provenance 已被测量。

### S3 · Agents' Last Exam（ALE）

- 来源：[作者维护的 benchmark 仓库](https://github.com/MaxIntelligenceAgency/ALE-Benchmark)。
- ALE 在 Agent 运行结束后才把 hidden reference 放入 grader，运行在真实 OS sandbox，并保存统一 trajectory、原始日志、结果和 artifacts，提供 reference 不泄漏给被测 Agent 的工程控制边界。
- 该仓库没有在同一 trace 上改变 verifier family、evidence view 或 reference condition；它是 `EX-004` 的 reference-control 设计候选，不是三轴因果证据。

## Reasoning

1. `verifier independence` 不能由“用了多个模型”代理。最小操作应固定 Agent rollout、evidence packet 和 reference 条件，再替换跨家族或独立实现的 verifier，并以外部状态/规则 oracle 计 false accept、false reject、attribution 和 shared-error；`trajectory-judge` 的 always-flag 结果说明只比较 recall 会制造伪独立性。
2. 新材料补强 `EX-002` 的 evidence-view/interpretation 轴，并为 `EX-001` 提供固定 trace、多 judge 的最小设施；它们没有补足 reference owner/version、semantic-equivalent/corrupted reference、success provenance 或同一 trace 的三轴交互。
3. `BabelJudge` 的“由降级构造真值”和 ALE 的“运行后隐藏 reference”是两种不同的 reference control：前者检查 judge 能否识别已知损坏，后者避免 Agent 运行期泄漏答案；二者都不能证明 reference 的任务契约有效，也不能替代独立 adjudication。

## New bottleneck

没有发现正交的新 Claim。真正的瓶颈收窄为：在一个外部 oracle 可回放的任务族上，如何把 `evidence view`、`verifier implementation/family` 和 `reference/provenance condition` 分成可独立重放的因素，而不是把多 judge、隐藏 reference 和构造真值混为一个安全保证。

## 证伪方向

- 若同一 trace 在跨家族/独立实现 verifier、完整/部分 evidence 和不同 reference 条件下的 false accept/reject、attribution 与排名稳定性均不变，三轴缺口可收窄为测量工程问题。
- 若只改变 evidence view 才产生稳定差异，而 verifier family 与 reference/provenance 在固定外部 oracle 后不再留下残差，则保留 EX-002，削弱 EX-001/004 的独立必要性主张。
- 若 reference/provenance 条件在固定 verifier/evidence 后仍产生可回链的误判或 success-attribution 差异，保留 EX-004 的两个诊断对象，但不把它们写成普遍必要门。

## 下一步最小实验

固定模型、任务、工具、预算和一条可回放 rollout，交叉：

`verifier = programmatic / same-family LLM / cross-family LLM / independent implementation`

`evidence = trajectory-only / state+receipt / authorized-partial`

`reference = correct-versioned / semantic-equivalent / corrupted-or-unknown`

由不接触 judge score 的 external oracle 记录实际 effect、false accept/reject、step attribution、calibration、ranking stability 和空分母；先用非 LLM oracle 校验分母，再加入 LLM/human adjudicator。另行做 `CLEAN/GOLD/SHAM` provenance 重运行，不把运行前信息干预与运行后 judge 重评分混成一个因果效应。

## Source 需求

- clip+compile 三份材料，固定版本、原始 verdict/trajectory、扰动构造器和 denominator。
- 寻找同一 replay fixture 上同时提供跨 verifier、授权部分 evidence、hidden reference ledger、语义等价 reference 与 external post-state oracle 的 factorial benchmark。
- 取得真实 Agent trace 上的 reference owner/version、provenance ledger 和多人独立 adjudication；缺少这些字段时，EX-004 仍只作为审计缺口。

## Evidence boundary

以上材料均为受控 benchmark、开源 harness 或工程设计。没有把不同 judge 模型、隐藏 reference、synthetic oracle 或作者自述直接当作独立现实证据，也没有创建稳定 Entity/Topic 页面。
