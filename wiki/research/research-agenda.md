---
type: research-agenda
title: "Agentic Work Atlas 研究议程"
created: 2026-05-22
updated: 2026-07-09
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
> 本页只保留活跃操作节、当前最值得推进的方向和最小动作。已收敛判断见 [[resolved-judgments]]（06-24/07-02/07-03/07-04/07-06 五批次共 61 条）；已收敛操作原则见 [[resolved-principles]]（9 条）；旧方向库与长问题库见 [[exploration-archive-20260628]]；图谱健康度历史快照见 [[research-snapshot-20260703]]；07-07 盘点详细缺口见 [[inventory-20260707]]；**07-09 深度探索详细记录见 [[inventory-20260709]]**。

## 图谱健康度（07-09 实测）

| 指标 | 07-07 | **07-09** | 变化 | 动作 |
|------|-------|-----------|------|------|
| Entity / Topic / Comparison / Output | 307/31/19/5 | **318/33/19/5** | +11/+2/0/0 | 继续建 topic（10 新簇零承载） |
| Entity:Topic 比 | 9.9:1 | **9.6:1** | 略改善 | 中层断层持续 |
| 待编译 raw | 2 | **0** | ✅ 清零 | 编译完全追上 |
| 零入链 comparison | 13/19 | **13/19** | 未变 | 需 topic 系统引用 |
| 零入链 topic | 9 | **9** | 确认 | 根因=单向链接架构 |
| 零被引 output | 5/5 | **5/5** | 未变 | Output 断层持续 |
| Output 转化率 | 1.6% | **1.6%** | 未变 | 需写 2-3 个 output |

> 完整历史快照见 [[research-snapshot-20260703]]；07-09 详细盘点见 [[inventory-20260709]]。

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
| Agent Control Plane 壁垒转移定理（修正）：壁垒非单向迁移而是四维重组（推理+治理+数据+协议）。执行-评估分离定理=共享生成器。MCP 标准化已达 70-80%（两前提中第二开关快速打开） | 追踪独立 CP 厂商融资/增长；验证可追溯性护城河量化阈值 | 部分验证（MCP 标准化强验证，独立厂商数据待收集） |
| 认知分工终态定理：发散 = 1 人 + AI，收敛 = 多独立视角。共同锚点 = 偏差换噪声 | 对照实验：共享 AI vs 不同 AI vs 无 AI | 待实验设计 |
| 全球南方 AI 跃迁双速定理：AI 可跳过技术层，不可跳过制度层 | 找同时加速个体 + 组织的成功案例 | 待案例收集 |
| 中国 AI 双速瓶颈：高政策推动 × 低组织准备度。瓶颈 = 科层碎片 + FinOps 缺失 | 找 Token FinOps 实际建立案例 | 待案例收集 |
| 合成数据自举边界：天花板 = f(任务结构化程度 × 验证器质量) | 找合成数据训练使模型超越训练分布的任务类型 | 待实证 |
| 模型可解释性缺口：Agent 推理链可解释性 > 单模型 XAI 供给 | 测量 agent 推理链中"不可解释步骤"的比例 | 待工具/方法 |
| 判断力净退化期量化：不同判断力类型有不同退化曲线 | 各类型退化曲线测量 | 待纵向研究 |
| Loop 三前提定理：Loop > Prompt ⟺ SNR > θ ∧ 变异分析 ∧ 延迟 << τ。任一违反 → Prompt ≥ Loop | 对照实验：高/低 SNR × 有/无变异分析 × 快/慢延迟的 2³ 设计 | 待实验设计 |
| 增强陷阱热力学：人类参与线 = 耗散结构，维持代价递增而动力递减。10 分钟 AI 使用即可观测退化 | 追踪 Liu et al. 后续研究；调查"轻度使用者不退化"阈值 | 待纵向验证 |

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
| P0 | Loop Engineering | 知识库完全缺失 | Ng/Cherny/Steinberger + **Fareed Khan 17 技术** | clip + 建 entity |
| P0 | Agent Identity & IAM | 知识库完全缺失 | Forrester/SPIFFE/SPIRE agent identity | clip + 建 entity |
| P0 | Spec-Driven Development | 知识库完全缺失 | AWS Kiro/GitHub Spec Kit/Tessl | clip + 建 entity |
| P1 | Token FinOps entity + topic | 3 raw 待编译 | raw 已到齐 | compile → 建 entity |
| P1 | AI-Native Testing topic | 07-03 roundtable 完成 | raw 已到齐 | 回填 → 建 topic |
| P1 | AI Governance Regimes comparison | 07-03 roundtable 完成 | raw 已到齐 | 回填 → 建 comparison |
| P1 | Agent Observability topic | 4 entity 零承载 | Datadog/New Relic APM 演化史 | 建 topic skeleton |
| P1 | Skill Engineering topic | 5 entity + 07-03 新剪藏 | Anthropic Skill Engineering 实践 raw | compile → 建 topic |
| P2 | 死 topic 清理（9 个零入链） | 详见 [[inventory-20260707]] | — | 补内容 or 归档 |
| P2 | 模型可解释性 (XAI) | 仅 3 处提及 | mechanistic interpretability 文献 | clip + 评估 |
| P0 | Output #1: 认知分工终态定理 | 4 轮辩证最高密度 | 07-06 研究日志原料充足 | 写 output |
| P0 | Context Engineering topic | 6 entity 已就绪 | 外部共识已形成 | 建 topic skeleton |
| P0 | Comparison 层激活 | 13/19 零入链 | 已知哪些 topic 应引用 | 补引用 |
| P1 | Agent Security topic | 11 entity 簇 | 已有 entity | 建 topic skeleton |
| P1 | Agent Memory topic | 9 entity 簇 | 已有 entity | 建 topic skeleton |
| P1 | AGI Economics topic | 12 entity 簇 | 已有 entity | 建 topic skeleton |
| P1 | Output #2: AI 本体论改写 | 07-06 深度综合 | 配对反效率悖论 | 写 output |
| P2 | Agent Failure Modes entity | Braintrust Topics + 88% 事件率 | 需 clip | clip + 建 entity |
| P2 | 多模态/具身 AI entity | Microsoft CUA GA + BMW AEON | 需 clip | clip + 建 entity |
| P2 | 中国 AI Agent 生态 | Youdao/DingTalk/MiniMax | 需 clip 中文 source | clip + 建 entity |
| P2 | Q1 2026 source 补充 | 1-3 月仅 4 raw | 需定向 clip | clip |

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

