---
type: source-summary
title: "How Claude's text watermark works"
source_raw:
  - "[[20260816-anthropic-claude-text-watermark]]"
created: 2026-08-16
updated: 2026-08-16
tags:
  - source-summary
  - ai-policy
  - content-provenance
  - watermark
  - eu-ai-act
evidence_level: high
claim_type: extracted
authors:
  - "Anthropic"
venue: "Anthropic News, 2026-08"
---

# How Claude's text watermark works

> 来源：Anthropic News（2026-08 前后）。**证据定级 high**：Anthropic 官方对自家 Claude 文本水印机制的完整说明 + SynthID-Text Nature 2024 一手 + EU AI Act + EU Code of Practice 政策原文链接。**claim_type extracted**：主体为 Anthropic 官方机制说明（事实），跨域对标为综合判断。

## 判题（主题宪法）

- **主问题命中**：AI 内容真实性 / 责任承担 / 合规路径（命中"组织与部署"主线）
- **结构性强**：机制清晰（低熵 token 选择 + 随机性源切换 + key-encoded 检测），可沉淀为三个 entity（Watermark / SynthID-Text / C2PA）
- **机制优先**：SynthID-Text 算法 + EU AI Act 合规路径 + 边界条件（factual / code / proofreading 处水印稀疏）
- **不冲淡主线**：一手政策 + 一手算法机制 + 边界条件

→ 收录，标准路径（三步编译法），触发 3 个新 entity。

## 编译摘要

### 1. 浓缩

- **核心结论 1**：**Claude 文本水印 = 基于"低熵 token 选择的随机性源切换"**——LLM 在生成每个 token 时本就有随机性（如"cold and..."之后选 overcast 还是 grey），水印仅替换这个随机性的来源（从通用 PRNG 换成"key + 前文"），让第三方可用 key 事后检测序列是否与带水印的生成路径一致
  - 关键证据：SynthID-Text（Aaronson 2022 提案 → DeepMind 2024 Nature 论文）是算法祖先；Claude 采用其变体；Aaronson 2022 是奠基性提案
  - 关键证据：检测能力受文本长度影响（短文本水印稀疏）；factual passages / code / proofreading 处 token 选择余地小，水印稀疏
- **核心结论 2**：**水印合规驱动 = EU AI Act + EU Code of Practice on Transparency of AI-Generated Content**（2026-07 签署）——Anthropic 与 ~190 个签署方承诺标记 AI 生成文本；Claude 全球范围内启用（无法按地域隔离）；2026-08-02 之前的 Claude 模型有过渡期
  - 关键证据：190 signatories；Code of Practice 在 2026-07 签署；EU AI Act 要求"methods of marking"；Anthropic 选择全球启用因为"无法 durable 地按地域 scope"
  - 关键证据：合规目标 = 文本归属判定（"what is the likelihood this was partly written by Claude"），不是用户身份追溯——watermark key 不包含用户/组织信息
- **核心结论 3**：**水印 vs 文件型内容凭证 = 两种独立信号**——文本用 SynthID-Text 水印；文件（.png/.jpg/.svg）用 C2PA metadata 内容凭证（cryptographically signed note in file's metadata）。两类信号互补但机制独立
  - 关键证据：C2PA 是开放行业标准（同 camera 厂商 + photo-editing 软件使用）；Anthropic 将提供 "drop a file and check" 工具
- **核心结论 4（候选第三条）**：**水印与 AI 检测软件（如 Pangram）的本质差异**——水印需要 provider 的 key（密码学验证），检测软件基于语言模式（heuristic 启发式）；前者准确率高但需密钥，后者是经验估计
  - 关键证据：Anthropic 列出 AI 模型常见的语言模式（"this isn't [X], it's [Y]"、"quietly" 等）

### 2. 质疑

- **关于"水印不影响输出质量"**：作者声明 SynthID-Text 在 Gemini 流量上 thumbs up/down 评分无统计显著差异；Claude 内部测试无影响。但评估仅在 thumbs rating 与"controlled study comparing watermarked vs unwatermarked answers"层面，未披露 token-level 分布差异是否影响事实一致性 / 创造力长尾 / 罕见词频率。**真正的"无影响"主张缺乏长期与多样任务的对照**
- **关于"无法按地域 scope"**：Anthropic 自承"don't yet have a durable way to scope it by region"——这意味着非 EU 用户的输出也被强制水印。这与"最小干预"原则存在张力，且未给出技术原因（key 不可地域化？还是部署架构不允许？）。这是一个 **policy 主张而非纯技术约束**
- **关于"watermark 不改变用户权利"**：作者声明"doesn't change a user's rights under our terms"——但 EU AI Act 第 4 条 Article 50 要求"告知用户内容是 AI 生成"，水印是技术手段而非告知机制；watermark 检测 API 是事后验证，不能替代前端 disclosure。**合规覆盖与告知义务是否完全等价，是另一个开放问题**
- **关于边界条件**：作者说"factual passages / code / proofreading 处水印稀疏"——这意味着高价值 AI 内容（事实性写作、代码）反而最难检测；轻编辑可能移除部分水印。这削弱了"AI 内容归属"的强主张
- **关于"Anthropic 自家与 Pangram 区分"**：Anthropic 强调自家水印 vs Pangram 检测软件的差异——但 Pangram 在 Anthropic 未提供 key 时仍可作为第三方估计手段。两者是互补关系，不是"watermark vs no watermark"二元对立
- **数据可靠性**：Anthropic 自家声明 + 引用 SynthID-Text 论文（高可信第三方）；EU Code of Practice 签署方列表（公开）；EU AI Act 引用（公开法规）。整体高可信，但"Anthropic 自家无影响"声明缺少独立第三方评估

