---
type: entity
title: Agent Orchestration
aliases:
  - Agent Orchestration
definition: "协调 Agent 及确定性执行器的任务、依赖、状态、权限边界、失败恢复与结果确认；可采用代码、工作流或模型辅助，不必另设 LLM 编排者"
created: 2026-04-09
updated: 2026-11-28
tags:
  - AI-Agent
  - OpenClaw
  - Multi-Agent-System
evidence_level: high
claim_type: mixed
related_entities:
  - '[[Claude-Code-CLI]]'
  - '[[Context-Engineering]]'
  - '[[Agent-Swarm]]'
  - '[[Three-State-Protocol]]'
  - "[[Invisible-Orchestrator]]"
  - "[[Multi-Agent-System-Pathology]]"
  - "[[Captain-Mindset]]"
  - "[[Kun-Chen]]"
source_raw:
  - "[[20261019-meta-thin-orchestrator-data-agents]]"
  - '[[OpenClaw + 6 个 Agent 运转半个月，从聊天到干活的完整工程实践]]'
  - '[[OpenClaw + CodexClaudeCode Agent Swarm The One-Person Dev Team Full Setup]]'
  - "[[MachinaCheck Building a Multi-Agent CNC Manufacturability System on AMD MI300X]]"
  - "[[Multi-Agent 火了，但 AI 的组织病还没人治｜Hao好聊趋势]]"
  - "[[20260620-l8-principal-agentic-workflow]]"
  - "[[20260728-fowler-orchestrator-tax]]"
  - "[[20260819-anthropic-claude-tag-oncall]]"
  - "[[20261002-openrouter-langchain-crewai-routing]]"
---

# Agent Orchestration

## Meta 的 Thin Orchestrator：把控制平面从领域推理中剥离（2026-10）

[[20261019-meta-thin-orchestrator-data-agents]] 记录了一条可核验的工程分层：Meta 面向推荐系统数据列入库搭建约 1,300 行 thin orchestrator，复用 14 个隔离专业 Agent 和 20 多个工作流。中央的七步协议包括加载专家说明、重复检查、必填字段、自动发现、可靠性门禁、专业委派和结果确认；作者称只有专业委派涉及领域 LLM 推理。通过三类 workflow template 组合同一组专家、按运行时加载 25 个以上知识文件，避免把数据源专有知识全部塞进中央上下文。

- **判断（综合）**：编排层应稳定承担 **路由/依赖/状态/幂等/失败恢复/确认**，领域执行层承担局部专业判断；知识版本需可追溯。薄并不等于忽略跨 Agent 业务一致性，仍需跨阶段契约和最终核验。
- **证据**：[[20261019-meta-thin-orchestrator-data-agents]]（The Approach / What We Built / Why This Works）。
- **边界**：3–4 天人工、约一天早期自动化和不到一小时新架构的数字是 Meta 自报不同流程基线；缺少同条件配对，不能据此宣布普适倍数。作者未来的自动改知识反馈循环尚未实现。
- **对当前系统的适配约束**：不因该案例复制新 n8n 编排器或把 ChatGPT 工作推给外部 Agent；先测现有 Workers 与状态机是否满足可验证 Claim、ACK、ownership 与失败语义，再决定改造。



> [!definition] 定义
> Agent 编排层（Orchestration Layer）负责协调委派、依赖、状态和实际结果。OpenClaw 项目经理式委派是下述个人案例之一，并不定义通用编排架构。

## 为什么需要编排层

直接使用 Claude Code 或 Codex 的问题：

- **上下文局限**：有效上下文与任务需求、检索和模型有关，不是固定200K限制。
- **交互阻塞**：需明确审批与暂停/恢复策略；不应为避免等待绕过授权。
- **进程失控**：需要可观测状态、超时、恢复和结果确认。

编排层可提供这些能力，也可由既有 runtime、工作流或直接执行接口实现。增加一层 Agent 不保证持久运行或故障恢复。

## 编排者角色

### 项目经理模式

OpenClaw 作为项目经理，Claude Code 作为开发工程师：

> "我只跟项目经理说需求，项目经理自己拆任务、盯进度、处理报错、测试验收。开发工程师闷头写代码就行。"

核心职责：
- 接收产品需求 → 写 PRD + 技术方案 → 用户确认
- 拆解功能 → 逐个委派 Claude Code 开发
- 监控进度 → 处理报错 → 自动修复或升级
- 开发完成 → 自动测试 → 发报告给用户

### Zoe 编排者（6 Agent 实战）

Zoe 是"首席编排者"，不只是管理员：

- **技术方案设计**：三态通信协议、Task Watcher、通信 Guardrail 都是 Zoe 自主设计
- **任务编排**：指派 ainews 深入调研，委派 ACP 编码专家实现
- **系统运维**：每天 3 次巡检，检查 cron 执行状态、磁盘使用、session 健康度
- **记忆系统维护**：每周分析 MEMORY.md，执行分层压缩

## 编排架构示例

### 1+5+6 阵型

