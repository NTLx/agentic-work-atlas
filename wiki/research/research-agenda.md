---
type: research-agenda
title: "Agentic Work Atlas 研究议程"
created: 2026-05-22
updated: 2026-07-07
tags:
  - agentic-work-atlas
  - llm-wiki
  - knowledge-management
related_entities:
  - "[[LLM-Wiki]]"
  - "[[Agentic-Engineering]]"
  - "[[Agent-Harness]]"
  - "[[Human-Governor-Agent-Operator]]"
  - "[[Judgment]]"
---

# Agentic Work Atlas 研究议程

> [!note] 使用边界
> 本页只保留活跃操作节、当前最值得推进的方向和最小动作。已收敛判断见 [[resolved-judgments]]（06-24/07-02/07-03/07-04/07-06 五批次共 61 条）；已收敛操作原则见 [[resolved-principles]]（9 条）；旧方向库与长问题库见 [[exploration-archive-20260628]]；图谱健康度历史快照见 [[research-snapshot-20260703]]。

## 图谱健康度（07-07 待实测）

| 指标 | 上次值 (07-04) | 动作 |
|------|--------|------|
| Entity / Topic / Comparison / Output | 307 / 31 / 19 / 5 | **建 8-10 topic**（六簇零承载） |
| Entity:Topic 比 | 9.9:1 | 中层断层持续，需第五动作 synthesize |
| lint 分数 | 100/100 PASS | 阻断已清零 |
| 待编译 raw | 2 | 编译基本追上剪藏速度 |
| 完全孤儿 entity | 5 | 需补承载 or 归档 |
| 零入链 comparison | 8 | 需补承载 or 归档 |
| 零被引 output | 5/5 | output 层彻底孤岛 |
| Output 转化率 | 5/307 ≈ 1.6% | 目标 ≥20%，需从存量判断中提取 |

> 完整历史快照、成簇明细与缺失领域清单见 [[research-snapshot-20260703]]。

## 当前研究焦点

| 焦点 | 为什么重要 | 下一步 |
|------|-----------|--------|
| **图谱整合与 topic 建设** | 301 entity / 31 topic = 9.7:1，六簇零承载；第五动作缺失 | 建 8-10 topic skeleton；优先记忆/AGI经济/安全三簇 |
| **Output 断层修复** | 5 output 无法验证 61 条收敛判断；零被引；已 34 天无新产出 | 转 ≥2 output：Agent Observability 产业分析 + 元合成 rank 文章 |
| **Loop Engineering** | H1 2026 新范式：设计循环让 agent 自驱动 | clip source → 建 entity → 与 Ralph-Loops/Agent-Logic 交叉 |
| **Agent Identity & IAM** | 非人类身份管理是 agent sprawl 的核心瓶颈 | clip source → 建 entity → 与 Agent-Security 交叉 |
| **Spec-Driven Development** | 从 vibe coding 到 spec-driven 的范式迁移 | clip source → 建 entity → 与 Vibe-Coding/Software-2.0 交叉 |
| **Token FinOps 与 AI 计量** | 企业 AI 采用的隐性瓶颈；98% FinOps 实践已操作 AI 成本 | compile → 建 Token FinOps entity + topic |
| **AI-native 测试与验证** | 评测治理四部曲完成，下一层是工程实践 | 回填 → 建 AI-Native-Testing topic |
| **跨境 AI 治理差异** | EU/US/CN 三范式对 Agent 部署的实质影响 | 回填 → 建 AI-Governance-Regimes comparison |

## 活跃假设

> 仅保留 hypothesis 级别或仍在活跃验证的条目。已 synthesized/extracted 的判断已移至 [[resolved-judgments]]。

