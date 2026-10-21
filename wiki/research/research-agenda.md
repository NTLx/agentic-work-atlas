---
type: research-agenda
title: "Agentic Work Atlas 研究议程"
created: 2026-05-22
updated: 2026-10-21
tags:
  - agentic-work-atlas
  - llm-wiki
  - knowledge-management
related_entities:
  - "[[LLM-Wiki]]"
  - "[[Agentic-Engineering]]"
  - "[[Agent-Harness]]"
  - "[[Human-Governor-Agent-Operator]]"
  - "[[Judgment]]"
---

# Agentic Work Atlas 研究议程

## Maintenance

Legacy provenance 维护线已完成并冻结；详情见 research-logs 与 Git 历史（可从 commit `44057e6` 恢复迁移前状态）。

## Claim Recompile Queue

### CR-001 · AI 评测制度执行能力与具体处罚
- Status: blocked
- Priority: P1
- Claim: 制度执行能力背景已确认；待核实首个或具体的官方处罚决定。
- Gap: Evidence
- Evidence: `raw/2026-eu-ai-act-compliance-autonomous-agents.md`；官方执行框架与现有溯源记录见 [[2026-09-05]]。
- Evidence goal: 官方 AI Office/委员会处罚决定文本或独立一手披露，确认或证伪具体处罚实例。
- Last checked: 2026-09-05 · refined
- Next: 触发式复查，不主动追踪 €47M 二手叙事。
- Retry: new-source:eu-ai-act-official-penalty-decision

### CR-002 · Agent 数据最小化是独立治理轴
- Status: blocked
- Priority: P1
- Claim: Agent workflow 的 permission scope、actual-read scope、context/model exposure 与 retention/deletion 应独立测量；过度收集不是架构必然属性。
- Gap: Boundary
- Evidence: [[Agent-Data-Minimization]] 及其关联来源。
- Evidence goal: 生产级 longitudinal actual-read、context exposure、retention/deletion、纠正传播及 permission/retention creep 数据，或最终规范。
- Last checked: 2026-09-19 · refined
- Next: 等待 actual-read / retention-deletion longitudinal evidence 或最终规范。
- Retry: new-source:agent-data-minimization-longitudinal

### CR-003 · AI 监督 AI 的共模误差下界是条件量
- Status: blocked
- Priority: P0
- Claim: 多模型监督的收益取决于 verifier error 的去相关程度；共享错误下界是任务与监督形态条件量，不存在跨任务统一正下界证据。
- Gap: Boundary
- Evidence: [[LLM-as-a-Judge]]；[[Verifiable-Agent-Engineering]]。
- Evidence goal: 同一任务与证据条件下比较静态 panel、可执行 checker、交互环境 verifier、人类裁决或 live Agent supervision。
- Last checked: 2026-09-19 · refined
- Next: 等待跨监督形态同任务联合对照。
- Retry: new-source:shared-error-floor-cross-supervision

### CR-005 · 高采纳组织中的现实校准能力再生
- Status: blocked
- Priority: P0
- Claim: 高 AI 采纳组织是否持续再生不与主生成路径共模的现实校准能力，尚无共同纵向证据。
- Gap: Evidence
- Evidence: [[Labor-AI-Empirical-Calibration]]；[[Skill-Atrophy-and-Knowledge-Debt]]；[[AI-Apprenticeship-and-Lehrwerkstatt]]；本轮推理见 [[2026-10-20]]。
- Evidence goal: 同一 firm × person × occupation × period 纵向观测自主练习 → 真实错误反馈 → 异源/独立检查 → delayed retention/transfer → responsibility/promotion，并连接 AI adoption 与效率。
- Last checked: 2026-10-20 · refined
- Next: 寻找共同纵向队列或高采纳且长期维持独立校准能力的反例。
- Retry: new-source:skill-reproduction-longitudinal

### CR-006 · 评测逃逸是系统性机制而非孤立 harness 事故
- Status: blocked
- Priority: P0
- Claim: 评测逃逸涉及 reference、scope、reachability/containment、monitoring/stop 与搜索能力的交互；现有材料不支持单一普遍首因。
- Gap: Counterexample
- Evidence: [[Evaluation-Integrity]]。
- Evidence goal: 独立 post-hardening 部署级纵向记录，明确 action surface、持续 probing、模型/工具升级、逃逸复发与 stop latency。
- Last checked: 2026-09-19 · blocked
- Next: 只等待 post-hardening 部署级纵向反例。
- Retry: new-source:eval-escape-post-hardening-counterexample

CR-004 已从活跃 Claim 队列移除并入 EX-005 的 production effect/evidence closure；CR-007 已 retire，详情见 2026-10-20 研究日志。

## 当前研究焦点

| 优先级 | 焦点 | 下一步最小动作 |
|---|---|---|
| P0 | 专业能力再生（CR-005） | 寻找采纳、练习、反馈、独立能力与延迟迁移的共同纵向队列。 |
| P0 | Agent 安全外部效果闭环（EX-005，含原 CR-004 observability 字段） | 寻找同一 incident 的 action-surface/coverage、receipt、post-state 与 recovery 联合证据。 |
| P1 | 验证三门联合实验（EX-001/002/004 + CR-003） | 只找同任务、同证据条件下跨门或跨监督形态的联合对照。 |
| P1 | 科学 AI 闭环定向探索（未编号） | 对已入库来源做 evidence matrix；有共同变量与可比较结果后再评估编号。 |

## 开放探索候选