### 07-09 新增问题

- **Loop Engineering 的 17 技术如何分类**——哪些是核心循环模式，哪些是外围辅助？
- **架构质量 = Token 效率**——这个等式是否成立？如果是，"好架构"首次有了直接经济度量
- **Rot 失败模式**（>100k tokens 质量退化）——这对长周期 agent 的设计意味着什么？
- **Delegative UI vs Conversational UI**——Agent 交互的下一个范式转折在哪里？
- **中国企业 Agent 实践为何在知识库中系统性缺失**——是 source 获取问题还是主题宪法过滤？

## 07-07 盘点结论摘要

> 完整缺口分析详见 [[inventory-20260707]]。

**核心发现**：307 entity / 31 topic = 9.9:1 中层断层；11 个 entity 层系统盲区；10 个缺失 topic；6 个缺失 comparison。

## 07-09 深度探索结论（本次新增）

> 完整分析（10 个新簇、主题宪法审计、Output 转化分析、外部信号表）详见 [[inventory-20260709]]。

**五大发现**：
1. **10 个新 entity 簇**无 topic 承载（安全 11 / 记忆 9 / AGI 经济学 12 / Token 经济学 6 / Context 6 / 人-AI 协作 6 / 采纳部署 7 / LLM 病理 7 / 评测 7 / SE 范式 7）
2. **Layer 3 自反性缺口**："刀不能削自己的把"——Knowledge Compilation/Context Engineering 无 topic，无质量度量 entity
3. **链接架构根因**：单向链接导致 9 个 topic 零入链；entity 需添加 `topics:` 字段
4. **编译已完全追上**（0 pending raw）
5. **Output 三大推荐**：认知分工终态定理 / AI 本体论改写+反效率悖论 / Control Plane 壁垒转移

**假设验证更新**（3 个增强）：
- Control Plane 壁垒转移 → **增强**（Control Plane vs Orchestration 正式分层）
- Agent Identity 危机 → **增强**（Identiverse 2026 确认 Visibility ≠ Enforcement）
- Loop Engineering 杠杆 → **增强**（17 技术分类学出现）

**新外部信号**（07-07 后）：Loop Engineering 17 技术分类学 / Kiro 替代 Amazon Q / Fortune 500 80%→17% 裂缝 / Context Engineering = 2026 #1 技能 / 88% 组织报告 Agent 事件 / Microsoft CUA GA / 中国 AI Agent 生态（Youdao/DingTalk/MiniMax）

### 07-09 优先启动（P0）

1. **Output 断层破冰** → 写认知分工终态定理 output（最高辩证密度，4 轮辩证）
2. **Loop Engineering entity + topic** → clip Fareed Khan 17 技术 → 建 entity
3. **Context Engineering topic** → 6 entity 已就绪 → 建 topic skeleton
4. **Comparison 层激活** → 为 13 个零入链 comparison 补 topic 引用
5. **链接架构修复** → 为 entity 添加 `topics:` frontmatter 字段

### 07-09 短期推进（P1）

