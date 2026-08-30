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

仓库中的 `.agents/skills/` 是本仓库的 Skill capability inventory，不是所有
Runtime 的自动发现入口。Agent 当前真正可调用的 Skill 集合，以当前 Runtime
实际发现并向模型暴露的 catalog 为准。不同 Runtime 可以有不同发现入口；例如
Claude Code 的项目级 Skills 通过 `.claude/skills/` 自动发现。

`skills-lock.json` 只记录来源、路径、版本引用和内容哈希，用于供应链追踪与
漂移审计，不是 Runtime capability registry，也不参与 Skill 路由。

Schema 不维护完整的 `Task → Skill`、`Intent → Skill` 或 `Source Type → Skill`
表。新增一个符合 Agent Skills 规范且 description 清楚的 Skill，原则上只需
让 Runtime 发现它，不需要为它新增工作流分支。

## Dynamic Selection

在 compile、query、explore、produce 或其他 Wiki 任务中，Agent 按以下协议循环
判断：

1. 先理解用户意图、当前知识状态和任务边界，不先寻找 Skill。
2. 用 search-first 或当前操作规定的最小上下文定位材料，并说清最大的
   未解决认知瓶颈。
3. 查看当前 Runtime catalog 中 Skill 的 `name + description`，判断它是否真的
   能解决这个瓶颈；允许选择 `none`。
4. 选择最小充分的 Skill 集；只对真正选中的 Skill 读取完整 `SKILL.md`，以及
   该 Skill 指定且当前动作需要的附属资源。
5. 在执行前检查 compatibility：读取选中 Skill 声明的工具权限、持久化行为、
   交互要求、headless 能力和网络边界，与当前 Wiki operation 的 side-effect
   budget 比较。只有 `safe` 才执行；发生冲突时改选其他 Skill 或 `none`。
6. 执行一个局部认知动作或执行动作，记录其结果的来源和不确定性。
7. 观察结果：如果任务已经足够，停止；如果出现新的瓶颈，再重新查看能力描述
   并选择下一步。不要在任务开始时预先构造完整 Skill DAG 或静态流水线。

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
