---
type: source-summary
title: "Token 经济转点：OpenClaw、Hermes 到本地自研的 Agent 进化之路（硅谷101 E249）"
source_raw:
  - "[[20260819-valley101-e249-token-economic-pivot]]"
created: 2026-08-21
updated: 2026-08-21
tags:
  - source-summary
  - token-economics
  - valley101
  - agent-infra
  - singularity
evidence_level: medium
claim_type: mixed
---

# Token 经济转点：OpenClaw、Hermes 到本地自研的 Agent 进化之路（硅谷101 E249）

> 来源：硅谷101 E249，泓君 × 张宏江 × 黄东旭，2026-08-19，87 min。**证据定级 medium**：三位嘉宾都是头部从业者/投资人，所述案例与数据有一手经验支撑；但强主张（「奇点已至」「Token 拐点已到」「Fable 5 绝对智能碾压」）多为定性判断与个案，缺少跨场景对照。**claim_type: mixed**——嘉宾叙述 + Agent 综合判断。

## 编译摘要

### 1. 浓缩

- **核心结论1**：2026 年是 Token 经济从「Maxing」转向「Efficient」的拐点，但**不是因为 AI 热潮退烧，而是工程纪律追上来了**。三个事件共同击碎了 Token Maxing 的合理性假设——GPT-5.5 / DeepSeek V4 / Fable 5 让「无脑用最强模型」变成「在合适环节用合适模型」
  - 关键证据：Uber 4 个月烧完全年 AI 预算、Meta 计划限员工 Token、Stripe 内部警告 Opus 4.8 成本（拐点已到的市场信号）；同时 Fable 5 让东旭「烧了 10 亿 Token 都搞不定的问题被一次精准解决」（单模型能力跨过工程阈值）
- **核心结论2**：**强单模型在最难问题上可碾压多 Agent 蜂群**（Fable 5），但「Agent 动力学」——多 Agent 互相挑刺、上下文互补——在广度任务和次强模型场景下仍不可替代。基础设施层机会大于终端应用
  - 关键证据：东旭把 Fable 5 投入卡住的多 Agent 讨论立刻解锁；张宏江「超级模型改进会向下传导至蜂群」；清华论文「3 个臭皮匠超过 1 个诸葛亮」（看似矛盾，但适用条件不同）；东旭投资分层原则——不投终端应用，投数据平台 / Memory / Observability / Agent-Native Cloud / FDE
- **核心结论3**：**杰文斯悖论在 Agent 时代成立**——单位 Token 价格年降 10x，但 Agentic Loop 带来 100x+ 增长，多 Agent 网络叠加更高阶 Loop，市场反而扩大；行业利润可能从「发电机」（模型层）转向「电网」（Agent-Native Cloud 调度层）
  - 关键证据：东旭 Claude/OpenAI API 消耗 + ARR 双涨；张宏江「成熟技术 + 价格下降 = 市场更大」；To B 走蒸汽机模式（先工厂后家庭）；日 `$300` vs 工程师日成本 = 清晰账目；本地 DeepSeek V4 Flash 全功率 `~$1/天` 电费解锁新工作负载（CVPR/NeurIPS 论文批量总结）

### 2. 质疑

