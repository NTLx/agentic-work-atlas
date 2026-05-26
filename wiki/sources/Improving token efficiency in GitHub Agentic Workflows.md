---
type: source-summary
title: "Improving token efficiency in GitHub Agentic Workflows"
source_raw:
  - "[[Improving token efficiency in GitHub Agentic Workflows]]"
created: 2026-05-24
updated: 2026-05-25
tags:
  - source-summary
  - AI-Agent
  - agentic-workflows
  - token-efficiency
---

# Improving token efficiency in GitHub Agentic Workflows

## 编译摘要

### 1. 浓缩

- **核心结论1**: Agentic workflows 的 token 成本必须像 CI 成本一样被观测、审计和持续优化。
  - 关键证据: GitHub 维护数百个 agentic workflows，自动触发在 PR 和 repo 维护中运行，成本会在无人注意时积累。由于 workflow 行为由 YAML 指定且反复执行，比交互式桌面 agent 更适合系统优化。
  - GitHub 使用 API proxy 统一捕获 Claude CLI、Copilot CLI、Codex CLI 等不同框架的 token usage，每次 workflow 输出 `token-usage.jsonl`，记录 input、output、cache-read、cache-write、model、provider 和 timestamps。
- **核心结论2**: GitHub 用 agentic workflows 反过来优化 agentic workflows，形成小型自我改进闭环。
  - 关键证据: Daily Token Usage Auditor 聚合近期 token usage，找出突然变贵、最贵和异常的 workflows；Daily Token Optimizer 读取 workflow source 和 logs，创建 issue，指出具体低效点并提出修改建议。
  - Auditor 和 Optimizer 自己也是 agentic workflows，其 token usage 也出现在报告中，形成可观察的成本治理循环。
- **核心结论3**: 两类高收益优化是删除未使用 MCP tools，以及把确定性数据获取移出 LLM 推理循环。
  - 关键证据: LLM API 无状态，agent runtime 常把 MCP tool names 和 JSON schemas 放进每次请求。GitHub MCP server 有 40 个 tools 时，每轮可能增加 10-15 KB schema；如果只用 2 个工具，其他 38 个都是纯 overhead。烟测 workflow 中移除未用 tools 后，每次调用上下文减少 8-12 KB。
  - 对 PR diff、file contents、review comments 等确定性数据，GitHub 用 `gh` CLI 预下载或通过安全 proxy 让 agent 调用 CLI，替代 MCP reasoning step，把 GitHub 数据读取从 LLM loop 中移出。
- **核心结论4**: 衡量效率不能只看 raw tokens，而要考虑模型价格、cache、输出成本、workload 变化和质量。
  - 关键证据: GitHub 提出 Effective Tokens 公式：`ET = m × (1.0 × I + 0.1 × C + 4.0 × O)`，其中模型倍率区分 Haiku/Sonnet/Opus，output tokens 权重更高，cache-read tokens 权重更低。
  - 他们还强调 live repository workload 会变化，同一 workflow 可能处理 5 行修复或 200 行 PR。需要同时看 turns-per-run、tokens-per-call、tool-call completion rate 等过程信号，避免把少做工作误认为效率提高。
- **核心结论5**: 初步结果显示，结构性优化可以带来显著降本，但也暴露好工作量测量仍然困难。
  - 关键证据: Auto-Triage Issues 优化后 109 次运行下降 62%；Daily Compiler Quality 提升 19%；Community Attribution 提升 37%；Security Guard 和 Smoke Claude 分别改善 43% 和 59%。但 Contribution Check 因工作负载转向更大 PR，ET 反而上升 5%。
  - 文章最后指出，下一步应从 workflow-level 走向 episode-level 和 portfolio-level，识别重复读取、失败循环、重叠 workflows 和可缓存中间 artifacts。

### 2. 质疑

- **关于适用性的质疑**: GitHub 的优化依赖 agentic-workflows security architecture、API proxy、workflow artifacts 和 GitHub Actions 环境。小团队未必需要完整体系，但至少需要 token logging 和高频 workflow 排序。
- **关于 CLI 替代 MCP 的质疑**: CLI 很适合确定性数据读取，但不适合需要 agent 规划、跨系统组合或权限语义复杂的操作。优化原则不是"不用 MCP"，而是"不要把确定性读取放进 LLM reasoning loop"。
- **关于 ET 公式的质疑**: 输出 4x、cache-read 0.1x、模型倍率是工程近似，随 provider 定价和缓存机制变化而变化。公式的价值在于统一比较，不是普适经济学定律。
- **关于质量测量的质疑**: 文章承认缺少 tokens-per-unit-of-correct-work 的 ground truth。过程信号稳定不等于输出质量稳定，长期仍需要 outcome instrumentation。
- **关于 optimizer 自身风险的质疑**: 自动优化 workflow 可能过度剪裁工具、切换模型或减少上下文，带来隐性质量下降。Optimizer 的建议也需要 review 和回滚。

### 3. 对标

- **与 [[Agent-Workflow-Patterns]] 对标**: 这篇补上了 agentic workflow 的成本治理模式：logging、auditing、optimization issue、tool pruning、deterministic pre-steps。
- **与 [[Model-Context-Protocol-MCP]] 对标**: MCP tools 带来的 schema overhead 是生产使用中的真实成本，说明 MCP server 设计不仅要看功能，还要看上下文预算。
- **与 [[Tool-Use-Architecture]] 对标**: 最重要原则是把确定性 data fetching 从 LLM loop 移走，把 LLM 留给需要推理、判断和综合的环节。
- **与数据库查询优化对标**: 先有慢查询日志，再有索引、查询改写和缓存。Agentic workflows 也需要从 raw token 日志走向 episode 和 portfolio 级优化。
- **与 [[Verifiability]] 对标**: 优化必须验证行为未退化。否则降低 token 只是削弱工作，而不是提高效率。

### 关联概念

- [[Agentic-Engineering]]
- [[Agent-Workflow-Patterns]]
- [[Agent-PR-Review]]
- [[Model-Context-Protocol-MCP]]
- [[MCP-Registry]]
- [[Tool-Use-Architecture]]
- [[Verifiability]]
