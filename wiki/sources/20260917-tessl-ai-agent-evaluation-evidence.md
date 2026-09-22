---
type: source-summary
title: "AI Agent Evaluation Starts With Evidence"
canonical_url: "https://tessl.io/blog/ai-agent-evaluation-starts-with-evidence"
raw_state: index
original_raw_file: "20260917-tessl-ai-agent-evaluation-evidence.md"
original_body_sha256: "6a2e588059dbf6447420cc0a68752f826c05bf6410a53d069ca9fddd7855d526"
indexed_at: "2026-09-22"
created: 2026-09-22
updated: 2026-09-22
tags:
  - source-summary
  - agent-evaluation
  - verification
  - observability
evidence_level: medium
claim_type: mixed
source_locator:
  - "Why Did I Test Against S3 Itself?：S3 behavior oracle 与约 1,500 tests"
  - "Why 100 Percent Coverage Was The Wrong Target：coverage gaming"
  - "Edge Cases / Never Ignore Flaky Tests：风险发现与 flaky discipline"
  - "What Can Tests Not Tell You? / Why Did Observability Matter So Much?：testability、trace 与 type constraints"
  - "The Human Is Part Of The Feedback Loop：多信号 evidence loop"
---

# AI Agent Evaluation Starts With Evidence

## 编译摘要

### 1. 浓缩

- **核心结论 1：Agent evaluation 的核心不是单一分数，而是一条由多个独立信号构成的 evidence loop。**
  - 关键证据：作者最终列出 test oracle、edge-case discovery、flaky-test discipline、traces、performance checks、security review、type-system constraints 和 human judgement；这些信号共同回答“系统是否在收敛到更好状态”。
- **核心结论 2：真实系统行为比文档或 coverage 指标更适合作为 Agent 的反馈基线，但 oracle 本身也需要解释。**
  - 关键证据：作者用真实 S3 行为作为 oracle，构建约 1,500 个兼容性测试；同时指出 S3 的 eventual consistency 会让测试需要 retry，说明 oracle 不等于 specification。追求 100% coverage 时，Agent 会生成技术上提高覆盖率但不提升信心的 trivial tests。
- **核心结论 3：人类在反馈回路中的稀缺角色是决定“什么值得怀疑、什么风险需要暴露、什么信号还缺失”。**
  - 关键证据：作者发现自己比 Agent 更擅长从文档怀疑零长度、极端长度等 edge cases；稀有 bug 没有 reproduction 时 Agent 常猜修复，有 trace/repro 后才明显更可靠；架构与安全也不能由 tests 自动决定。

### 2. 质疑

- **关于 S3 oracle 的质疑**：复制现有协议天然拥有外部 reference behavior，这比原创系统更容易建立 oracle；该模式不能直接迁移到没有已知正确行为的产品和研究任务。
- **关于规模的质疑**：350k 行 Rust、约 5,000 tests/2 分钟是作者个人项目/演讲语境中的实践数据，没有独立代码质量审计或与人工团队的对照。
- **关于 human-in-loop 的质疑**：作者强调保持理解失败模式，但没有量化人在 loop 中的时间成本，因此不能从本案推出最优人工介入比例。
- **关于“测试说谎”的质疑**：真正问题不是测试本身，而是测试选择、oracle、coverage proxy、flakiness 和观测盲区；因此不能简化为“tests 不可信”。

### 3. 对标与约束

- **与 [[Agent-Verification]] 对标**：该来源提供了“oracle 独立性 + risk-directed tests”的具体工程形态：通过测试只有在 oracle 和风险选择合理时才构成证据。
- **与 [[Agent-Observability]] 对标**：trace 的价值不是日志更多，而是为稀有失败建立 reproduction 与 post-state evidence；若系统不暴露内部信号，测试面本身就受限。
- **与 Goodhart 风险对标**：让 Agent 追 100% coverage 会诱导它优化代理指标而非信任目标，是 verification metric gaming 的直接案例。
- **硬约束**：无法观测的状态不能被测试充分覆盖；没有 reproduction 的 rare bug 会显著扩大 Agent 猜测空间。
- **综合判断**：成熟 Agent eval 应被设计成“证据组合问题”而不是“评分问题”——任何单一指标都可能被优化或误读，可信度来自多种信号的交叉约束与人类风险判断。

## 证据边界

- 本文是 Justin Cormack 的一手工程经验总结，不是受控实验。
- 数字主要描述特定 S3-compatible object storage 项目，适合支持机制判断，不适合外推通用生产率。
- 作者同时指出 tests、observability、types、安全 review 各有不同覆盖面，因此不应把任何一项升级为充分条件。

## 关联概念

- [[Agent-Verification]]
- [[Agent-Observability]]
- [[Verifiable-Agent-Engineering]]
- [[Human-Governor-Agent-Operator]]
