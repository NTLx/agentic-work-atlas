---
type: source-summary
title: "How to Evaluate LLM Provider Performance Across Latency, Throughput, and Uptime"
source_raw:
  - "[[20260728-openrouter-evaluate-llm-provider-performance]]"
created: 2026-07-29
updated: 2026-07-29
tags:
  - source-summary
  - token-economics
  - evaluation
evidence_level: medium
claim_type: mixed
---

# How to Evaluate LLM Provider Performance Across Latency, Throughput, and Uptime

> OpenRouter（2026-07-28）方法论博客：同一 model slug 在不同 provider 端点行为不同——基础设施、量化、负载处理、路由默认值都改变结果。给出四指标框架（TTFT/吞吐/可用性/量化）+ 百分位读法（读尾部不读均值）+ 量化风险梯度 + benchmark 六问 + 五步清单，终点是把评估转化为路由策略。来源：OpenRouter 官方。证据等级：medium（厂商方法论文章——评估框架独立有效，但实证仅一个未给数值的数据点，且结论"用路由层别硬编码 provider"恰是 OpenRouter 产品目录）。

## 编译摘要

### 1. 浓缩

- **核心结论1**: 评估从 workload 出发，不从 provider 出发。同一 model slug 跨 provider 端点行为不同（基础设施/量化/负载处理/路由默认值），四指标各有适用 workload
  - 关键证据:
    - **延迟（TTFT）**: 请求→首 token，用户面 chat/agent/流式界面看这个
    - **吞吐（output tokens/sec）**: 生成开始后的持续输出速度，批量生成/长文本/代码看这个——"强 TTFT 的 provider 长文本体验仍可能弱，反之亦然"
    - **可用性**: benchmark 条件表现好 ≠ 高峰不挂/不限流/不报错尖峰
    - **量化**: 隐藏的质量变量（见结论2）
- **核心结论2**: 两条读法纪律——读尾部不读均值，查 serving 路径再怪模型
  - 关键证据: "provider 可以 p50 很强而 p99 很弱"——均值隐藏尾部停顿，用户记住的是卡住的那次请求；滚动 5 分钟窗口的 p50/p75/p90/p99 百分位统计。量化风险梯度：fp16/bf16（低风险）→ fp8/int8（中）→ fp4/int4（更高）；摘要管线可容忍低精度，tool-calling agent/推理/代码编辑对静默质量损失容忍度低。2026-06-24 实例：两家 provider 服务同一 claude-sonnet-4.5，p99 尾部都比 p50 暗示的宽得多
- **核心结论3**: 评估终点是路由策略，不是 provider 选择。benchmark 只做候选短名单（六问：TTFT/输出速度是否分开报告、尾部还是均值、是否标明端点与 serving 设置、是否考虑量化、是否反映当前性能、是否匹配你的 prompts），最终用自己的 prompts 测量，结果固化为路由设置（sort/百分位阈值/quantizations 过滤/ignore/fallbacks），provider 选择绑定自己的测量而非硬编码名字或市场排名
  - 关键证据: 五步清单（定义 workload → 外部 benchmark + 实时数据短名单 → 自己的 prompts 测试（含会打垮弱 provider 的 prompts）→ 查量化与 provider 行为 → 通过路由执行结果）；OpenRouter 默认路由行为：过去 30 秒有重大故障的 provider 降权，稳定者按价格加权负载均衡，其余作 fallback

### 2. 质疑

- **关于激励结构的质疑**: 文章每个方法论段落的落点都是"that's what our routing layer is designed to handle"——"别硬编码 provider、用路由层"恰是 OpenRouter 的产品目录。与库内 langchain（框架厂商）/ ai-mania（咨询）/ if-ai-is-so-great（部署服务商）/ github-harness（工具厂商）构成**激励结构五连同构**：都批评某种"直连/硬编码"行为，都出售中介层。评估方法论本身（百分位纪律、量化作为隐藏变量）独立于结论有效，可单独提取；结论方向需参照激励审视
- **关于证据密度的质疑**: 全文仅一个具体数据点（2026-06-24 双 provider claude-sonnet-4.5 延迟曲线），且未给数值只有定性描述；"滚动 5 分钟窗口"统计是平台自有数据，无第三方可复核的方法披露。方法论主张（如"量化改变难题表现"）无对照实验支撑
- **关于适用边界的质疑**: 百分位方法论假设"有足够流量产生有意义的尾部统计"——低 QPS 长尾 workload 的 p99 没有统计意义，文章未讨论；五步清单第 3 步"跑会打垮弱 provider 的 prompts"假设已有 eval 集，对没有 eval 基础设施的团队是循环建议
- **关于 FAQ 的质疑**: FAQ 节是搜索优化导向内容（信息密度显著低于正文），与正文重复；文章整体是"方法论包装的产品文档"混合体裁

### 3. 对标

- **与库内命题的直接收敛**: [[Token-Supply-Chain]]"多模型定价透明性"节（07-18）记录 tokenizer 差异 → `$/token × token 数` 双变量偏差（**计数侧**隐藏变量）；本文补上**质量侧**——同一模型、不同精度/基础设施 = 不同行为。两侧合起来构成模型消费的完整隐藏变量表。学术成本路由（RouteLLM 省 2x+、IPR 省 43.9%）与本文的工业路由手册互补覆盖同一命题："路由是可测量的工程问题，不是信仰选择"
- **量化隐藏变量 ≈ [[Mechanical-Sympathy-for-LLMs]] 的操作实例**: "check the serving path before blaming the model"（两家 provider 同一模型、难题表现不同，先查 serving 精度再怪模型）正是 Fowler/Thompson 机械同理心的 LLM serving 版——理解机制实际如何运行，而非推测模型能力
- **与 vectoral 中转市场的两端对照**: [[Token-Supply-Chain]] 灰色形态节（relay 市场 97.8% 折扣）是"同一 model slug、不同 serving"的极端版——买家连端点背后是什么精度、什么 key 来源都不知道。OpenRouter 的 quantizations 字段 = serving 透明度的制度化；relay 市场 = 完全不透明。两者是 provider 评估光谱的两端（综合判断）
- **跨域类比: 百分位纪律 ≈ SRE 的 SLI/SLO 传统**: "读尾部不读均值"是 web 工业十五年前的教训（p99 尾延迟决定用户体验，均值掩盖尾部）——LLM serving 工业正在重新发明 SRE 轮子，这本身说明该领域工程成熟度所处阶段（综合判断）。量化风险表 ≈ 供应链分级："便宜端点用精度换成本，买方需显式声明可接受等级"

### 关联概念

- [[Token-Supply-Chain]] — 网关/代理层的工业评估方法论；补上定价透明性命题的质量侧隐藏变量
- [[Mechanical-Sympathy-for-LLMs]] — "查 serving 路径再怪模型" = 机械同理心的操作化
- [[Layered-AI-Sourcing]] — provider 评估与路由策略是分层采购的执行层工具
