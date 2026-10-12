---
type: source-summary
title: "How our vibe coded website looks like a designer made it"
canonical_url: "https://railcode.dev/blog/vibe-coded-website"
source_raw:
  - "[[20260810-railcode-vibe-coded-website]]"
raw_state: index
created: 2026-10-12
updated: 2026-10-12
tags:
  - source-summary
  - vibe-coding
  - design
  - taste
  - coding-agents
evidence_level: medium
claim_type: mixed
source_locator:
  - "opening: counterexample to generic AI design slop; coding agents as means to realize a specific creative vision"
  - "A whole lotta rollercoasters: external inspiration, intensity spectrum, multiple variants, go-wild outliers"
  - "Rollercoaster Tycoon: generated playable experiment rejected as too much; search narrows to a visual asset"
  - "Going off the rails: isolated asset becomes coherent system only after contextual iteration"
  - "Forks on forks: single-HTML exploration, side-by-side forks, retained lineage, parameter playgrounds"
  - "Inspiration: concrete reference work as steering substrate"
  - "closing process summary: generate broadly, discard heavily, preserve forks, use playgrounds, iterate"
---

# How our vibe coded website looks like a designer made it

> Yakko Majuri 对 Railcode 官网设计过程的一手复盘。价值不在证明“AI 已替代设计师”，而在于把一个非设计师如何用 coding agents 扩展审美探索空间、保存分叉、比较候选、构造直接操作的 design playground 讲得足够具体。来源是单个 founder 的自述，模型偏好和最终审美评价均不能外推为普遍结论。

## 1. 浓缩

### 1.1 Coding agent 的设计价值首先是扩展搜索空间，不是一次生成成品

作者先从 Railcode 的 “code on rails” 品牌语义联想到 rollercoaster，再围绕这个概念让 agent 生成大量视觉候选。方法并不是要求一个“好设计”，而是显式要求：

- 同一概念覆盖不同 intensity / complexity；
- 一次至少生成多个版本；
- 部分版本给明确方向，剩余版本允许“go wild”；
- 大多数结果预期会失败，但失败候选仍可能触发新的方向。

其中一个夸张 neon 方案并未被采用，却让作者联想到 Rollercoaster Tycoon，进而把整个网站的视觉世界从 ASCII rollercoaster 推向 amusement park。

**判断**：生成式设计更适合表示为搜索问题，而不是生成问题：

```text
seed / reference
  → broad candidate generation
  → human rejection / selection
  → recombination / association
  → local refinement
  → new candidate branch
```

模型降低的是候选生成成本；方向性仍来自人类对“哪里有感觉、哪里不对、什么值得继续”的连续选择。

### 1.2 “坏候选”可以具有 option value

作者明确说大量初始设计“绝大多数很差”，但早期暴露过的组件和风格会在后续突然变得有用。例如 CTA 的最终方向来自更早一批并未采用的网站 mockup。

**判断**：当候选生成足够便宜时，探索阶段不应只最小化失败率。部分看似浪费的候选承担的是 **option generation**：扩大人类当前能看到的解空间。

这与“让模型直接给最优答案”的工作流相反。对于审美探索，过早压缩成单一候选可能损失比节约的 token 更多的信息。

**边界**：这不意味着候选越多越好。作者的流程依赖自己持续比较、记忆和筛选；候选过量也会形成注意力成本。本文没有测量最优分支数。

### 1.3 Fork lineage 把 subjective taste 变成可回看的决策轨迹

作者在设计阶段尽量维持单个 HTML 文件，主要理由不是工程架构，而是方便快速复制版本、只改少数变量、并排比较。他不会删除 forks，而是保留探索分支；最终可能继续某个 fork，也可能回到父版本。

可以抽象为：

```text
artifact v0
 ├─ fork A: one variable changed
 ├─ fork B: another direction
 │   └─ fork B2
 └─ fork C

side-by-side comparison
      ↓
human selection
```

**判断**：在难以形式化的品质层，provenance 不只是审计需求，也是判断工具。保留“我从哪里来、拒绝了哪些版本”可以让创作者比较决策，而不是被最新一次生成覆盖历史。

这为 Vibe Coding 增加了一个此前较少被讨论的正向结构：如果探索性工作保留 branch lineage，vibe 不必等于无状态、无记忆、一次性 prompting。

### 1.4 Playground 把高频微调从语言接口移回直接操作

在颜色选择上，作者没有持续通过自然语言要求 Claude 修改具体色值，而是让 agent 构建一个 playground，使自己可以实时调整 accent、text、grass、background 等变量。

**判断**：好的 AI 创作工作流不会把所有 interaction 都强行语言化。Agent 可以用来**生成更适合人类判断的界面**，然后把连续、低语义、视觉反馈密集的参数搜索交回 direct manipulation。

```text
agent generates search instrument
          ↓
human manipulates variables directly
          ↓
fast perceptual feedback
```

这比“prompt → 等生成 → 再 prompt”更贴合视觉判断的反馈速度。

### 1.5 Taste 在这里表现为 rejection bandwidth，而不是 prompt 文采

整篇文章最稳定的模式是：大量生成 → 大量拒绝 → 少数保留 → 再分叉。作者最终满意的设计并不是模型一次推导出的统一 style，而是自己不断拒绝 out-of-place 元素、调整整体语境、让 hero 反向约束后续页面所得。

**判断**：在高生成供给场景中，Taste 的操作能力可以进一步拆成：

```text
exposure bandwidth
× comparison bandwidth
× rejection bandwidth
× recombination ability
× attention to local inconsistency
```

其中 coding agent 主要扩大 exposure / generation bandwidth；是否形成 coherent design，则依赖后四项。

## 2. 与现有知识的关系

### 对 [[Vibe-Coding]]

本文不是对 Karpathy 原始 Vibe Coding 定义的反驳。它仍然是直觉驱动、快速生成、以感受导航的探索过程。但它显示 Vibe Coding 在创意品质层可以拥有比“单次 prompt + 不看代码”更成熟的工作结构：

- broad generation；
- explicit branching；
- side-by-side comparison；
- preserved lineage；
- direct-manipulation playground；
- sustained human selection。

因此要区分 **vibe as epistemic mode** 与 **sloppy process**。直觉导航并不必然要求丢失版本历史或拒绝比较工具。

### 对 [[Taste]]

现有 Taste 页已把 taste 定义为生成供给过剩后的选择函数。本文给出一个非常具体的设计域实例：作者真正花时间的不是让模型“多做一个”，而是决定哪个方向有生命、哪个只是局部漂亮但放进整体后失调、哪个坏方案值得保留一个 motif。

它还补充了一个训练机制：**保存 forks 并并排比较**。Taste 的训练需要 exposure + attention，而 branch lineage 让比较从模糊记忆变成显式对象。

## 3. 证据边界

- 单个 founder 的过程报告，没有对照实验，不能推出该方法优于专业设计流程。
- “网站看起来像设计师做的”来自作者收到的反馈与个人判断，不是盲评。
- 作者偏好某一模型用于设计属于个人经验，受模型版本、提示习惯和任务类型影响，不应升级为模型排名事实。
- 生成 4–10 个候选、单 HTML 探索等是作者工作习惯，不是通用最佳参数。
- 文章强调 coding agents 让作者更愿意参与设计，而不是“设计师不再需要”。专业设计中的用户研究、可访问性、品牌系统和复杂交互验证并未被本文覆盖。

## 4. 关联概念

- [[Vibe-Coding]]
- [[Taste]]
- [[Agentic-Engineering]]
- [[Friction-as-Design-Signal]]
- [[Ownership]]
