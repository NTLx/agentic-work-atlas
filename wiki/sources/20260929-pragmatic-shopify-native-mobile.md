---
type: source-summary
title: "Why has Shopify dropped React Native?"
canonical_url: "https://newsletter.pragmaticengineer.com/p/shopify-native-mobile"
source_raw:
  - "[[20260929-pragmatic-shopify-native-mobile]]"
raw_state: full
created: 2026-10-12
updated: 2026-10-12
tags:
  - source-summary
  - mobile-engineering
  - coding-agents
  - software-architecture
  - verification
evidence_level: medium
claim_type: mixed
source_locator:
  - "Public section 1: Why Shopify chose React Native in 2020"
  - "Public section 2: Still happy five years later"
  - "Public section 3: Why ditch React Native now?"
  - "Public subsection: One engineer, two platforms with AI"
  - "Public subsection: Shared codebases more trivial with AI"
  - "Paywall boundary: section 4 heading immediately followed by ‘This post is for paid subscribers’"
---

# Why has Shopify dropped React Native?

> Gergely Orosz 对 Shopify 从 React Native 转回 Swift/Kotlin 原生开发的分析。当前 canonical 的公开页面只完整开放第 1–3 节：第 4 节标题出现后立即进入付费墙，因此本次编译严格限定在公开部分，不把目录中的 Airbnb、Notion、Kotlin Multiplatform 或后续预测段落当作已读证据。核心转向同时能被 Shopify 2026-09-10 的第一方工程复盘独立核验，但第一方文章只作为交叉核验，不用于补写 Pragmatic Engineer 的付费内容。

## 编译摘要

### 1. Shopify 改变的不是“React Native 好不好”，而是原先架构决策的成本函数

公开部分最重要的历史对照是：Shopify 在 2020 年选择 React Native 的三个主要理由——避免同一 feature 在 iOS/Android 重写两次、提高人才跨栈流动、减少 feature parity 成本——后来确实兑现。到 2025 年 Shopify 仍公开称迁移成功：六个 app 已迁到 RN，跨平台共享实现明显提高 productivity，同时性能和稳定性也达到其目标。

因此 2026 年的回摆不是“过去选错了”。Mustafa Ali 的核心解释是：coding agents 已经能承担足够多的 implementation、translation、testing 和 review，使“双平台实现”不再具有 2020 年同样高的人工成本；而 native 原本就存在的优势——更靠近平台能力、第一方 tooling、更少 framework/dependency layers——仍然存在。

**判断**：AI 不只改变“写代码有多快”，还会改变**软件抽象是否值得存在的经济前提**。一个 abstraction 的价值通常来自：

```text
saved duplicated labor
+ shared semantics
+ talent portability
- abstraction tax
- dependency / debugging / performance cost
```

当 Agent 大幅压低 duplicated implementation / translation labor，原来为了节省人工重复而引入的 abstraction premium 会下降；此时过去合理的架构决策可能需要从 first principles 重算。

这并不推出“AI 时代都应该 native”。更准确的结论是：**architecture choice 应随着 Agent 改变各成本项而重新计算，而不是把过去成功的技术标准永久化。**

### 2. AI 让 duplication cost 下降，但不会让双实现自动保持一致

公开第 3 节转述 Shopify 的经验：同一开发者现在可以借助 LLM 跨 iOS/Android 工作；Agent 可以把一端实现 port 到另一端，也可以长期比较两套实现、发现 feature/behavior gaps。

但 Shopify 并没有因此把 parity 交给“模型觉得差不多”。文中明确描述一个 shared verification test suite：同一套 business-logic tests 同时验证 Swift 和 Kotlin 实现，并且 feature 必须在两个平台通过同一 correctness contract 才能发布；测试还可在 desktop headless 运行，为 Agent 提供快反馈。

**判断**：Agent 使“双实现”重新变得经济，前提不是 translation 变便宜本身，而是组织能把 **shared semantics 从 shared implementation 中剥离出来**：

```text
shared implementation (React Native)
        ↓ Agent lowers duplication cost
separate native implementations
        +
shared specification / behavioral oracle
        +
fast headless verification
```

