---
type: entity
title: Agent Ergonomics
aliases:
  - Agent Ergonomics
  - Agent 人体工学
  - AXI
definition: "将 Agent 视为工具的第一公民（first-class citizen），通过 token-efficient 输出格式、低延迟接口和结构化交互设计优化工具对 Agent 的效率。Kun Chen (2026) 提出 AXI 十原则，benchmark 显示 AXI 标准工具比传统 MCP server 节省 3x token 成本。"
created: 2026-06-22
updated: 2026-11-11
evidence_level: medium
claim_type: mixed
tags:
  - agentic-engineering
related_entities:
  - "[[ACI-Agent-Computer-Interface]]"
  - "[[Agent-Harness]]"
  - "[[Tool-Use-Architecture]]"
  - "[[Agentic-Engineering]]"
  - "[[Agentic-Workflow-Token-Efficiency]]"
source_raw:
  - "[[20261110-latentspace-resend-designing-for-agents]]"
  - "[[20260620-l8-principal-agentic-workflow]]"
  - "[[20261022-latentspace-modal-d]]"
---

> [!definition] 定义

## Resend 的 Agent Experience：可发现性、准确理解与实际完成是三种不同质量（2026-11）

[[20261110-latentspace-resend-designing-for-agents]]（**05:02–06:54、37:55–49:53、58:28–1:12:14**）展示 Agent-first developer product 的几类独立障碍：coding agent 即使面对已有 Cloudflare Email 配置，也可能推荐新服务；Resend 的 JS 定价滑块让 Agent 错误计算 120 万封邮件价格，换成机器可读 Markdown 表后几天复测得到正确值；MCP 中 Contacts 单次返回太大造成上下文容量问题。团队同时保持 API、CLI、SDK、UI 和 Remote MCP 等不同的消费表面。

- **判断（综合）**：Agent Ergonomics 不止要求 token-efficient，还需要 **准确发现/选择、机器可读事实、明确权限、任务级完成与可核验终态**。HTML 与 Markdown 价格不应双维护，应从同一事实源生成；应在相同任务下比较 80+ 命名 MCP tools 和 Code Mode 2-tool 方案的成功率、总 tokens、轮次和响应体积。
- **证据**：[[20261110-latentspace-resend-designing-for-agents]]；与 [[20261022-latentspace-modal-d]] 的 Agent benchmark/API 兼容债、[[20261028-latent-space-supabase-agents]] 的文件化状态相互补充。
- **边界**：Resend 受访者自报 MCP 增长、定价修复是单个前后对比，不能因增长或一次答对断言 llms.txt/.md 必然改变所有模型的推荐；80+ 和 2-tool 未做对照测评。


> Agent Ergonomics 是一种工具设计哲学：不为人类优化界面，而为 Agent 优化接口。核心指标是 Agent 完成同一任务所需的 token 数、turns 数和成功率。

## 核心原则（AXI 十原则摘要）

Kun Chen 在 AXI（axi.md）中提出 10 条 Agent-first 工具设计原则，核心要点：

1. **Token-efficient 输出格式**：不用 JSON，用紧凑格式可节省约 40% tokens
2. **低延迟接口**：减少 round-trip，batch 操作优于逐条调用
3. **结构化交互**：给 Agent 可直接解析的结构化数据，而非人类可读的自由文本
4. **确定性语义**：工具返回值含义明确，Agent 无需猜测或二次确认
5. **错误信号清晰**：错误信息包含足够上下文让 Agent 自行修复

## Agent 成为 API Consumer 后：文档也是未来行为接口（Modal，2026-10）

[[20261022-latentspace-modal-d]] 把 Agent Ergonomics 从“单次工具调用效率”扩展到 **API lifecycle**。Modal 会让真实 Agent 自主完成部署、启动 sandbox 等任务，并观察它是否自然选择 Modal、是否能正确完成任务；这比只测人类 developer experience 更接近 Agent-first 产品的真实消费方式。

更值得注意的是 deprecation 问题：Erik Bernhardsson 说，公开网络中存在大量旧 Modal syntax，而这些代码会进入模型训练数据；即使官方文档已经升级，Agent 仍可能反复生成旧调用方式。因此 Modal 需要更谨慎地下线 feature，并尽可能更新公开 examples。

这形成一种新的技术债：**model-memory compatibility debt**。

```text
public docs / examples / repos
        ↓ enter training corpora
model learns API habits
        ↓ months / years later
agent generates old syntax
        ↓
provider must preserve compatibility
or supply strong correction signals
```

**判断**：面向 Agent 的接口稳定性不只由当前 docs / SDK 决定，还受历史公开代码在模型参数中的滞后记忆约束。Agent-first API 因此需要同时优化：可发现性、machine-readable semantics、legacy compatibility、examples consistency，以及 task-level Agent benchmark。

访谈还指出，sandbox 这类 Agent workload 更自然的接口可能是 imperative SDK：launch → act → tear down，而不是只为人类基础设施工程师设计的声明式 DSL。这里的核心不是“imperative 永远优于 declarative”，而是 **ACI 应匹配 Agent 实际控制循环**。

- **证据**：[[20261022-latentspace-modal-d]]，Transcript 52:30–57:00；来源描述 Agent benchmark、旧 syntax、公开代码训练数据及 SDK 形态。
- **边界**：这是单一基础设施厂商的一手观察，没有公开 benchmark 量化旧 syntax 的失败率；基础模型的具体训练数据不可完全观测，“进入训练数据”应理解为公司基于行为的机制判断，而非逐样本 provenance 证明。

## 关键数据点

- GitHub MCP server vs GitHub CLI benchmark：同一任务，MCP 花费 **3x token 成本** + **2x 延迟**，无明确收益
- Token-efficient 输出格式相比 JSON 可节省约 **40% tokens**
- Chrome DevTools AXI 相比其他浏览器工具：更少 turns、更少 tokens 完成相同任务
- AXI 工具在 ProgramBench 评测中显示最高成功率 + 最低成本

## 前提与局限性

- AXI benchmark 由作者自行设计和执行，methodology 和 dataset 未公开，需独立复现验证
- Token-efficient 格式（非 JSON）可能增加 Agent 的解析错误率，尤其在模型能力较弱时
- AXI 原则适用于 CLI/API 工具，对需要丰富上下文的 MCP 工具（如需要 schema 描述的工具）适用性待验证
- 工具设计优化是**一次性投入**，需要评估 ROI：高频使用的工具（如 GitHub、浏览器）优化价值高，低频工具不值得专门优化

## 关联概念

- [[ACI-Agent-Computer-Interface]] — Agent-Computer Interface，更广义的 Agent 友好接口设计
- [[Agentic-Workflow-Token-Efficiency]] — Token 效率在 agent 工作流中的系统性优化
- [[Tool-Use-Architecture]] — 工具使用的系统架构设计
- [[Progressive-Disclosure]] — 工具信息的按需加载，减少 system prompt 膨胀
