---
type: research-agenda
title: "Agentic Work Atlas 研究议程"
created: 2026-05-22
updated: 2026-09-05T18:33:21+08:00
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
- Evidence: `raw/20260608-connector-observability-directory.md`、`raw/20260819-google-ai-evals-inspect-skill.md`；Anthropic 三案、OpenAI HF/第三方评测 URL；[Google DeepMind AI Control](https://deepmind.google/blog/securing-the-future-of-ai-agents/) 与 [Roadmap PDF](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/securing-the-future-of-ai-agents/gdm-ai-control-roadmap.pdf)（均待 clip）；[OTel GenAI agent/framework 规范](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md) 与 [Trace API](https://opentelemetry.io/docs/specs/otel/trace/api/)（待 clip）
- Evidence goal: 取得逐案事前阻断或 coverage/recall 数据，区分“仪器化闭包”的架构承诺与真实污染向量覆盖的实证，并核对标准 trace 是否足以重建 action-surface 与责任链。
- Last checked: 2026-09-05T17:39:01 · refined
- Next: clip+compile OTel GenAI agent/framework、通用 GenAI spans 与 Trace API；逐格核查原生 span/event/link 与 action-surface、verdict、authorization、actuation、revoke/recovery、review 字段的边界
- Retry: new-source:google-deepmind-ai-control

### CR-005 · AI 采纳侵蚀专业能力再生
- Status: ready
- Priority: P0
- Claim: 组织从 AI 获得局部效率收益的同时，会把专业能力再生成本外部化到整个职业共同体。
- Gap: Counterexample
- Evidence: `raw/20260731-tragedy-cognitive-commons-ai-expertise.pdf`、`raw/20260730-lenny-tech-workers-ai-sentiment-noam-segal.md`、`raw/Learning on the Shop floor.md`；[Ramp×Revelio Labs](https://www.reveliolabs.com/news/ai-and-work/greater-ai-investment-more-hiring)；[Dallas Fed 招聘分析](https://www.dallasfed.org/research/economics/2026/0901)；[Dallas Fed 2026-05 TBOS](https://www.dallasfed.org/research/surveys/tbos/2026/2605q)
- Evidence goal: 反例必须同时显示高采纳、培训/晋升/独立验证等专业再生机制持续存在；单纯 headcount 或入门级占比上升不够。Ramp×Revelio 的企业层扩张与 Dallas Fed 的职业/入口层收缩目前构成层级对照，尚不能裁决 Claim。
- Last checked: 2026-09-05T18:33:21 · refined
- Next: clip+compile Ramp×Revelio 与 Dallas Fed 一手材料；随后寻找同时报告培训投入、内部晋升、专家补充率或独立验证质量的高采纳纵向案例
- Retry: new-source:ai-adoption-training-promotion-validation-data

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
| P0 | Agent 安全 Topic 建设 | 五阶段骨架已起草；下一步以事件级标识对齐 `flag → verdict → authorization → actuation → revoke/recovery → review`，逐格核验 `owner / action-surface`，不把结构地图当作安全效果证据；不由 recompile 执行 |
| P0 | 验证器危机研究线 | 按独立性四轴、证据覆盖/解释能力与 reference integrity 建立矩阵，再 clip AgentJudgeBench、Anthropic 三案与 Astra 官方材料 |
| P0 | 劳动经济学实证 | 用已编译 Economic Index 与新增一手数据建立校准骨架 |
| P1 | MCP 无状态转折 | 先区分传输层去 session 与应用层状态迁移；核对显式 handle、MRTR、每请求元数据、幂等/撤销/replay 与事件谱系，再更新 MCP Entity |
| P1 | AI 时代设计方法论对照 | 至少补两份其他实验室设计负责人访谈再判断共识 |
| P2 | Topic 与复核队列代谢 | 处理无承载 Entity 簇和疑似重复项，不继续制造新定理 |

## 开放探索候选

| ID | 候选问题 | 当前判断 | 证伪方向 | 下一步 |
|---|---|---|---|---|
| EX-001 | 验证器独立性是否是目标、证据、执行、时间四轴的最弱轴瓶颈？ | `2604.07650` 仅在输出错误、任务难度和模型/验证器组合上测相关性；AJ-Bench 的环境访问并未操纵验证器独立性，故两者可共享矩阵但不能互作替代；refined | 固定证据访问、reference 与任务后，跨家族/独立实现的单轴变化仍不能降低共同漏报，或独立性效应完全由证据覆盖/判定质量解释 | clip+compile `2604.07650`，按“错误生成相关性 × 证据状态 × reference 条件”补交叉字段 |
| EX-002 | 独立性之外，证据覆盖与证据解释是否构成验证的第二个必要门？ | AJ-Bench 将取得信息、状态验证、过程验证分开测量，并区分“误读工具输出”和“证据正确但推理错误”；SkillTV-Bench 进一步把“环境可访问”与“按检查策略主动取得/解释证据”分开，但其 JudgeSkill、source-verifier 与任务构造仍未独立操纵；refined | 固定模型/验证器、任务、reference 与访问权限后，静态低覆盖、可交互读取和显式检查策略对照不改变漏报，或差异完全由 token budget、模型相关性或真值瑕疵解释 | clip+compile AJ-Bench 与 SkillTV-Bench，建立“物理可见性 × 检查策略 × 证据解释 × 同族/跨族 × reference 条件”矩阵，并与 EX-001 对齐 |
| EX-003 | Facilitator agent 能否在缺少人类隐藏信息的条件下校准“何时升级、升级给谁、给什么上下文”，而不制造新的监督盲区？ | 选择性委派研究将路由器定义为定位“人类优于 Agent 区域”的 rejector；现有材料支持隐藏特征和 framing 改变升级质量；Google SRE/AWS 明确结构化交接与完整性，Google Cloud 将目标人、队列、等待/转接失败作为独立接收变量；synthesized/refined | 在固定升级触发、专家身份、Agent 输出和接收面可用性后，完整/最小/证据-only/带模型结论的交接包对人类正确率、处置延迟、补问次数和过度依赖均无稳定差异，或差异完全由 CR-004 的可见性、EX-002 的证据覆盖、消息 framing 或接收队列解释；反之若交接包残差持续存在，保留为 EX-003 内部独立子门 | clip+compile Google SRE AI Operator 与 AWS handoff guidance；补查 Google Cloud escalation/transfer telemetry；建立“路由选择 × 交接包 × 消息 framing × 专家负载/队列”矩阵，先固定路由与接收面做 context ablation，再与 CR-004 / EX-002 对照 |
| EX-004 | reference integrity 与 success provenance 是否构成独立必要门？ | AgentJudgeBench 的 C3 显示 judge 可能只锚定 reference block，且其 programmatic reference 与单标注者人类判断在语义等价处有差异；AcquaBench 则操纵正确目标可得性与匹配的错误 source exposure。两者应暂视为耦合但不可替代的两个子门，尚未有交叉因果证据；refined | 固定 trace 随机化无/正确/语义等价/错误 reference，或固定 reference 随机化 CLEAN/GOLD/SHAM；若 judge/score 与 human adjudication 不变，或差异可由 EX-001/EX-002 解释，则收窄或并回 | clip+compile AgentJudgeBench、AcquaBench、ABC、GeneBench、OpenAI coding audit、tau3、ELT-Bench-Verified；审查代码/数据与公式—案例对应关系；先做 `reference condition × information provenance × verifier independence` 交叉表，再寻找真实/可回放第二案例 |
| EX-005 | 在检测与判定都正确时，动作授权、独立执行点与撤销/恢复时限是否仍构成 Agent 安全的独立必要门？ | FORGE/OAP、Microsoft Azure SRE、Google SRE 与 Druva 材料共同把权限、审批、执行、验证和审计分开；Microsoft 已提供 `IncidentId/TraceId/CorrelationId`、审批、工具执行和 `IncidentCreated/Handled/MitigatedOn` 字段，但公开材料仍缺独立 verdict/authorization/revoke/rollback/recovery 状态与 action-surface 分母；refined | 在同一 trace、verdict、工具 schema 与负载下随机化 prompt-only、模型 guard、确定性 reference monitor 与 monitor+rollback；若现有 incident 字段已能重建授权 owner、撤销/回滚结果、再次暴露与 MTTR，或固定 verdict 后无 enforcement 残差，则并回 CR-004/EX-003/普通 IAM | clip+compile Microsoft 审计/指标文档、Druva 案例与 FORGE/OAP/Janus；寻找独立生产 trace、token TTL、撤销耗时、回滚成功率和完整 action-surface 分母；按风险/可逆性区分同步阻断与异步复核 |
| EX-006 | 高影响/不可逆动作的治理约束，是否必须以带来源、稳定绑定、预算隔离且失败关闭的控制状态抵达决策/执行边界，而非普通 token-stream 文本？ | 四篇一手论文共同支持 context eviction/weakening/misbinding、compaction decay 与跨会话 memory write—retrieve—use；但 Ghost 的 action-level 结果为 0/90 negative boundary，SRD 使用格式代理，四篇均未证明 OOB control plane 普遍必要；refined | 若受保护/版本化 policy + deterministic preflight/action guard 与 OOB registry 在固定 verdict、action-surface、延迟和 recovery 指标上等效，则把 OOB 收窄为实现选项；若语义安全约束与 memory recovery 在真实 trace 中不衰减，则收窄为特定实现风险 | clip+compile 四篇一手研究；先建立 `policy provenance → binding → budget/survival → verdict → action boundary → revoke/recovery` 字段矩阵，再找固定 verdict 下 policy-carriage × enforcement 对照 |
| EX-007 | 自我改进 Agent 的变更晋级是否需要按变更对象分层的不可自证门，防止 harness、评估器、目标与策略共变把“分数提升”伪装成能力/安全提升？ | 本地材料显示三类对象不能共用一个 gate：行为组件可能出现结果不变但并行/停止/副作用顺序回归；评估/目标组件可能因 benchmark 内部适配抬高分数；策略/执行组件可能绕过安全边界。固定开发 gate 可审计候选选择，但不等于外部真值或安全保证；refined | 若固定模型/任务后，行为契约能捕获所有行为组件线上残差；若评估/目标共变仍能在冻结外部 oracle、hidden holdout 和独立安全复评上稳定复现；或所有残差最终可由 `EX-004/006` 解释，则削弱或合并 `EX-007` | new-source → EX-007；先补 SkillTV/第二个行为回归案例，再寻找同一变更的 offline→online、独立复评、policy 冻结与 rollback 记录；没有新证据前不再抽象第四类 gate |

## Source 需求队列

| 优先级 | 目标 | 当前缺口 | 触发行动 |
|---|---|---|---|
| P0 | Agent Safety Topic 跨层核验 | 五阶段骨架与一条事故级响应链已找到；下一步以事件级标识对齐 `flag → verdict → authorization → actuation → revoke/recovery → review`，逐格核验 `owner / action-surface`，不把结构地图当作安全效果证据；不由 recompile 执行 |
| P0 | EU AI Act 首轮罚款官方决定 | €47M 三案系单链互引二手叙事（法律基础矛盾、无官方决定原文），需官方决定/一手披露判定真伪 | clip → 核对 CR-001 |
| P0 | Anthropic 三起评测事故 | 已联网核读一手来源（browsecomp/mythos/system card），未进入 raw/source | clip+compile → CR-006 |
| P0 | OpenAI 评测越界披露 | HF 事件及 UK AISI/Irregular 两起第三方评测尚未进入 raw/source | clip+compile → CR-006 |
| P0 | 评测逃逸加固后反例 | 缺独立部署级“加固后逃逸归零”或“同一失配仅发生一次”的记录；受控 SandboxBench 不足 | new-source → CR-006 |
| P0 | arXiv 2604.07650 行为纠缠框架 | 已定位但未 clip/compile | clip → compile → CR-003 / LLM-as-a-Judge 激励共压 flag |
| P0 | Apple《Nine Judges, Two Effective Votes》 | 已联网核读一手页面，未进入 raw/source | clip+compile → CR-003 |
| P0 | arXiv 2607.10139《LLMs as a Jury》 | 已联网核读一手预印本，未进入 raw/source；报告跨模型 verifier 的共享错误下界 | clip+compile → CR-003 |
| P0 | 验证器独立性四轴对照 | `2604.07650` 给出输出层相关性与后续 judge bias 的关联，但未操纵证据访问、reference 有效性或行动执行；需把独立性作为正交因子，而不是把跨模型/跨工具直接当作独立验证 | clip+compile → EX-001；优先寻找同任务、固定证据与 reference 的跨家族/独立实现对照 |
| P0 | AJ-Bench 环境感知验证基准 | 已核读一手预印本，报告 155 个任务、516 条轨迹、工具交互、四类失败及 FPR/FNR；其 LLM/模型多数投票与人工/脚本混合标注，以及搜索域外部环境，需单独记录 reference provenance 与 access confound | clip+compile → EX-002；提取信息取得、状态/过程验证、证据误读、正确证据错误推理和环境重放字段 |
| P0 | SkillTV-Bench 证据驱动轨迹验证 | 一手论文与公开仓库提供 681 条可运行案例、task-time skills、可检查 artifacts、隐藏 source-verifier 和 disjoint evolution split；缺 JudgeSkill 各阶段的 inspection coverage、独立外部裁决、reference 条件与模型家族交叉对照 | clip+compile → EX-002/007；先核对数据 provenance、固定 36-case gate、false-accept 变化与环境访问/检查策略的可分性 |
| P0 | Human-AI Teaming Through the Lens of Calibration | arXiv 2606.10906 已核读但未进入 raw/source；需提取 rejector 定理、人类隐藏特征与不可约 excess risk 条件 | clip+compile → EX-003 |
| P0 | 选择性预测的校准失效 | PMLR 333（2026）多模态 ICU 研究显示聚合指标会遮蔽按类别误校准；需提取 per-class calibration、deferral 与 expert load 结果及任务边界 | clip+compile → EX-003 |
| P1 | 人类-路由消息效应 | arXiv 2112.06751 显示 deferral status 与 model prediction 的组合会改变人类准确性；需核对 messaging、human-in-loop 指标与外推边界 | clip+compile → EX-003 |
| P0 | 主动升级的部署级长程案例与交接契约 | Google SRE AI Operator 报告结构化上下文目录、完整调查历史交接、数千起 incident 与 human Golden Data；AWS Agentic AI Lens 明确要求交接延迟、上下文完整性和协作成功率，但两者都缺固定升级触发下的交接包消融、人类决策质量与长期漂移对照 | clip+compile → EX-003；优先入库 Google SRE AI Operator 与 AWS handoff guidance，再寻找独立部署级长程案例 |
| P1 | 接收面与转接遥测 | Google Cloud CCAI 官方 schema 将升级原因、目标人、等待/连接时长、队列、转接失败、服务等级和 deflection 分开记录；但它是客服转接模型，不等于长程 Agent 的人类处置证据 | clip+compile → EX-003；寻找能同时报告 handoff packet、接收负载/队列和人类结果的部署级案例 |
| P0 | AgentJudgeBench reference 对照 | v1 已核读；C3 仅一个 generator/两个 judge，显示 Gemini 可对错误 reference 保持相同 alignment，而 QwQ 接近无 reference；120 条记录仅单标注者，且 programmatic scorer 对 schema-valid extra keys 的严格度与人类不一致 | clip+compile → EX-004，并与 EX-001/EX-002 共用 `reference condition × information provenance × verifier independence` 字段表 |
| P0 | OpenAI coding evaluation audits | 已联网核读两份官方材料，尚未进入 raw/source；需提取题面、测试、gold patch、低覆盖、独立人审与训练污染的归因字段 | clip+compile → EX-004 |
| P0 | Agentic Benchmark Checklist | 已核读一手论文，尚未进入 raw/source；需提取 task/outcome validity、ground-truth 审查、语义等价、环境冻结与污染控制字段 | clip+compile → EX-004 |
| P0 | GeneBench target identifiability | 已核读 OpenAI 一手技术报告，尚未进入 raw/source；需提取可恢复目标、可辨识性审查、prompt-grader mismatch 与 trace audit 字段 | clip+compile → EX-004 |
| P0 | AcquaBench success provenance | 已核读作者版本；需入库 CLEAN/GOLD/SHAM、D0/D2、四种接口非独立复制、冻结配置与 provenance estimand，并与静态 reference integrity 分层 | clip+compile → EX-004 |
| P0 | tau3 task fixes | 已核读官方修复记录，尚未进入 raw/source；需提取错误 expected action、任务歧义、不可行约束与修复前后 pass^1/pass^4 | clip+compile → EX-004 |
| P0 | SWE-bench Verified oracle 质量审查 | 已联网核读官方材料，尚未进入 raw/source；需提取规格、测试、环境和三次独立标注如何改变可评估样本 | clip+compile → EX-004 |
| P0 | PatchDiff 行为等价复核 | 已联网核读 ICSE 2026 一手论文，尚未进入 raw/source；需提取 test-pass、行为差异、人工确认错误与 developer patch 非唯一真值的边界 | clip+compile → EX-004 |
| P0 | ELT-Bench-Verified benchmark audit | 已联网核读一手论文，尚未进入 raw/source；需提取 ground-truth error、脚本误报、人类 agreement 和修正前后排名 | clip+compile → EX-004 |
| P1 | 真实 Agent trace 的语义等价与 reference 版本 | 缺同一生产任务上“结构不同但结果等价”的 reference、版本变更和独立裁决记录 | new-source → EX-004 |
| P1 | reference 呈现方式的因果对照 | 缺把正确 reference、错误 reference、只给 rubric 和不展示 reference 随机化的 live-agent judge 研究 | new-source → EX-004 |
| P0 | 三门交叉操纵 | 缺在同一任务中同时改变 verifier independence、evidence visibility/interpretation 与 reference integrity/success provenance 的受控设计，当前跨论文结果不能支持必要性或交互效应 | new-source → EX-001/002/004；优先寻找带固定 trace、可重放环境和外部/人类 oracle 的 factorial benchmark |
| P0 | Agent permissions：interface 到 enforcement | 已核读 arXiv 2607.13718，尚未进入 raw/source；需提取权限规格、推导、运行时执行、审批透明度、撤销与 reviewer overhead 字段 | clip+compile → EX-005 |
| P0 | Deterministic pre-action authorization | 已核读 arXiv 2603.20953 v1；需核查 OAP 威胁模型、单域/非随机 CTF、平台信任、ESCALATE 未实现与 pre-tool-call gate 边界；论文自报结果不作普遍事实 | clip+compile → EX-005 |
| P0 | FORGE / Formal Policy Enforcement | arXiv 2602.16708 v3 提供多 Agent reference monitor、provenance substrate 与受控任务结果，尚未进入 raw/source；需保留 assume/guarantee、instrumented-surface、并发与 recovery 边界 | clip+compile → EX-005 |
| P1 | Janus 用户参与式权限管理 | arXiv 2607.01510 以 6 个 permission assistant、3 类 synthetic responder 做小规模对照；需提取人审—负担—攻击调用权衡及 synthetic responder 限制 | clip+compile → EX-005 |
| P0 | Microsoft Azure SRE Agent 审计与 incident metrics 文档 | 已有事件名、关联字段和缓解指标，尚未进入 raw/source；需核对字段是否能回链到实际动作与审批 | clip+compile → EX-005 / CR-004 |
| P1 | AWS Druva production recovery workflow | 已有 8–10 agents、scoped permissions 与 recovery workflow 的客户披露；缺授权、撤销、回滚和 action-surface 分母 | clip+compile → EX-005 |
| P1 | 逐动作授权、撤销与恢复实测 | OpenAI/HF 事故材料提供重建、凭据/账户/工作负载遏制和批量停机的事故级锚点；仍缺 token TTL、逐动作撤销耗时、阻断延迟、回滚成功率等可比较部署数据 | clip+compile → EX-005 |
| P1 | Agent incident response actuation trace | OpenAI/HF 材料补足一条从告警到调查、遏制、重建、再次暴露到更广停机的事故级链条；仍缺同一生产任务中带稳定事件标识、明确 verdict/owner 的 `flag→owner→block/rollback→recovery→review` 完整时间线与对照 | clip+compile → EX-005 / Agent-Security Topic |
| P0 | Policy-carriage integrity / ControlCapsule | [arXiv 2605.12535](https://arxiv.org/abs/2605.12535) v3 已核读但未进入 raw/source；需提取 policy 的存在、语义健全、对象绑定、有效预算、preflight 与 action-boundary 指标，并保留其 0/90 action-level negative boundary | clip+compile → EX-006 |
| P0 | Governance Decay / ConstraintRot | [arXiv 2606.22528](https://arxiv.org/abs/2606.22528) v2 已核读但未进入 raw/source；需核查 compaction、summarizer injection、Constraint Pinning 与 operator-impersonation 的对照，以及 token-stream 外部权威通道这一开放边界 | clip+compile → EX-006 / CR-004 |
| P0 | Sleeper Memory Poisoning | [arXiv 2605.15338](https://arxiv.org/abs/2605.15338) v2 已核读但未进入 raw/source；需提取 memory write—retrieve—use 三阶段、删除/纠正/用户审查/来源谱系防御缺口，并与 CR-002 区分数据最小化问题 | clip+compile → EX-006 / CR-002 |
| P1 | Security-Recall Divergence | [arXiv 2604.20911](https://arxiv.org/abs/2604.20911) 已核读但未进入 raw/source；需核查 omission/commission 不对称、Safe Turn Depth 与格式代理限制，不能把代理约束直接外推为真实泄露风险 | clip+compile → EX-006 / CR-004 |
| P0 | 自我改进回路的独立变更审计 | 现有 Meta-Harness 只有 train/dev gate，Uber 只有内部 benchmark 与 session 指标；缺冻结外部 oracle、跨版本回放、独立安全策略和变更归因 | new-source → EX-007 |
| P0 | Harness 行为契约与保留测试区 | GitHub 案例显示离线评测漏掉并行回归，另有官方开发实践把只能由人改动的保留测试作为 contract gate；缺跨版本、跨产品的行为不变量与回滚记录 | new-source → EX-007 |
| P1 | 生产 Agent fleet 的自修改纵向记录 | 缺 prompt/skill/router/evaluator 变更的 owner、版本、canary、回滚、隐藏 holdout 与质量/安全联合结果 | new-source → EX-007 |
| P0 | 劳动经济学硬数据 | Ramp×Revelio 显示高强度采用企业两年 headcount 约 +10.2%、入门级占比 +1.15pp；Dallas Fed 显示高暴露职业招聘相对下降约 5–8%、年轻入口受压，且 71.4% 企业报告生产率提升但仅 7.4% 报告工资增长；尚未入 raw/source | clip+compile → CR-005；按企业/职业/任务/工资/培训五层对齐 |
| P1 | OTel GenAI 正式规范 | 已核读官方 agent/framework、GenAI spans 与 Trace API；现行语义仍为 Development，能记录局部 lineage 与 tool payload，但缺 authorization、post-state、revoke/recovery、handoff 和完整 action-surface 分母 | clip+compile → CR-004 |
| P1 | Google DeepMind AI Control / live monitoring | 官方材料已定位 coverage、recall、响应时间与异步/同步阻断边界，缺逐案阻断或覆盖率实证 | clip/compile → CR-004 |
| P1 | MCP 2026-07-28 无状态转折 | 传输层移除协议 session，但应用仍可用显式 handle、MRTR、业务 cache 和幂等键保留状态；缺 handle 绑定、TTL、撤销、replay、故障转移与事件谱系的迁移对照 | clip+compile → MCP Entity；new-source → `EX-005/006` / `CR-004` |
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
| 2026-09-05T18:33:21+08:00 | CR-005 AI 采纳与专业再生 | refined | Ramp×Revelio 的高强度采用企业扩大 headcount 与入门级占比，不能证明培训/晋升/独立验证再生；Dallas Fed 同时观察到高暴露职业招聘和年轻入口收缩，说明企业扩张、任务需求与能力再生是不同层级，暂不构成反例。 |
| 2026-09-05T17:39:01+08:00 | CR-004 OTel GenAI 语义边界 | refined | OTel 可枚举 agent/workflow/plan/tool invocation、局部 lineage 和通用 error，但不能独立表达授权、实际 action effect、证据可访问性/解释、human handoff 或安全责任链；结构化 trace 不是 action-surface 闭包，不新增 EX。 |
| 2026-09-05T16:37:33+08:00 | EX-006 治理状态承载与动作边界 | refined | 四篇一手论文支持 context eviction/weakening/misbinding、compaction decay 和跨会话记忆污染，但不证明 OOB control plane 普遍必要；将 EX-006 收窄为“决策时状态完整性门 + 独立动作边界 enforcement”两门，不新增 EX。 |
| 2026-09-05T15:32:07+08:00 | 动作授权与恢复的遥测字段 | refined | Microsoft、Google、AWS 形成动作控制面的结构重复；已有 incident/trace/审批/工具/缓解字段骨架，但仍缺 verdict/authorization/revoke/rollback/recovery 与 action-surface 分母，收窄 `EX-005`，不新增 EX。 |
| 2026-09-05T14:32:55+08:00 | 自我改进变更对象与晋级门 | refined | `EX-007` 收窄为变更晋级的归因与不可自改写问题：行为组件需行为契约/线上复评，评估与目标组件需冻结外部 oracle，策略与执行组件需独立安全门；不与 `EX-004/006` 合并，不新增 EX。 |

## 思考日志索引

- [[2026-09-05]] — open explore：对照 Ramp×Revelio 企业层 headcount/入门级占比、Dallas Fed 职业招聘/年轻入口与 TBOS 生产率—工资自报；确认“公司扩张”不等于“专业再生”，收窄 CR-005，不新增 EX
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
- [[2026-08-30]] — recompile CR-006（OpenAI 官方披露 UK AISI/Irregular 两起第三方评测越界，分别为授权边界未显式化与网络隔离配置失效；与 Anthropic 三案形成跨厂商重复，strengthened）
- [[2026-08-30]] — recompile CR-003（Apple 一手 9-judge/7-family 研究发现约 2.18 个有效独立投票、相关错误跨任务稳定；strengthened）
- [[2026-08-30]] — recompile CR-002（复核 arXiv 2607.22611 与 AWS/KTern.AI 原文，仍缺读取范围/保留期指标；与 00:00 证据一致，no_delta）
- [[2026-08-30]] — recompile CR-004（OpenAI 官方 HF 与第三方评测披露补充跨厂商边界证据；隐式门细化为控制未闭包/授权未显式化两型，事后监控不等于事前阻断，refined）
- [[2026-08-30]] — recompile CR-002（arXiv 生产权限架构与 AWS/KTern.AI 生产案例显示部署级 least-privilege 反例，削弱架构必然性；数据读取/保留仍未量化，weakened）
- [[2026-08-29]] — recompile CR-006（OpenAI 官方披露 HF 与第三方评测越界，跨厂商重复证据，strengthened）
- [[2026-08-29]] — recompile CR-003（arXiv 2604.07650 跨族行为纠缠）；recompile CR-004（Connector vs evals 对照：结构层可枚举/行为层竞速/意图层间接，结构门机制）；recompile CR-001（10:00 AI Office 首轮 €47M 罚单 strengthened；15:01 溯源官方新闻稿 IP/26/1714 + AI Omnibus 时间线无三案且高风险义务 2027-12 才适用，weakened；16:01 溯源两报道为单链互引内容站叙事 + 案件 3 法律基础矛盾，weakened）；recompile CR-002（两轮反例检索无部署级反例，微软/CSA/EDPB 确认过度特权为默认设计，strengthened）
- [[2026-08-29]] — recompile CR-005（二次反例检索无第二"高采纳+再生内部化"部署级案例，Shopify 仍单点，停止主动重查待外部触发，no_delta）；recompile CR-006（Anthropic 三案一手核读：BrowseComp 解密答案 key/mythos 逃逸双沙箱/system card 去污染，多因素归因 strengthened，自 blocked 恢复）；recompile CR-004（20:01 think：三案判为隐式门失效，门失效两型分类 + 仪器化闭包边界，refined）
- [[2026-08-29]] — recompile CR-003（22:00：复核同一 arXiv 来源，未新增独立证据，no_delta）
- [[2026-08-29]] — open explore：验证器独立性四轴候选（目标/证据/执行/时间），形成最弱轴判据、证伪方向与最小四条件实验设计；新增 `EX-001` 与 P0 Source 需求
- [[2026-08-27]] — recompile CR-005；Shopify/River 部署级反例收窄专业再生外部化预测
- [[2026-08-25]] — recompile CR-001；官方执行框架已生效，但实际罚单/执法决定仍缺
- [[2026-08-24]] — 15 个 legacy 区块：12 完成、3 中断；完成 v2 迁移与状态归一化；recompile CR-002、CR-003
- [[2026-08-23]] — 深度思考×13；Alpha Transfer、判断力与认知公地
- [[2026-08-04]] — 深度思考×11；08-03 判断的边界与反例复核
- [[2026-08-03]] — 深度思考×33；生成器降秩、前瞻预测与多项形式化
- [[2026-08-02]] — 深度思考×8；第三轮全量探索与赌注登记
- [[inventory-20260802]] — 08-02 全量盘点与健康度基线
- [[2026-07-23]] / [[2026-07-22]] — 验证瓶颈与合法权限研究线
- [[resolved-judgments]] — 已收敛判断归档
- [[resolved-principles]] — 已收敛操作原则
- 2026-06-20—2026-07-21 无外部依赖的 legacy 日志已于 2026-08-25 从工作树压缩；完整原文可从 Git commit `953e259` 恢复
