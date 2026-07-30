---
type: raw
source: "https://ai.nejm.org/doi/10.1056/AIoa2500973"
title: "Implementation of an AI-Triggered Rapid Response — Association with Mortality"
author:
  - "Thomas A. Nahass"
  - "Joseph S. Hanna"
  - "Stephen P. O'Mahony"
published: 2026-07-29
created: 2026-07-30
description: "RWJBarnabas Health 与 Rutgers 团队在 NEJM AI 发表的真实世界实施研究：Epic Deterioration Index（EDI）在 11 家医院的系统级部署。EDI 持续读取 EHR 中的生命体征、实验室结果、护理评估与年龄，每 15 分钟重算风险，达到最高风险阈值时自动通知快速反应团队（RRT）。覆盖 23,132 名高风险患者：高风险患者院内死亡率从 23.1% 降至 18.6%（风险校正后院内死亡优势比下降约 18%）；RRT 介入比例从 25.3% 升至 37.5%；ICU 转入率未显著增加。研究性质为观察性实施效果研究（observational study），不能归因为算法单独作用——作者明确表态 'The mortality benefit was not produced by an algorithm but by the partnership around the algorithm'。对 Agentic Work Atlas 主线的价值：这是'AI 如何进入真实组织并沉淀为能力'的医疗现场样本——死亡率的下降来自模型 + EHR 集成 + 自动通知 + 医护培训 + 临床响应流程 + 持续监控的组合，即'风险识别—通知—责任人接收—临床评估—干预—复盘'闭环，而非一个风险分数。医疗 AI 项目失败模式清单（无明确告警责任人、告警时机不当、告警疲劳、未嵌入 EHR 与排班、缺乏跨院区标准化、无结局与工作量监控）与软件 agentic 部署的 harness/工作流设计问题同构。"
tags:
  - clippings
  - ai-implementation
  - organizational-change
  - healthcare-ai
  - clinical-decision-support
---

# Implementation of an AI-Triggered Rapid Response — Association with Mortality

*Thomas A. Nahass et al. (RWJBarnabas Health / Rutgers Robert Wood Johnson Medical School) · NEJM AI · 2026-07-29 · DOI: 10.1056/AIoa2500973*

> **剪藏说明**：NEJM AI 原文为付费/受限内容，多通道抓取均失败；本剪藏以 EurekAlert 官方新闻稿全文为主体（含论文元数据、全部关键数据与作者引述），News-Medical 解读内容与之高度重合，仅列链接。

---

