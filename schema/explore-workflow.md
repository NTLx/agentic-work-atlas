---
title: "Explore 管控规则与 Source 需求"
type: schema-subdoc
---

> 本文档是 Agentic Work Atlas Schema 子文档，由 README.md 路由表按需加载。

# Explore 管控规则与 Source 需求

Explore 有两个不同模式：

- **开放探索**：发现新问题、反例方向和 Source 需求。
- **Claim Recompile**：只检查 agenda 队列中的一个既有 Claim，不负责发现第二个主题。
  `tools/daily-thinking-agent-prompt.md` 是执行入口，`schema/recompile-workflow.md`
  是唯一运行协议。

## Explore 管控规则

`explore(topic)` 的输出必须包含：

- **新问题**：下一轮值得验证的问题。
- **证伪方向**：哪个判断可能是错的，应该找什么反例 source。
- **Source 需求**：日常阅读和剪藏时应主动寻找什么材料。
- **下一步目标建议**：下一轮最应该推进哪个主题、问题或剪藏方向。
- **最小实验**：下一步最小可执行动作。

这些是 Research lifecycle 的输出契约，不是 Skill 调用契约。Agent 先读取当前
Wiki、Research Agenda 和相关 Source，再判断最大的研究缺口；只有在某种局部
认知动作确实有帮助时，才查看 Runtime 当前发现的 Skill 的 `name + description`
并选择最小充分能力。可以选择不使用 Skill，也可以在得到中间结果后重新判断
下一步，但不得预先生成完整 Skill 表或固定 Skill pipeline。

Skill 输出只能作为 reasoning：不能自动成为事实、Evidence、稳定 Claim 或新页面，
也不能仅凭多个 Skill 的一致意见扩大 Research Agenda。Source 需求、反例方向和
最小实验仍须按本文件及 `schema/research-module.md` 的边界写入。

### Claim Recompile 技能边界

定时重编译是 bounded autonomy，而不是开放探索。它只能从当前明确支持
headless、无人值守且输入契约适配当前 Gap 的 Runtime Skill 中选择 reasoning
operator；交互式 Skill 不能被强行模拟成无人值守操作。每轮最多一个重型
reasoning Skill，不因 Skill 数量增加而增加 Action；具体的 One Claim、One Gap、
One Action、One Delta、Source-Class Gate、写入边界和 guard 规则以
`schema/recompile-workflow.md` 为准。

### 盲区审计边界

盲区扫描不是按编译篇数触发的固定流水线。只有用户明确要求，或 agenda 已把某个
可验证的视角缺口列为当前行动时才调用；结果先进入 Source 需求队列，不直接制造
新 Topic 或永久保存新 Raw。

Research Agenda 是缓冲层，不是事实层。它只能支撑“我们正在研究什么”，不能支撑
“事实是什么”。当 agenda 中的问题长期没有 Source 支撑、没有被 Output 使用、也
没有推动 Compile，应删除、合并或归档。

## Source 需求队列

`wiki/research/research-agenda.md` 应维护一个 `## Source 需求队列`，用于把探索
结果转化为日常信息获取目标。

```markdown
## Source 需求队列

| 目标 | 当前缺口 | 下一步 source | 触发行动 |
|------|----------|---------------|----------|
| xxx | 缺反例 / 缺一手案例 / 缺工程细节 | 寻找什么材料 | clip / compile / output / 暂缓 |
```
