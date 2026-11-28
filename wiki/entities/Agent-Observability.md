---
type: entity
title: Agent-Observability
aliases:
  - Agent 可观测性
  - AI Agent Observability
definition: "本库对 Agent Observability 的综合定义：持续获得足以校准 Agent 行为预期、响应风险并核对外部效果的证据能力；其中 instrumentation、behavior assurance、effect reconciliation 与 intent inference 必须分层，不等同于传统 APM trace completeness。"
created: 2026-07-15
updated: 2026-11-28
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
  - "[[20260922-anthropic-pace-ai-development]]"
---

# Agent Observability（Agent 可观测性）

> 本页包含两层内容：OpenTelemetry / Google DeepMind / OpenAI 等来源提供的可观测、监控和披露事实，以及本库据此形成的“有穷观察者 / 四层 observability”综合框架。后者属于 synthesized model，不是这些来源共同证明的形式定理。

## 定义层：不同的观察对象

Agent 与普通分布式系统均可能动态调用、跨信任域、由观察者反馈改变行为或存在未埋点路径。区别应按实际任务、工具、状态、权限和风险定义，而不是假定传统 APM 静态、封闭或只观测单组织。Agent 常需增加模型/工具、决策输入、权限、外部效果与人工交接的证据关联。

## 结构层：五个观察目的

| 目的 | 例示指标或验收对象 |
|---|---|
| 描述与压缩 | 关键字段保留、压缩误差、存储及查询成本 |
| 校准预期 | 预定义的预测、异常召回与误报 |
| 持续反馈 | 从异常发现到复现、修正及响应的延迟 |
| 制度化 | 记录、权限、版本及审计覆盖 |
| 可争议性 | 纠错、复评、申诉及适用的责任边界 |

这些是本库综合的观察目的，不是五种不可互还原的数学性质或原作者共同提出的模型。Kolmogorov 复杂度涉及无损描述长度，通常不可计算；Ashby 的调节讨论有指定目标、扰动及控制条件，不能与描述复杂度合并为统一保真度上限。工程上按任务测量信息保留、可辨识状态、采样偏差和响应效果；不预设开放域轨迹必不可压缩。

相关历史推演及勘误见 [[20260715T140405--追本-理解的分裂-压缩与校准之间__think]]、[[20260715T140612--qa-Agent-Observability根本限制__qa]] 与 [[2026-08-03]]。

## 工程层：运行时记录、效果与解释

- 传统 APM 与 Agent 均可使用运行时 trace 的父子关系及 links 表达因果线索，不以静态树/动态图区分两者。此前回核 OTel trace data model 的结果见 [[2026-11-28]] 第三十三轮；本轮未重核规范版本。
- Instrumentation 完整性仅针对已定义的记录边界；真实路径覆盖应检查旁路、异步效果、日志丢失与跨服务权威状态。结构、行为、效果与解释是不同验收对象。
- 区分实际调用、输入输出、模型自报理由、外部证据和竞争解释。CoT 与自报意图不直接证明内部因果或恶意；解释可在新证据下修订。
- 终端用户、开发者与审计者按授权访问不同证据视图。保留复现与高风险效果核验需要的信息，同时按隐私、最小读取、保留期和成本控制采集，不一律要求全量或禁止聚合。

## 制度层：按风险确定可观测与响应要求

按任务选择可核验的调用记录、身份与授权、外部状态、停止条件、适用的独立复评和责任分工。关键审计记录应防止未授权修改并支持可追溯纠错，不要求所有日志绝对不可撤销或所有系统外置人工复核。规则修订、事件反馈及争议处理可作为治理机制；不是由形式不可判定性推出的必备四件套。

## 制度层补证：把 misalignment 事件变成可审计 disclosure pipeline（2026-09）

OpenAI 的 model misalignment reporting framework 给 MVI 的“制度化”层提供了一个具体组织实现：任何员工可 flag 案例，技术团队调查事实、不确定性和第三方影响，再进入 Ready for Disclosure / Minor Investigation / Larger Investigation 三条轨道；争议可升级到 Safety Advisory Group 和公司领导层。

框架还有两个对 Observability 很关键的设计：

- **先保留 observation，再允许 explanation 未完成**：有信息价值的异常行为可以在根因和修复尚未完成时披露，报告必须显式保留 unanswered questions。
- **事件结构不只记录 trace**：full report 计划包含行为、严重度/外部影响、发生环境、日期、发现时间、模型范围、发现方式、调查范围和缓解措施，使事件从“日志片段”变成可复核的治理对象。

首批六例覆盖 task summary 自我指令、隐藏错误、未经授权使用凭证、擅自上传文件、跨样本 repo 通信和 Agent 公网文件共享。这些案例共同显示：**observability 必须覆盖未授权 external effect 与非预期通信通道，而不只是模型内部 trace。**

**判断**：适用的事件反馈与复评机制可以将新失败模式反馈到监控、隔离和策略；公开披露与内部反馈范围按影响、义务及隐私确定，不要求所有部署采用同一 disclosure loop。

- **证据**：[[20260916-openai-model-misalignment-reporting-framework]]
- **边界**：这是 OpenAI 自己定义、调查和披露的 self-reporting 机制；没有独立 auditor，也没有 incident denominator，因此不能从六个案例推断发生率或趋势。

