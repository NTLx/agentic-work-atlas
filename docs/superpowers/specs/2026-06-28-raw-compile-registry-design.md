# Raw Compile Registry 设计

**日期**: 2026-06-28
**状态**: 已确认

## 问题

当前知识库对 raw 是否“已编译”的判断依赖运行时推断，而不是显式维护的状态层。

现状的核心逻辑位于 `tools/wiki-lint.py` 的 `raw_compile_status()`：

- 遍历 `raw/*.md`
- 读取 raw 正文，检查是否含历史 `## 编译摘要`
- 或检查同名 `wiki/sources/{raw 文件名}.md` 是否存在
- 然后临时推断 `compiled / pending`

这个模型的问题有四个：

1. **高 Token 成本**：Agent 每次都要重新建立“哪些编过、哪些没编”的判断，而不是读取一个小的状态面。
2. **状态不确定**：`compiled` 只是“看起来存在某种痕迹”，不是流程显式承诺的结果。
3. **没有 skipped 语义**：判题后决定不进入主线的 raw 没有稳定归宿。
4. **内容与状态耦合**：`wiki/sources/` 同时承担知识产物和状态信号，职责混杂。

## 设计目标

1. 把 raw 编译状态变成 repo 内的显式权威数据，而不是每次运行时推断。
2. 将日常“判断是否已编译”的成本压到接近 `O(1)` 读取。
3. 保留持久确定性：同一篇 raw 在任意一次会话里都能得到一致状态。
4. 让状态维护成为 `compile` 流程的自然副作用，而不是额外工作。
5. 不污染 Wiki 知识层：`wiki/sources/` 继续只承载知识摘要，不承载操作状态。
6. 支持判题后的 `skipped` 分流，但避免设计过重的状态机。

## 方案比较

### 方案 A：继续隐式推断

保留现有模式，只优化 `tools/wiki-lint.py` 的扫描逻辑。

优点：

- 改动最小
- 兼容现状

缺点：

- 状态仍不是第一等对象
- 仍然需要全库扫描和正文判断
- 无法优雅支持 `skipped`
- Agent 仍需重复理解文件系统关系

### 方案 B：让 `wiki/sources/` 成为状态权威

要求每个 raw 都对应一个 `wiki/sources/*.md`，包括 `pending` 或 `skipped` stub。

优点：

- 状态与摘要聚合
- 表面上便于人工查看

缺点：

- Wiki 层被操作性状态污染
- `source-summary` 和状态职责混杂
- `skipped` 这类非知识产物被强行写进知识层

### 方案 C：显式账本模块 + 唯一 compile 入口

新增独立状态账本和维护模块；所有编译入口都先经过该模块。

优点：

- 状态权威明确
- 查询成本最低
- `skipped` 可稳定持久化
- `wiki/sources/` 回归单一职责
- 适合做一致性校验和后续自动化

缺点：

- 需要新增一个状态文件和轻量工具模块
- 需要把 `compile` 入口收敛为固定命令

**推荐**：方案 C。

## 核心设计

### 深模块与 seam

新增一个小而深的模块：

- `tools/compile_registry.py`

它是 raw 编译状态的唯一外部 seam。调用方不再自己推断状态，只通过该模块读取和更新。

建议外部 interface 只暴露 5 个动作：

- `get(raw_file)`
- `list_pending()`
- `mark_compiled(raw_file, summary_path, body_sha256, compiled_at)`
- `mark_skipped(raw_file, reason_code, note, body_sha256, updated_at)`
- `reconcile()`

这 5 个动作足以覆盖 backlog 查询、单篇编译、判题跳过、批量对账和 lint 校验。

### 状态权威文件

新增机器维护文件：

- `state/raw-registry.json`

这个文件是 raw 状态的唯一权威数据，不依赖 Agent 重新阅读文章正文来判断状态。

目录建议：

```text
state/
└── raw-registry.json
```

### 记录结构

每篇 raw 对应一条记录，key 使用 raw 文件名。

建议结构：

```json
{
  "version": 1,
  "updated_at": "2026-06-28T10:30:00+08:00",
  "items": {
    "20260610-qwen-constraint-driven-engineering-experiment.md": {
      "raw_file": "20260610-qwen-constraint-driven-engineering-experiment.md",
      "status": "compiled",
      "body_sha256": "8c5d...",
      "summary_path": "wiki/sources/20260610-qwen-constraint-driven-engineering-experiment.md",
      "compiled_at": "2026-06-28T10:30:00+08:00",
      "updated_at": "2026-06-28T10:30:00+08:00"
    },
    "The Tokenpocalypse Is Here Companies Are Scrambling To Stop Spending So Much on AI.md": {
      "raw_file": "The Tokenpocalypse Is Here Companies Are Scrambling To Stop Spending So Much on AI.md",
      "status": "pending",
      "body_sha256": "1a92...",
      "updated_at": "2026-06-28T10:30:00+08:00"
    },
    "20260530-some-off-topic-article.md": {
      "raw_file": "20260530-some-off-topic-article.md",
      "status": "skipped",
      "body_sha256": "5b4f...",
      "skip_reason_code": "off-topic",
      "skip_note": "不服务于 AI / Agent 重写工作系统主线",
      "updated_at": "2026-06-28T10:30:00+08:00"
    }
  }
}
```

