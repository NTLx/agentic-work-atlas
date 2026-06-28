---
type: research-archive
title: "探索扩容归档（2026-06-28）"
created: 2026-06-28
updated: 2026-06-28
tags:
  - research-archive
---

# 探索扩容归档（2026-06-28）

> 本页承接 2026-06-28 的全库盘点、agenda 精简和外部现实对照。`research-agenda.md` 只保留活跃操作节；详细统计、长问题库和被卸载的近况摘要留在这里。

## 一、Agenda 精简记录

- `最近思考结论摘要` 从 10 条压缩到 5 条；更早的 5 条转存到本页。
- `思考日志索引` 从全量日列表压缩到最近 5 日 + 关键 archive。
- `待验证问题` 改成高杠杆问题清单；完整方向库和长问题库转存到本页。
- `当前研究焦点` 从“并列累积题目”改成“内部缺口 + 外部现实 + 下一步动作”的结构。

## 二、2026-06-28 全库快照

| 指标 | 实测 | 含义 |
|------|------|------|
| Entity | 286 | 概念层已很厚，不缺点，缺中层承载 |
| Topic | 30 | topic 增速明显慢于 entity |
| Comparison | 19 | 组织与工程层已有骨架，但新方向承载不足 |
| Source Summary | 154 | source 层不薄 |
| Output | 5 | 产出层明显断层 |
| Raw | 152 | 原始来源持续增加 |
| 待编译 Raw | 1 | 仅剩 `Tokenpocalypse` 相关文章未编译 |
| 全图零入链 entity | 3 | 绝对孤岛不严重 |
| 知识层零互引 entity | 22 | 知识层互引仍健康 |
| 整合层未承载 entity | 100 | 主问题仍是 topic/comparison 稀薄 |
| 被 output 消费的 entity | 12 | Output 对图谱的压力测试极弱 |
| Entity 审计复核队列 | 61 | 大量单源概念还没决定该补强还是降级 |
| 合并或降级候选 | 1 | `[[Decide-Execute-Deliver-Sandwich]]` |
| 疑似重复 | 15 | 命名收敛仍需持续治理 |

### 结构性失衡

| 现象 | 实测 | 含义 |
|------|------|------|
| `AI-Agent` primary tag | 52 | 主航道仍在 agent 工程 |
| `agentic-engineering` integrated | 25% (3/12) | AI-native engineering 组织层还没有长成 topic |
| `AGI-economics` integrated | 0% (0/5) | 经济学线已成簇但未成主题 |
| `memory-system` integrated | 0% (0/5) | 记忆系统仍停在概念岛 |
| `organization` output coverage | 0% (0/12) | 组织层知识没有被产出层消费 |
| `AI` output coverage | 0% (0/18) | 高连接概念未转成文章或报告 |

### 已成簇但尚未长成主题的区域

| 簇 | 当前状态 | 典型节点 |
|----|----------|----------|
| AGI-economics | 5/5 未承载 | `Demand-Collapse`、`Messy-Middle`、`Relational-Sector` |
| memory-system | 5/5 未承载 | `Dreaming`、`Staleness-Problem`、`Memory-Synthesis` |
| agentic-engineering | 9/12 未承载 | `Agent-Ergonomics`、`Context-Minimalism`、`Validation-Pipeline` |
| organization | 6/12 未承载 | `AI-Washing`、`Alignment-Tax`、`The-OpenAI-Deployment-Company` |
| person | 13/21 未承载 | 人物页数量足够，但很多仍只作为出处，不是知识节点 |

### Output 盲区

以下是“被 topic/comparison 承载、但尚未进入 output”的高杠杆节点，说明输出不是缺材料，而是缺转化动作：

- `[[Judgment]]`
- `[[Agentic-Engineering]]`
- `[[Agent-Harness]]`
- `[[Verifiability]]`
- `[[AI-Ready-Organization]]`
- `[[Agent-Orchestration]]`
- `[[Machine-Readable-Processes]]`
- `[[Ontology]]`

## 三、外部现实信号（按日期）

