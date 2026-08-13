---
type: source-summary
title: "Your contributors are AI-first now. Is your project?"
source_raw:
  - "[[20260812-github-ai-first-contributors]]"
created: 2026-08-13
updated: 2026-08-13
tags:
  - source-summary
  - agent-generated-prs
  - contributor-governance
  - open-source-maintenance
evidence_level: medium
claim_type: mixed
---

# Your contributors are AI-first now. Is your project?

> 来源：GitHub 官方博客（2026-08-12），作者 Andrea Griffiths，核心受访者为 AutoGPT 创始 AI 工程师 Nicholas Tindle。**evidence_level 取 medium**：一手项目内部叙事，机制层（AGENTS.md 目录作用域、skill 发现、五类 gate）可对照 AutoGPT 仓库独立验证，但全部成效数据（80 万 star、150 open PRs、800 contributors）均为自报、无独立审计；主张多为口述经验而非对照实验。

## 编译摘要

### 1. 浓缩
- **核心结论1：文档不是问题，发现（discovery）才是**——agent 不会主动去读 contributor docs，只读"面前的东西"（当前工作目录层级）。AutoGPT 的应对：先铺 `CLAUDE.md`（因 Claude 缺仓库上下文），再因 Copilot/Codex 忽略 Claude 文件而集中到中央 `AGENTS.md` 并让 Claude 文件指向它。关键机制：`AGENTS.md` 按**目录作用域**，而 skill 可跨目录发现——skill 的 description 被 agent 在启动时预扫描，任务匹配时拉入完整指令，因此 skill 可以告诉 agent"该去哪个目录找 AGENTS.md"。
  - 关键证据: "Agents read what's in front of them, at the level of the directory they're working in"；前端工程师把"组件在这些文件夹里就要写 Storybook 测试"的 guide 做成 skill 后所有 harness 自动发现；后端用同构规则"80% 覆盖否则别开 PR"。
- **核心结论2：门禁（gates）是最低成本的行为修正杠杆，且规则先于自动化改变行为**——AutoGPT 的五类 gate：① PR 模板强制（"不符合模板自动关闭"——自动化还没跑，agent 行为已被改变；人类不按模板反而被识别为"真人"受宽容）② test plan 措辞触发 `test PR` skill（agent 为填 checkbox 自动装 agent browser、起 app、真跑代码）③ CI 当墙（Codecov 覆盖率作为 required check，agent 自己回读失败、加载测试 skill 补测试）④ CLA 当人形探测器（浏览器 + OAuth 单独域，agent 难通过；一周不签就关 PR）⑤ review thread 必须以修复 commit 的 SHA 才能 resolve（`pr-address` skill 声明 fix→commit→push→reply→resolve 序列，SHA 从 `git rev-parse HEAD` 取，反"acknowledged 不算修复/引用无关 commit"）。
  - 关键证据: "the rule changed agent behavior before the automation ever ran"；"If you don't follow the template, I know you're probably a person, and I'm going to be kinder"；"an agent that marks every review thread as resolved without touching the code"。
- **核心结论3：治理的关键是克制**——把失效的自动化关掉（第一版把 Claude Code 接进 GitHub Actions 做失败旁白 bot，因 CI 常挂、"bot 全天复读失败不比失败本身好"而关停，且顺带避免 CI 里多一个宽凭据）；拒绝合并是合法选择（合入他人 LLM 输出是不对称成本：upkeep 永远归你；SQLite 只收 bug report 是合法的开源边界）；关闭时要重建的 PR 可加贡献者 co-author。
  - 关键证据: "It's basically somebody else paying for your compute"；"Closing the pull request and building the fix yourself is a legitimate choice"；四个 gotcha（bad AGENTS.md worse than none、GraphQL rate limit 需 GitHub App、八 agent PR 测试 rig 贵到只对很小/很大的 PR 跑、授权 apps 需定期审计）。

