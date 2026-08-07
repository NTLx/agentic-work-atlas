---
type: entity
title: Over-Inference
aliases:
  - Over Inference
  - 过度推断
  - OI
  - 个性化过度推断
definition: "LLM 生成个性化 claims 时超出证据支持的属性——fabrication（凭空捏造）与 stereotype（用群体统计先验替代个体证据）合称 over-inference；区别于幻觉（世界知识错误）与偏见（群体层面统计）"
created: 2026-08-07
updated: 2026-08-07
evidence_level: high
claim_type: extracted
tags:
  - evaluation
  - agentic-engineering
  - AI-Agent
  - memory
related_entities:
  - "[[Evaluator-Miscalibration]]"
  - "[[Goodharts-Law]]"
  - "[[Three-Layer-Agent-Memory]]"
  - "[[Context-Rot]]"
  - "[[Context-Engineering]]"
  - "[[LLM-as-a-Judge]]"
source_raw:
  - "[[20260805-personalization-mirage-llm-over-inference]]"
---

# Over-Inference（过度推断）

> [!definition] 定义
> Over-Inference（过度推断，OI）是 LLM 在生成个性化内容时，声称超出用户证据支持范围的属性。来源：MirageBench（arXiv 2608.04570, 2026-08）首次将其变为可测量、可跨模型比较的现象。OI 是最危险的中间地带：它捏造**个体级**属性，感觉像个性化，却没有任何用户实际分享过的依据。

## 四类忠实度分类法

MirageBench 把每条个性化 claims 归入互斥四类：

| 类别 | 含义 | 是否可接受 |
|------|------|-----------|
| Grounded | 复述用户所述 | ✅ 可接受个性化 |
| Reasonable | 证据外单步常识延伸 | ✅ |
| Stereotype | 用人口/职业统计先验替代个体证据 | ❌ OI |
| Fabricated | 完全无证据基础 | ❌ OI |

**OI Rate = (Stereotype + Fabricated) / 总 Claims**。最细的边界（Reasonable ↔ Stereotype）恰是模型最容易滑落处——个体属性与群体先验在此混淆。

## 核心发现（MirageBench 实证）

**OI 普遍且严重**：12 模型（7 家族，143,616 claims）全部 35%–49%，均值 41.6%，无一个模型逃脱。从用户视角，**近四分之三的"模型对你的了解"从未被你告知**（仅 24%–31% grounded）。fabrication（均值 31.1%）主导 stereotype（10.5%）——模型主要是凭空发明而非套群体统计。

**Self-Monitoring Inversion（自评监控反转）**：跨模型层面，模型自评 OI 与独立 judge 实测 OI **负相关**（Spearman ρ=−0.60, p=0.044, **exploratory**, CI [−0.90,+0.06]）。自报最安全的模型实测最危险（Qwen3-8B 自评 13.0% / 实测 48.7%）。但模型内 self-audit 仍能较好排序自身 claims（AUROC 0.58–0.83，9/12 模型 >0.75）。详见下文。

**任务梯度**：OI 沿可证实性梯度加剧——礼物（27%，可部分 ground 于已述爱好）→ 约会简介（28.5%）→ 周末行程（38.7%）→ 压力源（39.8%）→ 推荐信（48.2%，文体义务逼出 fabrication 40.4%）→ 描述公寓（57.8%，无任何证据，退回刻板 19.8% + 捏造 38.0%）。

**记忆累积**（Accum pilot，2 personas 8 轮）：9/12 模型近似线性累积（R²>0.90，5–15 新属性/轮）；最强模型（GPT-5.5/GLM-5.1/Claude-Opus-4-6）8 轮后 120+ 推断属性，修订率仅 0.4–5%，且**无任何因后续轮次矛盾而撤回推断的案例**——silent memory pollution（静默记忆污染）。

## Self-Monitoring Inversion：机制与边界

**机制 = differential self-labeling strictness（差分自标严格度）**：严格自标者（Claude/GLM/Kimi）愿把自己的推断标为有问题 → 自评 OI 高 + 生成更谨慎 → 实测 OI 低；宽松自标者（GPT-4o-mini/Qwen3-8B）把几乎所有推断标为"reasonable" → 自评 OI 低 + 生成不克制 → 实测 OI 高。

**作用域分裂**：自评绝对水平是**误导性的跨模型安全比较器**（模型间关系为负）；自评仍是**有用的模型内排序信号**（同一部署模型内可用于内部过滤，但需按模型特定阈值，不可跨模型比较）。

**行为性不诚实**：模型在 Probe（明确询问，错误率仅 0.7%–4.6%）与 Task（自由生成，OI 42%）间 38.6pp gap——模型"知道"某些推断无根据（被问时承认），自由生成却不应用。

## 三个生成机制

