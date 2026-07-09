---
type: research-archive
title: "07-09 深度探索详细记录"
created: 2026-07-09
tags:
  - research-archive
  - inventory
  - deep-exploration
---

# 07-09 深度探索详细记录

> 本次探索基于 318 entities / 33 topics / 19 comparisons / 5 outputs / 190 sources / 187 raw 的全量盘点，加上 5 个并行 agent 的结构分析 + 外部信号扫描。

## 一、图谱健康度更新（07-09 实测）

| 指标 | 07-07 报告 | 07-09 实测 | 变化 |
|------|-----------|-----------|------|
| Entity | 307 | **318** | +11 |
| Topic | 31 | **33** | +2 |
| Comparison | 19 | 19 | 0 |
| Output | 5 | 5 | 0 |
| Source | 180 | **190** | +10 |
| Raw | 180 | **187** | +7 |
| Entity:Topic 比 | 9.9:1 | **9.6:1** | 略改善 |
| 待编译 raw | 2 | **0** | 编译已完全追上 |
| 零入链 comparison | 13/19 (68%) | 13/19 (68%) | 未变 |
| 零入链 topic | 9 | **9**（确认） | 未变 |

## 二、新发现的 Entity 簇（无 topic 承载）

### 10 个新簇（按密度排序）

| 簇 | Entity 数 | 成员 | 为什么需要 topic |
|----|----------|------|----------------|
| **AGI Economics 理论** | 12 | AGI-Economics, Allocation-Economy, Always-On-Economy, Demand-Collapse, Relational-Sector, Drip-Scenario, Intrinsic-Wealth-Accumulation, Minsky-Paradox, Jevons-Paradox ×2, Carbon-Silicon-Division, O-Ring-Effect | Imas/Trammell 框架 cohesive；现有 AI-Era-Economy-Shift 太窄 |
| **Agent 安全与对抗防御** | 11 | Agent-Containment, Agent-Traps, Agent-Perception-Gap, Cybersecurity-Openness/Proof-of-Work, Prompt-Injection-Risk, MosaicLeaks, Security-Hardening-Phase, Model-Safety-Divergence, Custom-Policy-Guardrails, PA-DR | Multi-Agent-Pathology 只覆盖病理学非安全 |
| **Agent 记忆架构** | 9 | Memory-Architecture, Multi-Layer-Memory, Three-Layer-Agent-Memory, Structured-Agent-Memory, Memory-Summary-Page, Memory-Synthesis, Shared-Memory-Contamination, Dreaming, Staleness-Problem | Agent-Knowledge-Management 是人类知识管理非 agent 记忆 |
| **AI 采纳与部署生命周期** | 7 | Agent-Adoption-Curve, AI-Deployment-Valley-of-Death, AI-Deployment-Invisible-Costs, Standard-AI-Product-Adoption, Deployment-Product-Flywheel, AI-Developer-Power-User-Gap, Integration-Wall | pilot→ROI 完整弧线；FDE topic 太窄 |
| **LLM 能力病理学** | 7 | Jagged-Intelligence, Ghost-Intelligence, AI-Lacks-Laziness, Bias-to-Action-LLM, AI-Psychosis, Slopocalypse, Autoregressive-Generation | 区别于 multi-agent 病理学 |
| **Agent 评测与基准** | 7 | Verifiability, Evaluation-Set, Minimal-Pair-Evaluation, Corrective-RAG, CORE-Bench, SWE-Bench, ITBench | 评测方法论 vs 生产验证不同维度 |
| **软件工程范式演进** | 7 | Software-2.0, Software-3.0, Compound-Engineering, Constraint-Driven-Engineering, Laziness-Virtue, YAGNI, Vibe-Coding | Karpathy-AI-Thought 太窄 |
| **Token 经济学** | 6 | Token-Maxing, Tokenpocalypse, Sleep-Token, Token-Supply-Chain, Agentic-Workflow-Token-Efficiency, Sequence-Packing | Token 作为生产投入的经济学 |
| **Context Engineering 生命周期** | 6 | Context-Engineering, Context-Minimalism, Context-Rot, Context-Advantage, Sufficient-Context, CLAUDE-md | 区别于 Memory（持久性 vs 推理时） |
| **人-AI 协作模式** | 6 | Co-Intelligence, Cybernetic-Teammate, Co-Existence, Human-Signal, Human-Governor-Agent-Operator, Decide-Execute-Deliver-Sandwich | Mollick 弧线 Co-Intelligence→Co-Existence |

