---
type: entity
title: Skills-as-Products
aliases:
  - Skills as Products
  - 技能即产品
  - Agent Skills Governance
definition: "把 agent skill 当长期维护的产品而非一次性文档治理的方法——标准化目录（SKILL.md/OWNERS/EVAL.yaml）+ check-in CI 管线 + 持续评估（on-submit 与每周，2x2 矩阵度量 accuracy×efficiency uplift）+ 责任到人（skill owner 应对 API 变化与质量退化）"
created: 2026-08-13
updated: 2026-08-13
evidence_level: medium
claim_type: mixed
tags:
  - agent-skills
  - governance
  - eval
related_entities:
  - "[[Skill-Chains]]"
  - "[[Skill-Internalization]]"
  - "[[Thin-Harness-Fat-Skills]]"
  - "[[Validation-Pipeline]]"
  - "[[Agent-Verification]]"
  - "[[Progressive-Disclosure]]"
  - "[[Model-Context-Protocol-MCP]]"
source_raw:
  - "[[20260803-google-agent-skills-build-test-scale]]"
  - "[[20260812-github-ai-first-contributors]]"
  - "[[20260819-google-ai-evals-inspect-skill]]"
---

# Skills-as-Products（技能即产品）

> [!definition] 定义
> **Skills-as-Products** 是 Google Agent Skills（2026-08）的核心立场："a skill is a living product, not a one-off document."——把 agent skill 当作需要长期维护、评估、归属的产品来治理，而非写一次就完的指令文档。这是 skill 从开发资产变成产品资产的治理框架。

## 标准化目录（Anatomy）

```
{skill-name}/
├── SKILL.md       # Required: 主指令 + frontmatter 元数据
├── OWNERS         # Required: skill 维护者（内部）
├── EVAL.yaml      # Required: 评估 prompt 套件 + rubrics（内部）
├── reference/     # Optional: 技术文档与 schemas
├── scripts/       # Optional: 可执行辅助脚本
├── assets/        # Optional: 静态资源
└── _internal/     # Optional: 测试 mocks（内部）
```

架构原则：**优先引用 remote MCP tools**（obtain 内置 auth 和 IAM 治理），必要时才退到 CLI/API；公开发布通过自动化 export 规则剥离内部资产。

## 质量治理机制

### Check-in CI/CD（每次提交）
- Linter：frontmatter / 行数 / 目录布局 / 命名规范
- Link checker（推荐 lychee）：消灭 404 与幻觉链接
- AI-assisted checklist：校验指令结构模式与 guardrail

### 持续评估（on-submit & weekly）
- **On-submit**：作者必须提供显式 prompt 套件 + 评分 rubrics，内部先验证
- **Weekly**：全库定时回归，catch API/model/harness 变化导致的退化
- **度量维度**：accuracy（响应质量/任务完成率）× efficiency（token 数 + 完成时间）
- **对照法**：对比 agent 有/无 skill 的表现，跨多 agent 框架重复跑取统计显著 → 2x2 矩阵判定是否带来可测 uplift

### Ownership 责任制
- Repo maintainers：库健康 / CI / 架构标准
- Skill owners：长期维护（API 变就更新、eval 发现退化就修）
- 作者支持：内部 authoring skills + 基于 ADK 的多 agent 自批判循环

## 关键数据点

- Google Agent Skills 启动即获 15,000+ GitHub stars（生态热度，非质量证据）
- 2x2 矩阵（accuracy × efficiency）是 skill 价值的判定标尺
- DevRel Skills 并行项目把内部流程（内容转换/SEO/内部报告）编码为 skill

## 前提与局限性

- **重治理成本**：OWNERS/EVAL.yaml/CI/每周回归/跨框架统计面向库级多团队协作；单项目/小团队 ROI 未论证——这是平台方预算，不是使用者预算
- **作者偏差**：写 skill 的人同时写"有/无 skill"对照的 eval prompt 与 rubric，作者评自家 skill
- **依赖漂移规律**：skill 会随 API/model/harness 变化而腐烂，持续 eval 是必须而非可选
- **MCP 攻击面**："remote MCP 优先"把 auth/IAM 外包给 server 端，但 MCP server 是新攻击面（tool 注入/权限放大），文章未谈安全模型

## 关联概念

- [[Skill-Chains]] — 链式组合是 skill 之上的 workflow 形态
- [[Skill-Internalization]] — 吸收而非安装，是 skill 产品质量的消费侧
- [[Thin-Harness-Fat-Skills]] — skill 是 fat skills 的治理载体
- [[Validation-Pipeline]] — skill eval 是验证管线在指令资产域的实例
- [[Agent-Verification]] — with/without 对照是验证命题的资产域应用
- [[Progressive-Disclosure]] — description 预扫描 + 按需装载是渐进式披露的工程化
- [[Model-Context-Protocol-MCP]] — skill 优先引用 remote MCP 与 [[Skills-as-Products|技能质量]] 绑定