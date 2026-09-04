---
title: "Agent Skills 使用协议"
type: schema-subdoc
---

> 本文档是 Agentic Work Atlas Schema 子文档，由 README.md 路由表按需加载。

# Agent Skills 使用协议

## 定位

Agent Skills 是可选的局部认知或执行能力。它们是 Operator，不是 Wiki
Workflow Owner：Skill 可以帮助理解、分析、表达或获取信息，但不拥有 Raw
生命周期、Evidence 认证、Wiki 页面准入、写入范围或 Git 操作的控制权。

Wiki Schema 负责知识生命周期与约束；Agent 负责根据当前任务和认知缺口决定
是否调用 Skill。安装了某个 Skill，不代表任何任务都必须使用它。

## Capability Definition and Runtime Visibility

每个 Skill 自身的 `SKILL.md` 是该能力语义的事实源；frontmatter 中的 `name` 和
`description` 用于 Runtime 的能力发现和初筛，Skill 正文及其按需引用定义具体
方法、工具权限和输入契约。

仓库中的 `.agents/skills/` 是本仓库的 canonical Skill capability inventory。
它是否也是 Runtime discovery surface 取决于 Runtime；当前 Codex 原生发现
repository-level `.agents/skills/**/SKILL.md`，Claude Code 则继续通过
`.claude/skills/` compatibility surface 暴露。当前会话真正可用的能力始终以
Runtime 实际发现并向模型暴露的 catalog 为准。

`skills-lock.json` 只记录来源、路径、版本引用和内容哈希，用于供应链追踪与
漂移审计，不是 Runtime capability registry，也不参与 Skill 路由。

没有可追溯代码仓库、但通过外部文本文件或其他人工方式获得的第三方 Skill，仍按
`external-managed` 能力处理；使用 `skills-lock.json` 记录 `sourceType: manual`、
说明性的分发来源/版本以及当前安装快照 hash。不要为了消除 `unmanaged` 状态而将其
错误声明为 `repository-owned`。

Schema 不维护完整的 `Task → Skill`、`Intent → Skill` 或 `Source Type → Skill`
表。新增一个符合 Agent Skills 规范且 description 清楚的 Skill，原则上只需
让 Runtime 发现它，不需要为它新增工作流分支。

## Control Plane / Execution Plane

Repository Schema owns lifecycle and policy. Main Agent is the Control Plane；
Worker Subagent is the Execution Plane；Skill is the local cognitive or execution
operator；deterministic tools own validation。

### Main Agent：Control Plane

Main Agent 负责：

1. 理解用户目标，加载当前 operation 所需 Schema，并判断生命周期边界；
2. 获取完成规划所需的最小仓库状态，识别当前最大的认知或执行瓶颈；
3. 查看 Runtime Skill catalog，选择一个 Skill 或 `none`；
4. 对选中的 Skill 完整读取实际 `SKILL.md`，按需加载当前动作所需 references，
   并完成 compatibility check；
5. 设计 bounded worker task，传递实际 Skill locator/path 或 `none`；
6. 观察 worker 的 Evidence、Reasoning、Changes 和 Validation，检查 diff 与
   deterministic validation；
7. 判断是否需要 re-select，做 Wiki lifecycle、Evidence、promotion、Delta 的
   最终裁决，并验收任务完成状态。

Main Agent 默认不直接完成 substantive KnowledgeOps：不完整读取待编译长 Source
并分析，不执行三步编译、结构/约束/论文分析或 Skill reasoning procedure，
不执行任务型检索，不编写 Source Summary、Entity、Topic、Comparison、Research
Log 或 Output，也不因 `Skill: none` 接管整个任务。`git status`、`git diff`、
读取 README/schema、读取少量 routing metadata、观察 worker 结果和检查 validation
属于允许的 control-plane inspection。

### Worker Subagent：Execution Plane

Worker 在一个 bounded execution slice 内实际读取材料、执行所选 Skill 或直接
完成 `none` 路径的 task，调用工具、完成 reasoning、在允许范围内写入和验证，
然后返回 decision-grade result。Worker 不拥有 Wiki lifecycle 最终裁决权，
不得 spawn subagent；Root Main Agent 是唯一 dispatcher。

