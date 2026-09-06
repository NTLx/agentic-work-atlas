---
type: research-log
title: "EX-005 效果结算与独立对账 follow-up：负面边界"
date: "2026-09-07"
tags:
  - research-log
  - ex-005
  - effect-lineage
  - reconciliation
---

# 结论

**未找到合格的新案例或测试；本轮判定为 `no_delta`。**

在本轮实际核读的公开一手材料中，没有一个同案/同一测试单元同时公开并可验证：

`action identity 或 policy version → provider request/receipt → revoke/cancel outcome → provider-authoritative post-state → compensation result → independent reconciliation/review`

最接近的材料分别补强了链条的不同部分，但不能拼接成一个合格闭环。BCCA 2026 的作者实验明确把本地 provider 运行标为非独立证据，并没有在途取消/撤销测试；Stripe 官方文档明确描述幂等、取消、退款和 5xx 后 reconciliation，但没有公开同一请求的完整案例导出或独立复核。

## 搜索范围与准入门槛

- 只核读第一方材料：作者论文与作者维护的代码/冻结实验产物、官方 API/工程文档；未用二手报道或通用架构目录作为 Evidence。
- 只寻找具体公开案例或测试，不把 trace 字段表、协议能力清单或一般 observability 文档当作命中。
- “独立 reconciliation/review”要求对外部效果或补偿后终态作独立于执行/写入路径的复核；独立 seed、独立标注或运行时自己重读本地状态不自动满足该条件。

## 证据核查

### E1 · Recourse/BCCA：最接近的作者测试，但缺取消与独立终态验收

来源：

- 论文（作者论文，arXiv）：<https://arxiv.org/abs/2609.01939>
- 论文 HTML：<https://arxiv.org/html/2609.01939>
- 作者代码、实验仓库：<https://github.com/mpi-dsg/recourse>
- EffectReceipt schema：<https://raw.githubusercontent.com/mpi-dsg/recourse/main/prototype/schemas/effect_receipt.v1.json>
- RecoveryReceipt schema：<https://raw.githubusercontent.com/mpi-dsg/recourse/main/prototype/schemas/recovery_receipt.v1.json>
- Postgres provider bench：<https://raw.githubusercontent.com/mpi-dsg/recourse/main/prototype/runtime-ts/packages/adapter-postgres/bench/provider-postgres.ts>
- 冻结的 Postgres cell 结果：<https://raw.githubusercontent.com/mpi-dsg/recourse/main/prototype/reproducibility/paper-v1/results/rq-provider-postgres/cells.json>

Source class：**作者论文 + 作者维护的可复现实验/代码 artifact**。

Evidence：

- EffectReceipt 绑定 `contractId`、`jobId`、`intentHash`、`paramsHash`、资源 ID、前/后状态摘要和可选 `providerReceiptHash`；RecoveryReceipt 通过 `effectReceiptHash` 绑定效果，并记录恢复 artifact、`success/partial/failure/inconclusive` 结果和残余测量。论文将每个 `κ` 的 evidence schema 版本化。
- 公开的 provider-compatible 测试覆盖 Docker Postgres、local bare Git 和 LocalStack SSM；冻结 cell 中能看到 `pg_txid`、`pre_lsn`、`post_lsn`、效果回执哈希、恢复结果和 residual harm。论文报告 Postgres 20 cells、15 admitted，且同时覆盖完整恢复、部分恢复和失败恢复。
- 论文明确说明：这些环境是 ephemeral、single-machine、operator-controlled；第二个本地进程重查同一容器也不构成独立验证，回执属于 L2，不是 provider-attested L1 或 public replay L0。作者还把“升级到真实 managed provider + provider-side attestation channel”列为未来工作。
- 论文的 routing suite 有两名标注者独立标注 10 个故障类，但作者同时说明 router、labels 和 predicates 都由同一协议实现；这验证的是规则符合性，不是外部 provider post-state 或补偿后业务不变量的独立复核。Base Sepolia 的 arbitrator 也是 mock。

缺口：

- 有 action identity / contract identity；没有一个不可变 `policy_version` 到 provider request 的公开同案 join。
- 有本地状态摘要和 adapter 生成的 receipt；没有 provider-authenticated request/receipt 或 managed-provider authoritative read-back。
- 没有 `revoke-after-send`、in-flight cancel 或取消后的 provider outcome 测试。
- 有 compensation / RecoveryReceipt；但没有独立 reconciliation 证明补偿后外部业务不变量恢复。

判定：**具体测试，部分命中；不能关闭 EX-005。**

