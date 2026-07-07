---
type: source-summary
title: "Fragments: July 6, 2026"
source_raw:
  - "[[20260706-martin-fowler-fragments]]"
created: 2026-07-07
updated: 2026-07-07
tags:
  - source-summary
  - agentic-engineering
  - token-economics
  - software-design
  - enterprise-ai
evidence_level: medium
claim_type: mixed
---

# Fragments: July 6, 2026

## 编译摘要

### 1. 浓缩

- **核心结论1**: Agentic 开发已跨越从"aspirational"到"production"的鸿沟，仅用 5 个月（2026.2 FOSE Utah → 2026.7 FOSE Europe）
  - 关键证据: Giles Edwards-Alexander: "Deer Valley had hesitancy... Engelberg had confidence: the value is here. This was not a conference for true believers: the evidence is in."
  - 关键证据: Greg Herlein: "Everybody in the room was doing it. Shipping it. Not slides - production. The whole debate about whether this changes software engineering is over."
  - 关键证据: 有参会者已编目了数十个 agentic engineering pattern libraries——模式正在涌现但尚未标准化

- **核心结论2**: Harness Engineering 的术语演化速度本身就是信号——2026 年 2 月 FOSE Utah 还不是一个术语，5 个月后已成热议话题
  - 关键证据: Fowler 原话: "there was much talk now about harness engineering, when that wasn't even a term in Utah"
  - 关键证据: 与 Token 成本焦虑并列：以前人们想尽办法激励大家用 AI，现在开始担心 token 开销

- **核心结论3**: 架构与设计质量对 Agent 仍然重要——"DX=AX Circle"（开发者体验与 Agent 体验是同一个圆），且 token 消耗量可作为设计质量的新度量
  - 关键证据: Laura Tacho: "the Venn Diagram of Developer Experience and Agent Experience is a circle"
  - 关键证据: 新度量思路——同一变更所需 token 越少，架构质量越好
  - 关键证据: "we're at the first time ever where the computers care about code quality"
  - 关键证据: Mathias Verraes 补充：好的设计是 AI 依赖风险的 hedge——我们不知道未来模型是否可用、成本多高

- **核心结论4**: Token 成本危机持续升级——404 Media 泄露数据显示某公司 token 年化支出从 `$5M`（2025.8）飙至 `$120M+` 预测（2026 财年），企业从激励使用反转为限额配给
  - 关键证据: 某公司 token 账单: 2025.8 `$5M` → 2026.5 `$15M` → 全年预计 `$120M+`
  - 关键证据: Citi、Amazon 等公司限制前沿模型使用，要求员工用更弱模型
  - 关键证据: 最大问题不是软件工程 agentic programming，而是非技术员工用 AI 做 PDF→PPT 等咀嚼 token 的任务
  - 关键证据: 极端应对——Caveman 插件让 AI "像原始人一样说话"以节省 token

- **核心结论5**: AI 伦理的实践立场从"退出=纯洁"转向"在场=关怀"——Charity Majors: "You show care by showing up"
  - 关键证据: "The way you make the world a better place is by getting down in the muck and building it"
  - 关键证据: Fowler 自己组织了一场 FOSE 讨论会，也未产生突出方案——伦理行动路径本身就是一个开放问题

### 2. 质疑

- **关于"跨越鸿沟"结论**: Fowler 仅参加了 1/5 的并行 session（五条轨道只能听一条）。FOSE 退修会是自选群体的早期采纳者聚会——"Everybody is shipping"描述的可能是前沿群体的状态，不代表行业整体。但这不影响结论的方向性意义：前沿群体的共识已从"是否"转向"如何"。

- **关于"架构仍然重要"结论**: 辩论尚未解决。两种假设（Galaxy Brain vs DX=AX Circle）并存，都是假设而非验证结论。Token 消耗量作为设计度量是有趣的提议，但"好架构只有随时间推移才显现质量"意味着短期 token 测量可能不可靠。Adam Tornhill 的 Code for Humans and Machines 观点存在确认偏差风险——他本就主张代码质量。

- **关于 Token 成本数据**: 404 Media 基于泄露材料（Slack 聊天、内部仪表盘），样本量和代表性存疑。`$120M` 年化预测可能包含外推误差。但多个独立来源（Accenture、Uber、Citi、Amazon）的交叉验证增强了可信度。

- **关于 AI 伦理立场**: Charity Majors 的论点有力量——"退出"确实不帮助被伤害的人——但"在场并建设"是否真的推动改变，还是只是让人感觉良好地继续使用有问题的技术？Fowler 自己也承认这个方向的行动方案"不突出"。

- **关于 LLM 生成代码的质量问题**: Fowler 提到即使有好的 harness，LLM 生成代码仍有重复和关注点混合。这质疑了"好 harness 就能产出好代码"的简化假设——Harness Engineering 是必要条件，不是充分条件。

### 3. 对标与旁逸

- **跨域关联1 — Token 成本成为设计度量** → 类似计算机体系结构中能耗从"次要指标"变为"首要设计约束"的转变。正如 Dennard scaling 终结后每瓦性能成为芯片设计的核心度量，token 成本可能成为软件架构的"每 token 可维护性"度量。

- **跨域关联2 — Mechanical Sympathy for LLMs** → Fowler 将 Martin Thompson 的 Mechanical Sympathy 概念（理解硬件实际行为以写出高性能代码）迁移到 LLM 领域。这暗合了 Martin Thompson 原概念的精髓：不是抽象地推测，而是基于对系统实际运行方式的经验理解来做决策。Fowler 明确反对"推测 LLM 未来会做什么"，主张获取对当前 LLM 的机械同理心。

- **跨域关联3 — Aspirational → Production 的 5 个月跨越** → 对应 Gartner 炒作周期中从"期望膨胀期"到"泡沫低谷期"再到"稳步爬升期"的压缩版。但这里的跨越方向相反——不是泡沫破裂，而是直接进入生产。说明 Agentic 开发可能跳过了典型的幻灭阶段。

- **边界分析**: 全文观察适用于 2026 年中、北美/欧洲前沿科技公司生态。Token 成本危机主要在大型企业（Citi、Amazon、Accenture）中显现。小型团队和个人开发者的 token 成本约束可能完全不同。"Architecture still matters"辩论的参与者主要是已有架构投资的人——可能存在 survivorship bias。

### 关联概念

- [[Harness-Engineering]] — 术语从不存在到热议的 5 个月演化
- [[Tokenpocalypse]] — 新数据点：`$5M→$15M→$120M` 年化
- [[Token-Maxing]] — 非技术员工"咀嚼 token"是成本主因
- [[Agentic-Engineering]] — 从 aspirational 到 production 的跨越
- [[Mechanical-Sympathy-for-LLMs]] — Fowler 新造术语
- [[Friction-as-Design-Signal]] — token 消耗作为设计质量反馈信号
- [[AI-Deployment-Invisible-Costs]] — Token 成本是不可见成本的典型案例
