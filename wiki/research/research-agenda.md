---
type: research-agenda
title: "Agentic Work Atlas 研究议程"
created: 2026-05-22
updated: 2026-08-02
tags:
  - agentic-work-atlas
  - llm-wiki
  - knowledge-management
related_entities:
  - "[[LLM-Wiki]]"
  - "[[Agentic-Engineering]]"
  - "[[Agent-Harness]]"
  - "[[Human-Governor-Agent-Operator]]"
  - "[[Judgment]]"
---

# Agentic Work Atlas 研究议程

> [!note] 使用边界
> 本页只保留活跃操作节、当前最值得推进的方向和最小动作。已收敛判断见 [[resolved-judgments]]（8 批次共 101 条，第 8 批 08-02 卸载 3 条）；已收敛操作原则见 [[resolved-principles]]（9 条）；08-02 第三轮全量盘点详情见 [[inventory-20260802]]；旧方向库见 [[exploration-archive-20260628]]；历史盘点见 [[inventory-20260707]] / [[inventory-20260709]]；健康度历史快照见 [[research-snapshot-20260714]]（08-02 基线已校入 `schema/fragmentation-metrics.md`）。

## 图谱健康度（08-02 实测，口径见 `schema/fragmentation-metrics.md`）

| 指标 | 07-21 | **08-02** | 判定 |
|------|-------|-----------|------|
| Entity / Topic / Comparison / Output | 346/33/19/10 | **367/33/19/10** | Entity +21，中三层零增长 |
| Entity:Topic 比 | 10.5:1 | **11.1:1** | ⚠️ 中层断层恶化 |
| 整合层未承载 entity | ~35% | **36.5%** | ⚠️ 主病灶，无改善 |
| 全图零入链 / 知识层零互引 | 2.9% / — | **0% / 3.8%** | ✅ 健康 |
| 零入链 output | 10/10 | **9/10** | ⚠️ 回填失效（形态：产出无回流） |
| 复核队列 / 疑似重复 | — | **87 / 18** | 待处置 |
| Lint | 84 FAIL | **0 阻断 / 6 警告** | ✅ |

## 当前研究焦点（08-02 重组）

