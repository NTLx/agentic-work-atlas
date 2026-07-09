---
type: index
title: 智能体时代工作图谱索引
updated: 2026-07-09
tags:
---

# 智能体时代工作图谱索引

> 围绕 AI / Agent 如何重写工作系统的主题知识库，通过 LLM Wiki 模式持续编译知识自行进化。

---

## 📊 知识库概览

| 指标 | 数值 |
|-----|------|
| Entity 页面 | 318 个 |
| Topic 页面 | 33 个 |
| Comparison 页面 | 19 个 |
| Raw 文章 | 187 个 |
| Source Summary | 184 个 |
| Output 作品 | 5 个 |
| Research 日志 | 26 个 |

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
| [[wiki/entities/Loss-Function-Development\|Loss Function Development（损失函数开发）]] | 用大规模盲评 eval 集作为损失函数驱动 Agent 长周期优化的工程范式 | Elvis Sun LFD |
| [[wiki/entities/Mechanical-Sympathy-for-LLMs\|Mechanical Sympathy for LLMs（LLM 机械同理心）]] | 工程师应获取对 LLM 实际工作原理的经验性理解——而非推测未来能力 | Martin Fowler 2026 |
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
| [[wiki/entities/AI-in-Mathematics\|AI in Mathematics（AI 数学）]] | AI在数学领域的应用与进展，包括自动定理证明、问题求解、概念发现等 | Grant Sanderson 播客 |
| [[wiki/entities/Conceptual-Breakthroughs\|Conceptual Breakthroughs（概念突破）]] | 产生新的概念、理论或框架来统一或重新组织现有知识的能力 | Grant Sanderson 播客 |
| [[wiki/entities/Grindability-vs-Verifiability\|Grindability vs Verifiability（可磨性与可验证性）]] | AI成功的关键因素区分：可磨性比可验证性更重要 | Grant Sanderson 播客 |
| [[wiki/entities/Autoregressive-Generation\|Autoregressive Generation（自回归生成）]] | 通过预测下一个token来生成文本的方式，是当前LLM的核心机制 | Grant Sanderson 播客 |
| [[wiki/entities/Code-Cleanliness-Agent-Footprint\|Code Cleanliness Agent Footprint（代码整洁度的 Agent 足迹效应）]] | 代码整洁度不影响通过率但显著降低 agent 操作成本（token −7-8%、revisitation −34%） | SonarSource Minimal-Pair Study |
| [[wiki/entities/Minimal-Pair-Evaluation\|Minimal Pair Evaluation（最小对比对评估）]] | 构造仅目标变量不同的仓库对以隔离其对 coding agent 的因果影响 | SonarSource Minimal-Pair Study |
| [[wiki/entities/Agentic-Speculation\|Agentic Speculation（Agent 投机探索）]] | Agent 与数据系统交互的高吞吐异构查询流模式，80-90% 子计划重复但冗余提升成功率 | BAIR Intelligence is Free |
| [[wiki/entities/Structured-Agent-Memory\|Structured Agent Memory（结构化 Agent 记忆）]] | 按多属性维度组织的纠正性记忆，通过属性匹配精确召回，区别于 MD+embedding 范式 | BAIR Intelligence is Free |
| [[wiki/entities/Goodharts-Law\|Goodhart's Law（古德哈特定律）]] | 当代理指标成为优化目标时就不再是好度量——指标 gaming 导致真实目标被替代 | 万维钢·现代思维工具100讲 |
| [[wiki/entities/Knowledge-Debt\|Knowledge Debt（知识债务）]] | 开发者委托 agent 编码后沉默积累的理解缺口，与 Technical Debt 同构 | Accenture Labs SHIELD 论文 |
| [[wiki/entities/Incidental-Learning\|Incidental Learning（附带学习）]] | 通过费力解决问题非预期获得的知识——被 AI agent 短路的学习路径 | Accenture Labs SHIELD 论文 |
| [[wiki/entities/SHIELD\|SHIELD]] | 多 agent 系统，通过 out-of-band 渠道在不打断开发流程的前提下偿还 Knowledge Debt | Accenture Labs SHIELD 论文 |

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
| [[wiki/entities/Context-Advantage\|Context Advantage（上下文优势）]] | Andrew Ng 提出：人类在 AI 时代的不可替代性源于信息不对称而非品味 | Loop Engineering |
| [[wiki/entities/Kun-Chen\|Kun Chen]] | 前 L8 Principal Engineer，AXI / No Mistakes / First Mate 工具链作者 | L8 Principal Agentic Workflow |
| [[wiki/entities/Pro-Worker-AI\|Pro-Worker AI（亲劳动者 AI）]] | 使人类专业知识更有价值而非更不必要的 AI 方向，核心机制是新任务创建 | Hamilton Project |
| [[wiki/entities/Task-Framework\|Task Framework（任务框架）]] | Acemoglu/Autor 的技术变革五分类——以任务为分析单元区分自动化与新任务创建 | Hamilton Project |

#### 知识与语义
| Entity | 定义 | 来源 |
|--------|------|------|
| [[wiki/entities/LLM-Wiki\|LLM Wiki]] | 为 AI 消费设计的、具有强语义关联和证据溯源的知识库 | CC+Obsidian Wiki |
| [[wiki/entities/Ontology\|Ontology（本体）]] | 对现实业务世界的数字化建模，承载语义结构与规则 | Ontology 系列 |
| [[wiki/entities/UModel\|UModel（统一可观测模型）]] | 阿里云基于本体论的 IT 世界统一建模框架，以实体为中心、以图为核心 | Ontology 泛谈系列 |
| [[wiki/entities/NLAH\|NLAH（自然语言智能体驾驭层）]] | 将 Agent 驾驭策略从代码中外置为可执行的自然语言文档 | NLAH 论文解读 |
| [[wiki/entities/Sleep-Token\|Sleep-Token（睡后 Token）]] | 让 Token 在人离线时持续产出候选结果的工作模式 | Qoder 工程实践 |
| [[wiki/entities/Knowledge-Compilation\|Knowledge Compilation（知识编译）]] | 将非结构化来源提炼为结构化、可查询知识节点的动作 | Agentic Work Atlas Schema |
| [[wiki/entities/Human-Curation\|Human Curation（人类策展）]] | 人类在信息过载时代的核心价值——选择、组织、解释信息 | Grant Sanderson 播客 |
| [[wiki/entities/Theory-of-Mind\|Theory of Mind（心智理论）]] | 理解他人心理状态的能力，是有效沟通、教学和策展的基础 | Grant Sanderson 播客 |

#### Agent 安全与攻防
| Entity | 定义 | 来源 |
|--------|------|------|
| [[wiki/entities/Agent-Traps\|Agent Traps（Agent 陷阱）]] | 按 Agent 运行周期六环节分类的恶意环境内容系统框架——感知→推理→记忆→行动→多Agent→人类 | Google DeepMind AI Agent Traps |
| [[wiki/entities/Persona-Hyperstition\|Persona Hyperstition（人格超实）]] | 关于模型"人格"的公共叙事通过检索/训练回流使模型产生符合叙事行为的自我实现反馈循环 | Google DeepMind AI Agent Traps |
| [[wiki/entities/Agent-Perception-Gap\|Agent Perception Gap（Agent 感知差）]] | 人类和 Agent 消费同一网页时解析路径的根本差异——HTML源码树 vs 视觉渲染——是所有内容注入陷阱的共同入口 | Google DeepMind AI Agent Traps |
| [[wiki/entities/Prompt-Injection-Risk\|Prompt Injection Risk（提示注入风险）]] | 在内容中嵌入"给 AI 看的隐藏指令"试图影响 AI 综述/推荐的风险 | Ethan Mollick Co-Existence |
| [[wiki/entities/Agent-Containment\|Agent Containment（Agent 隔离与遏制）]] | 通过环境层隔离限制 Agent 可操作范围的安全架构 | Anthropic Security Practices |
| [[wiki/entities/Multi-Agent-System-Pathology\|Multi-Agent System Pathology（多 Agent 系统病理）]] | 多 Agent 系统在形成组织结构后出现的协作、认知、责任和内态失真问题 | Hao 好聊趋势 |

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

*原始剪藏文章（189 个）*

*所有文章存放在 `raw/` 目录，使用短链接格式引用（如 `[[文章名]]`）。*

最新编译：2026-07-09——批量编译 3 篇未编译 raw 材料（Hamilton Project Pro-Worker AI、万维钢 Goodhart's Law、Accenture Labs Agents That Teach），新增 6 个 Entity（Pro-Worker-AI / Task-Framework / Goodharts-Law / Knowledge-Debt / Incidental-Learning / SHIELD）+ 3 个 source summary + 2 个 Topic（Pro-Worker-AI-and-Labor-Policy / Skill-Atrophy-and-Knowledge-Debt）。

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

*索引版本: v2.11*
*最后更新: 2026-07-09*
