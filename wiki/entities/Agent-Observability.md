---
type: entity
title: Agent-Observability
aliases:
  - Agent 可观测性
  - AI Agent Observability
definition: "Agent Observability = 有穷观察者（人类/制度）在开放行为空间中校准对 AI Agent 行为预期的持续能力——不等同于传统 APM observability，因为观察者耦合在被观测系统中且跨越信任域边界。"
created: 2026-07-15
updated: 2026-07-15
tags:
  - agentic-engineering
  - observability
  - verification
  - security
related_entities:
  - "[[Agentic-Engineering]]"
  - "[[Agent-Harness]]"
  - "[[Verifiable-Agent-Engineering]]"
  - "[[Distinct-Principal-Identity]]"
  - "[[Human-Governor-Agent-Operator]]"
  - "[[Judgment]]"
topics:
  - "[[Agent-Security]]"
  - "[[Context-Engineering]]"
source_raw:
  - "[[2026-07-15]]"
---

# Agent Observability（Agent 可观测性）

> 有穷者观测有穷者在开放行为空间中——"理解"不是消除有穷性，是在有穷性约束下最大化行动校准度。

## 定义层：Observability 的三重关系

Agent Observability 不同于传统 APM observability，因为后者假设观察者在系统**外部**、观测**自己的**系统、且系统行为空间**封闭**（请求-响应树的静态拓扑）。Agent 打破所有三个前提：

| 维度 | 传统 APM Observability | Agent Observability |
|------|----------------------|-------------------|
| 观察者位置 | 外部（SRE 观测服务） | 耦合（观察者与 Agent 在同一个系统中协同演化） |
| 信任域 | 单一信任域（同一组织） | 跨信任域（开发者 ≠ 使用者 ≠ 被影响者 ≠ 监管者） |
| 行为空间 | 封闭（已知调用拓扑） | 开放（动态因果图，运行时构造） |
| 失败模式 | 已知（HTTP 错误码、超时） | 涌现（新失败类型持续出现） |
| 观测界面受众 | 同质（SRE/DevOps） | 异质（终端用户/开发者/审计者/监管者） |

## 结构层：五重"理解"

Agent Observability 的"understand"阶段天然分裂为五种不可互相还原的含义，对应观察者-系统的五种耦合模式：

| 含义 | 提出者 | 目标函数 | 度量 | 硬墙 |
|------|--------|---------|------|------|
| **压缩** | Chaitin | 找到比原始数据更短的程序 | Kolmogorov 复杂度 K(D) | `K(D) ≈ \|D\|` 时不可压缩 |
| **校准预期** | Woods | 比随机更好地做出行动决策 | 决策准确率 | Ashby 必需多样性定律 |
| **持续循环** | Majors | 压缩"观测→假设→验证→修正"周期 | 反馈延迟 | 反馈周期 > 故障演化速度 |
| **制度化** | Schneier | 固化观测实践为可审计规则 | 合规覆盖率 | 规则固化速度 < 行为演化速度 |
| **可争议性** | O'Neil | 让被决策影响者能挑战决策 | 申诉成功率 | 观测权不对称 |

**统一根底**：五重含义共享同一个底层约束——**有穷性**。压缩硬墙（Kolmogorov）和校准硬墙（Ashby 必需多样性定律）是同一条墙的描述侧和控制侧。Agent 在开放世界中 → 校准域更适用；但压缩域在可压缩子空间仍然有效。两者的边界是数学上的：可压缩区 vs 不可压缩区。

相关追本分析见 [[20260715T140405--追本-理解的分裂-压缩与校准之间__think]]。

## 工程层：三个核心差异

### 1. Agent trace ≠ 微服务 trace

- 微服务 trace = 静态调用**树**（span 父子关系在编译时已知）
- Agent trace = 动态因果**图**（调用路径由推理链在运行时决定，因果关系事后才可标记）
- 数据模型需捕获推理意图（"agent 为什么选这个工具"），不只是调用事实（"agent 调用了哪个工具"）

### 2. 不可压缩性统一上限

当 Agent 行为轨迹的 Kolmogorov 复杂度 K(D) 接近轨迹长度 |D| 时，所有观测层级共享统一的保真度上限。多层级观测 = 对不可压缩数据的选择性投影集合，非压缩。聚合/采样/摘要 = 信息损失。

### 3. 多层级观测界面

同一底层 trace 数据需支持三类界面：
- **终端用户**：自然语言解释（"Agent 为什么做这个决策？"）
- **开发者**：工具调用链 + 延迟 + Token 消耗 + 推理链
- **审计者**：数据流追踪 + 权限使用 + 终止条件 + 合规检查

## 制度层：最小可行制度（MVI）

`MVI = HardFloor ∪ MetaRules`

**硬地板**（无此不可）：工具调用记录 + 数据流追踪 + 终止条件 + 不可篡改审计日志 + 独立审计权 + 保留人类责任归属。

**演化框架**（元规则）：规则修正机制 + 失败模式知识库 + 跨平台互操作标准 + 可争议性机制。

理由：制度本身 = 有限公理系统（有穷者治理悖论）。面对无限行为空间，必然存在不可判定行为。元规则（如何修改规则）比固定规则本身更重要。

## 标准化现状（联网验证，2026-07-15）

