---
type: index
title: 智能体时代工作图谱索引
updated: 2026-06-11
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
| Entity 页面 | 247 个 |
| Topic 页面 | 27 个 |
| Comparison 页面 | 18 个 |
| Raw 文章 | 115 个 |
| Output 作品 | 4 个 |

---

## 🏗️ 核心实体 (wiki/entities/)

*概念实体按照首字母排序（此处列出部分核心节点）。*

#### 基础架构与工程
| Entity | 定义 | 来源 |
|--------|------|------|
| [[wiki/entities/Agentic-Engineering\|Agentic Engineering（代理式工程）]] | 默认使用 Agent 辅助并持续改进的软件工程范式 | Agentic Engineering Patterns |
| [[wiki/entities/Agent-Harness\|Agent Harness（智能体脚手架）]] | 包装模型并提供工具、上下文、护栏的运行时环境 | The Anatomy of an Agent Harness |
| [[wiki/entities/Constraint-Driven-Engineering\|Constraint-Driven Engineering（约束驱动工程）]] | 通过分阶段硬约束与分层验收实现 Agent 交付收敛的范式 | Qwen3.7-Max Experiment |
| [[wiki/entities/Automated-Criteria\|Automated Criteria（自动化判据）]] | 从编排层到真机层客观判定 Agent 执行结果是否成功的体系 | Qwen3.7-Max Experiment |
| [[wiki/entities/Pixel-Facts\|Pixel Facts（像素事实）]] | 将 UI 树 dump 坐标作为不可违反的几何约束注入 Agent 的技术 | Qwen3.7-Max Experiment |
| [[wiki/entities/HaaS-Harness-as-a-Service\|HaaS (Harness-as-a-Service)]] | 从提供底层模型 API 转向提供预配置 Agent 运行时的服务范式 | Agent Harness Engineering |
| [[wiki/entities/Context-Rot\|Context Rot（上下文腐烂）]] | 随着窗口填充，模型推理和任务完成能力非线性下降的现象 | Agent Harness Engineering |
| [[wiki/entities/Ralph-Loops\|Ralph Loops]] | 拦截退出信号并重注入提示，实现 Agent 长程任务的循环技术 | Agent Harness Engineering |
| [[wiki/entities/AGENTS-md\|AGENTS.md]] | 作为 Agent “棘轮”规则手册的根目录规范文件 | Agent Harness Engineering |
| [[wiki/entities/Code-Execution\|Code Execution]] | Agent 直接在沙箱运行代码并获取反馈的能力 | Simon Willison |
| [[wiki/entities/Vibe-Coding\|Vibe Coding（氛围编程）]] | 依靠直觉和多轮提示快速产出原型但缺乏严谨验证的开发模式 | Andrej Karpathy |
| [[wiki/entities/Model-Context-Protocol-MCP\|MCP（Model Context Protocol）]] | 统一的模型与工具连接协议标准 | Pinterest Engineering |

#### 组织与变革
| Entity | 定义 | 来源 |
|--------|------|------|
| [[wiki/entities/AI-Ready-Organization\|AI-Ready Organization（AI 就绪组织）]] | 具有清晰流程语义、数据基座和容错机制的组织形态 | Stanford Enterprise AI Playbook |
| [[wiki/entities/AI-Factory\|AI Factory（AI 工厂）]] | 将 AI 能力规模化、标准化交付的组织化生产线 | P&G Case Study |
| [[wiki/entities/Forward-Deployed-Engineer\|Forward Deployed Engineer（前线开发工程师）]] | 深入客户现场识别约束并交付定制化 AI 解决方案的角色 | Palantir / OpenAI |
| [[wiki/entities/Knowledge-Work\|Knowledge Work（知识工作）]] | 正在被 AI 重新定义效率边界和价值内核的工作类型 | Jevons Paradox for Knowledge Work |

#### 知识与语义
| Entity | 定义 | 来源 |
|--------|------|------|
| [[wiki/entities/LLM-Wiki\|LLM Wiki]] | 为 AI 消费设计的、具有强语义关联和证据溯源的知识库 | CC+Obsidian Wiki |
| [[wiki/entities/Ontology\|Ontology（本体）]] | 对现实业务世界的数字化建模，承载语义结构与规则 | Ontology 系列 |
| [[wiki/entities/Knowledge-Compilation\|Knowledge Compilation（知识编译）]] | 将非结构化来源提炼为结构化、可查询知识节点的动作 | Agentic Work Atlas Schema |

---

## 📄 Raw (raw/)

*原始剪藏文章（114 个）*

*所有文章存放在 `raw/` 目录，使用短链接格式引用（如 `[[文章名]]`）。*

最新编译：3 篇关于智能体基础设施与工程范式的核心材料：Addy Osmani《Agent Harness Engineering》、Anthropic《Paving the way for agents in biology》以及通义实验室《质量是「收敛」出来的》（Qwen3.7-Max 实验）。新增 12 个 entity，包括 [[Context-Rot]]、[[Deterministic-Retrieval]]、[[Constraint-Driven-Engineering]] 与 [[Automated-Criteria]]。

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
*最后更新: 2026-06-10*