| 假设 | 验证方向 | 状态 |
|------|---------|------|
| Agent Control Plane 壁垒转移定理：壁垒从模型→运行时治理。独立窗口 = f(多模型采用 × 监管) | 追踪独立厂商融资；测量多模型采用率 | 待外部实证 |
| 认知分工终态定理：发散 = 1 人 + AI，收敛 = 多独立视角。共同锚点 = 偏差换噪声 | 对照实验：共享 AI vs 不同 AI vs 无 AI | 待实验设计 |
| 全球南方 AI 跃迁双速定理：AI 可跳过技术层，不可跳过制度层 | 找同时加速个体 + 组织的成功案例 | 待案例收集 |
| 中国 AI 双速瓶颈：高政策推动 × 低组织准备度。瓶颈 = 科层碎片 + FinOps 缺失 | 找 Token FinOps 实际建立案例 | 待案例收集 |
| 合成数据自举边界：天花板 = f(任务结构化程度 × 验证器质量) | 找合成数据训练使模型超越训练分布的任务类型 | 待实证 |
| 模型可解释性缺口：Agent 推理链可解释性 > 单模型 XAI 供给 | 测量 agent 推理链中"不可解释步骤"的比例 | 待工具/方法 |
| 判断力净退化期量化：不同判断力类型有不同退化曲线 | 各类型退化曲线测量 | 待纵向研究 |

## 活跃验证中（精选最高优先级可证伪判断）

> 从 61 条已收敛判断中挑选当前最值得投入验证资源的 5 条。完整清单见 [[resolved-judgments]]。

| 判断 | 证伪路径 | 最小验证动作 |
|------|---------|-------------|
| AI 评测制度化已启动：US AI Incident Reporting Act(2026-06-26)=强制7天报告+`$2M`/天罚款 | 追踪首次执法行动的时间、力度和效果 | 设置 Google Alert |
| 反效率文化悖论：恢复可习得性需要"刻意不效率"文化，需外部强制打破 Commons Dilemma | 找自愿采纳"学习优先于效率"并保持竞争力的组织 | 搜索 "learning over efficiency" 组织案例 |
| 图谱中层断层——Topic聚合=缺失的第五动作：四动作模型缺少 synthesize | 设计第五动作触发条件，测试是否能自动检测 entity 簇密度≥阈值 | 实现 entity 簇密度检测 prototype |
| Agent Identity 危机定理：非人类 identity 增长 > IAM 治理增长 | SPIFFE 能否扩展到动态 agent？agent 冒充攻击真实案例？ | 搜索 SPIFFE agent identity 实践 |
| Loop Engineering 杠杆定理：Loop 设计的杠杆 > Prompt 设计的杠杆 | 测量不同 loop 设计模式的生产力差异 | 找 loop vs prompt A/B 对照研究 |

## Source 需求队列

| 优先级 | 目标 | 当前缺口 | 下一步 source | 触发行动 |
|--------|------|----------|---------------|----------|
| P0 | AGI Economics topic | 15 entity 零承载 | 经济学框架性论文 | 建 topic skeleton |
| P0 | Memory Systems topic | 13 entity 零承载 | 认知心理学记忆模型文献 | 建 topic skeleton |
| P0 | Security & Privacy topic | 16 entity 零承载 | 安全/隐私对标 OWASP Top 10 for Agent | 建 topic skeleton |
| P0 | Output 断层 | 5 output 零被引，34 天无新产出 | 07-02/03/04/06/07 日志原料充足 | 写 2 个 output |
| P0 | Loop Engineering | 知识库完全缺失 | Ng/Cherny/Steinberger loop 设计实践 | clip + 建 entity |
| P0 | Agent Identity & IAM | 知识库完全缺失 | Forrester/SPIFFE/SPIRE agent identity | clip + 建 entity |
| P0 | Spec-Driven Development | 知识库完全缺失 | AWS Kiro/GitHub Spec Kit/Tessl | clip + 建 entity |
| P1 | Token FinOps entity + topic | 3 raw 待编译 | raw 已到齐 | compile → 建 entity |
| P1 | AI-Native Testing topic | 07-03 roundtable 完成 | raw 已到齐 | 回填 → 建 topic |
| P1 | AI Governance Regimes comparison | 07-03 roundtable 完成 | raw 已到齐 | 回填 → 建 comparison |
| P1 | Agent Observability topic | 4 entity 零承载 | Datadog/New Relic APM 演化史 | 建 topic skeleton |
| P1 | Skill Engineering topic | 5 entity + 07-03 新剪藏 | Anthropic Skill Engineering 实践 raw | compile → 建 topic |
| P2 | 死 topic 清理（7 个零入链） | 见下方死 topic 清理 | — | 补内容 or 归档 |
| P2 | 模型可解释性 (XAI) | 仅 3 处提及 | mechanistic interpretability 文献 | clip + 评估 |
| P2 | 编译 2 pending raw | Goodhart's Law + AI Agent Traps | 已有 raw | 批量 compile |

