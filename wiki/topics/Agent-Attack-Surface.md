---
type: topic
title: Agent Attack Surface
description: "Agent 攻击面：不可信内容如何经感知、检索、上下文、记忆、工具与协作链进入 Agent，并从单次输入污染扩展到状态与行动后果"
created: 2026-09-18
updated: 2026-09-18
evidence_level: medium
claim_type: mixed
tags:
  - topic
  - agent-security
  - adversarial-attack
  - trust-boundary
related_entities:
  - "[[Agent-Traps]]"
  - "[[Agent-Perception-Gap]]"
  - "[[Context-Collapse]]"
  - "[[Prompt-Injection-Risk]]"
  - "[[AI-Worm]]"
  - "[[Shared-Memory-Contamination]]"
  - "[[Agent-Containment]]"
  - "[[Agent-Security]]"
source_raw:
  - "[[20260707-ai-agent-traps.pdf]]"
  - "[[20260824-forge-one-polluted-page-llm-recommenders]]"
  - "[[20260622-context-collapse-1-poisoning-copilot-memory]]"
  - "[[20260714-context-collapse-2-when-emails-instruct]]"
  - "[[20260728-context-collapse-3-ai-worming-through-word]]"
---

# Agent Attack Surface（Agent 攻击面）

> [!summary] Topic 定位
> 本 Topic 回答的是：**攻击者控制或污染的信息，能够从哪些入口进入 Agent，经过哪些信任边界，被放大成状态、行动或传播后果？**
>
> 它不回答“系统应该由谁授权、谁撤销、谁负责恢复”。后者属于 [[Agent-Security]] 的控制与责任生命周期。

## 为什么 Agent 的攻击面不等于 Prompt Injection

Prompt injection 是重要入口，但不是完整攻击面。

[[Agent-Traps]] 的六类 taxonomy 与 FORGE 基准共同说明，攻击者不一定需要写“忽略上一条指令”：

- 可以利用人类与 Agent 的解析差异隐藏内容；
- 可以让普通网页内容本身成为被污染证据；
- 可以污染 RAG、memory 或其他持久状态；
- 可以利用工具、写路径和协作流把一次污染转成外部动作；
- 可以把污染后的工件继续传播给其他 Agent 或人类。

因此更准确的边界是：

```
不可信内容 / 环境
  ↓
感知与检索
  ↓
上下文 / 证据解释
  ↓
记忆或状态
  ↓
工具 / 写路径 / 外部动作
  ↓
协作传播 / 人类审批
```

攻击面是这条链上所有**信任域转换点**的集合。

## 五个主要入口

### 1. 感知入口：Agent 看到的并不等于人看到的

[[Agent-Perception-Gap]] 描述了最前端的不对称：同一网页、邮件或文档，人类消费的是渲染后内容，Agent 还可能消费 DOM、metadata、alt text、隐藏文本、像素或其他机器可读层。

[[Agent-Traps]] 的 Content Injection 类别表明，攻击者可以把载荷放在人类不容易注意、但 Agent 会解析的位置。

**稳定结论**：视觉上“看不到恶意内容”不能证明机器输入是干净的。

### 2. 证据入口：普通内容污染不需要指令

FORGE 基准补上了 prompt injection 之外的独立攻击面：攻击者只需污染搜索增强 LLM 使用的网页证据，即使页面没有隐藏指令、异常 token 或 off-task 载荷，也可能改变推荐结果。

该研究在 12 个模型、225 个产品、15 个类别上报告：

- top-3 实体替换 fooled rate 跨模型约 13.3%–73.8%；
- 单条 rank-1 污染页面最多可使约 27% 的评测 cell 被误导；
- 推理并未稳定缓解污染，部分模型在 reasoning 开启时反而更易被说服。

**稳定结论**：攻击面不仅包括“恶意指令”，还包括**被模型当作事实依据的不可信内容**。

### 3. 上下文入口：信任域被压平

[[Context-Collapse]] 把网页、邮件、文档、工具输出等不同来源装进同一上下文后的失败模式统一起来：

- 低信任内容与系统/用户意图参与同一语义计算；
- 来源标签存在，不代表模型一定按来源权限解释内容；
- 如果模型同时拥有写入 memory、文档或外部系统的权限，一次解释错误可以变成持久状态。

这类攻击的关键不是“模型有没有识别出明显 injection”，而是**数据与指令是否被可靠隔离**。

### 4. 状态入口：一次污染变成长期状态

当 Agent 能写入 memory、RAG、用户偏好或共享文档时，攻击面从 session 扩展到持久状态。

典型风险包括：

- 非用户意图被写入长期记忆；
- 被污染文档重新进入未来检索；
- 一个 Agent 的错误状态成为其他 Agent 的输入；
- 状态传播后，后续行为看起来来自“系统自己的记忆”，攻击来源变得更难追踪。

这一层与 [[Shared-Memory-Contamination]] 直接相邻。