### 3. 对标（跨域）

- **与 [[Anthropic]] 的关系**：本文是 Anthropic 2026 年发布的第三类机制声明——前两类是 [[Recursive-Self-Improvement|模型层 RSI]]（80% 合并代码由 Claude 写）+ [[N-Hour|N-Hour 安全研究]]（补丁后数小时内被 AI 构建利用代码）。本文是**合规层声明**：当 AI 改变工作系统时，谁来标记 AI 输出 → 这是组织与部署主线"AI 责任"侧的具体落地
- **与 [[SynthID-Text]] 的算法同源**：SynthID-Text 由 Google DeepMind 于 Nature 2024 发布，是当前主流 LLM 文本水印算法基础；Anthropic / Google / 其他签署方都在用同一技术族。这是**AI 责任基础设施的标准化集中点**
- **与 [[C2PA-Content-Credentials]] 的协同**：文本水印 vs 文件元数据是两种独立信号，覆盖两个不同威胁面。两者一起构成"AI 内容归属"基础设施
- **跨域对标 1（密码学水印传统）**：物理钞票水印 / 数字文档签名 / 音频指纹（Shazam）/ 图像感知哈希——AI 文本水印是同一家族的 LLM 实例。区别：传统水印是离散符号（人眼/耳可辨），LLM 文本水印是统计模式（人类不可辨）
- **跨域对标 2（金融服务 KYC / AML）**：watermark 类似于"AI 输出 KYC"——知道生成方是谁，但不知用户是谁。这与金融服务"know your customer"是同构关系，差别是金融服务追溯用户，watermark 追溯 provider
- **跨域对标 3（学术诚信）**：学生论文查 AI 是 watermark 检测 API 的天然应用场景；但作者声明"watermark only determines Claude was involved, not whether text is human-written"——这意味着"用 watermark 验证学生论文"是**有限应用**，需要结合其他方法
- **约束分析（ljg-constraint 应用）**：
  - **硬约束（世界规律）**：token 选择有随机性（算法基础）；key 必须保密（密码学基础）；factual / code 处 token 唯一性强，水印稀疏（语言结构）
  - **软约束（工程选择）**：使用 SynthID-Text 而非其他算法（市场收敛）；global rollout 而非地域 scope（部署简化）；文件用 C2PA 而非其他标准（生态选择）
  - **自设约束（解释性）**："watermark 不改变用户权利 / 不是 ownership 信号"——这是 Anthropic 主动框定解读的政策姿态，**不是技术事实**

## 关联概念

- [[Claude-Text-Watermark]]（本文触发的新 entity）
- [[SynthID-Text]]（本文触发的新 entity——Google DeepMind Nature 2024 算法）
- [[C2PA-Content-Credentials]]（本文触发的新 entity——文件元数据标准）
- [[Anthropic]] — 实施方；Anthropic entity 应回写 source_raw
- EU AI Act — 政策驱动
- Content Provenance — 内容归属通用问题
- [[AI-Policy-Framework]] — 政策框架
- [[Distinct-Principal-Identity]] — Agent 身份的反面：内容归属而非身份归属
- [[Reverse-Information-Paradox]] — AI 内容时代"AI 与人协作的产物归谁"的延伸问题

## 数据卡片

| 维度 | 数值 |
|------|------|
| 合规驱动 | EU AI Act + EU Code of Practice on Transparency of AI-Generated Content |
| Code of Practice 签署 | 2026-07 |
| 签署方总数 | ~190 |
| Anthropic 决定 | 全球 rollout（无法 durable scope by region）|
| 旧模型过渡期 | 2026-08-02 之前发布的模型有过渡期 |
| 算法基础 | SynthID-Text（Aaronson 2022 → DeepMind 2024 Nature）|
| 文件类型支持 | .png, .jpg, .svg（更多类型未披露）|
| 水印稀疏场景 | factual passages / code / proofreading |
| 检测 API | 即将推出（实现细节 in process）|
| 第三方检测 | Pangram 等（heuristic 启发式，无 key）|
| 用户追溯 | 不可（watermark key 不含用户信息）|