---
type: entity
title: Model Introspection
aliases:
  - Model Introspection
  - 模型自省
definition: "让模型生成对自身错误或行为的解释，用于提出调试假设与归纳行为模式；其自述不等同于对真实内部机制的直接读取"
created: 2026-05-08
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - AI
related_entities:
  - "[[Cat-Wu]]"
  - "[[Jagged-Intelligence]]"
  - "[[AI-Psychosis]]"
  - "[[Product-Overhang]]"
  - "[[Research-Preview]]"
  - "[[Competent-Output]]"
  - "[[Mechanistic-Interpretability]]"
source_raw:
  - "[[How Anthropic’s product team moves faster than anyone else - Cat Wu (Head of Product, Claude Code)]]"
  - "[[Anthropic's Boris Cherny: Why Coding Is Solved, and What Comes Next]]"
  - "[[20260617-huggingface-agentic-resource-discovery]]"
  - "[[20260730-lenny-anthropic-first-technical-pm-dianne-penn]]"
  - "[[20261018-lenny-emmanuel-ameisen-interpretability]]"
---

# Model Introspection（模型自省）

> [!definition] 定义
> **Model Introspection（模型自省）** 是一种 AI 使用技能：当模型犯错时，不只修复错误，而是追问模型“分析你刚才为什么犯这个错”。这类自述可用于提出调试假设、归纳失败模式和补充评测集，但它仍是模型生成的解释，**不能视为对真实内部计算的直接访问**。

## 关键数据点

- **Cat 的实际用法**：经常让 Claude "分析你刚犯的错误，告诉我你为什么会犯"——将此视为 debugging workflow 的标准步骤
- **洞察深度**：模型自述可以提出关于系统性偏差的假设；不能由自述频率或细节推定真实机制。
- **与其他 debugging 方法的关系**：模型可交互提出新假设，但没有本页证据证明它比其他 debugging 方法更有效。
- **隐性知识提取**：自述可提示待检验行为，不足以识别训练数据分布或 RL 因果机制；微调候选需独立验收。

## 前提与局限性

- 不能仅由语言生成机制断言模型完全没有自省能力，也不能由自述证明具有可靠元认知。控制内部激活的实验与日常自然语言自述是不同证据
- 模型对错误原因的解释可能是幻觉——"我是因为 X 犯的错"可能只是听起来合理，实际上真正原因是完全不同的模式偏差
- 过度依赖自省可能产生"自我强化偏差"——模型在自省中发现的模式可能进一步固化其偏见
- 区分真正有用的自省和 post-hoc rationalization 需要人类 [[Judgment|判断力]]

## 作为产品研究方法的模型自省

Cat Wu 在 Anthropic 产品团队将模型自省从 debugging 技巧升级为产品研究方法。其逻辑是：模型解释可产生待复现的失败假设，只有跨样本对照才能确认系统性行为。

这对产品团队有三层价值：

1. **能力边界测绘**：模型的自述可提出失败条件候选，经外部测试后用于绘制 [[Product-Overhang|产品能力溢出]] 的边界。
2. **发布决策支撑**：不能以模型自述质量决定可发布性；[[Research-Preview|Research Preview]] 仍需基于实际功能、风险、失败模式与退出能力验收。
3. **评测集补充**：模型自省揭示的失败模式可以被转化为新的评测用例，补充到 [[Evaluation-Set|评测集]] 中，形成"自省 → 评测 → 训练 → 自省"的闭环。

Dianne Penn（Anthropic Head of Product, AI Research & Labs，2026-07）补充了第四层——**用户反馈归因**：PM 团队读失败对话 transcripts，把模糊抱怨（"Claude hallucinated"）分解为可行动的失败分类：该调用 tool 时没调用（tool use 失败）/ 检索了正确文档但取错事实（search synthesis 失败）/ 对齐问题。这一归因过程缩短了"用户反馈 → 研究者可行动项"的距离，是 evals-as-PRD 工作流（[[Evals-as-PRD]]）的前置步骤。⚠️ 与 Palantir 可解释性文的张力：自省揭示的是 harness 层错误（prompt 误导、编排失败），不保证揭示模型内部真实原因——自省用于修 harness，[[Transparent-Tool-Handoff|工具层检查]]用于修任务执行，两者互补。

