---
type: entity
title: Stacked-PRs
aliases:
  - Stacked Pull Requests
  - stack
  - 堆叠 PR
definition: "把巨型 pull request 按逻辑分层拆成依赖链栈（stack）的方法——每个 PR 限定单一关注点、CI 对统一栈基评估、可配不同审查者受众；反馈沿依赖链级联传播，专为 AI 生成的大 diff 恢复可审查性"
created: 2026-08-13
updated: 2026-08-13
evidence_level: medium
claim_type: mixed
tags:
  - code-review
  - git
  - agentic-engineering
related_entities:
  - "[[Git-Fluent-Agents]]"
  - "[[Agent-PR-Review]]"
  - "[[Agent-Generated-PRs]]"
  - "[[Agent-Unit-of-Work]]"
  - "[[Agent-Harness]]"
source_raw:
  - "[[20260804-stacked-prs-giant-ai-generated]]"
---

# Stacked-PRs（堆叠 PR）

> [!definition] 定义
> **Stacked PRs** 是 GitHub（2026-08）推广的巨型 PR 拆解方法：把大型特性按逻辑分层（data → API → wiring → UX）拆成一个栈（stack），每个 PR 限定**单一关注点（single concern）**、小到能在审查者脑中容纳，并自然承接上一个 PR 已审过的上下文。CI 与合并规则针对**栈基（stack base）**评估，反馈沿依赖链级联传播。

## 核心机制

### 两难：难审查 vs 难维护
- 巨型 PR（1,000+ 行 / 案例 1,721 行）：reviewer 被"长的 AI 描述"劝退 → 搁置、反馈质量下降
- 手工小 PR 链：手动同步 + 解冲突难维护
- Coding agents 放大选择的需要："they can't take away the choice of how you structure your pull requests. They amplify the need to make it."

### 栈结构（购物助手示例）
| Layer / Branch | What to ship | Depends on |
|---|---|---|
| L1 `feat/catalog-data` | 类型化 catalog + 种子数据 + 验证 | main（栈基） |
| L2 `feat/search-api` | 已验证的 `/api/products/search` | `feat/catalog-data` |
| L3 `feat/chat-grounding` | Chat 调 API 基于真实产品作答 | `feat/search-api` |
| L4 `feat/grounded-ui` | 产品引用卡片 + 状态 | `feat/chat-grounding` |

独立关注点（data/API/wiring/UX）可为每层配不同审查者受众（data owner / UI owner）。

### 工具链
- `gh extension install github/gh-stack` + `gh skill install github/gh-stack`（或 `npx skills add`）
- `gh init stack` → `gh stack add` → `gh stack push` / `gh stack submit` → 栈地图导航
- 反馈向上传播：`gh stack sync` 从 origin 拉取、对底层之上每个分支级联 rebase、推送并同步 PR 状态

### 已知坑：Web rebase
Web 端 rebase 按钮在 GitHub 服务器运行，committer 被重置为点击者、commits 不签名——对签名提交强制的团队是 silent-breaking；文档推荐终端执行 `gh stack rebase && gh stack push`。

## 审查纪律

- **自顶向下阅读**获取上下文（"哦，所以想在聊天界面展示产品卡片"）
- **自底向上审查**在已确定的检查点（checkpoints）上构建
- 底层发现的问题修复后沿链向上传播，无需手工 cherry-pick

## 关键数据点

- 触发场景：AI 生成 1,000+ 行 diff（案例 1,721 行）
- 栈分层：data → API → wiring → UX 四层，每层单一关注点
- 工具：`gh-stack` extension（`gh stack add/push/sync`）

## 前提与局限性

- **总轮次成本未量化**：每层单独过 CI + 单独审查往返，多层叠加开销高于单 PR；小团队/单人项目管理栈的复杂度可能吞掉收益
- **依赖线性假设**：纯线性依赖链才适合级联 rebase；交织耦合的变更冲突成本非线性上涨
- **平台依赖**：依赖 `gh-stack` 扩展与 GitHub 平台，非 GitHub 环境可迁移性存疑；自动 rebase 同样可能产生未签名提交（真正的修复是签名集成，文档未给出）

## 关联概念

- [[Git-Fluent-Agents]] — stack 是 agent 掌握高级版本控制的具象（级联 rebase / sync）
- [[Agent-PR-Review]] — 栈化是巨型 AI PR 的 reviewability 修复；每层不同 owner = 关注点匹配审查
- [[Agent-Generated-PRs]] — AI 生成 1,000+ 行 diff 是 stack 的触发场景
- [[Agent-Unit-of-Work]] — 工作单元粒度在审查维度的实例化
- [[Agent-Harness]] — "agent 放大但结构选择由人定"的编排层含义