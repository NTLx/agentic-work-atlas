---
type: source-summary
title: "Our approach to EU text provenance rules"
canonical_url: "https://openai.com/index/eu-text-provenance/"
raw_state: index
original_raw_file: "raw/20261005-openai-eu-text-provenance.md"
original_body_sha256: "0435ba9ea4ca5a80d6979e0d3dd3908f634f070857eba04e9f797d8e75a48ee2"
indexed_at: 2026-10-21T12:43:24+08:00
created: 2026-10-21
updated: 2026-10-21
tags:
  - source-summary
  - content-provenance
  - text-watermarking
  - ai-policy
evidence_level: high
claim_type: mixed
authors:
  - "OpenAI"
venue: "OpenAI News, 2026-10-05"
source_locator:
  - "textGrain 机制与 SynthID 对标：How our watermarking works and performs，第 1–2 段"
  - "1% target FPR 下的长度、题材和同义词编辑检测数据：同节，第 3–4 段及 ELI5 图表说明"
  - "Astra benchmark 质量主张与数值：Impact of watermarking on output quality，表格"
  - "水印不能推出的结论：What a text watermark doesn’t tell you，五项限制"
  - "API、EU 产品与 detector 的 rollout：Our next steps"
  - "分层 provenance：Our broader approach to content provenance"
---

# Our approach to EU text provenance rules

## 编译摘要

### 1. 浓缩

- **核心结论1**：OpenAI 的 textGrain 是独立的文本水印实现：它在模型选词中加入不可见统计信号，再由 detector 检查该信号；OpenAI 称其与所测试方法（包括文本 SynthID）相比表现相当或更好，但没有说 textGrain 属于 SynthID。
  - **关键证据**：`How our watermarking works and performs` 明确将 textGrain 命名为 OpenAI 的技术，并说明它向 word choices 加入 statistical signal；同节把 SynthID 列为对照方法。
- **核心结论2**：textGrain 的检测率依赖文本长度、选词自由度和编辑程度。OpenAI 报告，在 1% target false positive rate 下，心理学类 200-token 段落约检出 80%，400-token 约 95%；数学等受约束文本显著更低。对 400-token 段落做同义词替换，替换 10% 时检测率约从 92% 降到 66%，替换 25% 时降到 17%。
  - **关键证据**：检测率与编辑实验均在 `How our watermarking works and performs`；图表说明实验材料是 ELI5 上的 watermarked responses，编辑数据来自英文回答。
- **核心结论3**：水印只提供有限的生成路径信号，不能测量人类贡献、确立所有权或责任、识别用户、验证内容真假；未检出也不证明人工写作。OpenAI 的 rollout 与此限制相配：API 全球对部分模型提供 opt-in；符合条件的 ChatGPT/Codex 在 EU 逐步启用；文本 detector 初期仅向获批研究者和专家组织开放。
  - **关键证据**：`What a text watermark doesn’t tell you` 明列上述推断边界；`Our next steps` 说明分渠道部署及 detector 的个案审批策略。

### 2. 质疑

- **关于检测性能**：关键数字来自 OpenAI 自家的实验与 detector，属于厂商自评；原文披露了目标 FPR、部分文本长度、题材及编辑比例，但不能据此推定其他语言、模型、真实使用分布或第三方复现下的表现。目标 FPR 也不等于每个部署场景的实际误报率。
- **关于输出质量**：Astra 多项 benchmark 表格中，OpenAI 自评称有/无水印未见“meaningful”性能差异。该结论是 OpenAI 基于其选定 benchmark 的自我评估；表格数值有升有降，未提供足以把“未见有意义差异”推广到长尾任务、主观质量或所有模型的独立验证。
- **关于检测结果解释**：命中只能支持“文本含有该 provider 水印信号”这一有限判断，不量化 AI 与人的贡献比例，也不构成作者身份、责任、权利或真实性证明；未命中可能源于篇幅短、编辑、翻译、模型覆盖范围等，不能反推人工写作。
- **关于部署策略**：EU 产品逐步启用、API 全球 opt-in、detector 限定专家访问，是 OpenAI 在技术不确定性下的政策选择。与 Anthropic 来源所述的全球启用策略不同；不能把 Anthropic 的 rollout 理由或范围套用于 OpenAI。
- **数据与来源可靠性**：OpenAI 官方页面是其自身机制、计划和实验数字的一手来源，适合提取“OpenAI 如何实现/自评/部署”的事实；其性能与质量主张仍有厂商自评边界。技术报告当时标注为后续补充，本文未把未披露的算法细节补写为事实。

### 3. 对标

- **与 [[Claude-Text-Watermark]] / [[SynthID-Text]] 对照**：两者都属于生成阶段嵌入、事后由 provider detector 验证的文本水印技术族；Anthropic 页面将 Claude 实现描述为 SynthID-Text 变体，而 OpenAI 把 textGrain 作为独立实现，并把 SynthID for text 列为比较对象。共同技术类别不意味着算法同一。
- **与启发式 AI detector 对照**：文本水印在生成时携带特定实现的统计信号，由相应 detector 检查；heuristic AI detectors 则从文本表面模式估计生成来源，不应混作同一种机制。二者的错误类型和证据含义不同。
- **部署与跨域判断（综合）**：Anthropic 的来源记录全球启用 Claude 水印；OpenAI 采取 EU 合格产品逐步启用、API 全球 opt-in、detector 受限访问。它们显示同一合规/内容 provenance 问题可以导向不同的部署边界，而非单一行业默认策略。
- **分层 provenance（OpenAI 的框架）**：OpenAI 将开放标准/Content Credentials、不可见水印、verification 工具与政策、滥用检测、举报、调查及 enforcement 组合使用。C2PA/Content Credentials 记录文件来源与历史，水印可在 metadata 被移除后留下信号；这是互补层，不表示 C2PA 就是文本水印。
- **共同边界（跨来源综合）**：短文本或低选词自由度的文本更难检出，编辑/改写会削弱信号；检测到的是生成路径相关信号，不能据此确定身份、责任、所有权或真实性，未检出也不能证明人工创作。各实现的量化表现和 rollout 仍须分开归属各自来源。

## 证据定位

- textGrain 的命名、机制及与 SynthID 的比较：原文 `How our watermarking works and performs`。
- 1% target FPR、200/400-token 心理学结果、数学类较低结果及 synonym 编辑实验：同节正文和 ELI5 图表说明。
- Astra 的 benchmark 表与“meaningful”质量判断：`Impact of watermarking on output quality`；这是 OpenAI 的自评。
- 人类贡献、所有权/责任、用户身份、真实性及未检出边界：`What a text watermark doesn’t tell you`。
- 分渠道 rollout 和 detector 访问策略：`Our next steps`。
- C2PA、不可见水印、verification 与政策执法的组合：`Our broader approach to content provenance`。

### 关联概念

- [[Text-Watermarking]]
- [[Claude-Text-Watermark]]
- [[SynthID-Text]]
- [[C2PA-Content-Credentials]]
- [[20260816-anthropic-claude-text-watermark]]
