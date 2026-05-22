---
type: research-agenda
title: "LLM Wiki 研究议程"
created: 2026-05-22
updated: 2026-05-23
tags:
  - research-agenda
  - llm-wiki
  - knowledge-management
related_entities:
  - "[[LLM-Wiki]]"
  - "[[Knowledge-Compilation]]"
  - "[[RAG-vs-LLM-Wiki]]"
  - "[[Agent-Knowledge-Management]]"
---

# LLM Wiki 研究议程

> [!note] 使用边界
> 本页只记录未验证问题、反例和下一轮剪藏方向，不作为事实页。稳定结论应回填到 entity、topic 或 comparison。

## 本次探索结论

当前 Wiki 已能支撑一个基本判断：LLM Wiki 的核心不是“用 LLM 查资料”，而是把 raw source 编译成可复用的知识中间层。

还不足的是：四动作模型里的 `produce(query)` 和 `explore(topic)` 样本太少，尚不能判断它们是否能长期稳定地产生高价值输出和好问题。

## 2026-05-23 第二轮探索

这次探索从上一轮 output 反推：`produce(query)` 已经能生成清楚文章，但文章中的新判断目前还缺少明确的回填规则。

核心判断：
- **探索不应只是发散**：好的 `explore(topic)` 应该产出可验证问题、下一步 source 选择、以及是否需要升级为正式 Wiki 页面。
- **output 是压力测试**：如果 output 中出现清楚但无回链的判断，说明 Wiki 还缺证据页、comparison 或 topic 承载。
- **research agenda 是缓冲层**：未验证问题先进入本页；只有被 source 支撑、被多次使用或能稳定解释多个材料时，才升级为 entity、topic 或 comparison。
- **当前最大缺口不是目录，而是晋升规则**：什么时候把一个问题保留、删除、合并或升级，还没有稳定标准。

本轮产生的最小实验：
1. 选取一篇 output。
2. 抽出其中 3 条关键判断。
3. 逐条检查是否能回链到 entity、topic、comparison 或 raw source。
4. 对无支撑但有价值的判断，决定是补 source、补 comparison，还是保留在研究议程。

## 待验证问题

- **编译质量如何衡量**：除了链接、frontmatter 和裸符号检查，还需要什么知识层面的质量指标？
- **输出如何反向回填**：一篇 output 中产生的新判断，什么情况下应升级为 entity、topic 或 comparison？
- **探索如何避免污染事实层**：未验证假设应保留多久，何时删除、归档或转为正式页面？
- **人类最小参与点在哪里**：人只做 source 策展和最终判断是否足够，还是必须参与每次编译摘要审查？
- **规模边界在哪里**：纯 Markdown + index 在多少页面后明显不够，需要引入混合检索或图谱加权？
- **判断如何晋升为知识**：output 中的新判断需要满足哪些条件，才能从表达性内容升级为稳定 Wiki 内容？
- **研究议程如何衰减**：长期未被 source 支撑、未被 output 使用的问题，是否应定期删除或归档？
- **探索是否需要证伪任务**：每轮 `explore(topic)` 是否都应提出至少一个反例方向，防止 Wiki 只强化既有叙事？

## 下一批剪藏方向

- Karpathy 关于 LLM Wiki、Software 3.0、Agentic Engineering 的一手材料。
- GBrain 或类似系统的工程实现细节，特别是混合检索、完整文件精读和图谱加权。
- Obsidian-Wiki / Skills 类系统如何把工作流封装成 Agent 可执行能力。
- 知识编译质量评估方法：冲突检测、证据回链、概念去重、过时判断。
- 输出驱动的 Wiki 演化案例：文章、报告或决策 memo 如何反向更新知识库。

## 暂不做

- 不新增 `explore/`、`audit/`、`claims/` 等目录。
- 不引入向量数据库或自动调度。
- 不为探索结果设计复杂模板。
- 不把一次性问题写成稳定知识页。