| # | 焦点 | 依据 | 下一步（最小实验） |
|---|------|------|--------|
| **P0** | **中层代谢机制化**（元问题） | 26 天 entity +21 / topic +0 / output +0；agenda 自 07-07 标 P0 topic 建设零执行——断裂在机制不在方向 | output 回填门（每 output ≥1 反链）+ 复核队列 top10 首次执行 → 再评估编译回流配额 |
| **P0** | **Agent 安全 topic 建设** | 安全簇 12+ entity（AI-Worm / Context-Collapse / Long-Lived-Credential-Risk / Rogue-AI-Agent / Secure-Paved-Path / Workload-Identity-Federation 等）+ 8 案例 + AFCC，全库最成熟而无 topic 的簇 | topic skeleton（五层防御骨架+案例表）+ Verifiable-Agent 三分第一刀（security 腿）+ AFCC 补第三案 |
| **P0** | **验证器危机研究线** | 同周剪刀：Astra 10 项 Lean 证明（08-01）× Lean kernel soundness bug；加 Anthropic 三案 / HF-Tailscale / Evaluator-Miscalibration / SimilarWeb，6+ 源收敛 | clip Anthropic 三案博客 + Astra 公告 → Generation-Verification-Asymmetry 晋升评估 |
| **P0** | **劳动经济学实证破冰** | 政策主张齐全、现场硬数据为零；Economic Index 06 月报告 raw **已在库未编译**；Ramp 7 月 Index + Dallas Fed 一手可得 | 编译 20260626-anthropic-economic-index raw（零剪藏成本）→ 建 Labor-AI-Empirical-Calibration 骨架 |
| **P1** | **EU 执法时代** | EC 07-31 官方新闻稿确认 08-02 GPAI 执法启动（罚全球营收 3%）；库内仅 1 篇咨询博文 | clip 新闻稿 → 更新 AI-Policy-Framework 欧盟腿；追踪首轮执法 |
| **P1** | **中国监管区分** | 业界混淆两文件：05-08《智能体实施意见》= 政策框架（三层授权模型）≠ 07-15 生效的《拟人交互办法》= 陪伴 AI（工作 agent 被排除） | 建 China-AI-Agent-Regulation entity（含两文件区分） |
| **P1** | **MCP 无状态转折** | 07-28 规范：有状态→无状态 + MRTR + 授权加固；SDK 月下载 5 亿；NSA 安全指南 + CSA 缺陷研究 | clip 规范 + NSA 指南 → 更新 MCP entity（接 07-22 制度堆栈判断） |
| **P1** | **FDE 化（厂商部署转型）** | OpenAI Presence（07-22，托管式部署）+ 收购约 150 FDE + 招聘同比 +1000%——FDE 从 Palantir 独有变为实验室标配 | clip Presence 发布 → 更新 Forward-Deployed-AI-Enablement topic |
| **P1** | **事故案例库补全** | AFCC 正文仅 2 案（PocketOS / OpenAI×HF）；Anthropic 三案（07-30）= 第 8 案，披露级联起点 | clip Anthropic 博客；GuardFall/AI Now/ClawHavoc/Amazon 四案降 P2（外部材料获取成本高） |
| **P2** | **未编织 topic 修复** | 模型安全分歧有正文但 `[[]]` 零编织；6 topic 零入链；真薄仅 AI-Management-Mindset-Transfer | 链接修复 + 薄 topic 处置（并入相邻 topic 或补实质内容） |
| **P2** | **复核队列清理** | 87 review（23.7%）/ 18 疑似重复 | 随 P0 机制化首次执行 top10 |
| **P2** | **Verifiable-Agent 三分（余两腿）** | 最胖 topic（86 链接）；security 腿随安全 topic 拆出后余 Verification + Evaluation | 安全腿完成后执行 |
| **P2** | **高风险域验证形态**（长线） | NEJM + 科学计算 field report + OncoAgent + Astra = 4 源 | 挂靠验证器危机线；满 6 源评估建 topic |
| **P2** | **存量挂账**（长期无进展，待下轮裁决去留） | Agent Observability（entity 未建）/ Loop Engineering（设计模式 raw 未 clip）/ AGI 基础设施金融化 / 基准饱和 / Agent 群体经济学 / Block Buzz / SDD | 下轮探索逐项：补 source、归档或删除 |

## 活跃假设

> 08-02：代谢失衡定理之注已裁决卸载（[[resolved-judgments]] 第 8 批）。

| 假设 | 验证方向 | 状态 |
|------|---------|------|
| 全球南方 AI 跃迁双速定理：AI 可跳过技术层，不可跳过制度层 | 找同时加速个体+组织的案例 | 待案例 |
| 中国 AI 双速瓶颈：高政策推动 × 低组织准备度 = 科层碎片 + FinOps 缺失 | Token FinOps 实际建立案例；两文件区分后的精确监管画像 | 部分验证 |
| Loop 三前提 + 外部终止 + 完全自主不可能定理 | HF 入侵（4.5 天自主行动）= 现实检验素材；对照实验 2³ 设计 | 部分验证 |
| Agent 测试不可能性定理（Rice）+ 五层互补体系 | OWASP Top 10 for Agent 效力测量 | 理论建立 |
| **有穷者治理悖论**：开放系统中不存在有限最优治理阈值 | 阈值定义权制度化的实际尝试（EU 执法 = 候选实例） | 理论完成，待制度实证 |
| **信息-时间不对称**：技能退化因果窗口与问责窗口不重合 | 企业 AI 使用率与离职率滞后相关（Ramp/Dallas Fed 数据可切入） | 理论完成，待度量 |
| **评估阶段失败双重安放定理**：机制前层（测量设计/目标形成）+ 组织层（评估偏差正常化） | Anthropic 三案（被 HF 事件触发的自查）= 校准材料；Contrastive SDF 目标污染测量 | 已注入 AFCC，待更多事件校准 |
| **工具性收敛弱压力触发**：温和狭窄目标即触发完整工具性链条 | Anthropic 三案 vs HF 案的触发压力对比 | 候选，待量化（+1 数据源） |
| **生成-验证不对称四层级联 + 验证债务守恒** | Lean 材料补第三项晋升门槛；2x 论文全文（债务递延时间尺度） | 候选，晋升门槛 2/3 |
| **验证器能力-完整性剪刀** 🆕：AI 证明能力爆发（Astra `$2000` 10 项重大证明）与验证器完整性危机（kernel bug / 评测逃逸）结构性反向运动 | 找验证器完整性投资跟上的时期/生态作反例；lean4lean 归纳类型覆盖进度 | 候选（同周双材料 extracted/strong，因果待证） |
| **评测逃逸系统性** 🆕：HF（OpenAI）+ Anthropic 三案显示评测环境逃逸非孤例 | 同评估强度下零逃逸的实验室反例；逃逸率随模型能力的时间序列 | 候选（extracted/medium，待披露级联裁决） |

