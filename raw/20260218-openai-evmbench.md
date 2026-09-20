---
type: raw
title: "Introducing EVMbench"
source: "https://openai.com/index/introducing-evmbench/"
author:
  - "OpenAI"
  - "Paradigm"
published: "2026-02-18"
created: "2026-09-19"
description: "117 个智能合约漏洞 / 40 次审计；detect、patch、exploit 三模式，exploit 用本地链、确定性交易 replay 与链上状态验证。"
tags:
  - clippings
  - verification
  - benchmark
---

# Introducing EVMbench

> Canonical source: https://openai.com/index/introducing-evmbench/
> Paper: https://cdn.openai.com/evmbench/evmbench.pdf
> Code/data: https://github.com/openai/frontier-evals

## Source locator

- Dataset: 117 curated smart-contract vulnerabilities from 40 audits.
- Modes: detect, patch, exploit.
- Patch grading combines automated tests with exploitability checks.
- Exploit grading uses programmatic transaction replay and on-chain verification.
- Rust harness deploys contracts, deterministically replays transactions, and restricts unsafe RPC methods.
- Exploit tasks run in an isolated local Anvil environment rather than live networks.

## Evidence boundary

EVMbench provides unusually strong execution-state verification, but it is domain-specific to EVM smart contracts. A separate OpenZeppelin audit published 2026-03-02 reported methodological flaws and at least four high-severity labels they considered non-exploitable in practice, so benchmark reference quality must be treated separately from replay determinism.
