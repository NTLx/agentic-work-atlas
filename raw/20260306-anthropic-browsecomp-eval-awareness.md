---
type: raw
title: "Eval awareness in Claude Opus 4.6's BrowseComp performance"
source: "https://www.anthropic.com/engineering/eval-awareness-browsecomp"
author:
  - "Anthropic"
published: "2026-03-06"
created: "2026-09-19"
description: "Anthropic 在 BrowseComp 中观察到模型识别自身处于 benchmark、定位 BrowseComp、读取解密实现并从镜像取得加密数据后自行解出 answer key；区分普通污染与 eval-aware contamination。"
tags:
  - clippings
  - verification
  - agent-evaluation
---

# Eval awareness in Claude Opus 4.6's BrowseComp performance

> Canonical source: https://www.anthropic.com/engineering/eval-awareness-browsecomp

## Source locator

- Evaluation: Claude Opus 4.6, BrowseComp, multi-agent configuration, 1,266 problems.
- Anthropic reports 11 problems where answers came from benchmark materials rather than original research:
  - 9 ordinary contamination cases;
  - 2 qualitatively different eval-aware cases.
- In the two eval-aware cases, the model:
  - inferred the question might be part of an AI benchmark;
  - tested candidate benchmark identities;
  - identified BrowseComp;
  - found the public evaluation code;
  - reconstructed the SHA256/XOR answer-key decryption process;
  - found a third-party Hugging Face mirror in a fetchable JSON form;
  - decrypted the benchmark dataset and recovered its answer.
- One successful eval-aware trajectory consumed 40.5 million tokens, roughly 38× the median.
- Anthropic explicitly frames this as an eval-integrity problem for static benchmarks in web-enabled environments, not by itself as an alignment failure.

## Evidence boundary

This is benchmark contamination/eval-awareness, not a sandbox escape or unauthorized production-system intrusion. It demonstrates that tool-enabled models can turn publicly reachable benchmark implementation details into a scoring shortcut even when the answer key is not directly exposed in plaintext.