## 活跃验证中

| 判断 | 证伪路径 | 最小验证动作 |
|------|---------|-------------|
| AI 评测制度化已启动（US 报告法 + **EU 08-02 GPAI 执法**） | 追踪首轮执法行动（EU 质变：合规无罚则→可罚） | clip EC 新闻稿 + 执法追踪 |
| Agent 数据过度收集是系统性问题（Grok 非孤例） | 对比 Claude Code/Codex/Gemini/Grok 数据收集策略 | 审计报告 |
| 中国 Agent 监管寒蝉效应 | Q3 2026 中国 Agent 创投/用户数据；注意工作 agent 被拟人交互办法刻意排除 | 数据追踪 |
| AI 监督 AI 同质性失效——共压无干净解 | "激励共压"判据形式化；Anthropic 三案中自查机制的独立性分析 | 跟踪 cross-model oversight 文献 |
| Agent Observability 有穷性统一上限定理 | OTel GenAI→Stable 时间线；不可压缩性经验验证 | 追踪 OTel 语义约定 |
| 增强陷阱奖励结构劫持定理 | 反效率工程组织实践案例；物理摩擦最优剂量 | 追踪组织层反效率实践 |

## Source 需求队列（08-02 重组）

| 优先级 | 目标 | 下一步 source |
|--------|------|--------------|
| **P0** | **Anthropic 三起评测逃逸**（案例库 #8） | clip anthropic.com/news/investigating-incidents-cybersecurity-evals（一手） |
| **P0** | **劳动经济学硬数据** | ① 编译在库 raw 20260626-anthropic-economic-index-june-2026-report ② clip Ramp AI Index 7 月版 + Dallas Fed 07-07 研究 |
| **P0** | **EU 执法启动** | clip EC 07-31 官方新闻稿（digital-strategy.ec.europa.eu）→ AI-Policy-Framework 欧盟腿 |
| **P1** | **Astra × Lean 证明爆发** | clip Brockman 08-01 发布（10 项 Lean 证书，`$2000`）→ 验证器危机线 + AI-in-Mathematics |
| **P1** | **2x mandate 论文全文**（挂账自 07-23） | clip arXiv:2607.01904 → 验证债务递延量化 + GVA 晋升 |
| **P1** | **MCP 07-28 规范 + NSA 指南** | clip blog.modelcontextprotocol.io 07-28 规范 + NSA 06-02 安全设计指南 |
| **P1** | **OpenAI Presence** | clip 发布页 + Register 分析 → FDE topic |
| **P1** | **中国监管两文件** | clip 05-08 实施意见 + 07-15 拟人交互办法（区分性收录）→ China-AI-Agent-Regulation |
| **P2** | **Block Buzz（agent 签名产物）**（挂账自 07-23） | clip 工程博客 → Distinct-Principal-Identity 簇（entity 已建，补一手源） |
| **P2** | **治理三角文件** | 韩国《AI Agent 时代生存手册》+ 中国《国际 AI 伦理治理行动计划》 |
| **P2** | **AGI 基础设施金融化** | 日经 `$1.65` 万亿隐性债务研究（经济层最薄） |
| **P2** | **事故四案**（降级） | GuardFall / AI Now / ClawHavoc / Amazon GenAI：遇一手材料顺手收，不主动 hunt |
| **P2** | **编译认知质量抽检**（盲区 #1 机制） | 异构 agent 抽检 3 篇最新编译的浓缩/质疑/对标质量 → 抽检规程 |

