---
type: raw
title: "Establishing Best Practices for Building Rigorous Agentic Benchmarks"
source: "https://arxiv.org/abs/2507.02825"
author:
  - "Yuxuan Zhu"
  - "Tengjun Jin"
  - "Yada Pruksachatkun"
  - "Andy Zhang"
  - "Shu Liu"
  - "Sasha Cui"
  - "Sayash Kapoor"
  - "Shayne Longpre"
  - "Kevin Meng"
  - "Rebecca Weiss"
  - "Fazl Barez"
  - "Percy Liang"
  - "Daniel Kang"
published: "2025-07-03"
created: "2026-09-20"
description: "Agentic Benchmark Checklist：把 agent benchmark 有效性拆成 task validity、outcome validity 与 reporting；要求语义等价、ground-truth 正确/隔离、Oracle solver、人类一致性、环境与污染控制，并展示缺陷可使性能相对误估最高达 100%。"
tags:
  - clippings
  - verification
  - agent-evaluation
---

# Establishing Best Practices for Building Rigorous Agentic Benchmarks

> Canonical source: https://arxiv.org/abs/2507.02825
> Version used in prior research: v5.

## Source locator

- Introduces the Agentic Benchmark Checklist.
- Organizes benchmark rigor around task validity, outcome validity and benchmark reporting.
- Checklist topics include semantic equivalence of valid outputs, ground-truth correctness, ground-truth isolation from the subject agent, Oracle solver, judge/human agreement, environment and setup validity, contamination controls and impact of identified flaws.
- Cross-benchmark analysis reports that task/reward-design flaws can under- or overestimate performance by as much as 100% in relative terms.
- In an older τ-bench assessment, empty-action behavior could pass some tasks; reported do-nothing success rates were 38% for airline and 6.0% for retail.
- Applying ABC-derived corrections to CVE-Bench reduced reported performance overestimation by 33%.

## Evidence boundary

ABC is an audit framework and collection of case analyses, not a theorem that its checklist is necessary/sufficient for every benchmark. Individual examples refer to particular benchmark versions. Oracle solver and human review are validation tools, not guarantees that all semantic-equivalence or ground-truth errors have been found.
