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
不同 Runtime 可以直接发现它，也可以通过自己的 compatibility surface（例如
`.claude/skills/`）暴露；当前会话真正可用的能力始终以 Runtime 实际发现并向模型
暴露的 catalog 为准。

`skills-lock.json` 只记录来源、路径、版本引用和内容哈希，用于供应链追踪与
漂移审计，不是 Runtime capability registry，也不参与 Skill 路由。

没有可追溯代码仓库、但通过外部文本文件或其他人工方式获得的第三方 Skill，仍按
`external-managed` 能力处理；使用 `skills-lock.json` 记录 `sourceType: manual`、
说明性的分发来源/版本以及当前安装快照 hash。不要为了消除 `unmanaged` 状态而将其
错误声明为 `repository-owned`。

Schema 不维护完整的 `Task → Skill`、`Intent → Skill` 或 `Source Type → Skill`
表。新增一个符合 Agent Skills 规范且 description 清楚的 Skill，原则上只需
让 Runtime 发现它，不需要为它新增工作流分支。

## Orchestrator / Execution Context

Repository Schema owns lifecycle and policy。Orchestrator 是当前负责整体任务控制
的 Agent，通常就是产品中的 Main Agent；Schema 不依赖这些命名。实际 work unit 由
Execution Context 执行：它可以是 Orchestrator 自己，也可以是当前 Runtime 提供的
其他上下文。当 Orchestrator 把 bounded work unit 交给另一个 execution context 时，
该 context 称为 Execution Delegate。这是逻辑角色，不等同于任何特定产品功能。

Orchestrator 负责：

1. 理解用户目标，加载必要 Schema，明确 Knowledge lifecycle 和 side-effect budget；
2. 获取完成规划所需的最小上下文，识别当前 bounded work unit 与主要瓶颈；
3. 查看 Runtime catalog，独立判断选择一个 Skill 或 `none`；
4. 获得足够的 capability information 来完成 selection、compatibility 和 execution
   planning；需要读取 name/description、完整 `SKILL.md`、references，或由 Runtime
   提供其他 trusted capability contract，取决于当前 Runtime 的 invocation semantics；
5. 选择 direct、delegated 或 bounded parallel execution；
6. 观察 execution result、Evidence、Reasoning、Changes、Validation 和 side effects；
7. 必要时 replan，并完成 Wiki lifecycle、Evidence、promotion、Delta 的最终裁决。

Orchestrator 可以直接完成低成本、低歧义、短程、上下文很小且没有明显 delegation
收益的 work unit，例如精确搜索、provenance 查询、少量 metadata 读取、deterministic
检查或很小的 bounded Wiki 修改。它也可以把较重、长程、需要隔离或可并行的 work unit
交给 Execution Delegate。

Execution Context 负责在 bounded contract 内获得必要上下文、获得 Skill 的 authoritative
instructions（若选择了 Skill）、调用工具、完成 reasoning、执行允许的写入与验证，并
返回 decision-grade result。它不拥有 Wiki lifecycle、Evidence strength、promotion 或
Delta 的最终裁决权，也不得未经 Orchestrator 裁决扩大任务范围。

## Independent Decisions: Capability vs Execution

Skill selection 与 execution strategy 是两个独立决策：

```text
Capability: 需要额外 Skill X，或 none
Execution:  direct、delegated，或 parallel delegates
```

合法组合包括 `Skill: none` + direct、`Skill: none` + delegated、已选 Skill + direct，
以及已选 Skill + delegated。`Skill: none` 只说明当前 work unit 不需要额外认知
Operator，不要求也不禁止 delegation。

## Execution Strategy

不要建立 classifier 或固定 topology。以下因素明显存在时，优先考虑 Execution Delegate：

- 需要加载大量 task-local context，或需要真实执行较重 Skill 的完整 procedure；
- 工作长程、多步骤，或会产生较多 intermediate output；
- 独立 context 能减少 Orchestrator context pollution，或需要更合适的模型、权限、环境；
- 多个子任务彼此独立，存在真实 parallelism，或需要隔离较大的写入/工具执行；
- delegation 的额外 context、token、latency、协调和失败成本低于 direct execution。

反之，direct execution 是一等路径。Orchestrator 应采用最小充分 execution topology；
delegation 和 Agent 数量都不是质量指标。

当采用 delegation 时，Orchestrator 使用当前 Runtime 实际可用且最合适的 mechanism。
Schema 不规定 subagent、child thread、session、worker、executor package、remote Agent
或其他 primitive，也不维护 Runtime 到 mechanism 的映射。建立 clean、partial、isolated、
explicit context package 或其他上下文的具体方式由 Runtime 自行决定，但应优先提供
minimal sufficient context，避免无必要复制完整主会话。