因此真正被替换的可能不是“共享”本身，而是**共享的层级**：从共享生产代码，迁移到共享 specification、tests、review checkpoints 和 behavioral contract。

### 3. Agent 改写 abstraction boundary，同时把 verification 推成新的 binding constraint

这篇案例非常适合补充 [[AI-Labor-Bottleneck-Shift]]：过去移动端的瓶颈之一是“同一功能写两次”；Agent 把这一 Execute cost 压低后，新的难点变成：如何保证两份实现行为一致、性能不退化、platform-specific 优势被正确利用，并让同一个工程师能安全跨专业栈工作。

也就是说：

```text
旧瓶颈：duplicated implementation labor
            ↓ Agent
新瓶颈：specification + parity verification + platform quality
```

这是比“AI 让工程师写得更快”更具体的瓶颈迁移：**当重复实现成本不再主导决策，架构会倾向移除为了节省人工而存在的中间层，但 correctness contract 的重要性会上升。**

### 4. “一名工程师、两个平台”是角色边界扩张，不是专业知识消失

公开部分引用 Shopify 观察：LLM 使开发者更容易在非主栈贡献代码，团队仍保持一个产品团队而不是重新拆回独立 iOS/Android 团队。这支持 AI 扩大 individual execution surface。

但来源同时强调 native 的价值恰恰来自 platform capability、first-party tooling、rendering/performance control。由此不能推出 Swift/Kotlin、iOS/Android 专业知识不再重要；更合理的是：Agent 降低跨栈 translation cost，让一个工程师可以覆盖更大的 execution surface，而深层 platform judgment 仍决定质量上限。

这与 [[Role-Merging]] 已有“跨界尝试 ≠ 专家消失”的边界一致，因此本轮不再修改该页。

### 5. 12 周重写是 capability existence evidence，不是通用 migration benchmark

公开部分报告 Shop app 已在约 12 周内完成 fully-native rewrite，并要求后续 rebuild 达到或超过原有 performance、stability、accessibility 和 product quality。这证明在 Shopify 的代码库、团队、AI tooling 与 reference implementation 条件下，greenfield/native rewrite 的时间成本已经显著改变。

但它不是一般性的“React Native → native 只需 12 周”基准：

- Shopify 有成熟 RN reference implementation；
- 有大量既有 native/mobile expertise；
- Agent tooling、verification harness 和内部流程并不代表中位团队；
- 公开部分没有提供完整人力、token/compute、返工、缺陷率与长期维护成本。

因此该数字应作为**架构决策的成本曲线发生过实质变化的案例**，而不是迁移工期估算公式。

## 与现有知识的连接

- **[[AI-Labor-Bottleneck-Shift]]**：新增“Agent 会改变 abstraction economics”。被压低的不只是 coding time，还可能是 cross-platform duplication/translation cost；瓶颈随后迁往 shared specification、verification 与 platform quality。
- **[[Agent-Verification]]**：两套 native implementation 共享同一 headless business-logic test suite，是“实现独立、oracle 共享”的工程案例；Agent 可以生成/port 两份实现，但 release contract 应独立于某一份实现。
- **[[Role-Merging]]**：支持 individual execution surface 扩张，但没有新证据证明 specialty 消失，因此只在本 Summary 对标，不扩散修改。

## 证据与访问边界

- Pragmatic Engineer canonical 当前公开到第 3 节结束；第 4 节标题后进入 paid subscriber wall。本次 Raw 是公开内容的有界证据摘要，不含也不重构付费内容，因此保留 `raw_state: full`，不做 index settlement。
- 公开部分中的 Shopify 核心转向、Agent 跨平台 porting、shared tests 与 12-week Shop rewrite 可被 Shopify 官方工程文章交叉核验；但厂商第一方材料同样不是独立 benchmark。
- 文章标题“dropped React Native”容易被读成生态层结论；实际证据只支持 **Shopify 在其当前成本函数下转向 native**，不能推出 React Native、Flutter、KMP 等跨平台方案对其他团队普遍失去价值。
