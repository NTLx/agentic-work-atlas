---
type: entity
title: AGENTS.md
aliases:
  - AGENTS-md
definition: "放置在代码库根目录的 Markdown 规范文件，作为 Agent 的“棘轮（Ratchet）”规则手册或知识地图，记录特定代码库的约束、习惯和过去错误的补丁"
created: 2026-06-10
updated: 2026-06-16
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
> **AGENTS.md** 是 Agentic Engineering 中的一种核心配置文件。它与 `CLAUDE.md` 类似，但更强调作为**针对 Agent 失败的永久补丁集**。

## 关键数据点
- 在 OpenAI Codex 的优先级栈中，`AGENTS.md` 内容通常被级联并拥有极高的 System Prompt 优先级。
- 建议保持在 60 行以内。
- **OpenAI 实践（2026）**：将 AGENTS.md 从"规则手册"重定义为"目录"——约 100 行，作为 map 指向 docs/ 中的深层知识。原因：巨型指令文件会挤占上下文、过多指导变成非指导、单体手册会立即腐烂、难以做机械检查。
- **知识库结构**：docs/ 目录包含设计文档（含验证状态和 core beliefs）、架构文档（域和包分层地图）、质量文档（各领域分级和差距追踪）、执行计划（进度和决策日志）、已知技术债务。
- **机械验证**：专用 linter 和 CI 任务验证知识库时效性、交叉链接和结构正确性；doc-gardening agent 自动扫描过时文档并开修复 PR。

## AutoGPT 实践：目录作用域与 skill 发现（2026-08-13 编译新增）

AutoGPT（[[20260812-github-ai-first-contributors]]）在大型 OSS 的维护者视角补充了 AGENTS.md 的两个关键机制：

- **CLAUDE.md → 中央 AGENTS.md 的收敛**：先铺 `CLAUDE.md`（因 Claude 生成 PR 缺仓库上下文），但 Copilot/Codex 忽略 Claude 文件——于是集中标准 `AGENTS.md` 并让 Claude 文件指向它。关键教训：**agents 不会主动读 docs，只读"面前的东西"（当前工作目录层级）**，文档必须放在 agent 会看的地方。
- **目录作用域 vs skill 跨目录发现**：`AGENTS.md` 严格按目录作用域（sits beside the code it governs），而 **skill 可跨目录发现**——skill 的 description 在启动时被 agent 预扫描，任务匹配才拉入完整指令，因此 skill 可以告诉 agent"该去哪个目录找 AGENTS.md"。
- **反面教训**：AutoGPT 曾在全库铺 AGENTS.md，导致上下文污染、把 agent 注意力引向无关文件——"A bad AGENTS.md file is worse than no AGENTS.md"。这是成本敏感、反直觉的实践（更全的 docs ≠ 更好的 agent 行为）。

## 前提与局限性
- **前提**: Agent 必须有读取文件系统的权限，且 Harness 能够将其内容注入 System Prompt。
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
