---
type: research-log
title: "Explore：环境真值、执行真值与成功来源"
date: "2026-09-07"
tags:
  - research-log
  - verifier
  - reference-integrity
  - success-provenance
  - ex-004
---

# Explore：环境真值、执行真值与成功来源

## Scope

本轮深化 `EX-004`「reference integrity 与 success provenance 是否构成独立必要门」。问题不是再找一个多模型 judge，而是核对三种容易被混成一个“oracle”的对象：

1. **reference truth**：题目、目标、expected action 或 gold patch 是否正确、可辨识、语义等价；
2. **environment-state truth**：运行时看到的外部状态是否与固定 fixture 的真实状态一致；
3. **execution/post-state truth**：动作、最终状态、交易或副作用是否真的达到判定条件。

本轮只把论文和官方一手材料当作 Evidence；“三种真值不能互相替代”是基于它们边界的 Reasoning，不是来源直接宣称的结论。

## Evidence

### 1. EnvTrustBench：环境状态 oracle 与 trace oracle 被显式分层

来源：[论文 HTML](https://arxiv.org/html/2605.08828)，v2（2026-05-12）。

论文把每个 case 表示为场景、初始工作区、初始外部环境、任务目标和 validation oracle。外部环境可以包含 API response、server-backed state、网页和 package metadata；agent 只接收经 tool boundary 暴露的部分观察。作者把 outcome oracle 与 trace oracle 分开：前者检查最终 artifact、状态 mutation、选择的路径和 tool effect，后者检查观察历史、验证动作、tool call、计划变化和最终响应。

论文报告 11 个场景、55 个 case、6 个模型 backbone、5 个 scaffold，14 个 model–scaffold stack，共 3,850 次通过/失败运行；其中 3,206 次进入错误路径，aggregate EMR 为 83.3%。这些是受控 fixture 的行为结果，不是生产发生率。

它对本问题的直接增量是：**外部环境真值不是最终答案的同义词**。同一最终错误或正确结果，还需要沿 trace 判断 agent 是否把暴露的环境 claim 当成行动依据。作者明确说明其 oracle 边界只覆盖固定真实状态下的 case-specific false path，不测生产发生率、一般 prompt injection、广义 tool safety 或所有下游伤害。

### 2. EVMbench：执行状态可由 replay 与链上验证判定，但 reference 仍有边界

来源：[OpenAI 官方介绍](https://openai.com/index/introducing-evmbench/)，及其[论文 PDF](https://cdn.openai.com/evmbench/evmbench.pdf)（2026-02-18）。

EVMbench 使用 117 个来自 40 次审计的漏洞，提供 detect、patch、exploit 三种模式。exploit 模式把 agent 交易在隔离的本地 Anvil 链上重放，并用程序化 grader 和链上验证判断资金是否被抽走；官方介绍还说明 harness 用 Rust 实现确定性部署与 replay，并限制危险 RPC。

这提供了一个比“模型最后说成功”更强的 execution/post-state oracle：交易被重放，结果在链上状态中核验。但它不是完整的 reference/provenance 交叉设计：detect 模式以人类审计者标记的漏洞作为 reference，官方明确承认无法可靠判断 agent 额外发现的漏洞是真漏洞还是 false positive；exploit 模式按顺序重放交易，精确时序相关行为在范围外，本地干净 Anvil 状态也不是 mainnet fork。

### 3. OpenAI coding evaluation audit：reference/测试有效性可独立损坏 execution score

来源：[官方审查](https://openai.com/index/separating-signal-from-noise-coding-evaluations/)。

该审查把任务 prompt、tests、gold patch、model attempts 和 failure traces 放进质量审计；被标记的任务再由五名有经验的工程师独立判断。公开结果显示，低覆盖测试、过严测试、题意不足和误导性 prompt 都可能让通过/失败不再代表完整有效的解决方案。作者报告 agent pipeline 标记 27.4% 任务、人工标记 34.1% 任务为 broken，并明确将 hidden tests 与 prompt 不一致视为评测失效来源。

这说明 execution pass/fail 即使由确定性 test 得出，也不能自动承担 reference truth；但它仍不是 success provenance 的干预实验，也没有同一 agent trace 上对正确/错误 reference 与外部状态进行 factorial 操纵。

## 横向判定

| 来源 | reference truth | environment-state truth | execution/post-state truth | trace/provenance | 三门交叉 | 判定 |
|---|---|---|---|---|---|---|
| EnvTrustBench | case objective/oracle 由生成器固定；未操纵 reference 正确性 | 有 true environment state 与环境 claim 的对照 | 有 final artifact、state mutation、tool effect | 有 outcome oracle + trace oracle | 否 | 强化 environment truth 与 process provenance 的分层 |
| EVMbench | detect 依赖人类审计 reference；extra finding 真值不闭合 | 本地 Anvil fixture；非 mainnet truth | exploit 有 transaction replay + on-chain verification | 有交易轨迹，但未操纵 source provenance | 否 | execution/post-state oracle 的近邻反例 |
| OpenAI coding audit | prompt/tests/gold patch 可被人工审查发现失真 | 题目环境有，但不是独立真值因子 | hidden tests/pass rate 可被错误 reference 污染 | failure traces 用于审计，不作 provenance 干预 | 否 | reference integrity 的现实审计边界 |

## 当前判断：refined

本轮没有发现需要新建 `EX-008` 的正交缺口。`EX-004` 应进一步写成三层诊断，而不是一个泛化的 oracle gate：

`reference truth → environment-state truth → execution/post-state truth`

三层都可以有各自的 trace/provenance 绑定；某层的确定性并不能替代另一层。例如：

- 有正确的 execution/post-state，不证明 agent 没有通过错误 reference 或泄漏路径得到答案；
- 有 environment-state oracle，不证明题目的 expected action 或 gold patch 代表正确目标；
- 有固定 reference 和 final score，不证明外部环境 claim 被正确验证，也不证明 success 来源可归因。

这不是把三层宣称为普遍“必要条件”。当前一手材料只支持它们是不可互替的测量对象，并提示最小完整设计至少要分别记录三者的 owner/version/hash、可见投影、trace transformation 和 outcome 证据。

## 新问题

在同一固定任务与可回放 trace 上，能否用三组可独立核验的对象——`reference manifest`、`environment state hash`、`execution receipt/post-state`——区分以下四种情况：真成功、错误 reference 导致的伪成功、未验证环境 claim 导致的路径成功、以及正确路径但错误 post-state？

## 证伪方向

- 若一个固定版本、外部可核验的 execution/post-state oracle 在不同 reference 与 evidence-provenance 条件下仍能稳定识别能力、路径和归因，则三层可以收窄为同一 benchmark validity gate 的不同字段。
- 若 EnvTrustBench 式 trace oracle 在 reference 被替换为语义等价、错误或泄漏版本后不改变归因，说明 reference integrity 对 success provenance 没有独立决策增量。
- 若 EVMbench 式 deterministic replay 加上 state hash 能在 reference、环境 claim 和 trace transformation 改变时仍唯一恢复“为何成功”，则 replay-validity/provenance binding 不必作为额外门；否则仍需保留。
- 若差异只出现在构造 benchmark 或单一 action surface，而在真实可回放、多来源环境中消失，应把结论收窄为 benchmark-construction artifact。

## Source 需求

- **P0，clip+compile**：EnvTrustBench，提取 `true environment state → outcome oracle/trace oracle → final artifact/state mutation`，保留 3,850 次运行的 accepted denominator 与生产外推限制。
- **P0，clip+compile**：EVMbench，提取 detect/reference、patch tests、exploit transaction replay、on-chain verification、顺序 replay 和本地链限制，不能把交易 replay 写成 mainnet truth。
- **P0，新 source**：寻找同一可回放 case 同时公开 `reference manifest/version`、environment state hash、visible/held-out trace、execution receipt/post-state 与至少两个独立 verifier 的材料。
- **P1，新 source**：寻找把 semantic-equivalent reference、正确/错误环境 claim、以及 external adjudication 置于同一任务的 factorial 设计；只有单独的 hidden grader 或多模型比较不算命中。

## 最小实验建议

构造一个 deterministic tool environment，固定 agent rollout 和工具 schema；每次运行写入 `case_id`、`reference_version`、`environment_state_hash`、`trace_hash`、`action_id`、`provider_receipt` 与 `post_state_hash`。至少随机化三类条件：

1. reference：正确、语义等价、错误；
2. environment claim：无 claim、正确 claim、错误但可验证 claim；
3. verifier view：outcome-only、完整 trace、完整 trace + provider receipt。

用规则 verifier、独立模型 verifier 和人工/外部 adjudicator 记录：final outcome、path correctness、reference anchoring、evidence provenance、post-state mismatch、误放行/误拒绝和归因一致性。只有同一 `trace_hash` 与 `post_state_hash` 能绑定到每个 cell 时，才估计 interaction；否则结果只能作为匹配案例，不能算 factorial evidence。

## 结论

- **Delta**：`refined`。
- **EX 处理**：更新 `EX-004` 为三层 oracle / provenance 边界，不新增 Explore。
- **知识生命周期**：不创建稳定 Entity/Topic/Comparison；EnvTrustBench 与 EVMbench 进入 source 需求，待后续 `clip+compile`。
- **主要未决**：公开材料仍没有在同一 trace 上联合操纵 reference truth、environment-state truth、execution/post-state truth 和 verifier independence。
