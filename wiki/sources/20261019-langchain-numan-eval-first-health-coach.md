---
type: source-summary
title: "How Numan built an eval-first AI health coach with LangGraph and LangSmith"
canonical_url: "https://www.langchain.com/blog/how-numan-built-an-eval-first-ai-health-coach-with-langgraph-and-langsmith"
raw_state: index
original_raw_file: "20261019-langchain-numan-eval-first-health-coach.md"
original_body_sha256: "ed2341f4c234cb0a3b892fe5eb518da367fbc9dae15b7b3181d5414ee51cc8d0"
indexed_at: "2026-11-07T09:48:40+08:00"
created: 2026-11-07
updated: 2026-11-07
tags:
  - source-summary
  - agent-evaluation
  - agent-safety
evidence_level: medium
claim_type: mixed
source_locator:
  - "Where standard eval approaches fell short for Nu / static single-turn and scripted multi-turn failures"
  - "The eval framework we run today / themed datasets and category-specific judges"
  - "The thing we ship is the thing we test / production LangGraph parity and provider migration"
  - "Behavioural tests to keep the regulatory boundary / MHRA scope, release gates and guard nodes"
  - "Simulating conversations instead of scripting them / patient persona, scenario, turn limit, prototype"
  - "Simulating conversations instead of scripting them / conflicting missed-dose rubrics and clinician ownership"
  - "The stack: LangGraph and LangSmith / trace, annotation, datasets, experiments"
  - "Where we are heading: scaling the criteria, not just the agent / online evaluator still future"
---

# How Numan built an eval-first AI health coach with LangGraph and LangSmith