## 高杠杆待验证问题

### 从思考未穷尽处

- Token FinOps 能否成为独立的企业软件品类（类似 CloudHealth 之于云成本）？
- Agent Control Plane 独立厂商能否在模型厂商内化之前建立护城河？
- 判断力退化的"净退化期"能否被量化——不同判断力类型的时间曲线？
- Exit-Sovereignty 能否被设计为 AI 工具的强制性 affordance？
- 中国 AI 采用中"科层碎片化"的结构性根源——是暂时过渡还是体制性永久特征？

### 从外部现实新缺口（07-04/07-07 探索）

- **Loop Engineering 的设计空间**——loop 的最优终止条件、反馈粒度、人类介入频率如何随任务类型变化？
- **Agent Identity 的标准会是什么**——SPIFFE/SPIRE 模式能否扩展到 AI Agent？还是需要全新的 identity 范式？
- **Spec-Driven Development 的边界**——什么类型的软件适合 spec-driven，什么类型永远需要 vibe？
- **MCP 生态的治理风险**——Anthropic 控制的 MCP 是否会造成单点依赖？是否需要 CNCF 式中性治理？
- **Agent 测试的"OWASP Top 10"何时出现**——Property 不变量库的标准化进度？
- **模型可解释性在 Agent 时代是否成为瓶颈**——单模型可解释性 vs Agent 推理链可解释性的 gap 有多大？
- **合成数据自举的数学边界**——模型能否通过自我生成数据超越训练分布？边界在哪里？

## 新方向摘要（07-07 深度盘点更新）

> 详细四层方向表已迁移至 [[exploration-archive-20260628]]。此处整合本次全量盘点（307 entities + 31 topics + 19 comparisons + 5 outputs + 180 raw）发现的缺口和新增方向。

### 🆕 Entity 层主题缺口（307 entity 审计发现）

> 以下主题在 entity 层几乎完全缺失，与主题宪法的四层面存在系统性盲区。

| 缺失主题 | 详情 | 为什么重要 |
|----------|------|-----------|
| **多模态/具身 AI** | 零 entity。知识库严重偏向 text/code 中心 | Agent 的行动面正从 API 扩展到视觉/GUI/物理世界 |
| **AI 监管与法律（细节层）** | 仅原则层 governance entity，无 EU AI Act/US EO/CN 法规的具体 entity | 监管正从原则→具体执法，需要可操作的法规 entity |
| **数据与训练方法** | 几乎空白：无 data curation/synthetic data/training flywheel entity | Agent 时代的核心瓶颈之一是训练数据的质量和来源 |
| **AI 能源与可持续性** | 零 entity | Agent 24/7 运行模式的能耗结构完全未被讨论 |
| **国际/地缘 AI 动态** | 仅 Hardware-Sovereignty 触及 | US-CN 竞争、出口管制、全球南方的系统性缺失 |
| **AI 伦理与道德哲学** | 无系统处理 | 仅 Positionality/Ownership 触及边缘 |
| **Agent 时代 HCI/UX** | 仅 ACI/Agent-Ergonomics 两个 entity | 人机交互界面正在被 Agent 重写 |
| **教育与培训系统** | 仅 Lehrwerkstatt/Osmosis-Learning | 大学和培训体系如何适应 Agent 时代 |
| **Agent 失败模式分类学** | Agent-Traps/Multi-Agent-Pathology 存在但无系统分类 | 实际部署中最需要的就是失败模式知识库 |
| **AI 保险与责任** | 零 entity | Agent 造成损害时谁负责——这是生产化的前提条件 |
| **开源 AI 生态** | 仅 Cybersecurity-Openness 触及 | open-weight models/开源 agent 框架/开放vs封闭辩论

