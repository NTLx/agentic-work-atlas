---
type: source-summary
title: "Why I Left Google DeepMind"
source_raw:
  - "[[20260715-why-i-left-google-deepmind]]"
created: 2026-07-16
updated: 2026-07-16
tags:
  - source-summary
  - ai-safety
  - ai-ethics
  - alignment
  - military-ai
  - ai-governance
evidence_level: high
claim_type: extracted
---

# Why I Left Google DeepMind

> Alex Turner（TurnTrout，原 Google DeepMind 研究科学家）2026-07-15 一手叙事。记述他因 Google 签署无限制军方 AI 合同而离职的全过程，以及对"AI 伦理承诺在压力下如何失效"的反思。一手材料，证据等级 high。

## 编译摘要

### 1. 浓缩

- **核心结论1：Google DeepMind 的伦理承诺在政治压力下失效，Anthropic 的承诺守住了——承诺信用 = 已付代价总和**
  - 关键证据：Google 与 Pentagon 签署机密 AI 合同，合同限制甚至比 OpenAI 更弱，未限制致命自主武器或大规模 AI 监控。Google 高管曾坚称"不会签"，但 Turner 事先警告被忽视。
  - 关键证据：Anthropic 拒绝 Pentagon"取消致命武器安全限制"要求 → 被 Hegseth 威胁列为"供应链风险"（强制所有军方承包商停用 Claude）+ 取消 `$200m` 合同 + 援引 Defense Production Act 强制供货。Anthropic 起诉 Pentagon 并守住红线。
  - 关键证据：Jeff Dean 2018 签署 Lethal Autonomous Weapons Pledge（"既不参与也不支持致命自主武器的开发、制造、贸易或使用"），2026 在 Google 签署无限制合同后仍留任。Turner 判定：留任 = 实质上"支持开发"。
  - **Turner 的判据**：承诺信用 = 已支付代价的总和。Anthropic 守住红线因其付了 Pentagon 诉讼的代价，Google 没付。

- **核心结论2：伦理承诺的失效是链条式的——多个"权力节点"逐个失守**
  - 关键证据：Turner 试图动员 AI 业界 luminaries（Stuart Russell / Yoshua Bengio / Geoffrey Hinton）反对 Pentagon 施压 AI 公司。Russell 在 iaseai 会议上口头承诺发起成员投票支持 Anthropic，但 iaseai 领导层（Mark Nitzberg）随后静默取消投票，从未发表声明。Bengio 办公室拒绝表态。
  - 关键证据：Turner 组织 250+ GDM 员工联名请愿 Jeff Dean、Jeff 公开联署支持 Anthropic 的 amicus brief——这是 C-suite 高管公开与公司沉默决裂的罕见动作，一度让 Google/Pentagon 谈判"卡住"。但 Jeff 未就 Google 自家合同施压 Sundar，合同仍签。
  - 关键证据：Turner 写 25 页 Red Line Framework（军方/监控法律专家审阅）提交 Demis Hassabis，被转交政策团队后"枯萎无人理"直到合同签署。
  - **链式失守**：iaseai（学术界）→ Jeff Dean（内部高管）→ Demis/Sundar（公司决策层）逐个在压力下未兑现承诺或表态。

- **核心结论3："留任 = 共谋"的伦理判据，与"可见付代价反抗"的真伦理分界**
  - 关键证据：Turner 自陈三种诚实选项：公开解释留任如何符合承诺 / 公开声明不再持有该承诺并说明原因 / 离职。"挂着承诺却沉默"不在其中。
  - 关键证据：Turner 拒绝跳槽到竞争对手实验室拿高额奖金，也拒绝了 OpenAI 安全团队的招揽——"我现在失业"。他的离职是可见的、付代价的反抗。
  - 关键证据：Turner 把"留任 steering 正向"的辩护驳为"什么 steering？"——Google Gemini 项目面临的最清晰红线都没产出一条约束性条款，"seat at the table"在那种情境都失效，何时才有效？

### 2. 质疑

- **关于"留任=共谋"的质疑**：Turner 的判据较严苛——"合同未禁止自主武器 ≠ 主动支持自主武器"的辩护（"blindfold 不免除责任"）有合理性，但"留任即共谋"可能忽略内部持续施压的累积价值。Turner 自己承认 Jeff 的 amicus 联署"让 Pentagon 犹豫"，说明留任者也能产生部分影响。判据的严厉度本身是价值判断。
- **关于"承诺信用=已付代价"的质疑**：该判据（07-16 think 追本的核心）是 Turner 叙事 + revealed preference + 量子测量类比的 synthesized 判断，非 Turner 原文显式陈述。Turner 给的是直觉（Anthropic 付了代价、Google 没付），理论形式化是 Agent 综合判断，应标 synthesized。
- **关于私密通讯的质疑**：Turner 明确声明"绝不未经许可引用任何人的私密言辞"，对私密对话"最小化描述"——这意味着支持其论证的更强证据被自我审查切掉了。读者需"相应地权衡"他的描述。

### 3. 对标

- **跨域关联1（吹哨伦理学）**：Turner 的"可见付代价反抗"与 Anthropic agentic misalignment 报告中 Opus 4.5"隐蔽零代价教唆吹哨"形成镜像——前者是伦理（可见性+代价），后者按 07-16 think 追本判据是"未定义"（零代价不可观测）。同一事件的两面：人 vs AI 的伦理承担结构差异。
- **跨域关联2（承诺经济学）**：与 commitment / credibility 文献同构——承诺的价值在于不可逆的代价绑定（burning ships）。AI 公司的"AI 安全承诺"若无对应代价支付记录（被触发的红线、被拒的合同、被弃的利润），则与 motivated mislabeling 同构：一个从未被测量的量，一份从未被支付的账。
- **跨域关联3（组织治理）**：与 07-14 有穷者治理悖论 + 信息-时间不对称闭合——决策者（Sundar）永不收到自己决策的反馈（承诺信用的侵蚀滞后且不可见），AI 伦理承诺的失效在组织压力下是结构性的而非偶发。

### 关联概念

- [[LLM-as-a-Judge]]
- [[Agent-Observability]]
- [[Anthropic]]
- [[AI-Policy-Framework]]
- [[Frontier-Developer-Obligations]]
- [[Societal-Resilience]]