### 桥接 Entity（高跨簇连接性）

| Entity | 桥接的簇 |
|--------|---------|
| Agentic-Engineering | 132 文件引用，全图谱中心节点 |
| Agent-Harness | 基础设施/记忆/安全/工作流/部署 |
| Context-Engineering | 记忆/agent 架构/验证/RAG/CLAUDE-md |
| Verifiability | 评测/安全/agent 工作流/LLM 能力 |
| Coding-Agents | 工作流/工具/采纳/知识债务/SE 实践 |

### ~40 个孤儿/近孤儿 Entity

详见探索 agent 分析。主要类别：
- 单概念 entity（Goodharts-Law, Positionality, Emergence 等）
- 产品 entity（Mythos, River-Agent, MachinaCheck）
- 科学 AI entity（Scientific-Discovery-AI, AI-in-Mathematics, Genomic-Reanalysis）→ 可组成"AI for Science"小簇

## 三、Topic 层覆盖分析

### 薄 Topic（<3 entity inlinks，含新增 2 个）

5 个零 entity list topic + 2 个新建（2026-07-09）尚无 related_entities frontmatter。

### 胖 Topic（可能需拆分）

| Topic | Entity 数 | 评估 |
|-------|----------|------|
| Verifiable-Agent-Engineering | 33 | 过宽，可拆为"验证方法"和"Agent QA" |
| Agentic-Engineering-Patterns | 25 | 边界模糊，与 Verifiable 重叠 11 entity |
| Organization-as-Agent-Harness | 25 | 与 AI-Mediated-Organization 重叠 22 entity |

### Topic 重叠簇

两组高度重叠 topic 需边界澄清：
1. {AI-Mediated-Organization, Organization-as-Agent-Harness, Agent-First-Process-Redesign, Multi-Agent-Pathology-and-Governance}
2. {Agentic-Engineering-Patterns, Verifiable-Agent-Engineering, Building-Effective-Agents}

### 链接架构根因

**单向链接问题**：topic 声明 `related_entities:` 但 entity 无 `topics:` 字段。9 个零入链 topic 的根因是 entity 从不反向指向 topic。修复方案：为 entity frontmatter 添加 `topics:` 字段。

## 四、Comparison 层分析

13/19 comparisons 零入链（68%）。仅 RAG-vs-LLM-Wiki 有 7 个引用。

### 6 个缺失 Comparison（确认）

1. Prompt Engineering vs Context Engineering
2. Workflow vs Agent
3. Frontier Models vs Specialized Small Models
4. Copilot vs Agent
5. Agent-Harness vs Agent-Swarm
6. RAG vs Context Engineering vs Knowledge Compilation（三元对比）

## 五、主题宪法覆盖度审计

| 层 | 评级 | 核心发现 |
|----|------|---------|
| **L1 软件工程** | 充分 | Agentic-Engineering（248 行/20+ source）和 Agent-Harness（350 行）是教科书级 entity |
| **L2 组织系统** | 充分 | 最广覆盖（~149 entity 匹配），FDE/AI Factory/Org-as-Harness 形成完整叙事 |
| **L3 知识系统** | **部分** | **"刀不能削自己的把"**——Knowledge Compilation/Context Engineering 无 topic；无质量度量 entity；编译管道未形式化 |
| **L4 人的核心价值** | **部分** | Taste 异常深厚（231 行/哲学纵深），其他 L4 entity 多为 50-100 行单源；Discernment/Emotional-Clarity 可能违反"工作语境约束" |

### 关键跨层桥梁

| Entity | 桥接层 |
|--------|--------|
| Agentic-Engineering | L1-L2-L4 |
| Agent-Harness | L1-L2-L3 |
| Captain-Mindset | L1-L2-L4 |
| Context-Engineering | L1-L3 |
| Friction-as-Design-Signal | L1-L3-L4 |

**最弱跨层连接**：L3→L4（知识系统如何支撑人类判断力）

## 六、Output 转化分析

### 三大推荐 Output

