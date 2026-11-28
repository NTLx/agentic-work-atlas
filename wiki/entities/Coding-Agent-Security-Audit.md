---
type: entity
title: Coding-Agent-Security-Audit
aliases:
  - Coding Agent 安全审计
  - Coding Agent Security Audit
  - DFD-VDF 审计范式
  - 数据流审计
definition: "面向Coding Agent的候选数据流审计设计：版本化的数据流声明（DFD）、实际运行与服务端保证证据（VDF）及未覆盖范围说明，以补充既有安全、隐私与控制审计；不是正式行业标准。"
created: 2026-07-17
updated: 2026-11-28
evidence_level: medium
claim_type: synthesized
tags:
  - security
  - AI-Agent
  - coding-agent
  - audit
related_entities:
  - "[[Context-Rot]]"
  - "[[Token-Supply-Chain]]"
  - "[[Flattening-as-Governance-Consequence]]"
  - "[[Least-Agency]]"
  - "[[Rogue-AI-Agent]]"
  - "[[Long-Lived-Credential-Risk]]"
source_raw:
  - "[[20260610-anthropic-ai-exploits-security-patches]]"
  - "[[20260518-zero-trust-for-ai-agents]]"
  - "[[20260414-cybersecurity-proof-of-work]]"
  - "[[20260801-tailscale-hugging-face-ai-agent-intrusion]]"
---

# Coding-Agent-Security-Audit（Coding Agent 安全审计）

> [!definition] 定义
> 本库提出的Coding Agent数据流审计设计：DFD（Data Flow Declaration，机器可读的数据流声明）+ VDF（Verified Data Flow，针对声明及实际运行的验证证据）+ 未覆盖范围说明。它是补充现有安全与隐私审计的候选框架，非已颁布、认证或独立验证的行业标准。

## 为什么需要数据流视角

工具、文件、代码执行、网络、委派与身份权限之间的组合可能形成新的风险路径；组合关系是威胁建模启发式，不是可计算的乘法定律，也不证明所有路径不可枚举。应针对具体版本、部署、插件和权限建立可达性与信息流模型。