- **关于「拐点已到」的质疑**：嘉宾叙述把市场转向归因于「Fable 5 跨过能力阈值」，但前向市场信号（Uber 烧完全年预算、Stripe 警告成本）本身可能只是 token 涨价期的局部反应；2026 Q4-2027 Q1 是否真正出现「Token Maxing → Token Efficient」结构性转折尚需横截面数据验证。
- **关于「Fable 5 绝对智能碾压」**的质疑：东旭「10 亿 Token vs 一次精准解决」是个案叙事，缺少 eval-on-eval 的对照证据；多 Agent 蜂群在该问题上失败的原因可能是 prompt / harness 设计问题，而非「模型能力不足」。清华「3 臭皮匠 > 诸葛亮」的论文结论与「超级模型碾压」看似矛盾，实际适用任务特征不同——但嘉宾未做精确定义区分。
- **关于「奇点已至」**的质疑：张宏江以「学习能力超人类」定义奇点是**自设定义**（自设约束）。如果换用 Gödel machine（自改进系统）作为 AGI 标准（东旭的立场），则远未到达。AGI 标准的选择直接决定结论，**这不是事实判断而是框架选择**。
- **关于「db9 1 人 3 个月 `$10M ARR`」**的质疑：原文用「潜在」二字，ARR 是 projected 不是 realized；ROI 推算没扣除前期研发成本与失败风险。属于个案，不可推广。
- **关于「OpenClaw 标志 Agent 元年」**的质疑：东旭和 Peter 关系密切，叙事上对 OpenClaw 评价偏高；OpenClaw 在企业级稳定性问题上承认未解决（memory、config）；「工程师而非科学家做出一周 Agent」更可能是工程巧合而非范式信号。
- **关于「本地模型 `~$1/天` 电费」**的质疑：Mac Studio 电费低是因为模型本身够小（30 Token/s 是有限吞吐）；如果对比 4×H100 集群，本地模型经济学优势收窄。「宽带比喻」类比有局限——Token 不是带宽，而是延迟敏感型资源。

### 3. 对标与旁逸

### 3a. 对标（跨域类比）

- **Token Maxing → Token Efficient 的拐点 ↔ 云成本优化（FinOps）成熟**：2015-2018 年云迁移潮后，企业经历了类似的「账单失控 → 可观测性 → 单位经济优化」三阶段（综合判断）。当前 Agent 时代重演同一剧本：先爆发性实验 → 再单位经济学。当前知识库 [[Agentic-Workflow-Token-Efficiency]] 与 [[Token-Supply-Chain]] 已经在追踪这一弧线，本期节目强化了「拐点已到」的时点判断。
- **「Fable 5 绝对智能碾压多 Agent」 ↔ 单专家 vs 委员会（Asch / Surowiecki）**：社会心理学早有「群体智慧」研究——任务是否可分解、个体是否独立、是否有多样性来源决定群体能否超过最强者（综合判断）。本期的「3 臭皮匠 > 诸葛亮」与「Fable 5 碾压」看似矛盾，实际是任务可分解性维度上的不同位置。
- **「本地模型 `$1/天` 电费」 ↔ 拨号 → 宽带的网络经济学**：嘉宾自带的类比准确——带宽扩容解锁新工作负载（视频通话、TikTok），Token 降价解锁新工作负载（批量论文总结、24/7 Agent）。但**只有当价格跨过「用途发现阈值」时**才会出现新市场，与 [[Jevons-Paradox]] 的微观机制一致。
- **「行业利润从发电机转向电网」 ↔ 电力公用事业演化**：通用目的技术（GPT）通常经历「专有发电 → 电网调度」两层利润结构（综合判断）。当前大模型层（发电）的高利润可能随 Token 降价收窄，而 [[Agent-Infra|Agent 基础设施]] / Agent-Native Cloud（电网）成为新利润中心——可对标 1900-1930 年美国电力行业的演化。
- **「Raft / Slock 频道式 Agent 协作」 ↔ 微服务通信的轻量化回归**：Raft 用「频道」而非共享 runtime context 做 Agent 间通信，与微服务放弃共享数据库、转向事件流（Kafka）有结构同构（综合判断）。暗示：随着 Agent 数量增长，「共享内存式编排」（如 LangGraph）会被「消息总线式编排」取代。

### 3b. 旁逸（跨域洞察）

