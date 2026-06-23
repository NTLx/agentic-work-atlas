---
type: entity
title: Company-Brain
aliases:
  - Company Brain
  - 公司大脑
  - Context Layer
  - 上下文层
  - Organization Brain
definition: "让组织对 Agent 可读的共享上下文层——folder 树结构 + markdown 文件，Agent 可搜索、检索和写回。通过 Capture → Curate → Store → Execute → Experience 循环持续进化，让 Agent 拥有对组织的 20/20 视野。核心指标：Agent 能否在几分钟内产出基于真实数据的个性化提案。"
created: 2026-06-23
updated: 2026-06-23
evidence_level: medium
claim_type: mixed
tags:
  - knowledge-management
  - organizational-design
  - context-engineering
  - AI-native-org
related_entities:
  - "[[Context-Engineering]]"
  - "[[Knowledge-Compilation]]"
  - "[[Progressive-Disclosure]]"
  - "[[LLM-Wiki]]"
  - "[[Skill-Chains]]"
  - "[[Agent-Harness]]"
  - "[[AI-Native-Engineering-Org]]"
source_raw:
  - "[[20260608-become-ai-native-org]]"
---

> [!definition] 定义
> Company Brain 不是数据库或知识库产品的名字，而是一种**组织设计原则**：把公司的一切（策略、会议记录、决策、产出、客户信号）转化为 Agent 可读、可搜索、可写回的 folder + markdown 结构，让 Agent 拥有对组织的 20/20 视野。

## Capture → Curate → Store → Execute → Experience 循环

| 阶段 | 职责 | 实现方式 |
|------|------|---------|
| **Capture** | 从 Slack/会议/邮件/Linear 收集信息 | Cron job 每小时运行 |
| **Curate** | 像图书馆员一样决定什么该留、什么该忽略、什么该触发行动 | Agent 审查 + 规则过滤 |
| **Store** | 存入 Brain（folder 树 + markdown 文件） | Agent 可搜索、检索、写回 |
| **Execute** | Agent 利用 context 执行工作（skill chains、prototypes） | 基于 context 的个性化产出 |
| **Experience** | 客户体验 → 信号回流（买更多？流失更快？） | 市场反馈回流进系统 |

## Traces / Exhaust（决策痕迹）

执行过程中产生的决策、探索和中间产物是"cutting room floor"素材，必须回流进 Brain：

- 为什么做了这个决策
- 探索了哪些替代方案
- 哪些 skill 被触发了、为什么
- 客户反馈的原始信号

这些不是"文件坟墓中无人查看的文档"，而是可复用知识。Brain 将这些 traces 转化为 lessons、artifacts 和更新后的 skills。

> **关键约束**: 不能让 Agent 的未审核产出直接回流进 Capture。必须经过人类判断（Experience 层），确保只有"好"的 context 进入系统。

## 关键数据点

- LCA (Late Checkout Agency) 的 Brain 支撑提案 skill chain：从过去会议记录中提取个人化时刻（如 Maya 的唱片店隐喻），几分钟内生成品牌化提案微站
- "20/20 Vision": Agent 拥有对组织的完美视野——不需要发 14 条消息或等几天才能回答"谁两周前入职了"
- Context bootstrapping: 对新项目，通过 Mobbin MCP（设计模式库）+ 外部设计系统 + 自建 skills 快速建立初始 context
- Brain 是 folder 树结构，不是向量数据库——markdown 文件可被人直接阅读和编辑

## 与其他知识系统的区别

| 维度 | Company Brain | LLM Wiki | 向量数据库 |
|------|--------------|----------|-----------|
| 结构 | Folder 树 + Markdown | Entity/Topic/Comparison | Embedding 向量 |
| 可读性 | 人 + Agent 双可读 | Agent-first | Agent-only |
| 写入者 | 人 + Agent | Agent（人审查） | 自动索引 |
| 回流机制 | Experience 层过滤 | 回填检查 | 无 |
| 目的 | 组织 20/20 视野 | 知识编译和复用 | 语义检索 |

## 前提与局限性

- **质量衰减风险**: 随着信息累积，curator 如何防止 context 腐烂？这与 [[Context-Rot]] 问题同构
- **捕获覆盖度**: 如果关键对话发生在 Brain 未覆盖的渠道（如微信、电话），context 会有盲区
- **Curator 质量**: 如果 curator 过于激进地过滤，可能丢失有价值的弱信号
- **安全与权限**: Brain 包含敏感信息（客户数据、内部策略），需要精细的访问控制
- **冷启动成本**: 从零搭建 Brain 需要大量前期投入（连接工具、定义 schema、训练 curator）
- **不是向量数据库**: Folder + markdown 结构不支持语义搜索，检索依赖 Agent 的搜索能力

## 关联概念

- [[Context-Engineering]] — Company Brain 是 Context Engineering 在组织层面的应用
- [[Knowledge-Compilation]] — Brain 的 Store 阶段本质上是持续的知识编译
- [[Progressive-Disclosure]] — Agent 按需检索 Brain 中的信息，不一次性加载
- [[LLM-Wiki]] — Wiki 是 Brain 的一种实现形式，但 Brain 更强调组织级覆盖面
- [[Skill-Chains]] — Skill chain 的产出质量直接依赖 Brain 的丰富度
- [[AI-Native-Engineering-Org]] — Company Brain 是 AI Native Org 三层架构的基础层
