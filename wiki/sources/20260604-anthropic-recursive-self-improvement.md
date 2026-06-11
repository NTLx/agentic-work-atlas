---
type: source-summary
title: "Anthropic：当 AI 改写 AI 自身（递归自我改进的一手数据）"
source_raw:
  - "[[20260604-anthropic-recursive-self-improvement]]"
created: 2026-06-06
updated: 2026-06-06
tags:
  - source-summary
  - recursive-self-improvement
  - agentic-engineering
  - anthropic
  - coding-agents
  - ai-deployment
---

# Anthropic：当 AI 改写 AI 自身（递归自我改进的一手数据）

## 编译摘要

### 1. 浓缩

- **核心结论 1**: 截至 2026 年 5 月，Anthropic 合并进代码库的代码 80%+ 由 Claude 写，工程师人均合并量比 2024 年涨 8 倍；2025 末"AI 代码质量差于人类"的口径在 2026 已达 parity（人类匿名打分下不可区分）
  - 关键证据: "more than 80% of the code we merge into Anthropic's codebase was authored by Claude" (Anthropic, 2026-05)
  - 关键证据: 工程师"merging 8x as much code per day as they were in 2024" (130 人样本，median 估计)
  - 关键证据: Open-ended task success rate 2026-05 达 76%，code quality parity 在 2026 年中达成
  - 关键证据: Mythos Preview 在研究判断上 64% 胜率（vs Opus 4.5 的 51%，半年涨 13 个点）

- **核心结论 2**: 任务视野（task horizon）作为 AI 能力的可信度量，从 2024-03 的 4 分钟涨到 2026-03 的 12 小时，每 4 个月翻一倍；同一时间窗 SWE-bench 与 CORE-Bench 都从个位数到接近饱和
  - 关键证据: Claude Opus 3 (2024-03) 4 分钟 → Sonnet 3.7 (2025-03) 90 分钟 → Opus 4.6 (2026-03) 12 小时
  - 关键证据: 视野翻倍意味着视野 12 月 ×8、24 月 ×64，突破"一天工作"与"一周工作"两道线
  - 关键证据: 实验执行加速：Opus 4 (2025-05) ~3x → Mythos (2026-04) ~52x（4x 人类 baseline 需 4-8 小时）
  - 关键证据: March 2026 员工调查（130 人）median 自评 4x 生产率

- **核心结论 3**: 未来三种 case（stall / compounding efficiency / full recursive self-improvement）都意味着社会必须为"AI 改 AI"做制度准备；"verifiable pause" 是 Anthropic 主张的协调机制，但作者承认 training run 比导弹井更容易隐藏
  - 关键证据: Stalls 假设算力/能量约束先绑住，capability freeze 也足以颠覆现状
  - 关键证据: Compounding case 100 人公司可干 10 万-100 万人活
  - 关键证据: Full recursive case 中 misalignment 可能"在继任模型里 compounding"
  - 关键证据: 协调机制是"verifiable slowdown or pause"，需 frontier 实验室共同承诺

### 2. 质疑

- **关于"80% 代码由 AI 写"的质疑**:
  - **边界条件**: 80% 是 commit-level，不是 deploy-level；merge ≠ production。集成之墙（legacy、SSO、权限、审计）不在 merge 数里。
  - **数据可靠性**: 数据来自单一机构（Anthropic），工具链与人才密度都是极端右尾；外推到中位软件公司前必须打折。
  - **Metric gaming 风险**: "code quality parity" 在内部评审中被打分，主观度未披露。

- **关于"任务视野每 4 月翻倍"的质疑**:
  - **外推有效性**: 视野度量建立在 SWE-bench / software 类任务；不能直接外推到物理实验、销售谈判等非软件任务。
  - **拐点风险**: 4 月翻倍是经验外推，不是物理定律——上下文长度、工具稳定性、算力上限都可能成为拐点。
  - **重复性**: Mythos Preview 是预览版，公开数据未到。

- **关于"verifiable pause"机制可行性的质疑**:
  - **作者自承**: "training runs are far easier to conceal than missile silos" — 暂停机制在技术可行性上被作者自己质疑。
  - **协调博弈**: frontier 实验室之间一旦有一家不遵守协调，单边暂停 = 战略自杀。
  - **公共选择问题**: 谁有权威和资源去做"verifiable"？监管机构对前沿训练缺乏专业能力。

- **关于"研究判断 64% 胜率"的质疑**:
  - **任务类型**: 内部研究组内的判断（"哪种优化方向更快"）≠ open-ended 基础科学问题判断（"哪个未解问题最值得追"）。
  - **样本范围**: Mythos 与 4.5 对比是版本之间，胜率定义未公开。

- **关于作者真实意图的元质疑**:
  - 这篇博文是技术报告还是机构对监管的策略性喊话？把对齐放在第三种未来的脚注里、不当主标题——这种"机构克制"是有意为之，让监管者读起来觉得"他们在自我反思"，又让算力扩张派读出来"反正还是要扩"。

### 3. 对标

- **跨域关联 1 (与历史比较)**: 任务视野每 4 月翻倍 = 软件工程的"摩尔定律"——和 1965 年摩尔本人预测晶体管密度每 18-24 月翻倍不同，AI 时代"翻倍"是产品能力，不是物理参数；可与早期 Moore's Law 在 CPU 上的对等冲击对照。
- **跨域关联 2 (与组织经济学)**: 工程师 8x 写码但团队规模不变——R&D 成本结构从"工资主导"变成"算力主导"，可对照 1990s 制造业的"机器人替代蓝领"在白领研发上的版本；类比软件业自身的"开源吞噬专有软件"。
- **跨域关联 3 (与制度设计)**: "verifiable pause" 机制在 AI 上的可行性可对标核不扩散（NPT）的国际核查机制；NPT 跑了 50+ 年仍有薄弱处（朝鲜、伊朗），AI 训练的"代码可隐藏"特性比核弹更难核查。

### Q-A 深度骨架

完整 Q-A 链见 `~/Documents/notes/20260606T202733--qa-anthropic-recursive-self-improvement__qa.md`，核心 8 个 Q：

1. **Anthropic 拿什么证据说 AI 已经在改 AI？** — 三组独立数据交叉验证：生产端（80%）、质量端（parity）、研究端（64%）
2. **为什么作者把"研究判断"也单列出来？** — AI 越过执行边界，开始反超"哪个问题值得做"
3. **任务视野每 4 月翻倍意味着什么？** — 这是"AI 时代的摩尔定律"，过滤掉 benchmark 噪音
4. **三个未来场景为什么不是预测而是策略性框架？** — 公共子集是"verification 必须现在做"
5. **80% 代码由 AI 写 ≠ 80% 软件由 AI 写** — 差距在 verification 和 integration
6. **工程师 8x 但团队规模不变意味着什么？** — R&D 成本结构从工资主导变算力主导
7. **作者为什么把"alignment 不确定性"放在脚注？** — "机构自我克制"是有意为之
8. **8x 工程师 + 64% 判断胜率，人类剩余比较优势在哪？** — 选题 + 拒绝 + 责任

### 关联概念

- [[Recursive-Self-Improvement]]
- [[Anthropic]]
- Marina-Favaro
- Jack-Clark
- [[Anthropic-Institute]]
- [[Task-Horizon]]
- [[AI-Psychosis]]
- [[AI-Capability-Gap]]
- [[Coding-Agents]]
- [[Agentic-Engineering]]
- [[AI-Labor-Bottleneck-Shift]]
- [[Allocation-Economy]]
- [[Verifiability]]
- [[Agent-PR-Review]]
- [[Research-Taste]]
