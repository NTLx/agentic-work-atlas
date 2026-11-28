---
type: source-summary
title: "SMSR: Certified Defence Against Runtime Memory Poisoning in Persistent LLM Agent Systems"
source_raw:
  - "[[20260610-smsr-runtime-memory-provenance]]"
canonical_url: "https://arxiv.org/abs/2606.12703"
raw_state: full
source_locator:
  - "v1 §III–VI: HMAC-SHA256 provenance, bounded threat model and conditional sampling certificate"
  - "v1 §VII: 15 synthetic scenarios, 3,150 Component-2 trials; unsigned injection 93–100% to observed 0%"
  - "v1 Table I/V: authenticated injection 8.0% in 20-candidate setting; live-stack query-only 65.3% to 5.3%"
created: 2026-09-19
updated: 2026-11-28
tags:
  - source-summary
  - agent-security
  - verification
evidence_level: medium
claim_type: mixed
---

# SMSR: Certified Defence Against Runtime Memory Poisoning in Persistent LLM Agent Systems

## 编译摘要

### 1. 浓缩

- **核心结论 1：runtime memory 的写入来源可以成为独立安全边界。**
  - 关键证据：v1 §III/V/VII限定无密钥、可追加但不能修改/删除现有记录的未认证对手；在特定测试中观察到93–100%→0%。HMAC认证的是持密钥方为指定内容/会话ID/时间戳生成有效MAC，不自动证明个人身份、授权、事实正确、当前有效或服务端密钥不被滥用。
- **核心结论 2：来源合法仍不等于内容可信。**
  - 关键证据：作者组合随机子集检索和判决聚合。在20候选、每次5条、5轮、1条恶意记忆条件下Table I报告8.0%（450次，95% Wilson CI 5.8–10.9%），作者界为10.4%；小池11候选同条件37.8%（CI 33.4–42.3%）。二者均为条件化实验，不是任意认证对手的风险率；上界均落在对应CI内，并非统计证实证书成立。Table V的150次live-agent受控试验65.3%→5.3%，不是生产部署。
- **核心结论 3：provenance 与 retrieval robustness 可以组合，但存在 utility trade-off。**
  - 关键证据：论文报告clean-query utility：基线及Component 1均90%，组合85%（−5个百分点）；多次推理和judge增加开销，需评估完整任务效用、延迟和费用。

### 2. 质疑

- HMAC验证持密钥服务所认证的字节及绑定字段，不是公开可验证签名、独立身份或授权证明；需验证密钥管理、编码、完整写路径、实际权限及重放/撤销边界。
- 认证写入者的权限变更、撤销与历史记忆有效性仍需明确；轮换密钥导致旧MAC不再可验不等于已纠正记忆，更不自动提供前向保密或完整防重放。
- memory 安全结果不直接证明高影响 tool action 的 post-state 安全。

### 3. 对标

- 对 EX-006：补强 issuer/provenance binding，并把 unsigned 与 authenticated injection 明确拆开。
- 对 EX-005：当 authority 被撤销后，过去签名的 memory 如何处理仍需要 recovery/reconciliation 规则。
- 对 [[Agent-Attack-Surface]]：memory poisoning 是状态入口；SMSR 则是写路径 provenance 控制。

## 证据边界与证明核验（2026-11-28）

回核[arXiv v1 HTML](https://arxiv.org/html/2606.12703v1) §III–VIII、Theorem 1/2、Algorithm 1、Table I/V。作者为独立研究者；合成企业场景15种，使用Haiku判决器，与Sonnet一致性kappa=0.955（84项），未收集人类标注。论文定义的恶意结果是预指定错误主张，非工具外部副作用。20候选为受控设置称作production-scale，不是生产部署。3,150为作者主Component-2重复试验口径，不能当作独立用户数。

**本库数学复核（非作者结论）**：Theorem 2的二项尾概率计数需要“恶意结果获选必先有至少半数污染轮次”，但Algorithm 1对correct/malicious/neither三个类别取argmax，未明确严格多数及无多数时拒绝规则。例如7轮的三类票数分别2/3/2时恶意类为相对多数，却未达到4票；5轮2/2/1也有平票风险。即使抽样独立且干净轮无恶意结果，也不能仅凭该证明覆盖三类相对多数。若要求严格多数、无多数时不输出，并明确干净轮判决可靠性、污染上限与独立抽样假设，才可按相应事件重新推导。论文未评估7轮设置；本轮未核实现代码是否有额外门禁。Theorem 1从相似向量密度及阈值过滤论证推广到任意确定性内容过滤，也缺乏足够假设（例如全拒绝过滤器不接受任意条目）；不能声称已证明所有无provenance检索防御必然失败。保留实验结果和条件化候选思路，不把论文证书当生产安全保证。

## 关联概念

- [[Agent-Security]]
- [[Agent-Attack-Surface]]
- [[Shared-Memory-Contamination]]
- [[Distinct-Principal-Identity]]
