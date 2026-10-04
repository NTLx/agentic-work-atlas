---
type: source-summary
title: "AI coding has made CI a bottleneck, so we reworked ours to keep up"
canonical_url: "https://linear.app/now/ci-bottleneck-reworked"
raw_state: index
original_raw_file: "20260921-linear-ci-bottleneck-reworked.md"
original_body_sha256: "0f532a197c75bcc4a5131652aa5bae91fbbadb865c7f3d10be3cab789020297b"
indexed_at: "2026-10-05T04:21:30+08:00"
created: 2026-10-05
updated: 2026-10-05
tags:
  - source-summary
  - agentic-engineering
  - ci
  - verification
  - developer-infrastructure
evidence_level: high
claim_type: mixed
source_locator:
  - "Opening — agent throughput vs CI validation bottleneck; test-suite growth and wait/runner metrics"
  - "Upgraded infrastructure and tooling — runners, tsgo, AST-only lint"
  - "Optimize the jobs that gate other work — change detection, checkout resilience, critical-path removal"
  - "Reduce repeated setup — base image, filtered installs, cache economics, DB snapshots, batching"
  - "Make test execution more efficient — shard balancing, isolate:false trade-off, agent-skill update"
  - "Improvements that compound across a system — counterfactual ~11 min suite and ~2,000 tests/week"
---

# AI coding has made CI a bottleneck, so we reworked ours to keep up

## 编译摘要

### 1. 浓缩

- **核心结论 1：coding agents 把 verification infrastructure 推上了关键路径；当生成吞吐增长快于 CI 吞吐时，CI 不再只是质量保障层，而成为软件交付系统的 binding constraint。**
  - 关键证据：Linear 报告其测试套件自年初接近四倍增长，但通过系统性 CI 优化把 PR 等待从 6 分钟以上压到约 5 分钟，同时将单测试 runner time 约减半；作者明确把原因框定为 agents 加速代码生产而 validation 没有同比例提速。
  - **判断**：AI coding 的“verification bottleneck”不仅是 reviewer attention，也有纯基础设施版本：runner capacity、critical-path latency、setup overhead、test scheduling 和 flaky/network tails 都会限制 Agent 能多快得到可信反馈。

- **核心结论 2：CI 优化的主要对象不是单个慢 job，而是整个依赖图的 critical path 与重复固定成本。**
  - 关键证据：Linear 将 change-detection 这类小 gate 从约 26 秒 median 降至 8 秒，并把不需要 gate merge 的 cache marker write 移出关键路径；同时通过预装依赖、filtered workspace install、schema snapshot、合并短 checks 等方式消除每个 job/shard 重复支付的 setup cost。
  - **判断**：在高并发 Agent 组织中，验证系统应像生产服务一样做 queueing / critical-path / fixed-cost 分析；“每个检查都更快一点”不一定等于 feedback loop 更快，真正要优化的是 merge path 的 dominators 和重复启动成本。

- **核心结论 3：更快 verification 不能靠削弱 oracle；性能优化本身需要 correctness envelope，并且应被写回 Agent skill。**
  - 关键证据：Linear 把 `isolate: false` 的 module-state sharing 称为 correctness risk 最高的优化之一，只允许明确安全的测试逐文件 opt-in，并补 teardown；不安全的测试继续隔离。由于 agents 已写多数测试，团队进一步更新 agent skills，让新生成测试默认遵守这套性能/隔离约束。
  - **判断**：Agent 时代的 CI optimization 是双目标问题：既要降低 feedback latency / runner cost，又不能让优化改变测试语义。把经过验证的基础设施约束写进 coding-agent skills，是把一次性基础设施知识变成持续生成约束的机制。

### 2. 质疑

- **关于“AI 导致 CI 成为瓶颈”的质疑**：这是 Linear 团队的内部因果解释。文章展示 tests/usage 的增长与 CI 压力，但没有给出 Agent adoption 的时间序列、对照团队或代码变更量的完整分母，因此可以支持“共同发生并形成工程压力”，不能严格证明单一因果。
- **关于总体改进归因的质疑**：runner 迁移、tsgo、lint 重写、checkout、setup、sharding、module sharing 等多项措施叠加；PR wait 的整体改善不能拆成互相独立的 causal contribution。
- **关于成本数字的质疑**：87,000 runner-minutes/月、17% monthly savings 等都依赖 Linear 当时 workload、runner 定价与 monorepo 结构；可用于说明 fixed-cost magnitude，不应外推为通用 ROI。
- **关于 cache 结论的质疑**：`node_modules` cache 比 rebuild 更慢是该仓库 lockfile churn、网络/存储与 filtered install 性能共同决定的局部结果；可迁移的是“测 restore vs rebuild”，不是“不要缓存”。
- **关于隔离优化的质疑**：`isolate:false` 的收益来自共享 module registry，但这正改变测试执行语义。Linear 通过 opt-in/teardown 管风险；其他代码库若状态边界不同，可能产生隐藏的 order dependence 或 false green。
- **关于测试增长的质疑**：每周约 2,000 个新 tests 说明验证工作量快速扩张，但数量本身不等于 evidence quality；如果 Agent 生成大量低判别力测试，CI 可能同时变慢与变得虚假自信。

### 3. 对标与约束

- **与 [[AI-Labor-Bottleneck-Shift]] 对标**：这是“执行变便宜 → verification 变稀缺”的基础设施级实证。瓶颈迁移不只发生在人类 review；机器验证本身也有容量、成本和等待时间上限。
- **与 [[Verifiable-Agent-Engineering]] 对标**：可验证边界必须把 verifier 的 latency/cost/availability 纳入运行条件。一个理论上很强但 20 分钟才能反馈的测试系统，会直接压低可用 Agent 并发度和迭代速度。
- **与 [[Dominator-Analysis]] 对标**：change detection、checkout 等前置 gate 对多个 shards 形成支配节点；优化这些 dominator 的收益高于等量优化非关键路径工作。
- **与 [[Skill-Internalization]] 对标**：Linear 在改变测试隔离策略后同步更新 agent skills，使新测试默认服从性能 opt-in 规则；这是一种“基础设施经验 → 生成约束”的知识内化。
- **硬约束**：任何 CI 加速必须同时观察 correctness、flake rate、false negative/positive、tail latency 和 runner cost；只压 median 或 runner-minutes 容易把风险转移到不可见维度。
- **系统约束**：更激进 sharding 只有在每 shard 固定 setup 成本已足够低时才有效；并行度不是免费资源，setup overhead、queue capacity 和 straggler distribution 决定边际收益。

## 证据边界

- 来源为 Linear 工程团队成员 Mufeez Amjad 2026-09-21 的一手生产复盘，包含较丰富的 before/after 时延、runner time 和工作量数据，因此对 Linear 自身事实取 `evidence_level: high`。
- 文章不是受控实验；跨措施因果贡献、Agent adoption 的独立效应以及其他语言/仓库结构的可迁移性仍需谨慎。
- 稳定知识吸收“verification infrastructure 也会成为 AI coding 的绑定瓶颈”“关键路径与固定成本优先”“性能优化不能弱化 correctness oracle”三条机制，不把具体百分比当作普适目标。
- canonical URL 当前稳定可访问；完成 registry 与 section locator 后，Raw 适合结算为 index。

## 关联概念

- [[AI-Labor-Bottleneck-Shift]]
- [[Verifiable-Agent-Engineering]]
- [[Dominator-Analysis]]
- [[Skill-Internalization]]
