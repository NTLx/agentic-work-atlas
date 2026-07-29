---
type: source-summary
title: "Why DoorDash, Instacart, and Uber Eats Integrated LLMs Into Search Three Different Ways"
source_raw:
  - "[[20260728-bytebytego-llm-search-integration-depth]]"
created: 2026-07-29
updated: 2026-07-29
tags:
  - source-summary
  - enterprise-ai
evidence_level: medium
claim_type: mixed
---

# Why DoorDash, Instacart, and Uber Eats Integrated LLMs Into Search Three Different Ways

> ByteByteGo（2026-07-28）对三家外卖巨头 LLM 搜索重建的二手综合：同一问题、同一研究基础、三种迥异架构。核心命题——把 LLM 加入既有技术栈归结为一个问题："LLM 应该多深地触达运行时？"，而答案由**既有基础设施**决定，模型选择是次要的。来源：ByteByteGo Newsletter（基于各家官方工程博客披露）。证据等级：medium（二手综合，数据均为公司自报，但三案对比结构有综合价值）。

## 编译摘要

### 1. 浓缩

- **核心结论1**: 中心命题——集成深度问题优先于模型选择问题。"Adding an LLM to an existing stack comes down to one question: how deeply should the LLM reach into the runtime?" 三家公司对同一问题给出不同答案，决定因素是既有基础设施而非所选模型（"the specific model each company picked was secondary"）
  - 关键证据: 三家都在同一时间窗口、基于重叠的研究文献、面对相似的生产约束重建搜索，却得到三种完全不同的架构
- **核心结论2**: 集成深度光谱的三档案例
  - 关键证据:
    - **DoorDash（浅/外围）**: LLM 主要在离线批处理中增强既有知识图谱（从 SKU 数据抽取属性），运行时仅用于把查询解析为可链回图谱字段的 chunk；**RAG 倒置为 guardrail**——ANN 检索 top-100 taxonomy 概念，LLM 从列表中选取而非生成（"RAG defines the entire output space"，系统只产出设计已知的概念）；效果：热门菜品 carousel 触发率约 +30%，运行时保持基本经典
    - **Instacart（中/查询理解层）**: 三层策略——context engineering（RAG 注入 Instacart 专属上下文）+ 后处理语义过滤 + Llama-3-8B 微调；**按 head/tail 流量分布切分 serving**：头部 → 离线 RAG 缓存（延迟容忍、深度上下文工程），尾部 → 实时微调模型（<300ms，adapter merging + H100 + autoscaling）；效果：query rewrite 覆盖率 50%→95%+（精度 90%+），冷启动尾部（底部 2% 查询）scroll depth -6%、投诉减半；下游检索/排序仍是传统 ML/IR
    - **Uber Eats（深/embedding 骨干）**: 微调 Qwen 作双塔检索的 backbone——query tower 在线实时 embed、document tower 离线预 embed 数十亿文档进 HNSW 索引；经济性靠优化栈成立：Matryoshka（256 维 serving，vs 完整 1536 维召回损失 <0.3%）、int7 标量量化（延迟减半、召回 >0.95）、hexagon/city/fulfillment 预过滤；ANN k 调优：延迟 -34%、CPU -17%；每条查询和每个文档都是 LLM 派生向量
- **核心结论3**: 三个在所有架构中存活的普遍 tradeoff
  - 关键证据: ① 混合系统是默认形态（经典检索/知识图谱/ANN 索引仍做大部分工作）；② 预训练世界知识只是 head start，领域上下文必须经 RAG/微调或两者注入；③ guardrails（受限词表、相似度过滤、taxonomy 强制）悄悄决定输出是否与 catalog 对齐

### 2. 质疑

- **关于二手综合的质疑**: 全文基于各家官方工程博客（Uber ×2、DoorDash ×2、Instacart ×2，均列于文末），是二手综合而非一手数据；30%/95%/-34% 等数字全部是公司自报，无独立验证，发布时点接近营销窗口
- **关于因果方向的质疑**: "基础设施决定集成深度"是事后归因（post hoc）——三家是成功大厂的幸存者样本，没有失败集成案例对照。同样可能的混淆解释是：组织能力同时决定了基础设施积累和集成选择，而非基础设施单向决定集成深度
- **关于光谱可迁移性的质疑**: 食品搜索域是刻意选择的观察窗口（主观查询 + 长尾 + 多语言 + 复合约束同时出现在同一搜索栏）；"集成深度光谱可作为任意生产系统的心智模型"是文章的宣称而非结论，向其他域（如事务型系统、实时控制）的迁移未论证
- **关于"模型选择次要"的质疑**: 文章为强调基础设施把模型选择推到极端次要位置，但 Uber 案例中 Qwen 的跨语言能力（解决 Spanish "pan" 歧义）是模型内在的世界知识，不是基础设施——模型能力与基础设施的交互作用被简化成了基础设施决定论

### 3. 对标

- **Instacart head/tail 切分 = [[Dual-Tier-LLM-Architecture]] 的工业案例**: 该实体既有案例是医疗（OncoAgent 复杂度评分器路由 9B/27B）与制造（MachinaCheck），Instacart 补上第三例，且路由键不同——不是任务复杂度评分而是**流量分布**（头部高频可预计算，尾部冷启动需实时模型）。双层路由的键至少有三种形态：任务复杂度 / 流量分布 / 风险等级（综合判断）
- **DoorDash "RAG 倒置" ≈ [[Deterministic-Retrieval]] 的生成侧镜像**: 确定性检索约束"取什么"（工具层 100% 可靠），DoorDash 约束"输出什么"（LLM 只能从 top-100 已知概念中选取，RAG 定义整个输出空间）。两者同属"把 LLM 关进无聊可靠的空间"这一设计家族，分别作用在输入端与输出端（综合判断）
- **Uber 优化栈 ↔ Token-Supply-Chain 成本路由**: MRL 降维 + int7 量化 + 预过滤 = "同一模型、不同 serving 配置、不同成本质量曲线"，与 [[20260728-openrouter-evaluate-llm-provider-performance]] 的量化隐藏变量命题同构——provider/服务层是独立于模型选择的优化维度
- **跨域类比: 集成深度 ≈ 电气化史**: 工厂没有用电机直接替换蒸汽机中央驱动——围绕电机特性（小型、可分布式）花了几十年重组生产线（Paul David 的经典研究）。三家外卖公司的故事是同一模式的当代版：集成深度不取决于新动力源多强，而取决于既有机器布局允许它装在哪里（综合判断）

### 关联概念

- [[Dual-Tier-LLM-Architecture]] — Instacart head/tail serving 切分是双层架构的工业案例（路由键 = 流量分布）
- [[Deterministic-Retrieval]] — DoorDash RAG 倒置是其生成侧镜像（约束输出空间而非获取路径）
- [[Context-Engineering]] — Instacart 三层策略中的 RAG 上下文注入是 context engineering 的搜索域实例
