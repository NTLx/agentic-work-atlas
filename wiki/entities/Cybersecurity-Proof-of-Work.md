---
type: entity
title: Cybersecurity Proof of Work
aliases:
  - Cybersecurity Proof of Work
  - 安全 Proof of Work
  - Security as Proof of Work
definition: "Drew Breunig提出的安全经济学类比：自动化搜索预算可能影响攻防，但安全结果还依攻击面、验证、修复、控制和实际部署；非计算量决定安全性的定律"
created: 2026-04-21
updated: 2026-11-28
tags:
  - cybersecurity
  - ai-security
evidence_level: medium
claim_type: mixed
related_entities:
  - '[[Drew-Breunig]]'
  - '[[Mythos]]'
  - '[[Security-Hardening-Phase]]'
  - '[[Agentic-Engineering]]'
  - '[[AISI]]'
  - '[[Verifiable-Agent-Engineering]]'
source_raw:
  - "[[20260414-cybersecurity-proof-of-work]]"
  - "[[20260727-hf-agent-intrusion-technical-timeline]]"
  - "[[20260822-just-a-rumour-of-a-bug]]"
---

# Cybersecurity Proof of Work

> [!definition] 定义
> Drew Breunig (2026) 提出的概念：网络安全变成 token 成本博弈，作者假设防御方可能需要更高搜索预算以取得优势。不是必要或充分条件，也不能由单个实验推出预算均衡。

## 关键数据点

- **作者假说（非方程或经验证定律）**: "to harden a system you need to spend more tokens discovering exploits than attackers will spend exploiting them"
- **成本基准**: AISI TLO实验设置100M Token预算上限；`$12,500`是Breunig的历史费用估算，不是AISI实付、统一单价或2026-11现价
- **测试结果**: Mythos Preview在AISI TLO受控模拟中3/10完整完成，平均22/32评分步骤；20小时为作者对人类的估计而非匹配对照
- **边际收益**: 在所测至100M Token预算范围仍观察到进展，不证明没有边际收益递减或无限扩展
- **工程推论**: 防御者不能只问“有没有安全审计”，还要问“覆盖了哪些风险、证据是否可靠、修复是否验收、剩余风险是多少”；预算是资源约束而非安全指标
- **组织推论**: 部分安全检查可成为可预算、重复与比较的工作流；专家分析、风险判断及修复验证仍重要

## 传言驱动的 exploit 搜索（2026-08-22 编译新增）

Anil Madhavapeddy 记录的 cohttp 修复显示，防御侧风险分析还需考虑从披露到实际缓解生效的延迟：作者在公开 PR 后约十分钟观察到对应探测，并用 Agent 在不到一分钟内构造了可探测本地服务的 exploit。文章引用的基准还显示，早期[研究摘要](https://arxiv.org/abs/2404.08144)报告15个已知漏洞的特定评测中，两种信息条件下结果为87%和7%；不同模型、样本和真实环境不可直接外推。

**判断**：当 Agent 能读代码、运行实验时，安全问题的粗粒度传言就可能成为 exploit 搜索入口，防守方可能面临验证、修复、打包和发布吞吐瓶颈，需结合真实缺陷与发布流程测量。

- **证据**：[[20260822-just-a-rumour-of-a-bug]]
- **边界**：这是单点维护者观察与特定基准共同支持的机制判断，不足以证明所有公开 PR 的探测都由 Agent 触发，也不能推出所有漏洞只靠模糊线索即可利用。

## 前提与局限性

- **前提**: 
  1. 在给定任务及工具条件下，额外搜索预算可能提高发现率；需要实测增量收益
  2. Tokens 成本相对稳定或下降
  3. 攻击者预算还受动机、能力、组织、目标和风险影响，市场价值不是唯一上限
- **局限性**: 
  1. 推理成本变化可能改变博弈规则
  2. 真实攻击场景比测试更复杂
  3. 未考虑新型防御技术（如 AI 检测 AI 生成的攻击）

## 证据与实践边界（2026-11-28）

回核[AISI 4月评测](https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities)图3及Implications，100M为上限、不同模型运行数不一，模拟环境缺少主动防御及常见防护，另一OT场景未完成；不据此推断生产攻防胜负。Drew Breunig原文是观点（见[[20260414-cybersecurity-proof-of-work]]）。

**本库综合**：预算应优先用于高风险暴露面、可验证的控制缺口和可靠修复；追踪经验证发现、实际缓解覆盖、修复后残余风险和重复发现率，按风险及增量价值停止或继续，而不是追求比假想攻击者消耗更多Token。发现、修复、发布、实际生效分别验收。未复跑评测或独立测量生产收益。

## 关联概念

- [[Drew-Breunig]] — 提出者
- [[Mythos]] — Anthropic通用前沿模型及后续受限模型家族
- [[Security-Hardening-Phase]] — 作者建议的安全硬化阶段，非强制顺序
- [[Agentic-Engineering]] — 受影响的编程范式
- [[AISI]] — 提供 Mythos 攻击任务评测的机构
- [[Verifiable-Agent-Engineering]] — 把安全搜索变成可预算、可审计的验证边界

## 跨域对标

| 类比 | 原域 | 映射 |
|------|------|------|
| **加密货币 Proof of Work** | 比特币挖矿 | 算力投入是影响搜索机会的因素；不建立漏洞发现概率线性关系 |
| **Linus's Law 扩展** | 开源软件 | "eyeballs + tokens = shallow bugs" |

## 实践影响

1. **开源软件仍然重要**: 共享审计及维护可能产生复用收益；开源与自建的安全性需按维护、依赖、部署和响应比较
2. **Agentic Coding 三阶段**: 开发、代码审查和安全硬化可分阶段并行或循环；各阶段均可能有资源与人工判断瓶颈
3. **代码成本**: 生成成本下降不等于安全交付成本下降；漏洞价值、验证、修复、维护与事故风险共同影响总成本
4. **机器速度攻击使普通弱点更昂贵**（HF 2026-07 入侵，[[20260727-hf-agent-intrusion-technical-timeline]]）：17,600 个攻击动作，成功路径藏在数千条失败路径生成的噪声里；HF披露的行为规模及取证复杂度提示关联分析成本；单案不提供人与Agent匹配成本比较，也不证明全部缺陷的普遍可发现性。详见已校准source。
