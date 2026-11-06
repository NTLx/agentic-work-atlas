# LLM WiKi 自进化修复 · 第一阶段任务书

- 建立日期：2026-11-06
- 范围：现有 ChatGPT Daily → Weekly → Hourly → Monthly + n8n + ServerFS 生产链路的正确性与可恢复性
- 原则：先保证事实、证据、身份和状态可靠，再逐步解除特定模型/产品绑定；不一次性重构
- 性质：阶段验收任务书；**不**作为 queue、RSS digest、work_events 或 Git 状态的第二份运行账本。真实运行状态以 n8n 和 Git 为准

## 目标及边界

第一阶段只解决自进化自身的缺陷：来源跨日重名/重 key、证据不足的 RSS 批次结算、Promotion→Integration 的可追溯性及回归验收。不得为了清理积压而改派、强行完成、清空旧数据或绕过 Source Evidence Gate。

第一阶段暂不修改 `claimed_by=chatgpt-*`、`worker=hourly|weekly|monthly`、`execution_policy=chatgpt_direct_only`，不切换为 Grok/OpenClaw，不新建数据库或重做整体编排。这些明确进入后续“执行器去耦”阶段。

## 工作项与验收

### P1-A · 来源身份与证据等级（首批已实施）

- [x] Schema 区分候选知识命题的 `canonical_key` 与上游来源 `source_identity`；为官方 GitHub 仓库定义稳定的身份及跨日报告归并规则
- [x] Daily/Weekly 定时任务加入向后兼容的来源归并约束；Weekly 需保留原 Event IDs、旧 key 与 evidence_version lineage
- [x] 修改 Source Summary 证据等级：被 Wiki 多次复用不再构成提高 `evidence_level` 的依据
- [x] 执行只读 Wiki lint、审查 diff、提交推送、验证 GitHub CI
- [ ] 观察实际新 Daily/Weekly 运行是否为同一原始来源保留可归并的身份、未丢失已存在 lineage
- [ ] 对代表性同源/同命题、同源/不同命题、转载、镜像、版本变化进行回归对照；必要时再做确定性 normalize 工具

**已发现真实案例**：`https://github.com/NVIDIA/auto-ontology` 对应 `github:NVIDIA/auto-ontology`、`nvidia-auto-ontology` 两个既有 canonical_key；不得重写历史记录来“修正”身份。

### P1-B · RSS 逐条 Evidence Receipt 与安全恢复（确定性门禁已上线，历史恢复中）

- [x] 确定增量 Receipt 合同：`rss.article.evidence_checked:<digest_id>:<item_key>`，复用原 `work_events`，不增加独立运行表
- [x] Daily 增加逐条证据核验、Record work event、Exact readback、历史 Digest 增量恢复约束
- [x] 首批真实 RSS Item 的 stable Event ID、verified/excluded 两种 Receipt 已写入 `work_events` 并按 exact ID 回读；verified 均有一手原文与 source_locator，excluded 只依据元数据按相关性排除、不伪称已读正文
- [ ] 验证真实 `source_gap` 增量恢复、重复 Upsert 幂等性与跨运行回读的一致性
- [x] n8n `Complete RSS intelligence digest`（ID `bSFpuTgbGCGVJTku`）已发布逐条 Receipt 强制门：在状态更新前核对 Digest/Item/Event 身份、终态、来源 URL、读取状态、证据定位或排除理由；缺失、冲突、source_gap 均拒绝封账；更新后校验精确 Item ID 集合
- [ ] 完成全场景验收：本轮已验证模拟合法 verified、合法 excluded、无 Receipt、source_gap、无 source_locator；生产历史 digest 的零/部分 Receipt 检查后未产生虚假完成。仍待验证旧 digest 重试、并发、跨 Digest 混用、部分更新、全量真实合法封账
- [ ] 对历史未封账批次按原 digest 补证并据真实证据逐项结算；不可直接批量将 processing 改为 processed