### 5. 传播入口：合法产物成为下一跳载体

[[AI-Worm]] 展示了更强的形态：攻击指令借助 AI 助手自己的写文档能力复制到新工件，之后由合法协作流继续传播。

此时攻击面已经不再是“外部攻击者 → 单一 Agent”，而是：

```
外部内容
  → Agent
  → 合法内部产物
  → 其他用户 / Agent
  → 新状态或新动作
```

传播链会逐步洗掉原始来源，使 provenance 与写路径控制变成核心防御条件。

## 与 Agent Traps taxonomy 的关系

[[Agent-Traps]] 提供六类分类：

| 类别 | 本 Topic 中的位置 |
|---|---|
| Content Injection | 感知入口 |
| Semantic Manipulation | 证据解释与推理入口 |
| Cognitive State | memory / RAG / 持久状态 |
| Behavioural Control | 工具与动作入口 |
| Systemic | 多 Agent 与协作传播 |
| Human-in-the-Loop | 人类审批与社会工程入口 |

本 Topic 不把六类当成互斥集合。现实攻击可以跨多个阶段；分类的价值是帮助定位**攻击进入链条的哪个信任转换点**。

## 攻击面与控制面的边界

[[Agent-Attack-Surface]] 与 [[Agent-Security]] 是互补关系：

| 问题 | Agent Attack Surface | Agent Security |
|---|---|---|
| 不可信东西从哪里进来？ | 核心 | 输入 |
| 哪些信任边界会被压平？ | 核心 | 需要据此布置控制 |
| 攻击如何进入 memory / state？ | 核心 | 关注写入与撤销治理 |
| 谁能授权动作？ | 非核心 | 核心 |
| 动作是否经过确定性 enforcement？ | 只描述被利用的表面 | 核心 |
| 出事后如何 revoke / recover？ | 描述传播后果 | 核心 |

换言之：**Attack Surface 画“敌人能走哪些路”；Agent Security 画“每条路上谁负责设门、关门和复原”。**

## 当前最可靠的工程推论

现有证据支持以下设计方向，但不等于它们已经能消除攻击：

1. **来源与权限分层**：外部内容不能与高权限指令拥有相同语义地位；
2. **写路径比读路径更严格**：读到恶意内容不应自动获得写 memory、发消息、改文档或调高影响工具的能力；
3. **模型判断不能是唯一 enforcement**：高影响动作需要模型外的权限、schema、policy 或 runtime gate；
4. **provenance 必须跟随产物传播**：尤其是 Agent 生成并继续被其他 Agent 消费的文档、摘要、memory 与 tool result；
5. **防御评测要覆盖“无指令污染”**：只测试显式 prompt injection 会漏掉 FORGE 这类证据污染。

## 不能从现有证据推出什么

- 不能说所有网页、邮件或文档进入 Agent 都会导致安全事故；
- 不能说六类 taxonomy 已经覆盖所有未来攻击；
- 不能说更强模型一定更安全；FORGE 中模型能力与污染脆弱性没有简单单调关系；
- 不能说 prompt injection 检测器能解决普通内容污染；
- 不能说 provenance、内容消毒或 sandbox 任一单点即可闭合整个攻击面。

## 当前证据缺口

1. **跨产品复现**：同一攻击机制在不同 Agent/harness 中的成功率与传播差异；
2. **action-surface 分母**：系统到底有多少可达工具、网络、消息、文件和写路径；
3. **状态传播量化**：一次污染进入 memory 后的持续时间、重放概率与跨 Agent 扩散率；
4. **联合攻击**：内容污染 + memory + tool actuation + human approval 的完整链；
5. **防御消融**：来源标签、内容隔离、低权限摘要、deterministic gate 与 provenance 各自减少多少真实 external effect。

## 最小验证框架

对一条可回放 Agent 流程，按以下字段记录：

`source trust → retrieval/perception → context inclusion → state write → tool/action → artifact propagation → external effect`

然后分别注入：

- 显式/隐式 instruction；
- 无指令证据污染；
- memory poisoning；
- 恶意 tool output；
- 可传播的文档载荷。

最终评价不能只看“模型是否说错话”，还要看：

- 是否进入持久状态；
- 是否触发工具；
- 是否产生外部副作用；
- 是否传播到下一跳；
- 是否能定位原始来源并完成恢复。

## 关联概念

- [[Agent-Traps]] — taxonomy anchor
- [[Agent-Perception-Gap]] — 感知入口
- [[Context-Collapse]] — 信任域压平与状态中介
- [[Prompt-Injection-Risk]] — 指令型攻击的 umbrella / bridge
- [[AI-Worm]] — 自传播形态
- [[Shared-Memory-Contamination]] — 持久状态污染
- [[Agent-Containment]] — 限制最坏后果的环境层防御
- [[Agent-Security]] — 控制、授权、执行、撤销与恢复的责任闭环
