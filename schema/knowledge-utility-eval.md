---
title: "Knowledge Utility Eval（知识效用评测）"
type: schema-subdoc
---

> 本文档是 Agentic Work Atlas Schema 子文档，由 README.md 路由表按需加载。

# Knowledge Utility Eval（知识效用评测）

## 目的

LLM Wiki 需要同时回答两个不同问题：

- **Control Plane**：仓库有没有坏？由 lint、schema、registry、provenance、Raw lifecycle 等机制回答。
- **Value Plane**：已有知识是否真的让后续问题更容易被找到、综合和复用？由本评测回答。

`lint = 0` 只能证明结构约束通过，不能证明知识产生了增量价值。反过来，某次回答很好也不能替代 provenance、Raw lifecycle 或 lint。

本评测不是第五个 Wiki lifecycle，也不是日常 clip / compile 的完成门；它只用于周期性检查知识库是否在产生真实复利。

## 三个维度

### Find：能否找到已经知道的东西

评估固定问题进入 `schema/query-workflow.md` 后，Agent 是否能以 search-first 和 bounded context 找到最小充分的已有知识，而不是重新从外部研究。

评分：

- `0`：Wiki 已有直接知识，但没有找到，或绕开 Wiki 重新研究后给出答案。
- `1`：找到部分相关页面，但遗漏关键页面、上下文明显过宽，或没有保留必要的 evidence boundary。
- `2`：找到最小充分页面，并能指出来源、边界或当前缺口。

### Synthesize：能否把分散知识组合成新的判断

评估跨 Topic / Entity 的真实问题。重点不是“引用了几个页面”，而是能否把关系、约束、反例和边界组合起来。

评分：

- `0`：基本由单一页面作答，或产生无依据的新判断。
- `1`：使用多个页面，但主要是并列摘要，关系与边界较弱。
- `2`：跨页面形成可追溯综合，明确说明关系、冲突、条件或限制，且不把 Reasoning 冒充 Evidence。

### Reuse：后续产物是否真正复用了已有知识

Reuse 不以“链接数量”充当价值本身。评估一个时间窗口内的实际 Output / 持久化产物：

- `0`：已有相关稳定知识却基本没有被使用，重复研究或重复造页明显。
- `1`：存在实际复用，但追踪不完整，或复用主要停留在引用层，尚未明显减少重复研究、提高综合质量。
- `2`：多数抽样产物能复用已有稳定页，且复用对检索范围、综合质量或新增知识判断产生了可观察影响。

同时记录 `reuse_trace_coverage`：窗口内有多少持久化 Output 显式包含 `## 本文使用的 Wiki 页面`。它只是**可观察性指标**，不能被解释成真实复用率。

## 固定问题集

固定问题位于：

`evals/knowledge-utility/cases.yaml`

规则：

1. Full run 使用全部 20 个固定 case；Smoke run 可使用 6 个代表性 case。
2. 回答阶段只把 `query` 提供给 answering context；`reference_anchors` 与 `success_condition` 只供评估阶段使用，避免把答案路径直接提示给回答者。
3. 默认**禁止外部联网补证据**。评测测的是 Wiki 自身效用；如果 Wiki 证据不足，正确行为是明确说不足，而不是临时去 Web 补齐。
4. 固定集不随一次失败立即改写。只有 case 已明显脱离主线、知识边界发生实质变化，或连续多轮证明 case 设计失真时才调整，并说明原因。

## 运行与记录

默认每月做一次 Full run；当 query/output schema 有实质变化时可额外执行 Smoke run。不要为每次 clip / compile 单独运行。

记录写入：

`state/knowledge-utility/YYYY-MM-DD.md`

每次记录至少包含：

```markdown
# Knowledge Utility Eval · YYYY-MM-DD

- mode: smoke | full
- wiki_revision: <git commit>
- external_web: disabled

## Find
| case | score | evidence | failure |

## Synthesize
| case | score | evidence | failure |

## Reuse
- window: ...
- score: 0 | 1 | 2
- reuse_trace_coverage: X / Y
- evidence: ...
- limitation: ...

## Delta
- compared_with: ...
- improved: ...
- regressed: ...
- action: ...
```

只保留三个维度，**不计算总分**。把 Find / Synthesize / Reuse 合成单一 KPI 会重新制造 Goodhart 风险，也会掩盖“检索很好但复用很差”这类结构性问题。

## 如何使用失败

一次失败先定位到知识系统问题，不直接增加 Schema：

- **Find 失败**：先检查命名、aliases、Topic/Entity 边界、search-first 是否能命中；只有重复失败才考虑结构调整。
- **Synthesize 失败**：先检查稳定页之间是否缺少关系、边界或反例，而不是立即新增总览页。
- **Reuse 失败**：先检查 Output 是否真的需要已有知识、查询是否先读 Wiki、是否存在重复页面；不要用强制增加 wikilink 数量来“修复”。

只有同类失败在多轮评测或多个 case 中重复出现，才值得修改 Schema、索引或知识结构。

## 反代理指标原则

以下指标可以帮助诊断，但都不能单独证明知识效用：

- lint 通过率
- Entity / Topic 数量
- wikilink 数量
- Raw 数量
- `## 本文使用的 Wiki 页面` 覆盖率
- 单次回答读取页面数

评测的最终问题始终是：**已有知识是否减少了重复研究，并让真实问题得到更快、更完整、更有边界的回答。**
