---
type: source-summary
title: "Agents that can pay: building Restock with Stripe's Link and Managed Deep Agents"
canonical_url: "https://www.langchain.com/blog/agents-that-can-pay-with-stripe-link"
raw_state: index
original_raw_file: "20261008-langchain-stripe-link-agent-payments.md"
original_body_sha256: "6d032cdd19112242f20f14282fd2840b4991e5a03e93a1b12a3b849282ded0dc"
indexed_at: "2026-11-06T00:57:55.293Z"
created: 2026-11-06
updated: 2026-11-06
tags:
  - source-summary
  - agent-security
evidence_level: medium
claim_type: mixed
source_locator:
  - "Original article section: Key Takeaways"
  - "Original article section: Choosing how to pay"
  - "Original article section: How the pieces fit"
  - "Original article section: Search and cart"
  - "Original article section: Setting the upfront amount"
  - "Original article section: Keeping credentials out of the model"
  - "Original article section: Reviewing the purchase in Slack"
  - "Original article section: Paying with Link over MPP"
  - "Original article section: Confirming the order"
  - "Original article section: Get started"
---

# Agents that can pay: building Restock with Stripe's Link and Managed Deep Agents

> 证据来源：https://www.langchain.com/blog/agents-that-can-pay-with-stripe-link（2026-10-08，Srimanth Tangedipalli、Sydney Runkle、Nathan Drezner）。2026-11-06 读取官方网站公开正文并逐节核对。原文以 canonical URL 为权威；本 Wiki 保存自撰释义、章节定位和推理边界，不存储网页逐字全文；original_body_sha256 仅记录临时来源索引记录的哈希，**不是**网页全文校验值。**本文数据若未注明独立验证，均为该来源的报道/作者陈述。**

## 编译摘要

### 1. 浓缩

- **核心结论 1：Agent 可以搜索与准备交易，但财务授权不能由模型文本代替。**
  - **原文证据**：Restock 是运行于 Slack/Managed Deep Agents 的样例：Zinc 检索商品、准备购物车；Stripe Link 持有用户支付凭证；MPP 使用 HTTP 402 返回支付要求；先 Slack 确认购物车和金额，再由 Link 再次明确批准。

- **核心结论 2：预算、授权、凭证与订单状态是四类不同的控制对象。**
  - **原文证据**：样例上限 25 美元，用户批准 23 美元预付；工具验证商品、费用、审批时效；Link session 属用户 Connection，商家 API key/地址属 Agent Connection，支付 token 临时使用并不向模型暴露。真正成交以 Zinc 返回 order_placed 确认，而非模型的自述。

- **核心结论 3：HTTP 原生支付协议降低浏览器支付脆弱性，但覆盖性有限。**
  - **原文证据**：作者对照浏览器代填信用卡的易碎流程与 MPP-enabled API 的明确支付契约，提供 rehearsal、link-test、live 三阶段测试；样例实际完成一次托管部署的交易并收到退款。

### 2. 质疑与证据边界

- 示例价格被明确标注为演示数字，不得当作一般产品费用或标准计费。
- 样例仅支持美国、美元、单办公室部署，不是生产支付系统的独立安全认证。
- MPP 需要商家或聚合平台支持，human approvals、幂等、退款争议处理仍需要专门实现。

### 3. 对标与应用约束

- **跨域迁移（综合判断，非原文证实）**：与 [[Agent-Security]] 的确定性执行/授权/撤销链相连：把购物车签名、预算上限、审批身份、token 隔离与商家回执作为模型外不变量。
- **使用前提**：任何架构类比只能用于提出评测与工程变更候选；生产推广需真实权限、失败恢复、成本与回归实测。

## 重要判断（Claim / Evidence / Boundary）

- **判断**：Agent 可以搜索与准备交易，但财务授权不能由模型文本代替。
  - **证据**：一手来源 [Agents that can pay: building Restock with Stripe's Link and Managed Deep Agents](https://www.langchain.com/blog/agents-that-can-pay-with-stripe-link)，定位至「Key Takeaways / Choosing how to pay / How the pieces fit / Search and cart」及上方事实摘要。
  - **边界**：示例价格被明确标注为演示数字，不得当作一般产品费用或标准计费。

### 关联概念

- [[Agent-Security]]
- [[Agent-Verification]]
- [[Human-Governor-Agent-Operator]]