[AICPA SOC 2说明](https://www.aicpa-cima.com/resources/download/get-description-criteria-for-your-organizations-soc-2-r-report)涵盖安全、可用性、处理完整性、保密和隐私相关控制；[ISO/IEC 27001:2022](https://www.iso.org/standard/27001)为适应组织规模与需求、随其演变的风险管理体系；不能将其描述为仅审计静态产品或已知攻击面。数据流声明和验证可以补充产品行为及实际部署证据，但不替代完整安全、隐私、合规审计。

## DFD + VDF：候选证据合同

| 层 | 核对对象 | 最小证据 |
|---|---|---|
| 声明（DFD） | 数据类别、触发条件、目的、处理方、目的地、保留期、训练/再利用选择、权限与版本 | 版本化文档/配置、可核对的数据流图和适用范围 |
| 运行验证（VDF） | 工具、文件、进程、网络、实际访问/传输、副作用与声明一致性 | 受控合成数据、访问与出站记录、独立运行证据、具体软件/配置版本 |
| 服务端保证 | 处理、保留、删除、第三方再传输与训练用途 | 适用合同、服务端审计及独立保证材料；注明未证实范围 |
| 控制与响应 | 最小权限、完整中介、预算、撤销、异常响应和补偿 | 负向授权用例、资源端终态、回归与恢复证据 |

**综合判断**：声明、实际传输、服务端保留、训练使用是不同命题。客户端观察到某域名、请求大小或网络活动，并不足以确定负载内容、服务器处理、后续保留或训练用途；未观察到某次传输也不是全版本/全路径不发生的证明。验证应在授权隔离环境中使用非真实敏感数据，按风险选择样本并保护审计记录。第三方审计的独立性、抽样、时间范围及盲区须明确。可信执行环境可提供特定技术保证，但不是通用服务端治理证明。

## 关键数据点

已有材料与证据边界：

- 2026-07 Grok Build案例：历史研究者报告0.2.99的代码库上传与隐私设置问题（[7月14日报道](https://www.theverge.com/ai-artificial-intelligence/965600/spacexai-grok-build-repository-upload)；早期研究者PRIVACY_OPTOUT文档本轮返回404，仅保留为历史线索）。[7月17日第三方复测](https://github.com/arafatkatze/grok-build-privacy-retest/blob/main/evidence/report.md)在0.2.102、已选择退出、一次受控任务中报告未见代码库上传或四个合成标记外传；云端推理请求及运营遥测仍存在。复测未切换所有设置、覆盖所有功能或核验服务端保留；公开源码快照与已签名二进制版本不同，不能声称可复现构建。不能把历史版本问题定性为所有版本“opt-out是假的”。
- [[20260801-tailscale-hugging-face-ai-agent-intrusion]]：前轮已校准的厂商事故反思，支持将凭据可读性、授权范围、隔离及撤销纳入审计；不是本轮独立取证。
- [[20260518-zero-trust-for-ai-agents]]：指南提供最小权限、身份、运行时治理与隔离设计；不是已验证的认证标准。参见[[Least-Agency]]、[[Policy-as-Code-for-Agent-Governance]]。
- [[20260610-anthropic-ai-exploits-security-patches]]、[[20260414-cybersecurity-proof-of-work]]：安全评估提示风险窗口与持续防御价值，不能由攻击能力实验推出DFD+VDF完整性或固定安全预算。
- 历史圆桌记录中的Iternal 65%/86%/14.4%、Lushbinary SBOM四阶段、IEEE-USA RFI、Northflank、Augment/Cursor等线索，本轮未获得足以核验样本、版本、指标定义或部署效果的原始材料；不保留为经证实统计或产品现状。需重新核验后才能引用。

## 工程验收原则

1. 先盘点任务合同、身份及有效权限，再定义必须允许和禁止的实际动作及数据流。
2. 以版本化声明约束可用数据、用途与目的地；不可把用户提示词当作实际授权。
3. 验证真实执行点及资源状态，含合理的拒绝、失败、撤销及重复执行条件；按风险检查替代接口和子组件覆盖。
4. 客户端证据与服务端保证分别报告；不得将未观察事件、TLS、签名、证书或日志视为整个系统安全证明。
5. 工具、模型、插件、授权、数据处理政策或环境发生实质变更时重验受影响范围。独立验收集和回滚路径可降低持续演化带来的验证盲区。

## 制度与标准化：历史推演的保留边界

2026-07-17/18模拟圆桌及追本讨论中的Schneier、Zuboff、Wu、Mickos、Hightower、Marlinspike、Beda等角色意见均为模型模拟观点，非本人真实发言、真实政策提案或已验证定理。历史讨论保留在研究日志和Git；这里仅保留可继续检验的假说：

- 企业安全、采购、法律、工程与开发者可共同要求供应商说明和验证数据处理。CISO是可能的组织杠杆之一，不是唯一行动者，也不能笼统断言其个人承担法律责任。
- 按目的、数据类别、接收方、保留期、再利用、删除及可验证性多维披露；是否用于训练不能单独决定总体保护强度，“去标识”也不必然匿名。原Tier1/2/3为历史设想，非认证或安全等级；标签可能产生误导性合规信号。
- 标准分类与测量口径影响可观察行为和市场激励；多方参与可能减少单边利益偏差。“定义权不可拆分定理”、固定公式、Fortune 500阈值和1–7年制度时间表无独立证据，降格为待验证机制或撤去精确预测。
- 身份认证、运行时授权和行为审计互补；SPIFFE等身份标准可提供部分基础，不能推出其必然成为市场赢家。无需等待统一标准才能使用现有资源端权限、审计和证据合同。

## 前提与局限性

DFD/VDF是本库综合，不是现有正式数据流标准；声明加抽样观察加盲区标注也不能称为完整审计。控制证据需要覆盖实际威胁与部署范围，必要时使用独立评估。安全收益、性能开销、组织采纳及市场效应尚待实证。2026-11-28核对上述公开资料及相关本地来源；未在本轮实测任何Coding Agent、未审计用户机器、未取得服务端私有日志或完整第三方保证。

## 关联概念

- [[Least-Agency]] — 最小能力、授权范围及完整中介。
- [[Policy-as-Code-for-Agent-Governance]] — 区分规则表达、执行与审计证据。
- [[Agent-Containment]] — 控制可达环境及真实副作用。
- [[Long-Lived-Credential-Risk]] — 凭据可读性、范围及生命周期。
- [[Token-Supply-Chain]] — 数据用途与价值链问题。
- [[Flattening-as-Governance-Consequence]] — 组织治理候选机制，非必然因果关系。