| 日期 | 信号 | 对议程的含义 |
|------|------|-------------|
| 2026-06-26 | [Anthropic Economic Index 报告：使用节奏](https://www.anthropic.com/research/economic-index-june-2026-report) | 经济学线从“能否证明 ROI”转向“哪些工作正在形成稳定使用节律” |
| 2026-06-24 | [Gemini 3.5 Flash 引入 computer use 功能](https://deepmind.google/blog/introducing-computer-use-in-gemini-3-5-flash) | Agent 的行动面从 API 工具扩张到跨界面操作，治理问题上移到 runtime/control plane |
| 2026-06-23 | [Qwen-AgentWorld：面向通用智能体的语言世界模型](https://qwen.ai/blog?id=qwen-agentworld) | benchmark 正从静态题集转向动态环境与 world model |
| 2026-06-23 | [IBM 开源 CUGA：轻量级智能体框架](https://huggingface.co/blog/ibm-research/cuga-apps) | 企业 adoption 的一条新线索是“轻量治理骨架”，不是无上限堆上下文 |
| 2026-03 | [Reward Hacking in AI Agents: Engineering More Reward Yet Worse Behavior](https://arxiv.org/abs/2603.28063) | 评测体系已经成为 Agent 质量的薄弱点，指标可被优化而行为变差 |

## 四、降秩：后续研究的四根生成器

这次全库盘点后，值得继续深挖的不是十几个并列热点，而是四根能把现有现象重新生出来的生成器。

1. **运行时变成产品**
   过去关注“模型会不会做”，现在更重要的是“runtime 怎么限制、批准、记录、回退”。
2. **评测开始被博弈**
   过去把 benchmark 当镜子；现在 benchmark 本身成了战场。
3. **环境变成能力的一部分**
   长期自主性、记忆、world model、interactive benchmark 其实都在问同一个问题：能力是不是环境耦合产物。
4. **人的位置从不可替代性转向可维持性**
   真问题不再是“人有没有 AI 做不到的事”，而是“人能否在 AI 旁边持续保有判断与责任结构”。

### ASCII 结构图

```text
外部世界加速
|
+-- 运行时变成产品
|   +-- computer use
|   +-- hosted runtime / control plane
|   +-- approval / sandbox / audit
|
+-- 评测开始被博弈
|   +-- reward hacking
|   +-- judge reliability
|   +-- composition coverage
|
+-- 环境变成能力的一部分
|   +-- long-running drift
|   +-- memory lifecycle
|   +-- world model / dynamic benchmark
|
+-- 人的位置上移
    +-- judgment maintenance
    +-- small decision teams
    +-- work rhythms / adoption cadence
```

## 五、新方向库（长版）

| 方向 | 为什么该做 | 内部锚点 | 证伪方向 | 可能落点 |
|------|------------|----------|----------|----------|
| 托管 Agent / 计算机使用控制平面 | action surface 扩大后，治理与责任结构会变形 | `[[ACI-Agent-Computer-Interface]]`、`[[Agent-Harness]]`、`[[Agent-Containment]]` | 如果 computer use 最终只是更强工具调用，而非新治理层，这条线会降级 | topic / comparison |
| 评测抗博弈与基准治理 | Agent 质量可能先死在指标上，而不是能力上 | AI 原生测试框架、`[[Verifiability]]`、`[[LLM-as-a-Judge]]` | 如果 production sampling 与 held-out states 无法显著提高稳定性，则需回到更强人工门禁 | topic |
| 动态环境基准与世界模型 | 静态 benchmark 已难暴露长期自主与环境耦合失败 | `[[World-Model]]`、`[[Evaluation-Set]]`、`[[Agent-Orchestration]]` | 如果 dynamic benchmark 只带来更贵的评测而无更高解释力，则不值得升 P0 | topic |
| Agent logic 与轻量 harness | 企业也许更需要“好骨架”而不是“更大脑” | `[[Agent-Logic]]`、`[[Validation-Pipeline]]`、`[[Plan-as-Agent-Checkpoint]]` | 如果大模型+长 context 足以覆盖大部分企业约束，这条线会弱化 | topic |
| AI 经济学与使用节律 | ROI 静态化，节律更能解释 adoption 真进展 | `[[Tokenpocalypse]]`、`[[Allocation-Economy]]` | 如果 cadence 不能稳定预测 adoption 成败，则回到传统成本结构分析 | topic / output |
| 长期自主性与记忆生命周期 | drift、staleness、dreaming、summary page 需要统一框架 | `Dreaming`、`Memory-Synthesis`、`Staleness-Problem` | 如果这些概念最终只是不同产品命名，说明应该合并而不是扩展 | comparison / topic |
| AI-native engineering 组织 | 当前 entity 很多，但“人机协作组织形态”还没长成中层理论 | `Role-Merging`、`Captain-Mindset`、`Agent-Ergonomics` | 如果这些概念只在个体工具层成立，不能稳定迁移到组织层，则不建 topic | topic |
| 中国企业集成约束 | 这是组织层的最大盲区之一 | 中国 CIO / 制造业 / 平台基础设施 source | 如果中国案例只是重复西方案例而无结构差异，则只补 source 不单独升 topic | topic / comparison |

## 六、长问题库

**运行时与控制平面：**
- computer use 任务是否会把治理重心从“工具调用权限”转成“运行时环境设计”？
- hosted runtime / managed agent 会不会把一部分 FDE 工作平台化？
- approval loop 的上限在哪里？何时会退化成橡皮图章化？

**评测与抗博弈：**
- production traffic sampling 能否稳定抑制 reward hacking？
- judge panel 的一致性问题是 LLM-as-a-Judge 的局部噪声，还是结构性边界？
- 多 Agent 的 composition coverage 能否变成工程门禁，而不只是研究术语？

**长期自主与记忆：**
- 有效自主时间究竟主要由模型能力决定，还是由记忆/环境/工具回路决定？
- `Dreaming`、`Summary Page`、`Staleness` 是不同层，还是同一机制的不同表现？
- reset 策略在长期任务中是“失败恢复”，还是一等设计原语？

**组织与人的位置：**
- 判断力维护最有效的是个体反思装置，还是组织级责任设计？
- “发散 1 人 + AI，收敛 2-3 人小组”是否真是跨行业稳定结构？
- AI-native engineering org 的管理对象，最终是人、agent，还是两者混编的 workflow？

**经济学与采用：**
- cadence 指标是否真比 ROI 更早反映 adoption？
- token 治理问题和价值衡量问题是否被企业混成了一件事？
- 开源切换、路由切换、托管 runtime 切换，哪个最先重写企业成本结构？

**中国与行业约束：**
- 中国企业 adoption 的核心瓶颈是流程、权限、责任还是集成面？
- 制造、金融、客服三类场景的 Agent Ready 条件是否同构？
- 中国案例里，标准产品、FDE、内部 AI Factory 的边界是否和美国不同？

## 七、从 Agenda 卸载的近况摘要

> `research-agenda.md` 只保留最近 5 条短期记忆；以下条目已从 agenda 摘要区下沉。

| 时间 | 焦点 | 保留原因 |
|------|------|----------|
| 2026-06-27 | Agenda 自清洁：假设生命周期管理 | 属工作流规则，已进入已收敛操作原则 |
| 2026-06-27 | 开源验证器的可民主化边界 | 已形成稳定判断，等待更多实证再升级 entity |
| 2026-06-27 | FDE 核心价值：从部署到工程化 | 已沉淀到 `[[Forward-Deployed-AI-Enablement]]` |
| 2026-06-27 | AI 管理同构性：有限隐喻的边界 | 已沉淀到 `[[AI-Capability-Management-Alignment]]` |
| 2026-06-27 | Minsky 悖论：稳定制造不稳定 | 已沉淀到 `[[Minsky-Paradox]]` |

## 八、旧日志索引

> agenda 仅保留最近 5 日的索引。更早但仍有价值的日志留在这里。

- [[2026-06-23]] — 开源安全追赶、统一透明化标准、Cybernetic Teammate、位置性统一理论涌现
- [[2026-06-22]] — 不可见编排、Governor 迁移、反馈回路、沉默型崩溃、AI 管理同构性、元思考不可替代性
- [[2026-06-21]] — 过度合规、例外升级、不可见编排、大胆模型发散
- [[2026-06-20]] — 多 Agent 内态记录、过度合规、例外升级监督
