---
type: research-log
title: "EX-006 控制状态抵达执行边界：公开证据复核"
date: 2026-09-07
tags:
  - research
  - explore
  - EX-006
  - control-state
  - provenance
---

# EX-006 控制状态抵达执行边界：公开证据复核

## Mode

Open Explore 后台研究。研究对象为：高影响/不可逆动作是否必须以带来源、稳定绑定、预算隔离且失败关闭的控制状态抵达执行边界？本日志只沉淀 Research 层的证据边界、推理和下一步，不创建稳定 Entity/Topic，也不替代 Schema 或 agenda。

## Capability

实际使用 `research`：先启动后台研究代理做独立一手来源搜寻，再由主代理直接核验论文原文、作者代码/仓库与官方规范。来源只取论文原文、作者代码/数据集页面和作者/项目官方规范；没有把架构宣称当成效果证据。

## Trigger

复核截至 2026-09-07 的公开一手来源，判断是否存在在同一 agent 任务或可回放轨迹中，对照“上下文/记忆携带策略”与“外部签名/来源绑定控制状态”的因果或准因果证据，并跨越 compaction、memory poisoning、authority update、failover、recovery、preflight/action-boundary。

## Evidence posture

以下是 Evidence；只记录来源实际做了什么、比较了什么、观测到了什么。由这些结果推导的“因此”统一放在后面的 Reasoning。`外部签名`特指控制或写入边界的可验证签名/认证来源；普通 provenance 字段、提示词中的“官方声明”、摘要中的政策文本不自动等同于密码学签名或 authority binding。

## Evidence

### 1. 上下文携带与约束衰减：已有较强的同任务对照，但不是外部控制状态对照

