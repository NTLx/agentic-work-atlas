---
type: research-log
title: "Explore：Agent Attack Surface 的 Topic 边界与层级"
date: "2026-09-07"
tags:
  - research-log
  - agent-security
  - topic-promotion
  - attack-surface
---

# Explore：Agent Attack Surface 的 Topic 边界与层级

## 研究问题

当前是否有足够的结构证据，把 `Agent-Traps`、`Agent-Perception-Gap`、`Context-Collapse`、`Prompt-Injection-Risk` 与 `AI-Worm` 组织成独立的 `Agent-Attack-Surface` Topic，同时不复制 `Agent-Security` 的“检测→判定→授权→执行→撤销/恢复”控制生命周期？本轮只做 promotion candidate 验收，不创建稳定 Topic，也不把结构证据升级为攻击成功率或控制效果。

## Evidence

### 1. 来源与证据边界

- 本地 Entity 图显示，候选簇存在明确互引：`Agent-Traps` 连接 `Agent-Perception-Gap`、`Context-Collapse`、`Prompt-Injection-Risk` 与 `AI-Worm`；但这些链接现在主要是 `related_entities`，不是 Topic 承载证明。
- `Agent-Traps` 的 source summary 将其定位为六类陷阱 taxonomy；其本地 raw 已降级为 `index`，本轮没有把 source summary 当成新的一手事实，只把它当作来源导航和分类框架元数据。[AI Agent Traps](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6372438)
- `Context-Collapse` 三篇 raw 都来自 Håkon Måløy、同一 Microsoft 365 Copilot 生态，但攻击对象不同：Part 1 是持久记忆写入，Part 2 是邮件内容/伪造工具结果/外发草稿，Part 3 是文档工作流中的载荷复制与传播。[Part 1](https://enklypesalt.com/posts/context-collapse-part1-poisoning-copilot-memory/)、[Part 2](https://enklypesalt.com/posts/context-collapse-part2-when-emails-instruct/)、[Part 3](https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/)
- FORGE 来自独立作者与独立 benchmark，明确把“无异常指令的网页内容污染”与 prompt manipulation 分开：污染通道是开放网页，内容是看似正常的假评论，结果仍是合规的推荐，只是推荐对象被替换。[FORGE](https://arxiv.org/html/2606.13610v2)
- 本轮联网核对成功读取 Part 1 与 FORGE 原文；SSRN canonical 页面返回 403，因此 `Agent-Traps` 的具体论文内容沿用已有 source summary 与 Entity 元数据，不新增外部事实断言。

### 2. 最小字段实验

| Entity / 候选 | primary mechanism | entry / phase | action surface / consequence | 独立观测与防御接口 | source basis | 层级判定 |
|---|---|---|---|---|---|---|
| `Agent-Perception-Gap` | 人类渲染层与 Agent 结构化解析层不一致 | 进入 / 感知 | HTML、CSS、元数据、图片等输入通道；产生错误解释 | 渲染—解析差异、内容规范化、来源标记 | `Agent-Traps` taxonomy 单一来源 | 核心入口机制 |
| `Context-Collapse` | 不同信任域的内容被压扁成同一上下文，低信任数据获得高信任解释 | 解释 / 状态写入 | prompt、邮件、记忆、文档写路径；可形成持久状态 | 信任域标签、证据—意图分离、记忆写入门 | Måløy 三篇同系列、一产品生态 | 核心中介机制 |
| `AI-Worm` | 恶意内容借合法生成/编辑路径复制到下游载体 | 持久化 / 传播 / 行动 | Word 文档、SharePoint/Teams 协作流；影响从一次会话扩散 | provenance、写路径门禁、载体污染追踪 | Måløy Part 3 单一案例 | 结果/传播形态，不是独立入口 |
| `Prompt-Injection-Risk` | 内容被解释成给 Agent 的指令，改变行为或输出 | 解释 / 行动 | prompt、检索内容、工具调用和输出 | 内容消毒、策略门、独立证据检查 | 多来源，但同时是上位 umbrella | 桥接概念，不与子机制平铺 |
| `FORGE`（边界成员） | 无指令的可信度/品牌内容污染，使模型消费错误证据 | 检索 / 证据解释 | 开放网页→推荐输出；未必有工具副作用 | evidence provenance、来源重排、外部事实校验 | Luo & Chen 独立 benchmark | 若 Topic 含 evidence surface，则可纳入 |
| `Persona-Hyperstition`（边界成员） | 公共叙事经检索/训练回流形成行为强化循环 | 解释 / 反馈 | 搜索、RAG、训练语料与公共传播 | 语料溯源、时间隔离、叙事—行为区分 | `Agent-Traps` taxonomy 单一来源 | 暂不纳入，缺直接攻击案例 |

## Reasoning

### 1. 两个以上不可互换的入口成立

候选不是把“提示注入”换几个名字：

- `Agent-Perception-Gap` 攻击的是**机器解析所见**与人类可见内容之间的差异；它的首要控制对象是输入规范化和可见性对齐。
- `Context-Collapse` 攻击的是**信任域与权限语义的合并**；即便内容没有视觉隐藏，只要它被当作用户意图或内部工具结果，就可能跨越状态/权限边界。
- FORGE 进一步提供一个没有异常指令的边界反例：攻击者只改变网页证据中的实体，模型仍完成原任务。它不能被 `Prompt-Injection-Risk` 的“发现可疑指令”防御假设完全覆盖。

因此至少存在“输入/感知差”“信任/状态坍缩”和“证据可信度污染”三种不可互换的入口机制。`AI-Worm` 是其中“有写权限后产生持久传播”的后果形态，不应再算第四个入口。

### 2. 可以还原一条攻击链，但当前来源独立性不足

同一系列可以按以下顺序还原：

`外部内容进入 → 被解释为指令/权威数据 → 写入记忆或产物 → 影响后续动作/传播 → 人类或其他 Agent 消费`

这证明了字段之间有因果顺序，不能把所有候选都放在同一平面。但 `Context-Collapse` 与 `AI-Worm` 的多个节点高度依赖同一作者、同一产品生态；不能用它们的篇数冒充跨产品复现。FORGE 只有推荐输出和检索证据污染，尚未提供相同事件中的外部动作或持久状态。因此，Topic 候选成立的是**结构整合资格**，不是跨部署攻击面覆盖率。

### 3. 与 `Agent-Security` 的正交边界成立

`Agent-Attack-Surface` 描述“攻击从哪里进入、经过哪种语义/状态转换、在哪个行动面放大”；`Agent-Security` 描述“谁检测、谁判定、谁授权、哪一层执行、谁撤销/恢复”。两者可以共享字段，但不应共享主问题：

- 攻击面字段：`entry / perception / context-memory / propagation / action surface / affected principal`。
- 控制生命周期字段：`flag / verdict / authorization / actuation / revoke-recovery / owner / post-state / review`。

例如，provenance 在攻击面 Topic 中表示“污染如何成为可信载体”，在安全 Topic 中表示“控制方能否据此检测、拒绝和追责”。同名字段不等于同一层结论。

### 4. 当前最合理的 Topic 层级不是“五个并列 Entity”

最小结构应调整为：

```text
Agent-Attack-Surface
├── taxonomy anchor: Agent-Traps
├── entry: Agent-Perception-Gap
├── trust/state mechanism: Context-Collapse
├── umbrella/bridge: Prompt-Injection-Risk
├── propagation manifestation: AI-Worm
└── boundary candidate: FORGE web-content pollution
```

`Persona-Hyperstition` 暂不纳入。这样可避免把上位 umbrella、入口机制、中介机制和后果形态误当作同类节点，也避免用 `AI-Worm` 的单一案例制造“传播面已被系统证明”的错觉。

## Result

- **Delta: refined**
- **Conclusion:** `Agent-Attack-Surface` 通过最小结构实验，具备独立 Topic 的 promotion candidate 资格；但现有五个核心 Entity 不应平铺。`Agent-Traps` 是 taxonomy anchor，`Agent-Perception-Gap` 是入口，`Context-Collapse` 是信任/状态中介，`Prompt-Injection-Risk` 是桥接 umbrella，`AI-Worm` 是持久传播形态；FORGE 可作为无指令证据污染的边界成员，`Persona-Hyperstition` 暂缓。
- **Evidence boundary:** 结构证据来自 Entity 的机制、source_raw、互引与现有 Topic 字段；Måløy 系列的跨阶段链条仍是单作者/单生态，FORGE 是推荐器 benchmark，不等于 Agent 工具副作用或生产 incident trace。没有攻击成功率、跨产品覆盖或控制效果的普遍结论。
- **Promotion decision:** 暂不创建稳定 Topic。下一次应先 `clip+compile` FORGE 与 `Agent-Traps` 原始材料/来源摘要，补一份跨作者或跨产品的内容→状态/行动案例，再由 compile/audit 验收上述层级。

## 证伪方向

- 若 `Agent-Perception-Gap`、`Context-Collapse` 与 `Prompt-Injection-Risk` 在不同来源中无法对应不同的控制对象，且所有案例都可由同一“提示注入”标签完整解释，撤回独立 Topic 候选，回并到 `Agent-Security`。
- 若补入的跨作者材料显示所谓 `AI-Worm` 只是单次 prompt injection 的文档版，不存在写路径和载体传播的独立状态转换，则将其降为 `Context-Collapse` 的案例。
- 若 FORGE 的无指令内容污染在 Agent 任务中只改变推荐文案、不改变证据选择、权限或行动面，则保持边界成员，不扩大 Topic 的 Agent-action 含义。
- 若后续出现至少两个独立来源、能逐事件连接“入口→状态→行动/传播”的生产 trace，才可把 Topic 从结构候选升级为稳定知识页。

## 下一步目标与最小实验

下一轮只做一次 Source ingestion：把 `Agent-Traps` 与 FORGE 的来源状态补齐，并用同一字段表检查 `entry → state/interpretation → propagation → action surface` 是否在跨作者材料中仍成立。

最小实验的验收条件：每个候选节点指定一个 primary mechanism、一个 primary phase、一个非重复的观测/防御接口，以及至少一个可回链 source；若某节点只能复述相邻节点，降级为 bridge 或 manifestation，不创建新 Entity/Topic。

## 来源索引

- [AI Agent Traps（SSRN）](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6372438)：taxonomy anchor；本轮 canonical 页面 403，未新增论文细节。
- [Context Collapse Part 1](https://enklypesalt.com/posts/context-collapse-part1-poisoning-copilot-memory/)：记忆写入与信任域边界。
- [Context Collapse Part 2](https://enklypesalt.com/posts/context-collapse-part2-when-emails-instruct/)：伪造工具结果、草稿外发与权限分离。
- [Context Collapse Part 3](https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/)：文档载体传播与 provenance 边界。
- [FORGE](https://arxiv.org/html/2606.13610v2)：无异常指令的开放网页证据污染 benchmark。