**2026-11-06 审计时的现场事实**：`rss-digest:2026-11-05` 15 个 processing，`rss-digest:2026-11-06` 23 个 processing；两天 A 模块均有 Discord delivered Receipt，但缺少对应 `rss.digest.completed`。这仅是当时快照，不代表后续状态；恢复前必须回读 n8n。

**2026-11-06 第一批执行结果**：原 `Complete RSS intelligence digest` 已在隔离节点验证与测试后发布新增证据门（active version `469de385-cd88-473a-ae2c-f14474088027`）；模拟 Data Table 写入节点已显式 pin，不涉及真实行更新。真实 Event 已记录 4 条（2 verified、2 excluded），分布于 2026-11-05 / 11-06 两批，每批 2 条。两批共 38 条 RSS 仍保持 `processing`，且无对应完成 Event；后续需按当时真实状态重新核验。

**剩余限制**：n8n 能确定性验证 Receipt 结构、关联与终态，不能仅靠这些字段证明 LLM 真正阅读原文；原文证据真实性仍由 ChatGPT 实际读取和人工可抽查 locator 保证。生产完整合法封账与网络/并发异常仍需进一步验收。日志保存策略已恢复（`saveManualExecutions=false`、`saveDataSuccessExecution=none`）。

### P1-C · Promotion/Integration 结果契约回归（正常成功路径已抽样核实）

- [x] 抽样核对 candidate Event → per-promotion Manifest → queue source_event_id → git wiki paths/commit → integration result Event：2026-11-02 一批 3 条 Promotion、共 4 个实际 Candidate IDs，3 个 completed queue/Integration Result；均对应实际 Git commit `83a4d1d1661084119aa057a6b850ba786d31e7cd`，实际提交变更文件与结果 Event 的 `wiki_paths` 三项一一对应，仓库对应文件仍存在
- [ ] 对 Manifest 缺失、证据变更、已覆盖/重复、变更不符合接受范围的情况证明不会盲写 Wiki
- [ ] 验证同一晋升运行重试不会重复生成稳定页、伪造提交或重开 terminal work
- [ ] 形成复用现有工具/测试基建的回归检查，不创建额外长期运行账本

### P1-D · 健康度、知识效用与稳定性验收（待实施）

- [ ] Lint、Entity Audit 与原有知识效用评测不回归；既有 20 例评测不能单独证明真实复用
- [ ] 为 Source Evidence/identity 和状态结算建立独立于写入 Prompt 的负例测试
- [ ] 将未封账 RSS 的缺口与恢复进度纳入现有 n8n 事件/运行报告可观测性；不等同于时间超期即失败
- [ ] 检查 n8n Workflow 定义和关键 Data Tables 的备份恢复能力；如果只有 workflow backup，没有数据恢复证据，则保留明确风险
- [ ] 只有连续真实执行和故障/恢复路径均有证据时，才宣告第一阶段完成

## 完成条件

1. 同一事实/来源在跨日、跨入口、重试时有稳定且可回溯身份；
2. RSS 无法在缺少逐条可审计终态证据时被确定性状态机误封账；
3. Promotion/Integration 的成功由真实 Git、Wiki、n8n 事实共同证实；
4. 源内容读取失败明确保留 `source_gap`，而不是改写成无变化/成功；
5. Wiki lint、CI、运行数据和多周期真实观察均可复核；无生产流程不可解释回归。

## 参考文件和生产资源

- Schema：`schema/knowledge-metabolism.md`、`schema/source-summary-template.md`
- Daily / Weekly：原有两个 ChatGPT 定时任务（不新增 Worker）
- n8n：`Record work event`、`Claim RSS intelligence digest`、`Complete RSS intelligence digest`、`Enqueue AI work`、`Mutate AI work state`
- 运行单一事实源：`work_events`、`rss_intelligence_items`、`ai_work_queue`、本仓库 Git history

