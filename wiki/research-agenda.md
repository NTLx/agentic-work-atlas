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

## 2026-05-23 第三轮探索

本轮 output 执行了第二轮提出的最小实验：抽取 output 中的 3 条关键判断，并检查它们是否有证据回链。

暴露出的问题：
- **内部实践判断缺外部支撑**：如“output 是 Wiki 的压力测试”，在本库实践中成立，但还没有一手 source 或成熟 topic 支撑。
- **研究议程本身可能变成弱证据源**：如果后续 output 频繁引用本页，本页会被误当成事实来源。需要明确：research agenda 只能支撑“我们正在研究什么”，不能支撑“事实是什么”。
- **晋升规则还缺负面样例**：当前规则能说明什么可以升级，但缺少“看似清楚但不应升级”的反例库。
- **输出后的检查动作尚未进入工作流**：现在靠人工自觉执行。若连续几次都有效，可以考虑把“三行回填检查”写入 Outputs 工作流。

下一轮最小实验：
1. 选一个非 LLM Wiki 主题做 output，例如 [[Agentic-Engineering-Patterns]] 或 [[Forward-Deployed-AI-Enablement]]。
2. 在 output 末尾加入“三行回填检查”。
3. 观察是否真的发现缺失 entity、comparison 或 source。
4. 若有效，再更新 schema；若无效，保持为临时实践。

## 2026-05-23 第四轮探索

本轮测试把新规范应用到非 LLM Wiki 主题：[[Forward-Deployed-AI-Enablement]]。

测试结果：
- **回填检查有效降低新增页面冲动**：4 条新判断中，3 条已有 topic/entity 承载，无需新增页面。
- **证伪方向暴露了真正缺口**：“标准化 SaaS agent 可能降低 FDE 重要性”目前缺少 source，应进入剪藏方向，而不是固化为结论。
- **支撑页面不等于一手证据**：回填检查能确认 Wiki 内部是否有承载页，但还不能保证判断有足够 raw source 支撑。高价值判断仍需回到 raw 或补 source。
- **模板已收紧**：回填检查从“支撑页面”改为“支撑依据”，要求标注 Raw、Wiki、Agenda 或无。
- **规则成本可接受**：三到四行回填检查不会显著增加 output 负担，但能迫使 Agent 区分表达、假设和稳定知识。

新问题：
- Output 回填检查中的“支撑页面”是否必须区分 Wiki 页面和 raw source？
- 对于策略性判断，是否应要求至少一个反例方向，才允许写入 output？
- 如果同一未验证假设在多个 output 中反复出现，应该先补 source，还是先建立 comparison？

## 待验证问题

- **编译质量如何衡量**：除了链接、frontmatter 和裸符号检查，还需要什么知识层面的质量指标？
- **输出如何反向回填**：一篇 output 中产生的新判断，什么情况下应升级为 entity、topic 或 comparison？
- **探索如何避免污染事实层**：未验证假设应保留多久，何时删除、归档或转为正式页面？
- **人类最小参与点在哪里**：人只做 source 策展和最终判断是否足够，还是必须参与每次编译摘要审查？
- **规模边界在哪里**：纯 Markdown + index 在多少页面后明显不够，需要引入混合检索或图谱加权？
- **判断如何晋升为知识**：output 中的新判断需要满足哪些条件，才能从表达性内容升级为稳定 Wiki 内容？
- **研究议程如何衰减**：长期未被 source 支撑、未被 output 使用的问题，是否应定期删除或归档？
- **探索是否需要证伪任务**：每轮 `explore(topic)` 是否都应提出至少一个反例方向，防止 Wiki 只强化既有叙事？
- **research agenda 能否作为证据源**：它只能记录问题，还是也能记录实践中的中间结论？
- **输出回填是否需要固定尾注**：每篇 output 是否都应包含“新判断 / 支撑页面 / 处理”检查表？
- **如何收集不应升级的反例**：哪些清楚、有启发的判断仍应留在 output，而不是进入稳定知识层？
- **支撑层级如何标注**：回填检查是否需要区分 raw source、Wiki 页面和 research agenda 三种不同证据强度？

## 下一批剪藏方向

- Karpathy 关于 LLM Wiki、Software 3.0、Agentic Engineering 的一手材料。
- AI Agent 开发、Agent Harness、验证、工具使用和上下文工程的一手工程实践。
- GBrain 或类似系统的工程实现细节，特别是混合检索、完整文件精读和图谱加权。
- Obsidian-Wiki / Skills 类系统如何把工作流封装成 Agent 可执行能力。
- 知识编译质量评估方法：冲突检测、证据回链、概念去重、过时判断。
- 输出驱动的 Wiki 演化案例：文章、报告或决策 memo 如何反向更新知识库。
- 标准化 AI 产品绕过 FDE 式高接触部署的反例案例。

## Source 需求队列

| 目标 | 当前缺口 | 下一步 source | 触发行动 |
|------|----------|---------------|----------|
| 验证“标准化 SaaS agent 会不会削弱 FDE” | 缺反例 | 找无 FDE、无咨询、无长期驻场，却完成核心工作流改造的企业案例 | clip 后编译到 [[Forward-Deployed-AI-Enablement]] |
| 补强 Agent Harness 作为软件工程主线 | 缺一手工程复盘 | 找 agent runtime、tool use、ACI、eval、replay、approval gate、权限边界、可观测性和失败恢复的实践文章 | clip 后编译到 [[Agentic-Engineering-Patterns]] 或 [[Verifiable-Agent-Engineering]] |
| 建立 output 回填的外部参照 | 缺一手实践 | 找团队如何用文章、报告、decision memo 反向更新知识库的案例 | clip 后更新 [[Knowledge-Compilation]] 或新建 comparison |
| 判断纯 Markdown LLM Wiki 的规模边界 | 缺工程数据 | 找 GBrain、Obsidian-Wiki 或类似系统的检索、图谱、文件精读实现细节 | clip 后更新 [[Agent-Knowledge-Management]] |
| 定义知识层面的 audit 指标 | 缺质量标准 | 找关于知识库质量、证据回链、冲突检测、概念去重的实践材料 | compile 后补充 Lint 工作流 |
| 识别不应升级的 output 判断 | 缺负面样例 | 从后续 output 中收集清楚但缺 source、只出现一次或只是修辞的判断 | 留在本页，暂不建新页面 |

## 暂不做

- 不新增 `explore/`、`audit/`、`claims/` 等目录。
- 不引入向量数据库或自动调度。
- 不为探索结果设计复杂模板。
- 不把一次性问题写成稳定知识页。
