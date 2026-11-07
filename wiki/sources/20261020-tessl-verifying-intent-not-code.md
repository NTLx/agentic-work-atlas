---
type: source-summary
title: "We stopped reviewing code and started verifying intent"
canonical_url: "https://tessl.io/blog/we-stopped-reviewing-code-and-started-verifying-intent"
raw_state: index
original_raw_file: "20261020-tessl-verifying-intent-not-code.md"
original_body_sha256: "13a71c2e50933aafa7e20b8bf4e0f281742d7dffe427d0e94d5c7674f2e1ba5c"
indexed_at: "2026-11-08T00:00:00+08:00"
created: 2026-11-07
updated: 2026-11-07
tags:
  - source-summary
  - code-review
  - verification
evidence_level: medium
claim_type: mixed
source_locator:
  - "Article header and byline / Ankit Jain, 20 Oct 2026, for AI Native DevCon"
  - "Why scaling code review for AI-generated code didn't work / four-times PR volume and review bottleneck"
  - "Review the intent, not the diff / requirements, acceptance criteria, edge cases, visual and trace evidence"
  - "Mine your PR comments, they're invariants waiting to happen / examples and historical review mining"
  - "Mine your PR comments / suggestion review last 1000 comments and take 20 most repeated; three-month transition scenario"
  - "Code review didn't disappear, it changed shape / Argue, Capture, Codify, Debate, Own"
  - "Author bio / Aviator founder and CEO; guest post hosted by Tessl, not an independently validated Tessl product assessment"
---

# We stopped reviewing code and started verifying intent

