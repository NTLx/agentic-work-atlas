---
title: "Outputs 工作流"
type: schema-subdoc
---

> 本文档是 Agentic Work Atlas Schema 子文档，由 README.md 路由表按需加载。

# Outputs 工作流

Main Agent 先确定输出对象、读者、已有 Wiki 依据、Evidence scope 和表达瓶颈，
再按 `schema/skill-mapping.md` 查看 Runtime 当前发现的 Skill 描述。Main 选择
Skill 或 `none`，若选 Skill 则读取实际 `SKILL.md` 并检查 compatibility，然后
派发一个 bounded output worker。Worker 读取必要 Wiki、读取实际 Skill（若有）、
生成内容，按允许范围写 `wiki/outputs/` 并完成回填检查。Skill output 默认是
reasoning，不能替代来源回链或 Output 回填门控。

Worker 若暴露新的不同表达或证据瓶颈，返回 `New bottleneck`；由 Main Agent
观察后决定是否 re-select 并派发 correction worker。Main 不直接替代 writer
worker 完成最终长文。

用户只要求一次性回答时，可以不写文件，也可以选择 `Skill: none`，但实际 output
execution 仍由 worker 完成。需要持久化时，只能写入本流程允许的 `wiki/outputs/`，
并遵守 Repository Schema 高于 Skill 原生 workflow 的优先级；不得因 Skill 的默认
目录或笔记行为写入无关位置。

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
