---
type: source-summary
title: "Designing for Agents — Zeno Rocha, Resend"
canonical_url: "https://lspace.beehiiv.com/podcast/s/latent_space_the_ai_engineer_podcast/designing_for_agents_zeno_rocha_resend"
raw_state: index
original_raw_file: "20261110-latentspace-resend-designing-for-agents.md"
original_body_sha256: "a2a233bf63328bf372a34dad471186fd9927beae158d9dc18f1638ae25c38bcb"
transcript_text_sha256_normalized: "be78f90023a2194ab4afff8e16760be9f89ae91da8683204ce4a194742e5dbcf"
indexed_at: "2026-11-11T08:28:19+08:00"
created: 2026-11-11
updated: 2026-11-11
tags:
  - source-summary
  - developer-platforms
  - agentic-engineering
  - tool-use
evidence_level: medium
claim_type: mixed
source_locator:
  - "Transcript 00:00–06:54: 创业定位、受访者自报规模、Agent 选择 API"
  - "Transcript 06:54–17:05: 邮件发送、限流、信誉、反滥用、追踪域风险"
  - "Transcript 17:05–23:55: 免费层、支持知识沉淀、DNS 与 Domain Connect"
  - "Transcript 23:55–31:58: React Email 开源入口、SDK 下载量与商业分销"
  - "Transcript 31:58–37:55: Amazon SES 薄封装和周边运维成本"
  - "Transcript 37:55–46:29: MCP、OAuth/RBAC、80+ tools、独立后台 API"
  - "Transcript 46:29–52:41: CLI、语言 SDK、多人邮件编辑与源代码模板"
  - "Transcript 52:41–58:28: Agent 收件箱愿景、送达信誉隔离"
  - "Transcript 58:28–1:06:00: AEO、FAQ、Markdown 文档与定价修复案例"
  - "Transcript 1:06:00–1:12:14: 推荐排名、分发、无登录试用与滥用风险"
  - "Transcript 1:12:14–1:16:51: 企业获客、价格与业务自报"
  - "Transcript 1:16:51–1:25:44: 家庭、产品品味、品牌命名"
---

# Designing for Agents — Zeno Rocha, Resend

