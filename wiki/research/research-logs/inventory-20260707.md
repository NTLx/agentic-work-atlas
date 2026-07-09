---
type: research-archive
title: "07-07 全量盘点详细记录"
created: 2026-07-07
updated: 2026-07-09
tags:
  - research-archive
  - inventory
---

# 07-07 全量盘点详细记录

> 本文档从 research-agenda.md 卸载，保存 07-07 深度盘点的完整缺口分析和方向表。

## Entity 层主题缺口（307 entity 审计）

| 缺失主题 | 详情 | 为什么重要 |
|----------|------|-----------|
| **多模态/具身 AI** | 零 entity。知识库严重偏向 text/code 中心 | Agent 的行动面正从 API 扩展到视觉/GUI/物理世界 |
| **AI 监管与法律（细节层）** | 仅原则层 governance entity，无 EU AI Act/US EO/CN 法规的具体 entity | 监管正从原则→具体执法 |
| **数据与训练方法** | 几乎空白：无 data curation/synthetic data/training flywheel entity | Agent 时代的核心瓶颈之一 |
| **AI 能源与可持续性** | 零 entity | Agent 24/7 运行模式的能耗结构完全未被讨论 |
| **国际/地缘 AI 动态** | 仅 Hardware-Sovereignty 触及 | US-CN 竞争、出口管制、全球南方的系统性缺失 |
| **AI 伦理与道德哲学** | 无系统处理 | 仅 Positionality/Ownership 触及边缘 |
| **Agent 时代 HCI/UX** | 仅 ACI/Agent-Ergonomics 两个 entity | 人机交互界面正在被 Agent 重写 |
| **教育与培训系统** | 仅 Lehrwerkstatt/Osmosis-Learning | 大学和培训体系如何适应 Agent 时代 |
| **Agent 失败模式分类学** | Agent-Traps/Multi-Agent-Pathology 存在但无系统分类 | 实际部署中最需要的就是失败模式知识库 |
| **AI 保险与责任** | 零 entity | Agent 造成损害时谁负责——生产化的前提条件 |
| **开源 AI 生态** | 仅 Cybersecurity-Openness 触及 | open-weight models/开源 agent 框架/开放vs封闭辩论 |

## 结构性缺口

| 缺口 | 详情 | 优先级 |
|------|------|--------|
| **Comparison 层严重欠链接** | 13/19 comparisons（68%）零入链 | **P0** |
| **Output 层终端孤岛** | 5 output 零被引；34 天无新产出；61 条收敛判断未被消费。转化率 1.6% | **P0** |
| **9 个 topic 零入链** | Agentic-AI-Ecosystem/AI-Management-Mindset-Transfer/AI-Mathematics-Future/AI-Mediated-Organization/CEO-Hands-On-AI/Karpathy-AI-Thought/Lean-Indie-Engineering/OpenClaw-Agent-System/模型安全分歧 | P1 |
| **安全簇稀疏** | AISI/Mythos/Agent-Containment 等仅 2 topic 覆盖 | P1 |
| **Research log 格式不一致** | 早期 log 有 blockquote 摘要，后期缺失；07-06/07-07 缺 frontmatter | P2 |

## 缺失 Topic（entity 簇已有但无 topic 承载）

| 缺失 Topic | 锚点 entity 数 | 为什么重要 |
|------------|---------------|-----------|
| **Agent Harness** | 11 entity 链入 Organization-as-Agent-Harness | 知识库最核心概念之一 |
| **Coding Agents** | 多个 topic 引用 Coding-Agents entity | Claude Code/Codex/Gemini CLI 工具谱系 |
| **Context Engineering** | Context-Engineering entity + comparison 存在 | 与 Prompt Engineering 的进阶关系 |
| **Agent Orchestration** | Agent-Orchestration/Agent-Swarm entity | 编排架构与 Multi-Agent-Pathology 不同维度 |
| **Knowledge Compilation** | LLM Wiki 核心操作 | 仅通过 Agent-Knowledge-Management 间接覆盖 |
| **Vibe Coding / Software 3.0** | Karpathy 系列 + 3 个 comparison | 有丰富 comparison 但无独立 topic |
| **Token Supply Chain / Model Economics** | Token-Supply-Chain entity | Token 作为生产资料的经济学 |
| **Verifiability** | 24+ entity 引用 | 知识库最高被引概念之一 |
| **Headless Agent** | 07-04 深度探索产出 | 已收敛判断但无 topic 承载 |
| **Agent-to-Agent Economy** | Settlement-Mechanism/Agent-Economic-Protocols entity | 多 Agent 经济系统 |

