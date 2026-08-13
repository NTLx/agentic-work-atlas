---
type: entity
title: Knowledge-Profiling
aliases:
  - 知识画像
  - Knowledge Profiling
  - 知识剖析
  - 五剖面
definition: "以事实（而非问题）为分析单位的 LLM 事实性诊断框架——把每条事实按其是否被编码、可取用程度分为五种剖面（encoding failure / recall failure / direct recall / recall with thinking / inference without encoding），分离'没学到'与'学到了取不出'两类错误"
created: 2026-08-13
updated: 2026-08-13
evidence_level: high
claim_type: extracted
tags:
  - llm-memory
  - factuality
  - evaluation
related_entities:
  - "[[Reversal-Curse]]"
  - "[[Memory-Architecture]]"
  - "[[Structured-Agent-Memory]]"
  - "[[Verifiability]]"
  - "[[LLM-as-a-Judge]]"
  - "[[Over-Inference]]"
source_raw:
  - "[[20260215-recall-bottleneck-parametric-factuality]]"
  - "[[20260812-google-recall-bottleneck-factuality]]"
---

# Knowledge Profiling（知识画像）

> [!definition] 定义
> **Knowledge Profiling（知识画像）** 是 Calderon et al.（ICML 2026）提出的行为学事实性诊断框架：把分析单位从事后逐题准确率移到"每条事实处于什么知识状态"，按 encoding（是否编码）与可及性（能否取用、是否需要 thinking）把事实分入五种剖面，从而区分"空书架"（没学到）与"丢钥匙"（学到了取不出）两类失败。

## 五种知识剖面

| 剖面 | 条件 | 干预指向 |
|------|------|---------|
| Encoding Failure（空书架） | 未编码且未知道 | pre-training（scaling / 数据覆盖） |
| Recall Failure（丢钥匙） | 已编码但取不出 | post-training / 推理时方法 |
| Direct Recall | 已编码且无需思考直接取用 | 理想状态 |
| Recall with Thinking | 已编码、仅靠 thinking 可取用 | 恢复机制的存在证明 |
| Inference without Encoding | 未编码但 thinking 可推断 | 低可靠，可能诱发幻觉 |

操作化三概念：**encoding**（在 pre-training 相似上下文中可复现 = 存在量词剪裁）、**knowledge**（跨措辞/语向可作答 = 全称量词剪裁）、**recall**（知道 = 已编码 + 可取的插值）。WikiProfile（2,150 维基自然事实 × 10 任务）是其基准载体。

## 核心发现：取用是瓶颈

- 前沿模型（Gemini-3-Pro / GPT-5）编码 95–98% 的事实，却仍无法直接取用 26–34%；scaling 主要补 encoding，recall 失败随规模占比反升。
- 长尾事实与反向问题（[[Reversal-Curse]]）的失败绝大多数是 recall 失败而非缺知识。
- thinking 恢复 40–65% 的已编码未直取事实，仅 5–15% 的未编码事实 → **thinking 主要是取用促进（recall facilitation），不只是推理**。

## 关键数据点

- 基准：WikiProfile 2,150 条维基自然事实 × 10 任务；13 个模型 × 8 采样，约 450 万响应
- 前沿模型编码 95–98% 事实，仍直接取用失败 26–34%；thinking 后仍失败 11–12%
- thinking 恢复 40–65% 已编码未直取事实，仅 5–15% 未编码事实

## 前提与局限性

- encoding 操作化（encoding-via-memorization）可能系统低估真实编码；`τ=0.5` 阈值为主观设定。
- 基准限 Wikipedia 类显著事实，不覆盖企业长尾专有知识。
- 作者为 Google Research 且评测自家 Gemini 系，存在利益相关。

## 关联概念

- [[Reversal-Curse]] — 被再框架为 recall 问题的相邻现象
- [[Memory-Architecture]] — 记忆系统工程层；知识画像提供事实层的诊断语言
- [[Structured-Agent-Memory]] — "知识存储 ≠ 可检索"的工程对应
- [[Verifiability]] — 识别（多选）强于生成（recall）的评测方式敏感性
- [[LLM-as-a-Judge]] — 该框架使用 prompted LLM autorater 做自动打分
- [[Over-Inference]] — 镜像现象："有却说不出来" vs "没有却说得出"