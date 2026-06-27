---
type: index
title: 智能体时代工作图谱索引
updated: 2026-06-28
tags:
---

# 智能体时代工作图谱索引

> 围绕 AI / Agent 如何重写工作系统的主题知识库，通过 LLM Wiki 模式持续编译知识自行进化。

---

## 📊 知识库概览

| 指标 | 数值 |
|-----|------|
| Entity 页面 | 285 个 |
| Topic 页面 | 30 个 |
| Comparison 页面 | 19 个 |
| Raw 文章 | 152 个 |
| Source Summary | 153 个 |
| Output 作品 | 5 个 |
| Research 日志 | 13 个 |

### 连接拓扑（2026-06-25 实测，口径见 `schema/fragmentation-metrics.md`）

| 指标 | 口径 | 实测 | 健康判定 |
|------|------|------|---------|
| 全图零入链 entity | 全图入链 | 1.1% (3/280) | 健康 |
| 知识层零互引 entity | 知识层互引 | 6.8% (19/280) | 健康 |
| 整合层未承载 entity | 整合层承载 | 35.0% (98/280) | 碎片化（目标 ≤20%） |
| 单点挂靠 entity | 知识层互引 | 16.8% (47/280) | 偏高（目标 <10%） |
| Top 3 hub | 知识层互引 | Agentic-Engineering 119 / Agent-Harness 78 / Context-Engineering 50 | 幂律温和，不干预 |
| Output 转化率 | 产出层 | 5 / 67+ 思考 ≈ 7% | 断层（目标 ≥20%） |

---

## 🏗️ 核心实体 (wiki/entities/)

*概念实体按照首字母排序（此处列出部分核心节点）。*