### E2 · Stripe：官方 API 语义覆盖多个节点，但不是同案证据包

来源：

- 幂等请求 API reference：<https://docs.stripe.com/api/idempotent_requests>
- 低层错误与 reconciliation：<https://docs.stripe.com/error-low-level?locale=en-GB>
- PaymentIntent cancel API：<https://docs.stripe.com/api/payment_intents/cancel>
- Refund/cancel/refund tracing：<https://docs.stripe.com/refunds>

Source class：**提供方官方 API 与运维文档**。

Evidence：

- Stripe 官方文档说明 `Idempotency-Key` 用于把重试识别为同一操作，并保存首次请求的 status code/body；这能提供动作级幂等身份，但文档没有把它定义为 policy version。
- PaymentIntent cancel API 返回对象状态 `canceled`，并规定取消后不能再用该 PaymentIntent 发起额外 charge；对 `requires_capture` 的剩余可捕获金额自动退款。Refund 文档还描述退款失败、异步银行处理、退款引用号以及受限状态下取消 refund。
- 5xx 请求的官方边界是“结果不确定”：Stripe engineers 会检查失败 mutation 并尝试 reconciliation，可能 roll forward 或 roll back；官方同时明确理想结果不保证，并建议用 metadata/webhook 交叉引用新建对象。

缺口：

- 文档示例把 PaymentIntent、取消结果、refund 和 webhook 分开描述，没有公开同一请求的 `action_id/idempotency_key → provider request ID/receipt → cancel-after-send outcome → final refund/charge state` 运行导出。
- 文档中的 reconciliation 由 Stripe 自身工程流程执行；没有公开独立于 provider 写入路径的 reviewer、复核报告或同案 reconciliation artifact。
- 没有 policy version 与调用绑定，也没有把补偿后的商户账务不变量和 provider 对账结果作为同一测试验收条件。

判定：**官方语义近似完整，但不是公开同案案例/测试；不能关闭 EX-005。**

## 验收矩阵

| 候选 | 身份/策略版本 | provider request/receipt | revoke/cancel outcome | 权威 post-state | compensation | 独立 reconciliation/review | 结果 |
|---|---|---|---|---|---|---|---|
| Recourse/BCCA 作者测试 | `contractId`/`jobId` 有；policy version 未形成同案 join | adapter receipt 有；provider-authenticated receipt 无 | 无 revoke-after-send / in-flight cancel | 只有 operator-controlled local sandbox 摘要 | 有 RecoveryReceipt | 无；独立标注只验证 routing conformance | 部分命中 |
| Stripe 官方 API 文档 | idempotency key / PaymentIntent ID 有；policy version 无 | provider response/webhook 语义有；无同案导出 | cancel/refund API 语义有 | 对象状态可读；无同案最终账务验收 | refund/reversal 有 | provider 自身 reconciliation；无独立 review artifact | 部分命中 |

## Negative boundary

本轮新增的是边界确认，不是新案例：

1. **回执存在不等于 provider truth。** Recourse 的 `providerReceiptHash` 只有在 provider 自己签名或可独立重放时才升级到 L1；实际 sandbox 运行仍是 adapter/operator-controlled L2。
2. **取消/退款语义存在不等于同案收敛。** Stripe 规定了可取消状态、取消后的对象状态和退款失败路径，但没有公开一个测试单元把这些状态与原始动作身份、补偿和独立对账结果连起来。
3. **补偿结果存在不等于独立终态验收。** `RecoveryReceipt` 或 provider 的 refund object 只能证明某个恢复/退款动作及其局部状态；没有独立 read-back、不变量检查和 review artifact，不能声称外部效果已闭合。

因此当前 `EX-005` 的最小未决缺口仍是：**一个可公开核验的同案 effect lineage，能从动作身份穿透 provider receipt、撤销/取消后的在途结局、权威 post-state、补偿结果，并由独立对账或复核闭合。** 本轮没有找到这样的新材料。

## 证据边界

- “未找到”仅针对上述实际核读的论文、作者 artifact 和官方 API/运维页面；不声称相关组织内部不存在私有记录。
- Recourse 的本地 provider 测试是具体实验，但其作者自己明确限定为 provider-compatible sandbox，不是 managed-provider 或独立 public-state evidence。
- Stripe 材料是官方能力与失败语义，不是一次公开事故报告或可复现的端到端测试；不能把多个 API 示例拼成同案事实。
- 本 bounded side task 只新增本文件；不修改 `research-agenda.md`、`research-logs/2026-09-07.md`、`raw/`、stable wiki 或任何现有文件。
