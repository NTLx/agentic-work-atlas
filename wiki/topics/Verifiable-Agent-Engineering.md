---
type: topic
title: Verifiable Agent Engineering
description: "可验证 Agent 工程：把 LLM 的非确定性推理关进可观察、可拒绝、可复现的工程系统"
created: 2026-05-18
updated: 2026-05-28
tags:
  - AI-Agent
  - verification
  - engineering
related_entities:
  - "[[Verifiability]]"
  - "[[Dominator-Analysis]]"
  - "[[Agentic-Engineering]]"
  - "[[Agent-Harness]]"
  - "[[Agent-PR-Review]]"
  - "[[Accessibility-Agent]]"
  - "[[Social-Model-of-Disability]]"
  - "[[Bias-to-Action-LLM]]"
  - "[[Accessibility-Complexity-Evaluation]]"
  - "[[Accessibility-High-Risk-Patterns]]"
  - "[[Corrective-RAG]]"
  - "[[Reflexion]]"
  - "[[Zero-PHI-Policy]]"
  - "[[Dual-Tier-LLM-Architecture]]"
  - "[[Sequence-Packing]]"
  - "[[MachinaCheck]]"
  - "[[Hardware-Sovereignty]]"
  - "[[Agentic-Workflow-Token-Efficiency]]"
  - "[[Agent-Generated-PRs]]"
  - "[[人机对齐]]"
  - "[[渐进式重构]]"
  - "[[Security-Hardening-Phase]]"
  - "[[Cybersecurity-Proof-of-Work]]"
  - "[[AISI]]"
  - "[[Mythos]]"
  - "[[Agent-Containment]]"
  - "[[Least-Agency]]"
  - "[[ITBench]]"
source_raw:
  - "[[The PR you would have opened yourself]]"
  - "[[用Agent评测思路管理AI Coding —— 31万行代码AI重构的实践]]"
  - "[[20260414-cybersecurity-proof-of-work]]"
  - "[[AI and the Future of Cybersecurity Why Openness Matters]]"
  - "[[Andrej Karpathy: From Vibe Coding to Agentic Engineering]]"
  - "[[Validating agentic behavior when “correct” isn’t deterministic]]"
  - "[[Agent pull requests are everywhere. Here's how to review them.]]"
  - "[[Building a general-purpose accessibility agent—and what we learned in the process]]"
  - "[[MachinaCheck Building a Multi-Agent CNC Manufacturability System on AMD MI300X]]"
  - "[[OncoAgent A Dual-Tier Multi-Agent Framework for Privacy-Preserving Oncology Clinical Decision Support]]"
  - "[[Maintainability sensors for coding agents]]"
  - "[[Improving token efficiency in GitHub Agentic Workflows]]"
  - "[[How we contain Claude across products]]"
  - "[[20260518-zero-trust-for-ai-agents]]"
  - "[[Using LLMs to secure source code]]"
  - "[[ITBench-AA Frontier Models Score Below 50% on the First Benchmark for Agentic Enterprise IT Tasks — by Artificial Analysis and IBM]]"
---

# Verifiable Agent Engineering（可验证 Agent 工程）

> [!summary] 核心洞察
> Agent 的能力上限不由“模型愿意做多少事”决定，而由“系统能验证多少事”决定。真正可规模化的 Agent 工程，不是放大自主性，而是扩大可验证边界。

## 为什么这是一个独立 Topic

现有 Agent 讨论容易把问题落在“模型更强”“工具更多”“循环更长”上。但 wiki 中多条线索指向同一个底层结构：

- [[Verifiability|可验证性]]解释了为什么代码、数学、测试驱动任务进步最快。
- [[Dominator-Analysis|支配者分析]]说明非确定性行为也能被提取出必经骨架。
- [[Accessibility-Agent|无障碍 Agent]]和[[Social-Model-of-Disability]]显示，真实生产系统需要知道何时不动手，因为错误自动化可能继续制造访问壁垒。
- [[MachinaCheck]]说明领域 Agent 不应把确定性工作交给 LLM。
- [[Corrective-RAG]]和[[Reflexion]]把“生成”变成可拒绝、可重试、可审计的管线。
- [[Zero-PHI-Policy]]、[[Dual-Tier-LLM-Architecture]]和[[Sequence-Packing]]则说明，高风险 Agent 的可验证性还包括数据边界、模型路由和训练管线。

这些不是零散技巧，而是同一件事：给非确定性智能修一条确定性轨道。

## 三个生成器

