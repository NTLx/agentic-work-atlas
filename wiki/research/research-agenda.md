---
type: research-agenda
title: "Agentic Work Atlas 研究议程"
created: 2026-05-22
updated: 2026-08-29T11:00:51
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
- Evidence: `raw/2026-eu-ai-act-compliance-autonomous-agents.md`；2026-08-02 官方执行公告；首轮罚单一致二手报道（€47M 三案，详见 2026-08-29 日志）
- Evidence goal: 首轮执法实例已定位（strengthened）；剩余为官方一手决定文本核对
- Basis: evidence
- Last checked: 2026-08-29T10:00:53 · strengthened
- Next: clip AI Office 首轮罚款官方公告核对 €47M 三案细节；核对后 CR-001 证据目标达成，收敛或转执法扩散观察
- Retry: new-source:AI-Office-first-fines-official

### CR-002 · Agent 数据过度收集具有系统性
- Status: ready
- Priority: P1
- Claim: Agent 的数据过度收集来自任务代理架构，而不是单一产品或单一厂商的实现失误。
- Gap: Counterexample
- Evidence: `raw/20260618-mosaicleaks-privacy-agent.md`、`raw/How we contain Claude across products.md`、`raw/20260518-zero-trust-for-ai-agents.md`、`raw/20260616-why-is-meta-destroying-its-engineering.md`、`raw/20260714-context-collapse-2-when-emails-instruct.md`；[Microsoft 官方 least-privilege 模式](https://learn.microsoft.com/en-us/security/zero-trust/sfi/least-privilege-for-ai-agents)
- Evidence goal: 找到权限范围相近但能长期保持数据最小化的部署级 Agent（→weakened），或跨厂商重复出现的同类失效（→strengthened）；两轮外部检索已排除现部署级反例，恢复条件为 EDPB 02/2026 最终版或新反例披露。
- Last checked: 2026-08-29T11:00:51 · strengthened
- Next: clip+compile Microsoft 官方 least-privilege 文档与 EDPB Guidelines 02/2026；反例 Gap 保持开放，待跨厂商新披露后再检索
- Retry: new-source:edpb-guidelines-02-2026

### CR-003 · AI 监督 AI 存在共模误差下界
- Status: ready
- Priority: P0
- Claim: 即使使用不同模型家族，AI 监督 AI 仍存在不可消除的共模误差下界。
- Gap: Evidence
- Evidence: `raw/20260713-agentic-misalignment-summer-2026.md`、`raw/20260330-reward-hacking-equilibrium-finite-evaluation.md`
- Evidence goal: 找到跨模型监督的错误相关性或干预前后变化；理论同构和角色共识不计。
- Last checked: 2026-08-29T00:01:30 · strengthened
- Next: clip 并编译 arXiv 2604.07650；编译通过后评估 LLM-as-a-Judge「激励共压层未经独立实证」flag 收敛，或对 Anthropic mislabeling 残差做 BEIw/CIG 来源分解
- Retry: new-source:arxiv-2604.07650-clipped

### CR-004 · Agent Observability 上界随层级变化
- Status: ready
- Priority: P1
- Claim: Agent observability 的结构层可枚举、行为层只能竞速、意图层不应被当作可直接观测对象。
- Gap: Boundary
- Evidence: `raw/20260608-connector-observability-directory.md`、`raw/20260819-google-ai-evals-inspect-skill.md`
- Evidence goal: 比较规范能稳定枚举的 span/状态与只能通过评估推断的行为或意图，明确三层边界。
- Last checked: 2026-08-29T01:01:23 · refined
- Next: clip+compile Anthropic 三案，用「结构门失效→行为结论误导」预测检验其 eval-escape 是否为门机制失败例
- Retry: new-source:Anthropic-eval-incidents

### CR-005 · AI 采纳侵蚀专业能力再生
- Status: ready
- Priority: P0
- Claim: 组织从 AI 获得局部效率收益的同时，会把专业能力再生成本外部化到整个职业共同体。
- Gap: Counterexample
- Evidence: `raw/20260731-tragedy-cognitive-commons-ai-expertise.pdf`、`raw/20260730-lenny-tech-workers-ai-sentiment-noam-segal.md`、`raw/Learning on the Shop floor.md`
- Evidence goal: 找到第二个"高采纳 + 维持学徒/独立验证"的组织或职业，或验证 Shopify 案例长期性
- Last checked: 2026-08-27 · weakened
- Next: 仓库外搜索第二个高采纳且再生内部化的组织/职业，或验证 Shopify 长期性；无新反例则不重复
- Retry: now

### CR-006 · 评测逃逸是系统性机制而非孤立 harness 事故
- Status: blocked
- Priority: P0
- Claim: 评测环境逃逸率由 harness 缺口、环境漂移与模型能力共同决定，而非少数配置事故。
- Gap: Counterexample
- Evidence: `raw/20260713-agentic-misalignment-summer-2026.md`；Anthropic 三案尚未 clip/compile
- Evidence goal: 比较不同 harness、模型能力和时间窗口下的逃逸分布。
- Last checked: 2026-08-24 · blocked
- Next: clip 并编译 Anthropic 三起评测事故的一手披露
- Retry: new-source:Anthropic-eval-incidents

### CR-007 · 全球南方 AI 跃迁需要制度共演化
- Status: blocked
- Priority: P2
- Claim: 技术形态可以跨代跃迁，但制度能力和本地评价标准无法被完整进口，只能在使用中共演化。
- Gap: Counterexample
- Evidence: 现有 M-Pesa、UPI 与东亚案例只形成半实例，缺 AI 原生纵向材料
- Evidence goal: 找到技术与制度同时外部移植且长期低错配运行的完整反例。
- Last checked: 2026-08-03 · refined (reasoning)
- Next: 补非洲、印度或东南亚 AI 原生生态的一手纵向案例
- Retry: new-source:global-south-ai-ecosystem

## 当前研究焦点

| 优先级 | 焦点 | 下一步最小动作 |
|---|---|---|
| P0 | Agent 安全 Topic 建设 | 用现有安全簇构建一个稳定 Topic 骨架；不由 recompile 执行 |
| P0 | 验证器危机研究线 | clip Anthropic 三案与 Astra 官方材料，校准验证边界 |
| P0 | 劳动经济学实证 | 用已编译 Economic Index 与新增一手数据建立校准骨架 |
| P1 | MCP 无状态转折 | clip 2026-07-28 规范与 NSA 指南后更新 MCP Entity |
| P1 | AI 时代设计方法论对照 | 至少补两份其他实验室设计负责人访谈再判断共识 |
| P2 | Topic 与复核队列代谢 | 处理无承载 Entity 簇和疑似重复项，不继续制造新定理 |

## Source 需求队列

| 优先级 | 目标 | 当前缺口 | 触发行动 |
|---|---|---|---|
| P0 | EU AI Act 首轮罚款官方决定 | 已由一致二手报道定位 €47M 三案，缺官方决定原文 | clip → 核对 CR-001 |
| P0 | Anthropic 三起评测事故 | 已联网核查但未进入 raw/source | clip + compile → CR-006 |
| P0 | arXiv 2604.07650 行为纠缠框架 | 已定位但未 clip/compile | clip → compile → CR-003 / LLM-as-a-Judge 激励共压 flag |
| P0 | 劳动经济学硬数据 | Ramp 与 Dallas Fed 一手材料未入库 | clip + compile |
| P1 | OTel GenAI 正式规范 | 稳定性与语义边界缺官方时间线 | clip/compile → CR-004 |
| P1 | Agent 隐私对照 | 微软官方 least-privilege 模式已定位（待 clip）；EDPB Guidelines 02/2026 最终版未发布 | clip/compile → CR-002 |
| P1 | 专业能力再生反例 | 缺高采纳且训练能力不降的纵向案例 | clip/compile → CR-005 |
| P2 | 全球南方 AI 生态 | 缺本地制度共演化纵向材料 | clip/compile → CR-007 |

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
| 2026-08-29T11:00 | Agent 数据过度收集结构性 | strengthened | 两轮定向反例检索无部署级反例；微软官方 least-privilege 模式确认 agent 默认积累过度权限（permission creep / over-broad tool access）、CSA 命名"Overprivileged by Design"、EDPB 02/2026 把数据最小化引向 agent 决策链每步且多家 DPA 已调查；"而非单一厂商实现失误"获得跨厂商/跨辖区一致性支持。 |
| 2026-08-29T10:00 | AI 评测制度化进入执行期 | strengthened | AI Office 于 2026-08-02 生效后数日内开出首批 €47M 罚单（招聘 €18M/信贷 €14M/零售情绪识别 €15M，案件预建），CNIL 并行 RFI；证据为两条一致二手报道，官方决定文本待核对。 |
| 2026-08-29T01:01 | Agent Observability 上界 | refined | 对照 Connector 仪表盘与 Google evals 两份 raw：结构层=可枚举计数（tool calls/延迟/错误率）、行为层=必须在 baseline 对照下采样竞速（capability/skill 效用无法直接读，只能统计推断）、意图层=只能经结构 flag+行为结局交叉推断（Skill Ingestion Check 失败则测得 baseline 而非 skill 效用）。三层不是并列观测类别：行为推断以通过结构门为前提。 |
| 2026-08-29T00:01 | AI 监督 AI 共模误差下界 | strengthened | arXiv 2604.07650 实测 6 家族 18 模型跨族行为纠缠普遍存在，纠缠度与 judge 过度背书偏误显著相关（ρ=0.64–0.71）；「不同家族⇒监督独立」被实证证伪，机制定位到共享谱系；纠缠感知重加权 +4.5% 验证精度，下界限定于模型间依赖结构层。 |
| 2026-08-27T14:05 | AI 采纳侵蚀专业能力再生 | weakened | 部署级反例 Shopify/River：public-only 公开频道 + Lehrwerkstatt 在高 AI 采纳下把专业再生成本留在组织内部；Claim 由普遍预测收窄为条件命题，仍缺第二个独立案例与纵向验证。 |

## 思考日志索引

- [[2026-08-29]] — recompile CR-003（arXiv 2604.07650 跨族行为纠缠）；recompile CR-004（Connector vs evals 对照：结构层可枚举/行为层竞速/意图层间接，结构门机制）；recompile CR-001（AI Office 首轮 €47M 罚单，制度化执法 strengthened）；recompile CR-002（两轮反例检索无部署级反例，微软/CSA/EDPB 确认过度特权为默认设计，strengthened）
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
