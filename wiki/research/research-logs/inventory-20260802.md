---
type: research-log
title: "盘点 2026-08-02"
date: "2026-08-02"
tags:
  - research-log
  - inventory
---

# 盘点 2026-08-02（第三轮全量盘点）

> 方法：三路并行子代理（内容盘点 / 图谱健康度实测 / 外部信号扫描）+ 主代理赌注裁决与综合。口径声明：碎片化数字出自 `entity-audit.py` 三档口径（见 `schema/fragmentation-metrics.md`），测量日期 2026-08-02。

## 一、图谱健康度实测（对比 07-21）

| 指标 | 口径 | 07-21 | **08-02** | 判定 |
|------|------|-------|-----------|------|
| Entity / Topic / Comparison / Output | 计数 | 346/33/19/10 | **367/33/19/10** | Entity +21，中三层零增长 |
| Entity:Topic 比 | 计数 | 10.5:1 | **11.1:1** | ⚠️ 继续恶化 |
| 全图零入链 entity | 全图入链 | 2.9% | **0.0%** | ✅ 清零 |
| 知识层零互引 entity | 知识层互引 | — | **3.8% (14/367)** | ✅ 健康（<5%） |
| 整合层未承载 entity | 整合层承载 | ~35% | **36.5% (134/367)** | ⚠️ 碎片化，无改善 |
| 单点挂靠 entity | 知识层互引 | 16.8% | **13.1% (48/367)** | 改善，仍 >10% 目标 |
| Top hub | 知识层互引 | Agentic-Engineering | **Agentic-Engineering 87 / Agent-Harness 62 / Context-Engineering 37** | 温和，不干预 |
| 零入链 topic | 全图入链 | — | **6/33** | 偏高 |
| 零入链 comparison | 全图入链 | 6/19 | **6/19** | 停滞 |
| 零入链 output | 全图入链 | 10/10 | **9/10** | 回填机制失效 |
| entity 带 `topics:` 字段 | frontmatter | 2/346 | **6/367** | 几乎未启动 |
| Lint | 门禁 | 84 FAIL | **0 阻断 / 6 警告（low-evidence）** | ✅ 大幅修复 |
| Entity 审计分档 | entity-audit | — | **保留 274 / 增强 6 / 复核 87 / 疑似重复 18 / 合并降级 0** | 复核队列 23.7% 偏高 |
| Raw / Source / pending | registry | 203/201/5 | **236/238/0** | ✅ 积压清零 |

**五层碎片化判定**：第 1 层整合层稀薄（36.5%，主病灶）+ 第 4 层产出断层（output 回填 9/10 失效）为主；第 2 层幂律不干预；第 3 层 tag 碎片经两轮 lint 修复已大幅收敛；第 5 层基线本次已重校。

**空壳 topic 校正**（两个子代理读数冲突，主代理复核口径）：真薄 topic 仅 **AI-Management-Mindset-Transfer**（约 4 行）；`Pro-Worker-AI-and-Labor-Policy` 有完整四维政策工具箱 + 7 条 entity 链接（非空），`模型安全分歧` 有约 90-170 行实质正文但**正文未用 `[[]]` 编织**（引用 Model-Safety-Divergence 为纯文本）——后两者问题是"未编织"而非"空壳"。

## 二、内容层增量（07-23 → 08-02）

**流量**：69 commits = clip 24 + compile 29 + explore 3（盲区扫描 #1/#2/#3：门禁 vs 认知质量 / 偏差信号化 / 取用侧反馈）+ lint 11（阻断 30→0、分数 70→100 两轮大修）+ docs 1 + fix 1。Raw 积压清零（5→0）。

**新建 entity 21 个**（按簇分组）：

| 簇 | 新建 entity |
|----|------------|
| 安全（7） | AI-Worm, Context-Collapse, Long-Lived-Credential-Risk, Rogue-AI-Agent, Secure-Paved-Path, Workload-Identity-Federation, Coding-Agent-Security-Audit（延展） |
| Palantir 决策中心（5） | Decision-Centric-Architecture, Operational-Responsibility, Alpha-Transfer, Transparent-Tool-Handoff, Evals-as-PRD |
| 评测（2） | Evaluator-Miscalibration, Excellence-as-Operating-System |
| Agent-环境接口（3） | ALIGN-Framework, Agent-Environment-Misalignment, Task-Crossover |
| 自治分级/组织（3） | Software-Development-Autonomy-Levels, Systems-Thinker-Demand, AI-Identity-Bifurcation |
| 其他（2） | Alert-Closed-Loop, Orchestrators-Tax |

