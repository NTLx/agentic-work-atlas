---
type: research-log
title: "EX-005：耐久执行停止、取消与外部效果 follow-up"
date: "2026-09-07"
tags:
  - research-log
  - ex-005
  - effect-lineage
  - cancellation
  - post-state
---

# EX-005：耐久执行停止、取消与外部效果

## 研究问题

公开执行框架中的 `stop/cancel` 是否已经把“停止意图”闭合为外部效果的终态，还是仍需单独记录在途执行、provider receipt、权威 post-state 与补偿结果？本轮特别寻找能把此前抽象的 `commit-state uncertainty` 落到提供方执行边界的一手材料。

## Evidence

### E1 · AWS Durable Execution：停止 durable execution 不等于停止在途调用

来源：[AWS Durable Execution SDK — Manage Executions](https://docs.aws.amazon.com/durable-execution/getting-started/manage-executions/)，官方开发者文档，核读定位为 “What happens to running code”。

可支持的事实：

- 停止 durable execution 不会停止当前正在运行的 Lambda invocation；正在执行的代码会继续运行。
- 如果函数在停止时仍在运行，它会继续到下一个 checkpoint；SDK 在尝试写入下一个 checkpoint 时才发现执行已停止并结束当前 invocation。
- checkpoint 之前已经发生的工作不会被回滚或取消；文档以步骤中的 external API call 为例，明确说明该类 side effect 仍然生效。

这是一条提供方明确写出的执行契约，不是 Agent 事故统计或取消成功率实验。它直接支持：执行器的 durable state、当前 invocation 状态和外部业务效果不是同一个状态对象。

局限：文档没有给出 agent action 的分母、provider receipt、unknown-commit 率、canonical business post-state 或独立 reconciliation；Lambda invocation 继续运行也不等于外部 API 一定成功或失败。

### E2 · AWS Step Functions：跨服务取消是 best-effort，且可能产生额外外部成本

来源：[AWS Step Functions — Discover service integration patterns](https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html)，官方开发者文档，核读定位为 `.sync` service integration。

可支持的事实：

- 当 `.sync` 任务被中止时，Step Functions 会 best-effort 尝试取消集成任务。
- 取消可能因为 IAM 权限不足或临时服务故障而失败；官方同时警告未能取消时可能继续产生集成服务费用。
- `.sync` 依靠事件和轮询监视被调用任务；监视停止、取消请求和被调用服务本身的最终状态不是同一件事。

这比抽象的“取消可能最终一致”多了一层提供方边界：上游 orchestration 可以知道自己已发起停止并继续监视，但它不因此拥有下游服务的终态。

局限：这是服务集成契约和失败语义，不是一次公开的 Agent trace；文档没有提供同一 action identity 下的取消请求、下游 receipt、最终资源状态和补偿审计包。

### E3 · MCP Tasks 与 A2A：协议层取消都保留“意图”和“状态查询”的分离

来源：[MCP SEP-2663 Tasks Extension](https://modelcontextprotocol.io/seps/2663-tasks-extension) 与 [A2A Protocol specification](https://a2a-protocol.org/dev/specification/)。二者作为协议对照，不计为新的独立部署证据。

可支持的事实：

- MCP 将 `tasks/cancel` 定义为 ack-only；取消处理 eventual consistent、cooperative，服务不被要求实际停止工作，也不保证最终进入 `cancelled`。需要知道当前状态时仍依赖 `tasks/get`。
- A2A 规定服务会尝试取消任务，但成功不保证；任务的 status、artifact 和 history 是协议任务记录。

Reasoning：这些协议都把 cancel request、task record 和最终结果分开；但 task record 或 artifact 仍不能自动证明外部 provider 的 canonical post-state。这个判断是跨协议推断，不是 MCP/A2A 已经证明的业务效果定理。

## 横向判定

| 层 | 一手材料能证明什么 | 仍缺什么 |
|---|---|---|
| cancellation intent | 停止请求已被接收，或 orchestration 已进入 stopped/cancelled 语义 | 是否阻断了当前 invocation 或下游任务 |
| in-flight execution | 当前调用可能继续到 checkpoint；跨服务取消可能失败 | 调用是否已经提交、提交到哪一个 provider |
| dispatch / provider receipt | 部分框架可记录任务或轮询状态 | 同案 provider-authenticated receipt 与 action identity 绑定 |
| canonical post-state | 当前材料只描述局部执行器/任务状态 | 下游业务资源的权威最终状态 |
| recovery / reconciliation | Step Functions/MCP/A2A 有重查或任务状态语义 | 补偿结果、unknown/partial/duplicate 分类与独立复核 |

## Reasoning

本轮的增量不是发现一个新的正交问题，而是为 `EX-005` 的三层边界补上了一个更清晰的提供方执行例：

`stop/cancel intent → in-flight invocation → checkpoint/dispatch boundary → external effect → provider post-state → reconciliation`

其中，checkpoint 不是外部效果的提交证明，而是 durable execution 发现停止并结束当前 invocation 的控制边界。若副作用在 checkpoint 之前已经发生，停止 durable execution 只能改变后续 checkpoint 和编排状态，不能逆推出该副作用已撤销。

因此将 `EX-005` 进一步收窄为：**撤销/停止、在途执行和外部效果结算必须分别验收；至少要有 action identity、provider receipt 或可查询的提交状态、权威 post-state，以及对 unknown/partial/duplicate 结果的补偿或独立对账，才可把“停止成功”写成“外部效果已收敛”。** 这不是说每个工作流都必须暴露同一 API，而是说没有这些等价证据时，不能把 orchestration state 当作 business effect truth。

本轮仍没有找到公开的 Agent 同案 trace 能同时闭合上述字段。因此不把 AWS 文档当作 EX-005 的最终验证，也不把 generic durable execution 的边界直接外推为所有 Agent 系统的发生率结论。

## Result

- **Delta：** refined
- **结论：** `EX-005` 保持独立，不新增 EX；新增“checkpoint / in-flight invocation”作为 effect-lineage 的必要分层，并以 AWS 官方契约补强“停止编排不等于撤销外部副作用”的边界。
- **New bottleneck：** 从 `cancel acknowledged` 到 `provider post-state known` 之间的 checkpoint/dispatch 窗口，仍缺同一 action identity 的公开测量。

## 新问题

在一个固定 Agent action 和可查询的模拟 provider 中，分别把停止注入在 `pre-dispatch`、`dispatch accepted but receipt lost`、`receipt received but checkpoint pending` 三个窗口，能否用 provider read-back 将结果稳定分类为 `not-committed / committed / partial / unknown`，并量化 cancel latency、duplicate risk 与 compensation success？

## 证伪方向

- 若公开 Agent runtime 能证明停止请求与 provider 的原子提交绑定，并在 receipt 丢失、worker 崩溃和服务故障下仍由权威 read-back 唯一恢复最终状态，则“必须单独测量 commit-state uncertainty”的强命题应收窄为特定 provider 集成的实现要求。
- 若所有停止窗口都能由同一个 durable execution status 唯一推出 provider post-state，则 checkpoint、dispatch receipt 和 post-state 可以合并为一个可验证状态；目前 AWS 文档恰好给出反向边界，因此需要实际系统证据才能推翻。
- 若只改变 orchestration 状态而不改变 provider read-back 的 committed/partial/unknown 分类，则应把取消成功率从效果安全指标中移出，保留为控制面指标。

## Source 需求与下一步目标

- **P0：** clip+compile AWS Durable Execution 与 Step Functions 官方文档，保留停止 invocation、checkpoint、best-effort cancellation、权限/服务故障和外部副作用字段；不要把通用编排契约改写成 Agent 事故证据。
- **P1：** 寻找 Agent 或 agentic workflow 的公开 trace，能够用同一 `action_id / provider_request_id / idempotency_key` 连接 stop/revoke、receipt 丢失、provider read-back、补偿与独立 review。
- **P1：** 在已有 ACRFence/Recourse 类实验中加入可控 checkpoint 窗口、receipt 丢失和 provider state query，区分 duplicate、partial、unknown 与安全 retry。

最小实验沿用 `EX-005` 的字段表，但增加 `checkpoint_index`、`invocation_state`、`dispatch_accepted_at`、`receipt_observed_at` 和 `provider_readback_at`。主要终点不是 task 是否显示 cancelled，而是 provider post-state 分类、重复副作用率、补偿成功率、对账延迟和 MTTR。

## 证据边界

- E1/E2 是官方执行契约与失败语义，不是 agent-specific 的效果测量。
- E3 是协议规范对照，不等于真实 provider receipt 或 canonical business state。
- 本轮没有修改 raw、稳定 Wiki 或已有 research note；本文件只承载本轮 Explore 的 reasoning 与 source 需求。
