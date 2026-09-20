---
type: topic
title: AI 时代设计师角色演化
created: "2026-08-17"
updated: "2026-09-19"
evidence_level: medium
claim_type: mixed
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
source_raw:
  - "[[20260816-openai-head-of-design-best-time]]"
  - "[[20250724-anthropic-product-design-claude-code]]"
  - "[[20260301-jenny-wen-design-process-dead]]"
  - "[[20260820-joel-lewenstein-crafting-last-mile-delight]]"
  - "[[20260528-microsoft-copilot-new-design]]"
  - "[[20260831-microsoft-coreai-product-simplicity]]"
  - "[[20260919-google-gemini-visual-design]]"
---

# AI 时代设计师角色演化

> [!topic] Topic 定位
> 围绕“AI 如何重写产品设计师的角色、流程、方法论与招聘标准”的主线进行综合。当前已有 OpenAI、Anthropic、Microsoft 与 Google Gemini 的可回溯一手材料；但各家披露层级不同——Anthropic/Microsoft 有团队运行与部分结果数据，Google 当前主要覆盖 design-object / trust / legibility——因此整体结论继续按 `medium` 处理。

## 核心命题（一句话）

**AI 正在压缩设计执行层，把更多工作重心推向“做什么、为什么做、如何验证、何时接受粗糙版本、谁承担最终决策责任”。但 judgment / taste 不能再写成永久的人类专属能力；当前更稳定的结论是 execution 可迁移，decision authority、quality allocation 与 accountability 仍需要明确 owner。**

## 三条核心张力（生成器）

### 张力 1：工程师 10x vs 设计师未 10x

| 角色 | AI 加成 | 瓶颈 | 原因 |
|------|---------|------|------|
| 工程师 | 10x–100x 产出 | 想法不够多 | coding agent 把"实现"变成 binary 任务 |
| 设计师 | 增量提升 | 仍然慢 | 设计是 messy + fluid 的 judgment loop，多次试错 + alignment |

**结论**：设计师的瓶颈不是"做得快不快"，而是"做得对不对"。这是 [[Jevons-Paradox-for-Knowledge-Work]] 在设计领域的具体体现——AI 加速产出，反而消耗了更多判断/对齐带宽。

### 张力 2：人类剩余价值 vs AI 能力

OpenAI / Ian Silber 强调用户理解、novelty 与 point of view；但 Anthropic / Jenny Wen 明确认为模型在 taste / judgment / design 上还会继续进步。因此这些更适合作为**当前差异化能力**，而不是永久的人类护城河。

目前更稳定的人类侧边界是组织责任：谁决定什么值得做、何时上线、哪一处值得投入最后一公里 craft，以及谁对结果负责。与 [[Taste]] 的关系应因此拆成“能力差异”与“责任归属”两个问题。

### 张力 3：极简默认 vs Broad Spectrum User

- **Capability overhang**（[[Capability-Overhang]]）：模型能力 >> 典型用户使用
- **Broad spectrum**：ChatGPT 同时服务"问疹子"和"建 Salesforce"
- **解法**：分层暴露——默认极简，cutting edge 给 care 用户

## 约束条件（边界）

| 约束类型 | 具体约束 |
|----------|----------|
| **硬约束** | 设计工作需要对目标、风险、反馈与结果做选择；但这些选择不应被预设为永久只能由人类完成，真正硬约束是 decision authority / accountability 必须可归属 |
| **软约束** | 产品 stability 决定 "Just do less" 是否适用；用户分层决定 capability overhang 是否关键 |
| **自设约束** | "设计师仍要保持 classical training"——Ian 想打破但确实存在的行业惯性 |

## 主要论述点（按 source 整合）

### OpenAI 视角（Ian Silber, 2026-08）

- 「Just do less」+ 「Systems thinking」是方法论核心
- 招聘不要求 AI 背景，要 curiosity + aptitude + prototyping + point of view
- Well-rounded team（generalists + visual + brand + prototypers + product thinkers）
- 两档 effort：sweat the details（关键 feature）vs ship in 4 hours（边缘 feature）

### Anthropic / Claude 视角（Product Design / Jenny Wen / Joel Lewenstein）

- [[20250724-anthropic-product-design-claude-code]]：设计师直接改前端与 state-management、把 mock 变成交互原型，并在设计阶段处理 error / logic / system status；内部自报部分执行 2–3x 加速。
- [[20260301-jenny-wen-design-process-dead]]：mock/prototype 在其经验中的工作占比由约 60–70% 降至 30–40%；长期 vision 收缩到 3–6 个月方向性原型；同时明确“最终仍有人决定什么值得做并承担责任”。
- [[20260820-joel-lewenstein-crafting-last-mile-delight]]：中间 flow/basic-components 层大量被 Claude 吸收，团队转向 code-first / prototype-first；“intentional craft”决定何处必须极致、何处可以粗糙换学习速度；多个 agent/PR 同时完成又制造新的 review / attention bottleneck。

