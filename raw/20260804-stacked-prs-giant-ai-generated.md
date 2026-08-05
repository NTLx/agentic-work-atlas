---
type: raw
source: "https://github.blog/engineering/turn-one-giant-ai-generated-pull-request-to-a-reviewable-stack/"
author:
  - "Julia Muiruri"
published: "2026-08-04"
created: "2026-08-05"
tags:
  - clippings
  - coding-agent
  - stacked-prs
  - reviewability
  - github
  - agentic-engineering
---

# Turn one giant AI-generated pull request to a reviewable stack

> Source: [github.blog/engineering/turn-one-giant-ai-generated-pull-request-to-a-reviewable-stack/](https://github.blog/engineering/turn-one-giant-ai-generated-pull-request-to-a-reviewable-stack/)
> Author: Julia Muiruri (@juliamuiruri4)
> Date: August 4, 2026
> Reading time: 9 minutes
> Tag: stacked pull requests

## 引言：巨型 PR 的两难

开发者面对大型特性时，要么把它塞进一个巨大的 pull request（难审查），要么拆成小 PR 链但要手工同步并解决冲突（难维护）。

> Both options have trade-offs. One is hard to _review_, while the other is hard to _maintain._

编码代理（Coding agents）让生产力提升——Gartner 预测到 2028 年各 SDLC 阶段将获得 50% 生产力增益——但"they can't take away the choice of how you structure your pull requests. They amplify the need to make it."

## 案例：为购物助手添加产品搜索

向代理发出一个添加产品搜索的提示，几分钟后回来审查。一个 PR 通常包含：

- 新的数据模型及其种子数据
- API 路由及其验证
- 客户端连接、UI 以及 empty/fallback/error 状态

> …all of this and more in one ginormous 1,000+ line diff.

**典型流程：** 创建 feature branch → 分配给编码代理 → 拿到代码和测试初稿 → 阅读代码 → 手动验证行为 → 推送并打开 PR → 检查 CI → 自审 → 请求 reviewer。

结果：审查者看到 1,721 行变更，被"长的 AI 描述"劝退——"I'll review this later." 巨型 PR 因此搁置，反馈质量下降，合并变慢。

## GitHub Stacked Pull Requests

**核心原则：分解（decomposition）。** 不再追求单一 PR 完成整个 issue，而是将特性拆解为逻辑分层，并识别依赖链。

巨型 PR 变成一个**栈（stack）**：由若干更小、逻辑有序的 PR 组成，每个 PR 限定**单一关注点（single concern）**，小到能在审查者脑中容纳，并自然承接上一个 PR 已审过的上下文。

### 准备工作

1. **设置栈基（stack base）**——CI 和合并规则都将针对栈基进行评估。
2. **识别核心基础工作单元**，放在栈底，依赖性工作逐层向上叠加。

### 栈结构示例（购物助手）

| Stack Layer (L#) / Branch | What to ship | Depends on |
|---|---|---|
| L1 (`feat/catalog-data`) | 带种子数据、验证和数据访问模块的类型化 catalog | main（栈基） |
| L2 (`feat/search-api`) | 已验证的 `/api/products/search` endpoint | `feat/catalog-data` |
| L3 (`feat/chat-grounding`) | Chat 调用 API 并基于真实产品数据作答 | `feat/search-api` |
| L4 (`feat/grounded-ui`) | 产品引用卡片 + 状态 | `feat/chat-grounding` |

独立关注点变得清晰：**data、API、wiring、UX**，可为每层分配不同的审查受众。Data 由 **data owner** 审，UX 由 **UI owner** 审。

### 安装 CLI 与 Skill

```bash
gh extension install github/gh-stack
gh skill install github/gh-stack
# 或
npx skills add github/gh-stack
```

### 各层使用的代理

| 层 / 分支 | Agent |
|---|---|
| L1 (`feat/catalog-data`) | Data modeler agent |
| L2 (`feat/search-api`) | Backend agent |
| L3 (`feat/chat-grounding`) | Frontend agent |
| L4 (`feat/grounded-ui`) | Frontend agent |

最后要**确认 CI 已存在**——每层都会针对栈基运行检查。

## 逐层构建的纪律

### Layer 1：Data catalog foundation

1. 调用 **Data Modeler agent**
2. 代理用 `gh init stack` 初始化栈并设置首分支 `feat/catalog-data`，基线为 main
3. checkout、工作、运行验证
4. `(All checks == green) ? commit the layer : Iterate`

> 审查者关注点：_Are the types correct? Is the data validated? Is the query helper safe?_ Period.

### Layer 2：Product search API

1. 调用 **Backend agent**
2. 代理用 `gh stack add` 在 L1 之上加入新层 `feat/search-api`，基线为 `feat/catalog-data`
3. checkout、工作、运行验证
4. 开发者手动测试 API
5. `(API works && All checks == green) ? commit the layer : Iterate`

> 审查者关注点：_Is input validated? Is the response contract stable? Are error/empty states handled here or pushed downstream?_

### Layer 3：Wire chat to the API

1. 调用 **Frontend agent**
2. 代理在 L2 之上加入 `feat/chat-grounding`，基线为 `feat/search-api`——同时继承 data access 模块和已验证的 API
3. checkout、工作、用 Playwright 运行浏览器测试
4. `(All checks == green) ? commit the layer : Iterate`

> 审查者关注点：_Is every answer tracing back to a real API response? What happens when the API fails or returns nothing?_

### Layer 4：Grounded UI and citations

L3 与 L4 虽作者相同（Frontend agent）但刻意分层——UI owner 不必审查底层数据流，反之亦然。

1. 在 L3 之上加入 `feat/grounded-ui`，基线为 `feat/chat-grounding`
2. checkout、工作、用 Playwright 运行浏览器测试
3. `(All checks == green) ? commit the layer : Iterate`

> 审查者关注点：_Does every citation link back to a real product? Are loading, empty and error states all covered?_

### 提交栈

四个本地分支就绪后：

```bash
gh stack push
gh stack submit
```

每个 PR 顶部出现**栈地图**——一种在栈中各 PR 之间一键跳转的导航。

## 审查与更新栈

栈地图是审查者的指南针：

- **自顶向下阅读** 获取上下文（"哦，所以我们想在聊天界面展示产品卡片"）
- **自底向上审查** 在已确定的检查点上构建

> Review bottom-up to build on the predetermined checkpoints.

### 反馈向上传播

审查 L1 时，Copilot Code Review（CCR）发现两个问题，审查者同意修复。

**开发者回到栈中：** 把反馈交给 L1 的作者（data modeler agent）；应用建议、测试、提交、推送。`feat/catalog-data` 被更新后，问题自然出现：_what does this mean for layers two, three, and four?_

GitHub 提示："Some branches in this stack have diverged and must be rebased"，并显示 "Unable to merge as a stack" 标志以阻止合并。

> **关于 Web 端 Rebase 按钮的警告：** 触发基于 Web 的 rebase 会在 GitHub 服务器上运行，committer 会被重置为点击按钮的人，产生的 commits **不会被签名**。若分支保护要求签名提交，这"一个点击会悄悄破坏流程"。更安全的做法是在终端执行：
> ```bash
> gh stack rebase
> gh stack push
> ```

**向上传播：** 使用一键同步命令：

```bash
gh stack sync
```

该命令会从 origin 拉取，对 `feat/catalog-data` 之上的每个分支执行级联 rebase，推送已 rebase 的分支，并从 GitHub 同步 PR 状态。

> This way, the change ripples upward without anyone touching layers two, three, or four by hand.

所有检查重新运行并通过，栈地图回到一条从 main 到 `feat/grounded-ui` 的干净可合并链。

## 关键论断

1. **分解不是分心，是 reviewer-friendly 的工程纪律**：当 AI 一次性生成 1,000+ 行 diff，巨型 PR 直接压垮 review cycle；stacked PRs 把 PR 化为可审单元，且不丢失依赖链。
2. **CI 必须基于栈基评估**：每层的"green check"必须在统一的栈基（stack base）上跑出来，否则分层无意义。
3. **审查分工 = 关注点匹配**：data owner / API owner / UI owner 各看自己关心的层；同一 agent（Frontend agent）出现在 L3 和 L4 也属合理，因为 UX 与 wiring 是不同的关注点。
4. **Web rebase 的隐藏成本**：committer 重写、未签名——对签名 commit 强制的团队是 silent-breaking 操作，文档直接给出命令行替代。
5. **反馈沿依赖链向上传播**：底层修复通过 `gh stack sync` 级联 rebase 推上去，不需手工 cherry-pick。

## 相关阅读

- [Stacked sessions and pull requests in the GitHub Copilot app](https://github.blog/ai-and-ml/github-copilot/stacked-sessions-and-pull-requests-in-the-github-copilot-app/) — Cassidy Williams
- [Don't stop early: Case-folding source code at memory speed](https://github.blog/engineering/architecture-optimization/dont-stop-early-case-folding-source-code-at-memory-speed/)
- [Tame Dependabot: Group your updates, slow the cadence, keep security fast](https://github.blog/security/supply-chain-security/tame-dependabot-group-your-updates-slow-the-cadence-keep-security-fast/)
- [The cost of saying yes has changed](https://github.blog/engineering/the-cost-of-saying-yes-has-changed/)

## 入门

[Get started with stacked pull requests →](https://docs.github.com/pull-requests/how-tos/stacked-pull-requests)