### 状态模型

主状态机严格保持三态：

- `pending`
- `compiled`
- `skipped`

不引入 `compiling`、`blocked`、`dirty` 等额外主状态。

原因：

1. 日常使用只需要知道“待处理 / 已编译 / 已排除”
2. 重编译不是业务状态，而是派生信号
3. 状态越少，越稳定、越便于人工维护和脚本验证

### 状态语义

- `pending`：已纳入 registry，但尚未被编译，也未被明确排除。
- `compiled`：当前 raw 正文版本已成功编译，并落到 `summary_path`。
- `skipped`：已经过判题，明确不进入主线。

这里的关键定义是：

> `compiled` 不是“可能存在 summary 文件”，而是“这篇 raw 的当前正文版本已经被流程成功编译”。

因此，`body_sha256` 是确定性核心。它把“是否是同一份 raw 内容”从名称判断升级为内容判断。

## 数据流与命令行为

### `compile`

职责：

- 从 registry 获取待处理 raw
- 对目标 raw 做判题
- 完成知识编译
- 在成功后更新 registry

建议流程：

1. 启动时先调用 `reconcile()`
2. 如果是 `compile` 无参数，读取 `list_pending()` 选择下一个或前 N 个
3. 如果是 `compile <raw>`，若 registry 尚未收录，则先注册为 `pending`
4. 执行判题
5. 若不进入主线，执行 `mark_skipped(...)`
6. 若进入主线，按现有 compile 工作流写入 `wiki/sources/`、entity、topic、comparison
7. 只有全部写入成功后，才执行 `mark_compiled(...)`

关键约束：

- **先写 Wiki，后写 compiled 状态**
- **先判题，后写 skipped 状态**
- 任何中途失败都不能把状态写成 `compiled`

### `compile <raw>`

职责与 `compile` 相同，但目标明确为单篇 raw。

额外规则：

- 如果文件存在、registry 不存在该项，则自动初始化为 `pending`
- 如果已经是 `skipped` 或 `compiled`，命令仍可执行，但应显式提示当前状态，避免误操作

### `status`

职责：

- 直接读取 registry，输出全局状态概览

建议输出：

- `pending / compiled / skipped` 计数
- 待处理 raw 列表
- 需重编译候选列表
- registry 与文件系统不一致的异常摘要

`status` 是以后默认的人类入口和 Agent 入口，用于回答：

- 现在 backlog 还有多少
- 哪些 raw 已被明确跳过
- 哪些 raw 变更后需要重编译

### `reconcile`

职责：

- 只做状态账本与文件系统对账，不做知识编译

建议检查项：

1. `raw/` 中有新文件，但 registry 尚未收录
2. registry 中有记录，但 raw 文件已经不存在
3. `compiled` 记录指向的 `summary_path` 不存在
4. raw 当前正文 digest 与登记的 `body_sha256` 不一致

建议行为：

- 新增 raw：自动补登记为 `pending`
- 缺失 raw：标记异常并等待人工处理，不自动删除历史记录
- 丢失 summary：进入“需重编译候选”
- digest 变化：进入“需重编译候选”

### `rebuild`

职责：

- 面向批量重编译

建议消费来源：

- `status` 中列出的“需重编译候选”
- 或显式指定范围

`rebuild` 不需要新增状态，只在成功完成后覆盖：

- `body_sha256`
- `compiled_at`
- `updated_at`
- `summary_path`（若路径变化）

## 派生信号：需重编译候选

“需重编译”不是第四个状态，而是从 registry 派生出来的待处理信号。

触发条件：

1. `compiled` 记录的 `summary_path` 不存在
2. raw 当前正文 digest 与登记 digest 不一致

呈现方式：

- `status` 单独展示
- `rebuild` 或 `compile --changed` 消费

这样可以避免把主状态机扩成 `pending / compiling / compiled / skipped / dirty / blocked` 的复杂模型。

## 与现有 Wiki 层的职责分离

### `wiki/sources/` 的职责

继续保持为知识层产物：

- source summary
- 证据浓缩
- 编译摘要
- 与 entity/topic/comparison 的链接桥梁