> **来源**：Latent Space，2026-11-10。受访者 Zeno Rocha（Resend 联合创始人兼 CEO）。[官方播客和完整 Transcript](https://lspace.beehiiv.com/podcast/s/latent_space_the_ai_engineer_podcast/designing_for_agents_zeno_rocha_resend)；[同一出版者文章版](https://latent.space/p/resend/)。
>
> **实际读取记录**：通过 Vercel Sandbox 获取官方网页 HTML（834,320 bytes，SHA-256: 00afc2e900f90e453e75ab7856b6e3b4d8f2e58fbdfe3ff97c332f0ee47e08ef），提取并保留全部 501 个带时间戳的 Transcript 语句，范围 00:00–1:25:44，提取文本 95,430 UTF-8 bytes，约 17,480 个空格分隔英文词，文本 SHA-256: **be78f90023a2194ab4afff8e16760be9f89ae91da8683204ce4a194742e5dbcf**。网页显示节目总时长 1:25:52。本文为原文可回溯的中文编译，而非 Transcript 全文拷贝。主持人于 04:51 明示自己是 Resend 天使投资人；访谈中的商业业绩与产品体验并非独立审计。

## 编译摘要

### 1. 浓缩

#### 1. Agent Experience（AX）不止让模型推荐，还要让它完成任务

- **原文（05:02–06:54）**：主持人已设置 Cloudflare Email、域名和 DNS，却发现 coding agent 在代码 PR 中仍推荐 Resend。这是一个 Agent 可能替人类完成技术采购初筛的具体例子。模型从哪个公开数据或内部理由作出推荐，访谈没有给出可复现的因果解释。
- **原文（37:55–46:29）**：Zeno 将产品目标描述为接近“formless”，API、CLI、SDK、Dashboard、MCP 作为不同入口供人和 Agent 选择。构建 Remote MCP 又迫使产品补 OAuth/RBAC 与资源级权限，不只是贴一层协议。
- **综合判断**：AX 应包含 **可发现/被选择 → 可被机器准确理解 → 可授权执行 → 可验证产生业务结果 → 可观察和修复**。AEO 排名与 MCP 调用量仅覆盖其中局部。
- **边界**：单个 PR 例子不能证明大模型普遍偏好 Resend，更不能证明该偏好来自某种 AEO 技术。

#### 2. React Email：开放的上游工具，带来下游服务的自然采用

- **原文（23:55–26:39）**：团队在做 Resend API 时，通过访谈发现工程师首先痛苦于跨邮箱客户端兼容的 HTML 邮件模板。于是先发布开源 React Email，文档特意支持与 SendGrid、Mailchimp、Mailgun 等竞品集成；开发者先用模板工具，之后需要发送服务时可能自然考虑 Resend。
- **细节**：React Email 以 JSX 模板组件和 TypeScript 等工程工具生成邮件 HTML；邮件客户端并不运行 React 的浏览器交互。它更接近编译器/模板工具，而不是完整交互式 Web App。
- **原文（28:11–28:50）**：Zeno 说 Resend SDK 的 NPM 下载量超过 SendGrid 两倍，也承认竞品实际发送邮件量可能远高于 Resend，因此 **NPM downloads ≠ 邮件发送量 ≠ 收入/市占率**。
- **综合判断**：真正的分发护城河可能来自提供可移植且能先解决问题的上游工具，而不是只在 Agent 的推荐榜刷出现次数。
- **边界**：React Email 是否直接带来多大付费转化没有独立因果数据。

#### 3. “发送 API 成功”不是实际交付：队列、信誉和外部反滥用系统

- **原文（06:54–12:46）**：向 Gmail 等平台发送十万封邮件不能将 API 接收视为全部即时收件。供应商必须安排批次队列、节流、IP 和域名信誉、退信/投诉反馈，按历史和新客户行为对发信速率进行治理。嘉宾称其检测新近注册的域名、仿冒域名、异常突发发量等信号；其口述曾遇到约两万个域名的大规模滥用企图，未见独立案件材料。
- **原文（12:46–14:23）**：Resend 自动从 HTML 派生 plain-text 邮件；Zeno 自述显著改善投递质量，但未展示对照组或准确提升幅度。开信统计依赖 1x1 像素，而邮件隐私保护、预加载与安全扫描可让打开事件不对应真人阅读。
- **原文（14:23–17:05）**：共享 click-tracking 跳转域有典型 **noisy neighbor** 问题：某一租户群发钓鱼可污染共享域的信誉，让合法租户也被安全系统封锁。受访者主张自定义跟踪域、早期异常识别和区分“误用”与“恶意滥用”。
- **综合判断**：**API accepted ≠ queued ≠ provider accepted ≠ inbox delivered ≠ human read**。Agent 只收到 send API 的成功响应，不能据此宣称邮件被收件者阅读。业务交付应有真正的状态回执、重试/死信、撤销/补偿及租户信誉隔离。
- **边界**：邮箱最终交付由外部收件平台控制，不存在供应商对所有邮件送达收件箱的无条件保证。

#### 4. 免费层与高信任需要“产品内化的治理”共同存在

- **原文（17:05–20:11）**：Resend 早期客服需要逐人解决配置问题，后来采用一种制度：回复工单前，先把重复问题写成知识库文章并提供链接；再转向在产品中提前防止常见错误。Zeno 希望保留开发者免费层，同时监测投诉、异常发送模式并迅速处理。
- **原文（19:43–23:55）**：大量新用户不会配置 CNAME/TXT 等 DNS 记录。团队推动 Domain Connect，使 DNS 服务商与 SaaS 服务商通过授权式交互配置域名记录；受访者提到 Cloudflare、Vercel 等提供商。该体验类似 OAuth，但**不能据此认定 Domain Connect 与 OAuth 的认证/授权安全模型相同**。
- **综合判断**：高频的困难步骤应内化为自动检查、诊断、授权与状态核验，而不是要求每位用户学习低层协议；系统仍必须对 DNS 修改、身份授予、账号绑定等保留权限边界和审计。
- **边界**：这种“允许免费访问但监测后立即制止”的策略要以强风控系统为前提，不能直接移植给高副作用企业 Agent。

#### 5. 官方 Remote MCP 是产品后端与权限治理的外显，不是“80 个工具”本身

- **原文（37:55–42:45）**：初期由外部开发者提供本地 MCP，在增长后 Resend 为正式远端 MCP 补 OAuth、RBAC、资源权限与 observability，再争取进入官方客户端与插件目录。Zeno 认为 vendor-owned 官方连接比第三方临时封装更可靠；他自述个人使用场景中因 PostHog MCP 更符合使用方式，而从 Plausible 迁移。
- **原文（43:00–45:40）**：Resend 的 MCP 从初期不到或约 20 个工具增加到采访时 80 多个，希望尽可能覆盖 Dashboard 功能，包括发邮件之外的团队邀请、用量、账单、删除、账号管理。但受访者也发现 Contacts 工具返回过大数据，导致上下文放不下。**工具定义太多与某一个工具返回过大，是两个不同失效来源**。
- **原文（44:14–45:40）**：Dashboard 专用私有 API 和对外公共 API 如果分叉，日后维护成本会高。受访者认为 UI、MCP、CLI 应复用同一业务 API/backend contract，而不是每个入口重复实现。主持人对比 Cloudflare Code Mode 的约 2 个通用工具（search/execute），Resend 自报更多命名工具仍有效；未展示头对头成功率、token、延迟基准。
- **综合判断**：对 MCP 设计应评估 **task success、权限正确性、工具发现难度、工具 schema tokens、结果 payload、轮次/延迟与观察/审计能力**。不能由工具数量决定好坏；高危 billing、delete、provision 等操作即使支持，也应具有最小权限和独立确认机制。
- **边界**：调用量增长与用户赞赏不能直接证明更高 Agent 完成率；“一定要把 Dashboard 100% 操作开放”只是受访者产品偏好。

#### 6. CLI、SDK、多人 UI 共存：Agent 不应替代所有人工交互入口

- **原文（46:29–49:53）**：Resend 保留 CLI，并为招聘职位提供 CLI/API 申请方式和内嵌 Skills。团队维护多语言 SDK（Java、Rust、.NET 等），Zeno 说他们评估自动代码生成工具后仍更愿意手工生成 SDK，认为语言原生体验重要。这个偏好没有给出系统质量测评。
- **原文（50:29–52:04）**：多人可视化邮件编辑器与 Git 中受版本控制的邮件模板都很重要。非工程团队可共同编辑并通过模板 ID/变量发送，开发团队则可把模板纳入版本管理。
- **原文（52:41–54:23）**：Zeno 谈到面向 Agent 的可编程收件箱，拟支持创建大量 inbox、read/unread、star、label 等 API，称产品正在准备推出。**这不是已确认全部 GA 的现成功能**。
- **综合判断**：同一业务契约应可通过人类 GUI、自动化 CLI、MCP 和 SDK 访问；各入口权限、字段和可验证结果应一致。Agent Inbox 若涉及邮件正文和附件，还须明确 mailbox ownership、retention、最小访问、身份、审计、配额。
- **边界**：给招聘系统提供 CLI 是差异化演示，不等于所有业务都值得维护 CLI；Agent Inbox 仍属路线图讨论。

#### 7. AEO 的更可靠收益是“模型终于能准确读懂业务事实”

- **原文（58:28–1:03:07）**：Resend 从框架级文档（Django 等）和 FAQs 逐步覆盖 llms.txt、文档/营销页的 Markdown 文本。Zeno 用 Agent 对比向 120 万地址发送邮件的多个供应商价格时，发现 Resend 的交互式 JavaScript 价格滑块未被正确读取，模型算错价格且误评价。添加可直接读取的 Markdown 价格表，数天后重新询问得到正确数字。
- **原文（1:02:44–1:03:07）**：主持人指出 HTML 滑块与单独 Markdown 表会导致**双真相源**，Zeno 承认维护成本。这正是一个看似“Agent-friendly”的方案可能引入的工程债。1:04:48 还指出可视化 JS 图表中的竞争对比数据，需另行提供文本，以供简单 fetch 工具读取。
- **原文（1:06:00–1:12:14）**：受访者猜测模型偏好较新工具与近期性、公开案例有关，但无法从封闭模型中证明推荐机制。节目文章引述一项研究：在 Claude Code 能提取的 102 条推荐中，Resend 首选 64 次、SendGrid 7 次；同时提及另一项研究中 Postmark 在多个模型里更领先，显示结果高度依赖样本和模型。**64/102 不是 AI 用户市占率或可外推的第一选择概率**。
- **综合判断**：AI 可读页面应由**同一版本化权威事实源**生成 Markdown/HTML/API；固定计费、超额、DNS 设置、认证、退款等真实任务基准，在多模型/版本下评测**回答准确性与执行正确性**，不仅追踪提及排名。
- **边界**：前后几天模型回答变好不能排除模型版本、搜索收录、会话提示差异等因素；llms.txt 是否改善 AEO 排名访谈未验证。

#### 8. 商业数字、战略与后半段话题的证据层级

- **原文（00:00–05:02）**：Zeno 自述当时约 430 万 users、12 万付费客户、约 1000 万美元 ARR，列举大客户并谈 SDK NPM downloads。这里没有用户定义、MAU/收入审计/会计确认口径；不能将注册用户、活跃用户、付费客户或大企业客户混用。
- **原文（31:58–37:55）**：基于 AWS SES 虽能快速提供发送 API，但会叠加 SNS/SQS/CloudWatch/webhook 等能力的运维足迹。受访者说 Resend 在推动下沉到自主邮件基础设施；属于当时建设中的战略，不等于已完成替换。
- **原文（1:12:14–1:25:44）**：包含企业销售、创始人家庭生活、远程工作、设计品味和品牌命名。可用于理解创始人的产品取舍，但不能作为 AX 工程效能/商业因果的证据。

### 2. 质疑

1. **来源利益关系**：主持人是投资者，受访者是经营者。商业成绩、MCP 采用和推荐排行应保持 self-reported 标记。
2. **相关性不等于原因**：React Email、FAQ、llms.txt、AEO 排名和营收增长可以同时存在，不能证明某一举措独立导致结果。
3. **定价双真相源**：单独提供 pricing.md 有助机器阅读，也可能让账单与模型判断因页面漂移而不一致；建议从一个计算/规则引擎渲染双格式。
4. **MCP 广覆盖与权限**：可调用不代表应该授权；billing/delete/团队成员权限操作具有不同的副作用与确认要求。
5. **工具数量不是效能指标**：80+ 命名工具和 2 个 Code Mode 工具针对不同 discoverability/上下文/风险折中，需跑等价任务基准才可比较。
6. **客服文档并非唯一解决方式**：把重复问题变知识是良好的沉淀，但更好的闭环可能是消灭不必要的出错步骤，降低人工成本。
7. **邮件指标外推风险**：被 API 接收/排队/外部平台接受/成功送达/真实阅读/点击均非同一成功定义；跟踪像素/重定向也受隐私和安全扫描污染。
8. **免费账户恶意与无意误用**：策略应考虑错误阻断、恶意泛化和对正常客户的影响，不能只看滥用拦截率。
9. **路线图 ≠ 已部署能力**：大量 Agent Inbox API 和自主邮件底层基础设施仍在规划或开发中。
10. **Agent-facing 改进应避免人类体验回归**：Markdown 表无法取代可用性良好的人类价格计算器；一致数据源比复制内容更重要。
11. **多入口容易产生多套语义**：UI、MCP、CLI、SDK 如果各自重复权限/计费逻辑，可能造成不一致；共享 backend 则仍需独立验证关键规则没有系统性错误。
12. **公司和模型版本变化**：采访是在特定时间录制，不能把当时注册数、工具数、产品发布状态或模型选择排名当成长期常量。

### 3. 对标（本次仅知识沉淀，非生产变更）

| 来自访谈的机制 | 本库关联 | 可复用的工程测试 |
|---|---|---|
| Agent 先于人选择 SDK | [[Agent-Ergonomics]]、[[Evaluation-Set]] | 固定已有供应商、凭证、成本和安全边界后，检查 Agent 是否错误引入新依赖 |
| 同一产品事实的机器格式 | [[Agent-Ergonomics]] | 同一计费配置生成 HTML/Markdown/API，对照 120 万封计费与超额价格 |
| 多入口共享业务后端 | [[Model-Context-Protocol-MCP]] | GUI/CLI/MCP 同一任务的结果、权限、审计与失败语义一致 |
| 80+ tools / 2-tools Code Mode | [[Agent-Ergonomics]] | 比较真实任务成功率、tool schema token、payload、延迟、回退路径 |
| Remote MCP 先补 OAuth/RBAC | [[Model-Context-Protocol-MCP]] | 多用户、资源权限、敏感动作和会话身份的端到端权限测试 |
| 发送不等于送达 | [[Agent-First-Process-Redesign]] | 已受理、已排队、外部回执、失败补偿和最终状态分层 |
| 免费层 + 反滥用 | [[Agent-First-Process-Redesign]] | 误用/恶意区分、速率限制与租户隔离 |
| 支持工单形成知识库 | [[Agent-Knowledge-Management]] | 重复问答纳入来源/审核/有效期管理，下一次优先返回可验证答案 |
| Agent 可编程收件箱 | [[Agent-Data-Minimization]] | inbox 所属、附件敏感度、留存时长、审计和最小授权 |
| 上游开源工具推动下游产品 | [[Agent-First-Process-Redesign]] | 先测真实任务解决率、再测后续转化，而非只看 SDK 下载量 |

## 前提与局限性

这是完整访谈的一手来源，适于支持 Resend 的产品设计逻辑和被报道的失败案例，**不等于独立性能、增长或安全审计**。来源追溯以官方全文 URL 和时间戳为准。本 Source Summary 为证据地图而非独立 Evidence；已按公开稳定 URL + 细粒度时间戳的现行 schema 结算为 compiled/index。Registry 中的 original_body_sha256 (a2a233bf63328bf372a34dad471186fd9927beae158d9dc18f1638ae25c38bcb) 仅是已删除的临时来源登记文件哈希，**不是完整网页 Transcript 哈希**；规范化全文的 SHA-256 为 be78f90023a2194ab4afff8e16760be9f89ae91da8683204ce4a194742e5dbcf（95,430 字节）。

## 关联概念

- [[Agent-Ergonomics]]
- [[ACI-Agent-Computer-Interface]]
- [[Model-Context-Protocol-MCP]]
- [[Agent-First-Process-Redesign]]
- [[Agent-Knowledge-Management]]
- [[Agent-Data-Minimization]]
- [[Evaluation-Set]]
