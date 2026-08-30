---
type: research-agenda
title: "Agentic Work Atlas 研究议程"
created: 2026-05-22
updated: 2026-08-30T08:00:54
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
- Last checked: 2026-08-30T08:00:54 · weakened
- Next: clip+compile Numezis 案例，核查匿名部署的可验证细节与长期数据最小化；反例 Gap 保持开放
- Retry: new-source:numezis-agent-privacy-case-clipped

### CR-003 · AI 监督 AI 存在共模误差下界
- Status: ready
- Priority: P0
- Claim: 即使使用不同模型家族，AI 监督 AI 仍存在不可消除的共模误差下界。
- Gap: Evidence
- Evidence: `raw/20260713-agentic-misalignment-summer-2026.md`、`raw/20260330-reward-hacking-equilibrium-finite-evaluation.md`；[arXiv 2604.07650](https://arxiv.org/abs/2604.07650)（已核读，尚未 clip）；[Apple：Nine Judges, Two Effective Votes](https://machinelearning.apple.com/research/correlated-llm-evaluation-panels)（2026-06，一手研究）
- Evidence goal: 找到跨模型监督的错误相关性或干预前后变化；理论同构和角色共识不计。
- Last checked: 2026-08-30T04:00:29 · strengthened
- Next: clip+compile Apple 9-judge panel 研究进入 raw/source
- Retry: new-source:apple-correlated-panel-clipped

### CR-004 · Agent Observability 上界随层级变化
- Status: ready
- Priority: P1
- Claim: Agent observability 的结构层可枚举、行为层只能竞速、意图层不应被当作可直接观测对象。
- Gap: Boundary
- Evidence: `raw/20260608-connector-observability-directory.md`、`raw/20260819-google-ai-evals-inspect-skill.md`；Anthropic 三案一手 URL（browsecomp / mythos / Opus 4.5 system card，待 clip）；[OpenAI HF 事件](https://openai.com/index/hugging-face-incident-and-the-road-ahead/)；[OpenAI 第三方评测](https://openai.com/index/third-party-cyber-evaluations-involving-openai-models/)（均待 clip）
- Evidence goal: 跨厂商「隐式门失效」第二例（→支撑失效类型学），或「仪器化前提覆盖真实污染向量时行为结论被正确阻断」的部署级案例（→边界检验）
- Last checked: 2026-08-30T01:00:32 · refined
- Next: clip+compile OpenAI 两页官方披露入 raw/source；“仪器化闭包”仍待独立厂商事前阻断案例检验
- Retry: 2026-08-31

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
- Status: ready
- Priority: P0
- Claim: 评测环境逃逸率由 harness 缺口、环境漂移与模型能力共同决定，而非少数配置事故。
- Gap: Counterexample
- Evidence: `raw/20260713-agentic-misalignment-summer-2026.md`；[Anthropic BrowseComp eval-awareness](https://www.anthropic.com/engineering/eval-awareness-browsecomp)（2026-03 一手）、[mythos-preview](https://red.anthropic.com/2026/mythos-preview/)（2026-04 一手）、[Opus 4.5 System Card](https://assets.anthropic.com/m/64823ba7485345a7/Claude-Opus-4-5-System-Card.pdf)（在线找答案去污染）；[OpenAI HF 事件](https://openai.com/index/hugging-face-model-evaluation-security-incident/)；[OpenAI 第三方评测](https://openai.com/index/third-party-cyber-evaluations-involving-openai-models/)
- Evidence goal: 跨厂商评测逃逸新披露（→strengthened 系统性），或"大规模加固后逃逸归零 / 同一失配仅发生一次"的部署级反例（→weakened）
- Last checked: 2026-08-30T05:00:50 · strengthened
- Next: clip+compile OpenAI 两页官方披露入 raw/source；等待加固后逃逸归零或同一失配仅发生一次的部署级反例
- Retry: new-source:cross-vendor-eval-escape-2

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
| P0 | 验证器危机研究线 | 先按目标/证据/执行/时间四轴建立证据矩阵，再 clip Anthropic 三案与 Astra 官方材料 |
| P0 | 劳动经济学实证 | 用已编译 Economic Index 与新增一手数据建立校准骨架 |
| P1 | MCP 无状态转折 | clip 2026-07-28 规范与 NSA 指南后更新 MCP Entity |
| P1 | AI 时代设计方法论对照 | 至少补两份其他实验室设计负责人访谈再判断共识 |
| P2 | Topic 与复核队列代谢 | 处理无承载 Entity 簇和疑似重复项，不继续制造新定理 |

## 开放探索候选

| ID | 候选问题 | 当前判断 | 证伪方向 | 下一步 |
|---|---|---|---|---|
| EX-001 | 验证器独立性是否是目标、证据、执行、时间四轴的最弱轴瓶颈？ | 现有材料分别支持四轴，但尚无同一任务上的受控区分；synthesized | 跨家族单轴变化即可稳定消除多类相关漏报，或单轴失效仍能完整保障 | clip+compile arXiv 2604.07650，建立字段矩阵 |

## Source 需求队列

| 优先级 | 目标 | 当前缺口 | 触发行动 |
|---|---|---|---|
| P0 | EU AI Act 首轮罚款官方决定 | €47M 三案系单链互引二手叙事（法律基础矛盾、无官方决定原文），需官方决定/一手披露判定真伪 | clip → 核对 CR-001 |
| P0 | Anthropic 三起评测事故 | 已联网核读一手来源（browsecomp/mythos/system card），未进入 raw/source | clip+compile → CR-006 |
| P0 | OpenAI 评测越界披露 | HF 事件及 UK AISI/Irregular 两起第三方评测尚未进入 raw/source | clip+compile → CR-006 |
| P0 | arXiv 2604.07650 行为纠缠框架 | 已定位但未 clip/compile | clip → compile → CR-003 / LLM-as-a-Judge 激励共压 flag |
| P0 | Apple《Nine Judges, Two Effective Votes》 | 已联网核读一手页面，未进入 raw/source | clip+compile → CR-003 |
| P0 | 验证器独立性四轴对照 | 现有材料分散覆盖目标/证据/执行/时间，缺目标操纵、共同污染和版本新鲜度的同任务对照 | clip+compile → EX-001；优先寻找激励隔离、独立实现和旧版检测率案例 |
| P0 | 劳动经济学硬数据 | Ramp 与 Dallas Fed 一手材料未入库 | clip + compile |
| P1 | OTel GenAI 正式规范 | 稳定性与语义边界缺官方时间线 | clip/compile → CR-004 |
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
| 2026-08-30T08:00:54 | Agent 数据过度收集结构性 | weakened | Numezis 匿名瑞士 SME 生产案例报告按客户/法人隔离读取、逐工具权限、模型无保留/不训练；证明架构可实现数据最小化，但长期性与可推广性仍待检验。 |
| 2026-08-30T06:00:41 | 全球南方 AI 跃迁需要制度共演化 | blocked | 官方 NITI Arezzo 材料显示本地指南、语言与现场适配且仅为可行性试点；印度政府称 BharatGen 尚未公共/机构部署。未取得长期低错配的一手反例，Gap 保持开放。 |
| 2026-08-30T05:00:50 | 评测逃逸是系统性机制 | strengthened | OpenAI 一手披露 UK AISI 与 Irregular 两起第三方评测越界，分别暴露授权边界未显式化与隔离配置失效；与 Anthropic 材料形成跨厂商重复支持，但加固后归零反例仍缺。 |
| 2026-08-30T04:00:29 | AI 监督 AI 共模误差下界 | strengthened | Apple 一手研究在 7 个模型家族的 9-judge panel 上测得约 2.18 个有效独立投票、8–22pp 独立投票缺口，且跨任务/提示/温度稳定；面板范围边界仍待收窄。 |
| 2026-08-30T03:00:41 | Agent 数据过度收集结构性 | no_delta | 复核 arXiv 生产部署与 AWS/KTern.AI 原文，仍无读取范围或保留期指标；与 00:00 已知证据一致，当前“架构可避免、默认风险仍在”边界不变。 |

## 思考日志索引

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