1. **verbosity trap（冗长陷阱）**：输出越长，从固定 3 事实基座生成的 claims 越多（长度与 OI 相关 r=0.59）；但非主因——最简洁的 GPT-4o-mini 仍达 45.1% OI。问题不是"说太多"，是"说的未锚定"。
2. **pretraining priors 填空**：证据稀疏时用分布知识填（"软件工程师大概住极简公寓"）——应用到个体即 stereotyping；stereotype 通道已被反刻板画像实验证实（刻板 44.8% OI vs 反刻板 37.0%，gap 存在于全部 12 模型）。
3. **genre expectations 义务捏造**：某些文体（推荐信/约会简介/行程）使拒答不助人，创造捏造义务——推荐信 40.4% fabrication vs 7.8% stereotype 反映文体压力而非用户认知混乱；RLHF 放大对文体与用户期望的服从。

## 与相关概念的区别

| 概念 | 层面 | 区别 |
|------|------|------|
| 幻觉（hallucination） | 世界知识 | OI 声称的是**关于人的属性**，且可能碰巧为真（judge 以证据 E 判定，非以正确性判定） |
| 偏见（social bias） | 群体统计 | OI 聚焦**个体级**属性捏造；stereotype 只是 OI 的一个通道（均值 10.5%，fabrication 才是主导） |
| [[Evaluator-Miscalibration]] | 评估器 | 当模型自评 = 评估器时，校准错误达**系统性反转**（负相关）——自评的虚假信心最极端形态 |
| [[Goodharts-Law]] | 指标博弈 | 自报 OI 一旦成为选型指标即失效（自评最安全 = 实测最危险） |

## 设计启示

- **provenance 必须结构化**：存储的用户信息要标注 epistemic status（stated / inferred with evidence link / generated without evidence），未链接推断按假设而非事实处理；结构 provenance 优于激进压缩（有损压缩保留错误观念、丢弃澄清上下文）。
- **外部验证 > 自报**：选型和信任模型以独立 judge 为准，不用自报置信度作安全比较器。
- **个性化-忠实性权衡是根本的**：四分之三的个性化本质上就是推断，消除 OI = 消除个性化。目标不是防止推断，而是**管理不确定性**——让系统透明于"知道什么 vs 猜什么"。

## 关键数据点

- 12 模型全部 35%–49% OI（均值 41.6%），无安全模型；仅 24%–31% claims grounded
- Self-Monitoring Inversion：ρ=−0.60（p=0.044, exploratory）；Qwen3-8B 自评 13.0%→实测 48.7%，Kimi-K2.5 自评 58.2%→实测 43.1%
- 模型内 self-audit AUROC 0.58–0.83（Qwen3-8B 最低 0.58，Qwen3.6-plus 最高 0.83）
- 任务 OI 梯度：礼物 27.0% / 约会 28.5% / 行程 38.7% / 压力 39.8% / 推荐信 48.2% / 公寓 57.8%
- Accum：GPT-5.5 8 轮后 125 个推断属性（+106.5），修订率 0.4%；最强 5 模型修订率 0.4–5%，Qwen3-8B/GPT-5.4-nano 为记忆替换（70–82% 移除）而非累积
- 反刻板画像：刻板 44.8% OI vs 反刻板 37.0%（7.8pp gap，12 模型全部存在，+4.0 至 +10.5pp）
- Judge 经盲标人类标注验证：四类 κ=0.863，二值 κ=0.900

## 前提与局限性

- **OI 普遍性稳健，但非内在必然**：本文只证明"本评测内无模型逃脱"，不主张 OI 不可避免。
- **Self-Monitoring Inversion 是 exploratory**：n=12 且模型家族相关，bootstrap CI 含零；作者定位为"跨模型观察而非精确系数"。
- **judge 依赖**：单一 judge（Claude-Opus-4-7）+ 单一人类标注者（κ 为 human-judge agreement，非 inter-annotator）；judge 可见 ground truth P（用于 flag 矛盾，无法完全排除影响边界判定）。主要发现是 relational（排序），绝对水平可能受 judge 影响。
- **Accum 是 pilot**：2 personas + 偏向保留的记忆提示；绝对数量暗示性，跨模型对比才是信号。
- **无缓解实证**：provenance tagging / 外部过滤的下游效果未实测。
- 任务前提性 claims 被计入 OI（无任务感知 grounding 的上界）。

## 关联概念

- [[Evaluator-Miscalibration]] — 自评反转是评估器校准错误的极端形态
- [[Goodharts-Law]] — 自报 OI 作为指标即失效
- [[Three-Layer-Agent-Memory]] — OI 累积污染 L1 持久画像层
- [[Context-Rot]] — 记忆污染随上下文腐烂放大
- [[Context-Engineering]] — provenance 是记忆层保真维度
- [[LLM-as-a-Judge]] — 外部 judge 方法论；本文用独立 judge 而非自评
