---
type: source-summary
title: "Using Claude to reduce the attack surface of code"
canonical_url: "https://www.anthropic.com/research/attack-surface-reduction"
raw_state: index
original_raw_file: "20261020-anthropic-attack-surface-reduction.md"
original_body_sha256: "1c09284d2fb077e89ec49118b50d6c482860311b67957dd864c29b57c43d6947"
indexed_at: "2026-10-22T09:55:17+08:00"
created: 2026-10-22
updated: 2026-10-22
tags:
  - source-summary
  - cybersecurity
  - agentic-engineering
  - verification
evidence_level: high
claim_type: mixed
source_locator: "正文：Methods for reducing codebases’ attack surface；Claude’s findings；Case study: OpenSSH；Conclusion。"
---

# Using Claude to reduce the attack surface of code

## 编译摘要

### 1. 浓缩

- **核心结论 1**：相比逐个发现并修补漏洞，Attack Surface Reduction（ASR）把防御目标改写为“减少攻击者在部署状态下能够触达的代码与功能”。它不会消除未知漏洞，但可以在不知道漏洞具体位置的情况下同时降低一批未知漏洞的可达性与潜在严重性。
- **核心结论 2**：Anthropic 将 ASR 拆成三种可自动化检查：默认配置下不必要的 reachability、配置项之间导致安全控制失效的 interaction、以及认证/协议状态机等 hard gate 之前的 early reachability。
- **核心结论 3**：在 25 个、合计超过 500 万行代码的开源项目上，Claude 建立了 17,000+ 配置项清单，其中 3,842 个与安全相关，并报告 493 个问题。11 个 gated 项目全部存在非预期可达代码；其中包括 93 个不必要的 pre-auth surface、37 个认证前执行/记录状态的位置，以及 61 个会弱化 pre-auth control 的配置组合。
- **核心结论 4**：配置交互是高价值盲区。Claude 找到 162 个安全敏感且缺乏明确文档/警告的配置组合，其中 94 个会静默关闭安全控制。OpenSSH 案例进一步显示：约 4,500 行 ML-DSA-44 解析/验证代码在未启用算法时仍可被未认证客户端触达；修复后默认 pre-auth reachable code 约减少五分之一，并进入 OpenSSH 10.6。
- **核心结论 5**：Anthropic 的可复用 skill 不是只做静态猜测。每一轮先列 entry points，再用 dynamic trace 确认 finding；默认配置变更还要求项目测试和 black-box regression 与 baseline 完全一致，影响非默认行为的 gate 则留给人类裁决。

### 2. 质疑

- 493 是“issue”而不是 493 个可独立利用的漏洞，原文也明确指出不少 finding 单独并不可 exploit；不能把 issue count 直接转换成 CVE 数、风险降低比例或现实攻击成功率。
- 来源是 Anthropic Frontier Red Team 对自家模型/skill 的研究总结，没有公开完整 false-positive / false-negative denominator，也没有第三方复现所有 25 个项目，因此更适合作为“方法可行性 + 高价值案例”证据，而不是普遍 precision/recall 证明。
- ASR 只能缩小暴露面，不能证明剩余 reachable code 没有漏洞；同时，错误 gate 可能破坏少见但合法的部署配置，所以“默认行为不变”的回归测试并不能覆盖所有非默认使用场景。

### 3. 对标与约束

- **与漏洞发现的区别**：vulnerability finding 试图定位具体缺陷；ASR 先问“哪些复杂代码根本不需要对当前威胁主体可达”。二者是互补关系，而不是替代关系。
- **与 [[Agent-Verification]] 的连接**：dynamic trace、baseline regression、black-box suite 和 human adjudication 共同形成 evidence escalation chain，说明安全 Agent 的输出不能停在静态文本 finding。
- **与 [[Constraint-Driven-Engineering]] 的连接**：把 parser / protocol path 移到 authentication、allow-list 或显式 opt-in 之后，本质上是在运行时边界增加机器可检查约束，而不是要求模型更准确地“理解所有漏洞”。
- **硬边界**：ASR 的收益依赖真实 deployment/configuration；如果 inventory、dynamic trace 或 threat boundary 与线上环境不一致，得到的 reachability map 也会失真。

## 关联概念

- [[Attack-Surface-Reduction]]
- [[Agent-Verification]]
- [[Constraint-Driven-Engineering]]
- [[Agentic-Engineering]]
