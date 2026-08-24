---
title: "Explore 管控规则与 Source 需求"
type: schema-subdoc
---

> 本文档是 Agentic Work Atlas Schema 子文档，由 README.md 路由表按需加载。

# Explore 管控规则与 Source 需求

Explore 有两个不同模式：

- **开放探索**：发现新问题、反例方向和 Source 需求。
- **Claim Recompile**：只检查 agenda 队列中的一个既有 Claim，不负责发现第二个主题。`tools/daily-thinking-agent-prompt.md` 是执行入口，`schema/recompile-workflow.md` 是唯一运行协议。

## Explore 管控规则

`explore(topic)` 的输出必须包含：
- **新问题**：下一轮值得验证的问题。
- **证伪方向**：哪个判断可能是错的，应该找什么反例 source。
- **Source 需求**：日常阅读和剪藏时应主动寻找什么材料。
- **下一步目标建议**：下一轮最应该推进哪个主题、问题或剪藏方向。
- **最小实验**：下一步最小可执行动作。

Explore 可调用的技能（Agent 自主判断触发时机，无需用户指令）：

| 技能 | 触发条件 | 效果 |
|------|----------|------|
| **ljg-think** (追本之箭) | 需要对某个观点/现象层层下钻 | 层层降深到不可再分的底层结构 |
| **ljg-rank** (降秩) | 需要对整个领域提炼不可约生成器 | 找 2-3 个核心生成器，建立领域骨架 |
| **ljg-constraint** (约束) | 需要找出某个领域/角色/争论的真实约束 | 区分硬/软/自设约束，框出解空间，与 ljg-rank 配对使用 |
| **ljg-qa** (问答提取) | 需要从现有 Wiki 页面中抽取探测性问题 | 暴露知识缺口和推理断裂点 |
| **ljg-roundtable** (圆桌) | 需要对争议性 topic 做多立场辩证 | 生成证伪方向、分歧点、共识边界 |
| **ljg-blind** (盲区扫描) | 用户明确要求，或 agenda 已记录具体盲区审计需求 | 照出认知盲区 + 定向补充材料 → Source 需求队列 |
| **ljg-learn** (概念解剖) | 需要对探索中浮现的核心概念做深度理解 | 八维度解剖 → 顿悟句 → 填补概念空白 |
| **ljg-read** (伴读) | 探索中需要跨域联想激发新方向 | 跨域旁逸 → 发现被忽略的类比和关联 |
| **ljg-invest** (投资分析) | 探索涉及 AI 公司/项目评估时 | 秩序创造机器框架 → 判断收录价值 |
| **aihot** | 需要外部现实对照"业界现在怎么样了" | 查询最新 AI 行业动态，为证伪方向提供外部参照 |

### Claim Recompile 技能边界

定时重编译默认不调用重型 Skill。一次运行最多调用 `ljg-roundtable-recompile` 或 `ljg-think-recompile` 其中一个：前者只处理无法由 source 区分的竞争解释，后者只处理证据已基本充分的 Boundary/Mechanism Gap。外部搜索与重型 Skill 同轮互斥。本模式不调用 `ljg-qa`，也不调用会交互并写外部笔记的原始 roundtable/think Skill。

Skill 输出属于 reasoning，不是 Evidence；完整 transcript 不进入仓库。Claim Recompile 只修改 Research，稳定 Wiki 晋升由独立 compile/audit 操作完成。

### 盲区审计边界

盲区扫描不是按编译篇数触发的固定流水线。只有用户明确要求，或 agenda 已把某个可验证的视角缺口列为当前行动时才调用；结果先进入 Source 需求队列，不直接制造新 topic 或永久保存新 raw。

research agenda 是缓冲层，不是事实层。它只能支撑“我们正在研究什么”，不能支撑“事实是什么”。当 agenda 中的问题长期没有 source 支撑、没有被 output 使用、也没有推动 compile，应删除、合并或归档。

## Source 需求队列

`wiki/research/research-agenda.md` 应维护一个 `## Source 需求队列`，用于把探索结果转化为日常信息获取目标。

```markdown
## Source 需求队列

| 目标 | 当前缺口 | 下一步 source | 触发行动 |
|------|----------|---------------|----------|
| xxx | 缺反例 / 缺一手案例 / 缺工程细节 | 寻找什么材料 | clip / compile / output / 暂缓 |
```
