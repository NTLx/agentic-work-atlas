---
type: source-summary
title: "How I run multiple `$10K` MRR companies on a `$20`/month tech stack"
source_raw:
  - "[[How I run multiple USD10K MRR companies on a USD20month tech stack]]"
created: 2026-05-24
updated: 2026-11-28
tags:
  - source-summary
  - indie-developer
  - bootstrap
---

# How I run multiple `$10K` MRR companies on a `$20`/month tech stack

## 编译摘要

### 1. 浓缩

- **核心结论1: 低净现金消耗可延长跑道** — 作者用极低基础设施支出与高消耗融资公司对比；并非证明无限生存或所有经营支出均可控制
  - 关键证据: "Keeping costs near zero gives you the exact same runway as getting a million dollars in funding with a massive burn rate." Steve 因"太精益"被 pitch night 拒绝
  - 示例算术：`$10,000` ÷ `$20/月` = 500 个月（约 41.7 年），而 `$1M` ÷ `$50K/月` = 20 个月；只有在净现金消耗等于所用分母且稳定时才是实际跑道。

- **核心结论2: 技术选型由约束驱动，而非潮流** — 1GB RAM 约束 → Go 而非 Python（静态二进制 几MB vs gunicorn 500MB 基线）；单机约束 → SQLite+WAL 而非 Postgres RDS（查询走 C 函数调用纳秒级 vs TCP 往返毫秒级）；一人团队 → systemd service 而非 K8s
  - 关键证据: 2026-11-28 溯源：内存 SQLite `SELECT 1` 0.07s 与 PostgreSQL localhost 2.77s 的数字来自 [HN 评论者 eurleif](https://news.ycombinator.com/item?id=47736555)，不是作者原文；仅属调用开销微基准，非 WAL 持久化或真实业务基准；Go 交叉编译为静态二进制，scp 上传即运行，无依赖地狱

- **核心结论3: AI 成本有三层降本策略** — (1) 本地 GPU 处理批量任务：RTX 3090 (`$900` 一次性) + VLLM PagedAttention 并发推理，(2) OpenRouter 统一 API 网关 + 故障自动回退（Anthropic → OpenAI → 本地 VLLM），(3) GitHub Copilot per-request 定价漏洞：按请求而非 token 计费，一次请求可让 agent 运行 30 分钟修改数百文件，成本
  `$0.04`
  - 关键证据: "Somehow, Microsoft is able to charge per request, not per token." 作者自报使用 Opus 4.6 月账单约 `$60`；原文未给出 `$13/月` 订阅单价，也未提供等任务量、质量条件的竞品成本比较

- **商业启示（非原文实测结论）**：原文及作者网站列示多个产品，标题自报多个 `$10K` MRR 业务，但未逐项披露收入、销量、成本或 B2B 补贴 C 端的资金流，不能证明每个产品均超过该收入门槛或六产品商业组合的收益。
  - 边界：长期运营可能积累获客和维护经验；原始剪藏未提供 SEO 权重、排名、精确新增频率或不可复制性证据。

### 2. 质疑

- **关于"Copilot 定价漏洞"的持久性**: Microsoft 的 per-request 而非 per-token 定价模式显然低估了 agentic coding 的 token 消耗量。这是历史计费窗口，不能据此推断长期成本排序。2026-11-28 [GitHub 官方核验](https://docs.github.com/en/copilot/reference/copilot-billing/request-based-billing-legacy/what-changed-with-billing)：2026-06-01 起改为 usage-based，原有部分年付 Pro/Pro+ 可延续旧制至到期。新旧计费下的实际成本优势须重新测量。
- **关于 SQLite+WAL 的可扩展性上限**: WAL 模式下单写者限制真实存在。虽然读不阻塞写，但高并发写入场景（如实时协作编辑）确实会遇到瓶颈。Steve 的选择成立的前提是：他的 6 个产品"不需要"高并发写入。该案例不能代表大多数独立开发者产品；需按实际写负载、部署拓扑与恢复要求选型。
- **关于本地 GPU 的真实经济性**: RTX 3090 的 24GB VRAM 跑 32B 模型尚可，但前沿模型（Claude Opus 等级别）无法本地运行。他的"本地 AI"解决的是批量分类/摘要任务，不是替代前沿推理。电费 + 硬件折旧 + 维护时间 vs API 成本的完整 TCO 需要更精确的计算
- **关于"一个人"模式的不可复制性**: Steve 从 2008 年就开始积累，18 年的 SEO 权重、反链和用户信任构成的时间护城河，后发者无法复制。他今天的成功是他 18 年前开始的结果

### 3. 对标

- **跨域关联1 — 反云运动（Cloud Exit）**: Steve 的实践与 DHH (David Heinemeier Hansson) 的"cloud exit"运动在哲学上同源——都质疑"云=默认正确"的行业共识。差别在于 DHH 是从云迁回自建机房（大团队操作），Steve 是从一开始就不进云（单人操作），两条路径提出同一待检验问题：在实际负载和维护约束下，云服务的总成本是否高于简化或自管方案。不能从两个成功案例推出大部分产品的最优选型。
- **跨域关联2 — 边缘计算**: 本地 AI 推理（RTX 3090 + VLLM）本质上是将计算从云端移到边缘。这不仅是成本考量，也是延迟和隐私策略。与 CDN 将静态资产推到边缘的动机一致——让计算更靠近数据产生和消费的地方
- **跨域关联3 — 早期的云计算定价套利**: Copilot per-request 定价漏洞类似于早期 AWS 的预留实例 vs 按需实例套利，以及 Google Cloud 的 sustained use discount。平台在快速增长期往往定价偏低以获取市场份额，随后修补漏洞。识别和利用这种窗口期本身就是一种技能

### 关联概念

- [[Lean-Stack]]
- Runway-Math
- Anti-Enterprise-Mindset
- [[Constraint-Driven-Engineering]]
- B2B-Nurture-C-Model
- Time-Moat
- [[Steve-Hanov]]
- [[Vibe-Coding]]