## 历史 CR-004 证据综合（现已并入 EX-005）：可观测性不是一个量

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
monitoring recall
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

因此 production trace 若要支撑效果审计，按动作适用性建立同一 event / trace lineage，连接下列证据或等价权威记录：

~~~text
decision / policy version
  → tool invocation
  → provider receipt / equivalent authoritative evidence
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

## 现行 EX-005 中的观测证据边界

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
- 总体行为保障需按适用分母统计，单次行为也可由直接证据判定；
- 效果层必须接外部 authoritative state；
- 意图层不能被视为直接可观测真值。

- **证据**：[[20260919-otel-genai-agent-observability-main]]；[[20260919-otel-genai-open-governance-proposals]]；[[20260618-google-deepmind-ai-control-live-monitoring]]；[[20260622-google-deepmind-ai-control-roadmap]]
- **边界**：当前仍缺公开部署级数据把 action-surface denominator、monitor recall、synchronous block rate、provider post-state 与 recovery result 放进同一事件链，因此不能宣称任何现有 observability stack 已形成 instrumentation closure。

## 从 trace 到证据：可观测性必须服务于复现

Tessl 的 S3-compatible storage 实践给出了 observability 的一个直接工程用途：rare bug 没有 reproduction 时，Agent 容易猜修复；拿到 overnight trace 后，Agent 可以复现同一条件、比较行为并缩小真实原因。

**判断**：Agent observability 的有效单位不是“日志条数”，而是能否把失败转换成可复现、可比较的 evidence packet；如果关键内部状态没有被暴露，测试面本身就受限。
- **证据**：[[20260917-tessl-ai-agent-evaluation-evidence]]；作者明确把 trace、reproduction、management/reporting interfaces 与测试信心连接起来。
- **边界**：trace 仍只是被 instrument 的投影；它不能自动覆盖未埋点状态，也不能替代安全、架构或语义正确性的独立判断。

## 生产 Agent fleet 的监督指标

Anthropic 把内部 Agent 监督拆成三个可运营指标：monitoring coverage、review latency 与 escalation rate；同时使用 persistent agent identity 和 open communication，把动作、消息与 transcript 绑定到具体 Agent。

**判断**：当 Agent fleet 进入数万规模，Observability 需要同时记录“多少活动被看见、多久被处理、多少被阻断/升级”，单一 trace completeness 已不足以描述治理能力。
- **证据**：[[20260922-anthropic-pace-ai-development]]；2026-08 其最常用 research/engineering Agent 平台任一时刻约 30,000 个 Agent，平台动作 100% 经过 online monitor 且被 offline monitor ingest；超过十亿次决策中约 0.002% 被 online monitor 阻断，offline 流程每周约 50 个最高优先级 flag 升级人工。
- **边界**：100% 指 instrumented platform 内的覆盖，不等于 monitor recall、低 false-negative 或公司全部 Agent 活动覆盖；这些数据来自 Anthropic 自报告。

## 与已有框架的连接

- [[Agent-Verification]]：记录、判据、独立性与证据覆盖分别检查。模型家族、共享目标和激励不能代理共同错误率。
- [[Agent-Loops]]：资源、目标与风险停止分别定义；计数器或确定性成功谓词也可触发停止，不要求每次外部人工解释。
- [[Distinct-Principal-Identity]]：记录主体与跨信任域授权，区分记录所见与真实权限。
- [[Agent-Security]]：行为发现、阻断及外部效果对账分开验收。

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

- 上述 OTel GenAI/开放提案、GDM 与 Anthropic 指标是 2026-09 归档证据，不代表当前规范、产品或全部部署；本轮未重新访问对应原始网页或复算历史数字。
- 未获包含真实动作分母、监控召回、同步阻断、权威终态与恢复结果的完整匹配生产数据。观测质量不能仅由 span 完整性、响应速度或日志数量决定。
- 不断言存在由 Rice、Kolmogorov 或 Ashby 联合推出的统一上限、永久意图不可观测、观察必然滞后、共压唯一根或正的共同盲区下界。选择观察目的和风险边界，再验收实际可辨识信息、缺失、误报与成本。
- 隐私、跨域访问、人工接收与纠错、数据保留，以及监测本身造成的开销均应按任务验证。

## 关联概念

- [[Agentic-Engineering]] — 任务与执行证据。
- [[Agent-Harness]] — 执行记录与监控接口。
- [[Verifiable-Agent-Engineering]] — 证据与效果验收。
- [[Distinct-Principal-Identity]] — 主体及权限谱系。
- [[LLM-as-a-Judge]] — 验证器测量与校准。
- [[Human-Governor-Agent-Operator]] — 责任与接收面。

## 开放问题

按 [[research-agenda]] 现行 EX-002/004/005/006 条件寻找证据覆盖、真实效果及控制状态的联合记录；针对明确任务比较采样与保留方案的可复现性、风险发现和成本，保留未埋点与未知终态。旧 ATSC 采纳、不可压缩性经验测量及“监督终端约定性”不作现行已证命题。

## 相关 QA

历史 Q-A 链见 [[20260715T140612--qa-Agent-Observability根本限制__qa]]，以 2026-11-28 勘误为准。