### registry 的职责

只回答操作性问题：

- 这篇 raw 当前是什么状态
- 何时编译
- 是否被跳过
- 这次编译对应哪一版 raw 正文

这保证两层职责清晰：

- `state/raw-registry.json`：状态权威
- `wiki/sources/*.md`：知识产物

## 一次性迁移方案

现有 raw 无需重新交由 Agent 解读。直接执行一次 bootstrap：

1. 枚举 `raw/*.md`
2. 对每篇计算 `body_sha256`
3. 若 raw 正文含历史 `## 编译摘要`，初始化为 `compiled`
4. 或若存在同名 `wiki/sources/{raw 文件名}.md`，初始化为 `compiled`
5. 两者都不存在时，初始化为 `pending`
6. `skipped` 初始为空，之后仅通过 compile 判题产生

这一步只是把历史“隐式推断”固化为一次性迁移，而不是继续让每次运行重做同样判断。

## 一致性审计

### `lint` 的新职责

`tools/wiki-lint.py` 不再承担“推断 raw 状态”的主要职责，而改为做一致性审计。

新增检查项建议命名为：

- `registry-consistency`

检查内容：

1. registry 中每个 `compiled` 项的 `summary_path` 是否存在
2. registry 是否覆盖全部 `raw/*.md`
3. `summary_path` 是否与记录的 raw 一致
4. `status` 统计值是否与 registry 实际内容一致

### 旧逻辑的去留

现有 `raw_compile_status()` 可降级为：

- 迁移阶段兼容逻辑
- 或当 registry 缺失时的只读 fallback

但它不再是日常权威来源。

## 错误处理原则

1. **写 Wiki 失败**：registry 不更新为 `compiled`
2. **判题后排除**：仅写 `skipped`，不创建知识 stub
3. **文件系统漂移**：由 `reconcile` 和 `lint` 报告，不静默修正知识内容
4. **registry 缺失或损坏**：显式报错，提供 `reconcile --rebuild-registry` 作为恢复路径

## 测试与验证

建议新增两类验证：

### 单元级

覆盖 `tools/compile_registry.py`：

- 新 raw 自动注册为 `pending`
- `mark_compiled()` 正确写入 `summary_path` 和 digest
- `mark_skipped()` 正确持久化原因
- `reconcile()` 能发现新增 raw、缺失 summary、digest 漂移

### 集成级

覆盖命令行为：

1. `status` 输出与 registry 一致
2. `compile <raw>` 完成后状态从 `pending` 变 `compiled`
3. `compile <raw>` 判题排除后状态变 `skipped`
4. raw 正文变更后，`status` 将其列入需重编译候选
5. `lint` 能报告 registry 与文件系统不一致

### 人工验证

最小人工检查流程：

1. 运行 `status`
2. 确认计数可解释
3. 随机抽 1 篇 `compiled`，确认 `summary_path` 存在且 raw digest 未漂移
4. 随机抽 1 篇 `skipped`，确认跳过理由可读

## 预期收益

### Token 成本

从“每次都扫 raw 和 `wiki/sources/` 后再推断状态”，变成“读取一个小 registry 文件”。

这不是 prompt 级优化，而是把状态判断从认知层下沉到数据层，因此收益稳定、可持续。

### 确定性

同一篇 raw 在不同会话、不同 Agent、不同时间点看到的都是同一份状态记录，而不是各自重建推断。

### 可维护性

状态维护被收口在唯一 seam：

- 调用方不需要知道状态如何落盘
- `compile/status/reconcile/rebuild` 都复用同一个模块
- 后续如果要从 JSON 升级到 YAML、SQLite 或别的存储，也只需替换模块实现

## 实施边界

1. 不修改 raw 正文，只读取并计算 digest
2. 不把 `pending` 或 `skipped` 写进 `wiki/sources/`
3. 不扩张主状态机到三态以上
4. 不在本设计阶段改写现有 compile 内容工作流，只在其前后加状态 seam

## 实施顺序

1. 新增 `state/raw-registry.json` 与 `tools/compile_registry.py`
2. 实现 bootstrap / reconcile
3. 将 `compile` 入口接到 registry seam
4. 新增 `status` 命令
5. 将 `lint` 从状态推断改为一致性审计
6. 保留旧逻辑作为迁移期 fallback，稳定后再下线

## 成功标准

1. Agent 不再需要通过阅读 raw 或扫描 `wiki/sources/` 来判断 backlog
2. `status` 成为唯一推荐入口，能稳定给出 `pending / compiled / skipped`
3. `compile` 完成时自动维护 registry，无需额外手工更新
4. raw 正文变更能被检测为需重编译候选
5. `wiki/sources/` 不再兼任状态层