> 来源：[Tessl 官方博客（2026-10-20）](https://tessl.io/blog/we-stopped-reviewing-code-and-started-verifying-intent)；作者 **Ankit Jain**（Aviator 创始人/CEO），以 AI Native DevCon 嘉宾身份撰文。2026-11-07 实际读取全文。本文是一个软件工程负责人的团队实践叙述，**不是 Tessl Verifiers 产品独立评测，也不是大样本对照研究**。作者自述的规模及结果按 medium / mixed 处理。

**来源保留边界**：官方原文通过 canonical URL 和章节定位可回查；Wiki 保存原创分析，不复制外部全文。临时 Raw 只用于 Registry 来源登记，original_body_sha256 **只对应此登记记录，不是官方原文正文的哈希**；不能将本页视为全文镜像或独立 Evidence。

## 编译摘要

### 1. 浓缩

#### 核心结论 1：评审的高杠杆点前移到「意图契约」，实现后的审查则核对可复验证据。

- **证据（Review the intent, not the diff）**：作者称团队一年来合并 PR 的量增长约四倍，多数代码由 AI 生成，传统逐行看 diff 的 review 成为瓶颈。一个 400–500 行变更展示的是“做了什么”，但不能稳定说明“本应做什么”；既有 ticket 可能质量差，甚至与开发过程中变化的意图不一致。
- 团队做法是：**生成代码前由高级工程师审阅 acceptance criteria、业务/安全 constraints、edge cases；生成后每个 criterion 附 verdict 与证据**。作者举例 review 五条准则并审查截图、请求 Trace，而不是只阅读 500 行 AI diff。文中称 verdict 为 deterministic，但没有说明所有 verdict 如何实施，尤其未证明 LLM 判定可获得形式化确定性。
- **关键结构**：`intent → explicit acceptance contract → independent checks → captured artifact/trace → reviewer decision → human ownership`。可验证的 acceptance criteria 降低事后从代码反推需求的成本，但不能代替安全推理、代码架构与未知风险审查。

#### 核心结论 2：重复出现的 PR 评论应沉淀为项目不变量，而非长期消耗高级工程师注意力。

- **证据（Mine your PR comments）**：作者把资深审查者反复写出的意见视为隐性团队规范，建议从最近 **1,000 条 review comment** 找最常重复的 **20 类**，转换为适用范围明确、易判断的 invariant：例如涉及币种须用 `Money` type、禁止直接写 users 表、统一 structured logger 禁止 `print`。作者提到团队使用共用 `offer-skill` 解释代码变更。
- **边界**：原文写有 `X our recurring review comments` 等不完整表述，**没有给出实际采样评论总数或转化条数**。1,000/20 是作者的起步建议，不是其团队实际测量的项目规模。文中的“第一个月双轨、第二个月减轻、第三个月审查意图”是转型预期，不应写成有对照组的三个月实证曲线。
- **验证层次**：能由编译器、类型系统、SQL policy、静态 lint 或测试形式化的，应优先用确定性规则；更模糊的语义规则可经验证的 LLM Judge 帮助检查，但其误报、漏报与版本变动必须另外标注。

#### 核心结论 3：Human review 并未消失，而是将人类职能从「阅读每行代码」迁到方案争论、风险裁定和 Oracle 所有权。

- **证据（Code review didn't disappear, it changed shape）**：作者明确提出五步：**Argue**（Agent 之间提前争论方案）、**Capture**（将意图和验收条件写到 PR）、**Codify**（将历史高频 review 评论编码成不变量）、**Debate**（人审核真正重要的决定）、**Own**（决定由谁拥有验证规则）。他称团队不再以逐行 review 为必经环节，code review 不再是交付瓶颈。
- **综合判断**：流程最危险的遗漏恰恰是第五步。假如 Agent 可以连同业务实现一起悄悄放宽验收标准，所有 criteria 都 PASS 也不能证明正确；要保持规则/测试/权限/用户意图的所有权与被审变更适当分离。

### 2. 质疑、反例和适用边界

1. **「不读代码」不能按字面应用到所有风险级别**：安全敏感授权代码、加密、关键会计计算、竞态条件、数据库迁移、重要临床软件等，仍可能需要人工代码级审查、威胁建模、形式化或独立安全审计。原文未证明意图核对在这些领域能替代它们。
2. **Intent 自身可能错或不完整**：错误的验收标准被忠实实现，只会更快生成合规的错误系统。必须让使用者、领域负责人及安全责任人对风险场景有权挑战并批准需求。
3. **规则校准不等于自动判定的正确性**：作者用 deterministic verdict 一词，但没有公开所有判定器、Oracle 保护机制、human label agreement 或误报/漏报率；应区分 CI 执行确定性与评价依据可靠性。
4. **移转而非消除成本**：组织必须支付编写验收协议、维护 invariant register、搭建行为测试/trace 检查、观察生产反馈及解决争议的工作；四倍 PR 吞吐与瓶颈解除由团队自报，未提供投入成本、任务复杂度或质量对照。
5. **同平台不同作者**：这篇是 **Aviator CEO 的 Tessl 客座文章**。既有 [[20261015-tessl-repo-verifiers]] 是 Tessl 团队讲自己产品的语义规则产品说明；两者在「不变量」概念上可互证其工程主张，但不是相互独立的大样本有效性验证。
6. **规则的适用范围有限**：常见评论只覆盖已观察到的错误；未知攻击、跨服务副作用、遗漏权限与运行时依赖仍需不同测试层。绝不能因为标准足够具体，就误判为整个产品风险已受控。

### 3. 对标与约束（跨来源综合判断）

| 工程层级 | 本文新增机制 | 既有 Wiki 对照 | 验收责任 |
|---|---|---|---|
| 需求层 | `Capture` intent / acceptance / constraints | [[Agent-PR-Review]]、[[Plan-as-Agent-Checkpoint]] | 人类需求及风险负责人 |
| 规则层 | 高频 PR 评论 → 版本化 invariant | [[20261015-tessl-repo-verifiers]]、[[Verifiable-Agent-Engineering]] | Oracle owner，禁止同一 PR 静默放宽 |
| 运行层 | 构建、测试、截图、Trace 对应 criteria | [[Agent-Verification]]、[[20261015-meta-forum-ai-native-engineering]] | 独立证据/CI；不能只信模型描述 |
| 终态 | `Argue/Capture/Codify/Debate/Own` 中的 Own | [[Evaluation-Integrity]] | reviewer + domain owner + release approver |

**对 LLM WiKi / ServerFS / n8n 的迁移建议（综合，非作者实施）**：把反复出现的「source URL 未实际读取」「Claim 证据定位缺失」「状态机写入未持久化」「模型产生的成功宣告缺少 ACK」等 review 反馈归类成规范，用 schema lint / 回归测试 / guarded queue transition 优先确定性检查；对少量需语义判断的标准保留人工校准和 protected baseline。该建议**不授权本次修改生产代码或定时任务**。

## 重要判断（Claim / Evidence / Boundary）

- **判断（综合）**：AI coding 提高变更产量时，review 的上游瓶颈可以通过明确的意图协议和受保护的可执行验收转化为稽核，但对高风险变更仍需要人工结构/安全审查。
- **证据**：本文的「Review the intent, not the diff」「Mine your PR comments」「Code review didn't disappear」；结合 [[Agent-Verification]] 已有 Oracle 保护原则。
- **边界**：单团队自报实践，不构成“完全不读代码仍保持质量”的独立因果证据。

## 关联概念

- [[Agent-PR-Review]]
- [[Verifiable-Agent-Engineering]]
- [[Agent-Verification]]
- [[Evaluation-Integrity]]