## 与 Mechanistic Interpretability 的边界（2026-10）

2026-11-28 外部复核：[Anthropic concept injection 研究](https://www.anthropic.com/research/introspection) 在特定激活注入实验中发现有限内部状态识别能力，Opus 4.1 最佳实验协议约20%成功；其余常有漏检或混淆，非一般调试准确率。[CoT faithfulness 研究](https://www.anthropic.com/research/reasoning-models-dont-say-think) 在特定选择题提示与训练设置中也观察到解释遗漏关键信息。两项研究不支持自省一概无效，也不支持自述为真实因果链。激活干预、行为对照和日常自述应分开；新来源仅作本次旧论断的反证校准，正式剪藏仍按晋升门。

Emmanuel Ameisen 对 Anthropic interpretability 工作的说明给本实体增加了一条必须长期保留的证据边界：**模型自省和机制可解释性不是同一种证据。**

[[Mechanistic-Interpretability|Mechanistic Interpretability]] 直接记录模型的 intermediate activations，寻找稳定 representation / circuit 候选，并可通过修改内部激活验证行为是否按预测变化；Model Introspection 则让模型用自然语言解释自己为什么这么做。

~~~text
Model Introspection
= generated self-explanation
→ cheap hypothesis / debugging signal

Mechanistic Interpretability
= internal measurement + intervention
→ mechanism evidence
~~~

**判断**：Model Introspection 的合理定位是 **hypothesis generator**，而不是 ground truth debugger。自省可以告诉我们“接下来值得检查什么”，但不能单独证明“内部真正发生了什么”。

- **证据**：[[20261018-lenny-emmanuel-ameisen-interpretability]]；访谈明确区分可 verbalize 的输出与只存在于 intermediate states 中的内部表征，并说明 interpretability 通过测量与干预这些状态建立解释。
- **边界**：Mechanistic Interpretability 本身也不完整；两者都不能单独替代外部行为验证、可执行 oracle 或真实环境证据。

这进一步收紧了本页既有的 `自省 → 评测 → 训练` 工作流：自省发现的 failure hypothesis 应进入 eval / trace / tool evidence / mechanistic study 中验证，而不是直接升级为原因结论。

## 与人类 debugging 的结构对比

| 维度 | Rubber Duck Debugging | Model Introspection |
|------|----------------------|---------------------|
| 对话对象 | 无响应的物体 | 犯了错的实体 |
| 信息来源 | 人类自己的推理 | 模型生成的解释（非直接内部链路） |
| 洞察深度 | 提出假设 | 提出补充假设，机制仍需验证 |
| 风险 | 人类确认偏差、遗漏 | 后验合理化、误导与确认偏差 |

传统 debugging 的核心瓶颈是人类看不到模型内部的决策路径。模型自省的价值不是"模型知道自己为什么错"（它可能不知道），而是"模型的解释能揭示人类看不到的模式"——即使解释本身不完全准确，它指向的方向仍然有价值。

## 关联概念

- [[Jagged-Intelligence]] — 模型自省揭示了锯齿状的内部结构。
- [[Taste]] — 判断模型自省的质量需要品味——区分真洞察和合理美化。
- [[Judgment]] — 辨别模型自省中的信号与噪音。
- [[Product-Overhang]] — 模型自省帮助产品团队发现模型已具备但尚未产品化的能力。
- [[Competent-Output]] — 自省只能作为判断输出是否合格的辅助信号，仍需外部证据验证。
- [[Mechanistic-Interpretability]] — 直接研究内部 activation / representation / circuit，与自然语言自省属于不同证据层。