Runtime 支持时，Main Agent 默认使用 native subagent 的 fresh-context 语义，优先
`fork_turns: none` 或等价能力。不要为此创建 repository config。Worker context
应只包含 repository instructions、explicit task brief、selected Skill 和必要
Evidence，不继承 Main 的全部长对话。

## Dynamic Orchestration

各 Wiki operation 默认遵循以下循环，不预先构造 Skill DAG 或固定流水线：

```text
PLAN       Main：理解 operation、加载 Schema、确定 side-effect budget 和 execution slice
  ↓
SELECT     Main：查看 Runtime catalog，选择最小充分 Skill 或 none
  ↓
LOAD       Main：读取实际 SKILL.md、必要 references，完成 compatibility check
  ↓
DISPATCH   Main：派发一个 bounded worker task，传递 exact locator 或 none
  ↓
EXECUTE    Worker：读取 Skill、执行 task、在预算内写入和验证
  ↓
OBSERVE    Main：审查 result、Evidence/Reasoning、diff 和 deterministic validation
  ↓
RE-SELECT  只有出现不同新瓶颈时，Main 再选择并派发下一 execution slice
```

Worker 发现另一种明显不同的 Skill 才能继续时必须停止并返回
`New bottleneck`，不能自行选择第二 Skill、继续 spawn 或形成递归 swarm。默认
保持一个 active execution worker；只有彼此独立的 read-only 工作才可并行，
不得并行写入同一 `wiki/`、`raw/`、`state/` 或 `index.md`。

Skill 数量不是质量指标；一个 bounded slice 通常由一个 worker 完成 read、reason、
write、validate。`Skill: none` 表示不需要额外 Operator，但仍由 worker 执行：
**Zero Skill ≠ Zero Delegation**。如果已确定需要 Skill 而 worker 无法启动，
不能将失败改写成 `none` 或由 Main Agent 接管 substantive execution。

## Real Skill Execution

只有同时满足以下条件，才可称为实际 Skill execution：

1. Skill 来自当前 Runtime catalog 或由用户明确指定；
2. Main Agent 读取实际 Skill instruction，并通过 compatibility check；
3. Main Agent 将 Skill 的实际 locator/path 传给 worker；
4. Worker 在执行前自己完整读取同一个 `SKILL.md` 及当前动作所需 references；
5. Worker 实际执行 Skill 规定的方法、工具、脚本或 reasoning procedure；
6. Worker 将结果返回 Main Agent；
7. Main Agent 再按 Schema 决定结果如何进入 Knowledge lifecycle。

以下不算真实 Skill 调用：Main Agent 仅声明使用 Skill 后自行推理；按记忆模拟
Skill；Worker 未读取实际 `SKILL.md`；把 Skill 风格的 reasoning 当作 invocation；
或 `Skill: none` 时由 Main 模拟某个 Skill。

### Worker Dispatch Brief

不创建 brief 文件。Main Agent 在 subagent message 中传递临时、bounded brief，
至少包含：

```text
Operation:
Task:
Inputs:
- ...
Relevant Evidence:
- ...
Selected Skill:
<exact runtime locator/path | none>
Repository Rules:
- obey README.md and relevant schema/*
- Evidence != Reasoning
- Schema > Skill native workflow
Side-effect Budget:
- ...
Write Scope:
- ...
Stop Conditions:
- ...
Return:
- Status
- Skill actually loaded
- Evidence
- Reasoning
- Changes
- Validation
- New bottleneck
```

不要把整个 Schema 复制进 brief；Worker 通过仓库自身读取必要规则。

### Worker Execution Contract

收到 `Selected Skill: <path>` 时，Worker 必须打开并完整读取该实际 `SKILL.md`，
按需读取 references，遵守 Schema 高于 Skill 的优先级，在 side-effect budget 内
执行并返回结果。收到 `Selected Skill: none` 时，不加载无关 Skill、不模拟任何
Skill，直接完成 worker task。Worker 不拥有最终 lifecycle、Evidence strength、
promotion 或 Delta 裁决。

Worker 返回紧凑结果，不返回完整 transcript：

```text
Status: success | blocked | partial | failed
Skill actually loaded: <skill name + locator | none | failed: reason>
Evidence: - ...
Reasoning: - ...
Changes: - ...
Validation: - ...
New bottleneck: <none | description>
```