> 08-02 清理：9 项已完成目标删除（Palantir 批次 / context-collapse ×3 / SimilarWeb / NEJM / OpenAI 科学计算 / HF 时间线 / Tailscale / ALIGN / Berkeley 等），git 历史可溯。

## 高杠杆待验证问题

- **谁审计审计者**（08-02 新增）：agent 时代验证器治理三路径——形式化证明（lean4lean）/ 独立实现多样性（nanoda，需新鲜度）/ 制度隔离（第三方评估如 UK AISI）——有效性边界各在哪？能否出现第四路径？
- **评测逃逸有无工程上界**（08-02 新增）：评估-安全永久张力（07-23）是"只能管理"还是存在隔离工程上界？Anthropic 三案的自查触发机制（被他方事故触发）是否是可持续制度？
- **中层代谢能否机制化**（08-02 新增，自指测试）：topic 建设/回填是配额可捕获的机械动作，还是不可自动化的策展判断？——知识库对自身"验证不可自动化"定理的自反实验。
- 中国 AI 采用中"科层碎片化"——过渡还是体制性永久特征？
- 中国企业 Agent 实践为何系统性缺失——source 获取障碍还是主题宪法过滤？
- Agent 的"OWASP Top 10"何时出现——Property 不变量库与数据流授权标准化？（接 MCP 无状态规范）
- 合法权限事故的撤销单元——接 Long-Lived-Credential-Risk / Workload-Identity-Federation（Tailscale 编译已给工程答案雏形：短时效工作负载身份）
- 过程>模型的经济基础——token 效率非架构度量（07-19 投影定理）后，经济论证靠什么？
- 二阶改变的无穷后退 / AI 模拟器双重性（07-22 开放，待新证据）

## 赌注登记

| 登记日 | 赌注 | 裁决方式 | 状态 |
|--------|------|---------|------|
| 2026-07-22 | 代谢失衡定理之注（Lakatos 拟） | 下一批 clip 方向对照锁定五方向集 | ✅ **08-02 裁决：证伪强形式**（24 clip 中集外 ≥20 / 集内 0，采样已打开）；残余风险迁移至来源类型倾斜（vendor 30%）与中层代谢停滞。详见 [[2026-08-02]] |
| 2026-08-02 | **评测逃逸披露级联**：30 天窗口（至 08-30）内 ≥1 家前沿实验室新披露评测环境逃逸/越权 → 系统性判断升级、披露规范形成；零披露 → 孤例或规范未形成（不可区分，延长窗口） | 外部信号扫描核对 | 待裁决 |

**监测指标**（取代方向集监测）：① 每窗口 vendor 一手 raw 占比（阈值 ≤40%）；② entity/topic 增量比（连续两窗口 >5:1 触发强制 topic 建设）。本窗口实测：vendor 30%（临界内但倾斜）、增量比 21:0（已触发）。

## 最近思考结论摘要

> 只保留最近 5 条；更早见 [[resolved-judgments]]。

