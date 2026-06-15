---
type: entity
title: Einstein Test
aliases:
  - Einstein Test
  - 爱因斯坦测试
definition: "用历史截断知识测试 AI 是否能提出后来才出现的突破性理论或深层问题的科学创造力基准"
created: 2026-05-08
updated: 2026-06-16
evidence_level: medium
claim_type: mixed
tags:
  - AI
  - benchmark
related_entities:
  - "[[Demis-Hassabis]]"
  - "[[Scientific-Discovery-AI]]"
  - "[[Taste]]"
  - "[[Jagged-Intelligence]]"
  - "[[World-Model]]"
  - "[[Continual-Learning]]"
source_raw:
  - "[[Demis Hassabis: Agents, AGI & The Next Big Scientific Breakthrough]]"
---

# Einstein Test（爱因斯坦测试）

> [!definition] 定义
> **Einstein Test** 是一种检验 AI 科学创造力的思想实验：只给系统某个历史时点以前的知识，看它能否自主提出后来才出现的突破性理论、问题或研究方向。它测试的不是“会不会解题”，而是“能不能发明值得解决的新问题”。

## 为什么重要

许多 AI benchmark 测试的是已知题库中的解题能力。Hassabis 提出的 Einstein Test 指向更深一层：科学创造不只是从已有问题中找到答案，还包括提出新的框架、问题和解释方式。

这一区分对 [[Scientific-Discovery-AI|科学发现 AI]] 很关键。一个系统能解黎曼猜想，仍然可能只是超强解题器；能提出新的千年难题，并让顶级研究者承认其深度，才更接近原创科学家的能力。

## 关键数据点

- Hassabis 用“只给 1901 年前知识，看系统能否推出后来突破”来说明测试思路；重点不在具体年份，而在历史知识截断。
- 他认为当前系统尚未展现真正的大规模发现能力，尤其缺少超出现有模式的类比推理。
- Move 37 代表在已知规则下找到惊人解法；Einstein Test 要求的是创造新框架或新问题。
- 该测试把“解决问题”和“提出问题”分开：前者可以靠搜索、推理和工具增强，后者还需要判断什么问题深刻、值得研究。

## 可操作化难点

| 难点 | 说明 |
|------|------|
| 历史截断 | 很难精确定义某一时点的可用知识边界 |
| 数据泄露 | 训练语料中可能残留后世概念、语言和隐喻 |
| 评价标准 | 如何判断一个新问题“足够深刻”需要人类专家共识 |
| 实验周期 | 科学突破可能需要长时间实验和工具链，不是一次回答能判定 |

## 与相邻概念的边界

- [[Scientific-Discovery-AI]] 讨论在组合搜索空间中找突破；Einstein Test 进一步测试能否定义新的搜索方向。
- [[World-Model]] 提供对环境和理论空间的内部表示；没有世界模型，系统难以提出稳定的新解释。
- [[Continual-Learning]] 让多轮实验和失败能积累；没有持续学习，科学探索会退化为一次性解题。
- [[Taste]] 在这里不是审美装饰，而是判断“什么问题值得研究”的能力。

## 前提与局限性

- Einstein Test 目前更像研究纲领，不是成熟 benchmark。
- 它可能低估实验数据的重要性：有些突破不是纯推理能产生，而是依赖新仪器、新观测和历史偶然。
- 如果训练数据无法彻底去除后世知识，测试结果会被污染。
- 即便系统通过某个历史截断测试，也不代表它具备通用创造力；可能只是特定领域的搜索空间被刻画得足够好。

## 关联概念

- [[Scientific-Discovery-AI]] - Einstein Test 是科学发现能力成熟度的高阶检验
- [[World-Model]] - 创造新理论需要可更新的世界模型
- [[Continual-Learning]] - 多轮探索需要把失败和发现累计起来
- [[Taste]] - 发明新问题需要判断深刻性和重要性
- [[Jagged-Intelligence]] - 解题强不等于提出问题强