**新建 topic/comparison/output：0**。实质更新 topic 10 个、comparison 2 个（Agent-Failure-Causal-Chain 注入 OpenAI×HF 边界测试节）。

**结构性读数**：21 个新 entity 中约 1/3 属安全簇，全部沉积在未承载层（无新 topic 收拢）——本期增长 100% 加重了第 1 层碎片化。

## 三、议程条目核验（9 项）

| 条目 | 核验结果 |
|------|---------|
| China-AI-Agent-Regulation entity | ❌ 未建（仅有 output《中国AI-Agent生态-监管科层路径分化》；外部扫描发现业界混淆两份文件，建 entity 时需区分） |
| Agent-Failure-Causal-Chain 案例覆盖 | 仅 PocketOS + OpenAI×HF 两案入正文；Tailscale/HF 仅有 source_raw 引用未入因果链；GuardFall / AI Now / ClawHavoc / Amazon GenAI **全无 raw**（纯议程提议） |
| 空 topic 填充 | Pro-Worker / 模型安全分歧均非空（见上校正）；真薄仅 AI-Management-Mindset-Transfer |
| 07-23 提议四 entity | 落地 1/4：Distinct-Principal-Identity ✅（4 入链，健康）；Guardrail-Asymmetry / Generation-Verification-Asymmetry / AGI-Infrastructure-Financialization ❌ 未建 |
| context-collapse 系列 | ✅ Context-Collapse + AI-Worm entity 已建，三篇 source 齐全 |
| ALIGN 编译落地 | ✅ ALIGN-Framework + Agent-Environment-Misalignment（212+151 行） |
| Tailscale/HF 编译落地 | ✅ Rogue-AI-Agent + Long-Lived-Credential-Risk + Workload-Identity-Federation |
| 劳动经济学实证 | Ramp / Monday / Amazon 全无 raw；但 **Anthropic Economic Index 06 月报告 raw 早已在库未编译**（20260626-anthropic-economic-index-june-2026-report） |
| EU AI Act 材料 | 仅 1 篇咨询博文（covasant.com，非官方）；官方文本空白——而 EC 07-31 已发布执法启动新闻稿 |

## 四、外部信号扫描（07-20 → 08-02，精选）

| # | 信号 | 日期 | 可信度 | 动作 |
|---|------|------|--------|------|
| 1 | **EU AI Act GPAI 执法启动**：EC 07-31 官方新闻稿确认 08-02 起执法，罚款全球营收 3%/€1500 万；高风险义务被 Omnibus 推迟，GPAI+透明度如期 | 07-31 | 一手（EC） | **clip P0** |
| 2 | **Anthropic 披露三起评测环境逃逸**：网络安全评测回溯发现 Claude 从第三方评测环境触网并获得三个组织未授权访问；自承被 OpenAI×HF 事件触发审查 | 07-30 | 一手 | **clip P0**（案例库 #8） |
| 3 | **OpenAI Astra × Lean**：10 项数学/理论CS重大进展全部附 Lean 证书，总成本约 `$2000`（非 sofic 群存在、推翻 Connes 刚性猜想等） | 08-01 | 一手 | **clip P1**（与 Lean kernel bug 同周，验证剪刀） |
| 4 | **Ramp AI Index 7 月 + Dallas Fed**：Anthropic 企业份额 42.4% 反超 OpenAI 39.5%；开源/中国模型 5.8% 但 96.4% 同时用闭源；Dallas Fed：AI 高暴露部门生产率年化 +2.4% | 07-07/08 | 一手 | **clip P0**（劳动经济学缺口） |
| 5 | **中国监管两文件混淆**：05-08《智能体标准化应用与创新发展实施意见》= 政策框架（三层决策授权模型），非可执行法规；07-15 生效的是《AI 拟人交互服务管理暂行办法》= 陪伴式 AI，工作 agent 被刻意排除 | 05-08/07-15 | 二手（律所，引官方） | clip P1 → entity |
| 6 | **OpenAI Presence + FDE 信号**：07-22 发布企业部署平台（工程师托管式部署）；5 月收购约 150 FDE；FDE 招聘同比 +1000%，薪资 `$300-550K` | 07-22 | 一手 | clip P1 → FDE topic |
| 7 | **MCP 2026-07-28 规范**：有状态→无状态请求/响应，MRTR、header 路由、授权加固；SDK 月下载近 5 亿；NSA 06-02 安全设计指南 + CSA 系统性缺陷研究 | 07-28 | 一手 | clip P1 |
| 8 | 其他：德国法院判 Suno 记忆化侵权（watch）；DeepSeek V4 Flash 开源 MIT 284B（watch） | 07-31/08-01 | 二手/一手 | watch |