- **「养龙虾」（迭代 Agent 学习用户数字足迹）↔ [[Agentic-Speculation|Agent 推测]] vs 真实代理**：嘉宾把「养龙虾」定位为 Agent 过滤而非完全代理——这是 [[Agent-Containment|Agent 收容]] 的一种隐式实践：让 Agent 替你**接收信息**而非替你**做决定**。这种「数字助理而非数字代理」的中间形态，是当前 Agent 工程中最被低估的工作流设计模式（综合判断）。
- **「Gödel machine 自改进系统」 ↔ 元学习 / AutoML 演进**：东旭对「真正 AGI」的 Gödel machine 标准并非空想——它对应学界 [[Sample-Efficiency]] 与 AutoML 的研究方向，但工程上始终卡在「安全自改进」的护栏问题上。当前所有「自改进」Agent（OpenClaw、Hermes Skills 蒸馏）都不是真正的 Gödel machine——它们是人类辅助下的局部优化（综合判断）。
- **「删生产库 vs 信任 AI」** ↔ [[Agent-Ergonomics|Agent 人体工学]] / 错误代价不对称：东旭自报删库事故但继续高强度使用 Agent——这种「事故-反思-继续」的循环，是 [[Harness-Engineering|Harness 工程]] 的核心动力学。信任不是建在「AI > 人类」宣称上，而是建在「自运行系统」的可恢复性上（综合判断）。

### 3c. 约束（边界分析）

- **「Agent-Native」判断标准的硬约束**：去掉 AI 后系统不能跑、成本上涨 1000 倍才算 Agent-Native——这条标准隐含一个硬约束：**模型能力必须稳定**。如果每次升级都破坏向后兼容，「Agent-Native」反而成为负债。本期嘉宾讨论未触及此点，是 [[Agent-Native]] 概念的一个待补盲区。
- **「Token 价格年降 10x」是软约束**：依赖三个不可控因素——(1) 硬件摩尔定律继续（物理硬约束），(2) 模型厂商维持价格战（商业软约束），(3) 美国对中国芯片出口管制不进一步升级（地缘硬约束）。任一变化都会打破这一速率。
- **「超级模型碾压多 Agent」是任务-条件依赖**：不构成普适规律。本期嘉宾未给精确定义区分，建议跟踪清华论文与 Fable 5 后续 eval 数据。
- **「奇点已至」是自设约束**：完全取决于 AGI 标准的选择。把它当作事实陈述会误导组织决策。

## 关联概念

### 直接引用 / 强关联
- [[Token-Maxing]] — 本期节目把 Token Maxing 重新定义为「目的性 maxing（投入）vs 排行榜刷榜（浪费）」，与既有 entity 的「成本失控」框架形成对照
- [[Agentic-Workflow-Token-Efficiency]] — Token Efficient 拐点的工程层面落地
- [[Token-Supply-Chain]] — Token 从采购到消费的治理框架，与本期「observability 投资机会」对应
- [[Jevons-Paradox]] / [[Jevons-Paradox-for-Knowledge-Work]] — 本期嘉宾直接调用此概念论证 Agent 时代总消耗上升
- [[Agent-Native]] — 东旭提出可操作的判断标准（去掉 AI 后能否运行 / 成本是否涨 1000 倍）
- [[Agent-Harness]] / [[Harness-Engineering]] — OpenClaw / Hermes / Raft 都是 Harness 层实践
- [[Agent-Observability]] — 东旭投资原则「Token 花在哪了」直接对应
- [[Agentic-Memory-Dosage]] — OpenClaw 「memory 是持续痛点」的对应概念
- [[Forward-Deployed-Engineer|FDE]] — 张宏江投资地图中的明确落点（Microsoft 6000 人 Frontier Company）
- [[Agent-Infra]] — Agent-Native Cloud / Memory / Sandbox 都属此层

### 旁逸关联
- [[Agent-Containment]] — 「养龙虾」= Agent 过滤而非完全代理
- [[Agent-Ergonomics]] — 「删库后继续使用」的信任建立循环
- [[Sample-Efficiency]] — Gödel machine 自改进系统的学界对应
- [[AGI-Economics]] — 「行业利润从发电机转向电网」的利润结构演化

### 待补盲区
- **OpenClaw** — 本期节目把它定位为「Agent 元年标志」，值得建独立 entity（当前未在 wiki 中）
- **Hermes / Raft** — Nous Research 与钱宇超（Kimi CLI）的 Agent 产品，独立 entity 待评估
- **Token-Efficient（vs Token Maxing）** — 本期节目暗示 Token-Efficient 是新阶段标签，与 Token Maxing 形成二阶对照；可在 comparison 页面 `Token-Maxing-vs-Token-Efficient` 中沉淀
