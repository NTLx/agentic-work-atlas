---
type: entity
title: AGENTS.md
aliases:
  - AGENTS-md
definition: "面向编码 Agent 的项目指引文件，提供仓库及目录范围的约定、操作入口和验证要求；发现、合并和优先级取决于具体客户端，不能替代权限或强制门禁"
created: 2026-06-10
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - documentation
related_entities:
  - "[[Agent-Harness]]"
  - "[[CLAUDE-md]]"
  - "[[Harness-Engineering]]"
  - "[[Skills-as-Products]]"
source_raw:
  - "[[20260419-agent-harness-engineering]]"
  - "[[20260611-openai-harness-engineering]]"
  - "[[20260812-github-ai-first-contributors]]"
---

# AGENTS.md

> [!definition] 定义
> **AGENTS.md** 是 Agentic Engineering 中的一种核心配置文件。它与 `CLAUDE.md` 等项目指引有相近用途，不是永久修复或强制执行边界。按实际客户端的加载规则管理作用域。

## 关键数据点
- Codex 官方文档（2026-11-28核对）说明启动时从全局配置及项目根到当前工作目录构建指令链；每层优先 `AGENTS.override.md`，再 `AGENTS.md`，再配置的 fallback；每目录至多一个非空文件。近层指引在合并文本中覆盖远层，`project_doc_max_bytes` 默认32 KiB、可配置。官方 Prompting Guide 说明所发现指引作为 user-role 消息注入，而非 system prompt；不应将项目指引视为安全授权。
- 60行、100行等是历史案例建议，不是规范硬限制；优先短小、可发现、可验证。参见 [Codex discovery guide](https://learn.chatgpt.com/docs/agent-configuration/agents-md) 与 [Codex Prompting Guide](https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide)。
- **OpenAI 实践（2026）**：将 AGENTS.md 从"规则手册"重定义为"目录"——约 100 行，作为 map 指向 docs/ 中的深层知识。原因：巨型指令文件会挤占上下文、过多指导变成非指导、单体手册可能快速过时、难以做机械检查。
- **知识库结构**：docs/ 目录包含设计文档（含验证状态和 core beliefs）、架构文档（域和包分层地图）、质量文档（各领域分级和差距追踪）、执行计划（进度和决策日志）、已知技术债务。
- **机械验证**：专用 linter 和 CI 任务验证知识库时效性、交叉链接和结构正确性；doc-gardening agent 自动扫描过时文档并开修复 PR。

## AutoGPT 实践：目录作用域与 skill 发现（2026-08-13 编译新增）

AutoGPT（[[20260812-github-ai-first-contributors]]）在大型 OSS 的维护者视角补充了 AGENTS.md 的两个关键机制：

- **CLAUDE.md → 中央 AGENTS.md 的收敛**：先铺 `CLAUDE.md`（因 Claude 生成 PR 缺仓库上下文），但 Copilot/Codex 忽略 Claude 文件——于是集中标准 `AGENTS.md` 并让 Claude 文件指向它。关键教训：该团队发现无显式入口的 contributor docs 很少被读；不能推断所有客户端只能读当前目录，文档必须放在 agent 会看的地方。
- **目录作用域 vs skill 跨目录发现**：在 AutoGPT 案例中指引靠近相关代码；实际自动发现规则须按客户端验证，而 **skill 可跨目录发现**——skill 的 description 在启动时被 agent 预扫描，任务匹配才拉入完整指令，因此 skill 可以告诉 agent"该去哪个目录找 AGENTS.md"。
- **反面教训**：AutoGPT 曾在全库铺 AGENTS.md，导致上下文污染、把 agent 注意力引向无关文件——"A bad AGENTS.md file is worse than no AGENTS.md"。这是成本敏感、反直觉的实践（更全的 docs ≠ 更好的 agent 行为）。

## 前提与局限性
- **前提**: 客户端须支持发现并加载相关指引（也可显式读取）；不得将文件文字等同系统级指令、审批或实际执行控制。对关键约束使用受保护的测试、CI、权限和审计。
- **局限**: 随着规则增加，可能导致 Prompt 竞争模型有限的注意力，加剧上下文腐烂。
- **投入成本**: 结构化 docs/、linter、CI 和 doc-gardening agent 需要大量前期投入，小团队可能负担不起。
- **泛化边界**: OpenAI 的实践高度依赖其特定仓库结构和工具链，不应假定无需类似投入即可复现。

## 关联概念
- [[Agent-Harness]]
- [[CLAUDE-md]]
- [[Harness-Engineering]]
- [[Context-Rot]]
- [[Agent-Legibility]] — AGENTS.md 作为目录是 Agent Legibility 的核心实践
- [[Progressive-Disclosure]] — 仓库知识库的渐进式披露策略
