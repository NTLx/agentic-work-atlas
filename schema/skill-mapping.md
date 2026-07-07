---
title: "ljg 技能与 Wiki 工作流映射"
type: schema-subdoc
---

> 本文档是 Agentic Work Atlas Schema 子文档，由 README.md 路由表按需加载。

# ljg 技能与 Wiki 工作流映射

## 核心原则：Agent 自主决策

所有技能选择由 Agent 基于材料特征自主判断，无需用户触发。Agent 在编译/探索/产出各环节自动评估材料属性，决定调用哪些技能、以什么顺序组合。用户的角色是提供材料和方向，不是驱动流程。

## 核心技能

| 技能 | 所在环节 | 定位 | Wiki 输出目录 | 编译产出 |
|------|----------|------|-------------|---------|
| **ljg-paper** (读论文) | compile | 论文类文章编译器 | `wiki/entities/` | 命题七拍叙事 + 速读卡 → 浓缩+质疑+对标 + 核心概念提取 |
| **ljg-paper-river** (倒读法) | compile | 研究型论文关系构建器 | `wiki/comparisons/` | 5 层倒读+正向追踪 → 概念演化脉络 + 对比分析维度 |
| **ljg-book** (拆书) | compile | 书籍类 raw 编译器 | `wiki/entities/` | 取景框 f(x) 分析 + hard-to-vary 检验 + 参考系图 |
| **ljg-qa** (问答提取) | compile, explore | 信息提问机 | 编译时注入 source summary；探索时生成探测问题 | 核心观点抽成 Q-A 对，为 entity/topic 提供结构化骨架 |
| **ljg-learn** (概念解剖) | compile(追加) | 概念八维度解剖 | `wiki/entities/` | 历史/辩证/现象/语言/形式/存在/美感/元反思 → 顿悟句 → entity 核心定义 |
| **ljg-read** (伴读) | compile(增强) | 深度伴读与跨域旁逸 | source summary 增强 | 结构标注 + 深度提问 + 跨域旁逸 → 跨领域类比洞察 |
| **ljg-think** (追本之箭) | compile(追加), explore | 纵向深钻 | `wiki/topics/` | 层层降深（表象→机理→原理→公理）→ 主题深度分析 |
| **ljg-rank** (降秩) | compile(追加), explore | 领域降秩（生成力） | `wiki/topics/` | 找 2-3 个不可约生成器 → Topic 核心结构 |
| **ljg-constraint** (约束) | compile(追加), explore | 约束分析（边界力） | `wiki/topics/`, `wiki/entities/` | 硬/软/自设约束分类 → 解空间映射 → 与 ljg-rank 互补 |
| **ljg-blind** (盲区扫描) | explore(周期性) | 元认知审计 | `wiki/research/research-agenda.md` | 对话历史盲区 + 微信读书精准补章 → Source 需求队列 |
| **ljg-plain** (白话) | audit, produce | 可读性校验 | N/A | Entity definition / Output 可读性校验（12 岁可读测试） |
| **ljg-writes** (写作引擎) | produce | 观点驱动写作 | `wiki/outputs/` | 观点驱动写作 → 博客/笔记作品 |
| **ljg-roundtable** (圆桌) | produce, explore | 多视角辩证 | `wiki/outputs/` 或 research agenda | 结构化多立场辩论 → 证伪方向、分歧点、共识边界 |
| **ljg-invest** (投资分析) | explore(FDE 专项) | 秩序创造机器评估 | source summary / entity 补充 | 「混沌→秩序」框架判断 AI 项目是否值得深度收录 |
| **obsidian-markdown** | audit(全环节) | 写入守卫 | N/A（质量门） | **所有 `.md` 文件写入前必调用** — 确保 Obsidian Flavored Markdown 合规 |

## 自主决策树

Agent 在每次编译/探索时自动执行以下决策，无需用户指令：

### 编译时：基础技能选择（按材料类型）

```
材料类型判断 →
  ├─ 论文/学术 → ljg-paper
  ├─ 书籍/长篇 → ljg-book
  ├─ 高密度结构化 → ljg-qa
  └─ 普通文章 → 三步编译法（标准路径）
```

### 编译时：追加增强技能（按材料特征，可叠加多个）

| 触发特征 | 追加技能 | Agent 自主执行方式 |
|----------|----------|-------------------|
| 源材料引入**新概念**（entity 库中未深入的核心术语） | ljg-learn | 对概念做八维度解剖，输出充实 entity 定义和「顿悟句」 |
| 源材料涉及**新领域/行业**（首次出现的领域级分析） | ljg-rank + ljg-constraint | 同时分析生成器和约束条件，两者配对输出 topic 页面 |
| 源材料含**跨域引用或类比**（引用其他领域文献/现象） | ljg-read | 伴读式分析，追踪跨域关联，旁逸洞察注入 source summary |
| 源材料讨论 **AI 公司/产品/项目**（FDE 相关） | ljg-invest | 用「秩序创造机器」框架评估收录价值 |
| 最近 **5 篇编译**未触发盲区扫描 | ljg-blind | 扫描对话历史思维盲区，输出充实 research agenda 的 Source 需求队列 |

### 产出时：技能选择

| 触发条件 | 技能 |
|----------|------|
| 需要博客/笔记输出 | ljg-writes |
| Topic 有争议性、需要多立场检验 | ljg-roundtable |
| Entity/Output 可读性不达标 | ljg-plain |

## 辅助技能（特定场景可选）

| 技能 | 触发条件 | 定位 | 说明 |
|------|----------|------|------|
| **aihot** | explore 需要外部现实对照 | AI 资讯查询 | 查询最新 AI 行业动态，为证伪方向提供外部参照 |
| **json-canvas** | 用户明确需要图谱类视觉输出 | Canvas 可视化 | 创建知识结构可视化（.canvas 文件） |
| **obsidian-bases** | 用户需要交互式数据仪表板 | 数据视图管理 | 创建审计数据视图（.base 文件） |

## 不适合纳入知识编译工作流的技能

| 技能 | 理由 |
|------|------|
| **ljg-relationship** | 人际关系结构分析（移情、阻抗、潜意识模式），属于人际心理分析，不属于知识编译 |
| **ljg-card** | 内容铸卡（PNG 视觉卡片），依赖 Playwright + Chromium，传播层工具而非编译层 |
| **ljg-word** | 单词精通，英语词汇深度分析，与知识编译主线无关 |
| **ljg-present** | 演讲铸造器，项目不以演讲为主要输出形式 |
| **ljg-travel** | 旅行文化研究，不在主线范围内 |
| **ljg-skill-map** | 技能地图，工具管理层面，不增加编译能力 |
| **ljg-push** | 推送引擎，技能仓库发布基础设施 |