> 一手来源：[LangChain Case Study / Numan（2026-10-19）](https://www.langchain.com/blog/how-numan-built-an-eval-first-ai-health-coach-with-langgraph-and-langsmith)；作者 Asif Laldin、Marcus Wadge-Dale、Shubhangi Hora、Konstantinos Georgakilas。2026-11-07 已读取原文。本文是自撰的证据地图及知识编译，不存储网页逐字全文。文中指标和改善属于团队自报，不构成独立临床安全性证据。

**来源保留边界**：官方原文位于上方 canonical URL；本页保存章节证据定位和综合分析。临时 Raw 仅为注册用来源记录，\`original_body_sha256\` 对应该记录，**不是网页原文正文的哈希**。不能把本索引当作原文镜像或独立 Evidence。

## 编译摘要

### 1. 浓缩

- **核心结论 1：对于医疗边界附近的会话式 Agent，错误的评测标准会把正确的对话节奏打成失败，或者掩盖关键越界。**
  - **证据（Where standard eval approaches fell short for Nu）**：Numan 的 Nu 是生活方式/健康指导 Agent，目标不包含医学诊断、处方或临床决策。早期静态单轮 fixtures 要求极短对话中同时完成共情、探询和建议，误罚了合理的逐步指导；将多个用户输入预写为固定脚本也失败，因为第二轮用户回答可能与 Agent 实际第一轮输出没有任何因果关系。全局平均分又会稀释少数高风险失败。
  - **证据（The eval framework we run today）**：团队保留单轮可判定项——supervisor 路由、药物问题安全回复、guard 生效、摘要——按 coaching/safety/medication/routing/summarization 等主题分别汇总并按每个 rubric 能在单轮观察到的内容判定；真正依赖多轮交互的行为不能用单轮指标冒充。

- **核心结论 2：评测运行的对象必须是同一个真实生产图，并把法律/临床边界变成变更时的阻断性回归测试。**
  - **证据（The thing we ship is the thing we test / Behavioural tests to keep the regulatory boundary）**：Nu 基于 LangGraph；supervisor 向各领域专家 subagent 交接。团队不复制 prompt 到独立测试 harness，而是在与患者实际交互的同一图上运行评测，避免评测和生产漂移；在跨两家前沿模型供应商选型时复用同一套主题测试，文章称一次供应商迁移测试缩短到一天（自报、无对照）。
  - **安全机制**：MHRA 相关医疗用途与一般 wellness/教育之间是产品声明的边界。出站安全 guard 对每条消息按临床安全规则核查，失败返回 supervisor 重新生成；仍失败则用安全 fallback。安全主题用回归门禁阻断发布；人工 health coaches 每天抽样审阅真实对话，以人的专业判断校准边界。
  - **重要区分**：声称按 wellness 范围设计、内部 guard 检查通过，不等于独立证明其没有医疗器械监管义务；医学/法规分类需依据司法辖区和实际用途单独核实。

- **核心结论 3：动态模拟患者与临床人员拥有的 rubric 相结合，是扩展覆盖面的方向，但原型不能冒充可发布的安全门。**
  - **证据（Simulating conversations instead of scripting them）**：最新原型给低成本患者模拟模型一个 persona、场景、待发掘困难与 turn limit，模型每轮根据 Nu 的真实回答继续对话，再由 judge 按主题评定整段 Transcript，可构造隐蔽请求或对抗性边界挑战。作者称这类模拟与 prompt hardening 降低了 jailbreak 情形的严重越界，但没有公开可复验的完整样本与绝对率。
  - **关键制度缺口**：原型中“漏服药物”场景的 rubric 自相矛盾：一套要求拒答并引导就医，另一套要求基于患者药品说明书给通用信息；同一 prompt 无法同时满足。**原文明确规定这一层仍是 prototype，采用工程师编写的 rubric，在临床人员签字审核前，不用于发布门禁，也不能支撑任何安全声明。**
  - **现状与计划分离**：LangSmith 当前记录生产/模拟 traces、实验和人工标注；对生产真实会话持续运行在线 evaluator、自动 backlog 和 prompt 调优仍为下一步或早期实验，不能计入已落地的保障。

### 2. 质疑与边界

1. **单轮与多轮测量不能相互替代**：药物问题的直接回答、guard 状态是单轮可检查的；是否在数轮中尊重对话节奏、适当探询并维持边界则需动态轨迹。若把“必须在两轮给出完整建议”写进评分，Agent 会为刷分过早建议。
2. **临床安全最终由谁拥有？** 工程团队可以实现自动测试，但临床边界的 rubric、冲突仲裁和版本批准必须由具备授权与专业资格的人负责；人类抽检不能证明没有低频严重失败。
3. **评价器误判与自我验证**：出站 guard、LLM Judge、同一模型家族和测试集会有共模漏报；回归门禁的确定性执行与“临床安全已得到保证”是不同层次。需要真实专家盲审、失败分析、分歧治理与 held-out 对抗场景。
4. **法律事实适用范围**：文中引用 MHRA 意在阐明其 UK wellness/medical device 边界设计，不能据其直接给其他地区的医疗软件作监管分类，也不能推广至诊疗、处方或临床决策产品。
5. **供应商迁移效果**：一日迁移、模拟改善属于单一企业案例，没有披露对照、风险分层或统计置信区间；不能外推所有多 Agent 更换模型供应商所需时间。
6. **上线前后监控不等价**：每日人工抽检属于当前机制；计划中的持续在线自动评分尚未落地，不能写成已运行的生产安全持续验证。

### 3. 对标与约束（跨来源综合判断）

| 层 | Numan 机制 | 关联知识 | 关键不可替代对象 |
|---|---|---|---|
| User journey 质量 | 单轮分类评测 + 自适应模拟多轮 | [[20261015-google-agent-evaluation-beyond-vibe-check]]、[[Rubric-Based-Evaluation]] | 不用单一平均分掩盖医疗越界 |
| Oracle ownership | 临床人员审阅和批准边界 rubric | [[Evaluator-Miscalibration]]、[[Evaluation-Integrity]] | 未签字原型不能变发布门禁 |
| Tested equals shipped | 直接测真实 LangGraph 图，LangSmith 留 traces | [[Verifiable-Agent-Engineering]]、[[Agent-Harness]] | 避免“独立仿制测试系统”与生产漂移 |
| Output guard | 模型判断 → 尝试重生成 → 安全 fallback | [[Agent-Security]]、[[Escalation-Based-Human-Oversight]] | guard 自身须受评测，不等于强制型医疗合规措施 |
| 人工监督 | 每日专家抽检与题目/标准校正 | [[Human-Governor-Agent-Operator]] | 抽样概率和漏报仍未知 |

- **应用到企业 Agent/生信产品（建议，非原文实施）**：对于会产生专业解释、数据筛选或临床相关输出的 Agent，将 `domain_owner`、`rubric_version`、`scenario_class`、`release_gate`、`guard_trace` 等分开标识；安全指标不得被一般答复质量平均分覆盖。专业边界、无授权动作/数据保护和结果正确性须分别由适格专家或独立测试批准。
- **应用到 LLM WiKi 的自动进化（类比）**：原文来源可核验、Claim 是否有足够证据、推断是否越界，应由不同质检规则把关；不能用“报告很好看”或 aggregate 分数推导知识质量。与健康监管无直接同构，应限于质量方法的借鉴。

## 重要判断（Claim / Evidence / Boundary）

- **判断（综合）**：一个受监管风险约束的会话 Agent，其最稀缺、最需要责任人的资产可能不是 prompt，而是能够识别不合格行为、允许纠错并拒绝发布的准确评测标准。
  - **证据**：本篇「Where standard eval approaches fell short」「Simulating conversations instead of scripting them」「Building an AI coach near a regulatory line」。
  - **边界**：该主张来自作者团队案例；未签临床批准的原型评测仅供研究，不可形成对患者安全的独立保证。

## 关联概念

- [[Evaluator-Miscalibration]]
- [[Verifiable-Agent-Engineering]]
- [[Evaluation-Integrity]]
- [[Rubric-Based-Evaluation]]
- [[Agent-Security]]
