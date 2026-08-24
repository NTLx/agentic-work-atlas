---
type: topic
title: AI 时代设计师角色演化
created: "2026-08-17"
updated: "2026-08-17"
tags:
  - topic
  - design
  - ai-era
  - role-evolution
related_entities:
  - "[[Ian-Silber]]"
  - "[[Just-Do-Less]]"
  - "[[Capability-Overhang]]"
  - "[[OpenAI-Design-Team]]"
  - "[[Lenny-Rachitsky]]"
---

# AI 时代设计师角色演化

> [!topic] Topic 定位
> 围绕"AI 如何重写产品设计师的角色、流程、方法论与招聘标准"的主线，整合 OpenAI、Anthropic、Claude 等一线 AI 公司设计负责人的论述。

## 核心命题（一句话）

**AI 时代设计的瓶颈从"产出"迁移到"判断"——设计师的天花板在判断力（用户理解、新事物发明、point of view）而非产出速度；方法论从"重设计"转向"Just do less + Systems thinking + 复用 primitives"；招聘从"专业深度"转向"T 型 + 高 curiosity + prototyping + systems thinking"。**

## 三条核心张力（生成器）

### 张力 1：工程师 10x vs 设计师未 10x

| 角色 | AI 加成 | 瓶颈 | 原因 |
|------|---------|------|------|
| 工程师 | 10x–100x 产出 | 想法不够多 | coding agent 把"实现"变成 binary 任务 |
| 设计师 | 增量提升 | 仍然慢 | 设计是 messy + fluid 的 judgment loop，多次试错 + alignment |

**结论**：设计师的瓶颈不是"做得快不快"，而是"做得对不对"。这是 [[Jevons-Paradox-for-Knowledge-Work]] 在设计领域的具体体现——AI 加速产出，反而消耗了更多判断/对齐带宽。

### 张力 2：人类剩余价值 vs AI 能力

人类在三个"训练数据之外"的维度上仍有护城河：

1. **用户理解**：truly understanding what people need（依赖 human feedback loop）
2. **新事物发明**：doing something new（iPhone 多点触控、Instagram 移动优先、Snapchat 反直觉交互）
3. **Point of view**：独特观点与品味——AI 时代最难被复制的判别力

与 [[Taste]] 直接相关——Taste 是 point of view 在创意领域的具体化。

### 张力 3：极简默认 vs Broad Spectrum User

- **Capability overhang**（[[Capability-Overhang]]）：模型能力 >> 典型用户使用
- **Broad spectrum**：ChatGPT 同时服务"问疹子"和"建 Salesforce"
- **解法**：分层暴露——默认极简，cutting edge 给 care 用户

## 约束条件（边界）

| 约束类型 | 具体约束 |
|----------|----------|
| **硬约束** | 设计领域存在 novelty（人类对新交互范式的探索需求不会被 AI 替代）；设计过程包含 judgment loop（设计本质） |
| **软约束** | 产品 stability 决定 "Just do less" 是否适用；用户分层决定 capability overhang 是否关键 |
| **自设约束** | "设计师仍要保持 classical training"——Ian 想打破但确实存在的行业惯性 |

## 主要论述点（按 source 整合）

### OpenAI 视角（Ian Silber, 2026-08）

- 「Just do less」+ 「Systems thinking」是方法论核心
- 招聘不要求 AI 背景，要 curiosity + aptitude + prototyping + point of view
- Well-rounded team（generalists + visual + brand + prototypers + product thinkers）
- 两档 effort：sweat the details（关键 feature）vs ship in 4 hours（边缘 feature）

### Anthropic / Claude 视角（参考 Jenny Wen）

- "Design process is dead"——prototype/mock/test/iterate 流程压缩
- 角色转向 "big picture planning + steering people"

### Lenny Survey 数据（2026）

- 设计师在所有维度最不幸福（最 overwhelm、最 anxious、最不 optimistic、最 tired）
- 但做好的人最强相关 = "amplified by AI"——与 Ian 观察一致

## 跨域同构

- **Just do less ↔ "do the simple thing first"**：Ian 自陈跨公司迁移——同一条方法论的不同表达
- **Capable overhang ↔ 工具表达力浪费**：Excel、AutoCAD、iPhone 早期都有同构现象
- **Systems thinking ↔ Agent harness engineering**：跨岗位同构——AI 时代跨职能硬需求
- **Building in public ↔ Lean Startup**：big swings + 快速反馈循环

## 招聘标准的演化

```
传统设计师招聘                    AI 时代设计师招聘
─────────────────              ─────────────────
专业深度（视觉/交互/系统）        Curiosity + Aptitude
产出 portfolio                   Prototyping + Point of view
工具熟练度（Figma/Sketch）        Systems thinking + AI tool fluency
T 型（深度 + 协作）               T 型 + AI literacy + 跨产品形态理解
```

## 关联概念

- [[Ian-Silber]] — 主要发言人
- [[Lenny-Rachitsky]] — workforce survey 数据来源
- [[OpenAI-Design-Team]] — 一手观察来源
- [[Just-Do-Less]] — 核心方法论
- [[Capability-Overhang]] — 产品设计哲学
- [[Taste]] — Point of view 的更一般化讨论
- [[Jevons-Paradox-for-Knowledge-Work]] — 剪刀差的理论背景
- [[Harness-Engineering]] — Systems thinking 的 agent 侧同构
- [[Vibe-Coding]] — 与设计/开发的边界讨论
- [[Build-First-Business-Ontology]] — ontology 优先于 UI

## 待解问题

