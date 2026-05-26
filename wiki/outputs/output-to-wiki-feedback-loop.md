---
type: output
title: "从 Output 到 Wiki：新判断如何回填"
created: 2026-05-23
updated: 2026-05-25
tags:
  - output
  - llm-wiki
  - knowledge-compilation
---

# 从 Output 到 Wiki：新判断如何回填

> [!summary] 核心判断
> Output 不是终点，而是 [[LLM-Wiki|LLM Wiki]] 的压力测试。它会暴露哪些判断已经被 Wiki 支撑，哪些判断只是临时表达，哪些判断值得升级为稳定知识。

## 为什么需要回填规则

上一轮 output 已经能说明 [[LLM-Wiki|LLM Wiki]] 和 RAG 的范式差异：RAG 在查询时临时理解材料，LLM Wiki 在摄取时把材料编译为可复用的知识中间层。

但这篇 output 同时暴露了一个问题：文章中会自然产生新判断。如果这些判断全部留在 output 里，Wiki 的稳定知识层不会变厚；如果全部升级为 entity 或 topic，Wiki 会被一次性观点污染。

所以需要一条极简规则：

> Output 中的新判断，先检查证据回链；只有稳定、可复用、被 source 支撑的判断，才进入 entity、topic 或 comparison。其余留在 research agenda。

## 三条判断回链检查

| 判断 | 当前支撑 | 处理 |
|------|----------|------|
| RAG 的问题不是检索，而是没有积累 | [[RAG-vs-LLM-Wiki]]、[[Agent-Knowledge-Management]] 已明确区分实时检索与持久编译 | 可保留在现有 comparison/topic，无需新页面 |
| Output 是 Wiki 的压力测试 | 目前主要来自本轮实践和 [[research-agenda]]（研究议程），缺少外部 source 支撑 | 继续留在 research agenda，不升级 |
| 好的查询答案可以回填为新的 Wiki 页面 | [[Knowledge-Compilation]] 已有 `Query → Answer → File back to Wiki → Compounding` 机制 | 可作为回填规则的基础，暂不新增 Entity |

这次检查说明：不是所有清楚判断都值得升级。第一条已经有承载页；第二条还只是实践假设；第三条已有机制基础，但还缺操作标准。

## 晋升规则草案

一个 output 判断要升级为稳定 Wiki 内容，至少满足三项中的两项：

1. **可追溯**：能回链到 raw source、entity、topic 或 comparison。
2. **可复用**：未来回答多个问题时会反复用到。
3. **可区分**：能澄清一个概念边界，而不只是换一种说法。

升级位置按问题类型决定：
- 如果判断定义一个概念，进入 entity。
- 如果判断整合多篇材料，进入 topic。
- 如果判断区分两个相近概念，进入 comparison。
- 如果判断只是提出问题、反例或待验证假设，留在 research agenda。

## 反向风险

回填机制也有风险。最危险的不是遗漏，而是把表达性判断过早固化成事实。

因此，output 回填应默认保守：
- 没有 source 支撑，不升级。
- 只出现一次，不升级。
- 只是写作修辞，不升级。
- 能被现有页面承载，不新增页面。

这符合本库的极简原则：让 Wiki 增厚，而不是让目录膨胀。

## 下一步

最小可行改进不是写脚本，而是在未来每次 output 后追加一个三行检查：

| 新判断 | 支撑页面 | 处理 |
|--------|----------|------|
| Output 是 Wiki 的压力测试 | [[research-agenda]] | 放入 research agenda |

如果这个动作连续多次有用，再考虑把它写入 schema 或工具。

## 本文使用的 Wiki 页面

- [[LLM-Wiki]]
- [[RAG-vs-LLM-Wiki]]
- [[Agent-Knowledge-Management]]
- [[Knowledge-Compilation]]
- [[research-agenda]]

## 回填检查

| 新判断 | 支撑依据 | 处理 |
|--------|----------|------|
| Output 中的新判断需要先做证据回链检查 | Wiki: [[Knowledge-Compilation]]；Schema 回填规则 | 保留 |
| Output 是 Wiki 的压力测试 | Agenda: [[research-agenda]] | 放入 research agenda |
| 晋升至少需要可追溯、可复用、可区分中的两项 | Schema 回填规则 | 保留 |
