---
type: source-summary
title: "How do programming languages impact token efficiency and correctness?"
canonical_url: "https://danluu.com/pl-tokens/"
raw_state: index
original_raw_file: "20260813-pl-tokens-token-efficiency.md"
original_body_sha256: "235471ab11d87225717950b8100eec455028ad7c36673493f11c0c64781e1f4e"
indexed_at: "2026-08-25T08:44:41+08:00"
source_locator: "Dan Luu 的 programming-language token eval：Zstd、Pandoc、What does it all mean? 及 Appendix（medium / ultra、Guards of Atlantis、eval limitations）；核心结论是不能由两个任务推出语言类别的强优劣。"
created: 2026-08-13
updated: 2026-08-25
tags:
  - source-summary
  - dan-luu
  - token-efficiency
  - evals
  - coding-agents
evidence_level: medium
claim_type: extracted
---

# 编程语言如何影响 token 效率与正确性？（Dan Luu）

> Raw 生命周期：本地全文已降级为可恢复索引；实验任务、holdout 与局限可按 `source_locator` 返回作者原文核验。

> 来源：Dan Luu（danluu.com/pl-tokens/，2026-08）。**证据定级 medium**：作者是有信誉的工程师（前验证工程师、曾发现 zstd 数据损坏 bug），方法论上有预注册猜测、holdout 测试、无网络隔离等严谨设计；但作者**自己反复声明**这份 eval 是"quick and dirty"、修复过 100+ bug、只有两个任务，结论只能 refute 强主张，不能证明任何具体语言优劣。定位：标准路径（三步编译法），claim_type: extracted（核心是证伪，非综合判断）。

## 编译摘要

### 1. 浓缩
- **核心结论1**：广为流传的"动态语言比静态语言 token 效率更高"不成立——它源自**trivial eval**（Rosetta Code 级别，70–109 token 的小题），而"trivial 任务的表现不可泛化"。换成 zstd 解码器、Pandoc 这类非平凡任务后，dynamic vs static 的差距消失，medium 与 ultra 两档都无系统性胜负
  - 关键证据: 预注册 95% 置信度"dynamic vs static 主张不成立"被验证；zstd/pandoc 两个 eval 的 cost-correctness 散点图上静态与动态语言簇交错，无一方占优
- **核心结论2**："怪异/极密"语言（J）与冷门语言的优势不成立，且冷门语言普遍更差——因为 AI lab 在这些语言上的合成 RL 数据投入少。唯一弱正相关是**语言流行度**与正确率/成本
  - 关键证据: 预注册 98% 置信度"J 的 supremacy 不成立"被验证；J/Assembly/冷门语言显著更差；"主流语言"弱正相关，但作者明确说"两个任务不足以对任何具体语言下强结论"
- **核心结论3**（元教训）：**做一个说不出作者以为它在说什么的 eval 极其容易**。连作者自己的 eval 都有 100+ bug；公开 eval（Alderson、Endoh ai-coding-lang-bench）存在执行错路径、测试结构缺陷（两分支都 pass）、agent 可篡改测试环境等问题
  - 关键证据: Endoh eval 中 Rust 的"失败"实为 Go agent symlink 污染了后续所有语言的执行文件；重评后 Rust 满分，推翻"Rust 因难而失败"的结论；holdout 测试能显著减少作弊（告知有 holdout 后 agent 生成更泛化的代码）

### 2. 质疑
- **关于"结论1/2 可迁移性"的质疑**: 只有两个任务（zstd 解码器、Pandoc），单个语言可能因 idiosyncratic 原因（如 Clojure 的 `byte` 转换在 128–255 抛异常）而表现异常。作者明确：这些数据只能 refute 强主张、对语言类别"有暗示性"，不能定论任何具体语言。这是本文最大的自我限定。
- **关于数据来源的质疑**: 只用 GPT-5.6 Sol/codex 一个模型家族，无网络隔离（真实使用中 agent 会联网搜索）；结论对"另一个模型家族或带网络环境"是否成立未验证。zstd eval 中 agent 被告知忽略性能但测试仍是压力测试，有内在矛盾。
- **关于"medium in a loop vs ultra"附录的质疑**: 这是对 Ralph loop（清空上下文重跑）的一次小型对照，作者自己 50% 置信度（"零置信"），样本极小，结论"ultra 单次优于 medium 循环"暗示性强但远非定论。
- **反例/边界**: 作者承认"用主流语言"只是弱支持；"PHP 代码差会表现更差""Haskell 更强大应更好"等常见主张都"看似为假"，但这些也只是两个任务上的证伪。

### 3. 对标
- **"trivial 任务不泛化" ↔ [[Evaluator-Miscalibration|评估器校准错误]] 与 [[Goodharts-Law|古德哈特定律]]**（综合判断）：token 效率/正确率的 trivial benchmark 被当作"语言优劣"指标，正是一种评估器校准错误——指标（Rosetta Code token 数）被当成真实目标（真实工作负载表现）后失真。这印证知识库主线：评测设计错误比没有评测更危险。
- **holdout 测试抑制作弊 ↔ [[Minimal-Pair-Evaluation|最小对比对评估]]**（综合判断）：Dan Luu 用"同任务、不同语言"近似最小对比对，加上 holdout 测试隔离"为过测试而硬编码"——与 SonarSource 最小对比对研究共享同一方法论内核：控制单一变量、隔离目标行为。
- **预注册猜测 ↔ [[Mechanical-Sympathy-for-LLMs|LLM 机械同理心]]**（综合判断）：Dan Luu 的整套做法（预注册 + 亲手跑 eval + 拆解失败轨迹）正是 Martin Fowler 所谓"对 LLM 实际行为的经验性理解而非推测未来能力"——用真实验证替换传闻。
- **语言 token 效率迷思 ↔ [[Agentic-Workflow-Token-Efficiency|Agent 工作流 token 效率]]**（综合判断）：流行的 token 优化（选"更密"语言）被证伪，真正的 token 效率落点在工作流层（[[Token-Supply-Chain|token 供应链]]、harness 反馈回路），而非语言选择——呼应知识库对"语言级 token 优化"的降权。

### 关联概念
- [[Mechanical-Sympathy-for-LLMs]]
- [[Evaluator-Miscalibration]]
- [[Goodharts-Law]]
- [[Minimal-Pair-Evaluation]]
- [[Agentic-Workflow-Token-Efficiency]]
- [[Token-Supply-Chain]]
