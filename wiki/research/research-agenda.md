---
type: research-agenda
title: "Agentic Work Atlas 研究议程"
created: 2026-05-22
updated: 2026-09-19
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

> [!note] 使用边界
> 本页是操作层，不是事实源。长论证见 [[resolved-judgments]]、[[resolved-principles]] 和每日研究日志。2026-08-24 迁移前的完整状态保留在 Git commit `44057e6`。

## Claim Recompile Queue

### CR-001 · AI 评测制度化进入执行期
- Status: blocked
- Priority: P0
- Claim: AI 评测治理已从自愿最佳实践进入可执行、可处罚的制度阶段。
- Gap: Evidence
- Evidence: `raw/2026-eu-ai-act-compliance-autonomous-agents.md`；官方执法启动新闻稿 [IP/26/1714](https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1714)（2026-07-31）与生效日新闻页（均无 €47M 三案记录）；AI Omnibus 将高风险义务推迟至 2027-12/2028-08；€47M 三案经溯源性定向为单链互引的二手内容站叙事，且 [AI in Europe 追踪](https://aiineurope.co/policy/europe-act-tracker-2026-08-31) 报告原作者已撤回该说法（均不能替代官方决定，详见 2026-09-05 日志）
- Evidence goal: 官方 AI Office/委员会处罚决定文本发布（确认或证伪 €47M 实例），或独立一手披露出现；€47M 三案现为 falsified 候选，制度能力面已一手确认
- Basis: evidence
- Last checked: 2026-09-05T05:00:35 · refined
- Next: 收敛为触发式复查，不再主动检索——€47M 三案保持未证实；等待 (a) AI Office 官方处罚决定文本，或 (b) 独立一手披露；时间观察锚点：AI Omnibus 新增禁止实践条（2026-12 生效）后第一次可验证执法 action
- Retry: new-source:eu-ai-act-official-penalty-decision

### CR-002 · Agent 数据最小化是独立治理轴
- Status: blocked
- Priority: P1
- Claim: Agentic workflow 对广权限、广检索、上下文累积和长期记忆存在结构性压力，但过度收集不是 Agent 架构不可避免的属性；permission scope、actual read scope、context/model exposure 与 retention/deletion 必须独立测量。
- Gap: Boundary
- Evidence: [[20260618-mosaicleaks-privacy-agent]]；[[20260905-numezis-governed-business-agent-sme]]；[[20260614-decentralized-granular-access-control-agentic-ai]]；[[20260710-aws-ktern-agentcore-sap]]；stable compile 见 [[Agent-Data-Minimization]]。
- Evidence goal: 取得生产级 longitudinal data-minimization evidence：task-level actual-read denominator、最小必要读取对照、context/model exposure、retention TTL/project-close deletion、correction/erasure propagation，以及 permission/retention creep 随时间的变化。
- Last checked: 2026-09-19T20:39:00+08:00 · refined
- Next: **停止主动扩 least-privilege 架构案例**；零未授权写入、per-agent least privilege、provider no-retention 与 audit log 均不能单独充当长期数据最小化证据。只在出现实际读取量/保留删除纵向数据或 EDPB 02/2026 最终规范时恢复。
- Retry: new-source:agent-data-minimization-longitudinal

### CR-003 · AI 监督 AI 的共模误差下界是条件量
- Status: blocked
- Priority: P0
- Claim: model-panel agreement 只有在 verifier errors 足够去相关时才能获得接近独立投票的收益；某些 task × panel × evidence 条件下存在可测 shared-error floor，但不存在“跨模型监督必然具有统一正下界”的证据。
- Gap: Boundary
- Evidence: [[20260408-arxiv-2604.07650-llm-judge-behavioral-entanglement]]；[[20260528-apple-nine-judges-two-effective-votes]]；[[20260711-llms-as-a-jury-shared-error-floor]]；stable compile 见 [[LLM-as-a-Judge]] 与 [[Verifiable-Agent-Engineering]]。
- Evidence goal: 若未来要恢复，只接受能把静态 model-panel consensus 与 executable checker、interactive environment verifier、human adjudicator 或 live Agent supervision 放入同一任务/证据条件的比较；用于判断 shared-error floor 是否跨监督形态保留。
- Last checked: 2026-09-19T19:14:00+08:00 · refined
- Next: **停止主动扩来源**；当前强版本已被近零数学 floor 反驳，条件化版本已稳定。等待跨监督形态联合对照。
- Retry: new-source:shared-error-floor-cross-supervision

### CR-004 · Agent Observability 上界随层级变化
- Status: blocked
- Priority: P1
- Claim: Agent observability 至少分四层：被声明/埋点的结构可枚举；行为可靠性必须用 action-surface coverage、recall 与 response latency 统计；外部效果需要 provider-authoritative post-state / recovery lineage；意图只能间接推断，不能当作直接可观测真值。
- Gap: Boundary
- Evidence: [[20260919-otel-genai-agent-observability-main]]；[[20260919-otel-genai-open-governance-proposals]]；[[20260618-google-deepmind-ai-control-live-monitoring]]；[[20260622-google-deepmind-ai-control-roadmap]]；stable compile 见 [[Agent-Observability]]。
- Evidence goal: 同一生产事件键下同时取得 reachable action-surface denominator、monitor coverage/recall、synchronous block/result、provider receipt/canonical post-state、revoke/recovery 与 independent review；用于区分 instrumentation completeness、behavior assurance 与 effect closure。
- Last checked: 2026-09-19T20:39:00+08:00 · refined
- Next: **停止主动扩 observability schema/roadmap 文档**；只接受部署级联合 trace、独立 conformance/coverage 测试或 current normative OTel 治理字段实质落地。旧 agenda 的 PR #483 本轮无法在 current repo 核实，不再保留事实地位。
- Retry: new-source:agent-observability-deployment-closure

### CR-005 · AI 采纳与专业能力再生之间仍缺共同纵向链
- Status: blocked
- Priority: P0
- Claim: 当前证据支持三个彼此分离的风险信号——高暴露职业的青年/早期职业入口走弱、培训供给未必转化为能力、AI assistance 在特定学习任务中可能降低短期无 AI 独立能力；但尚不能证明同一组织在获得效率收益的同时把专业能力再生成本系统性外部化。
- Gap: Boundary
- Evidence: [[20260305-anthropic-labor-market-impacts-ai]]；[[20260812-stanford-canaries-coal-mine-ai-employment]]；[[20260624-prompting-change-denmark-ai-adoption]]；[[20260414-nyfed-genai-training-access]]；[[20260201-how-ai-impacts-skill-formation]]；[[20260630-ramp-ai-jobs-firm-spending-workforce]]；[[20260901-dallasfed-ai-automation-job-postings]]；[[20260428-census-youre-not-hired-ai-early-career]]；stable calibration 见 [[Labor-AI-Empirical-Calibration]] 与 [[Skill-Atrophy-and-Knowledge-Debt]]。
- Evidence goal: 同一 firm × person × occupation × period 队列同时观测 AI adoption/intensity、产出/效率、entry hires、training participation/completion、unaided capability、delayed retention/transfer、promotion/qualification；或第二个高采纳但长期保持专家补充率/独立验证能力的组织反例。
- Last checked: 2026-09-19T22:51:00+08:00 · refined
- Next: **停止主动扩泛 deskilling / apprenticeship 案例**；等待共同纵向队列、Shopify/Lehrwerkstatt 长期结果，或能直接连接效率收益与能力再生的生产证据。
- Retry: new-source:skill-reproduction-longitudinal

### CR-006 · 评测逃逸是系统性机制而非孤立 harness 事故
- Status: blocked
- Priority: P0
- Claim: 评测完整性失效由 reference 暴露、scope contract 歧义、effective reachability/containment 缺口、monitoring/stop 断点与模型搜索能力共同决定；现有跨厂商材料不支持把所有事件归为少数配置事故，也不支持指定单一普遍首因。
- Gap: Counterexample
- Evidence: [[20260306-anthropic-browsecomp-eval-awareness]]；[[20260804-openai-third-party-cyber-evaluation-boundaries]]；[[20260826-openai-hf-incident-road-ahead]]；[[20260727-hf-agent-intrusion-technical-timeline]]；稳定编译见 [[Evaluation-Integrity]]。
- Evidence goal: 独立部署级 post-hardening 纵向记录——明确 threat model/action surface，持续 adversarial probing，大规模运行后低/零越界，模型/工具升级后仍成立，且已知 mismatch 修复后不通过替代路径复发。
- Last checked: 2026-09-19T19:14:00+08:00 · blocked
- Next: **停止横向扩事故清单**；只等待 post-hardening escape rate / mismatch recurrence / stop latency 的独立纵向反例或复现。
- Retry: new-source:eval-escape-post-hardening-counterexample

### CR-007 · 全球南方 AI 跃迁需要制度共演化
- Status: blocked
- Priority: P2
- Claim: 技术形态可以跨代跃迁，但制度能力和本地评价标准无法被完整进口，只能在使用中共演化。
- Gap: Counterexample
- Evidence: 现有 M-Pesa、UPI 与东亚案例只形成半实例，缺 AI 原生纵向材料
- Evidence goal: 找到技术与制度同时外部移植且长期低错配运行的完整反例。
- Last checked: 2026-08-30T06:00:41 · blocked
- Next: 等待新的已长期运行、同时报告本地制度/评价标准与部署结果的一手 AI 案例；当前不主动扩展检索
- Retry: new-source:global-south-ai-ecosystem

## 2026-09-18 研究代谢收敛

本轮知识审查确认：2026-08-29 至 2026-09-07 的 51 个 `Explore` 大多不是 51 个独立问题，而是对少数研究线的重复收窄。后续不再按 Explore 数量增长研究面，而按以下规则收敛：

| 研究簇 | 当前状态 | 处理决定 |
|---|---|---|
| EX-001 / EX-002 / EX-004 验证链 | 已多轮 refined，边界稳定为 verifier independence × evidence coverage/interpretation × reference/provenance | **冻结扩题**；只补 P0/P1 一手证据与联合对照，稳定边界编译进 [[Verifiable-Agent-Engineering]] |
| EX-003 handoff / facilitator | 第一批已编译进 [[Escalation-Based-Human-Oversight]]：trigger calibration、receiver selection、packet/message、human action/outcome 已形成连续事件链，timing/queue capacity 作为横切变量 | **保留单一开放问题**；没有固定 receiver/queue 下的 packet×timing 消融或同案生产 trace 前，不再新增子问题/横向来源 |
| EX-005 外部效果闭合 | 已收窄为 cancel/stop → in-flight → receipt → provider post-state → reconciliation | **保留为 P0 实验线**；不再用新的 API 文档替代同案闭链证据 |
| EX-006 控制状态承载 | 已收窄为 carrier integrity × authority binding × deterministic enforcement × effect/recovery | **保留为 P1 对照线**；若 exact replay + preflight 与 signed OOB 等效，则降为实现选项 |
| EX-007 自我改进变更治理 | 已收窄为 change attribution + feedback/control asymmetry | **冻结新 gate**；优先找 offline→online / hidden holdout / policy freeze / rollback 的同变更证据 |
| Agent Security | 已形成 [[Agent-Security]] stable Topic | **停止重复建 Topic**；研究只补 action-surface、revoke、recovery 和同案责任链缺口 |
| Agent Attack Surface | 已完成 [[Agent-Attack-Surface]] promotion：Agent Traps taxonomy + FORGE 无指令污染 + Context Collapse / AI Worm 跨产品链已形成独立承载 | **已收敛**；后续只补跨产品复现、action-surface 分母与防御消融，不再重复论证是否应建 Topic |
| MCP 状态迁移 | 已明确“去 session ≠ 去状态” | **并入 MCP / EX-005/006 边界维护**；不新增独立 EX |
| 劳动经济学 | 已收窄为 adoption carrier × firm selection × labor-flow composition | **保持独立 P0 实证线**；必须按共同企业/职业/时期键对齐，禁止跨层抵消 |
| AI 时代设计方法论 | 当前仅 partial | **保留 P1**；补跨公司、责任与反馈时延证据后再更新 Topic |

**停止条件**：若一次 Explore 只得到 `refined/no_delta` 且没有新增一手证据、反例、可执行实验或 stable promotion 条件，则不再新增 Explore；改为更新现有 agenda 项或等待触发式新证据。

**代谢优先级**：`clip/compile → stable Topic/Comparison 更新 → Output` 高于继续扩展 Explore。新增研究问题必须证明其不能被现有 CR/EX/Topic 吸收。

## 当前研究焦点

| 优先级 | 焦点 | 下一步最小动作 |
|---|---|---|
| P0 | Agent 安全 Topic 建设 | [[Agent-Security]] 五阶段骨架已稳定；EX-005/006 第一批证据已把 revoke/recovery 拆成 permission stop → in-flight stop → effect settlement → canonical post-state，并把 control carriage 拆成 carrier/provenance/survival/binding/preflight/enforcement。下一步只寻找同一生产 incident 的 `flag → verdict → authorization → actuation → revoke/recovery → canonical post-state → independent review` 联合 trace，不再横向累积架构文档 |
| P0 | 验证器危机研究线 | EX-001/002/004 与 CR-003 支柱来源均已 clip+compile；独立性门进一步细化为 error covariance / effective independent votes / task-conditioned shared-error floor，而不是模型数量或家族数。三门模型仍为 verifier independence ×（access→inspection→completeness→synthesis）×（reference→environment→execution→success provenance） | 下一步仅接受跨两门以上或跨监督形态的同轨联合对照，不再扩静态 benchmark 清单 |
| P0 | Evaluation Integrity / CR-006 | 已形成 [[Evaluation-Integrity]] stable Topic；BrowseComp、UK AISI/Irregular、OpenAI/HF 复发链与 HF victim-side forensic 已入库。当前只缺 post-hardening 纵向反例，不再扩事故列表或把 cyber capability 材料误算成 eval escape |
| P0 | 劳动经济学实证 | 先按“企业净 headcount × 职业/入门流量 × 再生代理”建立校准骨架；新增 adoption carrier 分层：formal/function/worker-task/operational；补共同企业—个人—职业—时期键、培训完成与独立能力；不要用企业扩张直接抵消入门招聘收缩 |
| P1 | MCP 无状态转折 | `SEP-2663` 已标 Final，但 Tasks 渲染规范仍为 Draft、官方 SDK 支持不齐；`taskId` 同时是 durable state locator 与 HTTP 路由键，cancel 只是最终一致的协作式意图，不证明停止或回滚；下一步核对主体绑定、TTL/撤销、replay/failover 与 effect lineage |
| P1 | AI 时代设计方法论对照 | 初步支持设计对象扩展到模型/系统行为、反馈/控制和可执行工作流；Anthropic 有团队案例，Google/Microsoft 目前只有方法指南；下一步补当前负责人/团队材料与责任、返工、反馈时延字段 |
| P2 | Topic 与复核队列代谢 | [[Agent-Attack-Surface]] 已完成 promotion，并与 [[Agent-Security]] 明确分工；下一步转向 Entity review 新基线与 legacy provenance，不再重复审查安全威胁面是否需要独立 Topic |

## 开放探索候选

| ID | 候选问题 | 当前判断 | 证伪方向 | 下一步 |
|---|---|---|---|---|
| EX-001 | 验证器独立性是否是目标、证据、执行、时间四轴的最弱轴瓶颈？ | `2604.07650` 与 REDAgentBench 已 clip+compile：前者在 18 LLM / 6 家族上用 BEI/CIG 量化行为纠缠并关联 judge over-endorsement，支持把 verifier independence 保留为独立变量；后者证明 evidence view 会改变测得结果，但未操纵 verifier family；refined | 固定证据访问、reference 与任务后，跨家族/独立实现的单轴变化仍不能降低共同漏报，或独立性效应完全由证据覆盖/判定质量解释 | 第一批证据已编译进 [[Verifiable-Agent-Engineering]]；后续只找固定 task/reference/evidence 下的 verifier-family / implementation 单轴对照，不再泛搜 |
| EX-002 | 独立性之外，证据覆盖与证据解释是否构成验证的第二个必要门？ | 两批证据已完成：AJ-Bench / Partial Evidence / REDAgentBench 区分 visibility、inspection、completeness 与 evidence-view；SkillTV-Bench 补 procedural verification knowledge，`Cited but Not Verified` 补 evidence-synthesis interference。当前可稳定写成 access → inspection procedure → completeness awareness → synthesis；refined | 固定模型/验证器、任务、reference、外部 oracle、token/time 预算后，上述任一层变化仍不能改变漏报/误报；或深度效应在独立事实 oracle 与固定信息预算下消失 | **冻结扩来源**；只在出现与 verifier independence 或 reference condition 同轨交叉的 factorial / matched study 时恢复 |
| EX-003 | Facilitator agent 能否在缺少人类隐藏信息的条件下校准“何时升级、升级给谁、给什么上下文”，而不制造新的监督盲区？ | 第一批 6 个来源已 clip+compile：2606.10906 给 rejector/hidden-feature 边界；PMLR 333 给 class-dependent calibration 反例；2112.06751 直接操纵 deferral message；Alibaba 给 trigger type/timing/human effort 现场异质性；Google SRE 与 AWS 给 packet/receiver/telemetry 生产契约。当前稳定链为 trigger/type → receiver → packet/message → human action → outcome，timing/queue capacity 横切；refined | 固定 Agent 输出、receiver 与 queue state 后，若 packet/message/timing 不再改变 human correctness、latency、clarification/rework 或依赖，则并回 EX-002；否则保留 handoff calibration 子门 | **停止横向扩来源**；只接受固定 receiver/queue 下的 packet×timing factorial，或同一生产 case 含 trigger/receiver/packet/version/handoff/ack/human action/outcome 的联合 trace |
| EX-004 | reference integrity 与 success provenance 是否构成独立必要门？ | 两批证据已完成：EnvTrustBench / EVMbench / REDAgentBench 区分 reference、environment、execution truth；AgentJudgeBench 提供 paired reference-availability intervention；AcquaBench 用 CLEAN/GOLD/SHAM 把 outcome correctness 与 success provenance 分开。当前可稳定写成 reference truth → environment truth → execution truth → success provenance；refined | 固定 verifier、trace 与 external post-state 后，若 reference condition / information-state provenance 不再改变误放行、归因、排名或成功率，则削弱该分层 | **冻结扩来源**；只寻找同时含 reference version、state hash、visible/held-out trace、receipt/post-state、information-state intervention 与跨 verifier 的联合 benchmark |
| EX-005 | 动作授权、独立执行点与撤销/恢复是否是独立必要门？ | 第一批已编译：ACRFence 证明 local restore ≠ external rollback；HBHC 提供有界 permission-stop；Microsoft Saga 提供 committed-effect compensation 基线。当前可稳定拆成 permission stop → in-flight stop → committed-effect settlement/compensation → provider-authoritative post-state reconciliation；refined | 若在固定 incident 中 credential revoke、in-flight cancel、compensation receipt 与最终 provider state 可证明等价，则可合并；否则继续保留 commit-state uncertainty / effect-lineage | **停止横向扩来源**；只寻找同一生产 incident 上带统一关联键的 revoke latency、unknown-commit、compensation result、canonical post-state 与 independent review |
| EX-006 | 高影响/不可逆动作是否必须以带来源、稳定绑定、预算隔离且失败关闭的控制状态抵达执行边界？ | 第一批已编译：Ghost in the Context / ControlCapsule 补 presence-soundness-binding-preflight；Governance Decay 补 carrier survival；SMSR 补 issuer/provenance；MemSecBench 补 Write→Execute→Forget 生命周期。当前稳定边界为 decision-time control integrity + authority/provenance binding + deterministic action-boundary enforcement；仍未证 OOB control plane 普遍必要；refined | 若 exact active-policy replay + preflight + deterministic enforcement 与 signed OOB carrier 在 compaction、authority update、failover、effect/recovery 上等效，则 OOB 仅为实现选项；否则保留独立 control carrier 子门 | **停止横向扩来源**；只接受 carrier × enforcement × provider post-state 的同轨生产级对照或 authority-update/recovery 反例 |
| EX-007 | 自我改进 Agent 的变更晋级是否需要按变更对象分层的不可自证门，防止 harness、评估器、目标与策略共变把“分数提升”伪装成能力/安全提升？ | 第一批 4 篇已 clip+compile：HarnessEvolve 提供模块解耦/双 gate/snapshot；HSI 提供 task harness→evolver strategy→frozen outer anchor；Harness Updating≠Benefit 分离 updater 与 beneficiary 并引入 activation/adherence；Rethinking 用 matched search + disjoint held-out 证明性能提升可能来自搜索/benchmark reuse。当前稳定为“变更归因 + feedback/control 双重不对称”；refined | 若固定模型/任务后，matched-search、held-out、activation/adherence 与独立安全复评都无法留下额外残差，或所有残差可由 EX-004/006 完整解释，则削弱或合并 EX-007 | **停止横向扩 benchmark**；优先寻找 production fleet 的 immutable change hash / evaluator version / feedback history / canary / rollback / post-rollback verification 联合记录 |

## Source 需求队列

| 优先级 | 目标 | 当前缺口 | 触发行动 |
|---|---|---|---|
| P0 | Agent Safety Topic 跨层核验 | 五阶段骨架与一条事故级响应链已找到；下一步以事件级标识对齐 `flag → verdict → authorization → actuation → revoke/recovery → canonical post-state → review`，并把 `authority stop / in-flight stop / effect reconciliation` 分开核验 `owner / action-surface`，不把结构地图当作安全效果证据；不由 recompile 执行 |
| P1 | AgentCore 跨层效果回执 | AWS AgentOps/AgentCore 一手材料把 framework、service、infrastructure、application telemetry、W3C trace context、Gateway policy、版本化 Runtime 与 CloudTrail 放入同一架构，但没有同案导出连接 `policy_version → action receipt → revoke-after-send → canonical post-state → independent review` | clip+compile → CR-004 / EX-005；优先寻找跨控制面、工具面和目标系统 audit log 的脱敏生产 trace |
| P2 | Agent Attack Surface 证据维护 | [[Agent-Attack-Surface]] 已由 Agent Traps taxonomy、FORGE 无指令污染与 Context Collapse / AI Worm 跨产品链完成 promotion；页面已区分攻击面与 [[Agent-Security]] 控制/责任闭环 | 后续仅在出现跨产品复现、状态传播量化、联合攻击或防御消融时更新；不再作为 Topic 创建候选 |
| P0 | EU AI Act 首轮罚款官方决定 | €47M 三案系单链互引二手叙事（法律基础矛盾、无官方决定原文），需官方决定/一手披露判定真伪 | clip → 核对 CR-001 |
| P0 | Anthropic 评测完整性材料 | **BrowseComp 已 clip+compile**：[[20260306-anthropic-browsecomp-eval-awareness]]；Mythos Preview 仅保留为 cyber capability / sandbox-exploit 能力背景，不再当作一次 eval-escape 事故；Opus 4.5 System Card 的去污染流程属于防御背景，当前不为 CR-006 重复入库 | 已收敛；后续只在 Anthropic 出现新的独立 eval-integrity incident 或 post-hardening 纵向结果时恢复 |
| P0 | OpenAI / HF 评测越界披露 | **已 clip+compile**：[[20260804-openai-third-party-cyber-evaluation-boundaries]]、[[20260826-openai-hf-incident-road-ahead]]；HF 受害方既有 [[20260727-hf-agent-intrusion-technical-timeline]] 已从 index 恢复 full Raw 并补入 CR-006 | 已编译进 [[Evaluation-Integrity]]；停止重复摄入同一事故的摘要版本 |
| P0 | 评测逃逸加固后反例 | 仍缺独立部署级 post-hardening 纵向记录：threat model/action surface 明确、持续 probing、大规模运行后低/零越界、模型/工具升级后仍成立、mismatch 不经替代路径复发、stop latency 可审计；受控 SandboxBench 不足 | **唯一开放缺口** → CR-006；等待触发式新证据，不主动横向搜索事故 |
| P0 | arXiv 2604.07650 行为纠缠框架 | **已 clip+compile**：[[20260408-arxiv-2604.07650-llm-judge-behavioral-entanglement]]；已进入 EX-001 三门模型，CR-003 仍需单独处理 shared-error floor 的任务域边界 | 后续只在 CR-003 recompile 时与 Apple / 2607.10139 对照 |
| P0 | Apple《Nine Judges, Two Effective Votes》 | **已 clip+compile**：[[20260528-apple-nine-judges-two-effective-votes]]；9 judges / 7 families 只有约 2.18 个有效独立投票，8–22 pp independent-voting deficit 已进入 CR-003 | 已收敛；只在独立复现或 live verifier panel 出现时恢复 |
| P0 | arXiv 2607.10139《LLMs as a Jury》 | **已 clip+compile**：[[20260711-llms-as-a-jury-shared-error-floor]]；七 benchmark 的 task-conditioned floor、cross-family panel 与 generator-family robustness 已进入 CR-003 | 已收敛；近零数学 floor 已否定普遍正下界强版本 |
| P0 | 验证器独立性四轴对照 | `2604.07650` 已 clip+compile；第一批证据已确认 independence 与 evidence/provenance 是可分的测量门，但仍缺固定 task/reference/evidence 的独立实现单轴实验；`trajectory-judge` / `BabelJudge` 目前不能补足这一缺口 | 仅寻找同任务、固定证据与 reference 的跨家族/独立实现对照；没有这种设计则保持 refined，不继续扩来源数量 |
| P0 | AJ-Bench 环境感知验证基准 | **已 clip+compile**：[[20260420-aj-bench-agent-as-judge]]；信息取得、状态验证、过程验证与 reference provenance 边界已进入 EX-002 / [[Verifiable-Agent-Engineering]] | 已收敛；除非出现新版本或独立复现，不再重复处理 |
| P0 | SkillTV-Bench 证据驱动轨迹验证 | **已 clip+compile**：[[20260806-skilltv-bench]]；已把 task-time procedural knowledge / inspection plan / inspection log 编译进 EX-002，并记录 JudgeSkill 同时改变知识与执行过程的混杂边界 | 已收敛；仅新版本或独立复现时恢复 |
| P1 | Cited but Not Verified 来源归因深度消融 | **已 clip+compile**：[[20260507-cited-but-not-verified]]；已将 Link Works / Relevant Content / Fact Check 分层和 2→150 tool-call synthesis degradation 编译进 EX-002，并明确不把该消融外推成普遍安全效果 | 已收敛；只有独立事实 oracle 或固定信息预算复现才恢复 |
| P0 | Human-AI Teaming Through the Lens of Calibration | **已 clip+compile**：[[20260609-human-ai-teaming-calibration]]；rejector calibration、人类隐藏特征与不可约 excess-risk 边界已进入 EX-003 | 已收敛；只在有生产 routing replication 或新的可辨识性反例时恢复 |
| P0 | 选择性预测的校准失效 | **已 clip+compile**：[[20260629-selective-prediction-clinical-calibration]]；class-dependent miscalibration 与 aggregate-metric masking 已进入 EX-003，明确全局 confidence threshold 不能自证可靠 deferral | 已收敛；临床任务结果不外推为通用 handoff 效果 |
| P1 | 人类-路由消息效应 | **已 clip+compile**：[[20211213-human-ai-interaction-selective-prediction]]；固定 receiver 下 deferral status / AI prediction 的消息操纵已进入 EX-003，确认 packet/message 本身是行为变量 | 已收敛；后续只找长程 handoff packet 的独立复现/消融 |
| P0 | 主动升级的部署级长程案例与交接契约 | **已 clip+compile**：[[20260514-alibaba-agentic-ai-hitl-field-experiment]]、[[20260919-google-sre-ai-operator-handoff]]、[[20260610-aws-agentic-handoff-contract]]；trigger type/timing/human effort、完整 investigation-history handoff、versioned packet/receiver/latency/completeness 字段已进入 EX-003 | 已收敛；三者仍缺固定接收面下 packet×timing 因果消融，后续只接受联合 trace/experiment |
| P1 | 接收面与转接遥测 | AWS packet/receiver/latency/completeness 与 Google SRE full-history handoff 已完成第一批编译；Alibaba 补 timing/human-effort，但当前仍没有同案把 packet version、receiver load/queue、handoff time 与 human outcome 全部连起来 | **仅保留联合生产 trace 缺口**；不再为“字段可记录”单独增加 schema 文档 |
| P0 | AgentJudgeBench reference 对照 | **已 clip+compile**：[[20260827-agentjudgebench]]；当前一手版本为 3,808 instances / 6 DAG topologies / 3 difficulty tiers，并提供 paired with/without-ground-truth 条件；旧 agenda 中 C3/120-record 描述不再作为当前版本依据 | 已进入 EX-004；后续只在版本更新或外部 reference audit 出现时恢复 |
| P0 | OpenAI coding evaluation audits | **已 clip+compile**：[[20260223-openai-swe-bench-verified-audit]]、[[20260708-openai-swe-bench-pro-audit]]；已固化 selected-subset denominator、题面/测试/gold patch 错配、low-coverage、独立工程师复核与 contamination 分离，并明确 benchmark-quality audit ≠ run-level external oracle | 已进入 [[Verifiable-Agent-Engineering]]；后续只在独立复现、修复后纵向结果或公开 benchmark manifest/version ledger 出现时恢复 |
| P0 | Agentic Benchmark Checklist | **已 clip+compile**：[[20250703-agentic-benchmark-checklist]]；task validity / outcome validity / reporting、semantic equivalence、GT correctness/isolation、Oracle solver、human agreement、environment/contamination 字段已进入 EX-004 | 已收敛；ABC 作为 audit contract 使用，不再把 checklist 当作必要/充分定理 |
| P0 | GeneBench target identifiability | **已 clip+compile**：[[20260423-openai-genebench-target-identifiability]]；agent-visible evidence → identifiable target → tolerant reference、独立 target review、trace/leakage/shortcut/prompt-grader audit 已进入 EX-004 | 已收敛；构造期 review 不当作逐 run external oracle，后续只等独立复核或公开逐题 manifest |
| P0 | AcquaBench success provenance | **已定位一手 arXiv 并 clip+compile**：[[20260727-acquabench-success-provenance]]；CLEAN/GOLD/SHAM matched intervention 已进入 EX-004，用于区分 outcome correctness 与 success provenance | 已收敛；等待独立复现或与 verifier/reference/environment truth 联合操纵的后续工作 |
| P0 | EnvTrustBench / EVMbench 三层 oracle | **已 clip+compile**：[[20260507-envtrustbench-evidence-grounding]]、[[20260218-openai-evmbench]]；已明确 environment truth / execution truth，并记录 EVMbench reference-quality 外部争议 | 第一批已收敛；后续只寻找能把 reference version、state hash、receipt/post-state 与跨 verifier 放在同轨的联合 benchmark |
| P0 | tau3 task fixes | **已 clip+compile**：[[202602-tau3-task-fixes]]；27 airline + 26 retail 的 expected-action / ambiguity / constraint / fallback / loophole 修复及 pass^1/pass^4 变化已进入 EX-004，并明确这是多变量 benchmark repair，不是 reference-only fixed-trace 实验 | 已收敛；后续只在 task/evaluator version ledger 或独立复现出现时恢复 |
| P0 | SWE-bench Verified oracle 质量审查 | **已 clip+compile**：[[20260223-openai-swe-bench-verified-audit]]；原始 1,699→500 的三专家筛选与 2026 年 selected 138-task 再审边界已固化；59.4% 仅属于该 hard subset，不能外推全 500 | 已并入 OpenAI coding audit / EX-004；停止重复建一份同源摘要 |
| P0 | PatchDiff 行为等价复核 | **已 clip+compile**：[[20250319-patchdiff-swe-bench-correctness]]；已固化 test-pass ≠ behavioral equivalence、developer patch ≠ unique truth、29.6% divergent / 28.6% confirmed-wrong-among-divergent 与 +6.2pp resolution-rate inflation 的边界 | 已进入 [[Verifiable-Agent-Engineering]]；后续只在独立复现、更多模型/基准或固定 trace 的 semantic-equivalence adjudication 出现时恢复 |
| P0 | ELT-Bench-Verified benchmark audit | **已 clip+compile**：[[20260331-elt-bench-verified]]；81 个 transformation-failure tasks 中 82.7% 含 benchmark-attributable error，Fleiss κ=0.851/0.755，30 个无法可靠修正的 GT columns 因专家 agreement 仅 57.8% 被移除；同一 SWE-Agent + Claude Sonnet 4.5 下 22.66%→32.51% | 已进入 [[Verifiable-Agent-Engineering]]；reference/evaluator correction 字段已闭合，不再继续横向扩同类 benchmark audit |
| P1 | 真实 Agent trace 的语义等价与 reference 版本 | PatchDiff 已补 coding benchmark 的 behavioral-equivalence discrepancy，但仍缺同一生产 Agent trace 上“结构不同但结果等价”的 reference、版本变更、provider state 与独立裁决联合记录 | 只接受 production trace / external adjudication；停止继续补离线 coding benchmark |
| P1 | reference 呈现方式的因果对照 | 缺把正确 reference、错误 reference、只给 rubric 和不展示 reference 随机化的 live-agent judge 研究 | new-source → EX-004 |
| P0 | 三门交叉操纵 | **REDAgentBench 与 Partial Evidence Bench 均已 clip+compile**：[[20260811-redagentbench-executable-red-teaming]]、[[20260506-partial-evidence-bench]]；前者固定 rollout 操纵 evidence/proof contract，后者固定 oracle 改变授权可见证据；仍没有同时操纵 verifier independence 与 reference/provenance 条件 | 只寻找带固定 trace、可重放环境、版本化 reference/provenance ledger、跨 verifier/外部 oracle 的 factorial benchmark；CAFE 仅作实验设计方法参考，不再重复摄取两份既有来源 |
| P1 | ALE Robotics 的 hidden-grader integrity 边界 | 官方协议把 hidden seed、verify 阶段隔离、engine-native 重算、validated/verified attestation 分开；但 anchor/reference 仍由同一 benchmark 体系提供，未操纵错误/语义等价 reference，也没有跨 verifier 或外部 truth 对照 | clip+compile → EX-004；提取 reference owner/version、hidden seed、grader isolation、score re-derivation、attestation 与 external adjudication 的分层字段 |
| P0 | Agent permissions：interface 到 enforcement | 已核读 arXiv 2607.13718，尚未进入 raw/source；需提取权限规格、推导、运行时执行、审批透明度、撤销与 reviewer overhead 字段 | clip+compile → EX-005 |
| P0 | Deterministic pre-action authorization | 已核读 arXiv 2603.20953 v1；需核查 OAP 威胁模型、单域/非随机 CTF、平台信任、ESCALATE 未实现与 pre-tool-call gate 边界；论文自报结果不作普遍事实 | clip+compile → EX-005 |
| P0 | FORGE / Formal Policy Enforcement | arXiv 2602.16708 v3 提供多 Agent reference monitor、provenance substrate 与受控任务结果，尚未进入 raw/source；需保留 assume/guarantee、instrumented-surface、并发与 recovery 边界 | clip+compile → EX-005 |
| P1 | Janus 用户参与式权限管理 | arXiv 2607.01510 以 6 个 permission assistant、3 类 synthetic responder 做小规模对照；需提取人审—负担—攻击调用权衡及 synthetic responder 限制 | clip+compile → EX-005 |
| P0 | Microsoft Azure SRE Agent 审计与 incident metrics 文档 | 已有事件名、关联字段和缓解指标，尚未进入 raw/source；需核对字段是否能回链到实际动作与审批 | clip+compile → EX-005 / CR-004 |
| P1 | AWS Druva production recovery workflow | 已有 8–10 agents、scoped permissions 与 recovery workflow 的客户披露；缺授权、撤销、回滚和 action-surface 分母 | clip+compile → EX-005 |
| P0 | ACRFence / checkpoint-restore 副作用 | **已 clip+compile**：[[20260321-acrfence-semantic-rollback]]；10/10 duplicate commit 与 stateless authority resurrection 已进入 EX-005；同时保留“ACRFence mitigation 尚未实现评估”的边界 | 已收敛；仅 mitigation 实测、跨框架复现或 provider-authoritative post-state 证据出现时恢复 |
| P0 | HBHC / 有界层级撤销 | **已 clip+compile**：[[20260520-hbhc-cryptographic-revocation]]；49-agent 四层级联撤销与确定性 zombie-window 已进入 EX-005，并明确 permission stop ≠ rollback | 已收敛；后续只关心 revoked-after-send、旁路 verifier 或独立复现 |
| P1 | 逐动作授权、撤销与恢复实测 | OpenAI/HF 事故材料提供事故级遏制锚点；MCP Tasks、A2A、Temporal、OAuth 与 AWS Step Functions 补足取消、令牌失效、在途终态、状态查询与补偿语义；Atomix/Cordon/Dapr/CAVA/Auditable Agents 区分 gate、provenance、dispatch receipt 与 provider post-state，但仍缺逐动作撤销耗时、未知提交率、post-state 对账、回滚成功率和 MTTR | clip+compile → EX-005 |
| P1 | Recourse/BCCA 与 Stripe 效果结算边界 | Recourse/BCCA 提供本地 provider-compatible effect/recovery receipt 与 residual 结果；Stripe 官方文档提供 idempotency、cancel/refund 与 5xx reconciliation 语义，但均缺 revoke-after-send、provider-authoritative post-state 与独立复核的同案证据 | clip+compile → EX-005；提取 `action/intent identity → provider receipt → cancel/recovery → post-state → independent reconciliation` 字段，保留 sandbox 与 provider 自身复核限制 |
| P0 | 跨系统撤销传播与恢复链 | Google IAM 策略变更通常约 2 分钟、可能 7 分钟以上；Entra 应用自有 session 需应用撤销；GitHub 事故显示恢复、豁免、缓存刷新和确认分步完成；缺 Agent action 同链实测 | clip+compile → EX-005 / CR-004 |
| P1 | Agent incident response actuation trace | 新事故与运营材料补足事件 ID、审批/工具事件和局部恢复字段，但仍缺同一事件键连接 `flag→verdict→policy version→action-surface→in-flight→revoke/recovery→canonical post-state→independent review` 的脱敏导出；优先取得同案 effect lineage，不再横向累积 schema 文档 | clip+compile → EX-005 / Agent-Security Topic |
| P0 | Policy-carriage integrity / ControlCapsule | **已 clip+compile**：[[20260502-ghost-in-context-policy-carriage-integrity]]；presence / semantic soundness / binding / control budget / preflight 与 0/90 behavioral negative boundary 已进入 EX-006 | 已收敛；只等待 carrier × enforcement × external post-state 联合对照 |
| P0 | Governance Decay / ConstraintRot | **已 clip+compile**：[[20260621-governance-decay-constraintrot]]；1,323 episodes 的 compaction decay、Constraint Pinning 与 survival≠authenticity 边界已进入 EX-006 | 已收敛；operator impersonation / authority authenticity 继续由 provenance 子门承接，不再重复扩 compaction 证据 |
| P0 | Sleeper Memory Poisoning | [arXiv 2605.15338](https://arxiv.org/abs/2605.15338) v2 已核读但未进入 raw/source；需提取 memory write—retrieve—use 三阶段、删除/纠正/用户审查/来源谱系防御缺口，并与 CR-002 区分数据最小化问题 | clip+compile → EX-006 / CR-002 |
| P1 | Security-Recall Divergence | [arXiv 2604.20911](https://arxiv.org/abs/2604.20911) 已核读但未进入 raw/source；需核查 omission/commission 不对称、Safe Turn Depth 与格式代理限制，不能把代理约束直接外推为真实泄露风险 | clip+compile → EX-006 / CR-004 |
| P1 | SMSR / runtime memory provenance | **已 clip+compile**：[[20260610-smsr-runtime-memory-provenance]]；HMAC write provenance、authenticated injection 分支与 utility trade-off 已进入 EX-006，并明确 authenticity≠semantic correctness | 已收敛；真实 backend / authority update / external post-state 作为联合证据缺口保留 |
| P1 | MemSecBench memory lifecycle | **已 clip+compile**：[[20260729-memsecbench-memory-lifecycle]]；Write→Execute→Forget 与 24-stack lifecycle 结果已进入 EX-006/EX-005，并明确 state repair≠effect repair | 已收敛；只等待部署级 effect lineage / authority update / post-state reconciliation 对照 |
| P0 | 自我改进回路的独立变更审计 | **第一批已 clip+compile**：[[20260901-harnessevolve-reference-trajectories]]、[[20260809-hsi-hierarchical-self-improvement]]、[[20260528-harness-updating-not-harness-benefit]]、[[20260827-rethinking-harness-evolution-evaluation]]；已编译进 [[Recursive-Self-Improvement]]，稳定区分 change attribution、runtime activation/adherence、matched-search delta 与 feedback/control authority | 已收敛；除非出现跨版本生产回放、不可改写安全 gate 或 rollback 后复验，不再补同类 benchmark |
| P0 | Harness 行为契约与保留测试区 | Rethinking 的 matched-search/held-out 反例已 clip+compile；HELIX 仍提供 target tests 通过但 PASS_TO_PASS 回归的增量行为契约证据，但其价值只在补 regression-aware sibling labels，不再用于扩展一般 self-evolution 论证 | HELIX 仅在下一轮需要行为契约字段时定向 clip；优先级低于 production fleet canary/rollback 记录 |
| P1 | 生产 Agent fleet 的自修改纵向记录 | 缺 prompt/skill/router/evaluator 变更的 owner、版本、canary、回滚、隐藏 holdout 与质量/安全联合结果 | new-source → EX-007 |
| P0 | 劳动经济学企业—职业交叉校准 | **前两批共 10 个来源已 clip+compile**；第二批新增 [[20260630-ramp-ai-jobs-firm-spending-workforce]]、[[20260901-dallasfed-ai-automation-job-postings]]、[[20260428-census-youre-not-hired-ai-early-career]]，把 observed firm AI spending→workforce stock、occupation exposure→posting demand、industry-state exposure→administrative early-career hires 纳入同一 [[Labor-AI-Empirical-Calibration]] | 已收敛到共同连接键缺口；`Prompting Change` 截至 2026-09-19 作者主页仍标 Draft coming soon，暂不重复检索会议 slides；只等待正式稿/方法或共同 firm × occupation × person 数据 |
| P0 | 劳动经济学代表性与预期偏差 | **Atlanta Fed 已 clip+compile**：[[20260324-atlanta-fed-firm-data-on-ai]]；已明确 retrospective reported attribution ≠ administrative realized，expected ≠ outcome，并与 NY Fed/ADP/CPS 不同 estimand 分层 | 已进入 [[Labor-AI-Empirical-Calibration]]；后续只需要同窗行政招聘/离职校准或共同企业键，不再重复摄取预期调查 |
| P1 | OTel GenAI 正式规范与开放提案 | **已 clip+compile**：[[20260919-otel-genai-agent-observability-main]]、[[20260919-otel-genai-open-governance-proposals]]；current main 仍为 Development，已覆盖 agent/workflow/plan/tool/retrieval/memory 等结构，但 authorization/post-state/revoke/recovery 尚非 cited current normative semantics；可核实开放提案含 #291/#427/#447/#457，旧 #483 未核实 | 已进入 [[Agent-Observability]]；只在 normative 合并、conformance/coverage 实测或 deployment trace 出现时恢复 |
| P1 | Google DeepMind AI Control / live monitoring | **已 clip+compile**：[[20260618-google-deepmind-ai-control-live-monitoring]]、[[20260622-google-deepmind-ai-control-roadmap]]；已固化 coverage/recall/time-to-response 与 async/sync response 区分，一百万 task 是监控规模而非 recall 证据，R2 >99% 等为 roadmap target | 已进入 [[Agent-Observability]]；只等逐案阻断、coverage/recall 实测与 post-state 联合 trace |
| P1 | MCP 2026-07-28 无状态转折 | `SEP-2663` 的设计状态为 Final，但官方 Tasks 页面仍为 Draft，且官方 SDK conformance 显示扩展实现未齐；`taskId` 既是状态定位又是路由键，per-request auth 与不可猜测 ID 不能替代 effect receipt；缺生产级主体绑定、TTL/撤销/replay、故障转移和 post-state 对账 | clip+compile → MCP Entity；new-source → `EX-005/006` / `CR-004` |
| P0 | Anthropic 设计负责人一手公开文本 | **已 clip+compile**：[[20250724-anthropic-product-design-claude-code]]、[[20260301-jenny-wen-design-process-dead]]、[[20260820-joel-lewenstein-crafting-last-mile-delight]]；已补齐代码化原型、系统状态、流程压缩、quality allocation、agent-review attention bottleneck 与 decision accountability，并纠正“judgment=永久人类护城河”的过强表述 | 已编译进 [[AI-Era-Designer-Role]]；Anthropic 这一支收敛，后续只在责任/RACI、质量/返工或 incident 结果数据出现时恢复 |
| P0 | Google Gemini / DeepMind 当前设计团队材料 | **部分收敛**：[[20260919-google-gemini-visual-design]] 已提供 current Gemini design-team 对 thinking/listening/synthesis/progress 可见化、trust、error forgiveness 与 relational experience 的直接材料；但仍缺 code-first workflow、RACI、launch review、rollout metrics 与 incident ownership | 已编译进 [[AI-Era-Designer-Role]]；P0 保持开放，但只接受当前 Gemini/DeepMind 团队的组织运行/责任/结果证据，不再补 PAIR 方法指南 |
| P0 | Microsoft AI / Copilot 当前设计团队材料 | **已 clip+compile**：[[20260528-microsoft-copilot-new-design]]、[[20260831-microsoft-coreai-product-simplicity]]；已补齐 current Copilot/CoreAI design workflow、设计师直接进 production code、output quality 作为设计对象、coherence bottleneck 与 rollout telemetry（>50% load reduction、约10% p95 response improvement、跨 app usage lifts） | 已编译进 [[AI-Era-Designer-Role]]；Microsoft 这一支阶段性收敛，只在 RACI / launch / incident / quality-retention 数据出现时恢复 |
| P1 | 跨公司设计结果对照 | OpenAI / Anthropic / Microsoft / Google Gemini 已形成四家公司一手对照，但结果口径仍不统一：Microsoft 有 rollout telemetry，Anthropic 有内部速度自报与 review/attention bottleneck，Google 主要是 trust/legibility design-object 证据 | 下一步只接受 feedback latency、返工/事故、模型/产品改动链、RACI/owner 的同口径记录；不再扩普通设计访谈 |
| P1 | Agent 隐私对照 | **第一批生产对照已 clip+compile**：[[20260905-numezis-governed-business-agent-sme]]、[[20260614-decentralized-granular-access-control-agentic-ai]]、[[20260710-aws-ktern-agentcore-sap]]；已稳定区分 permission / actual read / model exposure / retention-deletion，EDPB Guidelines 02/2026 最终版仍未发布 | 已编译进 [[Agent-Data-Minimization]]；停止扩 least-privilege 架构案例，只等 actual-read/TTL/erasure 纵向证据 |
| P1 | 专业能力再生反例 | 缺高采纳且训练能力不降的纵向案例 | clip/compile → CR-005 |
| P2 | 全球南方 AI 生态 | 缺已长期运行且能报告本地制度/评价标准与部署结果的一手材料；现有 NITI Arezzo 仅为试点，BharatGen 尚未公共/机构部署 | new-source → CR-007 |

## 活跃赌注

- **评测逃逸披露级联**（登记 2026-08-02）：至 2026-08-30，若至少一家前沿实验室新披露评测环境逃逸或越权，系统性判断获得新证据；零披露不能单独证伪，只触发延长观察窗。
- **中层代谢触发器**：Entity:Topic 比连续两个观察窗口大于 5:1 时，优先执行 Topic 建设而非继续 Explore。

## 定理网络导航

- **G1 有穷性**：系统会遇到自身边界。
- **G2 现实作为评估者**：失败、事故和外部后果使边界发出信号。
- **G3 遗骸化**：实践被制度化后会留下规则，同时丢失部分现场判断。

本节只作检索导航，不是证据，也不替代各定理的推导语境。完整降秩与三项缺口预测见 [[2026-08-03]]。

## 最近思考结论摘要

| 时间 | Claim | Delta | 摘要 |
|---|---|---|---|
| 2026-09-07T08:33:43+08:00 | EX-005 耐久执行停止与外部效果 | refined | AWS Durable Execution 明确停止 durable execution 不会停止在途 Lambda，checkpoint 前的外部副作用仍生效；Step Functions 将跨服务取消定义为 best-effort。新增 checkpoint/in-flight 窗口作为 effect-lineage 分层，不新增 EX。 |
| 2026-09-07T07:46:00+08:00 | EX-002 证据覆盖与解释 follow-up | refined | AJ-Bench/Partial Evidence Bench 分开证据取得与完整性意识；Cited but Not Verified 显示深度增加可能损害事实整合；收窄为 evidence-synthesis interference，不新增 EX。 |
| 2026-09-07T06:36:45+08:00 | EX-005 效果结算 follow-up | no_delta | Recourse/BCCA 有本地 provider-compatible effect/recovery receipt，Stripe 有幂等、取消、退款和不确定结果语义；仍无同案 provider-authoritative post-state 与 independent reconciliation/review 闭链。 |
| 2026-09-07T06:33:25+08:00 | EX-004 三层 oracle 与成功来源 | refined | EnvTrustBench 分开 environment-state、outcome 与 trace oracle；EVMbench 提供 deterministic transaction replay/post-state verification，但 reference truth、environment truth、execution truth 仍无同轨交叉；不新增 EX。 |
| 2026-09-07T04:42:26+08:00 | EX-006 控制状态抵达执行边界 | refined | ControlCapsule/ConstraintRot 补强状态衰减与 replay/preflight 边界；SMSR 补强 HMAC 写入来源绑定；OAP/FORGE 补强执行前授权；MemSecBench/ACRFence 补强生命周期与重复副作用。仍无 carrier × enforcement 的生产级 post-state 交叉证据，不新增 EX。 |

## 思考日志索引

- 2026-09-07 — open explore follow-up：核对 AWS Durable Execution、Step Functions `.sync`、MCP Tasks 与 A2A cancellation 语义；确认停止编排、在途 invocation、checkpoint、下游取消和外部 post-state 不是同一状态，新增 checkpoint/in-flight 窗口作为 `EX-005` effect-lineage 分层，`refined`，不新增 EX（详细研究：[[20260907--ex005-durable-stop-semantics--research]])
- 2026-09-07 — open explore：复核 AJ-Bench、Partial Evidence Bench、Cited but Not Verified，并以 SourceBench/AgentOracle 作为相邻 provenance 对照；确认证据可见性、检查策略、完整性意识与事实整合是不同测量面，新增 `evidence-synthesis interference` 内部瓶颈；`EX-002` refined，不新增 EX（详细研究：[[20260907--ex002-evidence-coverage-followup--research]])
- 2026-09-07 — open explore：核对 EnvTrustBench、EVMbench 与 OpenAI coding evaluation audit；确认 reference truth、environment-state truth、execution/post-state truth 是不同 oracle 对象，EnvTrustBench 提供 outcome/trace oracle，EVMbench 提供 deterministic replay/post-state 近邻，但没有同一 trace 的三层交叉；收窄 `EX-004`，不新增 EX（详细研究：[[20260907--environment-oracle-provenance--research]])
- 2026-09-07 — open explore：复核 ControlCapsule、ConstraintRot、SMSR、MemSecBench，并补充 OAP、FORGE、ACRFence 一手边界；确认 carrier 完整性、authority/provenance binding、deterministic enforcement 与 effect/recovery 仍是 EX-006 内部交叉项，未找到相对 exact replay + preflight 的生产级 post-state 优势证据，`refined`，不新增 EX（详细研究：[[20260907--control-state-boundary--research]])
- 2026-09-07 — open explore follow-up：补查 W2S/AAR 官方说明与作者代码；确认远程独立计分、快照和 commit ID 仍不能自动闭合 reward-hacking、反馈查询历史、精确变更内容与 evaluator 版本的 provenance 链；沿用“变更归因 + feedback/control 双重不对称”，不新增 EX（详细研究：[[20260907--self-improvement-change-gates--research]])
- 2026-09-07 — open explore：核查 EX-003 的交接校准边界；确认 2112.06751 只提供固定接收面的消息呈现效果，Alibaba 只随机部署，Google/AWS 主要是 handoff 契约，尚无 packet×receiver×timing 的联合因果证据；保留 EX-003、收窄其操作链，不新增 EX（详细研究：[[20260907--handoff-calibration-evidence-boundary--research]])
- 2026-09-07 — open explore：用 `entry / mechanism / phase / action surface / observable-defense / source class` 复核 `Agent-Attack-Surface`；确认候选具备独立 Topic 的结构资格，但五个 Entity 不应平铺，FORGE 作为无指令证据污染边界成员，`Persona-Hyperstition` 暂缓；不新增 EX（详细研究：[[20260907--agent-attack-surface-topic-boundary--research]])
- 2026-09-07 — open explore：核对 Atomix、Cordon、Dapr、CAVA、Auditable Agents 与 Microsoft compensation；确认 gate、signed history、action receipt 和 dispatch/compensation 状态不能替代 provider-authoritative post-state 与 independent reconciliation；收窄 `EX-005`，不新增 EX（详细研究：[[20260907--agent-effect-settlement-post-state--research]])
- [[2026-09-06]] — open explore：交叉核对纽约联储、丹麦匹配研究、Anthropic/CPS、Stanford/ADP、Census、Dallas Fed 与 Ramp；确认 adoption carrier、企业选择、职业/早期流量、培训可得性和独立能力属于不同测量层，当前不能形成四层共同估计，收窄劳动线为 `adoption carrier × firm selection × labor-flow composition`，不新增 EX（详细研究：[[20260906--labor-economics-cross-layer--research]])
- [[2026-09-06]] — open explore：核对 ALE Robotics 官方 benchmark protocol；确认 hidden grader/seed、verify 阶段隔离、engine-native 分数重算和 validated/verified attestation 可分层，但它们不等于 reference truth、语义等价或 verifier independence；收窄 `EX-004`，不新增 EX
- [[2026-09-06]] — open explore：核对 AWS AgentOps、Bedrock AgentCore Observability 与 AWS DevOps Agent；确认四层 telemetry、trace context、Gateway policy 和 recommendation-only 执行边界已提供结构化观测入口，但无同案外部 effect receipt、revoke-after-send、canonical post-state 与独立 review；收窄 `CR-004/EX-005`，不新增 EX（详细研究：[[20260906--agentcore-cross-layer-effect-lineage--research]]）
- [[2026-09-06]] — open explore follow-up：核对 MCP 2026-07-28 GA、SEP-2663、Tasks extension 与官方 SDK conformance；确认 `taskId` 同时承担状态定位与路由，cancel 只是最终一致的协作式意图，且规范/实现状态存在版本差异；收窄 MCP 与 `EX-005` 的交界，不新增 EX
- [[2026-09-06]] — open explore：审计 `EX-001`–`EX-007` 的近期代谢状态；未发现正交的新缺口，确认当前主要瓶颈是既有 P0 evidence debt；不新增 EX-008，下一步优先 `clip+compile`
- [[2026-09-06]] — open explore：核对 Alibaba 随机现场实验与 Google/Microsoft handoff 一手文档；确认升级类型/时机/人类投入有现场效果证据，交接包、路由和接收面是不同操作变量，但缺固定接收面下的 packet ablation；将 `EX-003` 收窄为四段事件链，不新增 EX
- [[2026-09-06]] — open explore：核查 `trajectory-judge`、`BabelJudge` 与 ALE 的固定 trace、构造真值、隐藏 reference 和多 judge 边界；补强 evidence-view/判定可靠性，但未找到 `verifier independence × reference/provenance` 的同 trace 因果交叉，不新增 EX
- [[2026-09-06]] — open explore：补查 REDAgentBench、Partial Evidence Bench 与 CAFE；确认 evidence view/授权可见性可在固定 rollout 或 oracle 下独立测量，但尚无同时操纵 verifier independence、reference integrity/provenance 的同 trace factorial 证据；收窄 `EX-001/002/004`，不新增 EX
- [[2026-09-06]] — open explore：核查 Ghost in the Context、Governance Decay、Security-Recall Divergence，并新增 SMSR、MemSecBench；将 `EX-006` 从“是否必须 OOB control plane”收窄为“决策时状态完整性 + 独立动作边界 enforcement”，保留 authority authenticity / provenance binding 为待证子门，不新增 EX
- [[2026-09-06]] — open explore：结构审计安全/零信任标签 Entity 的 Topic 承载；确认未承载项分为攻击面/内容陷阱簇与控制/身份簇，前者形成 `Agent-Attack-Surface` promotion candidate，后者优先接入既有 `Agent-Security`，不新增 EX
- [[2026-09-06]] — open explore：补查 `agent-infra` benchmark contract、`agentprov` provenance attribution 与 `tracegym` replay harness；确认 reference trust/control 需要可信侧 owner、version/digest、hidden grader 与 allowlisted projection，provenance observability 需要 visible trace 与 held-out truth 分离、变换/泄漏检查和 coverage；三者没有提供 EX-001/002/004 同 trace factorial 效果证据，将 `EX-004` 收窄为两层，不新增 EX
- [[2026-09-06]] — open explore：核对 MCP 2026-07-28 正式规范、Tasks extension、C# SDK stateless 文档与 SEP-2549；确认去除的是协议层 session，状态被转移到显式 handle、Tasks store、MRTR request state、cache 和 per-request metadata，且 Tasks cancel 仍是协作式/最终一致；新增 handle/task 绑定、TTL、撤销、replay、故障转移与 effect lineage 的 Source 需求，不新增 EX
- [[2026-09-06]] — open explore：核对 HELIX、Evo-Harness 与 Anthropic Automated Researcher/Weak-to-Strong Researcher；确认 recipe/trace 只能解决 intervention identity，环境 feedback 的来源与粒度会改变演化结果，hidden holdout/独立 evaluator 仍不能替代不可改写 control plane 与安全复评；将 `EX-007` 收窄为“变更归因 + feedback/control 双重不对称”，不新增 EX
- [[2026-09-06]] — open explore：补查 MCP Tasks、A2A、Temporal、OAuth 与 AWS Step Functions 一手材料；确认凭据/任务失效、在途停止、提交状态不确定与效果对账/补偿具有不同对象和时序，新增 `commit-state uncertainty` 作为 `EX-005` 子门，不新增 EX
- [[2026-09-05]] — open explore：核对 Anthropic Product Design team、Claude Design、Google PAIR 与 Microsoft Research/Agent design foundations 一手材料；初步支持设计对象扩展到模型/系统行为、反馈/控制和可执行工作流，但当前材料不足以证明判断/责任已成为跨公司主要瓶颈，结果 `partial`，不新增 EX
- [[2026-09-05]] — open explore：核对 ACRFence、HBHC、Google IAM propagation、Microsoft Entra emergency revocation、GitHub May availability report 与 AWS Agentic AI/DevOps containment；确认权限停止、在途连接停止和已提交外部效果收敛具有不同时间/对象语义，收窄 `EX-005` 为三层恢复门，不新增 EX
- [[2026-09-05]] — open explore：核对 Ramp、Dallas Fed、Federal Reserve、Atlanta Fed 与 Census 一手劳动数据；确认企业净 headcount 增长、职业岗位/早期职业招聘收缩和管理者未来预期处于不同测量层，收窄劳动经济学校准问题为“企业扩张 × 职业构成 × 入门流量 × 再生代理”的交叉矩阵，不新增 EX
- [[2026-09-05]] — open explore：核对 AgentJudgeBench、AcquaBench、ABC、GeneBench、OpenAI coding audits、τ³-bench 与 ELT-Bench-Verified；确认 reference integrity 与 success provenance 有分别操纵/审计证据，但缺 verifier independence × evidence visibility × external oracle 的同 trace 交叉设计，收窄 `EX-004`，不新增 EX
- [[2026-09-05]] — open explore：核对 OTel 主分支与开放 PR #483/#447；确认 #483 只表达 runtime-owned state delta、#447 只补部分 tool/API transfer，二者均不闭合 business post-state、授权实际放行、handoff owner/ack 或 revoke/recovery，收窄 `CR-004`，不新增 EX
- [[2026-09-05]] — open explore：核读 OTel GenAI agent/framework、GenAI spans 与 Trace API，并核对 guardrail PR #427；确认标准 trace 可枚举结构与局部 lineage，但不携带授权、实际副作用、恢复或交接语义，收窄 `CR-004`，不新增 EX
- [[2026-09-05]] — open explore：核读 Ghost in the Context、Governance Decay、Hidden in Memory 与 Security-Recall Divergence；确认治理状态存在装配、压缩、跨会话和抑制性约束衰减，但四篇都没有证明 OOB control plane 普遍必要；将 `EX-006` 收窄为决策时状态完整性门 + 独立动作边界 enforcement，不新增 EX
- [[2026-09-05]] — open explore：核对 Microsoft Azure SRE Agent 审计/指标文档、Google SRE Gemini CLI 案例、AWS Agentic Incident Response PoC 与 Druva production case；确认权限、审批、执行、验证和审计存在跨厂商结构重复，但缺 verdict/authorization/revoke/rollback/recovery 与 action-surface 分母，收窄 `EX-005`，不新增 EX
- [[2026-09-05]] — open explore：将 `EX-007` 从抽象独立闸门收窄为“变更对象→失败信号→晋级门”映射；行为组件需行为契约/线上复评，评估与目标组件需冻结外部 oracle，策略与执行组件需独立安全门；不与 `EX-004/006` 合并，不新增 EX
- [[2026-09-05]] — open explore：核对 [OpenAI/HF 事件技术报告](https://openai.com/index/hugging-face-incident-and-the-road-ahead/)、HF 技术时间线与 HBHC/CommitGuard/ContainmentBench；发现事故级授权/遏制/重建/再次暴露/停机链条，但无统一 verdict→actuation、撤销/回滚/MTTR 分母，收窄 `EX-005`，不新增 EX
- [[2026-09-05]] — open explore：核对 MCP 2026-07-28 规范/公告与 NSA 安全指导；确认移除的是传输层 protocol session，应用状态转为显式 handle、MRTR 与每请求元数据，收窄为“状态迁移、非状态消失”，不新增 EX
- [[2026-09-05]] — open explore：核读 SkillTV-Bench 论文与公开仓库；确认环境可访问、task-time skill、inspection plan/log 和 source-verifier gate 是不同变量，但其结果仍是 benchmark 内部闭环，细化 `EX-002/007`，不新增 EX
- [[2026-09-05]] — open explore：核对 arXiv 2604.07650、AJ-Bench、AgentJudgeBench 与 AcquaBench 的实验对象和控制变量；确认输出错误相关性、环境证据取得/解释、reference integrity 与 success provenance 是耦合但不可替代的三门，`EX-001/002/004` refined，不新增 EX
- [[2026-09-05]] — recompile CR-004：Google DeepMind AI Control 定义 coverage/recall/time-to-response 并披露百万任务监控原型，但无逐案阻断或完整污染覆盖实测；将“指标化控制面可观测性”与“行为覆盖闭包”分开，refined
- [[2026-09-05]] — open explore：将现有 Agent 安全 Entity/Source 映射为“检测→判定→授权→执行→撤销/恢复”五阶段 Topic 骨架；确认结构边界成立但 owner、action-surface、撤销/恢复仍缺实证，不新增 EX
- [[2026-09-05]] — open explore：Google Cloud CCAI escalation telemetry 与 Google SecOps 架构把接收队列、转接失败、结构化汇总和迭代上限加入 handoff 分析；将 `EX-003` 收窄为“交接包 × 接收面”两层，不新增 EX
- [[2026-09-05]] — recompile CR-003：复核 arXiv 2607.10139v3；shared-error floor 仍是任务错误结构与 consensus panel 条件量，不能外推至所有 AI 监督形态，no_delta
- [[2026-09-05]] — recompile CR-002：再次核查 Numezis 匿名 SME 案例；页面仍无读取量、上下文保留期、删除/TTL 或更长纵向数据，反例仍只改变“架构必然性”而未补足长期数据最小化，no_delta
- [[2026-09-05]] — open explore：Google SRE AI Operator 与 AWS Agentic AI Lens 把 handoff 明确为结构化上下文契约，并提出完整性、延迟和协作成功率指标；将 `EX-003` 收窄为“路由选择”与“交接包可接住性”两层，不新增 EX
- [[2026-09-05]] — recompile CR-001：官方执行框架与 AI Office 页面继续确认可执行/可处罚能力；二手追踪报告 €47M 叙事已被原作者撤回，未取得官方决定，实例证据收窄为未证实，refined
- [[2026-09-05]] — open explore：完成 Agent Safety “检测→判定→授权→执行→撤销/恢复”五阶段字段映射；确认结构边界成立，但 owner、action-surface coverage、撤销权和 recovery SLA 未闭合，不新增 EX
- [[2026-09-05]] — recompile CR-004：核读 Google DeepMind AI Control 博客与 Roadmap；将 coverage/recall/time-to-response 的架构指标与 R2 目标同实测区分，确认逐案阻断与完整污染覆盖仍无实证，refined
- [[2026-09-05]] — open explore：安全 Entity/Source 簇缺少独立 Topic；核对 `Agent-Containment`、`Least-Agency`、`Distinct-Principal-Identity`、`Policy-as-Code`、`Agent-Observability` 与现有安全 source summary，收窄为“检测→判定→授权→执行→撤销/恢复”五阶段骨架，不新增 EX
- [[2026-09-05]] — open explore：AgentJudgeBench 的 C3（仅单 generator/双 judge）与 scout 边界核对，结合 AcquaBench 的 CLEAN/GOLD/SHAM、D2 将 `EX-004` 收窄为静态 oracle integrity + 动态 success provenance 两个子门，暂不新增候选
- [[2026-09-05]] — open explore：FORGE/OAP/Janus 定向核验；把 `EX-005` 收窄为确定性 pre-action enforcement 的独立性获得初步支持，撤销/回滚与人审最优性继续开放
- [[2026-09-05]] — recompile CR-003：`ljg-think-recompile` 复核既有跨模型 consensus/verifier 证据；没有超出已知任务与 panel 条件边界的新证据，no_delta
- [[2026-09-05]] — open explore：GitHub prompt 压缩案例显示离线门漏掉并行行为回归；结合 Anthropic 的 harness 演化与 Uber 的固定模型归因，将 `EX-007` 收窄为行为契约门 + 独立归因/安全门
- [[2026-08-31]] — open explore：把 self-improving agent 的评估器、harness、技能和策略共变拆成变更治理问题；新增 `EX-007`，要求独立外部 oracle、冻结控制面、版本回放与回滚证据
- [[2026-08-31]] — open explore：把高影响动作前的治理状态承载拆成 policy-carriage / control-plane integrity 候选；记忆写入、上下文压缩和决策时装配可能删除、弱化或错绑规则，新增 `EX-006`
- [[2026-08-31]] — open explore：把检测/判定之后的动作授权、独立执行点与撤销/恢复时限拆成 Agent 安全的新候选层；与 CR-004 的可观测性、EX-003 的升级路由和 EX-004 的 oracle/source-lineage gate 分界，新增 `EX-005`
- [[2026-08-31]] — open explore follow-up：Agentic Benchmark Checklist、GeneBench、AcquaBench、tau3 与 OpenAI 新审计把 EX-004 从泛 reference integrity 收窄为 oracle/source-lineage gate，新增目标可辨识、来源污染和 expected action 回链字段
- [[2026-08-31]] — open explore：把 reference integrity 从模型独立性与证据覆盖中拆出；AgentJudgeBench 的 GT/无 GT/corrupted-GT 对照与 OpenAI/ELT-Bench benchmark audit 指向真值来源、语义、版本和呈现方式的独立缺口，新增 `EX-004`
- [[2026-08-31]] — open explore：把 Twilight Factory 的 facilitator agent 还原为选择性委派/二阶校准问题；人类隐藏信息、误校准与消息 framing 形成新监督盲区，新增 `EX-003`
- [[2026-08-31]] — open explore：把验证器独立性与证据覆盖/解释能力拆开；AJ-Bench 提供信息取得、状态验证、过程验证及四类失败的待剪藏一手基准，新增 `EX-002`
- [[2026-08-30]] — recompile CR-004（think 将“结构层可枚举”限定为已声明且被记录的接口/事件目录；运行时可达路径需经权限、隔离和日志闭包覆盖，行为受响应时限约束、意图仍非直接观测，refined）
- [[2026-08-30]] — recompile CR-003（arXiv 2607.10139v3 提供跨家族 verifier panel、任务域与逐域 shared-error floor；数学接近 0、GPQA 0.030、MMLU-Pro 0.143，换 generator 后复现；将 Claim 收窄为任务与 verifier 条件下的边界命题，refined）
- [[2026-08-30]] — recompile CR-002（复核 Numezis 同一匿名瑞士 SME 案例：6 个月部署、逐客户/法人隔离、模型无保留；未提供读取量或 TTL，长期数据最小化缺口不变，no_delta）
- [[2026-08-30]] — recompile CR-004（Google DeepMind AI Control blog 与 v0.1 Roadmap 定义 coverage/recall/time-to-response 与同步阻断指标及目标，但未给逐案实测；observability 边界进一步细化，refined）
- [[2026-08-30]] — recompile CR-003（跨模型共识 verifier 研究报告任务域相关的共享错误下界，换生成模型家族后复现；数学近零、科学非零，strengthened）
- [[2026-08-30]] — recompile CR-006（定向检索未找到独立部署级“加固后逃逸归零/同一失配仅一次”反例；受控实验与部署模拟均不足，blocked）
- [[2026-08-30]] — recompile CR-004（Google DeepMind AI Control 把边界具体化为低风险异步观察/高风险同步阻断；coverage、recall、响应时间与可见 CoT 限制支持“架构指标不等于仪器化闭包实证”，refined）
- [[2026-08-30]] — recompile CR-002（Numezis 匿名瑞士 SME 生产案例：按客户/法人隔离读取、逐工具权限、模型无保留/不训练；反例使 Claim weakened，但长期性与可推广性仍待检验）
- [[2026-08-30]] — recompile CR-007（NITI Arezzo 为本地适配的短期可行性试点，BharatGen 尚未公共/机构部署；未发现长期低错配一手反例，blocked）
- [[2026-08-30]] — recompile CR-002/003/004/006：least-privilege 反例削弱架构必然性但读取/保留仍缺量化；Apple 跨族 judge 仍有相关错误；OpenAI/Anthropic 评测越界补强跨厂商边界；observability 继续区分结构指标与事前阻断，均保留原有边界。
- [[2026-08-29]] — recompile CR-003/004/005/006/001/002：跨族行为纠缠、隐式评测门失效、专业再生反例不足、跨厂商越界与 AI Act 罚款叙事溯源等结论完成收窄；CR-005 停止主动重查，CR-006 自 blocked 恢复。
- [[2026-08-29]] — recompile CR-003（22:00：复核同一 arXiv 来源，未新增独立证据，no_delta）
- [[2026-08-29]] — open explore：验证器独立性四轴候选（目标/证据/执行/时间），形成最弱轴判据、证伪方向与最小四条件实验设计；新增 `EX-001` 与 P0 Source 需求
- [[2026-08-27]] — recompile CR-005；Shopify/River 部署级反例收窄专业再生外部化预测
- [[2026-08-25]] — recompile CR-001；官方执行框架已生效，但实际罚单/执法决定仍缺
- [[2026-08-24]] — 15 个 legacy 区块完成 v2 迁移与状态归一化；recompile CR-002、CR-003。[[2026-08-23]] / [[2026-08-04]] / [[2026-08-03]] — 深度思考、Alpha Transfer、生成器降秩与边界复核；[[inventory-20260802]]、[[2026-07-23]] / [[2026-07-22]]、[[resolved-judgments]] / [[resolved-principles]] — 盘点、验证瓶颈与已收敛判断索引；更早 legacy 日志可从 Git commit `953e259` 恢复
