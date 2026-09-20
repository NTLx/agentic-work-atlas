---
type: source-summary
title: "Introducing EVMbench"
source_raw:
  - "[[20260218-openai-evmbench]]"
canonical_url: "https://openai.com/index/introducing-evmbench/"
raw_state: full
source_locator:
  - "OpenAI overview: 117 vulnerabilities / 40 audits / detect-patch-exploit"
  - "paper code/data section and exploit-mode harness: deterministic transaction replay and on-chain verification"
  - "OpenZeppelin audit 2026-03-02 for reference-quality conflict"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - verification
  - benchmark
evidence_level: medium
claim_type: mixed
---

# Introducing EVMbench

## 编译摘要

### 1. 浓缩

- **核心结论 1：执行结果可以通过独立、可重放的外部状态来判定。**
  - 关键证据：EVMbench exploit 模式使用 Rust harness 部署合约、确定性 replay agent transaction，并通过链上状态做 programmatic verification。
- **核心结论 2：同一 benchmark 应把 detect、patch、exploit 当作不同验证对象。**
  - 关键证据：detect 衡量发现问题，patch 要同时保持功能并消除 exploitability，exploit 则验证端到端资产攻击是否真实完成。
- **核心结论 3：确定性执行 oracle 不能自动保证 reference truth 正确。**
  - 关键证据：OpenZeppelin 后续审计指出若干漏洞分类/可利用性问题；即使 replay 完全确定，若题目标注或漏洞 reference 本身有误，最终 score 仍可能测错对象。

### 2. 质疑

- EVM 状态天然可重放、可哈希、可程序化验证，这一优势不能直接迁移到开放式知识工作或 GUI 任务。
- OpenAI/Paradigm 构建的 benchmark 与外部 OpenZeppelin 审计存在 reference-quality 冲突，应把“执行真值”和“题目真值”分别记录。
- sandbox 中可验证的 exploit success 不等于现实网络攻击风险或经济损失概率。

## 冲突标记

- OpenAI/Paradigm：EVMbench 以精选高危漏洞作为 benchmark reference。
- OpenZeppelin（2026-03-02）：审计该 benchmark 后报告方法学问题，并指出至少四个 high-severity 条目在其实践判断中并不可利用。
- 处理：保留 EVMbench 的 deterministic replay / on-chain post-state 作为 **execution truth** 证据；不把其全部 vulnerability labels 当作未经争议的 **reference truth**。

### 3. 对标

- 对 EX-004：EVMbench 是“reference truth ≠ execution truth”的清晰实例；确定性 replay 能强化后者，却不能修复前者。
- 对 [[Verifiable-Agent-Engineering]]：可重放环境是高质量 verifier 的理想形态，但仍需要独立 reference audit。
- 对 [[Agent-Security]]：高影响动作最好留下可回放 receipt 与 canonical post-state，而不是依赖模型自述成功。

## 关联概念

- [[Verifiable-Agent-Engineering]]
- [[Agent-Verification]]
- [[Agent-Security]]
- [[Cybersecurity-Proof-of-Work]]