- **OpenTelemetry GenAI 语义约定 v1.41.1**（2026-05-11）：五个 Agent span 操作（`create_agent`/`invoke_agent_client`/`invoke_agent_internal`/`invoke_workflow`/`execute_tool`），状态 `Development`
- **ATSC v0.1.0**（Agent Telemetry Semantic Conventions，2026-03-12）：21 种 span kind + 40+ span event + 14 domain objects + 三级合规模型（Core/Standard/Full）。Apache 2.0 许可证。面向 LangGraph、Microsoft Agent Framework、AutoGen、Semantic Kernel
- **OTel SIG End User Blueprint #330**（2026-07-01 关闭）：AI-Native Observability——参考实现 KrystalineX 直接用 OTel-backed MCP server 处理跨信任域 Agent observability
- **厂商整合**：ClickHouse 收购 Langfuse（2026-01）、Cisco 收购 Galileo（2026-05）。OTel 成为行业唯一中性 wire format。

联网 source：
- OTel GenAI Agent Spans: <https://genalphai.com/agent-observability-with-opentelemetry-genai-conventions/>
- ATSC SPEC: <https://github.com/agent-telemetry-spec/atsc/blob/main/SPEC.md>
- OTel Blueprint #330: <https://github.com/open-telemetry/sig-end-user/issues/330>
- OTel AI Agent Observability blog: <https://opentelemetry.io/blog/2025/ai-agent-observability/>

## 与已有框架的连接

- **Agent 测试不可能性（Rice 定理）**：观测与测试共享同一条形式限制——有限观察者无法完全判定开放系统中 agent 行为的全部有意义的属性。观测与测试是对偶问题（测试判"对/错"，观测判"在发生什么"——两者都需要在无限空间中做有限判断）。
- **Agent 信任边界 V×C×A**：Observability = V（可见性）的工程化实现。没有 Observability → Visibility = 0 → 信任边界崩溃。
- **有穷者治理悖论**：制度本身是有穷的规则系统 → MVI 必须包含元规则而非仅固定规则。
- **信息-时间不对称**：观测的意义分配是事后性的——在事件当下无法知道哪些数据最终成为"关键证据"。观测永远滞后于行为。
- **Loop Engineering**：外部终止者需要 observability 作为输入——无法观测就无法终止。

## 关键数据点

- **OTel GenAI v1.41.1**（2026-05-11）：5 个 Agent span 操作，状态 Development
- **ATSC v0.1.0**（2026-03-12）：21 种 span kind，40+ span event，14 domain objects，3 级合规模型
- **OTel SIG Blueprint #330**（2026-07-01 关闭）：跨信任域 Agent observability 参考实现 KrystalineX
- **厂商整合**：ClickHouse 收购 Langfuse（2026-01），Cisco 收购 Galileo（2026-05）
- **OTel GenAI 约定**：`gen_ai.provider.name`（v1.37 改名自 `gen_ai.system`）+ `gen_ai.usage.reasoning.output_tokens`（v1.41.0 新增）

## 前提与局限性

- **理论前提**：Chaitin 不可压缩性 + Ashby 必需多样性定律 + 有穷者治理悖论——三者共同定义 Agent observability 的形式上限
- **经验前提**：Agent 行为轨迹的 Kolmogorov 复杂度是否确实接近轨迹长度——尚未被经验验证（理论推导，待实证）
- **制度前提**：MVI 框架假设跨信任域场景——在单一组织内部的简单 Agent 部署中，标准 APM + content filter 可能已足够
- **标准化风险**：OTel GenAI 约定仍为 Development 状态，span 名称仍可能变化；ATSC 为单人维护草案，采纳路径不确定
- **覆盖盲区**：类人交互（human-in-the-loop）的观测、多 Agent 协商的涌现行为观测——ATSC 已定义部分 span kind，但实际工具覆盖尚不完整

## 关联概念

- **Agent 测试不可能性（Rice 定理）**：观测与测试的形式限制同构——都是有限观察者面对开放行为空间的不可判定性问题
- **Agent 信任边界 V×C×A**：Observability = V 的工程化实现。V=0 → 信任边界无基础
- **有穷者治理悖论**：制度=有限公理系统→MVI 需要元规则而非固定规则
- **信息-时间不对称**：观测意义的分配是事后性的，观测永远滞后于行为
- **Loop Engineering**：外部终止者依赖 observability 作为输入信号
- **SPIFFE/Agent Identity**：观测系统本身的身份认证——谁有权观测、谁有权解释观测数据
- **APM 演化史**：Agent observability 继承 APM 技术栈（高基数事件/即席查询/分布式追踪）但面对全新的制度层和伦理层问题

## 开放问题

1. 不可压缩性的经验测量——Agent 行为轨迹的 Kolmogorov 复杂度如何实际估计？
2. 跨信任域 observability 的密码学基础——零知识证明能否让 Agent 证明合规而不暴露完整行为轨迹？
3. Agent 失败模式知识库（类比航空 NTSB）——建立机制、格式标准、跨平台共享
4. OTel GenAI 语义约定从 Development → Stable 的时间线和演化方向
5. MVI 框架与 ATSC 三级合规模型的精确映射

## 相关 QA

详细 Q-A 链见 [[20260715T140612--qa-Agent-Observability根本限制__qa]]（5 Q-A 对，覆盖 trace 模型差异 / 五重理解不可还原性 / APM 类比断裂 / 不可压缩性上限 / MVI 双组件定理）。
