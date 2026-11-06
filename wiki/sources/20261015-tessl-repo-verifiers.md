---
type: source-summary
title: "Verifiers: enforce your repo's rules on every agent change"
canonical_url: "https://tessl.io/blog/verifiers-enforce-your-repos-rules-on-every-agent-change"
raw_state: index
original_raw_file: "20261015-tessl-repo-verifiers.md"
original_body_sha256: "88e71e3bb806c4200281f9759b627ad03cd5f3252743debbe68ffcc6f8112725"
indexed_at: "2026-11-06T08:59:07.828Z"
created: 2026-11-06
updated: 2026-11-06
tags:
  - source-summary
  - verification
evidence_level: medium
claim_type: mixed
source_locator:
  - "Why we built them / distinction between linter, code review, verifier"
  - "How they work / verifier JSON, tessl.json scope and severity"
  - "How they work / default changed files, --all, --recursive"
  - "When to use one / narrow yes-no checks"
  - "Try it / tessl install tessl/tessl-verify / tessl change verify"
  - "Where to run them / local, pre-commit, CI, warn to error"
---

# Verifiers: enforce your repo's rules on every agent change

> 一手来源：[Tessl 官方博客（2026-10-15）](https://tessl.io/blog/verifiers-enforce-your-repos-rules-on-every-agent-change)，Amy Heineike、Simon Maple。2026-11-06 已读取原文。本文为厂商机制说明，不能当作独立测量的效果或安全认证；CLI 与配置仅按原文记录，**未在本仓库安装或运行 Tessl**。

**原文保留边界**：本来源按官方稳定链接结算为可恢复索引（raw_state: index）。临时 Raw 仅为注册用来源记录，original_body_sha256 是该记录的哈希而非原网页正文哈希；不可据此宣称保存或校验了全文。须按 canonical URL 与 source_locator 回查证据。

## 编译摘要

### 1. 浓缩

- **核心结论 1：仓库规则应从写代码前的自然语言指导升级为提交后可执行的检查，但只有明确的规则才适合作为 Verifier。**
  - **原文证据**：“Why we built them”“When to use one” 指出：普通 linter 能严谨覆盖语法/确定性约束，通用 AI 代码审查不会稳定检查每个具体项目规则；Verifiers 针对“每个面向用户的错误消息是否包含下一步行动”“所有 API 路由是否使用类型化 response helper”“handler 是否记录 secrets”一类可归约为 yes/no、证据能从变更文件观察到的约束。主观的“是否可读”不适用。
  - **原则**：能够被编译器、静态分析、规则引擎或单元测试确定性验证的，不应首先使用 LLM Judge。

- **核心结论 2：Verifier 的检查契约分离 rule definition、适用作用域、严重程度与判定器。**
  - **原文证据**：“How they work” 描述 repo 内 JSON verifier（instruction、applicability、yes/no checklist），在 `tessl.json` 的 `verify.groups` 配置中声明 `path`、`include`/`exclude` 与 `level`（`info/warn/error`）；使用 `tessl change verify` 后由 LLM Judge 阅读相关文件，对各项判定 pass/fail。一般只检查当前变更触及文件；修改 verifier 或配置会重新检查适用文件；可用 `--all` 全项目检查，`--recursive` 扩展到 monorepo。
  - **运行语义**：`warn` 给出警告不阻断 CI；`error` 非零退出并可以阻断 PR。scope/level 在 verifier 之外，便于不同团队复用同一规则并选择不同门禁强度。

- **核心结论 3：逐步提高门禁强度比直接信任自动判定更合理。**
  - **原文证据**：“Try it”“Where to run them”“Get started” 提供 `tessl install tessl/tessl-verify`、`tessl change verify`，建议先在本地、pre-commit 或 CI 以 warn 观察规则效果，形成真实 PR 误报/漏报证据后再升 error；反复出现的人工 code-review 评论是优先候选规则。
  - **互补关系**：开发前的 repo rule 指导生成，开发后的 verifier 检查产物；后者不是完整的权限、安全或业务正确性证明。

### 2. 质疑

- **“deterministic checks” 的术语边界**：产品每次运行相同规则和固定范围是一种*过程重复性*，不意味着 LLM Judge 每次针对相同代码必然给出同一答案。其 false positive/false negative、模型切换与上下文差异须通过标注回归衡量；避免把模型裁判当形式化证明。
- **Oracle 权属与防篡改**：repo 内 Verifier JSON 与 `tessl.json` 同代码存放，若 Agent 可同时改代码和削弱自己所受规则，CI 通过就没有独立性。实际使用应将 verifier 更新归入受保护的 CODEOWNERS、审批及审核流程；这是**跨来源综合工程建议**，原文并未证明产品自动保证此边界。
- **局部 diff 检查的覆盖盲区**：默认仅检查修改过的文件，适合 PR 增量质量门，但跨文件的架构不变量、运行态权限、外部副作用或隐含依赖可能不在可见集内。需要周期性全量检查或更强的专项测试。
- **GA 与验证效果是不同主张**：作者称 Verifiers 在发布时已 GA；该信息只是供应商产品状态说明，不代表在本仓库验证了真实误报率、费用、时延、CLI 版本兼容性或持续可用性。
- **严重性等级不是事实等级**：设置 `error` 只决定工作流是否阻塞，不会提高 LLM 判定本身的准确性；错误的规则越严格，越会制造噪音或错误阻断。

### 3. 对标与约束（综合判断）

| 控制对象 | 优先验证手段 | Verifier 的合理位置 |
|---|---|---|
| 语法/类型/静态安全 | 编译器、lint、静态分析 | 不重复实现 |
| 可观察的项目约定 | 规则代码；实在不可表达时布尔式 LLM Judge | 作为明示的、可校准辅助门 |
| 行为正确性 | 单元、集成和真实系统回放 | 不可仅凭静态代码判断取代 |
| 权限与不可逆动作 | 模型外授权器/运行时策略 | 仅检查代码是否存在应有控制，不证明控制已执行 |
| 规则更新/评估独立性 | 独立负责人保护 golden rules | 必须与实现 PR 分离治理 |

- **与 Google 评测方案的关系**：[[20261015-google-agent-evaluation-beyond-vibe-check]] 的 boolean judge 与本篇属于相近的“可明确判断的语义检查”；但 Google 的多轮轨迹与端到端路径测试是更大的系统级验证范围，Tessl Verifiers 聚焦代码改动。
- **与现有 [[Verifiable-Agent-Engineering]] 的关系**：Verifier 只能覆盖选择了哪些可见规则；若忽视规则/Oracle 修改权限和运行时副作用，仍可能发生“同一 Agent 写实现、写测试且降低门槛”的自证循环。
- **可检验试点（建议，尚未实施）**：选 2–3 条已经多次引起 code-review 反馈、又无法由现有 linter 严格表达的 yes/no 规则；以人工标注的 PR 样本比较误报/漏报与模型成本；再决定是否设 `error` 门禁。

## 重要判断（Claim / Evidence / Boundary）

- **判断（综合）**：把项目级语义不变量编译为可执行的窄规则是一种有益工程模式，但“规则可重复运行”不能替代“判定结果可信”和“规则不受被测者篡改”。
- **证据**：本篇 “How they work”“When to use one”“Where to run them”，结合 [[Agent-Verification]] 与 [[Evaluation-Integrity]] 对 Oracle independence 的现有定义。
- **边界**：仅引用官方产品说明，未运行第三方工具，也未获得其独立误报率或安全测试。

## 关联概念

- [[Verifiable-Agent-Engineering]]
- [[Agent-Verification]]
- [[Evaluation-Integrity]]
- [[Rubric-Based-Evaluation]]