#### 基础架构与工程
| Entity | 定义 | 来源 |
|--------|------|------|
| [[wiki/entities/Agentic-Engineering\|Agentic Engineering（代理式工程）]] | 默认使用 Agent 辅助并持续改进的软件工程范式 | Agentic Engineering Patterns |
| [[wiki/entities/Agent-Harness\|Agent Harness（智能体脚手架）]] | 包装模型并提供工具、上下文、护栏的运行时环境 | The Anatomy of an Agent Harness |
| [[wiki/entities/Constraint-Infrastructure\|Constraint Infrastructure（约束基建）]] | 系统化保证 Agent 运行时行为边界的基础设施层 | 阿里云 Agent Infra 约束基建 |
| [[wiki/entities/Constraint-Driven-Engineering\|Constraint-Driven Engineering（约束驱动工程）]] | 通过分阶段硬约束与分层验收实现 Agent 交付收敛的范式 | Qwen3.7-Max Experiment |
| [[wiki/entities/Automated-Criteria\|Automated Criteria（自动化判据）]] | 从编排层到真机层客观判定 Agent 执行结果是否成功的体系 | Qwen3.7-Max Experiment |
| [[wiki/entities/Pixel-Facts\|Pixel Facts（像素事实）]] | 将 UI 树 dump 坐标作为不可违反的几何约束注入 Agent 的技术 | Qwen3.7-Max Experiment |
| [[wiki/entities/HaaS-Harness-as-a-Service\|HaaS (Harness-as-a-Service)]] | 从提供底层模型 API 转向提供预配置 Agent 运行时的服务范式 | Agent Harness Engineering |
| [[wiki/entities/Context-Rot\|Context Rot（上下文腐烂）]] | 随着窗口填充，模型推理和任务完成能力非线性下降的现象 | Agent Harness Engineering |
| [[wiki/entities/Ralph-Loops\|Ralph Loops]] | 拦截退出信号并重注入提示，实现 Agent 长程任务的循环技术 | Agent Harness Engineering |
| [[wiki/entities/AGENTS-md\|AGENTS.md]] | 作为 Agent "棘轮"规则手册的根目录规范文件 | Agent Harness Engineering |
| [[wiki/entities/Agent-Verification\|Agent Verification（Agent 自主验证）]] | Agent 能自主运行验证循环的能力——不是 lint/type check，而是 agent 能自己启动测试环境 | Claude Code 一周年 |
| [[wiki/entities/LLM-as-a-Judge\|LLM-as-a-Judge（LLM 裁判）]] | 使用 LLM 按预定义 rubric 评估另一个系统输出质量的方法论，核心是按风险分层匹配评判策略 | Li et al. 2026 |
| [[wiki/entities/Auto-Mode\|Auto Mode（自动模式）]] | Claude Code 的自动执行模式——agent 自主决定运行工具，无需逐条等待用户确认 | Claude Code 一周年 |
| [[wiki/entities/Context-Minimalism\|Context Minimalism（上下文极简主义）]] | 给 agent 最小可能的 system prompt 和工具集，让模型自己决定如何拉取上下文 | Claude Code 一周年 |
| [[wiki/entities/Skill-Chains\|Skill Chains（技能链）]] | 多技能顺序执行的 macro skill 模式，通过 QA skill 约束幻觉 | Become AI Native Org |
| [[wiki/entities/Company-Brain\|Company Brain（公司大脑）]] | 组织可读的 context 层，Capture → Curate → Store → Execute → Experience 循环 | Become AI Native Org |
| [[wiki/entities/Code-Execution\|Code Execution]] | Agent 直接在沙箱运行代码并获取反馈的能力 | Simon Willison |
| [[wiki/entities/Vibe-Coding\|Vibe Coding（氛围编程）]] | 依靠直觉和多轮提示快速产出原型但缺乏严谨验证的开发模式 | Andrej Karpathy |
| [[wiki/entities/Model-Context-Protocol-MCP\|MCP（Model Context Protocol）]] | 统一的模型与工具连接协议标准 | Pinterest Engineering |
| [[wiki/entities/N-Hour\|N-Hour]] | 补丁发布后数小时内即被 AI 构建利用代码的新网络安全现实 | Anthropic Exploit Study |
| [[wiki/entities/Agent-Ergonomics\|Agent Ergonomics（Agent 人体工学）]] | 以 Agent 为第一公民的工具设计哲学，AXI 十原则 | L8 Principal Agentic Workflow |
| [[wiki/entities/Validation-Pipeline\|Validation Pipeline（验证管线）]] | 自动化端到端验证管线：对抗审查 + e2e + 证据生成 | L8 Principal Agentic Workflow |
| [[wiki/entities/Captain-Mindset\|Captain Mindset（船长思维）]] | 人从 sailor 到 captain 的角色转型，规划+质量把关 | L8 Principal Agentic Workflow |

#### 组织与变革
| Entity | 定义 | 来源 |
|--------|------|------|
| [[wiki/entities/AI-Ready-Organization\|AI-Ready Organization（AI 就绪组织）]] | 具有清晰流程语义、数据基座和容错机制的组织形态 | Stanford Enterprise AI Playbook |
| [[wiki/entities/AI-Factory\|AI Factory（AI 工厂）]] | 将 AI 能力规模化、标准化交付的组织化生产线 | P&G Case Study |
| [[wiki/entities/Forward-Deployed-Engineer\|Forward Deployed Engineer（前线开发工程师）]] | 深入客户现场识别约束并交付定制化 AI 解决方案的角色 | Palantir / OpenAI |
| [[wiki/entities/Knowledge-Work\|Knowledge Work（知识工作）]] | 正在被 AI 重新定义效率边界和价值内核的工作类型 | Jevons Paradox for Knowledge Work |
| [[wiki/entities/Role-Merging\|Role Merging（角色融合）]] | AI 让 PM/设计师/财务等非工程角色也能写代码，同时让工程师端到端交付产品 | Claude Code 一周年 |
| [[wiki/entities/AI-Capability-Management-Alignment\|AI Capability-Management Alignment（AI 能力-管理对齐）]] | 不同能力层级的 AI 需要不同管理方式，与管理人的能力-委派匹配模型同构 | 数字生命卡兹克 |
| [[wiki/entities/Agent-Adoption-Curve\|Agent Adoption Curve（智能体采纳曲线）]] | 智能体工具采纳的典型模式：开发者先采用，随后非开发者增速反超 | OpenAI Economic Research |
| [[wiki/entities/Kun-Chen\|Kun Chen]] | 前 L8 Principal Engineer，AXI / No Mistakes / First Mate 工具链作者 | L8 Principal Agentic Workflow |

