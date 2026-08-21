---
type: raw
source: "https://bidclub.ai/e/valley101-2026-08-19-e249-token"
author:
  - "泓君"
  - "张宏江"
  - "黄东旭"
show: "硅谷101"
episode: "E249"
published: "2026-08-19"
created: "2026-08-19"
duration: "87 min"
description: "硅谷101 E249｜三方对谈：Token 经济从「Maxing」转向「Efficient」的拐点已到；OpenClaw / Hermes / Raft 等本地化 Agent 进化；Fable 5「绝对智能碾压」与多 Agent 蜂群之争；Agent-Native 投资地图。"
tags:
  - clippings
  - token-economics
  - agent-native
  - openclaw
  - hermes
  - singularity
  - jevons-paradox
---

# E249｜Token 经济转点：OpenClaw、Hermes 到本地自研的 Agent 进化之路

> 来源：硅谷101 E249｜泓君 × 张宏江 × 黄东旭｜2026-08-19｜87 min｜YouTube captions（cleaned by claude-fable-5, reviewed by gpt-5.6-luna）

---

## TL;DR

**核心议题**：2025 是 Agent 元年，2026 是市场从「Token Maxing」转向「Token Efficient」的转折点。本文围绕三方对谈展开：

- **张宏江**（源码资本投资合伙人、前微软亚研院长）：AI 基建远未到过度投资；张以「学习能力超人类」定义奇点已至
- **黄东旭**（OceanBase 联合创始人、PingCAP 联合创始人）：Agent 重度玩家；用 OpenClaw / Hermes / Raft 等工具自建工作流；1 人 3 个月、日烧 $400-500 跑出潜在 $10M ARR 的 db9
- **泓君**（硅谷101 主理人）：主持人

**关键论点**：
1. 市场拐点已到：从 model 能力竞赛 → Agent 工程纪律
2. Fable 5「绝对智能碾压」：单模型解决多 Agent 蜂群搞不定的问题
3. 本地开源模型经济学（DeepSeek V4 / GLM-5.2）解锁新工作负载
4. 投资地图：基础设施（Memory、Observability、Sandbox、Agent-Native Cloud、FDE）> 终端应用
5. 杰文斯悖论：单位 Token 降价 10x/年，Agentic Loop 带来 100x+ 增长
6. 东旭的 Gödel machine 之约：等待真正自改进系统
7. 张宏江宣告「奇点已至」，东旭保留异议

---

## Section Summaries（按节目段落）

### 1. 转折点已到

市场从 model capabilities → Agent engineering。Uber 4 个月烧完 2026 财年 AI 预算；Meta 计划限制员工 Token 消耗；Stripe 内部警告 Opus 4.8 成本。

### 2. 张宏江：基建仍远未到过度投资

无泡沫。类比早期互联网/铁路/高速公路建设。股市 ≠ 技术发展。Token 价格每年下降约 10 倍。

> 东旭类比：今天的 AI 基础设施像 1950 年代机房大小的电子管计算机——许多需求尚未出现。

### 3. 东旭的 Token Maxing 史

- 2025 年 11 月开始：用 Opus 跑 db9（云原生分布式数据库）
- 无法精确评估最强 vs 次强模型在最难任务上的差异 → 总是用最强模型
- 账单：Pro Max $200/月 + 额外 $400-500/天
- ROI：1 人 3 个月 → 潜在 $10M ARR

### 4. Token Maxing 是滞后指标

区分：
- **目的性 maxing**（好设计 + 重度使用）vs **排行榜刷榜**（浪费）
- 极端案例：Agent 算 1+1 一百万次刷榜

### 5. OpenClaw 的历史地位

- 作者 Peter（工程师/架构师，非科学家）用约 1 周时间构建
- 信号：Opus 4.5（2025 年 11 月）跨过能力阈值
- 标志转折：从研究 → 工程、从 model → Agent
- 东旭用它做私人助理（不是写代码）

### 6. 为什么火的是 OpenClaw

开源 + 本地优先 + 极客扩圈（类 Linux）
催化剂：Claude 春节前后升级 + Moltbook（Agent 社交网络）数日后出现

### 7. OpenClaw 的局限

- 质量未打磨；大规模部署有 config/稳定性问题
- 启动过早；OpenAI 重点转向 Codex
- Peter 加入 OpenAI；项目交由基金会运营
- **记忆是持续痛点**：压缩而非存储 → 回滚、Token 浪费

### 8. Hermes

- 制作方：Nous Research
- 东旭重度用户
- 不宣称解决记忆问题 → 反而把成功经验蒸馏为 Skills（工程层面，非模型能力）
- 架构优于 OpenClaw
- 商业模式：与模型厂商谈判渠道/折扣 → Token 消费

### 9. Agent 作为数字世界入口

> 东旭：「自 OpenClaw 起，我再没打开过 Gmail。」

- 自称「智能原教旨主义者」——在重要邮件上信任 Opus 4.8 的判断
- Agent 作为 newsletter、HN 的过滤器
- 「养龙虾」= 反复迭代 Agent 学习用户数字足迹
- 决策类任务用 Agent 当过滤器而非完全代理

### 10. Slock（现名 Raft）

