---
type: source-summary
title: "How we found 24 Android vulnerabilities using our open source AI security agent"
canonical_url: "https://github.blog/security/how-we-found-24-android-vulnerabilities-using-our-open-source-ai-security-agent/"
original_raw_file: "20260928-github-android-ai-security-agent.md"
body_sha256: "8a928036a410016320449d0dbb953bee13de16f12bcaa1b664643c51c03f8417"
indexed_at: "2026-10-12T15:17:05+08:00"
raw_state: index
created: 2026-10-12
updated: 2026-10-12
tags:
  - source-summary
  - agentic-security
  - agent-harness
  - vulnerability-research
  - verification
evidence_level: high
claim_type: mixed
source_locator:
  - "Creating targeted audit taskflows for Android apps"
  - "Two examples of vulnerabilities found by the taskflows"
  - "LLMs are good at finding vulnerabilities but struggle at estimating severity"
  - "LLMs have great knowledge of API behavior"
  - "Notes on the results"
---

# How we found 24 Android vulnerabilities using our open source AI security agent

> GitHub Security Lab 的一手工程复盘。Kevin Stubbings 描述如何在开源 Taskflow Agent 上增加 Android 专用审计流程，并报告截至文章写作时共发现并提交 24 个 Android 漏洞。来源公开完整正文和具体已披露案例，适合支持 taskflow 设计与验证边界；但没有给出与人工审计或其他 Agent 的受控 benchmark、precision/recall 或完整发现分布，因此不能把“24 个发现”直接解释为相对效率倍数。

## 编译摘要

### 1. Domain-specific taskflow 的价值是把 threat model 外置成可执行搜索结构

通用审计 taskflow 已能分析代码，但 Android 有 exported activity、intent、deeplink、WebView、跨组件调用等特定 attack surface。作者因此没有只靠更长 prompt，而是把流程拆成至少两类显式阶段：先识别/分类 mobile entry points，再针对每个 entry point 与 component 引入移动端常见 vulnerability classes。

**判断**：在高专业度安全任务中，Harness 的核心增益之一是把专家的 **attack-surface decomposition + vulnerability taxonomy + search order** 从研究者脑内经验变成可执行 taskflow。模型能力决定搜索上限，taskflow 决定它是否系统性覆盖关键面。

这可以抽象成：

```text
repository
  → entry-point inventory
  → domain-specific attack-surface classification
  → vulnerability-class priors
  → candidate findings
  → exploitability / impact evidence
  → expert adjudication
```

这与此前 GitHub Security Lab fuzzing 来源的 coverage-feedback loop 互补：fuzzing source 证明 Harness 能围绕客观 coverage 信号持续迭代；本来源证明静态/逻辑审计还需要把**领域 threat model**编码进搜索过程。

### 2. Strict prompt + broad prompt + repeated runs 是对非确定性的结构化利用

作者同时运行更严格的 checklist-style prompt 和更开放的 broad prompt，并进行多次运行：严格约束用于降低常见漏洞类别的漏检，开放提示则保留模型跨组件联想和发现非模板化逻辑问题的空间。

**判断**：这里不是简单的“多跑几次提高概率”，而是一种轻量 **search ensemble**：

- strict branch 优先 coverage / recall of known classes；
- broad branch 优先探索未知组合；
- repeated runs 用来对冲 LLM nondeterminism；
- 后续 evidence stage 再压缩候选集合。

因此，在探索型 Agent 上，确定性不一定来自把模型变成单一路径；也可以来自让**搜索路径多样化，而让最终证据门更严格**。

**边界**：文章没有报告每个 branch 的独立贡献、run 数与 marginal yield，也没有漏报基准，因此不能量化 ensemble 的增益。

### 3. “能发现漏洞”与“能判断 severity”是两个不同能力

文章最重要的负面结果是：LLM 经常能指出真实代码弱点，却会高估实际影响，尤其在漏洞是否真正可利用取决于 runtime state、storage precedence、调用链或其他 mitigating factors 时。作者举例说明，一个表面可控的数据路径可能最终被内部状态覆盖，从而根本不形成有效漏洞。

作者因此要求进一步让模型构造 proof of concept，必要时给它 debugger 来运行 PoC 与原始代码；即便如此，仍要求熟悉 mobile security 的研究者复核每个 finding。

**判断**：安全 Agent 的验证链应至少拆成：

```text
code pattern / candidate bug
    ≠
reachable exploit
    ≠
real-world impact
    ≠
severity
```

模型在第一层表现好，不能自动继承到后三层。Severity 是一个依赖环境状态、mitigation、可达性和受影响资产的**系统级判断**，比模式匹配更接近 executable evidence 问题。

### 4. PoC 的主要作用不是“证明模型会攻击”，而是把 claim 推向可执行反证

显式要求 PoC 会迫使模型把漏洞报告中的假设落到具体 execution path；debugger / original code 则让系统能够观察实际状态，而不是只基于静态代码想象影响。

**判断**：在 Agent verification 中，PoC 可以被视为一种 **evidence escalation primitive**：当候选结论后果高、静态证据不足时，验证要求从文本论证升级为可运行实验。

这与软件工程中的 test、科学 Agent 中的 experiment、形式验证中的 proof kernel 属于同一结构：让 claim 接触一个比生成者自身叙述更难伪造的外部 oracle。

**边界**：PoC 仍可能只覆盖特定路径；测试环境与真实设备状态可能不同，成功 PoC 也不自动给出完整 CVSS / business impact。人类专业判断仍是最终 severity adjudication 的重要组成。

### 5. 24 个漏洞说明真实产出存在，但不足以证明 Agent 相对人类的效率

文章报告截至写作时已发现并报告 24 个 Android 漏洞，其中包含若干 critical findings，并展示 OsmAnd 与 Wikipedia Android 的已披露逻辑漏洞案例。案例支持 LLM 不只会找机械型 pattern bug，也可以跨组件组合逻辑与 API semantics。

同时文章也明确承认：

- 会返回现实中极难满足前提的候选；
- 会持续报告低 severity finding，即使 prompt 要求忽略；
- severity 经常判断错误；
- 复杂运行时状态会制造 false positive；
- 需要额外模型调用、PoC/debugger 与人工复核。

因此更稳妥的结论是：**Taskflow Agent 已经能成为安全研究者的高吞吐候选生成与调查工具，但本文没有证明它可以替代资深移动安全研究者，也没有证明单位时间/成本优于人工或其他自动化方案。**

## 与现有知识的连接

- **[[Agent-Harness]]**：新增“domain threat model as executable harness”。Harness 不只负责工具和状态，也可以编码 attack surface、漏洞 taxonomy 与搜索分支。
- **[[Agent-Verification]]**：新增 candidate finding → PoC/runtime evidence → severity adjudication 的证据升级链；finding confidence 与 impact confidence 必须分开。
- **[[20260924-github-security-lab-ai-fuzzing-taskflow]]**：前一来源偏动态 fuzzing 的 coverage loop；本来源偏 Android 逻辑审计与 severity calibration，两者共同显示安全 Agent 的价值来自 domain scaffold + objective evidence，而不是裸模型单轮审计。

## 证据边界

- GitHub Security Lab 第一方案例，Taskflow Agent 开源，正文公开完整。
- “24 vulnerabilities”是作者报告的累计发现数，不是受控实验结果；文章没有给出总扫描仓库数、人工基线、false-negative denominator、平均 token 成本或每个漏洞的人类投入。
- 两个公开案例证明 capability existence，不代表随机 Android repo 上的总体 detection rate。
- 作者关于未来模型 context/reasoning 改善会降低 false positive 的判断属于预测，不是本文验证结果。
