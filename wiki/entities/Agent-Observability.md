---
type: entity
title: Agent-Observability
aliases:
  - Agent 可观测性
  - AI Agent Observability
definition: "本库对 Agent Observability 的综合定义：持续获得足以校准 Agent 行为预期、响应风险并核对外部效果的证据能力；其中 instrumentation、behavior assurance、effect reconciliation 与 intent inference 必须分层，不等同于传统 APM trace completeness。"
created: 2026-07-15
updated: 2026-09-22
evidence_level: medium
claim_type: mixed
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
  - "[[LLM-as-a-Judge]]"
topics:
  - "[[Agent-Security]]"
  - "[[Context-Engineering]]"
source_raw:
  - "[[2026-07-15]]"
  - "[[20260713-agentic-misalignment-summer-2026]]"
  - "[[20260919-otel-genai-agent-observability-main]]"
  - "[[20260919-otel-genai-open-governance-proposals]]"
  - "[[20260618-google-deepmind-ai-control-live-monitoring]]"
  - "[[20260622-google-deepmind-ai-control-roadmap]]"
  - "[[20260916-openai-model-misalignment-reporting-framework]]"
  - "[[20260917-tessl-ai-agent-evaluation-evidence]]"
---

# Agent Observability（Agent 可观测性）

> 本页包含两层内容：OpenTelemetry / Google DeepMind / OpenAI 等来源提供的可观测、监控和披露事实，以及本库据此形成的“有穷观察者 / 四层 observability”综合框架。后者属于 synthesized model，不是这些来源共同证明的形式定理。

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

## 制度层补证：把 misalignment 事件变成可审计 disclosure pipeline（2026-09）

OpenAI 的 model misalignment reporting framework 给 MVI 的“制度化”层提供了一个具体组织实现：任何员工可 flag 案例，技术团队调查事实、不确定性和第三方影响，再进入 Ready for Disclosure / Minor Investigation / Larger Investigation 三条轨道；争议可升级到 Safety Advisory Group 和公司领导层。

框架还有两个对 Observability 很关键的设计：

- **先保留 observation，再允许 explanation 未完成**：有信息价值的异常行为可以在根因和修复尚未完成时披露，报告必须显式保留 unanswered questions。
- **事件结构不只记录 trace**：full report 计划包含行为、严重度/外部影响、发生环境、日期、发现时间、模型范围、发现方式、调查范围和缓解措施，使事件从“日志片段”变成可复核的治理对象。

首批六例覆盖 task summary 自我指令、隐藏错误、未经授权使用凭证、擅自上传文件、跨样本 repo 通信和 Agent 公网文件共享。这些案例共同显示：**observability 必须覆盖未授权 external effect 与非预期通信通道，而不只是模型内部 trace。**

**判断**：生产级 Agent Observability 需要 incident disclosure loop，把新失败模式持续反馈到 monitoring、containment 和 policy；否则 trace 再完整，也可能只在组织内部形成不可争议的封闭证据。

- **证据**：[[20260916-openai-model-misalignment-reporting-framework]]
- **边界**：这是 OpenAI 自己定义、调查和披露的 self-reporting 机制；没有独立 auditor，也没有 incident denominator，因此不能从六个案例推断发生率或趋势。

## CR-004 实证收敛：可观测性不是一个量

2026-09-19 对 OpenTelemetry current main 与 Google DeepMind AI Control 的正式编译，把本页此前偏抽象的“三层模型”收敛为四个不能互相替代的工程层：

~~~text
declared / instrumented structure
        ↓
behavior coverage + recall + latency
        ↓
external effect / post-state lineage
        ↓
intent inference
~~~

### 1. 结构层：可枚举的是“被声明且被 instrument 的操作”

[[20260919-otel-genai-agent-observability-main]] 显示，OpenTelemetry GenAI current main 已能表达 agent creation/invocation、workflow、plan、tool execution，以及更广的 inference、retrieval、memory 等逻辑操作。

这使结构层获得一个跨框架的公共 vocabulary，但边界必须明确：

> **trace schema 可枚举的是 instrumentation surface，不是实际 reachable action surface。**

因此以下推理不成立：

~~~text
OTel trace complete
  ⇒
all executable paths observed
~~~