**Ghost in the Context / ControlCapsule**（[论文摘要](https://arxiv.org/abs/2605.12535)，[作者论文全文 v3](https://arxiv.org/html/2605.12535v3)，[作者 artifact 链接](https://anonymous.4open.science/r/ghost-in-the-context)）在 AutoGen/tau3 与 OpenHands/SWE 的官方基准轨迹上做受压 counterfactual replay。它按 trace slice 配对，比较 protected placement、task-local placement、压力/容量条件，并把结果分到 policy assembly、preflight 和 action boundary。论文报告：固定 assembler 的行为校准为 0/90 unsafe proposals、0/90 unguarded violations；在 overload 表中，exact active-policy replay + preflight 有 25/48 fail-closed、0/48 silent incomplete control，exact active-policy replay best effort 则有 25/48 silent incomplete control。该结果支持“完整、可回放的控制状态加 preflight 可避免控制不完整时静默继续”。

但这不是“ControlCapsule 优于 exact replay + preflight”的效果证据：论文明确把后者作为强 baseline，并说明 overload 主要测 state-level assembly，不等同于模型实际合规优势。设计中的 registry、stable ID、issuer/scope、binding、分离预算、manifest 与 fail-closed 也主要是 reference design；没有证明密码学签名、服务故障 failover、恢复或真实 provider post-state。

**Governance Decay / ConstraintRot**（[论文摘要](https://arxiv.org/abs/2606.22528)，[论文全文 v2](https://arxiv.org/html/2606.22528v2)）在同一 session、同一禁止请求和相同模型/条件框架下比较 full policy、compaction 后的 policy、策略被摘要保留/丢弃、重复 compaction、summarizer injection 与 Constraint Pinning。论文报告 1,323 episodes、7 个模型；full policy 违规率为 0%，compaction 后 pooled violation 为 30%，策略保留于 summary 时为 0%，被丢弃时为 38%；重复 compaction 可升至 78%。Constraint Pinning 在普通条件下有效，但遇到 token stream 中伪装成 authoritative operator 的撤销指令，违规率升至 17%；增加 provenance wording 后为 10%。作者明确把无法区分真实与伪造 authority、需要可信 OOB operator channel 列为开放问题。

这里的 terminal outcome 是从模型发出的工具调用参数解析出的确定性违规，不是外部服务的 canonical post-state、receipt 或恢复结果。它提供 context/authority-in-token-stream 的准因果证据，却没有 signed OOB carrier、failover 或 recovery 对照。

### 2. 记忆完整性与生命周期：有签名写入对照，但动作边界仍不完整

**Sleeper Memory Poisoning**（[论文摘要](https://arxiv.org/abs/2605.15338)，[论文全文](https://arxiv.org/html/2605.15338v1)，[作者代码](https://github.com/ivaxi0s/LLM-agent-memory-poisoning)）把 injection 与 post-injection 分开：后续任务在移除原始恶意文档、独立对话和模拟 OpenClaw workspace 中执行，比较 embedding retrieval、external manager 和 all-memories context。报告未来 agentic action 被记忆触发的成功率约 60–89%；作者代码的 action judge 同时看目标、sandbox 文件、tool calls、最终文本和 workspace diff。该设计隔离了“恶意文档→记忆→未来动作”的跨阶段链路。

它没有外部签名控制状态、authority update、preflight/fail-closed、receipt 或 failover/recovery。external manager 是模拟的提示式记忆管理器，不应被计为可信控制面。

**SMSR**（[论文摘要](https://arxiv.org/abs/2606.12703)，[论文全文](https://arxiv.org/html/2606.12703v1)，[作者代码/数据](https://github.com/tarun-ks/smsr)）是本轮最直接的外部来源绑定证据之一：合法写入通过 trusted server-side signing oracle 写入 HMAC(content ∥ session_id ∥ timestamp)，检索只接受有效 tag；相同场景比较 unsigned injection、authenticated legitimate-user injection 与随机 memory ablation/voting。预置攻击下 unsigned ASR 从 93–100% 降至 0%；对 authenticated injection，第一组件按预期无法过滤，仍有约 8.0% ASR；query-only 设置下组合防御把 65.3% 降至 5.3%。

但指标是 Claude Haiku 对最终回答的判定，场景是模拟企业 RAG；没有外部副作用、动作 preflight、provider receipt、canonical post-state 或 recovery。HMAC 证明的是写入/检索来源完整性，不是“该来源有权批准这次不可逆动作”。论文提到 rollback 作为审计日志用途，但未评估。

**MemSecBench**（[论文摘要](https://arxiv.org/abs/2607.27080)，[论文全文](https://arxiv.org/html/2607.27080v1)）对 310 cases、48 contexts、24 个配置做 matched Write–Execute–Forget 生命周期实验，固定 task、harness、LLM、runtime、clean init、外部环境与 evidence protocol，比较 2 个 harness × 4 个 memory backend × 3 个 LLM。manifest 把写入、执行和清除阶段绑定到同一 case identity；E3 的风险通过 service/workspace/artifact 证据外化；Forget 从同一 verified post-W snapshot 检查修复，选择性修复率报告为 56.1%。评估有程序化 gate、隐藏 rubric 和人工一致性检查。

这提供了 memory backend、外部化副作用和修复后状态的准因果/配对证据，但没有对照 signed control capsule 或 external authority binding。文中出现的 source-material/template signature 是构建新鲜度校验，不是动作授权签名；Forget 是 repair 评估，不是 provider failover 或 checkpoint recovery。论文还明确不证明缓存、潜在表征等不可访问状态已不可恢复。

### 3. 执行前授权与来源图：有正向动作边界证据，但没有 carrier comparison

**Open Agent Passport (OAP)**（[论文摘要](https://arxiv.org/abs/2603.20953)，[论文全文](https://arxiv.org/html/2603.20953v1)，[官方规范](https://github.com/aporthq/aport-spec)，[作者参考实现](https://github.com/aporthq/aport-agent-guardrails)）在每次 tool call 前同步验证 Ed25519 passport、agent identity、capability scope、参数和 policy decision；阻断或允许后签发 receipt，服务不可用时 fail-closed。论文的 live Vault CTF 在相同模型/接口下比较 permissive 与 restrictive policy：879 次尝试中，permissive 成功率 74.6%，restrictive 成功率 0%，阻断率 100%。这是实际 tool-boundary 阻断证据，且涉及签名身份、能力范围和可审计 receipt。

但 OAP 没有在同一 trace 中随机化 compaction/memory carrier 与 signed passport carrier；没有 memory poisoning、authority update 后的版本/撤销对照、failover/recovery 或 provider canonical post-state。它证明了“同步、确定性的执行前控制点可阻断越权 tool call”，不能单独证明“外部签名控制状态相对于可靠 replay/context 是必要的”。官方规范本身只是规范/实现声明，不额外构成效果实验。

**FORGE**（[论文摘要](https://arxiv.org/abs/2602.16708)，[论文全文 v3](https://arxiv.org/html/2602.16708v3)）把消息、动作、事件 ID 和边注册为 provenance graph，并要求外部 VP approval signal 进入依赖图；无批准或无响应时，数据不能越过边界。小规模 info-flow 对照报告 instrumented 0/5 attack success、non-instrumented 5/5；另有 blocked action 后的 retry/recovery，作者指出 policy compliance 可由构造保证，但 recovery 仍可能失败。它是外部 reference monitor/provenance gate 的直接相关正向证据。

FORGE 的 VP 信号不是本轮定义下已证明的密码学签名控制状态；实验也没有把 context/memory carriage、compaction 或 authority spoof 与之做 factorial 对照，外部系统 post-state/receipt 证据有限。

### 4. Recovery 与不可重复副作用：证明了另一条残余风险

**ACRFence**（[论文摘要](https://arxiv.org/abs/2603.20625)，[论文全文](https://arxiv.org/html/2603.20625v1)）在 Claude Code CLI/Qwen3-32B 与模拟 bank/cloud/approval MCP 服务上，比较 checkpoint-restore 与 no-checkpoint；checkpoint 位于 verification 之后、不可逆动作之前。10/10 checkpoint-restore 测试出现 duplicate commits，no-checkpoint 为 0/10。该结果把 recovery/restore 与“实际外部副作用可能重复”联系起来。

它没有 signed control state、memory/context carrier 对照、fail-closed preflight 或 provider idempotency receipt；外部服务是模拟 MCP。因而它补足的是 action-boundary 之后的 side-effect lineage/recovery 维度，而不是 EX-006 的另一个独立主题。

### 5. 维度矩阵

| 来源 | fixed replay / 对照条件 | 外部 oracle / receipt | authority / provenance binding | preflight / fail-closed / action boundary | 实际副作用 / post-state | failover / recovery |
|---|---|---|---|---|---|---|
| ControlCapsule | 官方轨迹的 counterfactual pressure replay；protected vs task-local；assembler/overflow 对照 | 无 provider receipt；manifest/模拟边界证据 | typed registry/binding 设计；非已证密码学签名 | exact replay + preflight、fail-closed 的 state-level 结果；有 bounded action witness | 未证明真实 provider post-state | 未覆盖 |
| ConstraintRot | 同 session 的 full/compacted/omitted/pinned/injected 对照 | 无 | token-stream provenance wording；可被伪造 authority 穿透 | 无独立 preflight | 工具调用参数/模拟 terminal，不是 canonical post-state | 未覆盖 |
| Sleeper Memory Poisoning | injection/post-injection 分阶段；多记忆携带策略 | 无 | 无 signed authority | 无 | tool call、sandbox/workspace diff，由 judge 评估 | 未覆盖 |
| SMSR | 同场景 unsigned/authenticated 写入、预置/query-only、ablation | HMAC server-side signing oracle；无 action receipt | 写入/检索来源绑定 | 无 action preflight | 最终回答 ASR，无外部 post-state | 未覆盖；rollback 仅讨论 |
| MemSecBench | 同 case 的 matched Write–Execute–Forget；24 配置 | evidence manifest、service/workspace/artifact 记录 | case/evidence identity；非动作授权签名 | evaluator gates，不是执行前授权 | E3 外化风险与 verified post-W；可评修复 | Forget/repair；无 failover/relaunch |
| OAP | permissive vs restrictive policy 的同接口 live CTF；非 carrier replay | signed decision/receipt | Ed25519 passport、scope、identity | 每次 tool call 前同步验证，服务不可用 fail-closed | live tool-boundary block；无 provider canonical state | 未覆盖 |
| FORGE | instrumented vs non-instrumented、VP approval 对照 | 外部 approval signal；非明确密码学签名 | provenance graph + VP dependency | deterministic reference monitor，未批准不得过边 | info-flow/tool boundary；post-state有限 | blocked retry/recovery；无 failover |
| ACRFence | checkpoint-restore vs no-checkpoint | 模拟 MCP 服务，无 receipt/idempotency 证明 | 无 | checkpoint 在验证后、动作前；不等于 fail-closed | duplicate commit 10/10 vs 0/10 | 有 restore/re-execution 证据；无 carrier 对照 |

## Reasoning

截至 2026-09-07，未找到满足完整条件的公开一手证据：在同一 agent 任务/可回放轨迹中，同时随机化上下文/记忆携带策略与外部签名/来源绑定控制状态，并跨 compaction、memory poisoning、authority update、failover、recovery 和 preflight/action-boundary，以外部 receipt 或 canonical post-state 证明因果结果。

已有证据不是空白，而是被拆在不同层：

1. Governance Decay、ConstraintRot、ControlCapsule 对 context carriage 的控制最接近固定 replay/准因果证据；它们说明 policy 的可见性、稳定回放和 preflight 会影响“是否继续”或工具调用参数，但不能推出 OOB 签名的必要性。
2. SMSR 对写入来源的 HMAC 绑定有真正的外部 signing oracle 和 unsigned/authenticated 对照；它说明 provenance binding 能阻断未授权写入，但 authenticated legitimate-user injection 仍可通过，且没有把“可写入”与“有权执行不可逆动作”连接起来。
3. OAP/FORGE 给出较强的 action-boundary 正向证据：签名 passport、外部 approval 和确定性 reference monitor 可以在 tool boundary 前 fail-closed；但它们没有与可靠 context replay 或 memory carrier 作同轨迹对照。
4. MemSecBench、ACRFence 把副作用、post-state、repair/re-execution 拉出纯文本指标：记忆风险可外化到 workspace/service，restore 可能重复提交。它们也说明 recovery 是独立的 effect-lineage 问题，不能由“控制状态在上下文中可见”自动解决。

因此，本轮把 EX-006 进一步收窄为一个联合检验：

`carrier integrity/survival × authority binding × deterministic enforcement × external effect receipt × recovery semantics`

“带来源、稳定绑定、预算隔离且失败关闭”目前是合理的控制状态设计假设，但只有“signed/provenance-bound carrier 相对于 exact replay/context 的增量效果”被直接对照，且结果落到 `proposal → decision → dispatch → receipt/post-state → recovery` 链上，才足以回答“必须”。单纯看到政策被遗忘、HMAC 能挡 unsigned memory、或 OAP 能拦 tool call，都不足以完成这个合取命题。

## Result

**Status：refined。**

本轮新增的 OAP、FORGE、ACRFence 不是新的正交 EX：它们分别补强执行前签名授权、外部 provenance gate、以及 checkpoint/recovery 的副作用残余，但都落在 EX-006 原问题已声明的 action-boundary、authority/provenance 与 recovery 维度。它们使 EX-006 从“是否需要 OOB control plane”的宽问法，细化成可证伪的 carrier × enforcement × effect-lineage × recovery 对照。

不判定为 `no_delta`，因为本轮新增了一组直接相关的一手正向边界证据和一个实际重复副作用证据；不判定为 `new_gap`，因为缺口是原 EX-006 的未完成交叉项，不是不同对象；不判定为 `merged`，因为 state integrity/carrier survival 与 action enforcement/recovery 之间仍有独立残余风险；不判定为 `retired`，因为完整因果证据仍不存在。

### 新问题

在同一固定 trace 和可查询的模拟外部系统中，固定 `policy_digest、issuer/key_id、actor、object、action、condition、budget`，只随机化 carrier（task-local context、exact active-policy replay、persistent memory、signed OOB/passport）与 enforcement（model-only、deterministic preflight、preflight + reference monitor），再逐一注入 compaction、unsigned poisoning、authenticated poisoning、token-stream authority spoof、authority revoke/update、authorization timeout/failover、checkpoint restore；哪一个因素独立改变了 `proposal → verdict → submitted/unknown → canonical post-state → recovery`，是否存在 carrier × enforcement 的交互残差？

### 证伪方向

- 若 exact active-policy replay + deterministic preflight 在所有故障和恢复条件下与 signed OOB/passport 的 post-state、receipt、recovery 指标等效，则“外部签名是必须的”被证伪为过强命题，OOB 只是实现选项。
- 若 HMAC/OAP 只改变 memory admission 或授权 verdict，而在同一 idempotent provider 上的实际副作用、unknown-commit 与恢复结果不变，则来源绑定不能单独解释不可逆动作安全。
- 若 authenticated legitimate-user poisoning 或合法 authority update 仍能产生错误但格式正确的控制状态，而签名/来源绑定无法区分“有来源”与“正确授权”，则必须把 authority semantics 与 provenance integrity 分开。
- 若加入真实 receipt、重试和 service outage 后 OAP/FORGE 的边界收益或 ACRFence 的重复提交消失，则应收窄为模拟边界效应，而不是普遍控制结论。

### Source 需求

- **P0：** 一个公开 benchmark/code，把 carrier、签名/来源绑定、deterministic preflight/reference monitor 和同一 fixed replay 放入同一 factorial 实验，并提供 tool dispatch receipt、submitted/unknown 状态和 canonical post-state。
- **P0：** authority update/revoke 与 failover 的一手实现或 trace：至少有 signed vs token-stream update、旧版本/撤销/过期、授权服务不可用、重试后 unknown commit、恢复与最终状态。
- **P1：** 在 SMSR 与 MemSecBench 的公开代码/数据上复现“unsigned、authenticated legitimate、authenticated malicious-but-authorized”三类写入，并接一个确定性不可逆动作模拟器；记录 memory snapshot 到 action receipt 的绑定。
- **P1：** 在 ACRFence 类恢复实验中加入 correlation ID、idempotency key、provider receipt 和 action-state query，以区分 duplicate、unknown commit 与安全 retry。
- **P1：** 获取并复核 ControlCapsule 与 Governance/ConstraintRot 的作者代码/数据发布物，确认论文中 reconstructed metadata、grader 与 replay 是否能支持同轨迹再随机化；若不能，保留为论文级证据，不上升为可复现实验。

### 下一步目标建议

先完成“carrier × enforcement × fault × effect/recovery”字段矩阵，再做最小实验；不要继续收集只声称“政策在上下文外更安全”的架构文章。优先组合已有公开组件：Governance/ControlCapsule 的固定任务与 compaction 条件、SMSR 的 signing oracle、OAP/FORGE 的 boundary enforcement、MemSecBench/ACRFence 的外部化状态与恢复指标。研究目标应是识别最小必要条件，而不是证明某个具体 capsule/passport 产品普遍优越。

### 最小实验

用一个固定模型、固定 prompt/tool schema、固定预算和单一不可逆工具，接入确定性模拟 provider：支持 idempotency key、receipt、`submitted/unknown` 查询、canonical post-state 和可控授权服务故障。每个 case 配对运行四种 carrier：task-local context、exact active replay + preflight、persistent memory、signed OOB/passport；三种 enforcement：model-only、deterministic preflight、preflight + reference monitor。故障条件依次为 compaction、unsigned poison、authenticated legitimate poison、token-stream operator spoof、revoke/update、授权服务 timeout/failover、checkpoint restore。

每次动作记录：`trace_id、policy_digest、issuer/key_id、binding、carrier/version、budget、visible_state、preflight_verdict、monitor_verdict、dispatch_receipt、submitted/unknown、canonical_post_state、recovery_action、final_state、MTTR`。先固定 proposal 或使用同一 replay，隔离 carrier/enforcement 的因果影响；再在相同 seed/模型上放开真实 proposal。主要终点是 unsafe proposal、blocked action、actual side effect、unknown commit、duplicate commit、修复成功率和恢复时间，而不是只看最终回答 ASR。

## Scope boundary

本轮按用户约束只新建本文件；没有修改 `research-agenda.md`、daily log、raw、现有 research log 或稳定 Wiki 页面。Source 需求和下一步目标只作为本日志中的研究建议，不写入状态队列。

## 来源索引

- ControlCapsule：<https://arxiv.org/html/2605.12535v3>
- Governance Decay / ConstraintRot：<https://arxiv.org/html/2606.22528v2>
- Sleeper Memory Poisoning：<https://arxiv.org/html/2605.15338v1>；<https://github.com/ivaxi0s/LLM-agent-memory-poisoning>
- SMSR：<https://arxiv.org/html/2606.12703v1>；<https://github.com/tarun-ks/smsr>
- MemSecBench：<https://arxiv.org/html/2607.27080v1>
- Open Agent Passport：<https://arxiv.org/html/2603.20953v1>；<https://github.com/aporthq/aport-spec>；<https://github.com/aporthq/aport-agent-guardrails>
- FORGE：<https://arxiv.org/html/2602.16708v3>
- ACRFence：<https://arxiv.org/html/2603.20625v1>
