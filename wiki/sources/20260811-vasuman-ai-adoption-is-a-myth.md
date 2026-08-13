---
type: source-summary
title: "AI Adoption is a Myth — vas (Varick Agents CEO)"
source_raw:
  - "[[20260811-vasuman-ai-adoption-is-a-myth]]"
created: 2026-08-13
updated: 2026-08-13
tags:
  - source-summary
  - ai-adoption
  - agent-rollout
evidence_level: medium
claim_type: mixed
---

# AI Adoption is a Myth — vas (Varick Agents CEO)

> 来源：X post（2026-08-07，@vasuman，Varick Agents CEO，149 万 views）。**证据定级 medium**：一线企业 AI 实施者的现场观察、机制密度高，但属单条推文经验证言、样本量小、且作者公司（Varick）恰好销售"把 AI 塞进后台"服务——利益结构与库内已有 `20260719-if-ai-is-so-great-why-isnt-it-working`（同公司 Daniel Kornum 材料）一致，结论需与其服务目录对照看待。

## 编译摘要

### 1. 浓缩

- **核心结论1**: 组织内 AI 使用恒呈 **barbell 分布**：5-10% power users（天天用、建 skill、当 evangelist）、20% 每天用几次但用得差、70% 几乎不用；**即使完美 rollout 也如此**——某 exec 签 8 位数 license 后约 10% 的人烧掉 90% 的 token
  - 关键证据: 非技术企业 ops org（数千人）推 Claude Cowork 后"节奏完全一样，领导问 why"；"dashboards count as adoption, but nothing got faster——两者同时为真"；其余 90% 按 top decile 用法消费 → 花费约 10x，`$10M` 承诺变 `$100M`。
- **核心结论2**: **Adoption 指标是神话**——它把"技能连续谱"折叠成二元 yes/no（"这月登录了吗？">"这年登录了吗？"），于是出现"88% 组织在至少一个职能用 AI、却只有 6% 的 EBIT >5% 来自 AI"（McKinsey 2025）的悖论；"adoption is binary, skill is a spectrum"
  - 关键证据: MIT NANDA 的 GenAI Divide（5% 集成试点榨出百万价值、其余 95% 无 P&L 影响）；99.9% 企业只追踪登录/使用率，度量的是比"用得多熟、每 token ROI 多少"容易得多的问题；训练员工的不同答案（"哪 15% 需要模型判断、哪 85% 只需确定性代码"）每家公司都不同。
- **核心结论3**: 对策四件套——(1) 训练当**诊断**而非补救（暴露谁是 top slice）；(2) 给顶部切片一个"发布场所"（共享 skill 库：每个 skill 可发布、排名、被安装——唯一能把一个人的突破变成可分享物的机制；power users 愿用 edge 换 status）；(3) 其余大多数人**把 AI 塞进后台**（找出最重复流程，在 Salesforce/NetSuite/Dynamics 里 build agents，人变成 approve/reject/edit 接口人，如 AP analyst 90% 发票流程自动化）；(4) 汇报口径从 adoption 改为"工作的 手动/混合/全自动化份额"

### 2. 质疑

- **关于样本量**: 单条 X post + 少量现场案例（一家非技术 ops org、一位 8 位数 exec），无系统数据支撑"每个组织都是 5-10/20/70"。barbell 分布作为组织常态是强断言，当前证据是 N≈2 的经验观察，其与 `[[AI-Developer-Power-User-Gap|Power-User-Gap]]`（Cursor 大样本幂律）的合流是综合判断而非本篇原文事实。
- **关于利益结构**: Varick 销售 exactly "在用户既有系统后台 build agents" 服务——结论三"把 AI 塞进后台"正是其服务目录，激励结构需标注（与 07-19 Kornum 材料同源自利，咨询/部署公司"诊断后对照自己的处方"）。"训练无价值、后台之外无解"的强排他主张尤其需保守使用。
- **关于二元化的反批评**: Vas 批评 adoption 指标二元化，但他自己的 barbell（5-10/20/70）同样是离散快照；低估了工具快速改进对 skill floor 的抬升（Claude Cowork 等实用性上升会移动 20% 与 70% 的边界），也把"用得好"固定为静态手艺而非可培训技能。
- **关于与主线距离**: 极近——直接回答"AI 如何进入真实组织并沉淀为能力"（采用机制、度量错位、后台化部署），与 MIT NANDA 5%、McKinsey 88/6 的断裂互为微观机制解释。

### 3. 对标

- **与 [[The-GenAI-Divide]] 的机制补全**: GenAI Divide 解释了"高采用低转化"的宏观断裂，本材料给出断裂的**组织内机制**——adoption 度量的二元化 + 技能谱系的分层。原文事实层面两者是独立来源，机制层面形成闭合：高采用率（88%）与低转化（6%）可以同时为真，因为被度量的是登录而非技能。
- **与 [[AI-Developer-Power-User-Gap]] 的组织级推广**: Cursor 报告证明使用者内部的产出幂律（P99 = 46x P50）；本材料把同一结构推广到"是否在用 / 用得好不好"的组织全章（非开发者 70% 不用）。两个实体合成：AI 价值高度集中在少数人与少数工作流上。
- **与 [[Standard-AI-Product-Adoption]] 的"后台化"机制化**: 已有实体把标准产品路径列成"高频工作流 + 机器可读流程 + 人类升级路径"，Vas 给出升级路径的具体形态——AP analyst 从操作者变成 approve/reject 接口人，是 L1/L2 决策链光谱的现场实例。
- **与 [[AI-Deployment-Invisible-Costs]] 的量化锚点**: "完美 rollout 也会把 `$10M` best case 变 `$100M` worst case" 是隐性成本实体最生动的量化——采纳的隐藏成本不是失败试点，而是"所有人都要学 but 大多数人学不会"的推广成本。
- **与 [[AI-Washing]] 的叙事原料**: "88% 采纳"被 board 与厂商引用时，正是二元指标支撑的采纳洗白叙事；本材料提供拆穿它的度量错位论证。

### 关联概念

- [[AI-Adoption-Barbell]]
- [[AI-Developer-Power-User-Gap]]
- [[The-GenAI-Divide]]
- [[Standard-AI-Product-Adoption]]
- [[AI-Deployment-Invisible-Costs]]
- [[AI-Washing]]