---
type: entity
title: Validation Pipeline
aliases:
  - Validation Pipeline
  - 验证管线
  - No Mistakes Pipeline
definition: "将 Agent 产出的 first-pass code 自动推进到 clean PR 的端到端管线——包含意图理解、隔离 worktree、对抗性审查、e2e 验证、证据生成、文档更新和 PR babysitting。核心理念：人类不审 diff，而是通过管线生成的高质量证据做判断。"
created: 2026-06-22
updated: 2026-06-22
evidence_level: medium
claim_type: mixed
tags:
  - agentic-engineering
  - verification
  - code-review
related_entities:
  - "[[Agent-Verification]]"
  - "[[Agent-PR-Review]]"
  - "[[Agentic-Engineering]]"
  - "[[Captain-Mindset]]"
  - "[[Adversarial-Distillation]]"
source_raw:
  - "[[20260620-l8-principal-agentic-workflow]]"
---

> [!definition] 定义
> Validation Pipeline 不是传统 CI/CD（跑测试和 lint），而是将**对抗性代码审查**自动化为管线一环——Agent 在新 context window 中以审查者身份 review 另一个 Agent 的代码，生成证据（截图/视频/日志），并在低风险变更中免除人类审查。

## 管线步骤（No Mistakes 实现）

1. **创建分支 + commit** — 如果不存在分支则自动创建
2. **隔离 worktree** — 在独立 worktree 中执行验证，不影响当前 repo
3. **意图理解** — 分析原始 agent session，理解变更的真实意图
4. **Rebase** — 在最新 remote main 上 rebase 并解决 merge conflict
5. **对抗性审查**（Adversarial Review）— 在全新 context window 中审查代码；明显问题自动修复，有产品影响的歧义问题升级给人类
6. **端到端测试** — 基于原始意图测试变更，**记录证据**（截图/视频/日志）
7. **文档更新** — 自动更新相关文档以反映最新变更
8. **Lint 检查** — 确保无 lint 问题
9. **Push + PR** — 推送分支并创建 PR
10. **PR Babysitting** — 持续监控 PR 直到 merge，处理后续 merge conflict 和 CI 失败

## 关键数据点

- 作者（Kun Chen）日常 ship 40-50 production commits/天，依赖此管线扩展 velocity
- 低风险变更不看 diff——经验证后管线已覆盖人类能发现的问题
- 管线生成 PR 摘要包含：原始意图、变更内容、测试方式、管线发现的问题及修复
- 风险评估（risk assessment）指导人类决定审查深度：低风险 → 不看 diff；高风险 → 详细审查

## 前提与局限性

- **依赖隔离环境**：必须在 worktree 中运行，否则验证过程可能影响工作目录
- **对抗性审查可能产生 false positive**：新 context window 的审查者可能误判，需要人类仲裁
- **e2e 测试覆盖率取决于测试基础设施**：如果项目没有好的 e2e 测试框架，管线的验证能力受限
- **证据质量不均**：截图和视频对 UI 变更有效，对后端逻辑变更可能只有日志，证据说服力不一
- **PR babysitting 增加 token 消耗**：持续监控直到 merge 可能消耗大量 tokens，需要设定上限

## 与传统 CI/CD 的区别

| 维度 | 传统 CI/CD | Validation Pipeline |
|------|-----------|-------------------|
| 审查 | 人类审 diff | Agent 对抗性审查 + 人类仲裁 |
| 测试 | 单元测试 + 集成测试 | 基于意图的 e2e 测试 |
| 证据 | 测试通过/失败 | 截图/视频/日志等直接证据 |
| PR 维护 | 人类处理 conflict/CI | 自动 babysitting |
| 人类介入 | 每 PR 必须 | 仅高风险变更 |

## 关联概念

- [[Agent-Verification]] — Agent 自主验证的底层能力，Validation Pipeline 是其系统化实现
- [[Agent-PR-Review]] — Agent 审查 PR 的具体实践
- [[Captain-Mindset]] — 人类从审 diff 转向看证据的角色转型
- [[Adversarial-Distillation]] — 对抗性审查的知识蒸馏原理
- [[Skill-Chains]] — QA skill 约束幻觉是 Validation Pipeline 的轻量版本