1. ~~「Just do less」在 stable enterprise 产品上是否适用？~~ **08-23 操作化裁决**：判别标准 = 验证环能否放回短延迟介质——一个 feature 的验证环能回短延迟（原型/金丝雀/红队）→ 做；只能靠长期观测才知对错 → 砍。（衍生判据：可委托度 = f(观测延迟 × 反馈闭合媒介)；短延迟[代码/语法本体]可委托 AI 人只审边界，长延迟[行为/对话]前置化拆子环。）
2. ~~「Point of view」是否真是 AI 时代的护城河，还是 Ian 对自己角色的辩护？~~ **08-23 裁决**：是护城河但需细分——「可被叙述化的判断」（理解、立场、方法论）会被 AI 收编；护城河只在「不可言说」（Victor：不存在于可提取介质的、过程性的手感）+「长期理解」（Norman：需要生活史反馈的"人为什么这样做"）的接缝。结论仍需 Jenny Wen / Joel Lewenstein 对照访谈 clip 确认。
3. 设计流程压缩是否会让设计师变成"产品决策者"而非"产品工匠"？——**08-23 部分回答**：AI 压缩 prototype/mock 后，判断环节从隐形到礼形毕露（判断税集中暴露）；"卖产出"→"卖在场判断"迁移中。未闭合。
4. capability overhang 在窄用户产品（Notion、Cursor）上是否仍是关键设计挑战？——开放。
5. ~~workforce survey 中设计师最不幸福——是角色本身问题，还是过渡期阵痛？~~ **08-23 裁决：经济基础位移（裂层）**——"最佳时代"与"最不幸福"同为真，是同一职业裂层两侧（定价权卖产出→卖在场判断）；驳 Ian "unclear what is expected" 归因。理由：设计师不幸福 = 可胜任区间（prototype/mock）被压缩 + 判断区间分量被放大，AI 同时喂强鉴赏力、养钝手感。

## 判据形态：Less 的接收者与判断的可还原性（08-23 圆桌 + 追本注入）

> 来源：圆桌（Rams/Norman/Maeda/Victor）+ 追本 5 层 + qa 7 问（2026-08-23T14:00，详情见 [[2026-08-23]]）。

### 1. Less 是"谓词悬空"——使用前须声明对谁减

- **Rams 的 Less but better**（造物道德）：对物本体减——物体本身应是本质的；
- **Ian 的 Just do less**（工程资源分配）：对工作组织减——不造没必要的 feature，复用 primitives；
- **Maeda 法则**：减法必须有方向——减 obvious、加 meaningful；无方向的 less 退化为"啥也别干"；
- **Victor 判据**：看减法是否压缩"判断→结果"的反馈延迟，是则好 less，否则只是"少做省事"的伪装。

### 2. 观测延迟定价律（设计域投影）

设计判断（行为流对象：对话/AI 产品）的反馈环路 = 月级、依赖第三方观察；工程师（代码对象）= 毫秒级（编译器/运行时当场反馈）。**生产率剪刀差（engineers 10x, design hasn't）是测量学结果，不是能力差**——两种判断实验的观测延迟不同，比较本身失真。

**追本修正：延迟只测后验产物**。最贵的判断（预感：要不要做、往哪做）发生在产物存在之前、无反馈对象，整体不在延迟测量架构内。"让 AI 替你想"才真正取消预感的载体，而"复用 primitives"是躲进别人的预感遗骸。

### 3. 设计师不幸福 = 经济基础位移（裂层）

- 证据：Lenny survey 设计师在所有维度最不幸福；但"被 AI 放大"的人最强相关幸福感。
- 解释：AI 压缩 prototype/mock 后，设计师只剩 test/iterate 里的判断环节，分量瞬间放大；此前判断被动作稀释（隐形），现在礼形毕露。
- 结论：**"最佳时代"与"最不幸福"同为真 = 同一职业裂层两侧**（卖产出 vs 卖在场判断）；不幸福是位移不是阵痛。

### 4. 手感只活在「做」里（追本底层）

- 知识可传、**行为史只能活**（"我做过"与"我懂"是不同的东西；判断标准可传 AI 而不损失，因为已固定成遗骸）。
- AI 拿走的不是手艺，是"做"本身：从亲手成形 → 从成品里挑。挑选是消费行为史（比较史），不是生产行为史（成形史）。
- **鉴赏力可被 AI 喂强（对象在场，输出×时间），手感只能亲手养（对象缺席，AI 给的是结果不是过程）、越养越钝**。
- 后果：创作者从手艺人批量迁移成鉴赏家，且以"解放"之名不自知——人格断层，感知器官被换。
- 与判断残余搬家定理的对位：残余会搬家，但搬的是"可交给断言的部分"；"做"的宿主消失时，手感无新坐标可落（断代而非重生）。

### 5. 可还原性 = 选择问题（追本最底层）

设计判断的不可还原既非 Victor 的观测延迟（可逼近）也非 Rams 的戒律内核（不可迁走），是：**"做"是否还在发生**。AI 替代成品但不能替代"你继续做"。可还原性问题回答了"AI 能否拥有设计判断"，而真相是它从认识论问题（能否提取）改写为存在论问题（是否还做）——不可还原不是知识特性，是"做"的字面失败。

### 6. 与跨域同构的接法

- Jevons 的产出越便宜判断越贵 → 判断税集中暴露（本节的证）
- 判断残余搬家定理 → 手感断代（本节的检验边界）
- Delegative-UI 的"实质权威从职位迁到前提规定能力" → 定价权卖产出→卖在场判断（组织层同构）

## Source

- [[20260816-openai-head-of-design-best-time]] — Ian Silber x Lenny Rachitsky (2026-08-16)
- 期待对照 source：
  - Jenny Wen (Claude head of design) — "The design process is dead"
  - Joel Lewenstein (Anthropic head of design)
  - Mike Krieger (Anthropic CPO)
  - Kevin Weil (OpenAI former CPO)
  - Andrew Ambrosino (OpenAI Codex lead)