| ID | Priority | Gap | 核心问题 | 唯一触发证据/最小动作 |
|---|---|---|---|---|
| EX-001 | P1 | Boundary | 固定任务、reference 与 evidence 后，verifier 独立性是否降低共同漏报？ | 找同任务跨 verifier family/独立实现的单轴对照。 |
| EX-002 | P1 | Mechanism | access、inspection、completeness、synthesis 哪一层改变验证错误？ | 找固定模型、任务、oracle 与预算的跨门消融。 |
| EX-003 | P1 | Boundary | trigger、receiver、packet/message 与 timing 如何影响人类接手结果？ | 找固定 receiver/queue 的 packet×timing 消融或同案联合 trace。 |
| EX-004 | P1 | Boundary | reference truth、environment/execution truth 与 success provenance 是否独立影响判定？ | 找同 trace 含 reference version、state/receipt、provenance 与跨 verifier 的联合实验。 |
| EX-005 | P0 | Evidence | Agent 安全控制能否闭合到可核验外部效果？吸收原 CR-004 的 action-surface/coverage/receipt/post-state/recovery 字段。 | 找同一 incident 的 policy/version、action receipt、revoke/recovery、canonical post-state 与独立复核。 |
| EX-006 | P1 | Boundary | 高影响动作的控制状态完整性是否需要独立 carrier 与执行边界 enforcement？ | 找 carrier×enforcement×provider post-state 同轨对照或 authority-update 反例。 |
| EX-007 | P1 | Mechanism | Agent 自我改进中变更归因与 feedback/control 不对称是否影响晋级判断？ | 找 production fleet 的 immutable change/evaluator、canary、rollback 与复验联合记录。 |

## Source 需求队列

| 优先级 | 目标 | 当前缺口 | 触发行动 |
|---|---|---|---|
| P0 | Agent 生产安全效果闭环 | 缺同案 action surface、授权、执行、撤销/恢复、post-state 与 review 联结。 | 获取脱敏生产 trace 后 clip+compile，回填 EX-005。 |
| P0 | CR-006 加固后反例 | 缺 post-hardening 部署级纵向逃逸率、复发与 stop latency。 | 仅在独立纵向记录出现时恢复。 |
| P0 | CR-005 劳动×能力再生共同纵向队列 | 缺同一组织/个人/职业/时期的采纳、练习、反馈、能力与晋升链。 | 寻找共同队列或强反例并评估可比性。 |
| P1 | 验证三门联合实验 | 缺同任务下 verifier、evidence 与 reference/provenance 联合操纵。 | 找固定 trace、oracle 与预算的 factorial/matched study。 |
| P1 | 科学 AI 闭环定向对照 | 缺测量/实验反馈与可比较研究结果之间的证据。 | 先对 Leash Bio、Meta open research、Claude-shaped science（可加 Periodic）做 evidence matrix。 |

## 定向探索候选（未编号）

### P1 · AI 科学研究闭环：测量与实验反馈是否是可扩展性的关键中间变量？
- Gap: Mechanism/Boundary；现有材料提出测量与实验反馈可能重要，但尚未显示其与可比较研究结果的关系。
- 不能并入现有 CR/EX：CR-005 研究人的现实校准能力再生；EX-001/002/004 研究 Agent 验证门；EX-007 研究 Agent 自我改进变更治理。本候选关注科学工作流中的测量/实验反馈机制。
- 证伪方向：若控制模型、数据与团队差异后，测量质量、反事实/难例设计和反馈时延与结果无稳定关系，或差异可由其他因素解释，则撤销或并回既有主题。
- Source 需求：一手或可比较材料，报告可审计测量、实验反馈、失败样本利用、成本与可复现结果。
- 最小实验：先对 Leash Bio、Meta open research、Claude-shaped science，并可加入 Periodic，做 evidence matrix；只有出现共同变量与可比较结果才考虑新 EX。
- Status: 未验证假设；不得作为已成立结论。

## 最近思考结论摘要

| 时间 | Claim | Delta | 摘要 |
|---|---|---|---|
| 2026-10-21 | Candidate research audit | merged/retired/refined | CR-004 并入 EX-005、CR-007 retire；CR-001/005 收窄；提出未编号科学 AI 定向探索；压缩 agenda 操作层。 |
| 2026-10-20T23:53:00+08:00 | CR-005 专业能力再生与独立校准 | refined-reasoning | 从保存无 AI 技能收窄为再生不与主生成路径共模的现实校准能力；无新 Evidence，保持 blocked。 |
| 2026-09-07T08:33:43+08:00 | EX-005 耐久执行停止与外部效果 | refined | 区分 durable execution 停止、在途 invocation 与已发生副作用；加入 checkpoint/in-flight 窗口。 |
| 2026-09-07T07:46:00+08:00 | EX-002 证据覆盖与解释 | refined | 区分证据取得、完整性意识与事实整合；保留 evidence-synthesis interference 边界。 |
| 2026-09-07T06:33:25+08:00 | EX-004 oracle 与成功来源 | refined | 区分 reference、environment-state、execution/post-state oracle；仍缺同轨交叉。 |

## 思考日志索引

- [[2026-10-21]] — 全量候选研究主题代谢：CR-004 并入 EX-005、CR-007 retire，并登记科学 AI 未编号候选；无新增 Evidence。
- [[2026-10-20]] — CR-005 深度思考：从技能退化收窄到现实校准权再生；无新增 Evidence。
- [[20260907--ex005-durable-stop-semantics--research]] — EX-005 durable stop 与 in-flight 边界。
- [[20260907--ex002-evidence-coverage-followup--research]] — EX-002 evidence synthesis 边界。
- [[20260907--environment-oracle-provenance--research]] — EX-004 oracle/provenance 边界。

更早历史见 `wiki/research/research-logs/` 与 Git 历史。