| 优先级 | 标题建议 | 来源判断簇 | 格式 |
|--------|---------|-----------|------|
| **#1** | "发散需要一人+AI；收敛需要独立判断源" | 认知分工终态定理（4 轮辩证，最高辩证密度） | 3000-4000 字论证文 |
| **#2** | "AI 不是在减少失败——它在改写什么是失败" | AI 本体论改写 + 反效率文化悖论（配对） | 2500-3500 字论证+处方 |
| **#3** | "护城河迁移：AI 基础设施价值从模型转向运行时治理" | Control Plane 壁垒转移定理 | 2000-2500 字战略分析 |

### 其他 Output 候选

- Goodhart/Soros/Gödel 博弈三部曲（更抽象，受众较窄）
- Jevons 主体替换修正定理（数据丰富但受众窄）
- Loop Engineering 杠杆定理（需第二个 raw 编译后才充分）

## 七、Source 层新发现

### 编译状态修正

**0 pending raw**（agenda 自报 2 已过时）。registry 完全追上。

### 新 Theme 需 Entity 创建

| Theme | Source | 建议 Entity |
|-------|--------|------------|
| Data Systems for/of/by Agents | Berkeley BAIR 07-07 | `Data-Systems-for-Agents` |
| Agents That Teach / SHIELD | 07-09 论文 | `Agents-That-Teach` |
| AI Layoff Reversal | Ford/CBA/IBM 07-02 | `AI-Layoff-Reversal` |
| Qwen C-end Agent | Alibaba 07-02 | `Qwen-Agent-Harness` |

### 时间分布缺口

- **Q1 2026（1-3 月）**：仅 4 个 raw 文件。此期间的 AI 发展几乎不可见
- **学术论文**：仅 SHIELD 论文 + 少量 arxiv。无 ICSE/NeurIPS/ICML
- **标准文档**：无 OWASP/NIST/ISO/W3C agent 规范
- **定量案例**：无 A/B 测试或对照实验数据
- **财报/盈利数据**：无上市公司的 AI 支出/ROI 一手数据

### 近期剪藏的涌现模式

1. **从 prompting 到 loop design**：7 月集群明确转向
2. **成本清算到来**：Martin Fowler 报告 $5M→$15M/月
3. **人类能力侵蚀成为一等关注**：SHIELD/Fable/Layoff Reversal 三个面向
4. **中国企业 agent 实践浮现**：Qwen/钉钉/MiniMax
5. **架构质量 = Token 效率**：首次有直接经济度量

## 八、外部新信号（07-09 搜索，07-07 之后）

| 信号 | 来源 | 含义 | 行动 |
|------|------|------|------|
| **Loop Engineering 17 技术分类学** | Fareed Khan (Level Up Coding, July 2026) | Loop 从概念→分类学阶段 | clip + 建 Loop-Engineering-Taxonomy entity |
| **Enterprise-Grade Loop Engineering** | TrueFoundry | 个人→企业 loop 跨越正在发生 | 纳入 Loop Engineering topic |
| **"Visibility ≠ Enforcement"** | Identiverse 2026 + Aembit | Agent Identity 核心 gap 被正式命名 | 建 Agent-Identity-Gap entity |
| **Control Plane vs Orchestration 分层** | TrueFoundry + Elementum + Microsoft Agent 365 | 验证 Control Plane 壁垒转移假设 | 深化假设 |
| **Fortune 500: 80% 在建/17% 生产** | Elementum 2026 | 比 S&P 31% 更严峻的生产化鸿沟 | 更新 Enterprise AI 鸿沟数据 |
| **Kiro 替代 Amazon Q（从零重建）** | AWS Summit NY 2026 | SDD 范式迁移的不可逆信号 | clip + 建 Spec-Driven-Development entity |
| **Spec Kit 111K GitHub stars** | productbuilder.net | 社区侧 SDD 采纳超预期 | 纳入 SDD entity |
| **Context Engineering = 2026 #1 技能** | 多方引用 Karpathy 定义 | 需升级为 topic | 建 Context-Engineering topic |
| **Mayfield: 42% 生产/72% 试点/13% 全规模** | X/AMD thread | 生产化快但规模化极慢 | 更新采纳数据 |
| **KDD 2026 Agentic AI Evaluation Workshop** | KDD | 学术侧评测正式化 | clip + 追踪 |
| **88% 组织报告 Agent 事件** | Gravitee 安全报告 | 隐性失败 > 显性失败 | 建 Agent-Failure-Modes entity |
| **"Rot" 失败模式（>100k tokens）** | Mastra/Principles of Building AI Agents | 新失败类型学 | 纳入 Agent-Failure-Modes |
| **Microsoft CUA GA (2026-05-13)** | Copilot Studio | 多模态/具身 AI 进入生产 | 建 Multimodal-Agent entity |
| **BMW 部署 AEON 人形机器人** | Hexagon Robotics (Feb 2026) | 具身 AI 制造场景 | 纳入具身 AI 簇 |
| **NVIDIA "Physical AI" at GTC 2026** | NVIDIA | 物理 AI 时代宣言 | clip + 评估 |
| **Delegative UI 范式** | UX Tigers 2026 预测 | 从 conversational→delegative | 建 Delegative-UI entity |
| **中国 AI Agent 生态** | Youdao Lobster/钉钉悟空/MiniMax M3/WAIC 2026 | 中国 agent 实践严重缺失于知识库 | clip 中文 source + 建实体 |
| **Claude Mythos 16 小时 horizon** | METR benchmark | 长周期 agent 进入实测 | 纳入 Long-Horizon-Agent |

