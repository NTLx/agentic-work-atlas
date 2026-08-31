---
type: research-agenda
title: "Agentic Work Atlas 研究议程"
created: 2026-05-22
updated: 2026-08-31T13:21:31
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
- Evidence: `raw/2026-eu-ai-act-compliance-autonomous-agents.md`；官方执法启动新闻稿 [IP/26/1714](https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1714)（2026-07-31）与生效日新闻页（均无 €47M 三案记录）；AI Omnibus 将高风险义务推迟至 2027-12/2028-08；€47M 三案经溯源性定向为单链互引的二手内容站叙事（AI Policy Desk 引 Artur Markus 为源，官方锚点零罚款，案件 3 法律基础两文冲突，详见 2026-08-29 日志）
- Evidence goal: 官方 AI Office/委员会处罚决定文本发布（确认或证伪 €47M 实例），或独立一手披露出现；€47M 三案现为 falsified 候选，制度能力面已一手确认
- Basis: evidence
- Last checked: 2026-08-29T16:01:09 · weakened
- Next: 收敛为触发式复查，不再主动检索——等待 (a) AI Office 官方处罚决定文本，或 (b) 独立一手披露；时间观察锚点：AI Omnibus 新增禁止实践条（2026-12 生效）后第一次可验证执法 action
- Retry: new-source:eu-ai-act-official-penalty-decision