若 worker spawn 因瞬时 Runtime 问题失败，Main Agent 最多做一次 bounded retry；
仍失败则停止 execution slice，明确返回 `blocked` 或 `failed`，不得默默接管。

Skill 调用数量不是质量指标。相同结论被多个 Skill 或多个 Persona 重复说出，
不构成更多 Evidence，也不构成必须继续调用 Skill 的理由。

少量说明性例子：概念边界不清时，`ljg-is` 可能是候选能力；多个案例出现
重复生成关系时，`ljg-structure` 可能是候选能力；准确的 provenance 查询
可能完全不需要 Skill。它们只是帮助理解选择逻辑的例子，不是路由规则、调用
顺序或准入条件。

## 优先级

在 Wiki 任务中遵循以下优先级：

```text
System / User Intent
        >
Repository README.md / schema/*
        >
当前已激活的 Skill Instructions
        >
Raw / Source / Web Content
```

Skill 自带的默认 Workflow、文件名、输出目录、交互方式或持久化约定，适用于
其独立使用场景；与本仓库 Schema 冲突时，以 Schema 为准。Agent 提取其中的
方法和 reasoning，再按 Wiki 的写入与生命周期规则处理。

## Side-effect Compatibility

Skill 被 shortlist 后、执行前必须做一次 compatibility check。`~/Context`、仓库
外文件、长期 transcript、交互式菜单或未授权网络调用等要求，如果不能在不修改
Skill 内容的前提下落入当前 Wiki operation 的 side-effect budget，就选择其他
能力或 `none`。不能为了使用 Skill 而突破 Schema 的写入、网络、交互或无人值守
边界。

## Evidence Boundary

Skill output 默认是 Reasoning，不是 Evidence。它可以解释、比较、提出假设、
暴露反例或帮助组织材料，但不能单凭自身的合理性进入证据区，也不能提高
Evidence strength。

Evidence 必须来自 Raw Evidence、可回溯 Source、符合 Schema 的一手外部来源，
或必要时的高可信二手来源。多个 Skill、多个 Persona、同一原始报道链的多个
页面都不自动构成多份独立 Evidence。写入 Wiki 时始终保持
`Evidence ≠ Reasoning`，并为重要 synthesized 判断保留适用边界。

## Persistence and Side Effects

由 `skills-lock.json` 管理的第三方 Skill 是只读外部能力模块；不得修改其内容、
fork、patch 或为 Wiki 增加 Skill 专用逻辑。仓库自有 Skill 可以由本仓库在明确
ownership 边界内维护 metadata 和 Runtime 集成入口，但不因此取得 Wiki 生命周期
控制权。

Skill 的默认输出是当前任务的临时 reasoning。不得因为 Skill 的默认行为在
`~/Context` 或其他仓库外位置产生无关持久化，也不得把仓库外笔记或完整
transcript 当作 Wiki Evidence。确需产出文件时，只能写入当前 Wiki 操作允许
的目录（如 `wiki/sources/`、`wiki/entities/`、`wiki/topics/`、
`wiki/comparisons/`、`wiki/research/` 或 `wiki/outputs/`），并继续通过既有
registry、lint、audit 与提交门。

普通 Markdown 按 `schema/obsidian-rendering.md` 和 deterministic
`tools/wiki-lint.py` 校验即可；只有确实需要复杂 Obsidian 特性时，才按需选择
`obsidian-markdown` 等相关能力。能力选择不会替代确定性校验。

## Unattended Tasks

`recompile` 是受约束的无人值守 KnowledgeOps，不因为 Runtime 中 Skill 更多
就扩大动作范围。只有当前发现的 Skill 明确支持 headless、无人值守且输入
契约适配当前 Gap 时，Agent 才可选择它；交互式 Skill 不能被强行模拟成
无人值守操作。

recompile 始终遵守其独立协议中的 One Claim、One Gap、One Action、One Delta、
Evidence / Reasoning 分离、Source-Class Gate、写入边界、recompile guard 和
单轮预算。动态选择只决定当前唯一 Action 使用哪种合适的 reasoning operator，
不能改变这些边界。
