---
type: source-summary
title: "The Return of the Deployment Company"
source_raw:
  - "[[The Return of the Deployment Company]]"
created: 2026-05-23
updated: 2026-05-25
tags:
  - source-summary
  - FDE
  - AI-deployment
---

# The Return of the Deployment Company

## 编译摘要

### 1. 浓缩

- **核心结论1**：AI 原生产品削弱了传统 SaaS 的三个经济前提，因此头部 AI 厂商正在用 FDE 把模型能力变成高价值、难复制的现场部署服务。
  - 关键证据：文章指出 AI 产品有真实推理成本、工具生命周期缩短、基于人类 UI 习惯的锁定下降；OpenAI、Anthropic、Google 在 2026 年 5 月密集押注部署公司或 FDE 组织，包括 OpenAI DeployCo、Anthropic 与金融资本合作、Google Cloud 招募 AI deployment engineers。
- **核心结论2**：FDE 的核心资产不是“写了多少代码”，而是把客户现场的隐性知识编码进评测集、提示链、流程配置和交付经验。
  - 关键证据：文章用保险理赔等场景说明，真实规则常常存在于资深员工头脑里，必须通过现场观察、反复纠错和业务反馈才能提取。FDE 的商业价值在于把这些难以购买、难以复制的 tacit knowledge 转化为可运行系统。
- **核心结论3**：从企业买方看，FDE 会带来四类结构性风险：隐性知识流向外部、数据边界被重画、议价权被评测集锁定削弱、FDE 离开后只剩空壳。
  - 关键证据：文章提出企业应谈判评测集 IP、导出权、行业复用限制、续约价格保护和退出交接条款。特别是评测集和 prompt/config 不是附属品，而是后续议价与迁移能力的核心资产。
- **核心结论4**：到 2026 年，on-prem AI 的条件已经成熟，企业不应把 FDE 当作唯一答案，而应采用分层 sourcing。
  - 关键证据：文章认为开源模型能力差距缩小，vLLM、TGI、Ollama、LangChain、LlamaIndex、Open WebUI 等栈更成熟，HPE/Dell/Lenovo/NVIDIA 等硬件方案降低本地部署门槛。高频、高敏感、核心工作流更适合 on-prem；前沿、低频、需要旗舰能力的任务可用 FDE 或 cloud API；过渡期可以用 FDE 加速学习，同时建设内部 AI ops 能力。
- **核心结论5**：企业采购 AI 的关键问题不是“买不买 FDE”，而是“哪些能力必须留在组织内”。
  - 关键证据：文章给出五个合同问题：谁拥有 evaluation set；合同结束能带走什么；供应商是否承诺不把本公司知识用于同行；是否有续约价格保护；是否有 transition-of-service 条款。对于已签 FDE 合同的企业，作者建议同步建设内部团队、备份 evaluation set，并在续约时重谈这些条款。

### 2. 质疑

- **关于事实基础的质疑**：文章明确承认核心事实来自 2026 年 5 月公开公告和行业报告，关于三家厂商战略动机的部分属于作者解释，不能当作厂商官方口径。
- **关于 on-prem 成熟度的质疑**：开源模型、本地硬件和推理框架确实降低了本地部署门槛，但文章的成本比较是 illustrative estimates，不足以替代具体 TCO 模型。
- **关于 FDE 风险的质疑**：FDE 不必然制造外部依赖。若客户提前要求评测集可导出、知识不跨客户复用、内部团队共同建设并保留运行能力，风险会显著下降。
- **关于能力差距的质疑**：文章把多数企业任务归入开源模型可覆盖范围，这对 RAG、文档处理、客服和报告生成较合理，但对复杂 agentic、多模态、前沿推理、强合规审计场景未必成立。
- **关于 on-prem 执行成本的质疑**：本地部署不是一次采购问题，而是持续的组织能力问题。企业需要 AI operations architect、模型升级策略、推理服务 SLO、评测体系、红队测试、权限隔离和审计机制；这些长期成本可能比硬件采购更难。
- **关于买方视角的质疑**：文章站在企业买方风险控制视角，可能低估了 FDE 对缺少内部 AI 能力企业的启动价值。对很多组织而言，外部 FDE 是进入 AI 部署的第一条可行路径，而非纯粹的锁定陷阱。

### 3. 对标

- **跨域关联1：咨询业知识边界**：FDE 延续了高端咨询“知识会随顾问流动”的老问题，但新增差异是知识可能被编码进评测集和 AI 系统，复用性更强、锁定更隐蔽。
- **跨域关联2：企业 IT 采购**：AI sourcing 不应是 FDE 或 on-prem 的二选一，而应按工作流敏感度、调用频率、数据边界和是否需要前沿能力做分层。
- **跨域关联3：组织能力建设**：FDE 可以作为学习脚手架，但企业必须把评测集、提示配置、流程文档和运维能力留在内部，否则短期部署成功会变成长期能力空洞。
- **跨域关联4：硬件主权**：文章把 [[Hardware-Sovereignty]] 从技术偏好提升为战略议价工具。只要推理日志、prompt、评测集和运行经验都在供应商侧，客户就很难真正拥有 AI 能力。
- **跨域关联5：部署飞轮与锁定的双面性**：FDE 对供应商是 [[Deployment-Product-Flywheel|部署-产品飞轮]]，对客户可能是 [[Tacit-Knowledge-Lock-In|隐性知识锁定]]。同一个机制从卖方看是 moat，从买方看是依赖风险。
- **迁移判断**：部署公司的回归不是 SaaS 倒退，而是 AI 把“客户现场知识”重新变成产品能力的一部分。企业要做的是把外部部署转化为内部能力，而不是只购买一次系统上线。

### 关联概念

- [[Forward-Deployed-Engineer]]
- [[Forward-Deployed-AI-Enablement]]
- [[Evaluation-Set]]
- [[Tacit-Knowledge-Lock-In]]
- [[Layered-AI-Sourcing]]
- [[Hardware-Sovereignty]]
- [[Deployment-Product-Flywheel]]
- [[The-OpenAI-Deployment-Company]]
- [[AI-Factory-vs-Forward-Deployed-AI-Enablement]]