| 缺口 | 详情 | 优先级 |
|------|------|--------|
| **Comparison 层严重欠链接** | 13/19 comparisons（68%）零入链。Topic 未系统引用 comparison。Comparison 层是知识库的"隐藏资产" | **P0** |
| **Output 层终端孤岛** | 5 output 零被引；34 天无新产出；61 条收敛判断未被任何 output 消费。转化率 1.6%（5/307 entities） | **P0** |
| **9 个 topic 零入链** | 与 agenda 自报 7 个不同（Agentic-AI-Ecosystem/AI-Management-Mindset-Transfer/AI-Mathematics-Future/AI-Mediated-Organization/CEO-Hands-On-AI/Karpathy-AI-Thought/Lean-Indie-Engineering/OpenClaw-Agent-System/模型安全分歧） | P1 |
| **安全簇稀疏** | AISI/Mythos/Agent-Containment/Zero-PHI-Policy/Cybersecurity-Proof-of-Work 等 entity 存在但仅 2 topic（AI-Policy-Framework/模型安全分歧） | P1 |
| **Research log 格式不一致** | 早期 log 有 blockquote 摘要，后期缺失；07-06/07-07 log 缺 frontmatter | P2 |

### 🆕 缺失 Topic（entity 簇已有但无 topic 承载）

| 缺失 Topic | 锚点 entity 数 | 为什么重要 |
|------------|---------------|-----------|
| **Agent Harness** | 11 entity 链入 Organization-as-Agent-Harness | 知识库最核心概念之一，有 comparison 但无独立 topic |
| **Coding Agents** | 多个 topic 引用 Coding-Agents entity | Claude Code/Codex/Gemini CLI 工具谱系无 topic 覆盖 |
| **Context Engineering** | Context-Engineering entity + comparison 存在 | 与 Prompt Engineering 的进阶关系未被 topic 化 |
| **Agent Orchestration** | Agent-Orchestration/Agent-Swarm entity | 编排架构与 Multi-Agent-Pathology 不同维度，需独立 topic |
| **Knowledge Compilation** | LLM Wiki 核心操作 | 仅通过 Agent-Knowledge-Management 间接覆盖 |
| **Vibe Coding / Software 3.0** | Karpathy 系列 + 3 个 comparison | 有丰富 comparison 但无独立 topic |
| **Token Supply Chain / Model Economics** | Token-Supply-Chain entity | Token 作为生产资料的经济学未被 topic 化 |
| **Verifiability** | 24+ entity 引用 | 知识库最高被引概念之一，仅作为 Verifiable-Agent-Engineering 子节 |
| **Headless Agent** | 07-04 深度探索产出 | 已收敛判断但无 topic 承载 |
| **Agent-to-Agent Economy** | Settlement-Mechanism/Agent-Economic-Protocols entity | 多 Agent 经济系统无 topic |

### 🆕 缺失 Comparison（应对比但未对比的概念对）

| 缺失 Comparison | 为什么重要 |
|-----------------|-----------|
| **Prompt Engineering vs Context Engineering** | 自然进阶关系——从"写更好的 prompt"到"设计更好的 context" |
| **Workflow vs Agent** | Anthropic Building Effective Agents 的核心区分 |
| **Frontier Models vs Specialized Small Models** | 不同于 Closed-vs-Open 的另一维度 |
| **Copilot vs Agent** | 两种人机协作模式，entity 均已存在 |
| **Agent-Harness vs Agent-Swarm** | 两种多 Agent 架构的系统对比 |
| **RAG vs Context Engineering vs Knowledge Compilation** | 知识管理栈三层对比（当前仅两两对比） |

### 🆕 外部现实新信号（07-07 搜索发现）

> 以下为本次探索中新发现的外部信号，此前未在 agenda 中出现。

| 信号 | 来源 | 含义 | 行动 |
|------|------|------|------|
| **AI 评测制度化加速** | US AI Incident Reporting Act (2026-06-26) 已签署 | 从自愿→强制的质变已发生 | 追踪首次执法 + NIST Workshop 第二届 |
| **Anthropic Economic Index 更新** | Anthropic 2026H1 报告 | 开发者 60% 工作用 AI，但仅 0-20% 可完全委托 | 深化"可委托性边界"研究 |
| **Databricks 多 Agent 增长 327%** | Databricks 2026 报告 | Supervisor Agent 模式占 37% | 追踪多 Agent 编排模式演化 |
| **Forrester Agent Sprawl 警告** | Forrester 2026 | >50% 企业报告 agentic sprawl；非人类 identity 仍是 mess | 建 Agent Sprawl 治理 entity |
| **S&P Global: 31% 生产化率** | S&P Global 2026 | 80% 嵌入 agent 但仅 31% 进生产 | 深化 Enterprise AI 鸿沟分析 |
| **Gartner: 40% AI 项目将取消** | Gartner 2026 预测 | AI 部署死亡谷的量化预测 | 追踪实际取消率 vs 预测 |

