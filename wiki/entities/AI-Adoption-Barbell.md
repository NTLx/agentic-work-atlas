---
type: entity
title: AI-Adoption-Barbell
aliases:
  - AI Adoption Barbell
  - 采纳杠铃分布
  - 组织 AI 分层
definition: "组织内 AI 使用恒呈分层常态（5-10% power users、20% 用得差、70% 几乎不用），且即使完美 rollout 也如此；adoption 指标把技能连续谱折叠成二元 yes/no，造成'高采纳率、无业务影响'的度量错位"
created: 2026-08-13
updated: 2026-08-26
tags:
  - ai-adoption
  - ai-deployment
  - organizational-change
related_entities:
  - "[[AI-Developer-Power-User-Gap]]"
  - "[[The-GenAI-Divide]]"
  - "[[Standard-AI-Product-Adoption]]"
  - "[[AI-Deployment-Invisible-Costs]]"
  - "[[AI-Ready-Organization]]"
  - "[[Agent-Adoption-Curve]]"
  - "[[Forward-Deployed-Engineer]]"
source_raw:
  - "[[20260811-vasuman-ai-adoption-is-a-myth]]"
  - "[[20260530-cursor-developer-habits-report]]"
  - "[[20260825-emerge-enterprise-ai-adoption]]"
---

# AI-Adoption-Barbell（采纳杠铃分布）

> [!definition] 定义
> **AI-Adoption-Barbell** 是组织内 AI 使用呈杠铃状分层的常态：5-10% 的 power users 天天用、会用（skill、连接器、workflow），20% 每天用但用得差，70% 几乎不用。核心断言是**这层分布不因 rollout 质量而消失**——adoption 指标因二元性无法捕获技能连续谱，于是出现"88% 组织在用 AI、但只有 6% 的 EBIT 受影响"（McKinsey 2025）式度量错位。

## 为什么重要

[[The-GenAI-Divide]] 描述了"高采用、低转化"的宏观断口，但未解释断裂为什么存在。Barbell 提供组织内的微观机制：

1. **技能是连续谱、指标是二分**：adoption 记录的是"登录了吗、每周够 5 个 prompt 吗"，而决定业务结果的"用得好不好"是连续谱上很少有人到达的部分。被度量的问题与业务相关的问题脱钩。
2. **用 AI 和用好是两门手艺**：把粗用转精（slop-cannon → refined power user）和让不用的人上手一样难；"至少一半组织永远到不了第二种版本"。
3. **完美 rollout 不改变分布**：某 exec 签 8 位数 license 后，约 10% 的人烧 90% 的 token；若其余 90% 按 top decile 用法消费，花费约 10x——`$10M` 承诺变 `$100M`。

## 关键数据点

- 典型分布：5-10% power users / 20% 用得差 / 70% 几乎不用（N≈2 经验观察，非系统统计）
- 违反直觉：即使完美 rollout，仍约 10% 用户消耗 90% token
- McKinsey 2025：88% 组织在至少一个业务职能用 AI，仅 6% 的 EBIT >5% 来自 AI
- MIT NANDA GenAI Divide：5% 的集成试点榨出数百万价值，其余 95% 无 P&L 影响
- 交叉证据：Cursor 2026 使用数据（使用者内部产出幂律，Gini 0.72-0.77、P99 = P50 的 46x）支持同一分化结构

## 结构性采纳 gap（2026-08，Emerge VC 市场分析）

[[20260825-emerge-enterprise-ai-adoption]] 从供给侧确认并扩展 Barbell：采纳 gap 是**结构的**（激励／流程／数据／治理），不是技术成熟度。

- **个体采纳领先组织采纳**：54% 员工即使用未授权也会用 AI（BCG）；88% 员工工作中用 AI，但仅 5% 是效率提升 >20% 的 advanced users（EY）。Shadow AI（Menlo 报告 +68% 同比）是 Barbell 底部力量的公开显现——员工不等组织 rollout 自己先动。
- **更强模型不收紧 gap**：agents 依赖已重设计的流程、可访问的数据、可运行的治理；"agentic AI 提高能力上限，不降低采纳所需的下限投入"（综合判断详见 source summary）。
- **对策市场分层**：服务端（FDE、流程重设计、Workflow-Transformation-as-a-Service）与 in-workflow enablement 承接 Barbell 的"后台化"路径；人被推向对 agent 的监督（operator → supervisor）。这一判断与现场介入角色（[[Forward-Deployed-Engineer]]）的需求上升相互印证。

## 前提与局限性

- 分布比例来自单条 X post 的现场观察（非独立统计样本），作为"常态"是强断言——与 Cursor 幂律数据的合流是综合判断而非环节证据。
- 来源作者（Varick Agents CEO）销售 background agent 迁移服务，"70% 永远学不会"的悲观主张与其服务目录利益一致。
- 低估了工具改进对 skill floor 的抬升——新一代 agent 工具可能压缩 20%/70% 的比例，barbell 是快照而非固定常数。

## 组织对策（同源主张）

- 训练当**诊断**而非补救：先暴露谁是 top slice。
- 顶部切片给"发布场所"：共享 skill 库（发布、排名、安装），把个人的突破变成可分享物。
- 其余人**后台化**：把 AI 塞进用户已有系统（Salesforce/NetSuite/Dynamics），人退化为 approve/reject/edit 接口（如 AP analyst 90% 发票自动化）——参见 [[Standard-AI-Product-Adoption]] 的升级路径。
- 汇报口径：从"adoption"改为"工作手动/混合/全自动化的份额"。

## 关联概念

- [[AI-Developer-Power-User-Gap]] — 同一分化在"使用者内部产出"上的幂律版本；本实体补"是否在用/用得好不好"的组织层
- [[The-GenAI-Divide]] — 宏观断口的组织内机制
- [[Standard-AI-Product-Adoption]] — "后台化 + 人做接口"是标准产品路径的升级路径形态
- [[AI-Deployment-Invisible-Costs]] — 推广成本（人人要学但多数学不会）是隐性成本主体
- [[Agent-Adoption-Curve]] — 采纳的"谁先用"时间曲线，本实体是其"用得好坏"横截面