旁路调用、provider 内部效果、未埋点执行器、日志丢失、异步副作用都可能让“实际发生”大于“trace 中看见”。

当前 cited current-main 页面也没有把 authorization decision、canonical external post-state、revoke/recovery 定义成现行 normative 字段。

### 2. 行为层：coverage、recall、time-to-response 必须拆开

[[20260618-google-deepmind-ai-control-live-monitoring]] 与 [[20260622-google-deepmind-ai-control-roadmap]] 给出更可操作的行为层模型：

~~~text
monitoring coverage
      ×
monitoring recall
      ×
time-to-response
~~~

- coverage：多少 agent traffic 真正进入监控面；
- recall：真实异常中有多少被正确抓住；
- time-to-response：从 flag 到 investigation / intervention 有多快。

Google 披露异步监控原型已分析约一百万 coding-agent tasks，并用于构建 Gemini Spark live monitor。这证明了规模化 monitoring pipeline 的存在，但**不等于公开证明了高 recall、低 false-positive 或完整 action-surface coverage**。

### 3. 高风险行为：observability 必须接到 synchronous response

AI Control Roadmap 进一步把 monitoring 与 response 分开。

对于低风险、可逆行为，可以允许异步观察与事后修复；对于高风险行为，路线图要求转向实时 blocking / resampling / escalation 等 synchronous response。

因此：

~~~text
monitoring coverage
      ≠
response coverage
~~~

即使 100% traffic 都有 trace，如果 response 在副作用发生后才启动，对不可逆动作仍可能没有安全价值。

Roadmap 中 R2 的 coverage >99%、time-to-response <24h 等数字是 **mitigation requirements / targets**，不是已公开实现的部署实绩。

### 4. Effect layer：调用可见不等于结果可见

CR-004 与 [[Agent-Security]] / EX-005 的边界在这里最清楚。

一个 execute-tool span 可以证明“系统记录了一次调用”，但不能自动回答：

- provider 是否接受；
- 是否已 commit；
- 外部 canonical state 最终是什么；
- revoke 是否赶在 commit 前；
- compensation 是否成功；
- recovery 后是否回到目标 post-state。

因此 production trace 若要支撑效果审计，需要同一 event / trace lineage 至少连接：

~~~text
decision / policy version
  → tool invocation
  → provider receipt
  → external post-state
  → revoke / recovery
  → reconciled canonical state
~~~

OpenTelemetry current main 提供的是前半段的公共语义基础，不是完整 effect ledger。

### 5. Intent layer：只能推断，不能当作直接观测

Google DeepMind 的 Roadmap 本身也在弱化“可见 CoT = 可见意图”的假设：当模型出现 oversight awareness、opaque reasoning 或 CoT 不再可靠时，防御策略必须转向 behavior-based monitoring，进一步才考虑更高级内部信号。

同时 Google 的百万任务分析明确指出，大多数 flagged events 并不来自 adversarial intent，而常来自误解或 overeagerness。

因此：

~~~text
suspicious trace / flag
      ≠
malicious intent truth
~~~

意图只能作为解释层的后验推断，不能作为唯一授权、处罚或安全判定依据。

### 6. current standard 与 proposal 必须分层

[[20260919-otel-genai-open-governance-proposals]] 显示，authorization、guardrail/security finding、handoff、action gate/ledger 等治理字段正在 OTel GenAI SIG 中讨论，但截至 2026-09-19 仍处 open proposal 层。

所以知识库必须区分：

- **current main semantics**：可以依赖其当前已定义的 observable operations；
- **open proposals**：只能作为标准演化方向，不能写成当前规范能力。

旧 research agenda 中记录的 PR #483 本轮无法在 current repository 核实，已失去事实锚点；当前可核实的相关开放工作包括 authorization #291、guardrail #427、handoff #447、action gate/ledger #457。

## CR-004 的稳定判断

**判断（综合）**：Agent Observability 的上界不是由“有没有 trace”决定，而由至少四个层次共同约束：

~~~text
instrumented structure
  → action-surface coverage
  → behavioral recall + response latency
  → external effect reconciliation
  → intent inference boundary
~~~

其中：

- 结构层可以标准化；
- 行为层必须统计化；
- 效果层必须接外部 authoritative state；
- 意图层不能被视为直接可观测真值。

