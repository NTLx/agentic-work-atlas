---
type: entity
title: TDD for Agents
aliases:
  - TDD for Agents
  - Red-Green TDD for Agents
  - Agent TDD
  - Test-First for AI
definition: "把 red-green TDD（先写失败测试 → 写实现 → 测试通过 → 重构）应用为 coding agent 的核心验证范式——让 agent 跑每行代码，杜绝'代码看起来对但未跑过'的 silent failure"
created: 2026-08-20
updated: 2026-08-20
tags:
  - verification
  - testing
  - agentic-engineering
  - agent-verification
  - red-green-tdd
evidence_level: medium
claim_type: extracted
related_entities:
  - "[[Agent-Verification]]"
  - "[[Code-Cleanliness-Agent-Footprint]]"
  - "[[Explain-Test-Gold-Standard]]"
  - "[[Rubric-Based-Evaluation]]"
  - "[[Simon-Willison]]"
  - "[[Skill-Chains]]"
source_raw:
  - "[[20260820-talking-postgres-simon-willison-ai]]"
---

# TDD for Agents（Agent 时代的 TDD）

> [!definition] 定义
> **TDD for Agents** 是 Simon Willison 在 Talking Postgres Ep 42 中强调的 agent 时代核心验证范式：**先写失败测试 → 让 agent 跑测试确认失败 → 写实现 → 让 agent 跑测试确认通过 → 重构**。red-green cycle 强制让 agent 跑每行代码，让"代码看起来对但未执行"的 silent failure 无法通过 review。

## TDD 红绿循环的 agent 改造

```
传统 TDD（人写代码）          TDD for Agents
─────────────────          ────────────────
红：写失败的测试             红：写测试，让 agent 跑确认失败
绿：写最小实现               绿：让 agent 写最小实现，跑测试确认
重构：清理代码               重构：让 agent 清理，跑测试确认仍绿
```

## 为什么 agent 时代更需要 TDD

- **Agent 的 silent failure 模式**: Agent 可能写出"看起来对"的实现但实际未跑过测试；reviewer 看到代码无明显 bug 直接合并——到 production 才暴露
- **TDD 把"未跑"显形**: 先写失败测试、确认失败、再实现——任何跳过测试的代码会被 red 状态卡住
- **与 file revisitation 同构**: [[Code-Cleanliness-Agent-Footprint]] 发现 file revisitation −34%；TDD 通过显式测试调用减少"先写后忘"模式

## 适用边界

- **强适用**: 纯函数、算法、数据处理、API endpoint——逻辑可单元测试
- **弱适用**: UI 改动、infrastructure-as-code、配置变更——可能需要 integration test 或 E2E test
- **不适用**: 一次性脚本、experiment 代码——TDD 成本超过价值

## 与现有 concept 的关系

- [[Agent-Verification]] — TDD for Agents 是 verification 的一种工程形态
- [[Code-Cleanliness-Agent-Footprint]] — TDD 与 clean code 同向降低 agent 操作足迹
- [[Explain-Test-Gold-Standard]] — TDD 满足"代码解释清楚"，Explain Test 满足"reviewer 理解保真"
- [[Rubric-Based-Evaluation]] — TDD 是 rubric 中 "test_coverage" / "execution_evidence" 维度的最严实现
- [[Skill-Chains]] — 可包装为 "test-first skill" 在 skill chain 中调用

## 关键数据点

- 提出者: Simon Willison（Talking Postgres Ep 42, 09:12 节）
- 与 [[Code-Cleanliness-Agent-Footprint]] 同向：file revisitation −34% 来自 minimal pair 实验
- TDD 不只适用于 unit test——[verification pipeline]([[Validation-Pipeline]]) 中的对抗审查、E2E、证据生成都属广义 TDD

## 前提与局限性

- **前提**: 代码可测试（无副作用、依赖可注入、状态可断言）
- **前提**: 测试基础设施在 agent 环境可用
- **TDD 写不好会变形式主义**: 写一堆 pass 的测试但无断言逻辑，agent 通过 TDD 但代码仍错——TDD 是必要不充分
- **成本 vs 收益**: 一次性脚本、实验代码不值得 TDD；production 代码必须 TDD
- **Agent 不能保证测试覆盖**: 即使 red-green 循环，仍可能 edge case 未覆盖；TDD 减少不消除 silent failure

## 关联概念

- [[Agent-Verification]] — TDD 是 verification 的工程实例
- [[Code-Cleanliness-Agent-Footprint]] — TDD 与 clean code 同向
- [[Explain-Test-Gold-Standard]] — TDD + Explain 是 review 双保险
- [[Rubric-Based-Evaluation]] — test execution 是 rubric 关键维度
- [[Simon-Willison]] — 概念提出者
- [[Validation-Pipeline]] — TDD 是 validation pipeline 的子集
- Verifier Mental Model（forward reference，未建 entity） — verifier 视角下 TDD 的价值