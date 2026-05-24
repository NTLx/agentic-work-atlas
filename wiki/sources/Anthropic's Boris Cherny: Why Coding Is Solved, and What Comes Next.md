---
type: source-summary
title: "Anthropic's Boris Cherny: Why Coding Is Solved, and What Comes Next"
source_raw:
  - "[[Anthropic's Boris Cherny: Why Coding Is Solved, and What Comes Next]]"
created: 2026-05-24
updated: 2026-05-24
tags:
  - source-summary
  - claude-code
  - ai-coding
---

# Anthropic's Boris Cherny: Why Coding Is Solved, and What Comes Next

## 编译摘要

### 1. 浓缩

- **核心结论1: "编程已被解决"——模型写 100% 代码，工程师角色转变为"目标定义者"和 Agent 管理者。**
  - 关键证据: Boris 2026 年没写过一行代码，模型生成 Claude Code 仓库 100% 的代码。日常 10-30 个 PR/天，记录是 150 PR/天。主要工作设备是 iPhone——Claude App 代码 tab 中常驻 5-10 个 session、几百个 Agent，夜间有几千个 Agent 做深度工作。
  - 关键证据: Claude Code 的起源来自 **Product Overhang**（产品能力溢出）——模型已经具备的能力超出了现有产品的释放边界。2024 年底主流还是 typeahead（一行一行补全），Boris 团队判断"不需要补全了，直接让 Agent 写全部代码"。但这前六个月没有 PMF——他自己只用它写 10% 代码。真正的指数增长从 2025 年 5 月 Opus 4 开始，之后每一代模型都让曲线再次 inflection。
  - 关键证据: Anthropic 的策略是"为下一代模型构建产品"。Claude Code 早期是 deliberate 地"pre-PMF"产品——团队明确知道要等 6 个月模型才能配上。

- **核心结论2: Loops（循环调度）是 Agent 工作流的未来——简单到极致却最具爆发力的机制。**
  - 关键证据: Loop = 让 Claude 通过 cron 起定时循环，可以是每分钟、每五分钟、每天。Boris 有几十个 Loop 在运行：babysit PRs（自动修 CI、rebase）、维持 CI 健康（自动修 flaky test）、每 30 分钟抓 Twitter 反馈并聚类。
  - 关键证据: Anthropic 已推出 Routines（Loop 的服务器版）——关掉笔记本后 agent 继续运行。Boris 称 Loop"就是未来"，4.7 模型甚至开始自己建议启动 Loop。
  - 关键证据: Anthropic 内部没有手写代码——所有 SQL、代码、甚至 Claude 之间通过 Slack 互相通信，跨 Agent 的问询自动路由。

- **核心结论3: 软件构建将像识字一样普及——历史上的印刷术是最精确的类比。**
  - 关键证据: 15 世纪前欧洲识字率约 10%，识字的 scribes 为不识字国王服务。印刷术发明后 50 年，欧洲出版的文献超过了过去 1000 年总和。500 年后全球识字率 70%。Boris 认为软件开发将更快经历此过程。
  - 关键证据: "最好的会计软件编写者不是工程师，而是好会计师——领域知识是难的部分，编程是简单的部分"。模型抹平了编程能力差异，让领域专家直接成为 builder。
  - 关键证据: 未来团队将由 Cross-Disciplinary Generalists（跨学科通才）组成——既擅长产品工程，又精通设计、数据科学、产品管理。Claude Code 团队每个人（工程经理、PM、设计师、数据科学家、财务、用户研究员）都写代码。

### 2. 质疑

- **关于"编程已被解决"的质疑**: Boris 在访谈中也自我限定——"对我来说是的"，但承认"非常庞大复杂的代码库、小众语言"仍未解决。他的标准是"我可以全部用模型"，不等于"所有 GitHub 上的问题都被解决了"。
- **关于 Harness 重要性的质疑**: Boris 说 Harness 重要性在下降——"模型变得更好，就不需要那么多 safety mechanisms"。但这假设模型幻觉和安全性会持续线性改善——历史上模型进步是 jagged 的，某些安全问题可能长期存在。
- **关于 Loops 的质疑**: Loop 的极致特征是"最笨但最有效"，但大量 agent 无监督运行的累积风险——flaky test 的自动修复如果修复错了呢？大规模 agent-to-agent 通信的语义漂移如何管理？
- **关于护城河框架的质疑**: Boris 引用 Hamilton Helmer 的 7 Powers 框架认为 switching costs 和 process power 被 AI 削弱，但换个角度——如果每个人都有相同的 AI 工具，network effects 和 scale economies 也可能被 AI-powered startups 更快地挑战。

### 3. 对标

- **跨域关联1: 印刷术类比 ↔ 软件民主化**: Boris 的类比精确契合——scribes（抄写员）= 传统工程师，印刷术 = AI coding agents，识字率普及 = 编程能力普及。差异在于：软件民主化会比印刷术快得多（不需要等 500 年教育体系和农业社会转型）。
- **跨域关联2: Product Overhang ↔ 技术成熟度曲线 (Hype Cycle)**: Product Overhang 描述的是"模型能力 > 产品释放"的 gap——这是 AI 时代特有的不对称性（传统技术通常在产品成熟后才能力溢出）。Boris 的 pre-PMF 策略实质是"在 trough of disillusionment 入场，在 slope of enlightenment 收获"。
- **跨域关联3: Agent-to-Agent 通信 ↔ 企业服务总线 (ESB) / 微服务架构**: Boris 描述的"Claude 通过 Slack 互相 ping 对方"实质是 AI-native 的微服务编排——将 ESB 的模式从 API 端点转移到了自然语言对话层面。

### 关联概念

- [[Product-Overhang]]
- [[Agent-Loops]]
- [[Cross-Disciplinary-Generalist]]
- [[Software-Democratization]]
- [[Moats-in-AI-Era]]
- [[Claude-Code-CLI]]
- [[Agentic-Engineering]]
- [[Coding-Agents]]
- [[Agent-Swarm]]
- [[Vibe-Coding]]
- [[Harness-Engineering]]