### CR-002 · Agent 数据过度收集具有系统性
- Status: ready
- Priority: P1
- Claim: Agent 的数据过度收集来自任务代理架构，而不是单一产品或单一厂商的实现失误。
- Gap: Counterexample
- Evidence: `raw/20260618-mosaicleaks-privacy-agent.md`、`raw/How we contain Claude across products.md`、`raw/20260518-zero-trust-for-ai-agents.md`、`raw/20260616-why-is-meta-destroying-its-engineering.md`、`raw/20260714-context-collapse-2-when-emails-instruct.md`；[Microsoft 官方 least-privilege 模式](https://learn.microsoft.com/en-us/security/zero-trust/sfi/least-privilege-for-ai-agents)；[arXiv 2607.22611](https://arxiv.org/abs/2607.22611)（生产 8 个月的细粒度权限架构，自报只读 AI agent 与零未授权写入）；[AWS/KTern.AI 生产案例](https://aws.amazon.com/blogs/machine-learning/how-ktern-ai-built-agentic-ai-for-sap-on-amazon-bedrock-agentcore/)（20+ 生产 agents、per-agent least privilege；均待 clip/compile）
- Evidence goal: 复核部署级 least-privilege 案例是否包含长期数据最小化（读取范围/保留期）以决定是否进一步 weakened；若仅有权限/写入控制则收窄为默认风险，或等待跨厂商重复失效（→strengthened）；EDPB 02/2026 最终版或新反例披露可恢复检索。
- Last checked: 2026-08-30T13:00:40 · no_delta
- Next: clip+compile Numezis 案例，核查匿名部署的可验证细节与长期数据最小化；反例 Gap 保持开放
- Retry: new-source:numezis-agent-privacy-case-clipped

### CR-003 · AI 监督 AI 存在共模误差下界
- Status: ready
- Priority: P0
- Claim: 即使使用不同模型家族，AI 监督 AI 仍存在不可消除的共模误差下界。
- Gap: Boundary
- Evidence: `raw/20260713-agentic-misalignment-summer-2026.md`、`raw/20260330-reward-hacking-equilibrium-finite-evaluation.md`；[arXiv 2604.07650](https://arxiv.org/abs/2604.07650)（已核读，尚未 clip）；[Apple：Nine Judges, Two Effective Votes](https://machinelearning.apple.com/research/correlated-llm-evaluation-panels)（2026-06，一手研究）；[arXiv 2607.10139](https://arxiv.org/abs/2607.10139)（v3，2026-08-17，一手研究；跨家族 verifier panel 在 GPQA/MMLU-Pro 的 shared-error floor 分别为 0.030/0.143，数学任务接近 0）
- Evidence goal: 界定跨模型 consensus verifier 的 shared-error floor 是否依赖任务域、错误结构与 panel 组成，并区分该结果与所有 AI 监督形态之间的外推边界。
- Last checked: 2026-08-30T14:00:29 · refined
- Next: clip+compile arXiv 2607.10139 进入 raw/source，保留 v3 的任务域、model panel 与 shared-error 字段，供后续可回溯复核
- Retry: new-source:arxiv-2607.10139

### CR-004 · Agent Observability 上界随层级变化
- Status: ready
- Priority: P1
- Claim: Agent observability 的结构层可枚举、行为层只能竞速、意图层不应被当作可直接观测对象。
- Gap: Boundary
- Evidence: `raw/20260608-connector-observability-directory.md`、`raw/20260819-google-ai-evals-inspect-skill.md`；Anthropic 三案一手 URL（browsecomp / mythos / Opus 4.5 system card，待 clip）；[OpenAI HF 事件](https://openai.com/index/hugging-face-incident-and-the-road-ahead/)；[OpenAI 第三方评测](https://openai.com/index/third-party-cyber-evaluations-involving-openai-models/)；[Google DeepMind AI Control](https://deepmind.google/blog/securing-the-future-of-ai-agents/)（均待 clip）
- Evidence goal: 取得逐案事前阻断或 coverage/recall 数据，区分“仪器化闭包”的架构承诺与真实污染向量覆盖的实证。
- Last checked: 2026-08-30T15:00:33 · refined
- Next: clip+compile Google DeepMind AI Control 一手材料；核查运行时路径闭包、逐案同步阻断或 coverage/recall 实测数据
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
| P0 | Agent 安全 Topic 建设 | 用现有安全簇构建一个稳定 Topic 骨架；不由 recompile 执行 |
| P0 | 验证器危机研究线 | 按独立性四轴、证据覆盖/解释能力与 reference integrity 建立矩阵，再 clip AgentJudgeBench、Anthropic 三案与 Astra 官方材料 |
| P0 | 劳动经济学实证 | 用已编译 Economic Index 与新增一手数据建立校准骨架 |
| P1 | MCP 无状态转折 | clip 2026-07-28 规范与 NSA 指南后更新 MCP Entity |
| P1 | AI 时代设计方法论对照 | 至少补两份其他实验室设计负责人访谈再判断共识 |
| P2 | Topic 与复核队列代谢 | 处理无承载 Entity 簇和疑似重复项，不继续制造新定理 |

## 开放探索候选

| ID | 候选问题 | 当前判断 | 证伪方向 | 下一步 |
|---|---|---|---|---|
| EX-001 | 验证器独立性是否是目标、证据、执行、时间四轴的最弱轴瓶颈？ | 现有材料分别支持四轴，但尚无同一任务上的受控区分；synthesized | 跨家族单轴变化即可稳定消除多类相关漏报，或单轴失效仍能完整保障 | clip+compile arXiv 2604.07650，建立字段矩阵 |
| EX-002 | 独立性之外，证据覆盖与证据解释是否构成验证的第二个必要门？ | AJ-Bench 将信息取得、状态验证、过程验证分开测量；现有四轴模型尚未把“看见关键状态”和“正确使用证据”从独立性中拆出；synthesized | 在同一任务、同一模型与同一访问权限下，跨家族/独立性变化无法稳定改善漏报，或静态低覆盖验证与可交互验证表现相当 | clip+compile AJ-Bench，建立“静态/可交互 × 同族/跨族”矩阵；与 EX-001 合并判定边界 |
| EX-003 | Facilitator agent 能否在缺少人类隐藏信息的条件下校准“何时升级、升级给谁、给什么上下文”，而不制造新的监督盲区？ | 选择性委派研究把路由器定义为必须定位“人类优于 Agent 的区域”的 rejector；已核读但未剪藏的一手研究提示隐藏特征、误校准和消息 framing 都会改变升级质量；synthesized | 找到 observable-only 路由在分布漂移、专家能力差异和人类负载变化下与 human-context/oracle 路由等效的部署级证据，或主动升级对漏报、过载和人类判断无显著影响 | clip+compile 校准与 selective delegation 一手研究，寻找部署级 proactive escalation case；与 CR-004 / EX-002 对照 |
| EX-004 | 在验证器模型/目标独立性与证据覆盖之外，reference integrity（真值来源、语义等价、版本同步与呈现方式）是否构成独立必要门？ | AgentJudgeBench、ABC、GeneBench、AcquaBench 与 tau3 修复共同把问题收窄为 oracle/source-lineage gate：目标可辨识、来源不污染、规格/expected action 可回链；不是第五个模型独立性轴，仍待控制 EX-001/EX-002 后验证独立残差；refined | 同任务随机化无 reference/正确 reference/语义等价 reference/错误 reference 后，裁判错误、校准和排序对 reference 不敏感；或差异完全由已有目标耦合/证据覆盖解释 | clip+compile AgentJudgeBench、ABC、GeneBench、AcquaBench、OpenAI coding audit、tau3 task fixes、ELT-Bench-Verified；建立 reference owner—semantic equivalence—version—interface—lineage 字段矩阵；与 EX-001/EX-002 合并判定边界 |

## Source 需求队列

| 优先级 | 目标 | 当前缺口 | 触发行动 |
|---|---|---|---|
| P0 | EU AI Act 首轮罚款官方决定 | €47M 三案系单链互引二手叙事（法律基础矛盾、无官方决定原文），需官方决定/一手披露判定真伪 | clip → 核对 CR-001 |
| P0 | Anthropic 三起评测事故 | 已联网核读一手来源（browsecomp/mythos/system card），未进入 raw/source | clip+compile → CR-006 |
| P0 | OpenAI 评测越界披露 | HF 事件及 UK AISI/Irregular 两起第三方评测尚未进入 raw/source | clip+compile → CR-006 |
| P0 | 评测逃逸加固后反例 | 缺独立部署级“加固后逃逸归零”或“同一失配仅发生一次”的记录；受控 SandboxBench 不足 | new-source → CR-006 |
| P0 | arXiv 2604.07650 行为纠缠框架 | 已定位但未 clip/compile | clip → compile → CR-003 / LLM-as-a-Judge 激励共压 flag |
| P0 | Apple《Nine Judges, Two Effective Votes》 | 已联网核读一手页面，未进入 raw/source | clip+compile → CR-003 |
| P0 | arXiv 2607.10139《LLMs as a Jury》 | 已联网核读一手预印本，未进入 raw/source；报告跨模型 verifier 的共享错误下界 | clip+compile → CR-003 |
| P0 | 验证器独立性四轴对照 | 现有材料分散覆盖目标/证据/执行/时间，缺目标操纵、共同污染和版本新鲜度的同任务对照 | clip+compile → EX-001；优先寻找激励隔离、独立实现和旧版检测率案例 |
| P0 | AJ-Bench 环境感知验证基准 | 已核读一手预印本，报告 155 个任务、516 条轨迹、工具交互与四类失败；尚未进入 raw/source，需核查其访问、状态/过程验证与 FPR/FNR 字段 | clip+compile → EX-002 |
| P0 | Human-AI Teaming Through the Lens of Calibration | arXiv 2606.10906 已核读但未进入 raw/source；需提取 rejector 定理、人类隐藏特征与不可约 excess risk 条件 | clip+compile → EX-003 |
| P0 | 选择性预测的校准失效 | PMLR 333（2026）多模态 ICU 研究显示聚合指标会遮蔽按类别误校准；需提取 per-class calibration、deferral 与 expert load 结果及任务边界 | clip+compile → EX-003 |
| P1 | 人类-路由消息效应 | arXiv 2112.06751 显示 deferral status 与 model prediction 的组合会改变人类准确性；需核对 messaging、human-in-loop 指标与外推边界 | clip+compile → EX-003 |
| P1 | 主动升级的部署级长程案例 | 缺 facilitator/triage agent 同时报告漏升级、误升级、专家负载、上下文传递和漂移复核的公开纵向数据 | new-source → EX-003 |
| P0 | AgentJudgeBench reference 对照 | 已联网核读一手预印本，尚未进入 raw/source；需提取 GT/无 GT/corrupted-GT 条件、过度锚定样例、human validation 与合成数据边界 | clip+compile → EX-004，并与 EX-001/EX-002 共用字段表 |
| P0 | OpenAI coding evaluation audits | 已联网核读两份官方材料，尚未进入 raw/source；需提取题面、测试、gold patch、低覆盖、独立人审与训练污染的归因字段 | clip+compile → EX-004 |
| P0 | Agentic Benchmark Checklist | 已核读一手论文，尚未进入 raw/source；需提取 task/outcome validity、ground-truth 审查、语义等价、环境冻结与污染控制字段 | clip+compile → EX-004 |
| P0 | GeneBench target identifiability | 已核读 OpenAI 一手技术报告，尚未进入 raw/source；需提取可恢复目标、可辨识性审查、prompt-grader mismatch 与 trace audit 字段 | clip+compile → EX-004 |
| P0 | AcquaBench success provenance | 已核读一手预印本，尚未进入 raw/source；需提取 CLEAN/GOLD/SHAM 目标替换、来源暴露、冻结配置与成功归因字段 | clip+compile → EX-004 |
| P0 | tau3 task fixes | 已核读官方修复记录，尚未进入 raw/source；需提取错误 expected action、任务歧义、不可行约束与修复前后 pass^1/pass^4 | clip+compile → EX-004 |
| P0 | SWE-bench Verified oracle 质量审查 | 已联网核读官方材料，尚未进入 raw/source；需提取规格、测试、环境和三次独立标注如何改变可评估样本 | clip+compile → EX-004 |
| P0 | PatchDiff 行为等价复核 | 已联网核读 ICSE 2026 一手论文，尚未进入 raw/source；需提取 test-pass、行为差异、人工确认错误与 developer patch 非唯一真值的边界 | clip+compile → EX-004 |
| P0 | ELT-Bench-Verified benchmark audit | 已联网核读一手论文，尚未进入 raw/source；需提取 ground-truth error、脚本误报、人类 agreement 和修正前后排名 | clip+compile → EX-004 |
| P1 | 真实 Agent trace 的语义等价与 reference 版本 | 缺同一生产任务上“结构不同但结果等价”的 reference、版本变更和独立裁决记录 | new-source → EX-004 |
| P1 | reference 呈现方式的因果对照 | 缺把正确 reference、错误 reference、只给 rubric 和不展示 reference 随机化的 live-agent judge 研究 | new-source → EX-004 |
| P0 | 劳动经济学硬数据 | Ramp 与 Dallas Fed 一手材料未入库 | clip + compile |
| P1 | OTel GenAI 正式规范 | 稳定性与语义边界缺官方时间线 | clip/compile → CR-004 |
| P1 | Google DeepMind AI Control / live monitoring | 官方材料已定位 coverage、recall、响应时间与异步/同步阻断边界，缺逐案阻断或覆盖率实证 | clip/compile → CR-004 |
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
| 2026-08-31T13:03:27 | 真值参考完整性与锚定效应 | refined | 补充一手材料把 EX-004 收窄为 oracle/source-lineage gate：目标可辨识、来源污染、expected action/规格回链与版本完整性；它不是第五个模型独立性轴，仍待与 EX-001/EX-002 做受控拆分。 |
| 2026-08-31T12:02:57 | Facilitator 主动升级的校准瓶颈 | new_gap | 选择性委派把“何时叫人”变成 rejector 的二阶校准问题；人类隐藏信息、误校准和消息 framing 都能造成漏升级或改变人类判断；新增 EX-003，暂不升级稳定页。 |
| 2026-08-31T11:22:38 | 验证器独立性与证据覆盖 | refined | AJ-Bench 将信息取得、状态验证、过程验证分开，且工具调用、工具结果解释、证据充分后的推理仍分别失败；“独立性”不能替代“证据覆盖/解释能力”，新增 EX-002，暂不升级稳定页。 |
| 2026-08-30T15:00:33 | Agent Observability 上界 | refined | 将“结构层可枚举”限定为已声明且被记录的接口/事件目录；只有运行时可达路径被权限、隔离和日志闭包覆盖时才转为有效 observability。 |
| 2026-08-30T14:00:29 | AI 监督 AI 共模误差下界 | refined | arXiv 2607.10139v3 具体给出跨家族 verifier panel、七个 benchmark 与逐域 shared-error floor：数学接近 0，GPQA 0.030、MMLU-Pro 0.143；换 generator 后仍复现，Claim 收窄为任务与 verifier 条件下的边界命题。 |

## 思考日志索引

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