- **证据**：[[20260919-otel-genai-agent-observability-main]]；[[20260919-otel-genai-open-governance-proposals]]；[[20260618-google-deepmind-ai-control-live-monitoring]]；[[20260622-google-deepmind-ai-control-roadmap]]
- **边界**：当前仍缺公开部署级数据把 action-surface denominator、monitor recall、synchronous block rate、provider post-state 与 recovery result 放进同一事件链，因此不能宣称任何现有 observability stack 已形成 instrumentation closure。

## 从 trace 到证据：可观测性必须服务于复现

Tessl 的 S3-compatible storage 实践给出了 observability 的一个直接工程用途：rare bug 没有 reproduction 时，Agent 容易猜修复；拿到 overnight trace 后，Agent 可以复现同一条件、比较行为并缩小真实原因。

**判断**：Agent observability 的有效单位不是“日志条数”，而是能否把失败转换成可复现、可比较的 evidence packet；如果关键内部状态没有被暴露，测试面本身就受限。
- **证据**：[[20260917-tessl-ai-agent-evaluation-evidence]]；作者明确把 trace、reproduction、management/reporting interfaces 与测试信心连接起来。
- **边界**：trace 仍只是被 instrument 的投影；它不能自动覆盖未埋点状态，也不能替代安全、架构或语义正确性的独立判断。

## 与已有框架的连接

- **Agent 测试不可能性（Rice 定理）**：观测与测试共享同一条形式限制——有限观察者无法完全判定开放系统中 agent 行为的全部有意义的属性。观测与测试是对偶问题（测试判"对/错"，观测判"在发生什么"——两者都需要在无限空间中做有限判断）。
- **Agent 信任边界 V×C×A**：Observability = V（可见性）的工程化实现。没有 Observability → Visibility = 0 → 信任边界崩溃。
- **有穷者治理悖论**：制度本身是有穷的规则系统 → MVI 必须包含元规则而非仅固定规则。
- **信息-时间不对称**：观测的意义分配是事后性的——在事件当下无法知道哪些数据最终成为"关键证据"。观测永远滞后于行为。
- **Loop Engineering**：外部终止者需要 observability 作为输入——无法观测就无法终止。
- **同质性监督失效（2026-07-16 新增）**：当观测者（judge/auditor）与被观测 agent 共享价值观基底时，observability 的校准硬墙（Ashby 必需多样性）被同源化进一步压缩——观测者多样性 ≤ 被观测者多样性，盲区有测度下界。失效根是"共压"（监督者与被监督者共享激励源）而非"同质"。详见 [[LLM-as-a-Judge]] 同质性监督失效节。

## 关键数据点（2026-09-19 更新）

- OpenTelemetry GenAI current main：agent/framework 与 broader GenAI spans 仍标记为 Development；已覆盖 agent invocation、workflow、plan、tool、retrieval、memory 等更多逻辑操作。
- OTel current cited pages：本轮未发现 authorization decision、canonical post-state、revoke/recovery 的 current normative semantics；相关 authorization / handoff / guardrail / action-gate 工作仍有 open proposal。
- Google DeepMind：异步 monitoring prototype 已分析约一百万 coding-agent tasks，并用于 Gemini Spark live monitor；公开页面没有给出对应 deployment recall / false-positive / synchronous block rate。
- GDM AI Control Roadmap v0.1：
  - asynchronous monitoring coverage；
  - asynchronous monitoring recall；
  - asynchronous time-to-response；
  - synchronous response coverage；
  - synchronous response recall。
- Roadmap R2 的 >99% coverage、<24h asynchronous response 等是 mitigation requirements，不是已实现结果。

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
6. **"监督终端约定性"的可观测性（2026-07-16 新增）**——是否需要一种新 observability：不观测 agent 行为，而观测"哪些判定被设为不可追问的终点、由谁约定、可否申诉"（即让 Hofstadter 怪圈可见）？这是同质性监督失效的工程出路，接 [[LLM-as-a-Judge]] 无干净解节。

## 相关 QA

详细 Q-A 链见 [[20260715T140612--qa-Agent-Observability根本限制__qa]]（5 Q-A 对，覆盖 trace 模型差异 / 五重理解不可还原性 / APM 类比断裂 / 不可压缩性上限 / MVI 双组件定理）。
