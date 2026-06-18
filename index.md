---
type: index
title: 智能体时代工作图谱索引
updated: 2026-06-18
tags:
  - index
  - MOC
---

# 智能体时代工作图谱索引

> 围绕 AI / Agent 如何重写工作系统的主题知识库，通过 LLM Wiki 模式持续编译知识自行进化。

---

## 📊 知识库概览

| 指标 | 数值 |
|-----|------|
| Entity 页面 | 263 个 |
| Topic 页面 | 28 个 |
| Comparison 页面 | 18 个 |
| Raw 文章 | 140 个 |
| Output 作品 | 4 个 |

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
| [[wiki/entities/Auto-Mode\|Auto Mode（自动模式）]] | Claude Code 的自动执行模式——agent 自主决定运行工具，无需逐条等待用户确认 | Claude Code 一周年 |
| [[wiki/entities/Context-Minimalism\|Context Minimalism（上下文极简主义）]] | 给 agent 最小可能的 system prompt 和工具集，让模型自己决定如何拉取上下文 | Claude Code 一周年 |
| [[wiki/entities/Code-Execution\|Code Execution]] | Agent 直接在沙箱运行代码并获取反馈的能力 | Simon Willison |
| [[wiki/entities/Vibe-Coding\|Vibe Coding（氛围编程）]] | 依靠直觉和多轮提示快速产出原型但缺乏严谨验证的开发模式 | Andrej Karpathy |
| [[wiki/entities/Model-Context-Protocol-MCP\|MCP（Model Context Protocol）]] | 统一的模型与工具连接协议标准 | Pinterest Engineering |
| [[wiki/entities/N-Hour\|N-Hour]] | 补丁发布后数小时内即被 AI 构建利用代码的新网络安全现实 | Anthropic Exploit Study |

#### 组织与变革
| Entity | 定义 | 来源 |
|--------|------|------|
| [[wiki/entities/AI-Ready-Organization\|AI-Ready Organization（AI 就绪组织）]] | 具有清晰流程语义、数据基座和容错机制的组织形态 | Stanford Enterprise AI Playbook |
| [[wiki/entities/AI-Factory\|AI Factory（AI 工厂）]] | 将 AI 能力规模化、标准化交付的组织化生产线 | P&G Case Study |
| [[wiki/entities/Forward-Deployed-Engineer\|Forward Deployed Engineer（前线开发工程师）]] | 深入客户现场识别约束并交付定制化 AI 解决方案的角色 | Palantir / OpenAI |
| [[wiki/entities/Knowledge-Work\|Knowledge Work（知识工作）]] | 正在被 AI 重新定义效率边界和价值内核的工作类型 | Jevons Paradox for Knowledge Work |
| [[wiki/entities/Role-Merging\|Role Merging（角色融合）]] | AI 让 PM/设计师/财务等非工程角色也能写代码，同时让工程师端到端交付产品 | Claude Code 一周年 |

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

*原始剪藏文章（137 个）*

*所有文章存放在 `raw/` 目录，使用短链接格式引用（如 `[[文章名]]`）。*

最新编译：2026-06-17 批次——Anthropic Claude Code expertise、Tim Ferriss nonfiction、LangChain Loop Engineering/Agent Engineering/Legal Verifiers、Bayer PRINCE、ByteByteGo Open-Weight 共 8 篇 source summary。

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
*最后更新: 2026-06-13*