**稳定边界**：Anthropic 直接材料支持“设计对象与工作流扩展、execution compression、attention/review bottleneck、显式 quality allocation”；不支持“judgment 永久不可自动化”。

### Microsoft 视角（Copilot / CoreAI, 2026）

- [[20260528-microsoft-copilot-new-design]]：Jon Friedman 把 Microsoft 365 Copilot 的设计对象明确扩展到 output quality，包括 tone、structure、readability、usefulness 与 trustworthiness；新 interaction model 从 prompt box 转向 task-aware workspace 与 app 内 agentic mode。
- 同一来源给出真实 rollout 指标：load time 降低超过 50%，complex-prompt p95 first-token latency 约改善 10%，Word / Excel / PowerPoint / Outlook 的 Copilot usage 在短期 rollout 窗口分别上升 27% / 33% / 43% / 30%。
- [[20260831-microsoft-coreai-product-simplicity]]：当前 CoreAI 设计团队中，一部分设计师已经通过 VS Code / GitHub Copilot CLI 直接贡献 production code；AI 加速后，新问题变成跨 portal / workflow / navigation 的 consistency 与 coherence。
- CoreAI 把 product simplicity 拆为 Decision Making / Engineering Craft / Coherence Making / Product Craft，说明设计治理已经横跨决策、工程、一致性与体验，而非单一视觉层。

**稳定边界**：Microsoft 比其他来源更强地支持“execution speed → coherence/governance bottleneck”，并且给出 rollout telemetry；但仍未公开 model-behavior RACI、launch review ownership 或 incident accountability。

### Google Gemini 视角（current design team）

- [[20260919-google-gemini-visual-design]]：Gemini 当前设计团队把一个持续变化、不可完全预测的 AI assistant 当作 relational system，而不是固定工具。
- thinking、listening、synthesis、directional progress 等系统状态通过 motion / gradient / responsive container 被转译成用户可理解的 process cue。
- 设计目标显式包含 trust、discoverability、familiarity、error forgiveness 与 exploration safety。
- 团队把 designer 描述为持续重绘“变化中的地图”的 cartographer，而不是一次性定义固定界面。

**稳定边界**：Google 当前材料强支持“model/process legibility 本身是设计对象”，但尚不能支持 code-first workflow、RACI、rollout result 或 incident ownership，因此 Google 这一支仍低一档。

### 跨公司收敛

当前四家公司材料共同支持的最小模型是：

~~~text
AI execution friction ↓
        ↓
design object expands
(UI → output / behavior / system state / workflow)
        ↓
new bottleneck shifts
(review / coherence / quality allocation / attention)
        ↓
decision authority + accountability
must remain explicit
~~~

其中，最后一行是组织治理命题，不是“人类 judgment 永远优于模型”的能力定理。

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
2. ~~「Point of view」是否真是 AI 时代的护城河？~~ **09-19 对照后收窄**：不能再写成能力本体上的永久护城河。Jenny Wen 明确预期模型继续改善 taste/judgment/design；Joel Lewenstein 也把当前优势写成方向选择与 last-mile craft，而不是不可跨越能力。保留的稳定命题是：当前组织仍需有人承担方向、质量阈值与责任。
3. ~~设计流程压缩是否会让设计师变成"产品决策者"而非"产品工匠"？~~ **09-19 部分闭合**：不是二选一。Jenny/Joel 的材料显示执行层被压缩，但方向决策、quality allocation、last-mile craft 与 accountability 同时保留；更准确是“工匠执行减少 + 决策/审查/最后一公里 craft 权重上升”。
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
- [[20250724-anthropic-product-design-claude-code]] — Anthropic Product Design team case study
- [[20260301-jenny-wen-design-process-dead]] — Jenny Wen x Lenny Rachitsky (2026-03-01)
- [[20260820-joel-lewenstein-crafting-last-mile-delight]] — Joel Lewenstein x IDEO (2026-08-20)
- [[20260528-microsoft-copilot-new-design]] — Jon Friedman / Microsoft 365 Copilot redesign
- [[20260831-microsoft-coreai-product-simplicity]] — Jenny Lanier Wolski / Microsoft CoreAI
- [[20260919-google-gemini-visual-design]] — current Gemini design-team retrospective
- 后续跨公司对照仍缺：Google Gemini/DeepMind 与 Microsoft 的实际 RACI / launch review / incident ownership，以及各家可比的 feedback latency、返工率和质量结果。