| 生成器 | 它解决什么 | 典型实体 |
|--------|------------|----------|
| 可验证边界 | 哪些输出能自动判断对错 | [[Verifiability]], [[Agent-PR-Review]], [[WCAG]] |
| 确定性骨架 | 哪些步骤必须由代码、规则、图结构保证 | [[Dominator-Analysis]], [[MachinaCheck]], [[Corrective-RAG]] |
| 拒绝机制 | 什么时候停止生成、转人工、返回安全拒绝 | [[Bias-to-Action-LLM]], [[Accessibility-High-Risk-Patterns]], [[Reflexion]] |
| 数据边界 | 什么信息绝不能进入模型上下文 | [[Zero-PHI-Policy]], [[Hardware-Sovereignty]] |
| 资源路由 | 哪些任务应交给哪一层模型和人工门控 | [[Dual-Tier-LLM-Architecture]], [[Sequence-Packing]] |

缺第一根，Agent 只是在表演努力。缺第二根，系统会把所有复杂性都倒给 LLM。缺第三根，Agent 的“行动偏差”会把边界条件变成事故。

## 从“让 Agent 做”到“让 Agent 被验证”

传统自动化的核心问题是：能不能把流程写成规则。

Agentic 自动化的核心问题变了：能不能把结果、路径或中间状态变成可验证对象。

```
任务目标
  ↓
可观察状态   ← 日志 / 截图 / 代码快照 / 结构化输出
  ↓
验证骨架     ← 测试 / dominator / schema / 距离门控 / 规则引擎
  ↓
动作边界     ← 自动修复 / 重试 / 拒绝 / 人工接管
```

这解释了为什么“可验证性”比“智能程度”更接近工程第一性原理。模型可以更聪明，但系统必须知道什么时候相信它。

## 生产级 Agent 的反直觉

越接近生产，越不应该让 LLM 覆盖整个流程。

[[MachinaCheck]] 的价值不在“用了多个 Agent”，而在它只在需要制造推理和报告组织的环节使用 LLM。STEP 文件解析和工具匹配由确定性代码完成，因为这些环节不需要想象力，只需要正确性。

[[Accessibility-Agent|无障碍 Agent]] 的价值也不在“自动改所有问题”，而在识别复杂度、高风险交互和人工介入点。它背后的 [[Social-Model-of-Disability]] 进一步提醒：无障碍问题不是用户的问题，而是环境和界面设计制造的访问壁垒。因此一个能拒绝的 Agent，比一个永远动手的 Agent 更接近生产可用。

## 可验证性不是测试覆盖率

测试只是可验证性的一种形式。更完整的可验证工程至少包含四层：

| 层级 | 验证对象 | 示例 |
|------|----------|------|
| 输出验证 | 最终结果是否满足要求 | 单元测试、格式校验、WCAG 检查 |
| 路径验证 | 是否经过成功所需的必经状态 | [[Dominator-Analysis]] |
| 上下文验证 | 检索材料是否真的相关 | [[Corrective-RAG]] |
| 行为验证 | 系统是否在该停止时停止 | 高风险模式转人工、安全拒绝 |

真正的 Agent harness 是这四层的组合，而不是一个更长的 prompt。

## 高风险 Agent 的验证链

OncoAgent 把可验证 Agent 工程从代码与无障碍场景推进到临床决策支持。它的关键不是“一个医疗大模型”，而是一条连续验证链：

- [[Zero-PHI-Policy]]先把 PHI 从模型上下文外移，降低隐私泄露空间。
- [[Corrective-RAG]]把检索材料变成可评分、可重试、可拒绝的证据层。
- [[Dual-Tier-LLM-Architecture]]按复杂度把问题路由到不同模型和人工门控。
- [[Reflexion]]用 schema、安全扫描和 entailment 检查约束生成结果。
- [[Sequence-Packing]]让本地微调和双层专门模型更可承受，但训练效率必须接受评测集约束。

这条链说明，高风险 Agent 的验证不是单点测试，而是从数据进入系统前就开始，一直到生成后、人工接管和安全拒绝为止。

## 人机对齐先于规则自动化

美团 31 万行代码重构案例把 Agent 评测方法迁移到 AI Coding 管理：先让团队对工程标准形成共识，再把共识固化为 AI 可执行的 Rule/Skill。顺序不能反过来；如果人类之间没有对齐，AI Rule 只是把分歧写得更快。

这个案例补充了可验证工程的组织前提：验证规则不是凭空产生的，它来自团队对“什么算好、什么必须拒绝、什么可以例外”的共同判断。

## Agent PR 需要更多证据，而不是更少