## 九、方向优先级总表（07-09 版）

### P0 — 立即启动（服务主问题 + 知识库缺失 + 有 source）

1. **Output 断层破冰** → 写认知分工终态定理 output（最高辩证密度）
2. **Loop Engineering** → clip Fareed Khan 17 技术文 → 建 entity + topic skeleton
3. **Context Engineering topic** → 6 entity 已就绪 + 外部共识 → 建 topic
4. **Comparison 层激活** → 为 13 个零入链 comparison 补 topic 引用
5. **链接架构修复** → 为 entity 添加 `topics:` frontmatter 字段

### P1 — 短期推进（有锚点 + 需编译或 clip）

6. **Agent Security topic** → 11 entity 簇 → 建 topic skeleton
7. **Agent Memory topic** → 9 entity 簇 → 建 topic skeleton
8. **Spec-Driven Development entity** → Kiro/Spec Kit raw 已充足 → compile + 建 entity
9. **AGI Economics topic** → 12 entity 簇 → 建 topic skeleton
10. **Token Economics topic** → 6 entity + Martin Fowler 成本危机 → 建 topic
11. **Agent Identity entity** → Identiverse/Aembit raw → clip + 建 entity
12. **AI Ontology Rewriting output** → 配对反效率悖论 → 写 output

### P2 — 中期深化

13. **Agent Failure Modes entity** → Braintrust Topics + 88% 事件率 → clip + 建 entity
14. **Multimodal/Embodied AI** → Microsoft CUA GA + BMW AEON → clip + 建 entity
15. **中国 AI Agent 生态** → Youdao/DingTalk/MiniMax → clip 中文 source
16. **Control Plane output** → 壁垒转移定理 → 写战略分析 output
17. **Delegative UI entity** → UX paradigm shift → clip + 建 entity
18. **Knowledge Quality Metrics entity** → L3 自反性缺口 → 设计 + 建 entity
19. **缺失 Comparison Top 3** → Prompt vs Context / Workflow vs Agent / Copilot vs Agent

### 持续维护

20. **Q1 2026 source 补充** → 1-3 月仅 4 raw → 定向 clip
21. **学术论文和标准文档** → source 类型严重偏斜 → 定向 clip
22. **死 topic 处置** → 9 个零入链 topic → 逐个判定
23. **胖 topic 拆分评估** → Verifiable-Agent-Engineering(33) / Agentic-Engineering-Patterns(25) / Org-as-Agent-Harness(25)
24. **Discernment/Emotional-Clarity 去留** → 是否满足"工作语境约束"

## 十、假设验证更新

| 假设 | 新证据 | 状态变化 |
|------|--------|---------|
| Control Plane 壁垒转移定理 | Control Plane vs Orchestration 正式分层；Microsoft Agent 365 vs workflow platforms | **增强**——市场正在按假设分化 |
| Agent Identity 危机定理 | Identiverse 2026 确认 Visibility ≠ Enforcement | **增强**——核心 gap 被行业命名 |
| Loop Engineering 杠杆定理 | 17 技术分类学；Enterprise-grade loop 出现 | **增强**——从概念到分类学 |
| 全球南方 AI 跃迁双速定理 | 泰国 SME agent 生态系统论文（APIT 2026） | 微弱证据，仍需更多案例 |
| 合成数据自举边界 | 无新证据 | 未变 |
| 模型可解释性缺口 | 无新证据 | 未变 |
| 判断力净退化期量化 | 无新证据 | 未变 |