### 最优先启动（P0 — 直接服务主问题且知识库缺失）

1. **Loop Engineering** — 新范式。Ng 三循环框架。锚点：Ralph-Loops/Agent-Logic
2. **Agent Identity & IAM** — 非人类 identity 核心瓶颈。Forrester 警告
3. **Spec-Driven Development** — Vibe→Spec 范式迁移。AWS Kiro/GitHub Spec Kit
4. **Agent Sprawl 治理** — >50% 企业 sprawl。与 Identity 双生问题
5. **Comparison 层激活** — 13/19 零入链。Topic 应系统引用 comparison
6. **Output 断层紧急修复** — 1.6% 转化率。从 61 条收敛判断中提取 2-3 篇 output
7. **缺失 Topic 补建（Top 5）** — Agent Harness / Context Engineering / Verifiability / Knowledge Compilation / Headless Agent

### 次要启动（P1 — 有锚点待深化）

- Agentic Software 理论（Cao 2026）
- 多 Agent 编排 vs Loop 编排边界
- AI 治理与生产化因果关系（governance → 12x production）
- Enterprise AI 鸿沟（80% vs 31%）
- 知识库元方法论深化（第五动作 synthesize 工程化）
- MCP 生态治理
- AI 使用节律与认知健康
- 认知债务新型态
- Agent-to-Agent 经济与支付
- 安全簇 topic 建设（Agent Safety Top 10）
- 缺失 Comparison 补建（Top 3: Prompt vs Context Engineering / Workflow vs Agent / Copilot vs Agent）

### 需补 source（P2）

- 合成数据自举边界（完全缺失）
- AI 能源与环境可持续性（零 entity）
- 模型可解释性 Agent 时代缺口（仅 3 处提及）
- 全球南方 AI 跃迁实证案例
- 多模态/具身 AI（零 entity，Agent 行动面盲区）
- Agent 失败模式分类学（实际部署最需要）
- AI 保险与责任框架（生产化前提条件）
- Agent 时代 HCI/UX 设计范式
- 开源 AI 生态与开放vs封闭辩论

## 下一步目标建议与最小实验

### 立即执行（本次探索闭环）

1. **Comparison 层激活** → 最小实验：选 3 个最重要的 comparison（RAG-vs-LLM-Wiki 已有 7 入链除外），从对应 topic 中添加反向链接
2. **Output 断层破冰** → 最小实验：从 07-06 收敛判断中选 1 条最有解释力的（推荐：AI 本体论改写假说 or 反效率文化悖论），写 1 篇 output
3. **缺失 Topic 启动（Top 3）** → 最小实验：建 Agent-Harness / Context-Engineering / Verifiability 三个 topic skeleton（各 ≤30 行，含定义+锚点 entity 列表+开放问题）

### 短期推进（1-2 周）

4. **Loop Engineering 快速启动** → clip 1-2 篇 source → 建 entity → 交叉链接
5. **Agent Identity 快速启动** → clip 1 篇 source → 建 entity → 交叉链接
6. **Spec-Driven Development 启动** → clip 1 篇 source → 建 entity → 交叉链接
7. **记忆系统簇建 topic** → 13 entity → "编码→巩固→检索→遗忘"框架 → Agent-Memory-Lifecycle topic
8. **安全簇建 topic** → 16 entity → Agent Safety Top 10 topic skeleton
9. **回填 07-03/07-04 产出** → AI-Native-Testing topic + AI-Governance-Regimes comparison

### 持续维护

10. **死 topic 处置** → 9 个零入链 topic（本次盘点从 7→9 修正）逐个判定
11. **Research log 格式标准化** → 补 07-06/07-07 log frontmatter
12. **Comparison 补建** → Prompt vs Context Engineering / Workflow vs Agent / Copilot vs Agent

## 死 topic 清理

> 9 个 topic 零 entity 入链（07-07 盘点修正，此前自报 7 个）。需补内容承载 entity、或归档、或合并。