Researchers from [RWJBarnabas Health](https://www.rwjbh.org/) and [Rutgers Robert Wood Johnson Medical School](https://rwjms.rutgers.edu/) found that an artificial intelligence (AI)-enabled early warning system helped identify hospitalized patients at risk of rapid clinical decline sooner, contributing to fewer deaths among high-risk patients.

Published in *[NEJM AI](https://ai.nejm.org/)*, a journal from the *New England Journal of Medicine* group (*DOI: 10.1056/AIoa2500973),* the study evaluated outcomes among 23,132 high-risk patients across 11 RWJBarnabas Health hospitals. Deaths among high-risk patients fell from 23.1 percent to 18.6 percent following implementation of the AI-enabled early warning system, representing an 18 percent reduction in the risk-adjusted odds of in-hospital death.

Hospitalized patients can deteriorate quickly, often before obvious warning signs become apparent. Researchers evaluated the Epic Deterioration Index (EDI), an AI-enabled tool that continuously analyzes information already captured in the electronic health record, including vital signs, laboratory results, nursing assessments and age, to identify patients at increased risk of serious clinical decline. The system recalculates risk scores every 15 minutes and automatically alerts rapid response teams when patients reach the highest-risk category.

Before evaluating the technology in this study, RWJBarnabas Health and Rutgers spent several years developing and implementing a systemwide approach to using the EDI across its hospitals. The health system first integrated the tool into its electronic health record at its academic medical center, Robert Wood Johnson University Hospital, to pilot and refine it, including, how and when alerts were delivered, established automatic notifications to rapid response teams, trained clinicians on its use and continuously monitored its performance. Researchers from Rutgers then partnered with RWJBarnabas Health to evaluate the impact of this approach in real world clinical practice and rapidly rolled out the platform the other 10 hospitals.

"Our goal was to identify patients earlier, before they reached a point where intervention becomes much more difficult," said [Thomas Nahass, MD](https://mychart.rwjbh.org/MyChart/-/providers/ThomasNahassMD/WP-24woUXtILpDu6ayzM41alCVA-3D-3D-24ZW8EOER0Jx0RDmro6laZZsSzx6JwCBpa5hO1JupzLSo-3D), VP of Health Informatics and intensive care physician at RWJBarnabas Health, and Assistant Professor of Medicine at Rutgers Robert Wood Johnson Medical School and lead author of the study. "The deterioration index gives us an earlier point in time. If we can get a critical care eye on the patient sooner, we can change the course of their outcome."

When patients reached the highest-risk threshold, automated notifications were sent directly to hospital rapid response teams, enabling critical care specialists to quickly assess patients and determine whether additional interventions were needed. Following implementation, rapid response team activations among high-risk patients increased from 25.3 percent of hospital stays to 37.5 percent.

The study evaluated outcomes among high-risk adult patients receiving care at academic medical centers, community teaching hospitals and community hospitals throughout the RWJBarnabas Health system. Despite the increase in rapid response evaluations, transfers to intensive care units did not significantly increase, while mortality rates declined substantially.

"Every minute matters when a patient's condition begins to worsen," said [Andy Anderson, MD](https://www.rwjbh.org/why-rwjbarnabas-health-/leadership/), Chief Medical and Quality Officer, RWJBarnabas Health and study co-author. "This study demonstrates how AI-enabled tools, when paired with experienced clinical teams can help us identify patients at risk sooner and deliver the right care at the right time. These findings highlight the potential for innovation to improve quality, safety and outcomes for the patients we serve."

"This is what an integrated academic health system is for," said **Stephen P. O'Mahony, MD, FACP,** Senior Vice President and Chief Medical Information Office at RWJBarnabas Health and senior author of the study. "We combined Rutgers methodological rigor with the operational reach of 11 RWJBarnabas hospitals. The mortality benefit was not produced by an algorithm but by the partnership around the algorithm."

Researchers note that the mortality benefit likely resulted from a combination of factors, including staff education, enhanced clinical awareness, electronic health record alerts and automated rapid response team notifications working together as a coordinated systemwide approach. Because the study evaluated the Epic Deterioration Index, a tool already available within Epic, one of the nation's most widely used electronic health record systems, the findings may have implications for hospitals nationwide seeking to improve patient outcomes. Researchers are now evaluating the next phase of the initiative, which focuses on identifying patients whose risk scores are rising rapidly in hopes of enabling even earlier intervention.

*Along with Drs. Nahass and O'Mahony and, authors include: Co-first author Joseph S. Hanna, MD, Rutgers Robert Wood Johnson Medical School and Robert Wood Johnson University Hospital; Nancy Liu, MPH, and Jason Roy, PhD, Rutgers School of Public Health; Nicole Martinez, RWJBarnabas Health; Ethan A. Halm, MD, MPH, MDA, Rutgers Robert Wood Johnson Medical School; Amy Rockman, Rutgers Biomedical and Health Sciences; Christopher Gilligan, MD, MBA, Robert Wood Johnson University Hospital; Amy P. Murtha, MD, Rutgers Robert Wood Johnson Medical School and Vicente Gracias, MD, MD, FACS, FCCP, FCCM, Rutgers Biomedical and Health Sciences*

---

## 论文元数据（EurekAlert 提供）

- **Article Title**: Implementation of an AI-Triggered Rapid Response — Association with Mortality
- **Journal**: NEJM AI
- **DOI**: [10.1056/AIoa2500973](http://dx.doi.org/10.1056/AIoa2500973)
- **Method of Research**: Observational study
- **Subject of Research**: People
- **Article Publication Date**: 29-Jul-2026

## 相关链接

- NEJM AI 原文：https://ai.nejm.org/doi/10.1056/AIoa2500973
- EurekAlert 新闻稿（本剪藏主体）：https://www.eurekalert.org/news-releases/1137831
- News-Medical 数据与实施细节解读：https://www.news-medical.net/news/20260729/AI-enabled-tool-helps-identify-hospitalized-patients-at-risk-of-rapid-clinical-decline.aspx

## 剪藏笔记（用户判断，非 source 内容）

**优先级**：最高。**类型**：真实世界临床实施研究。

高价值判断——这是医疗 AI 行业非常重要的方向修正：

> 医疗 AI 的真正产品不是一个风险分数，而是"风险识别—通知—责任人接收—临床评估—干预—复盘"的闭环。

很多医疗 AI 项目失败，并非模型 AUC 不够高，而是：

- 没有明确谁负责处理告警；
- 告警时机不合适；
- 告警疲劳严重；
- 模型没有嵌入 EHR 和临床排班；
- 缺乏跨院区标准化实施；
- 没有监控患者结局和工作量变化。

因此，这项研究对医疗 Agent 和临床决策支持系统的启示，是应当把**组织工作流设计**和模型开发放在同等甚至更高的位置。