6. Agent Security topic（11 entity 簇）→ 7. Agent Memory topic（9 entity 簇）→ 8. Spec-Driven Development entity（Kiro/Spec Kit）→ 9. AGI Economics topic（12 entity 簇）→ 10. Token Economics topic（6 entity）→ 11. Agent Identity entity → 12. AI Ontology Rewriting output

## 最近思考结论摘要

> 只保留最近 5 条；更早见 [[resolved-judgments]]。

| 时间 | 焦点 | 临界发现 |
|------|------|---------|
| 2026-07-09 | Control Plane壁垒转移修正 | 壁垒=四维重组非单向迁移；护城河=中立性×可追溯性×信任；终局按买方分层；执行-评估分离定理=与认知分工终态的共享生成器；MCP标准化70-80%（窗口在打开） |
| 2026-07-09 | Loop杠杆定理边界条件 | 三前提定理（SNR+变异分析+延迟匹配）；边际递减从第4层起急剧下降；人类参与线=耗散结构非Gödel不可能；增强陷阱=热力学困境工程化；外部证据：10分钟AI使用即可观测退化 |
| 2026-07-09 | 全量盘点+深度探索 | 10个新entity簇无topic（安全11/记忆9/AGI经济学12/Token经济学6等）；L3自反性缺口（刀不削把）；单向链接架构=9个topic零入链根因；3个假设获外部增强；Output三大推荐确定 |
| 2026-07-07 | 图谱中层断层——Topic聚合=第五动作 | LLM Wiki四动作缺失"跨entity综合为topic"。9.7:1=结构性缺陷非内容量问题。第五动作=synthesize/surface，触发=entity簇密度检测 |
| 2026-07-06 | 认知分工终态定理（修正版） | 发散=1人+AI，收敛=四条件独立判断源。共同锚点=偏差换噪声。个体锚点需外部他者破解 |

## 思考日志索引

- [[2026-07-09]] — 深度探索：5 个并行 agent 全量盘点 + 外部信号扫描。10 新簇发现 / L3 自反性 / 链接架构根因 / 假设三增强 / Output 三推荐 + 深度思考①：Loop 杠杆定理边界条件（三前提/边际递减/人类参与线=耗散/增强陷阱） + 深度思考②：Control Plane 壁垒转移修正（四维重组/组合护城河/执行-评估分离定理/MCP标准化70-80%强验证）
- [[inventory-20260709]] — 07-09 深度探索详细记录（簇分析/宪法审计/Output转化/外部信号）
- [[2026-07-07]] — 9 轮：模型可解释性 / 全球南方跃迁 / 中国双速 / Exit-Sovereignty / Token FinOps / 净退化期 / 编码杠杆 / 记忆衰减 / 图谱中层断层（+roundtable×8+自反×1）
- [[2026-07-06]] — 10 轮：失败空间迁移 / AI评测制度化 / 认知分工 / 后果真实性 / 判断力扰动 / Agent Identity / Loop Engineering / Spec-Driven / Control Plane / 合成数据自举
- [[2026-07-04]] — 11 轮：可博弈性三重奏 / Agent生命周期 / Computer Use / Headless Agent / 元方法论 / Agent安全 / AGI经济学 / 重组双向制度 / 治理内生性 / 时间不对称 / Context Advantage
- [[2026-07-03]] — 15 轮：Agent Obs / 代理-现实差距 / Compliance-as-Code / Reward Hacking / Agent协议 / Context工具衰减 / 多Agent编排 / Skill Engineering / Token FinOps / 记忆 / 认知背离 / AI-native测试 / AI治理 / Agent框架 / 认知背离
- [[2026-07-02]] — 31 轮含元合成：评测/记忆/灵活性/治理/认知/全球南方/控制平面/AI认知/Headless/Harness/多Agent倒U/AGI经济学/中国AI/元合成rank/Context Advantage/Goodhart Soros Gödel/重组制度/治理内生性/判断力扰动/后果真实性/Token FinOps
- [[2026-07-01]] — 12 轮：协调/记忆/评测/治理/判断力/经济学/组织/Agent/CU/Reward/动态环境
- [[2026-06-30]] — 全库盘点 + 多轮探索
- [[exploration-archive-20260628]] — 06-28 全库快照 + 方向库 + 长问题库 + 07-04/07-07 卸载内容
- [[inventory-20260707]] — 07-07 全量盘点详细记录（缺口表/方向表/死topic）
- [[inventory-20260709]] — 07-09 深度探索详细记录（10新簇/宪法审计/Output转化/18外部信号）
- [[research-snapshot-20260703]] — 07-03 图谱健康度快照 + 成簇分析 + 缺失领域
- [[resolved-judgments]] — 已收敛判断（5 批次共 61 条）
- [[resolved-principles]] — 已收敛操作原则（9 条）