#### 知识与语义
| Entity | 定义 | 来源 |
|--------|------|------|
| [[wiki/entities/LLM-Wiki\|LLM Wiki]] | 为 AI 消费设计的、具有强语义关联和证据溯源的知识库 | CC+Obsidian Wiki |
| [[wiki/entities/Ontology\|Ontology（本体）]] | 对现实业务世界的数字化建模，承载语义结构与规则 | Ontology 系列 |
| [[wiki/entities/UModel\|UModel（统一可观测模型）]] | 阿里云基于本体论的 IT 世界统一建模框架，以实体为中心、以图为核心 | Ontology 泛谈系列 |
| [[wiki/entities/NLAH\|NLAH（自然语言智能体驾驭层）]] | 将 Agent 驾驭策略从代码中外置为可执行的自然语言文档 | NLAH 论文解读 |
| [[wiki/entities/Sleep-Token\|Sleep-Token（睡后 Token）]] | 让 Token 在人离线时持续产出候选结果的工作模式 | Qoder 工程实践 |
| [[wiki/entities/Knowledge-Compilation\|Knowledge Compilation（知识编译）]] | 将非结构化来源提炼为结构化、可查询知识节点的动作 | Agentic Work Atlas Schema |

#### AI 政策与监管
| Entity | 定义 | 来源 |
|--------|------|------|
| [[wiki/entities/Frontier-Developer-Obligations\|Frontier Developer Obligations（前沿开发者义务）]] | Anthropic 提出的前沿 AI 开发者必须承担的监管义务体系 | Anthropic AI Framework |
| [[wiki/entities/Societal-Resilience\|Societal Resilience（社会韧性）]] | 社会层面抵御和恢复 AI 可能加速或启用的威胁的能力 | Anthropic AI Framework |
| [[wiki/entities/Collingridge-Dilemma\|Collingridge Dilemma（科林格里奇困境）]] | 技术影响在早期难以预见，等到清晰时已难以管理 | Dario Amodei |

#### 多 Agent 系统与涌现
| Entity | 定义 | 来源 |
|--------|------|------|
| [[wiki/entities/Emergence\|Emergence（涌现）]] | 复杂系统中从简单规则和交互中自发产生的宏观行为 | Thousand Token Wood v3 |
| [[wiki/entities/Agent-Heterogeneity\|Agent Heterogeneity（Agent 异质性）]] | 多 agent 系统中使用不同架构/厂商的模型驱动不同 agent | Thousand Token Wood v3 |
| [[wiki/entities/Settlement-Mechanism\|Settlement Mechanism（结算机制）]] | 多 agent 经济系统中，在 agent 自由交易之后、结果固化之前的一个确定性覆盖点 | Thousand Token Wood v3 |

---

## 📄 Raw (raw/)

*原始剪藏文章（148 个）*

*所有文章存放在 `raw/` 目录，使用短链接格式引用（如 `[[文章名]]`）。*

最新编译：2026-06-26——Li et al. 2026《LLM-as-a-Judge in Healthcare: A Scoping Analysis》（PRISMA scoping review, 134 studies），新增 LLM-as-a-Judge entity + source summary。

---

## 🚀 快速操作

### 编译文章
```
compile              # 编译 raw 中所有未处理的文件
compile <文件名>     # 编译指定文章
rebuild              # 重新编译全部 Raw 文件（批量回溯）
```

### 查询知识
```
什么是 <概念>?
关于 <主题> 有什么讨论?
```

### 审计检查
```
lint               # 执行完整 lint 检查（含摘要覆盖检查）
status             # 查看知识库状态
```

### 知识编译（三步法）
1. **浓缩** - 提取核心结论（≤3条）+ 关键证据
2. **质疑** - 审视前提假设、数据可靠性、边界条件
3. **对标** - 跨领域找类似现象，建立知识迁移

---

*索引版本: v2.7*
*最后更新: 2026-06-26*
