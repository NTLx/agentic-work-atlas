---
type: source-summary
title: "How I run multiple `$10K` MRR companies on a `$20`/month tech stack"
source_raw:
  - "[[How I run multiple USD10K MRR companies on a USD20month tech stack]]"
created: 2026-05-24
updated: 2026-05-24
tags:
  - source-summary
  - indie-developer
  - bootstrap
  - lean-stack
---

# How I run multiple `$10K` MRR companies on a `$20`/month tech stack

## 编译摘要

### 1. 浓缩

- **核心结论1: 零成本跑道等价于百万美元融资** — 月支出 `$20` = 无限生存时间，VC 拒绝他的原因恰恰是他跑得太精简
  - 关键证据: "Keeping costs near zero gives you the exact same runway as getting a million dollars in funding with a massive burn rate." Steve 因"太精益"被 pitch night 拒绝
  - Runway 公式: `$10,000` ÷ `$20/月` = 500 个月 (41 年) vs VC 融 `$1M` ÷ `$50K/月` = 仅 20 个月

- **核心结论2: 技术选型由约束驱动，而非潮流** — 1GB RAM 约束 → Go 而非 Python（静态二进制 几MB vs gunicorn 500MB 基线）；单机约束 → SQLite+WAL 而非 Postgres RDS（查询走 C 函数调用纳秒级 vs TCP 往返毫秒级）；一人团队 → systemd service 而非 K8s
  - 关键证据: SQLite+WAL `SELECT 1` benchmark 0.07s vs PostgreSQL TCP 2.77s（40 倍差距）；Go 交叉编译为静态二进制，scp 上传即运行，无依赖地狱

- **核心结论3: AI 成本有三层降本策略** — (1) 本地 GPU 处理批量任务：RTX 3090 (`$900` 一次性) + VLLM PagedAttention 并发推理，(2) OpenRouter 统一 API 网关 + 故障自动回退（Anthropic → OpenAI → 本地 VLLM），(3) GitHub Copilot per-request 定价漏洞：按请求而非 token 计费，一次请求可让 agent 运行 30 分钟修改数百文件，成本 `$0.04`
  - 关键证据: "Somehow, Microsoft is able to charge per request, not per token." Copilot 订阅 `$13/月`，作者用 Opus 4.6 全天开发月账单 `$60`，Cursor 等竞品用户月支出 `$100+`

- **核心结论4: 一人运营 6 个 `$10K+` MRR 产品的商业模式组合拳** — B2B 高客单价（zwibbler `$5,999`/单 × 20 单/年）养 C 端产品矩阵；六种定价模式覆盖三种盈利逻辑（大额低频、小额高频、一次性前置）
  - 关键证据: websequencediagrams.com (2008-) 18 年 SEO 权重无法复制；每 3-5 年新增一个产品，需求永恒 > 热点时髦

### 2. 质疑

- **关于"Copilot 定价漏洞"的持久性**: Microsoft 的 per-request 而非 per-token 定价模式显然低估了 agentic coding 的 token 消耗量。这个漏洞迟早会被修补——一旦修补，Copilot 的成本优势将消失。依赖定价漏洞的策略本质上是不可持续的套利
- **关于 SQLite+WAL 的可扩展性上限**: WAL 模式下单写者限制真实存在。虽然读不阻塞写，但高并发写入场景（如实时协作编辑）确实会遇到瓶颈。Steve 的选择成立的前提是：他的 6 个产品"不需要"高并发写入。这适用于大多数独立开发者产品，但不适用于所有场景
- **关于本地 GPU 的真实经济性**: RTX 3090 的 24GB VRAM 跑 32B 模型尚可，但前沿模型（Claude Opus 等级别）无法本地运行。他的"本地 AI"解决的是批量分类/摘要任务，不是替代前沿推理。电费 + 硬件折旧 + 维护时间 vs API 成本的完整 TCO 需要更精确的计算
- **关于"一个人"模式的不可复制性**: Steve 从 2008 年就开始积累，18 年的 SEO 权重、反链和用户信任构成的时间护城河，后发者无法复制。他今天的成功是他 18 年前开始的结果

### 3. 对标

- **跨域关联1 — 反云运动（Cloud Exit）**: Steve 的实践与 DHH (David Heinemeier Hansson) 的"cloud exit"运动在哲学上同源——都质疑"云=默认正确"的行业共识。差别在于 DHH 是从云迁回自建机房（大团队操作），Steve 是从一开始就不进云（单人操作），两条路径指向同一结论：云的成本结构对大部分产品不是最优
- **跨域关联2 — 边缘计算**: 本地 AI 推理（RTX 3090 + VLLM）本质上是将计算从云端移到边缘。这不仅是成本考量，也是延迟和隐私策略。与 CDN 将静态资产推到边缘的动机一致——让计算更靠近数据产生和消费的地方
- **跨域关联3 — 早期的云计算定价套利**: Copilot per-request 定价漏洞类似于早期 AWS 的预留实例 vs 按需实例套利，以及 Google Cloud 的 sustained use discount。平台在快速增长期往往定价偏低以获取市场份额，随后修补漏洞。识别和利用这种窗口期本身就是一种技能

### 关联概念

- [[Lean-Stack]]
- [[Runway-Math]]
- [[Anti-Enterprise-Mindset]]
- [[Constraint-Driven-Engineering]]
- [[B2B-Nurture-C-Model]]
- [[Time-Moat]]
- [[Steve-Hanov]]
- [[Vibe-Coding]]
