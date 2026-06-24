---
title: "Outputs 工作流"
type: schema-subdoc
---

> 本文档是 Agentic Work Atlas Schema 子文档，由 README.md 路由表按需加载。

# Outputs 工作流

| 增强 | 方式 | 效果 |
|------|------|------|
| **ljg-writes 写作引擎** | 对 Topic/Entity 观点调用 ljg-writes | 输出 wiki/outputs/ 博客/笔记 |
| **ljg-roundtable 圆桌** | 对有争议的 output 主题调用 ljg-roundtable | 多立场辩证，让 output 包含分歧而非只表达单方 |
| **ljg-plain 白话重写** | 对 Entity definition 或 output 调用 ljg-plain | 校验"12 岁可读"质量标准 |

## Output 回填门控

Agent 生成 `wiki/outputs/` 文件时，默认必须在文末加入 `## 回填检查`。若用户明确只要一次性对话回答，可不写入文件，也不需要回填检查。

输出文件还应尽量加入 `## 本文使用的 Wiki 页面`，列出实际复用的 entity、topic 或 comparison。它不是引用格式，而是复利观察点：长期被 output 复用的页面是高价值知识节点，长期不被复用的页面可能是孤岛、重复或低价值内容。

```markdown
## 回填检查

| 新判断 | 支撑依据 | 处理 |
|--------|----------|------|
| xxx | Raw: [[Source]] / Wiki: [[Some-Page]] / Agenda: [[research-agenda]] / 无 | 保留 / 升级 / 补 source / 放入 research agenda / 不处理 |
```

处理规则：
- **保留**：判断已有 entity / topic / comparison 承载，无需新增页面。
- **升级**：判断满足晋升门槛，应进入 entity / topic / comparison。
- **补 source**：判断有价值但证据不足，优先补 raw source，不直接固化。
- **放入 research agenda**：判断是问题、假设或反例方向，不能当事实使用。
- **不处理**：判断只是修辞、一次性表达或已有页面的重复说法。

支撑依据强度：
- **Raw**：一手来源或原始剪藏，可支撑事实判断。
- **Wiki**：已编译页面，可支撑内部一致性和复用判断；关键结论仍应能追溯到 raw。
- **Agenda**：只支撑“待研究问题存在”，不能支撑事实判断。
- **无**：不得升级；只能补 source、放入 research agenda 或不处理。

晋升门槛：一个 output 新判断至少满足以下三项中的两项，才允许升级为稳定 Wiki 内容。
- **可追溯**：能回链到 raw source、entity、topic 或 comparison。
- **可复用**：未来回答多个问题时会反复用到。
- **可区分**：能澄清概念边界，而不只是换一种说法。

默认保守：没有 raw source 支撑、只出现一次、只是写作修辞、或能被现有页面承载的判断，不新增页面。