### 2. 质疑
- **关于"结论1"的质疑**：AGENTS.md 小项目可迁移性存疑——机制预设了 harness 支持 AGENTS.md 级联注入、agent 尊重目录作用域；复制到非 GitHub 生态/不同 harness 时发现机制不保证。AutoGPT 曾在全库铺 AGENTS.md 导致上下文污染（"bad AGENTS.md worse than no AGENTS.md"），说明这是成本敏感、反直觉的实践——小项目按"写更全的 docs"直觉去做很可能适得其反，收益/成本比未必为正。
- **关于"结论2"的质疑**：门禁的"规则先于自动化改变行为"依赖 agent 贡献者被工具生态驱动、有较强规范遵循动机；对低动机的 drive-by 贡献者，模板外 PR 会把识别逻辑推向"非模板=真人=更宽容"——这与"把关"目标存在张力，且 AI 工具链一旦学会 OAuth 浏览器流，CLA 人形探测器时效有限。gate 栈本身有维护债（GraphQL rate limit 需 GitHub App、授权 apps 需定期清理）。
- **关于"结论3"的质疑**：全部成效数据自报、无独立验证（150 open PRs / 800 contributors / PR 测试 rig 成本）；"规则先于自动化"是事后叙述，存在合理化痕迹；"合入是只读、关掉重建是合法"是维护者视角断言，未考虑对 AI 贡献生态的寒蝉效应（前文又说要 KPI 面包屑式的善意）。
- **关于边界的质疑**：文中的"维护者 knobs"（disable PRs / restrict issue creation）是 GitHub 平台 2026 新控制，属于平台侧治理，与小项目治理的复制无关——文末也承认"nobody's landed on the right shape yet"。

### 3. 对标
- **跨域关联1（综合判断）**：AutoGPT"把指令放到 agent 会看的地方 + skill description 预扫描"与 [[Skills-as-Products]]（Google Agent Skills 的 SKILL.md 标准化、description 引导装载）是同一机制的两种工程化——规则从"给人读的文档"变成"机器可触发、可被发现的行为资产"，是 [[Thin-Harness-Fat-Skills]] 与 [[Progressive-Disclosure]] 的实现实例。
- **跨域关联2（综合判断）**：五类 gate = [[Policy-as-Code-for-Agent-Governance]] 的开源实践条目；"CI 当墙（覆盖率为 required check）"与 [[Secure-Paved-Path]]"让正确方式成为最容易的方式"同构——把文化规则物理化为墙，而不是依赖自觉。
- **跨域关联3（综合判断）**：`pr-address` skill 反"review thread 假 resolve"直击 [[Agent-PR-Review]] 的 Agent Ghosting 检查点，是防幽灵的机制化方案；"引用的 fix commit 必须 link 被改行"是防 recycle 的 anti-spoofing，与 [[Agent-Verification]] 的"独立验证者要有真正独立目标"同源的轻量版。
- **跨域关联4（综合判断）**："合入别人 LLM 输出是不对称成本（upkeep 永远归你）"把 [[Agent-Generated-PRs]] 的"AI 代码 60 分钟存活率 vs 长期维护债"落成维护者操作准则；"close + co-author"是对 [[Human-Signal]] 的善意补偿。
- **约束分析（3c）**：硬约束——agent 只读工作目录层面的东西，指令必须物理上放在 agent 在场处（工具行为是世界的规律）；软约束——哪些规则进 AGENTS.md/skill、哪些进 CI 墙、哪些直接关闭，是项目自设策略；自设约束风险——"bad AGENTS.md worse than none"提醒治理资产本身会腐烂，需持续审计（对应"go audit your authorized apps"）。

### 关联概念
- [[AGENTS-md]]
- [[Agent-Generated-PRs]]
- [[Agent-PR-Review]]
- [[Skills-as-Products]]
- [[Policy-as-Code-for-Agent-Governance]]
- [[Secure-Paved-Path]]
- [[Agent-Verification]]
- [[Thin-Harness-Fat-Skills]]
- [[Human-Signal]]