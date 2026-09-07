---
type: research-agenda
title: "Agentic Work Atlas 研究议程"
created: 2026-05-22
updated: 2026-09-07T08:33:43+08:00
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
- Status: ready
- Priority: P0
- Claim: AI 评测治理已从自愿最佳实践进入可执行、可处罚的制度阶段。
- Gap: Evidence
- Evidence: `raw/2026-eu-ai-act-compliance-autonomous-agents.md`；官方执法启动新闻稿 [IP/26/1714](https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1714)（2026-07-31）与生效日新闻页（均无 €47M 三案记录）；AI Omnibus 将高风险义务推迟至 2027-12/2028-08；€47M 三案经溯源性定向为单链互引的二手内容站叙事，且 [AI in Europe 追踪](https://aiineurope.co/policy/europe-act-tracker-2026-08-31) 报告原作者已撤回该说法（均不能替代官方决定，详见 2026-09-05 日志）
- Evidence goal: 官方 AI Office/委员会处罚决定文本发布（确认或证伪 €47M 实例），或独立一手披露出现；€47M 三案现为 falsified 候选，制度能力面已一手确认
- Basis: evidence
- Last checked: 2026-09-05T05:00:35 · refined
- Next: 收敛为触发式复查，不再主动检索——€47M 三案保持未证实；等待 (a) AI Office 官方处罚决定文本，或 (b) 独立一手披露；时间观察锚点：AI Omnibus 新增禁止实践条（2026-12 生效）后第一次可验证执法 action
- Retry: new-source:eu-ai-act-official-penalty-decision

### CR-002 · Agent 数据过度收集具有系统性
- Status: ready
- Priority: P1
- Claim: Agent 的数据过度收集来自任务代理架构，而不是单一产品或单一厂商的实现失误。
- Gap: Counterexample
- Evidence: `raw/20260618-mosaicleaks-privacy-agent.md`、`raw/How we contain Claude across products.md`、`raw/20260518-zero-trust-for-ai-agents.md`、`raw/20260616-why-is-meta-destroying-its-engineering.md`、`raw/20260714-context-collapse-2-when-emails-instruct.md`；[Microsoft 官方 least-privilege 模式](https://learn.microsoft.com/en-us/security/zero-trust/sfi/least-privilege-for-ai-agents)；
  [arXiv 2607.22611](https://arxiv.org/abs/2607.22611)（生产 8 个月的细粒度权限架构，自报只读 AI agent 与零未授权写入）；[AWS/KTern.AI 生产案例](https://aws.amazon.com/blogs/machine-learning/how-ktern-ai-built-agentic-ai-for-sap-on-amazon-bedrock-agentcore/)（20+ 生产 agents、per-agent least privilege；均待 clip/compile）
- Evidence goal: 复核部署级 least-privilege 案例是否包含长期数据最小化（读取范围/保留期）以决定是否进一步 weakened；若仅有权限/写入控制则收窄为默认风险，或等待跨厂商重复失效（→strengthened）；EDPB 02/2026 最终版或新反例披露可恢复检索。
- Last checked: 2026-09-05T06:00:32 · no_delta
- Next: clip+compile Numezis 案例，固化已披露的隔离/保留字段；若仍无读取量或 TTL，收窄为默认过度权限风险；不再重复检索同一页面
- Retry: new-source:numezis-agent-privacy-case-clipped

### CR-003 · AI 监督 AI 存在共模误差下界
- Status: ready
- Priority: P0
- Claim: 即使使用不同模型家族，AI 监督 AI 仍存在不可消除的共模误差下界。
- Gap: Boundary
- Evidence: `raw/20260713-agentic-misalignment-summer-2026.md`、`raw/20260330-reward-hacking-equilibrium-finite-evaluation.md`；[arXiv 2604.07650](https://arxiv.org/abs/2604.07650)（已核读，尚未 clip）；[Apple：Nine Judges, Two Effective Votes](https://machinelearning.apple.com/research/correlated-llm-evaluation-panels)（2026-06，一手研究）；[arXiv 2607.10139](https://arxiv.org/abs/2607.10139)（v3，2026-08-17，一手研究；跨家族 verifier panel 在 GPQA/MMLU-Pro 的 shared-error floor 分别为 0.030/0.143，数学任务接近 0）
- Evidence goal: 界定跨模型 consensus verifier 的 shared-error floor 是否依赖任务域、错误结构与 panel 组成，并区分该结果与所有 AI 监督形态之间的外推边界。
- Last checked: 2026-09-05T07:00:28 · no_delta
- Next: clip+compile arXiv 2607.10139 进入 raw/source，保留 v3 的任务域、model panel 与 shared-error 字段，供后续可回溯复核
- Retry: new-source:arxiv-2607.10139

### CR-004 · Agent Observability 上界随层级变化
- Status: ready
- Priority: P1
- Claim: Agent observability 的结构层可枚举、行为层只能竞速、意图层不应被当作可直接观测对象。
- Gap: Boundary
- Evidence: `raw/20260608-connector-observability-directory.md`、`raw/20260819-google-ai-evals-inspect-skill.md`；Anthropic 三案、OpenAI HF/第三方评测 URL；[Google DeepMind AI Control](https://deepmind.google/blog/securing-the-future-of-ai-agents/) 与 [Roadmap PDF](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/securing-the-future-of-ai-agents/gdm-ai-control-roadmap.pdf)（均待 clip）。
  [OTel GenAI agent/framework 规范](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md) 与 [Trace API](https://opentelemetry.io/docs/specs/otel/trace/api/)（待 clip）；开放设计材料 [PR #483](https://github.com/open-telemetry/semantic-conventions-genai/pull/483) 与 [PR #447](https://github.com/open-telemetry/semantic-conventions-genai/pull/447)（非现行规范）
- Evidence goal: 取得逐案事前阻断或 coverage/recall 数据，区分“仪器化闭包”的架构承诺与真实污染向量覆盖的实证，并核对标准 trace 是否足以重建 action-surface 与责任链。
- Last checked: 2026-09-05T19:32:09 · refined
- Next: clip+compile OTel current main 与 PR #483/#447；按“状态 delta → 工具/转移 → 实际 post-state → handoff/recovery”逐格核查现行字段、提案字段与仍需自定义安全事件的边界
- Retry: new-source:google-deepmind-ai-control

### CR-005 · AI 采纳侵蚀专业能力再生
- Status: ready
- Priority: P0
- Claim: 组织从 AI 获得局部效率收益的同时，会把专业能力再生成本外部化到整个职业共同体。
- Gap: Counterexample
- Evidence: `raw/20260731-tragedy-cognitive-commons-ai-expertise.pdf`、`raw/20260730-lenny-tech-workers-ai-sentiment-noam-segal.md`、`raw/Learning on the Shop floor.md`
- Evidence goal: 找到第二个"高采纳 + 维持学徒/独立验证"的组织或职业，或验证 Shopify 案例长期性（08-29 两轮定向检索已确认暂无部署级第二反例）
- Last checked: 2026-08-29T12:00:37 · no_delta
- Next: 停止主动重查；等待外部触发——第二"高采纳+再生内部化"组织/职业案例披露，或 Shopify/Lehrwerkstatt 纵向（专家补充率长期不降）数据
- Retry: new-source:apprenticeship-counterexample-disclosures

### CR-006 · 评测逃逸是系统性机制而非孤立 harness 事故
- Status: blocked
- Priority: P0
- Claim: 评测环境逃逸率由 harness 缺口、环境漂移与模型能力共同决定，而非少数配置事故。
- Gap: Counterexample
- Evidence: `raw/20260713-agentic-misalignment-summer-2026.md`；[Anthropic BrowseComp eval-awareness](https://www.anthropic.com/engineering/eval-awareness-browsecomp)（2026-03 一手）、[mythos-preview](https://red.anthropic.com/2026/mythos-preview/)（2026-04 一手）、[Opus 4.5 System Card](https://assets.anthropic.com/m/64823ba7485345a7/Claude-Opus-4-5-System-Card.pdf)（在线找答案去污染）；[OpenAI HF 事件](https://openai.com/index/hugging-face-model-evaluation-security-incident/)；[OpenAI 第三方评测](https://openai.com/index/third-party-cyber-evaluations-involving-openai-models/)
- Evidence goal: 跨厂商评测逃逸新披露（→strengthened 系统性），或"大规模加固后逃逸归零 / 同一失配仅发生一次"的部署级反例（→weakened）
- Last checked: 2026-08-30T09:56:29 · blocked
- Next: 等待新的独立部署级纵向材料，取得后核查加固后的逃逸率与失配复发情况
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

## 当前研究焦点

| 优先级 | 焦点 | 下一步最小动作 |
|---|---|---|
| P0 | Agent 安全 Topic 建设 | 五阶段骨架已起草；AWS AgentCore 新增四层 telemetry、trace context、Gateway policy 与 application telemetry 的正向架构边界；下一步仍需以事件级标识对齐 `flag → verdict → authorization → actuation → revoke/recovery → canonical post-state → review`，不把结构地图当作安全效果证据；不由 recompile 执行 |
| P0 | 验证器危机研究线 | 按独立性四轴、证据覆盖/解释能力与 reference integrity 建立矩阵，再 clip AgentJudgeBench、Anthropic 三案与 Astra 官方材料 |
| P0 | 劳动经济学实证 | 先按“企业净 headcount × 职业/入门流量 × 再生代理”建立校准骨架；新增 adoption carrier 分层：formal/function/worker-task/operational；补共同企业—个人—职业—时期键、培训完成与独立能力；不要用企业扩张直接抵消入门招聘收缩 |
| P1 | MCP 无状态转折 | `SEP-2663` 已标 Final，但 Tasks 渲染规范仍为 Draft、官方 SDK 支持不齐；`taskId` 同时是 durable state locator 与 HTTP 路由键，cancel 只是最终一致的协作式意图，不证明停止或回滚；下一步核对主体绑定、TTL/撤销、replay/failover 与 effect lineage |
| P1 | AI 时代设计方法论对照 | 初步支持设计对象扩展到模型/系统行为、反馈/控制和可执行工作流；Anthropic 有团队案例，Google/Microsoft 目前只有方法指南；下一步补当前负责人/团队材料与责任、返工、反馈时延字段 |
| P2 | Topic 与复核队列代谢 | 优先审查安全威胁面 Entity 簇的 Topic 承载；区分攻击面整合与 Agent-Security 的控制/责任生命周期，不继续制造新定理 |

## 开放探索候选

| ID | 候选问题 | 当前判断 | 证伪方向 | 下一步 |
|---|---|---|---|---|
| EX-001 | 验证器独立性是否是目标、证据、执行、时间四轴的最弱轴瓶颈？ | `2604.07650` 仅在输出错误、任务难度和模型/验证器组合上测相关性；REDAgentBench 固定 judge backbone，只改变证据视图/证明契约，不能替代独立性操纵；refined | 固定证据访问、reference 与任务后，跨家族/独立实现的单轴变化仍不能降低共同漏报，或独立性效应完全由证据覆盖/判定质量解释 | clip+compile `2604.07650` 与 REDAgentBench，按“错误生成相关性 × 证据状态 × reference 条件”补交叉字段 |
| EX-002 | 独立性之外，证据覆盖与证据解释是否构成验证的第二个必要门？ | AJ-Bench 将取得信息、状态验证、过程验证分开测量；Partial Evidence Bench 将授权视图、完整性意识和 gap report 分开；REDAgentBench 在同一 rollout 上改变轨迹/状态/混合视图；`Cited but Not Verified` 补出检索深度增加而事实整合下降的边界；仍未与 verifier independence、reference 条件同轨交叉；refined | 固定模型/验证器、任务、reference、外部 oracle、token/time 预算后，静态低覆盖、可交互读取和显式检查策略对照不改变漏报；或去重/held-out/独立事实 oracle 后深度效应消失 | clip+compile AJ-Bench、SkillTV-Bench、Partial Evidence Bench、REDAgentBench 与 `Cited but Not Verified`，建立“物理可见性 × 检查策略 × 证据解释 × 同族/跨族 × reference 条件”矩阵，并保留 evidence-synthesis interference 子门 |
| EX-003 | Facilitator agent 能否在缺少人类隐藏信息的条件下校准“何时升级、升级给谁、给什么上下文”，而不制造新的监督盲区？ | 2112.06751 在固定接收面下显示消息呈现有随机效果；Alibaba 随机的是部署条件，升级时机/类型主要是机制比较；Google/AWS 分开描述 route、handoff packet、receiver 与 telemetry，但没有 packet×receiver×timing 的因果消融；refined | 固定 trigger、Agent 输出、receiver 与 queue state 后，packet/message/timing 的交互若无稳定差异则并回 EX-002；若 packet 或 timing 仍改变正确率、延迟、补问或过度依赖，保留子门 | clip+compile 现有 P0 材料；优先寻找固定接收面下的 packet ablation 或含 `trigger/type → route/receiver → packet/version → human action → outcome` 的生产 trace |
| EX-004 | reference integrity 与 success provenance 是否构成独立必要门？ | AgentJudgeBench/AcquaBench 缺同 trace 交叉；EnvTrustBench 补 environment-state truth 与 outcome/trace oracle，EVMbench 补 deterministic transaction replay 与 post-state verification；三类 oracle 仍未同轨交叉；refined | 固定 verifier、trace 与 external post-state 后，若 reference/provenance 仍改变误放行/误拒绝、归因或排名，保留三层；否则并回 benchmark validity，并区分 reference truth、environment truth 与 execution truth | clip+compile EnvTrustBench、EVMbench；寻找同时含 reference version、state hash、visible/held-out trace、execution receipt/post-state 与跨 verifier 的联合 benchmark |
| EX-005 | 动作授权、独立执行点与撤销/恢复是否是独立必要门？ | ACRFence/HBHC 区分 checkpoint、未来调用阻断与副作用；MCP/A2A/Temporal/OAuth/Step Functions 区分凭据失效、在途停止、未知提交和补偿；Atomix/Cordon 补强 gate/outbox，但 receipt 仍不等于 provider post-state；refined | 固定 trace/verdict/schema，对照 prompt-only、model guard、reference monitor、monitor+rollback；若取消、停止与 post-state 等价则收窄，否则保留 commit-state uncertainty/effect-lineage 并测 post-state reconciliation | clip+compile ACRFence、HBHC、Atomix、Cordon、Dapr、CAVA、Auditable Agents 与 Microsoft compensation；优先找同案关联键、provider receipt、权威 post-state、补偿结果和独立复核 |
| EX-006 | 高影响/不可逆动作是否必须以带来源、稳定绑定、预算隔离且失败关闭的控制状态抵达执行边界？ | ControlCapsule 支持 preflight/fail-closed 的状态层结果；Constraint Pinning 会被 operator-impersonation 穿透；SMSR 区分 unsigned 与 authenticated injection，MemSecBench 提供 Write→Execute→Forget；仍未证 OOB control plane 普遍必要；refined | 若 exact replay+preflight 与 signed OOB carrier 在 compaction、memory、authority update、failover、recovery 上等效，OOB 只是实现选项；否则保留 authority authenticity/provenance binding 子门 | clip+compile 相关研究、SMSR、MemSecBench；建立 `carrier → issuer → binding → survival → verdict → preflight → actuation → post-state → recovery` 矩阵，做载体×enforcement 对照 |
| EX-007 | 自我改进 Agent 的变更晋级是否需要按变更对象分层的不可自证门，防止 harness、评估器、目标与策略共变把“分数提升”伪装成能力/安全提升？ | HELIX/Evo-Harness/AAR 及新增 HarnessEvolve、HSI 支持把行为面、反馈/评估面、策略/控制面分层；Rethinking 的 matched search 与 held-out 反例显示性能门不能单独证明可复用能力。边界进一步收窄为“变更归因 + feedback/control 双重不对称”；refined | 若固定模型/任务后，行为契约能捕获所有行为组件线上残差；若评估/目标共变仍能在冻结外部 oracle、hidden holdout、不可改写的 feedback provenance 和独立安全复评上稳定复现；或所有残差最终可由 `EX-004/006` 解释，则削弱或合并 `EX-007` | clip+compile HarnessEvolve、HSI、Harness Updating Is Not Harness Benefit 与 Rethinking；继续寻找 offline→online、独立复评、policy 冻结、canary/rollback；暂不抽象第四类 gate |

## Source 需求队列

| 优先级 | 目标 | 当前缺口 | 触发行动 |
|---|---|---|---|
| P0 | Agent Safety Topic 跨层核验 | 五阶段骨架与一条事故级响应链已找到；下一步以事件级标识对齐 `flag → verdict → authorization → actuation → revoke/recovery → canonical post-state → review`，并把 `authority stop / in-flight stop / effect reconciliation` 分开核验 `owner / action-surface`，不把结构地图当作安全效果证据；不由 recompile 执行 |
| P1 | AgentCore 跨层效果回执 | AWS AgentOps/AgentCore 一手材料把 framework、service、infrastructure、application telemetry、W3C trace context、Gateway policy、版本化 Runtime 与 CloudTrail 放入同一架构，但没有同案导出连接 `policy_version → action receipt → revoke-after-send → canonical post-state → independent review` | clip+compile → CR-004 / EX-005；优先寻找跨控制面、工具面和目标系统 audit log 的脱敏生产 trace |
| P2 | Agent 威胁面 Topic 承载候选 | 最小结构实验确认候选具备 Topic 资格，但五个 Entity 不应平铺：`Agent-Traps` 是 taxonomy anchor，`Agent-Perception-Gap` 是入口，`Context-Collapse` 是信任/状态中介，`Prompt-Injection-Risk` 是 umbrella/bridge，`AI-Worm` 是传播形态；FORGE 可作为无指令证据污染边界成员，`Persona-Hyperstition` 暂缓 | clip+compile `Agent-Traps` 与 FORGE；补跨作者/跨产品的内容→状态/行动案例，再由 compile/audit 验收；先不创建稳定页 |
| P0 | EU AI Act 首轮罚款官方决定 | €47M 三案系单链互引二手叙事（法律基础矛盾、无官方决定原文），需官方决定/一手披露判定真伪 | clip → 核对 CR-001 |
| P0 | Anthropic 三起评测事故 | 已联网核读一手来源（browsecomp/mythos/system card），未进入 raw/source | clip+compile → CR-006 |
| P0 | OpenAI 评测越界披露 | HF 事件及 UK AISI/Irregular 两起第三方评测尚未进入 raw/source | clip+compile → CR-006 |
| P0 | 评测逃逸加固后反例 | 缺独立部署级“加固后逃逸归零”或“同一失配仅发生一次”的记录；受控 SandboxBench 不足 | new-source → CR-006 |
| P0 | arXiv 2604.07650 行为纠缠框架 | 已定位但未 clip/compile | clip → compile → CR-003 / LLM-as-a-Judge 激励共压 flag |
| P0 | Apple《Nine Judges, Two Effective Votes》 | 已联网核读一手页面，未进入 raw/source | clip+compile → CR-003 |
| P0 | arXiv 2607.10139《LLMs as a Jury》 | 已联网核读一手预印本，未进入 raw/source；报告跨模型 verifier 的共享错误下界 | clip+compile → CR-003 |
| P0 | 验证器独立性四轴对照 | `2604.07650` 与 `trajectory-judge` 已提供相关性/固定 trace 多 judge 入口，但仍未操纵证据访问、reference 有效性或行动执行；`BabelJudge` 仅有单 judge 结果，不能替代独立实现对照 | clip+compile → EX-001/002；寻找同任务、固定证据与 reference 的跨家族/独立实现对照 |
| P0 | AJ-Bench 环境感知验证基准 | 已核读一手预印本，报告 155 个任务、516 条轨迹、工具交互、四类失败及 FPR/FNR；其 LLM/模型多数投票与人工/脚本混合标注，以及搜索域外部环境，需单独记录 reference provenance 与 access confound | clip+compile → EX-002；提取信息取得、状态/过程验证、证据误读、正确证据错误推理和环境重放字段 |
| P0 | SkillTV-Bench 证据驱动轨迹验证 | 一手论文与公开仓库提供 681 条可运行案例、task-time skills、可检查 artifacts、隐藏 source-verifier 和 disjoint evolution split；缺 JudgeSkill 各阶段的 inspection coverage、独立外部裁决、reference 条件与模型家族交叉对照 | clip+compile → EX-002/007；先核对数据 provenance、固定 36-case gate、false-accept 变化与环境访问/检查策略的可分性 |
| P1 | Cited but Not Verified 来源归因深度消融 | 一手论文将 Link Works、Relevant Content、Fact Check 分开；2→150 次 tool calls 时事实核查下降而链接/相关性保持，补强 evidence-synthesis interference；但不是环境状态 oracle 或固定 trace 的 verifier factorial | clip+compile → EX-002；保留深度分层、人工校准、模型差异与 held-out/独立事实 oracle 边界，不外推为普遍安全效果 |
| P0 | Human-AI Teaming Through the Lens of Calibration | arXiv 2606.10906 已核读但未进入 raw/source；需提取 rejector 定理、人类隐藏特征与不可约 excess risk 条件 | clip+compile → EX-003 |
| P0 | 选择性预测的校准失效 | PMLR 333（2026）多模态 ICU 研究显示聚合指标会遮蔽按类别误校准；需提取 per-class calibration、deferral 与 expert load 结果及任务边界 | clip+compile → EX-003 |
| P1 | 人类-路由消息效应 | arXiv 2112.06751 显示 deferral status 与 model prediction 的组合会改变人类准确性；需核对 messaging、human-in-loop 指标与外推边界 | clip+compile → EX-003 |
| P0 | 主动升级的部署级长程案例与交接契约 | Google SRE AI Operator 报告结构化上下文目录、完整调查历史交接、数千起 incident 与 human Golden Data；AWS Agentic AI Lens 明确要求交接延迟、上下文完整性和协作成功率；Alibaba 现场实验补足升级类型/时机/人类投入效果，但三者都缺固定接收面下的交接包消融 | clip+compile → EX-003；优先入库 Alibaba 现场实验、Google SRE AI Operator 与 AWS handoff guidance，补 packet version/专家负载/结果字段 |
| P1 | 接收面与转接遥测 | Google Cloud CCAI 官方 schema 将升级原因、目标人、等待/连接时长、队列、转接失败、服务等级和 deflection 分开记录；但它是客服转接模型，不等于长程 Agent 的人类处置证据；Alibaba 显示接管时机和失败类型会改变后续投入 | clip+compile → EX-003；寻找能同时报告 handoff packet、接收负载/队列、升级时机和人类结果的部署级案例 |
| P0 | AgentJudgeBench reference 对照 | v1 已核读；C3 仅一个 generator/两个 judge，显示 Gemini 可对错误 reference 保持相同 alignment，而 QwQ 接近无 reference；120 条记录仅单标注者，且 programmatic scorer 对 schema-valid extra keys 的严格度与人类不一致 | clip+compile → EX-004，并与 EX-001/EX-002 共用 `reference condition × information provenance × verifier independence` 字段表 |
| P0 | OpenAI coding evaluation audits | 已联网核读两份官方材料，尚未进入 raw/source；需提取题面、测试、gold patch、低覆盖、独立人审与训练污染的归因字段 | clip+compile → EX-004 |
| P0 | Agentic Benchmark Checklist | 已核读一手论文，尚未进入 raw/source；需提取 task/outcome validity、ground-truth 审查、语义等价、环境冻结与污染控制字段 | clip+compile → EX-004 |
| P0 | GeneBench target identifiability | 已核读 OpenAI 一手技术报告，尚未进入 raw/source；需提取可恢复目标、可辨识性审查、prompt-grader mismatch 与 trace audit 字段 | clip+compile → EX-004 |
| P0 | AcquaBench success provenance | 已核读作者版本；需入库 CLEAN/GOLD/SHAM、D0/D2、四种接口非独立复制、冻结配置与 provenance estimand，并与静态 reference integrity 分层 | clip+compile → EX-004 |
| P0 | EnvTrustBench / EVMbench 三层 oracle | EnvTrustBench 将 true environment state、outcome oracle 与 trace oracle 分开；EVMbench 用交易 replay 与链上验证判定执行结果，但 reference 与 success provenance 未形成同轨交叉 | clip+compile → EX-004；提取 `reference manifest → environment state hash → action/receipt → post-state` 及 accepted denominator、replay 与真值限制 |
| P0 | tau3 task fixes | 已核读官方修复记录，尚未进入 raw/source；需提取错误 expected action、任务歧义、不可行约束与修复前后 pass^1/pass^4 | clip+compile → EX-004 |
| P0 | SWE-bench Verified oracle 质量审查 | 已联网核读官方材料，尚未进入 raw/source；需提取规格、测试、环境和三次独立标注如何改变可评估样本 | clip+compile → EX-004 |
| P0 | PatchDiff 行为等价复核 | 已联网核读 ICSE 2026 一手论文，尚未进入 raw/source；需提取 test-pass、行为差异、人工确认错误与 developer patch 非唯一真值的边界 | clip+compile → EX-004 |
| P0 | ELT-Bench-Verified benchmark audit | 已联网核读一手论文，尚未进入 raw/source；需提取 ground-truth error、脚本误报、人类 agreement 和修正前后排名 | clip+compile → EX-004 |
| P1 | 真实 Agent trace 的语义等价与 reference 版本 | 缺同一生产任务上“结构不同但结果等价”的 reference、版本变更和独立裁决记录 | new-source → EX-004 |
| P1 | reference 呈现方式的因果对照 | 缺把正确 reference、错误 reference、只给 rubric 和不展示 reference 随机化的 live-agent judge 研究 | new-source → EX-004 |
| P0 | 三门交叉操纵 | REDAgentBench 已在固定 rollout 上操纵 evidence view/proof contract，并以 service receipt、最终状态和盲审校准分离执行结果与观察标签；Partial Evidence Bench 已固定 oracle、改变授权可见证据；两者都没有同时操纵 verifier independence 与 reference/provenance 条件 | clip+compile REDAgentBench、Partial Evidence Bench；继续寻找带固定 trace、可重放环境、版本化 reference/provenance ledger、跨 verifier/外部 oracle 的 factorial benchmark；CAFE 仅作实验设计方法参考 |
| P1 | ALE Robotics 的 hidden-grader integrity 边界 | 官方协议把 hidden seed、verify 阶段隔离、engine-native 重算、validated/verified attestation 分开；但 anchor/reference 仍由同一 benchmark 体系提供，未操纵错误/语义等价 reference，也没有跨 verifier 或外部 truth 对照 | clip+compile → EX-004；提取 reference owner/version、hidden seed、grader isolation、score re-derivation、attestation 与 external adjudication 的分层字段 |
| P0 | Agent permissions：interface 到 enforcement | 已核读 arXiv 2607.13718，尚未进入 raw/source；需提取权限规格、推导、运行时执行、审批透明度、撤销与 reviewer overhead 字段 | clip+compile → EX-005 |
| P0 | Deterministic pre-action authorization | 已核读 arXiv 2603.20953 v1；需核查 OAP 威胁模型、单域/非随机 CTF、平台信任、ESCALATE 未实现与 pre-tool-call gate 边界；论文自报结果不作普遍事实 | clip+compile → EX-005 |
| P0 | FORGE / Formal Policy Enforcement | arXiv 2602.16708 v3 提供多 Agent reference monitor、provenance substrate 与受控任务结果，尚未进入 raw/source；需保留 assume/guarantee、instrumented-surface、并发与 recovery 边界 | clip+compile → EX-005 |
| P1 | Janus 用户参与式权限管理 | arXiv 2607.01510 以 6 个 permission assistant、3 类 synthetic responder 做小规模对照；需提取人审—负担—攻击调用权衡及 synthetic responder 限制 | clip+compile → EX-005 |
| P0 | Microsoft Azure SRE Agent 审计与 incident metrics 文档 | 已有事件名、关联字段和缓解指标，尚未进入 raw/source；需核对字段是否能回链到实际动作与审批 | clip+compile → EX-005 / CR-004 |
| P1 | AWS Druva production recovery workflow | 已有 8–10 agents、scoped permissions 与 recovery workflow 的客户披露；缺授权、撤销、回滚和 action-surface 分母 | clip+compile → EX-005 |
| P0 | ACRFence / checkpoint-restore 副作用 | 已核读 10/10 重复提交与 stateless token resurrection；缺 mitigation 实现评估、跨框架复现和真实外部 post-state | clip+compile → EX-005 |
| P0 | HBHC / 有界层级撤销 | 已核读 49-agent 受控结果；需核代码、网络分区/旁路覆盖与 revoked-after-send 条件，不能把未来调用阻断当作回滚 | clip+compile → EX-005 |
| P1 | 逐动作授权、撤销与恢复实测 | OpenAI/HF 事故材料提供事故级遏制锚点；MCP Tasks、A2A、Temporal、OAuth 与 AWS Step Functions 补足取消、令牌失效、在途终态、状态查询与补偿语义；Atomix/Cordon/Dapr/CAVA/Auditable Agents 区分 gate、provenance、dispatch receipt 与 provider post-state，但仍缺逐动作撤销耗时、未知提交率、post-state 对账、回滚成功率和 MTTR | clip+compile → EX-005 |
| P1 | Recourse/BCCA 与 Stripe 效果结算边界 | Recourse/BCCA 提供本地 provider-compatible effect/recovery receipt 与 residual 结果；Stripe 官方文档提供 idempotency、cancel/refund 与 5xx reconciliation 语义，但均缺 revoke-after-send、provider-authoritative post-state 与独立复核的同案证据 | clip+compile → EX-005；提取 `action/intent identity → provider receipt → cancel/recovery → post-state → independent reconciliation` 字段，保留 sandbox 与 provider 自身复核限制 |
| P0 | 跨系统撤销传播与恢复链 | Google IAM 策略变更通常约 2 分钟、可能 7 分钟以上；Entra 应用自有 session 需应用撤销；GitHub 事故显示恢复、豁免、缓存刷新和确认分步完成；缺 Agent action 同链实测 | clip+compile → EX-005 / CR-004 |
| P1 | Agent incident response actuation trace | 新事故与运营材料补足事件 ID、审批/工具事件和局部恢复字段，但仍缺同一事件键连接 `flag→verdict→policy version→action-surface→in-flight→revoke/recovery→canonical post-state→independent review` 的脱敏导出；优先取得同案 effect lineage，不再横向累积 schema 文档 | clip+compile → EX-005 / Agent-Security Topic |
| P0 | Policy-carriage integrity / ControlCapsule | [arXiv 2605.12535](https://arxiv.org/abs/2605.12535) v3 已核读但未进入 raw/source；需提取 policy 的存在、语义健全、对象绑定、有效预算、preflight 与 action-boundary 指标，并保留其 0/90 action-level negative boundary | clip+compile → EX-006 |
| P0 | Governance Decay / ConstraintRot | [arXiv 2606.22528](https://arxiv.org/abs/2606.22528) v2 已核读但未进入 raw/source；需核查 compaction、summarizer injection、Constraint Pinning 与 operator-impersonation 的对照，以及 token-stream 外部权威通道这一开放边界 | clip+compile → EX-006 / CR-004 |
| P0 | Sleeper Memory Poisoning | [arXiv 2605.15338](https://arxiv.org/abs/2605.15338) v2 已核读但未进入 raw/source；需提取 memory write—retrieve—use 三阶段、删除/纠正/用户审查/来源谱系防御缺口，并与 CR-002 区分数据最小化问题 | clip+compile → EX-006 / CR-002 |
| P1 | Security-Recall Divergence | [arXiv 2604.20911](https://arxiv.org/abs/2604.20911) 已核读但未进入 raw/source；需核查 omission/commission 不对称、Safe Turn Depth 与格式代理限制，不能把代理约束直接外推为真实泄露风险 | clip+compile → EX-006 / CR-004 |
| P1 | SMSR / runtime memory provenance | [arXiv 2606.12703](https://arxiv.org/abs/2606.12703) 提供 HMAC write boundary、authenticated injection 分支与 certificate/utility trade-off；缺真实 memory backend、外部 action post-state 和 human adjudication | clip+compile → EX-006 / CR-002 |
| P1 | MemSecBench memory lifecycle | [arXiv 2607.27080](https://arxiv.org/abs/2607.27080) 提供 Write→Execute→Forget 的 linked lifecycle benchmark；缺部署级 trace、合法主体恶意写入和与撤销/恢复链的对照 | clip+compile → EX-006 / CR-002 / EX-005 |
| P0 | 自我改进回路的独立变更审计 | Meta-Harness、HELIX、Evo-Harness、HarnessEvolve 与 HSI 分别提供 train/dev gate、recipe/trace/verifier 归因、feedback provenance、分层编辑边界与 held-out 选择；Rethinking 提醒匹配 test-time search 后，分数提升仍可能不是 harness benefit；仍缺跨版本回放、不可改写 feedback、独立安全策略、canary 和 rollback 记录 | clip+compile → EX-007；优先入库 HarnessEvolve、HSI、Harness Updating Is Not Harness Benefit 与 Rethinking，并对齐 change owner、component、版本/hash、外部 oracle、feedback provenance、canary、rollback |
| P0 | Harness 行为契约与保留测试区 | GitHub 案例显示离线评测漏掉并行回归；HELIX 的 Pytest 配对轨迹进一步显示 target tests 通过仍可有 PASS_TO_PASS 回归，干净 patch 也可能在语义边界上失败；Rethinking 还显示同 benchmark 搜索可能掩盖 held-out 退化；缺跨版本、跨产品的行为不变量与回滚记录 | clip+compile → EX-007；提取 HELIX 的 regression-aware sibling labels，与 Rethinking 的 matched search/held-out 字段及 GitHub 行为契约对齐 |
| P1 | 生产 Agent fleet 的自修改纵向记录 | 缺 prompt/skill/router/evaluator 变更的 owner、版本、canary、回滚、隐藏 holdout 与质量/安全联合结果 | new-source → EX-007 |
| P0 | 劳动经济学企业—职业交叉校准 | Ramp、Dallas Fed、Census、纽约联储和丹麦匹配研究各自只闭合局部层；formal/function/worker-task/operational adoption 不是同一变量，缺共同企业—个人—职业—时期键、培训完成与再生代理 | 先补 S3《Prompting Change》正式稿/方法；clip+compile S1–S7；建立带分母/状态/版本的 evidence long table 与 `firm × person × occupation × period` 字段表 |
| P0 | 劳动经济学代表性与预期偏差 | Atlanta Fed 近 6,000 家四国企业调查显示过去三年影响有限、未来预期生产率上升而就业下降；缺与实际招聘流量的同窗校准 | clip+compile Atlanta Fed Firm Data on AI；区分 realized / expected / platform-selected evidence |
| P1 | OTel GenAI 正式规范与开放提案 | 主分支仍为 Development，缺 authorization、post-state、revoke/recovery 和完整 action-surface 分母；PR #483 仅提议 state delta，PR #447 仅提议部分 tool/API transfer，均仍 Open | clip+compile → CR-004；补官方 conformance/实现测试 → CR-004 |
| P1 | Google DeepMind AI Control / live monitoring | 官方材料已定位 coverage、recall、响应时间与异步/同步阻断边界，缺逐案阻断或覆盖率实证 | clip/compile → CR-004 |
| P1 | MCP 2026-07-28 无状态转折 | `SEP-2663` 的设计状态为 Final，但官方 Tasks 页面仍为 Draft，且官方 SDK conformance 显示扩展实现未齐；`taskId` 既是状态定位又是路由键，per-request auth 与不可猜测 ID 不能替代 effect receipt；缺生产级主体绑定、TTL/撤销/replay、故障转移和 post-state 对账 | clip+compile → MCP Entity；new-source → `EX-005/006` / `CR-004` |
| P0 | Anthropic 设计负责人一手公开文本 | 官方 Product Design team case study 支持代码化原型、系统状态与 edge-case 设计，但缺 Jenny Wen / Joel Lewenstein 对模型行为、反馈、工作流和责任边界的直接说明 | clip+compile → AI-Era-Designer-Role |
| P0 | Google Gemini / DeepMind 当前设计团队材料 | Google PAIR 支持反馈、控制与模型行为是设计对象，但不是当前 Gemini/DeepMind 产品团队的实际工作流或结果证据 | new-source → AI-Era-Designer-Role |
| P0 | Microsoft AI / Copilot 当前设计团队材料 | Microsoft Research 的 2019 指南与 2026 Agent 设计基础支持 inference、错误、控制与长期行为设计，但缺当前组织分工、上线控制与反馈闭环 | new-source → AI-Era-Designer-Role |
| P1 | 跨公司设计结果对照 | 缺 feedback latency、原型—上线周期、返工/事故、模型/产品改动链与责任 owner 的同口径记录 | new-source → AI-Era-Designer-Role |
| P1 | Agent 隐私对照 | 微软官方 least-privilege 已定位；新增 arXiv 2607.22611、AWS/KTern.AI 与 [Numezis 匿名 SME 案例](https://advisory.numezis.com/en/work/business-agent-platform-sme)，均待入 raw/source；EDPB Guidelines 02/2026 最终版未发布 | clip/compile → CR-002 |
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