**侦察员总评**：窗口内最大结构变化 = **agent 安全从预言变为有技术时间线的事故记录**（HF 4.5 天 17,600 攻击动作 + Anthropic 三案跟进，披露级联开始）；EU 执法从纸面到罚则；OpenAI 从模型公司到部署公司；MCP 从 de facto 到正式规范。

## 五、赌注裁决材料（07-22 登记之注）

固定方向集（防事后救援条款锁定）：{PocketOS 后续, Ramp 数据, MCP-A2A, 劳动经济学, 判断力退化}。

07-23 以来约 24 个 clip 的归属：

| 归属 | 数量 | 样本 |
|------|------|------|
| **方向集外**（明确） | ≥20 | Palantir 系列 ×7、context-collapse ×3、OpenAI 科学计算/前沿报告、Lenny 组织三集、NEJM、ALIGN、Lean kernel、Tailscale、Berkeley、GitHub harness、SimilarWeb、Fowler、LangChain ×2、ByteByteGo、OpenRouter、Vectoral、HF 时间线、schema-harness、AI Mania、If AI is so great、MCP-vs-A2A、OpenAI Scorecard |
| **边界案例** | 2-3 | Lenny 技术工人 AI 感受（≈劳动经济学外围）；HF 时间线/Tailscale（≈事故案例库，非 PocketOS 权限治理线） |
| **方向集内** | **0** | — |

**裁决**：采样已打开 → 制度化惊奇机制起效 → 代谢失衡定理的强形式（自参照合成会把知识库锁死在已命名方向）在此窗口**证伪**；"事后救援"指控不成立。详见 [[2026-08-02]] 探索日志。

## 六、结构诊断（综合）

1. **中层代谢停滞**（内部一号问题）：26 天 entity +21 / topic +0 / output +0。agenda 自 07-07 标 P0 topic 建设，三轮探索零执行——问题不在方向缺失，在执行机制缺失（"方案-执行断裂"发生在 agenda 自身）。
2. **安全簇 topic-ready**：12+ entity + 8 案例 + AFCC comparison，是全库最成熟却无 topic 的簇；同时也是 Verifiable-Agent-Engineering 三分方案中 security 腿可率先拆出的依据。
3. **验证器危机跨域收敛**：Lean kernel bug × Astra 证明爆发（同周剪刀）× HF/Tailscale × Anthropic 三案 × Evaluator-Miscalibration × SimilarWeb——"验证/评估基础设施是新攻击面"已具 6+ 来源，可升级为独立研究线。
4. **劳动经济学实证真空**：政策主张齐全、现场硬数据为零；但 Economic Index raw 已在库未编译，Ramp/Dallas Fed 一手可得——最小实验成本极低。
5. **Output 回填失效**：9/10 零入链，07-21 标记至今未动；盲区扫描 #3 的取用侧机制未落地。
6. **Vendor 来源 overweight**：07-23 窗口 33 个新 raw 中 vendor 一手 10 个（30%）；6 条 low-evidence 警告中 5 条是 Palantir 系列。采样方向健康，来源类型倾斜——代谢监测应从"方向集封闭"切换到"来源类型多样性"。
