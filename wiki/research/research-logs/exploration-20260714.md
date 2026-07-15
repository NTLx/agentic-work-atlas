---
type: research-archive
title: "07-14 深度探索详细记录"
created: 2026-07-14
tags:
  - research-archive
  - exploration
  - external-signals
---

# 07-14 深度探索详细记录

> 基于外部信号扫描（38 条发现）+ 知识库自反分析（328 entity / 33 topic / 19 comparison / 5 output）。

## 一、外部信号 Top 10（07-10 ~ 07-14）

### 1. xAI Grok Build CLI 信任边界危机（07-10~14，持续发酵）
- **事件**：Grok Build CLI 在用户说"不要读任何文件"时仍上传整个 git repo（含密钥），opt-out 无效
- **数据**：12GB repo 上传 5.1GB，模型实际只用 192KB（~27,800× 过度收集）；.env 密钥明文传输
- **对比**：Claude Code / Codex / Gemini 无此行为；xAI 静默服务端关闭，未发公告
- **来源**：[Wire analysis](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547) | [Reproduce](https://github.com/cereblab/grok-build-exfil-repro) | [Comparison](https://github.com/cereblab/grok-build-exfil-repro/blob/main/COMPARISON.md)
- **对本库意义**：Agent 信任边界的标志性事件 → 新方向：Agent 数据治理与信任边界

### 2. 豆包/通义千问 Agent 功能强制关闭（07-15 生效）
- **事件**：中国《拟人化 AI 交互服务管理暂行办法》7/15 生效，字节豆包（3.45亿 MAU）和阿里通义千问关闭用户自建 Agent 功能
- **影响**：10/15 后用户数据清除；中国 AI Agent C 端生态重大转折
- **来源**：[TechNode](https://technode.com/2026/07/06/bytedances-doubao-and-alibabas-qwen-to-shut-down-ai-agent-features-on-july-15) | [Bloomberg](https://www.bloomberg.com/news/articles/2026-07-06/bytedance-alibaba-pull-ai-companions-as-beijing-tightens-rules)
- **对本库意义**：中国 AI Agent 监管的标志性事件 → 新方向：中国 AI 监管

### 3. SPIFFE/SPIRE Agent 身份突破
- **事件**：Joe Beda（SPIFFE 联合作者）+ IEEE 论文 + HashiCorp Vault 1.21 原生支持
- **关键发现**：Bearer token 在 agent 场景系统性失败（ambient authority）；SPIFFE 基于证书的工作负载身份消除静态 API key；root agent→sub-agent 凭证传递是核心架构挑战
- **来源**：[Stacklok](https://stacklok.com/blog/agentic-identity-explained) | [IEEE](https://ieeexplore.ieee.org/document/11431026) | [HashiCorp](https://www.hashicorp.com/en/blog/spiffe-securing-the-identity-of-agentic-ai-and-non-human-actors)
- **对本库意义**：Agent Identity 方向最强验证信号

### 4. 腾讯混元 Hy3：中国 Agent 里程碑
- **事件**：295B MoE（仅激活 21B），Apache 2.0 开源；ReAct 作者姚顺雨（27岁清华姚班）加入腾讯后首个正式模型
- **数据**：ClawEval 68.5 超 DeepSeek V4 Pro 和 Qwen 3.7 Max；BrowseComp 84.2 追平 GPT-5.5；WorkBuddy 任务解决率 72%→90%
- **来源**：[腾讯](https://www.tencent.com/zh-cn/articles/2202386.html)
- **对本库意义**：中国 AI Agent 生态的模型层突破

### 5. Loop Engineering 成为主流学科
- **事件**：Data Science Dojo 发布 10 大设计模式；AI Builder Club 发布指南；Towards AI 发布 7 大设计模式
- **核心洞察**：在任何循环中，验证器是瓶颈，不是模型
- **来源**：[10 Patterns](https://datasciencedojo.com/blog/loop-engineering-design-patterns) | [7 Patterns](https://pub.towardsai.net/the-7-design-patterns-every-ai-agent-developer-should-know-in-2026)
- **对本库意义**：Loop Engineering 方向最强外部验证

### 6. SDD 工具生态成熟
- **事件**：Spec Kit（111K★）vs AWS Kiro vs Tessl 三强对比；ThoughtWorks Birgitta Bockeler 三层分类法
- **来源**：[对比](https://particula.tech/blog/spec-driven-development-tools-spec-kit-vs-kiro-vs-tessl) | [SDD 2026](https://dev.to/krlz/spec-driven-development-in-2026)
- **对本库意义**：SDD 从理念到工具的完整生态

### 7. Context Engineering 独立学科地位确认
- **事件**：Anthropic 定义 + 五大核心模式（Progressive Disclosure / Compression / Routing / Retrieval / Tool Management）
- **来源**：[Sourcegraph Guide](https://sourcegraph.com/blog/context-engineering) | [State of CE 2026](https://pub.towardsai.net/state-of-context-engineering-in-2026)
- **对本库意义**：Context Engineering 方向最强外部验证

### 8. Token FinOps 独立品类确认
- **事件**：Helicone / Portkey / LiteLLM / Langfuse / Amnic / Kong 等 9+ 工具形成独立品类
- **数据**：agent 推理成本 = 月度 burn rate 18-27%；优化可降低 80%；Tokenizer 差异致标称价与实际成本严重偏离
- **来源**：[Top 8 Tools](https://amnic.com/blogs/ai-token-management-tools) | [Cost Optimization](https://regolo.ai/token-cost-optimization-in-2026) | [Real Price](https://playcode.io/blog/real-price-of-frontier-models)
- **对本库意义**：Token FinOps 假设最强实证

### 9. GPT-5.6 数学突破：AI 作为科学基础设施
- **事件**：GPT-5.6 Sol Ultra 一小时证明 50 年图论猜想（循环双覆盖猜想）
- **来源**：[IT之家](https://www.ithome.com/0/975/646.htm) | [OpenAI PDF](https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_proof.pdf)
- **对本库意义**：AI 能力边界扩展 → "知识工作"定义需要重划

### 10. 中国大厂 Agent 路线三极分化
- **事件**：阿里（钉钉悟空，B 端路线）/ 腾讯（QClaw+WorkBuddy，双线包抄）/ 字节（TRAE SOLO，工作台路线）
- **来源**：[36kr](https://www.36kr.com/p/3747994426897156)
- **对本库意义**：中国 Agent 生态的结构性分析框架

## 二、知识库五盲区（系统自反发现）

### 盲区 1：Agent Observability（零 entity！）
- **现状**：328 entity 中无任何 Agent Observability 相关 entity
- **外部信号**：Mindwalk（3D Agent 轨迹回放）；AI 评测框架 7 个比较；lab-prod gap 37%
- **为什么严重**：Observability 是 Agent 工程化的前提——没有观测就没有治理
- **建议**：clip Mindwalk + Datadog/New Relic APM 演化史 → 建 Agent-Observability entity + topic

### 盲区 2：Agent 信任边界与数据治理（零 entity）
- **现状**：无 entity 覆盖 agent 数据收集边界、最小权限、数据外泄防护
- **外部信号**：Grok Build CLI 事件是系统性问题的冰山一角
- **建议**：clip Grok 事件分析 + agent 数据治理最佳实践 → 建 Agent-Trust-Boundary entity

### 盲区 3：中国 AI 监管（零 entity）
- **现状**：无 entity 覆盖中国 AI 监管政策或拟人化管理办法
- **外部信号**：7/15 生效的监管直接关闭了 3.45 亿 MAU 平台的 Agent 功能
- **建议**：clip 政策原文 + 影响分析 → 建 China-AI-Agent-Regulation entity

### 盲区 4：多模型策略与路由（零 entity）
- **现状**：无 entity 覆盖模型选择、路由、成本优化策略
- **外部信号**：Tokenizer 差异致隐性涨价；多模型成本优化是独立需求
- **建议**：clip 实际价格分析 → 评估建 Model-Routing entity

### 盲区 5：具身 AI 与 Agent 交汇（零 entity）
- **现状**：零 entity 覆盖机器人/具身智能/Computer Use
- **外部信号**：宇树 G1 活体手术；蚂蚁 LingBot-VA 2.0（首个原生具身基础模型）；Microsoft CUA GA
- **建议**：clip 代表性案例 → 评估建 Embodied-AI entity

## 三、Entity 演变（07-09 → 07-14）

### 新增 16 entity（07-10~07-14）

| 新增 Entity | 日期 | 归属簇 |
|------------|------|--------|
| Agent-Unit-of-Work | 07-14 | Agent 任务规划 |
| AI-Assisted-Port | 07-13 | 软件工程 |
| Cognitive-Offloading | 07-09 | 认知经济学 |
| Distinct-Principal-Identity | 07-13 | Agent Identity |
| Goodharts-Law | 07-09 | AI 评测/治理 |
| Incidental-Learning | 07-09 | 认知经济学 |
| Knowledge-Debt | 07-09 | 认知经济学 |
| Plan-is-the-Permission | 07-13 | Agent 任务规划/治理 |
| Pro-Worker-AI | 07-09 | AI 政策/劳动 |
| Retrieval-as-a-Subagent | 07-14 | Agent 架构 |
| Reverse-Information-Paradox | 07-13 | 组织系统/AI 安全 |
| Reward-Hacking | 07-09 | AI 安全 |
| Rubric-Based-Evaluation | 07-14 | AI 评测 |
| Self-Hosted-Models | 07-14 | AI 部署 |
| SHIELD | 07-09 | 认知经济学/AI 安全 |
| Task-Framework | 07-09 | Agent 任务规划 |

### 新兴簇识别（07-09 基线 + 07-14 补充）

| 新兴簇 | Entity | 评估 |
|--------|--------|------|
| **Agent 任务规划与分解** | Agent-Unit-of-Work, Task-Framework, Plan-is-the-Permission, Plan-as-Agent-Checkpoint, Task-Horizon, Agent-Workflow-Patterns | ~6 entity，需独立 topic |
| **认知经济学** | Cognitive-Offloading, Incidental-Learning, Knowledge-Debt, Cognitive-Debt, Cognitive-Surrender, SHIELD | ~6 entity，与 Skill-Atrophy 交叉 |
| **Agent 部署与基础设施** | Self-Hosted-Models, AI-Assisted-Port, Agent-Infra, Headless-Automation | ~4 entity，薄但可增长 |

### Explore Agent 补充：三大新 Cluster（07-09 未识别）

#### Cluster A: Agent Governance & Delegation（5 entity）
- Distinct-Principal-Identity + Plan-is-the-Permission + Agent-Unit-of-Work + Plan-as-Agent-Checkpoint + Policy-as-Code-for-Agent-Governance
- **定义**：将 Agent 作为组织内的独立行动主体（principal），通过身份隔离、计划即权限、工作单元粒度和可执行策略四维度实现企业级 Agent 委派与治理
- **来源**：Martin Fowler 2026-07 Fragments + Microsoft/Vercel 企业 Agent 落地材料
- **当前归属**：被 Multi-Agent-Pathology-and-Governance 和 Verifiable-Agent-Engineering 部分覆盖，无独立 topic

#### Cluster B: Cognitive Safety & Skill Atrophy（4 entity）
- Cognitive-Offloading + Knowledge-Debt + Incidental-Learning + SHIELD
- **定义**：AI 委托的认知副作用——附带学习被短路、知识债务沉默积累、认知卸载导致能力退化，以及工程化偿还机制
- **Topic 状态**：`Skill-Atrophy-and-Knowledge-Debt` topic 已存在但 **related_entities 为空(0)**！

#### Cluster C: Evaluation Industrialization（3 entity）
- Rubric-Based-Evaluation + Goodharts-Law + Reward-Hacking
- **定义**：生产 Agent 评测工业化——从 rubric 设计、到指标失效（Goodhart）、到主动博弈（Reward Hacking）的完整问题链
- **当前归属**：被 Verifiable-Agent-Engineering 松散覆盖

### Topic 结构性问题（Explore Agent 发现）

#### 空 Topic ×3
| Topic | related_entities | Entity 是否存在 | 行动 |
|-------|-----------------|----------------|------|
| `Skill-Atrophy-and-Knowledge-Debt` | **0** | ✅ 4 entity 已存在未关联 | 立即填充 related_entities |
| `Pro-Worker-AI-and-Labor-Policy` | **0** | ✅ 6+ entity 可关联 | 填充 or 归档 |
| `模型安全分歧` | **0** | ✅ 1 entity 可关联 | 填充 + 考虑统一命名为英文 |

#### 胖 Topic 需拆分
| Topic | Entity 数 | 建议拆分 |
|-------|----------|---------|
| `Verifiable-Agent-Engineering` | **33** | → Verification + Security + Evaluation |
| `Organization-as-Agent-Harness` | **25** | → Harness + Governance & Delegation |
| `Agentic-Engineering-Patterns` | **25** | → Core Patterns + Infrastructure |

### 跨领域连接缺失（Explore Agent 补充）

| 交叉领域 | 状态 | 缺失 |
|---------|------|------|
| Agent Security × Organizational Governance | 中等 | 缺 Agent-Audit-Trail, Agent-Liability, Agent-Risk-Assessment entity |
| Context Engineering × Agent Memory | **弱** | 无 comparison；缺 Context-Memory-Boundary, Context-Memory-Consistency entity |
| Token Economics × AI Adoption | **弱** | 无 comparison；缺 Token-Budget-as-Adoption-Barrier, AI-FinOps entity |
| Loop Engineering × Reliability Engineering | **弱** | 缺 Agent-SLA, Long-Running-Agent-Reliability, Agent-Chaos-Engineering entity |
| Agent Identity × IAM Standards | **弱** | 缺 Agent-OAuth, Agent-Credential-Rotation, Agent-Federation entity |
| Code Generation Quality × Technical Debt | 中等 | 缺 Agent-Code-Quality-Metrics, Vibe-Coding-Debt, Generated-Code-Maintenance entity |

## 四、Topic 覆盖度更新

### 仍需新建的 topic（07-09 清单基础上）

| Topic | Entity 簇大小 | 优先级 | 备注 |
|-------|-------------|--------|------|
| Agent Security | 11 | P0 | 07-09 已识别，持续空缺 |
| Agent Memory Systems | 9 | P0 | 同上 |
| AGI Economics | 12 | P0 | 同上 |
| Token Economics | 6→10 | P1 | Entity 增长中 |
| Context Engineering | 6 | P1 | 外部共识确认 |
| Human-AI Collaboration | 6 | P1 | |
| AI Adoption & Deployment | 7 | P1 | |
| Agent Evaluation & Testing | 7→11 | P1 | Entity 增长 |
| SE Paradigm Evolution | 7 | P2 | |
| LLM Capability Pathology | 7 | P2 | |
| **Agent Observability** 🆕 | 0 | P0 | 全新！零 entity→需先建 entity |
| **Agent Trust Boundary** 🆕 | 0 | P0 | 全新！零 entity→需先建 entity |
| **Agent Task Planning** 🆕 | ~6 | P2 | 新兴簇 |
| **Cognitive Economics** 🆕 | ~6 | P2 | 新兴簇 |

## 五、四个层面宪法审计更新

| 层面 | 覆盖充分 | 覆盖不足 | 完全缺失 |
|------|---------|---------|---------|
| **软件工程** | Agentic Engineering, verification, harness, coding agents | Tool use architecture, **Agent Observability**, **多模型策略** | — |
| **组织系统** | AI-ready org, deployment patterns, FDE | **Agent 信任边界**, **中国监管合规**, 岗位演化实证 | — |
| **知识系统** | LLM Wiki, 知识编译, Context Engineering | 可复用语义层工具化, Ontology 实践 | — |
| **人的核心价值** | 判断力, 品味, 认知分工 | **AI 作为科学基础设施对"知识工作"的冲击**, 责任承担机制 | — |

## 六、外部信号完整列表（38 条，按类别）

### Agent 工程与工具（6 条）
1. Loop Engineering 10 大设计模式
2. SDD 工具生态（Spec Kit/Kiro/Tessl）
3. Ploy 从 Claude Opus 4.8 迁移至 GPT-5.6
4. Claude Code v2.1.207 + 桌面版浏览器
5. Mindwalk Agent 3D 轨迹回放
6. BMAD Method V6 多 Agent 敏捷框架

### 模型发布与能力（8 条）
7. GPT-5.6 Sol Ultra 证 50 年图论猜想
8. 腾讯混元 Hy3（姚顺雨，Agent 90%）
9. 腾讯混元 HyOCR-1.5
10. Soofi S 开源 30B（德国 AI 协会）
11. 商汤 SenseNova-Vision-7B-MoT
12. 蚂蚁 LingBot-VA 2.0（具身基础模型）
13. 小红书 PIPO 新架构
14. 宇树 G1 活体微创手术

### AI 安全与治理（8 条）
15. xAI Grok Build CLI 安全事件
16. 博科圣地利用主流 AI 策划袭击
17. 伊利诺伊全美最强 AI 安全法
18. GPT-5.6 删光 Mac 硬盘
19. EU 网络安全与 AI 行动计划
20. 爱尔兰 AI 监管法案
21. 苹果诉 OpenAI 挖角窃密
22. Altman/Anthropic CEO 改口就业影响

### 中国 AI Agent 生态（3 条）
23. 豆包/通义千问 Agent 关闭
24. 中国大厂 Agent 路线分化
25. 百度搭子成都 AI Day

### Agent 身份与 IAM（1 条）
26. SPIFFE/SPIRE Agent 身份突破

### Token 经济学（3 条）
27. Tokenizer 差异致隐性涨价
28. Token 成本管理工具 Top 8
29. Perplexity 跨模型信用额度分析

### AI 评测与验证（1 条）
30. 2026 AI 评测框架 7 个比较 + lab-prod gap 37%

### Context Engineering（1 条）
31. Context Engineering 五大模式

### 企业 AI 采用（2 条）
32. Deloitte + Writer 2026 报告（57% agent 生产部署，79% 面临挑战）
33. 纳德拉"反向信息悖论"

### 其他（5 条）
34. Meta 关 Instagram AI 深度伪造
35. Meta 路易斯安那 5GW 数据中心（`$500亿+`）
36. PixVerse 4.39 亿美元 C 轮
37. 11 天 Claude Fable 5 写 100 万行 Rust 重构 Bun
38. OpenAI 新提示词指南

## 七、上次优先启动项回顾（07-09 → 07-14 进展）

| 07-09 优先启动 | 状态 | 说明 |
|---------------|------|------|
| Output 断层破冰 | ❌ 未启动 | ~37 天无产出 |
| Loop Engineering entity | ❌ 未启动 | 外部已验证，待 clip |
| Context Engineering topic | ❌ 未启动 | 外部已验证，待建 |
| Comparison 层激活 | ❌ 未启动 | 13/19 零入链持续 |
| 链接架构修复 | ❌ 未启动 | 9 topic 零入链持续 |

> 07-09 的 5 个 P0 全部未推进。根因：编译惯性 > 结构性建设。