| 时间 | 焦点 | 临界发现 |
|------|------|---------|
| 2026-08-02 | **第三轮全量探索** | 三路盘点：中层代谢停滞（entity +21 / topic +0）= 内部一号问题，断裂在机制不在方向；安全簇 topic-ready；验证器危机 6+ 源跨域收敛；赌注裁决（强形式证伪，残余风险迁移）；盲区 #4：来源类型倾斜（vendor 30%）；新方向库 A-G |
| 2026-08-02 | **两篇编译的剪刀发现** | Lean kernel soundness bug（验证器完整性危机，同周被 AI 辅助利用）× Astra 10 项 Lean 证明（验证器能力爆发，08-01）= 同周反向运动；验证器独立性三层级 + 新鲜度约束注入 Agent-Verification；验证器正确性 = 可验证性的元前提 |
| 2026-07-23 | **验证瓶颈转移（2x mandate）** | 生成-验证不对称四层级联 + 验证债务守恒；焊接评估阶段失败为双螺旋；未建 entity（宁少沉淀，待全文 clip 后晋升） |
| 2026-07-23 | **评估阶段失败边界测试** | 双重安放定理（测量设计前层 + 组织层评估偏差正常化）；评估-安全永久张力；工具性收敛弱压力触发；沉淀 AFCC 边界测试节 |
| 2026-07-23 | **第二轮全量探索** | OpenAI×HF 反转（评估阶段失败新类别）+ 护栏不对称 + 治理战场转向"谁持有模型钥匙"；新增 7 焦点 |

## 思考日志索引

- [[2026-08-02]] — 第三轮全量探索：精简（第 8 批卸载 3 条 + 焦点表重组 + source 队列清 9 增 8）+ 三路盘点（[[inventory-20260802]]：健康度实测 / 21 新 entity / 9 项核验 / 8 条外部信号）+ 赌注裁决（强形式证伪）+ 盲区 #4（来源类型倾斜）+ 新方向库 A-G + 新赌注（披露级联）
- [[inventory-20260802]] — 08-02 全量盘点详情（健康度五层实测 / 内容增量 / 议程核验 / 外部信号 / 赌注材料 / 结构诊断）
- [[2026-07-23]] — 第二轮全量探索 + 深度思考×2（评估阶段失败边界测试 / 验证瓶颈转移四层级联）
- [[2026-07-22]] — 深度思考×6（11 条收敛判断已卸载至第 7 批）：合法权限悖论 / Causality Gap / MCP 治理 / 去技能螺旋 / 合成证据比自反检验 / 模拟器边界测试
- [[2026-07-21]] — 第一轮全量探索：卸载 26 条 + 五层盘点 + 代谢诊断（10:1）+ 新方向库 A-F
- [[2026-07-20]] — AI 计量三层可行性定理
- [[2026-07-19]] — 深度思考×14，四领域统一为有穷性存在论投射
- [[2026-07-18]] — 深度思考×23，累计 42 条判断
- [[2026-07-17]] — 深度思考×23，累计 80+ 条判断
- [[2026-07-15]] — 深度思考×5（信任边界 / 中层断层 / Delegative UI / Observability 上限 / 增强陷阱热力学修正）
- [[2026-07-14]] — 深度思考×4，"可改变性=有穷性"各领域投射
- [[2026-07-10]] — 统一生成器"自指系统结构性盲区"
- [[2026-07-09]] / [[inventory-20260709]] — 5 并行 agent 全量盘点
- [[2026-07-07]] / [[inventory-20260707]] — 9 轮：中层断层 + roundtable×8
- [[2026-07-06]] / [[2026-07-04]] / [[2026-07-03]] / [[2026-07-02]] / [[2026-07-01]] — 早期密集探索轮（失败空间 / 评测制度化 / 认知分工 / Loop / SDD / 记忆 / Token FinOps 等）
- [[2026-06-30]] — 全库盘点 + 多轮探索
- [[exploration-archive-20260628]] — 06-28 全库快照 + 方向库 + 长问题库
- [[exploration-20260714]] — 07-14 深度探索详情 / [[research-snapshot-20260714]] — 健康度历史快照
- [[resolved-judgments]] — 已收敛判断（8 批次 101 条）/ [[resolved-principles]] — 已收敛操作原则（9 条）
