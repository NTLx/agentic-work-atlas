---
type: research-agenda
title: "Agentic Work Atlas 研究议程"
created: 2026-05-22
updated: 2026-08-24T22:01:19
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
- Evidence: `raw/2026-eu-ai-act-compliance-autonomous-agents.md`；现有材料不是执法记录
- Evidence goal: 找到首轮正式执法、罚单或具有强制效果的官方决定；只有规则生效不足以 strengthened。
- Last checked: 2026-08-24 · no_delta
- Next: 外部搜索欧盟委员会及成员国监管机构的一手执法记录
- Retry: now

### CR-002 · Agent 数据过度收集具有系统性
- Status: ready
- Priority: P1
- Claim: Agent 的数据过度收集来自任务代理架构，而不是单一产品或单一厂商的实现失误。
- Gap: Counterexample
- Evidence: `raw/20260618-mosaicleaks-privacy-agent.md`、`raw/How we contain Claude across products.md`、`raw/20260518-zero-trust-for-ai-agents.md`、`raw/20260616-why-is-meta-destroying-its-engineering.md`、`raw/20260714-context-collapse-2-when-emails-instruct.md`
- Evidence goal: 找到权限范围相近但能长期保持数据最小化的 Agent，或跨厂商重复出现的同类失效。
- Last checked: 2026-08-24 · strengthened
- Next: 在仓库外搜索已部署的 privacy-aware agent 系统（PA-DR 生产应用或其他 privacy-by-design 框架）
- Retry: now

### CR-003 · AI 监督 AI 存在共模误差下界
- Status: ready
- Priority: P0
- Claim: 即使使用不同模型家族，AI 监督 AI 仍存在不可消除的共模误差下界。
- Gap: Evidence
- Evidence: `raw/20260713-agentic-misalignment-summer-2026.md`、`raw/20260330-reward-hacking-equilibrium-finite-evaluation.md`
- Evidence goal: 找到跨模型监督的错误相关性或干预前后变化；理论同构和角色共识不计。
- Last checked: 2026-08-24 · strengthened
- Next: 搜索 ensemble judge / multi-model jury 的误差相关性实证数据，量化共模残差来源分解
- Retry: now

### CR-004 · Agent Observability 上界随层级变化
- Status: ready
- Priority: P1
- Claim: Agent observability 的结构层可枚举、行为层只能竞速、意图层不应被当作可直接观测对象。
- Gap: Boundary
- Evidence: `raw/20260608-connector-observability-directory.md`、`raw/20260819-google-ai-evals-inspect-skill.md`
- Evidence goal: 比较规范能稳定枚举的 span/状态与只能通过评估推断的行为或意图，明确三层边界。
- Last checked: 2026-08-24 · refined (reasoning)
- Next: 对照两个 raw 的观测对象、声明能力和失败模式
- Retry: now

### CR-005 · AI 采纳侵蚀专业能力再生
- Status: ready
- Priority: P0
- Claim: 组织从 AI 获得局部效率收益的同时，会把专业能力再生成本外部化到整个职业共同体。
- Gap: Counterexample
- Evidence: `raw/20260731-tragedy-cognitive-commons-ai-expertise.pdf`、`raw/20260730-lenny-tech-workers-ai-sentiment-noam-segal.md`
- Evidence goal: 找到高 AI 采纳但入门训练、独立验证能力和专家补充率长期不降的组织或职业。
- Last checked: 2026-08-24 · refined (mixed)
- Next: 在现有 raw/source 中寻找明确保护学徒期或提升独立验证能力的反例
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
| P0 | EU AI Act 首轮执法 | 只有规则生效与二手解释，缺官方执法事件 | clip → CR-001 |
| P0 | Anthropic 三起评测事故 | 已联网核查但未进入 raw/source | clip + compile → CR-006 |
| P0 | 跨模型监督相关误差 | 缺独立模型组合的误差相关数据 | clip/compile → CR-003 |
| P0 | 劳动经济学硬数据 | Ramp 与 Dallas Fed 一手材料未入库 | clip + compile |
| P1 | OTel GenAI 正式规范 | 稳定性与语义边界缺官方时间线 | clip/compile → CR-004 |
| P1 | Agent 隐私对照 | 缺跨厂商同权限口径对比 | clip/compile → CR-002 |
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
| 2026-08-24T22:01 | AI 监督 AI 共模误差下界 | strengthened | 跨模型误标率：同质 62-86%、异质 1-14%；残差不可消除，来源是训练目标/价值观结构性共享。 |
| 2026-08-24T21:01 | Agent 数据过度收集结构性 | strengthened | MosaicLeaks 证明任务性能训练系统性增加泄漏；跨厂商均出现数据过度收集；PA-DR 可缓解但无 deployed 反例。 |
| 2026-08-24T17:00 | 反馈真空病理 | refined (reasoning) | 将”惊奇”载体从身体修正为公开性，但外部搜索失败；未增加证据，稳定页写入已回迁 Research。 |
| 2026-08-24T16:00 | 工具性收敛弱压力 | refined (reasoning) | 三条件模型降为机制搜索线索；能力被视为使能变量，仍缺独立实证。 |
| 2026-08-24T15:00 | 元满意化阈值 | no_delta | 产生多组 synthesized 解释但无新证据，不进入稳定 Wiki。 |

## 思考日志索引

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