默认保持 shallow delegation。只有当 task contract 允许、进一步 delegation 明显提高
质量或效率，且不突破 scope、side-effect、budget、ownership、single-writer 和
Evidence 边界时，Execution Context 才可继续 bounded delegation。不得创建新的 Skill
routing hierarchy、扩大 stable Wiki 修改范围或形成 uncontrolled agent swarm；对同一组
仓库文件默认保持 single writer，并行优先用于 read-only 或隔离验证。

## Dynamic Orchestration

各 Wiki operation 遵循以下通用循环，不预先构造 Skill DAG 或固定流水线：

```text
PLAN
  ↓
SELECT CAPABILITY
  ↓
CHOOSE EXECUTION MODE
  ↓
EXECUTE
  ↓
OBSERVE
  ↓
REPLAN
```

- **PLAN**：Orchestrator 理解 operation、加载必要 Schema、确定 lifecycle、side-effect
  budget 和 bounded work unit。
- **SELECT CAPABILITY**：选择最小充分 Skill 或 `none`。
- **CHOOSE EXECUTION MODE**：根据任务、上下文、Skill、成本和 Runtime capability 选择
  direct、delegated 或 bounded parallel execution。
- **EXECUTE**：实际 execution context 获得必要 context 和 Skill instructions，执行 task，
  在预算内写入和验证。
- **OBSERVE**：Orchestrator 审查 result、Evidence/Reasoning、diff、validation、side effects
  和新的 bottleneck。
- **REPLAN**：若出现新的瓶颈，重新独立选择 capability 与 execution mode；不预先建立完整 DAG。

Execution Context 若发现当前 work unit 需要另一种明显不同的能力，应返回 `New bottleneck`
或等价信号，由 Orchestrator 决定是否 replan。它不因这个信号自动扩大研究、写入范围或
生命周期。并行执行不得同时修改同一 `wiki/`、`raw/`、`state/` 或 `index.md`，除非 Runtime
明确提供安全 isolation / merge semantics 且 Orchestrator 有明确理由使用。

## Real Skill Execution

只有同时满足以下条件，才可声称使用某 Skill：

1. Skill 来自当前 Runtime catalog 或由用户明确指定；
2. 实际执行该 work unit 的 execution context 获得了该 Skill 的 authoritative instructions；
3. 该 context 实际遵循了与当前任务相关的方法、procedure、tools、scripts、references 或约束；
4. Skill 的 compatibility / side-effect 要求满足当前 Repository Schema；
5. 结果明确区分 Evidence、Skill-assisted Reasoning、execution result 和 validation；
6. Orchestrator 仍按 Schema 完成最终 Evidence、lifecycle、promotion 或 Delta 裁决。

Orchestrator 是否需要完整读取 `SKILL.md`，取决于当前 Runtime 的 Skill invocation semantics。
如果 Runtime 明确要求 Orchestrator 在执行或 delegation 前完整读取 Skill instructions，则
必须遵守 Runtime 自身要求；否则 Orchestrator 只需获得足够的 trusted capability information
来完成 selection、compatibility 和 planning。无论如何，实际 execution context 始终必须
获得 authoritative execution instructions。

以下不算真实 Skill 调用：只声称使用 Skill 后自行推理；按记忆或相似风格模拟；实际 context
未获得 `SKILL.md` 或等价 authoritative instructions；或把 Skill output 当成 Evidence。

### Execution Delegate Contract

不创建 contract 文件。采用 delegate 时，Orchestrator 传递 bounded、语义性的 task contract；
不要求某个 Runtime 使用完全相同的字段格式。最小内容包括：

```text
Operation:
Task:
Inputs:
- ...
Relevant Evidence / Context:
- ...
Capability:
<Skill / none>
Constraints:
- obey Repository Schema and relevant schema/*
- Evidence != Reasoning
- Schema > Skill native workflow
- ...
Side-effect Budget:
- ...
Write Scope:
- ...
Stop Conditions:
- ...
Return:
- Status
- Capability actually used
- Evidence
- Reasoning
- Changes
- Validation
- New bottleneck
```

不要把整个 Schema 复制进 contract；Execution Context 通过仓库自身读取必要规则。

当 Capability 为某 Skill 时，实际执行 context 必须获得其 authoritative instructions；
当 Capability 为 `none` 时，不加载无关 Skill、不模拟任何 Skill。Execution Context 返回
紧凑结果，不返回完整 transcript：

```text
Status: success | blocked | partial | failed
Capability actually used: <skill name + locator | none | failed: reason>
Evidence: - ...
Reasoning: - ...
Changes: - ...
Validation: - ...
New bottleneck: <none | description>
```

某个 delegation mechanism 因瞬时 Runtime 问题失败时，不要无限重试同一种 mechanism。
Orchestrator 应重新评估其他合法 delegate 或 direct execution；如果没有任何能真实执行
该 task / Skill 的 execution context，才明确返回 `blocked` 或 `failed`。不得因 delegation
失败而把 Skill 改写成 `none`，也不得凭记忆模拟 Skill。

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