## 缺失 Comparison

| 缺失 Comparison | 为什么重要 |
|-----------------|-----------|
| **Prompt Engineering vs Context Engineering** | 从"写更好的 prompt"到"设计更好的 context" |
| **Workflow vs Agent** | Anthropic Building Effective Agents 的核心区分 |
| **Frontier Models vs Specialized Small Models** | 不同于 Closed-vs-Open 的另一维度 |
| **Copilot vs Agent** | 两种人机协作模式 |
| **Agent-Harness vs Agent-Swarm** | 两种多 Agent 架构的系统对比 |
| **RAG vs Context Engineering vs Knowledge Compilation** | 知识管理栈三层对比 |

## 外部现实新信号（07-07 搜索发现）

| 信号 | 来源 | 含义 | 行动 |
|------|------|------|------|
| **AI 评测制度化加速** | US AI Incident Reporting Act (2026-06-26) | 从自愿→强制的质变 | 追踪首次执法 |
| **Anthropic Economic Index** | Anthropic 2026H1 报告 | 开发者 60% 工作用 AI，仅 0-20% 可完全委托 | 深化"可委托性边界" |
| **Databricks 多 Agent 增长 327%** | Databricks 2026 报告 | Supervisor Agent 模式占 37% | 追踪编排模式演化 |
| **Forrester Agent Sprawl** | Forrester 2026 | >50% 企业报告 agentic sprawl | 建 Agent Sprawl 治理 entity |
| **S&P Global: 31% 生产化率** | S&P Global 2026 | 80% 嵌入 agent 但仅 31% 进生产 | 深化 Enterprise AI 鸿沟 |
| **Gartner: 40% AI 项目将取消** | Gartner 2026 预测 | AI 部署死亡谷量化 | 追踪实际取消率 |

## 死 topic 清理（9 个零入链）

| Topic | 状态建议 |
|-------|---------|
| `Agentic-AI-Ecosystem` | 补承载（整合 Agent 互操作协议簇 + Token Supply Chain） |
| `AI-Management-Mindset-Transfer` | 补承载（有 AI-Capability-Management-Alignment entity） |
| `AI-Mathematics-Future` | 补承载（有 AI-in-Mathematics entity） |
| `AI-Mediated-Organization` | ⚠️ 高质量内容但零入链——需从 Organization-as-Agent-Harness 等添加反向链接 |
| `CEO-Hands-On-AI` | 补承载 or 归档 |
| `Karpathy-AI-Thought` | ⚠️ 综合性强但零入链——需从 Software-2.0/Vibe-Coding/LLM-Wiki entity 添加反向链接 |
| `Lean-Indie-Engineering` | 补承载 or 归档 |
| `OpenClaw-Agent-System` | ⚠️ 高质量内容但零入链——需从 Agent-Harness/Claude-Code-Automation 添加反向链接 |
| `模型安全分歧` | 补承载（安全簇 16 entity 待建 topic，可合并入新 Agent Safety topic） |

## 方向优先级总表（07-07 版）

### P0 — 直接服务主问题且知识库缺失

1. **Loop Engineering** — 新范式。Ng 三循环框架
2. **Agent Identity & IAM** — 非人类 identity 核心瓶颈
3. **Spec-Driven Development** — Vibe→Spec 范式迁移
4. **Agent Sprawl 治理** — >50% 企业 sprawl
5. **Comparison 层激活** — 13/19 零入链
6. **Output 断层紧急修复** — 1.6% 转化率
7. **缺失 Topic 补建（Top 5）** — Agent Harness / Context Engineering / Verifiability / Knowledge Compilation / Headless Agent

### P1 — 有锚点待深化

- Agentic Software 理论（Cao 2026）
- 多 Agent 编排 vs Loop 编排边界
- AI 治理与生产化因果关系
- Enterprise AI 鸿沟（80% vs 31%）
- 知识库元方法论深化
- MCP 生态治理
- AI 使用节律与认知健康
- 认知债务新型态
- Agent-to-Agent 经济与支付
- 安全簇 topic 建设
- 缺失 Comparison 补建（Top 3）

### P2 — 需补 source

- 合成数据自举边界
- AI 能源与环境可持续性
- 模型可解释性 Agent 时代缺口
- 全球南方 AI 跃迁实证案例
- 多模态/具身 AI
- Agent 失败模式分类学
- AI 保险与责任框架
- Agent 时代 HCI/UX 设计范式
- 开源 AI 生态与开放vs封闭辩论