| Topic | 状态建议 |
|-------|---------|
| `Agentic-AI-Ecosystem` | 补承载（可整合 Agent 互操作协议簇 + Token Supply Chain） |
| `AI-Management-Mindset-Transfer` | 补承载（有 AI-Capability-Management-Alignment entity） |
| `AI-Mathematics-Future` | 补承载（有 AI-in-Mathematics entity） |
| `AI-Mediated-Organization` | ⚠️ 高质量内容但零入链——需从 Organization-as-Agent-Harness 等添加反向链接 |
| `CEO-Hands-On-AI` | 补承载 or 归档 |
| `Karpathy-AI-Thought` | ⚠️ 综合性强但零入链——需从 Software-2.0/Vibe-Coding/LLM-Wiki entity 添加反向链接 |
| `Lean-Indie-Engineering` | 补承载 or 归档 |
| `OpenClaw-Agent-System` | ⚠️ 高质量内容但零入链——需从 Agent-Harness/Claude-Code-Automation 添加反向链接 |
| `模型安全分歧` | 补承载（安全簇 16 entity 待建 topic，可合并入新 Agent Safety topic） |

## 最近思考结论摘要

> 只保留最近 5 条；更早见 [[resolved-judgments]]。

| 时间 | 焦点 | 临界发现 |
|------|------|---------|
| 2026-07-07 | 图谱中层断层——Topic聚合=第五动作 | LLM Wiki四动作缺失"跨entity综合为topic"。9.7:1=结构性缺陷非内容量问题。第五动作=synthesize/surface，触发=entity簇密度检测 |
| 2026-07-06 | 失败空间迁移不等价定理（深化） | 底层机制=AI本体论改写。恢复=审计学习条件非审计能力。Klein悖论消解为经济悖论。反效率文化=commons dilemma |
| 2026-07-06 | AI 评测制度化六要素蓝图 | 分离机制×分通道×分级门槛×信息交换×分类学维护者×全球互认。NIST Workshop已启动。事件可定义性=比学习vs惩罚更深的前提 |
| 2026-07-06 | 认知分工终态定理（修正版） | 发散=1人+AI，收敛=四条件独立判断源。共同锚点=偏差换噪声。个体锚点需外部他者破解——Gödel自指→锚定是孤独的 |
| 2026-07-06 | 后果真实性不可消除定理（深化版） | 不可逆≠物理伤害=社会性+公共见证。存在性改变=皮层+社会疼痛通路。设计悖论消解：分离触发器设计和后果真实性 |

## 思考日志索引

- [[2026-07-07]] — 9 轮：模型可解释性 / 全球南方跃迁 / 中国双速 / Exit-Sovereignty / Token FinOps / 净退化期 / 编码杠杆 / 记忆衰减 / 图谱中层断层（+roundtable×8+自反×1）
- [[2026-07-06]] — 10 轮：失败空间迁移 / AI评测制度化 / 认知分工 / 后果真实性 / 判断力扰动 / Agent Identity / Loop Engineering / Spec-Driven / Control Plane / 合成数据自举
- [[2026-07-04]] — 11 轮：可博弈性三重奏 / Agent生命周期 / Computer Use / Headless Agent / 元方法论 / Agent安全 / AGI经济学 / 重组双向制度 / 治理内生性 / 时间不对称 / Context Advantage
- [[2026-07-03]] — 15 轮：Agent Obs / 代理-现实差距 / Compliance-as-Code / Reward Hacking / Agent协议 / Context工具衰减 / 多Agent编排 / Skill Engineering / Token FinOps / 记忆 / 认知背离 / AI-native测试 / AI治理 / Agent框架 / 认知背离
- [[2026-07-02]] — 31 轮含元合成：评测/记忆/灵活性/治理/认知/全球南方/控制平面/AI认知/Headless/Harness/多Agent倒U/AGI经济学/中国AI/元合成rank/Context Advantage/Goodhart Soros Gödel/重组制度/治理内生性/判断力扰动/后果真实性/Token FinOps
- [[2026-07-01]] — 12 轮：协调/记忆/评测/治理/判断力/经济学/组织/Agent/CU/Reward/动态环境
- [[2026-06-30]] — 全库盘点 + 多轮探索
- [[exploration-archive-20260628]] — 06-28 全库快照 + 方向库 + 长问题库 + 07-04/07-07 卸载内容
- [[research-snapshot-20260703]] — 07-03 图谱健康度快照 + 成簇分析 + 缺失领域
- [[resolved-judgments]] — 已收敛判断（5 批次共 61 条）
- [[resolved-principles]] — 已收敛操作原则（9 条）