- 作者：钱宇超（Kimi CLI 负责人）
- 东旭是首位天使投资人
- 类 Slack，但对象是 Agent（无共享 runtime context，只有频道信息）
- 用例：10 个顶级 Agent 互相挑刺做 code review
- 峰值：~1B Tokens/天，账单 $300-400/天
- 术语：「Agent 动力学」

### 11. 三个事件击碎 Token Maxing

- **GPT-5.5**、**DeepSeek V4**、**Fable 5**
- Fable 5 可以 one-shot 解决 Agent 蜂群都搞不定的问题，无需先前上下文
- > 东旭：「我前面烧了 10 亿 Token，Fable 5 非常精准地一次搞定了。」
- 开源模型现在可用于协作

### 12. 本地模型经济学

DeepSeek V4 Flash 在 Mac Studio 上：~30 Token/s，全功率下 ~$1/天电费

- 解锁之前负担不起的工作负载（如：批量总结 100+ 篇 CVPR/NeurIPS 论文）
- 宽带比喻：拨号 → 宽带解锁 TikTok / 视频通话

### 13. 现在的工作流

- 当前账单：$200-300/月（Claude top tier + Codex top tier）
- 主用模型：GPT-5.5/5.6、Codex；最难问题（DB 边界情况、5000-6000 行改动）用 Fable 5
- 角色抽象为「目标、验收、架构」 → 「Agent 管理学」

### 14. 杰文斯悖论

- Agentic Loop → Token 增长 100x+ vs Chatbot 时代
- 加上多 Agent 网络 + 高阶 Loop
- 单位节省 ≠ 总消耗下降
- 东旭：Claude/OpenAI API 消耗 + ARR 持续增长
- 张宏江：杰文斯悖论——成熟技术 + 价格下降 = 市场更大

### 15. 超级模型与蜂群

- 张宏江：超级模型改进会向下传导至蜂群 Agent
- 泓君：不相信绝对中心——韧性系统是分布式的
- 清华论文：「3 个臭皮匠超过 1 个诸葛亮」
- 东旭：把 Fable 5 投入卡住的多 Agent 讨论，立刻解锁其他 Agent

### 16. 投资地图

**分层**：终端应用先被碾压；基础设施（Memory、search、Sandbox、Harness）机会更多。

**东旭的投资原则**：
1. 不投自己用不上的
2. 数据平台 / memory / context management
3. observability（「Token 花在哪了」）
4. Agent-Native Cloud — 已投 InsForge

**张宏江的视角**：
- 垂直企业数据护城河 + FDE（Microsoft 刚宣布 6000 人 Frontier Company）
- Manus/Genspark = 实际是 To-Professional，仍然值得

### 17. Agent-Native 判断标准

> **思想实验**：去掉 AI/Agent 后还能跑吗？→ 是，则非 Agent-Native
> 成本在无 Agent 时上涨 1000 倍 → 真 Agent-Native

- 团队思维必须 Agent-first
- 东旭的「办公室政治」脚本：给 Agent 分配架构师/开发者/测试人格 → 不是真自我意识

### 18. 手搓软件、删库与信任 AI

- **正面惊喜**：Claude Code 自行搭建轻量 Google Slides 克隆做 PPT
- **负面**：删了生产库
- 信任建立不靠「AI > 人类」宣称，而是构建自运行系统
- 「连黎明都还没有到」

### 19. 推理成本与 To B

- Token 成本每年下降约 10x
- 推理能力每 3-4 月翻倍（历史 7 月翻倍）
- To B 走蒸汽机模式——先工厂，后家庭
- 日 $300 vs 工程师日成本 = 清晰账目
- KPI 修复：衡量效率/产出，不衡量原始 Token 消耗
- 行业利润可能从「发电机」转向「电网」

### 20. AGI 已至

- **张宏江**：过去 6 个月的模型在视觉 + 通用 IQ 上 > 100（人类均值右侧）
  - 编码能力超过平均工程师 → 由此定义 AGI
  - 奇点 = 机器学习能力 > 人类学习能力
  - 已到达
- **东旭**：等待真正的 Gödel machine（自改进系统）
- 存在性危机：人类可能首次面临不需要工作的时代

### 21. Llama Ventures 与时代坐标

- Llama = 年轻、AI 专注、华人中心、创始人都是成功创业者
- 两大 AI 中心：美国 + 中国
- 张宏江：这次革命可比火 / 电力
- 时代分界：过去 3 年 = 基础研究者；从 OpenClaw 开始 = 工程师 / 架构师 / 产品经理 / 创业者（Agent 时代）
- **东旭建议**：「Keep building」
- **张宏江建议**：「Get hands-on」

---

## 关键引用

> 「我前面烧了 10 亿 Token，Fable 5 非常精准地一次搞定了。」——黄东旭

> 「自 OpenClaw 起，我再没打开过 Gmail。」——黄东旭

> 「养龙虾」——黄东旭形容反复迭代 Agent 学习用户数字足迹

> 「Token spin 是输入，真正的产出是实验」——东旭引用 Garry Tan

> 「你必须像过去 sweat pixels 一样 sweat tokens」——东旭

> 「去掉 AI/Agent 后还能跑吗？能，则不是 Agent-Native」——东旭判断标准

> 「连黎明都还没有到」——东旭
