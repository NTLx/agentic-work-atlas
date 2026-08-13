---
type: source-summary
title: "Turn one giant AI-generated pull request to a reviewable stack"
source_raw:
  - "[[20260804-stacked-prs-giant-ai-generated]]"
created: 2026-08-13
updated: 2026-08-13
tags:
  - source-summary
  - stacked-prs
  - reviewability
  - agent-generated-prs
evidence_level: medium
claim_type: mixed
---

# Turn one giant AI-generated pull request to a reviewable stack

> 来源：GitHub 官方工程博客（2026-08-04），作者 Julia Muiruri，介绍 GitHub 的 stacked pull requests（`gh-stack` CLI + skill）。**evidence_level 取 medium**：操作命令可复现（gh stack init/add/push/submit/rebase/sync）、机制描述清晰，但主体是教程/演示口径（shopping assistant 示例），无真实团队长期使用的生产率/合并时间对比数据；Gartner 50% 是第三方预测引用。

## 编译摘要

### 1. 浓缩
- **核心结论1：巨型 AI PR 制造"难审查 vs 难维护"两难，coding agents 放大而非消除它**——大型特性塞进一个 1,000+ 行 PR 难审查（reviewer 被"长的 AI 描述"劝退），拆成手工小 PR 链则要手动同步与解冲突难维护；Gartner 预测 2028 各 SDLC 阶段 50% 生产力增益，但"agents can't take away the choice of how you structure your pull requests. They amplify the need to make it."案例：一个购物助手加产品搜索的提示，几分钟产出一个 1,721 行 diff（数据模型+种子数据 / API 路由+验证 / 客户端连接+UI+empty/fallback/error 状态混在一起）。
  - 关键证据: "one ginormous 1,000+ line diff"；"I'll review this later" 的搁置反应；1721 lines 的具体数字。
- **核心结论2：Stacked PRs = 分解为依赖链栈，每层单一关注点、CI 对统一栈基评估**——把巨型 PR 按逻辑分层（data → API → wiring → UX）拆成栈，每层限定单一关注点、小到能在审查者脑中容纳，并自然承接上一 PR 已审上下文；CI 与合并规则针对**栈基（stack base）**评估；可为每层分配不同审查者受众（data owner / API owner / UI owner）。
  - 关键证据: L1 `feat/catalog-data` → L2 `feat/search-api` → L3 `feat/chat-grounding` → L4 `feat/grounded-ui` 依赖链；每层配不同 agent（Data modeler / Backend / Frontend）；"Review bottom-up to build on the predetermined checkpoints"。
- **核心结论3：反馈沿依赖链向上传播，级联 rebase 是维护机制**——底层修复后，`gh stack sync` 从 origin 拉取、对底层之上的每个分支级联 rebase、推送并同步 PR 状态，无需手工 cherry-pick；Web 端 rebase 有隐藏成本：committer 被重置为点击者、产生的 commits 不签名，对签名提交强制的团队是 silent-breaking 操作，文档推荐终端执行 `gh stack rebase && gh stack push`。
  - 关键证据: "Some branches in this stack have diverged and must be rebased" + "Unable to merge as a stack" 阻止合并；"the change ripples upward without anyone touching layers two, three, or four by hand"；栈地图（stack map）在栈内一键跳转导航。

### 2. 质疑
- **关于"结论1"的质疑**：四个独立关注点的拆法（data/API/wiring/UX）是教程作者的主观设计，不保证对所有 feature 可分解——依赖链一旦非纯线性（交织耦合），级联 rebase 的冲突成本会非线性上涨；"reviewer 被劝退"是演示叙事，无对照数据证明单 PR 与 stack 的合并时间/反馈质量差异。
- **关于"结论2"的质疑**：stack 的**总轮次成本**未量化——每层单独过 CI、单独审查往返，多层叠加的总 CI 时间与审查开销高于单 PR；且每层"green"只在合并前对栈基成立，中间层单独合入后其 base 漂移需重新验证，文章未讲多层 review + merge 的编排细节。小团队/单人项目管理栈本身的复杂度可能吞掉收益。
- **关于"结论3"的质疑**：级联 rebase 由 `gh-stack` 自动执行，同样可能产生未签名提交——"Web rebase 不签名"的警告只是位置差异，真正的修复是签名集成，文档未给出；`gh stack sync` 自动 rebase 在冲突时会需要人工介入，其失败模式与处理未展开。
- **关于证据的质疑**：无真实团队长期使用数据；"1721 行"是单案例演示；Gartner 50% 是引用非验证；stack 生态依赖 `gh-stack` 扩展与 GitHub 平台支持，非 GitHub 环境的可迁移性存疑。

### 3. 对标
- **跨域关联1（综合判断）**："stack = 依赖链上的可审单元"是 [[Agent-Unit-of-Work]] 的"工作单元粒度"控制参数在 **review 维度**的实例化——把 unit of work 从"交给 agent 的执行粒度"细化到"给 reviewer 的审查粒度"，是同一组选择（大小/覆盖/交接/验证/边界）在审查侧的复现。
- **跨域关联2（综合判断）**：每层不同 owner 审查 = [[Agent-PR-Review]] 的"审查分工 = 关注点匹配"扩展；"自顶向下读上下文、自底向上审查"对应 bounded context / 分层模块化审查传统（Unix 管道哲学、微服务故障域）。
- **跨域关联3（综合判断）**：`gh stack sync` 级联 rebase 把静态分支的冲突管理变成 agent 可执行的确定命令，是 [[Git-Fluent-Agents]]"agent 掌握高级版本控制"的具象；Web rebase 改 committer/去签名是 [[History-Rewriting]] 风险的平台级实例。
- **跨域关联4（综合判断）**："agent 不会替你选 PR 结构，只会放大选择的需要"与 [[Agent-Harness]] / [[Human-Owns-Output]] 的"agent 放大但方向由人定"同源；是 [[Generation-Verification-Asymmetry]] 在协作层的表述——生成变便宜，审查/结构化的责任反而更重。
- **约束分析（3c）**：硬约束——reviewer 的认知容量有限，大 diff 必然劝退（人类注意力是世界规律）；软约束——是否拆分、按什么维度分层、每层配谁的审查是团队自设；自设约束风险——stack 工具的签名/平台依赖是工程债务，非 GitHub 环境需另行评估。

### 关联概念
- [[Stacked-PRs]]
- [[Git-Fluent-Agents]]
- [[Agent-PR-Review]]
- [[Agent-Generated-PRs]]
- [[Agent-Unit-of-Work]]
- [[Agent-Harness]]
- [[Human-Owns-Output]]
- [[Generation-Verification-Asymmetry]]