```
┌─────────────────────────────────────────┐
│           Zoe（编排者）                  │
│  技术设计 / 任务编排 / 系统运维          │
└─────────────────────────────────────────┘
         ↓ 委派任务
┌─────────────────────────────────────────┐
│  5 个专业 Agent                         │
│  ainews / Trading / Macro / Content / Butler │
└─────────────────────────────────────────┘
         ↓ ACP 编码委派
┌─────────────────────────────────────────┐
│  6 个编码专家（最大 6 并发）             │
│  Claude Code / Codex / Gemini / ...     │
└─────────────────────────────────────────┘
```

### Agent Swarm 编排

Elvis 的 Agent Swarm 系统：

- Zoe spawns agents，写 prompts，选模型，监控进度
- Telegram 通知 PR ready to merge
- 94 commits/天，7 PRs/30 分钟

## 编排 vs 直接使用对比

| 维度 | 直接用 Claude Code | OpenClaw 编排 |
|-----|-------------------|--------------|
| 人工参与 | 取决于交互/非交互模式与审批 | 可聚合审批与结果，但仍需责任人 |
| 问题处理 | 依 runtime 与任务合同 | 可统一恢复与升级策略 |
| 并行能力 | 可直接启动独立任务 | 可集中协调依赖与资源 |
| 上下文 | 可获授权业务及代码信息 | 可按任务分配最小必要上下文 |

## 关键设计原则

1. **分离关注点**：按任务依赖与风险划分职责；ACP 是一种实现，不是必选
2. **上下文专业化**：执行者须获完成任务所需业务约束和代码上下文，不宜机械隔绝
3. **协议级通信**：不是群聊问题，是协议问题——设计三态协议防止 ACK storm
4. **自主进化**：编排者从失败中学习，写更好的 prompts
5. **可审计编排**：编排者可以隐藏实现细节，但不应隐藏影响链条；谁改写输入、谁压制分歧、谁拥有最终写入权，都应能追踪。
6. **保护编排者工作记忆**（[[Orchestrators-Tax]]）：subagent 的真正价值不是并行省时，而是把噪声推理挡在 orchestrator 上下文之外——token 花一次就完，context 污染此后每轮收租。任务按 cognitive locality（所需知识）切分而非按任务列表切分；文件所有权重叠是合并信号，不是 spawn 信号。

OpenRouter（2026-10）把多模型系统拆成三个需分别设计的层：工作流编排负责计划、状态、记忆与委派；模型路由负责选择调用模型和错误回退；provider 路由负责选择模型的服务端点。模型或 provider 路由本身不提供任务编排；反过来，LangGraph/CrewAI 这类工作流编排也可与独立模型网关组合。详见 [[20261002-openrouter-langchain-crewai-routing]]。

## 关键数据点

- 1+5+6 阵型：1 个编排者（Zoe）+ 5 个专业 Agent（ainews/Trading/Macro/Content/Butler）+ 6 个 ACP 编码专家
- Zoe 每天 3 次巡检（10:00/14:00/22:00），检查 cron 执行状态、磁盘使用、session 健康度
- 52 个 cron 任务每天自动轮转，覆盖 A 股 + 美股双时区
- 旧个人案例的上下文设置不代表当前模型能力；应按任务测量有效检索、延迟和上下文成本
- 完全互联拓扑的无向节点对数为 n(n−1)/2：3节点3对、6节点15对；并非实际通信量或所有编排拓扑的复杂度

## 前提与局限性

- 编排层解决的核心问题：编码 Agent 上下文局限、需要人工确认会卡住、进程死掉没人知道
- 既有案例的 ACP 与角色配置不具有必要性；单 Agent/确定性流程足以完成时应避免不必要委派。
- 早期设了 coding、architect、PM 三个技术角色后发现产出与 Zoe + ACP 组合高度重叠，反而增加通信复杂度，后来全砍了
- 每加一个 Agent 都需要半天到一天调试，处理通信冲突、共享资源竞争、规则兼容
- 对有状态、多方协作任务，需要明确消息、状态、幂等与失败语义；具体协议不必统一为一种实现。
- 不可见编排可能提高短期效率，但会制造 [[Invisible-Orchestrator|不可见权力结构]]：worker 不知道谁改变了自己的输入和策略，系统很难审计判断变化来源。

## 关联概念

- [[Agent-Swarm]] — 编排层与 Agent 群体协作配合
- [[Three-State-Protocol]] — 协议级通信确保编排可靠性
- [[Context-Engineering]] — 编排层持有业务上下文，编码层持有代码上下文
- [[Agent-First-Enterprise]] — Agent 编排是 Agent-First 运营的核心实践
- [[Corrective-RAG]] — CRAG 作为编排中的检索质量控制节点
- [[Reflexion]] — Reflexion 循环是编排中的关键反馈模式
- [[Dual-Tier-LLM-Architecture]] — 分层路由是编排中的请求分发策略
- [[Invisible-Orchestrator]] — 编排层隐藏权力和信息改写时的风险结构
- [[Multi-Agent-System-Pathology]] — 多 Agent 编排成功后暴露的组织病理
- [[Captain-Mindset]] — First Mate 作为 meta-orchestrator 的船长编排模式
- [[Kun-Chen]] — First Mate / Treehouse 并行 worktree 编排工具链
- [[Orchestrators-Tax]] — 编排核心问题从"跑几个 agent"转为"什么配进入 orchestrator 上下文"

## 来源