[[The PR you would have opened yourself]] 说明，Agent 辅助开源贡献不应该把 review 成本转嫁给维护者。好的 Agent PR 要显式披露 agent-assisted，并提供比普通 PR 更多信号：生成示例、数值比较、逐层对比、dtype 验证，以及独立的 non-agentic test harness。

这里的原则很清楚：Agent 可以降低贡献者的生成成本，但不能降低维护者的证据要求。

## 安全硬化是独立验证阶段

[[Cybersecurity-Proof-of-Work|Cybersecurity Proof of Work]] 把 security review 从偶发审计改写为预算驱动的持续硬化阶段。开发和代码审查主要受人类输入限制；安全硬化则更接近 token 预算竞争：防御者需要投入足够多的自动化搜索和验证，才能赶上攻击者的探索成本。

[[AISI]] 对 [[Mythos]] 的测试让这个判断有了更具体的工程形态：同一攻击任务、同一 token 预算、同一成功标准下比较模型行为。它说明安全验证不能只看模型厂商声明，而要看模型在受控环境中能否持续推进攻击链、是否出现边际收益递减、每次尝试的成本是否可接受。

这使 Agentic Coding 呈现三阶段：开发、代码审查、安全硬化。安全不是最后补一份 checklist，而是可验证工程的一条独立流水线。

Hugging Face 的 [[Cybersecurity-Openness|Cybersecurity Openness]] 进一步补充：在高风险安全场景中，半自主 Agent 比完全自主 Agent 更适合作为防御系统。关键不是“人类在环”这个口号，而是人类能否看见环内发生了什么。开放脚手架、开放规则引擎、可审计日志和 trace，都会让验证边界更清楚。

## 传感器层：把内部质量也纳入可验证边界

Birgitta Böckeler 对这个 Topic 的补充在于：Agent 的可验证性不应只盯着“功能有没有做对”，还要盯着“代码库是否仍然值得继续让 Agent 修改”。一旦小改动开始牵连越来越多文件，或者改一个地方更容易把旧功能带坏，系统虽然还在产出代码，但它的可维护性边界已经在塌。

这篇文章把传感器明确铺成三层：会话内即时反馈、CI 复验、周期性漂移审查。type checker、ESLint、Semgrep、dependency-cruiser、测试覆盖、增量 mutation testing 和 GitLeaks 负责在开发过程中不断收缩错误空间；安全审查、数据处理审查、依赖新鲜度和模块耦合审查则负责发现慢变量上的退化。这样被验证的不只是输出结果，还包括结构、依赖和安全约束。

更关键的是，传感器不是纯报警器。作者把 lint message 改写成带工程判断的自我纠正提示，让 agent 学会什么时候该补类型、什么时候只压制 warning、什么时候阈值调整只能作为例外。这说明生产级 verification loop 不只是“有检查”，还要把检查包装成 agent 可消费的修正语言；否则反馈很快会退化成噪声，甚至把系统推向过度重构。

## 成本可观测性也是验证边界

[[Agentic-Workflow-Token-Efficiency]] 把“能运行”之外的另一类生产风险拉进验证边界：自动触发的 Agent 工作流可能在 CI 中静默累积 token 成本。GitHub 的做法不是靠主观节省，而是把每次 API 调用记录成 `token-usage.jsonl`，再由审计 Agent 和优化 Agent 反过来优化工作流本身。

这里的第一性原理和可验证 Agent 工程一致：不要让 LLM 承担不需要推理的工作。PR diff、文件内容、评论列表等确定性读取，应该前置为 CLI 或缓存步骤；MCP 工具 schema 也不应无差别塞进每个请求。这样减少的不只是成本，也减少了 Agent 误用工具、陷入回退循环和扩大上下文噪声的机会。

但 token 指标不能单独作为成功标准。模型切换、工作负载变大、输出质量下降，都可能让数字产生假象。因此成本验证必须和 turn 数、工具完成率、任务结果、质量传感器一起看；否则“优化”可能只是让 Agent 少做了该做的工作。

## 与现有 Topic 的关系

- [[Agentic-Engineering-Patterns]]回答“如何用 Agent 做软件工程”。
- [[Building-Effective-Agents]]回答“Agent 工作流有哪些架构模式”。
- [[Agentic-Workflow-Token-Efficiency]]回答“生产级 Agent 工作流怎样控制可观测成本”。
- 本 Topic 回答“这些模式怎样跨过 demo 与生产之间的断层”。

## 结论

Agent 工程的下一步不是更像人，而是更像实验室：输入可控，状态可观测，失败可复现，边界可拒绝。

当系统能验证一个 Agent，它才真正拥有这个 Agent。
