---
type: research-log
title: "研究日志 2026-09-06：AI 采用与劳动市场四层测量交叉校准"
date: "2026-09-06"
tags:
  - research-log
  - labor-economics
  - ai-adoption
  - measurement
---

# 研究问题

2026 年公开的一手来源，能否在同一测量框架内连接：AI 采用企业的净 headcount／招聘变化、职业或任务层暴露、entry-level／early-career 流量变化，以及培训／专业能力再生代理？

**Result：可以建立共同测量契约，并找到若干已经实现的局部连接；不能据本轮公开材料直接合并出覆盖四层的共同样本或效应量。** 最接近企业侧连接的是丹麦官方调查与行政记录的研究材料；最接近美国职业—青年流量连接的是 Anthropic/CPS 与 Stanford/ADP。培训调查补的是投入或可得性，编码实验补的是短期独立技能结果；这些来源没有公开的共同企业—个人标识。以下结论限于本轮核验集，不声称穷尽所有 2026 年研究。

本轮只交付本日志；不创建 Claim/EX、不更新 agenda/index、不晋升稳定 Wiki。检索与版本截止为 **2026-09-06**。2026 指公开研究版本年份，不要求底层观测全部发生于 2026；旧数据年份另列，不能包装成 2026 年已经发生的变化。

# 来源身份与版本门

| 编号 | 原始来源、publication/date/version | 纳入用途与身份边界 |
|---|---|---|
| S1 | Abel、Deitz、Emanuel、Montalbano，纽约联储 [Businesses Are Using AI to Transform Work, Not Cut Jobs](https://libertystreeteconomics.newyorkfed.org/2026/09/businesses-are-using-ai-to-transform-work-not-cut-jobs/)，**2026-09-01**；配套 [Chart Data](https://libertystreeteconomics.newyorkfed.org/wp-content/uploads/sites/2/2026/09/LSE_2026_AI_Survey_Charts_data_98b72a.xlsx) | 调查执行机构研究者直接报告 2026-08 区域企业调查；文章与工作簿同源，不计作两份独立证据。 |
| S2 | Yotzov 等，[Firm Data on AI](https://www.atlantafed.org/-/media/Project/Atlanta/FRBA/Documents/research/publication/working-paper/2026/03/24/03-firm-data-on-ai.pdf)，Atlanta Fed **Working Paper 2026-3，2026-03**，采用该 PDF 版本 | 美英德澳企业调查原作者工作论文；核对问法、权重与回溯/预期差异，不将作者结论视为央行政策立场。 |
| S3 | Bonin、Darougheh、Kuchler，[Prompting Change](https://www.bankofengland.co.uk/-/media/boe/files/events/2026/s-darougheh-slides.pdf)，封面标明 **BoE CCBS，2026-06-24**，30 页公开会议材料 | 丹麦央行研究者对 Statistics Denmark 调查和行政数据的原始研究报告；**暂定证据，非完整论文**。会议版本日期可确认，单独上传日未标明。页码以下均指 PDF 物理页。 |
| S4 | Massenkoff、McCrory，Anthropic [Labor market impacts of AI](https://www.anthropic.com/research/labor-market-impacts)，**2026-03-05；网页 2026-03-08 更正 Figure 7 图例**；[方法附录](https://cdn.sanity.io/files/4zrzovbb/website/e5f77fc0e77c0185110b5e4b909602791ae76eae.pdf)，2026-03 | 平台原始使用数据与 CPS 的作者分析。采用更正后的网页解释青年流量；附录与主文同源。 |
| S5 | Brynjolfsson、Chandar、Chen，[Canaries in the Coal Mine?](https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf)，封面 **2026-08**；[作者机构发布页](https://digitaleconomy.stanford.edu/news/canariesaug26/)确认 **2026-08-12** | 原作者使用 ADP 行政工资单的 2026 年修订论文；不沿用 2025 版标题数字或混入滚动 dashboard 的较新月份。 |
| S6 | Hashim、Kosar、van der Klaauw，纽约联储 [Use of Gen AI in the Workplace and the Value of Access to Training](https://libertystreeteconomics.newyorkfed.org/2026/04/use-of-gen-ai-in-the-workplace-and-the-value-of-access-to-training/)，**2026-04-14** | SCE 执行机构研究者对 **2025-11** 补充问卷的原始分析；2026 发表不等于 2026 员工状态。 |
| S7 | Shen、Tamkin，[How AI Impacts Skill Formation](https://arxiv.org/html/2601.20245v2)，**arXiv:2601.20245v1，2026-01-28；采用 v2，2026-02-01**；[版本记录](https://arxiv.org/abs/2601.20245) | 作者随机实验原文。HTML 正文还显示 August 24, 2026，版本身份以 arXiv 提交记录及固定 v2 为准，不将渲染日期当作新研究版本。 |

**排除／背景：** 纽约联储 [How Retrainable Are AI-Exposed Workers?](https://www.newyorkfed.org/research/staff_reports/sr1165)及其 [PDF](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr1165.pdf)均标 **2025-08，Staff Report 1165**，未确认 2026 修订，故不拿它补培训结果缺口。S4 内引用的 **2025 年发布、预测 2024–2034 的 BLS 职业预测**也不作为本轮 realized 主证据；其身份由 [S4 的预测小节](https://www.anthropic.com/research/labor-market-impacts)说明。S3 底层旧问卷即使存在培训题，也不能仅凭当前可访问就升级为已核实的 2026 四层研究结果。

# 逐来源证据与限制

## S1：同一企业调查能并列招聘调整与再培训，不能计算净岗位数

**事实：** 观测单位为纽约及北新泽西地区受访服务业／制造业企业；2026-08 询问过去六个月 AI 使用与用工调整，纯信息检索用途不计采用。采用率分母为各行业受访企业；用工行动图分母则是各行业 **AI 使用企业**。已读取官方工作簿 `Chart 3`：服务业报告少招、多招、裁员、再培训的比例分别为 **15%、13%、4%、34%**，制造业为 **6%、0%、0%、22%**。[S1 正文及图表口径](https://libertystreeteconomics.newyorkfed.org/2026/09/businesses-are-using-ai-to-transform-work-not-cut-jobs/)、[工作簿](https://libertystreeteconomics.newyorkfed.org/wp-content/uploads/sites/2/2026/09/LSE_2026_AI_Survey_Charts_data_98b72a.xlsx)

**测量边界：** 这是过去行动的自报；“少招”仍依赖企业对没有 AI 时会招聘多少人的反事实归因。工作簿只给边际比例，无企业行、交叉频数、行动涉及人数或标准误；本文与工作簿未充分披露本次各题有效样本数及权重细节。区域调查覆盖与应答选择是主要偏差，不能按平台用户样本理解，也不能外推全国。未观测字段包括职业代码、年龄／毕业年／职级、培训人数和技能结果。

**推断：** `13% − 15% − 4%` 没有净 headcount 含义：每家企业行动人数不同，行动也未被说明互斥。34% 是提供再培训的采用企业比例，不是34%的员工学会了新技能。**缺口：** 同企行动联表、人数和职业—青年—培训交叉分布。

## S2：作者称 realized 的就业影响，仍须与行政实绩分开

**事实：** 近 6,000 名美英德澳企业高管受访；AI 模块在 **2025-11 至 2026-01** 施测。美国 SBU、英国 DMP、德国 BOP-F 结果按就业加权，澳洲 BOSS 不加权；跨国合计按调查回应数加权。过去三年影响与未来三年影响分别提问，再将五档答案赋值为 0、±2.5、±7.5；Table 4 的就业合计分别为 **0.00%** 与 **预期 −0.68%**。[S2，方法、Figures 8–9 与 Table 4](https://www.atlantafed.org/-/media/Project/Atlanta/FRBA/Documents/research/publication/working-paper/2026/03/24/03-firm-data-on-ai.pdf#page=37)

**测量边界：** 单位是企业高管回答，分母不是 AI 裁撤岗位或青年求职者。过去三年指标是自报归因后赋值的影响量，不是两期工资单人数之差。国别抽样框、权重、施测月不同，合计也不是四国劳动人口共同权重。研究覆盖存续企业，存在应答及回溯偏差；无共同职业、青年、培训结果字段，另行调查的员工样本不能与企业逐一配对。[S2，数据与研究范围](https://www.atlantafed.org/-/media/Project/Atlanta/FRBA/Documents/research/publication/working-paper/2026/03/24/03-firm-data-on-ai.pdf)

**推断：** 可以在共同表中保留 `reported_retrospective_attribution` 和 `expected` 两类值；不能把 0.00% 标成实际净 headcount 不变，也不能与 S1 的行动企业比例相减。**缺口：** 同企可核验的人数变化、原始回答档及其与采用状态的交叉分布。

## S3：企业采用—行政用工—青年已经连接，培训仍未进入公开结果

**事实：** 2023/2024/2025 企业 IT Usage Survey 接入 **2018–2025 月度 BFL 雇主—雇员记录**；企业背景数据只到2024。描述表含 **4,468 家匹配企业、746,802 名员工**，总体范围为至少10名员工企业。设计比较2023首次采用者与从未采用者，使用调查权重、行业/规模/时间控制及企业采用前趋势；结果变量包括 **log FTE employment**、小时工资、季度招聘/离职。公开材料报告采用者 FTE 相对预趋势约低8%，调整集中于30岁以下，主要经少招；这是描述性事件研究。[S3，PDF pp.5–12](https://www.bankofengland.co.uk/-/media/boe/files/events/2026/s-darougheh-slides.pdf#page=5)

**测量边界：** FTE 是全职当量，不是人数；不能把约8%写成实际裁员8%。匹配样本比总体企业更大、出口商更多；采用非随机，趋势处理不能自动消除选择偏差。职业暴露图使用 Felten/Raj/Seamans 2023 理论指标，不是 S4 的 Claude observed exposure。材料对职业异质性的标题用 substitutability，正文又用 augmentation-exposed，分类及映射不足以复刻，本轮不替作者消解这个差异。[S3，PDF pp.6–12](https://www.bankofengland.co.uk/-/media/boe/files/events/2026/s-darougheh-slides.pdf#page=6)

**缺口：** 正式论文、实际连接键与职业 crosswalk、各回归有效分母、招聘/离职详细定义及准确末月均需补充；公开材料未报告培训、职级、毕业年或技能测评。**推断：** 它证明前三层可在受控微数据中连接，尚未证明研究者已将培训接入，也未向公众提供可直接合并的个体联表。30岁以下不能直接换成22–25岁或所有 entry-level 岗位。

## S4：职业任务暴露已接到青年新工作流量，但没有识别雇主采用

**事实：** 2026-03 研究使用 **2025-08、2025-11** Claude 数据构造职业暴露：工作用途与 API 任务通过流量门槛后，结合理论可行性、自动化权重和估算任务时间占比。附录强调该指标**不是纯任务覆盖百分比，也不测使用强度**。O*NET-SOC 经 crosswalk 接 CPS `occ1990`；青年分析使用22–25岁者相邻月的新工作报告，比较高暴露与零暴露职业。[S4 主文、脚注5/7](https://www.anthropic.com/research/labor-market-impacts)、[附录 pp.2–4](https://cdn.sanity.io/files/4zrzovbb/website/e5f77fc0e77c0185110b5e4b909602791ae76eae.pdf#page=2)

**测量边界：** 劳动结果是调查观测，暴露则含平台采样、模型分类与时间权重估算。报告自2016起比较失业趋势、以 ChatGPT 发布后为处理期；未在已核对方法中明确全部分析的最终月份及青年流量匹配/权重细则，故本轮不猜。青年图分母描述为年轻工人样本，不能擅自改成“上月失业者”；它不只代表首次就业。正文称新工作率相对2022下降约14%，仅边缘显著；这不是就业存量或裁员比例。[S4，Figure 7 与限制](https://www.anthropic.com/research/labor-market-impacts)

**偏差与缺口：** Claude 的客户、任务及 API 构成不代表所有 AI；低流量任务可能被记零，共享任务归属依赖分配。把2025暴露回接2022后的劳动变化，还存在后验暴露选择问题。CPS 转换误报、无历史职业的新进入者及退出劳动力市场者影响解释。未连接雇主 AI 采用、岗位职级或培训结果。**推断：** 这是一条可复用的职业层连接方法，不能据此宣称“采用 AI 的企业少招了14%的新人”。

## S5：工资单能拆存量与流量；公开汇总仍不提供企业采用和培训

**事实：** 固定采用2026-08论文，主样本为 **2021-01 至2026-06** 每月约350万至500万全职、70岁以下、正收入 worker–firm matches，企业保持在平衡面板。22–25岁高暴露职业的 **19%** 指相对低暴露组增长路径的就业存量缺口；招聘另定义为上月没有、本月出现的同企雇佣配对，离职反向；流量率用滚动12个月次数除以该年龄×暴露组12个月前存量。[S5，PDF pp.6–7、10–11、140](https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf#page=140)

**测量边界：** 职位名映射到 SOC 后接职业暴露，缺职位名记录涉及插补/剔除。ADP 客户、可分析子样本及持续存在企业造成选择；行业/规模结构有偏，作者明确将结果定位为描述性，且 ADP 差距比全国调查更明显。年龄是 early-career 代理；新增配对含换雇主，不等于应届生首次入职，离职不等于裁员或失业。[S5，PDF pp.6–7、29–32、41–44](https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf#page=30)

**缺口：** 匿名企业不能接实际采用信息；州/职业层使用代理不能补这个字段。没有个人培训或独立能力结果。公共 dashboard 可下载聚合序列，但本轮未确认可按完整 SOC 逐职业连接的公开结果表；不能把内部微数据可连接误写为公众已可连接。**推断：** S4 与 S5可以相互校准“青年进入变慢而非离职激增”的方向，但14%流量估计与19%存量差距不能平均，也不能当成独立的企业采用因果效应。

## S6：员工培训可得性有测量，培训完成与技能再生没有

**事实：** 2026-04 发表、2025-11 SCE 补充调查。当前就业者中39%报告当前或过去12个月工作使用 AI；**15.9%** 报告雇主当前提供 AI 培训。无培训者回答为获得培训愿放弃多少工资；有培训者回答为失去培训需补偿多少，分别是不同条件样本、不同方向的假想选择。作者明确提供培训不表示员工已参加或掌握技能。[S6，使用、培训与估值小节](https://libertystreeteconomics.newyorkfed.org/2026/04/use-of-gen-ai-in-the-workplace-and-the-value-of-access-to-training/)

**测量边界：** 单位为员工回答，培训比例分母为就业受访者，不是采用 AI 的企业。自报使用/培训可得性属于回溯或当前状态；支付意愿、失业预期属于陈述偏好或 expected，均非实现的工资/失业变化。调查称总体代表性，但本轮材料未充分给出补充题有效N、逐题权重与不应答调整；已就业者选择也不代表尚未进入职场者。

**推断：** S1 的34%与 S6 的15.9%不可解释为企业承诺与员工获得培训的差额：地区、月份、分母和培训定义均不同。短工龄、年轻与初级职级也不是同一变量。**缺口：** 企业标识、职业交叉表、培训参加/完成、独立能力与后续招聘结果。

## S7：独立技能测验提供结果代理，不能替代职业能力再生产率

**事实：** 主实验52人、每组26人；有 Python 使用经验、未用过 Trio 的受试者随机获得或不获得 AI 辅助，随后均在无 AI 条件下做理解测验。编码阶段至多35分钟；测验14题、总分27。论文报告组间差4.15分，AI组较低，`d=0.738, p=0.010`；平均完成时间差不显著。参与者经第三方众包平台招募，大多25–35岁；Table 1 中只有4人编程经验1–3年，因此“对新库不熟悉”不能当成“全是初级员工”。[S7，§4.2–5.2、Table 1](https://arxiv.org/html/2601.20245v2)

**测量边界：** 实际观测是单次学习后的无 AI 成绩与任务时间；不是预期，也不是长期职业能力。具体实验日历日期未在已核验方法中确认。样本筛选、付费参与、任务/工具/时间限制限制外推；随机分配只识别本实验条件下的技能获取效果，后验互动模式分类不等于随机培训方法。论文同时称分差为17%，本日志保留原始分数尺度，不将其另写成通用的“能力下降17%”。

**缺口：** 无雇主采用、雇佣流入流出、培训组织投入、延迟保持、跨任务迁移或晋升数据。**推断：** 它足以要求共同框架增加“撤去 AI 后能否独立完成”结果栏；不足以量化一个职业每年再生多少合格专业人员。

# 横向字段表

`R-admin`＝行政观测；`R-survey`＝实际状态/行为自报；`A-retro`＝回溯归因；`E`＝预期/假想选择；`X`＝实验结果。空缺不编码为零。

| 来源 | 单位／时间窗／分母 | 企业净用工与招聘 | 职业／任务暴露 | 青年入口 | 培训／能力 | 可连接性与主要缺项 |
|---|---|---|---|---|---|---|
| [S1](https://libertystreeteconomics.newyorkfed.org/2026/09/businesses-are-using-ai-to-transform-work-not-cut-jobs/) | 区域企业；2026-08回看6个月；行动以AI使用企业为分母 | R-survey+A-retro；行动占比，无人数净额 | 企业采用，无统一职业码 | 缺 | 企业是否再培训；无个人结果 | 同调查可并列；公开表无企业行或行动交叉分布 |
| [S2](https://www.atlantafed.org/-/media/Project/Atlanta/FRBA/Documents/research/publication/working-paper/2026/03/24/03-firm-data-on-ai.pdf) | 高管/企业；2025-11至2026-01；国别权重不同 | A-retro过去3年、E未来3年；非行政净人数 | 企业采用类型；无共同任务层 | 缺 | 缺 | 同问法可整理国别估计；不能视作统一人口的实际变化 |
| [S3](https://www.bankofengland.co.uk/-/media/boe/files/events/2026/s-darougheh-slides.pdf) | 丹麦匹配企业/员工；行政2018–2025；调查权重 | R-admin；FTE与季度招聘/离职 | 采用调查+理论职业暴露；完整映射待补 | <30岁；无职级/毕业年 | 公开结果缺 | 内部已连前三层；公众无微观联表；FTE≠人数 |
| [S4](https://www.anthropic.com/research/labor-market-impacts) | 任务→职业→CPS人月；暴露2025-08/11；精确流量风险集待补 | R-survey职业失业/新工作；无同企总量 | Claude观察+理论门槛+模型权重 | 22–25岁月度新工作率 | 缺 | 职业crosswalk可锚接；无雇主采用与培训 |
| [S5](https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf) | ADP人企配对；2021-01至2026-06；存量或12月前存量 | R-admin；headcount、招聘、离职分开 | SOC职业层外部暴露/使用代理 | 22–25岁；新增人企配对 | 缺 | 内部职业连接；外部无真实企业采用/培训键 |
| [S6](https://libertystreeteconomics.newyorkfed.org/2026/04/use-of-gen-ai-in-the-workplace-and-the-value-of-access-to-training/) | SCE员工；2025-11及过去12月；就业者/条件子样本 | 无同企净额；E失业判断 | 员工自报使用，非任务量表 | 年龄/工龄异质性，非招聘流量 | R-survey培训可得性；E估值 | 可校准员工侧变量定义；无企业联表/能力结果 |
| [S7](https://arxiv.org/html/2601.20245v2) | 受试者×学习任务；单次实验；主样本52人 | 缺 | 随机AI辅助，不是职业暴露 | 新库初学者，非劳动力入口 | X无AI测验；无长期保持 | 实验内部可连行为与成绩；不能连接上述企业/员工样本 |

# 共同框架及不可越过的边界

以下是**本轮设计与推断**，不是任何来源已经实现的综合数据库。

1. **统一字段，不统一分母。** 企业比例、员工比例、岗位数、FTE、任务权重、测验分数分别保留；每个数必须携带分母、权重、单位与估计对象。跨源进入长表只代表可比较其定义，不代表可合并估计。
2. **采用、暴露、使用三列分开。** 企业部署、职业技术可行性、平台观察使用不能互相填缺。模型估算任务时间也不能当企业实际工时。
3. **存量与流量分开。** 固定企业范围的人数变化可按新增雇佣减离职核算；职业/年龄小组还需单列换岗、跨年龄档，企业样本需单列进入/退出。FTE另受工时变化影响，不能直接套人数恒等式。
4. **青年不等于初级。** `age`、毕业至今时长、职业经验、企业工龄、岗位职级、首次就业分别记录。S3的<30、S4/S5的22–25、S7的新库初学者不存在可靠的一对一换算。
5. **培训是多段链。** 提供→参加→完成→练习/导师投入→无AI独立成绩→延迟保持/迁移→持续胜任。S1/S6与S7只占不同段，不能据前者证明后者，也不能把短测验外推为专业群体再生率。
6. **公开研究不等于公开微数据。** 内部可连接的企业/个人记录不能靠共同国家、行业或年龄在外部硬拼；行业均值附给个人只构成生态层代理。美国、丹麦、英国的数据先保留国别，不直接拼成“AI采用企业总体”。
7. **描述相关不自动升级因果。** S3/S5中的采用前趋势、行业选择及样本存续会影响解释；S4的暴露版本也晚于部分结果。S7的局部随机化不能替宏观就业研究补识别。

## 最小共同 schema

采用“来源—估计项长表 + 可选微观连接键”，不要求所有来源都有同一行粒度：

| 字段组 | 最小字段 | 规则 |
|---|---|---|
| 来源与版本 | `source_id, official_url, publication_date, version, accessed_at, locator` | 2026公开版本与底层数据年份分别校验；同源报告/附录/表格保持同一ID |
| 样本与时间 | `country, population, observation_unit, sample_n, period_start, period_end, frequency, weight_definition` | N与加权分母分别存；未知明确标缺，不用报告发布日期补观测末月 |
| 可连接键 | `firm_id, person_id, occupation_code, occupation_code_system, crosswalk_version` | 缺键保留为空；职业多对多转换保留权重/歧义；不构造假企业ID |
| 采用与暴露 | `adoption_definition, adoption_date, adoption_intensity, exposure_type, exposure_version, task_id, task_weight` | 理论、平台使用和企业/员工实际采用分别存；时间戳避免前视信息 |
| 职业阶段 | `age, graduation_year, occupation_experience, firm_tenure, job_level, first_job_flag` | 未测职级不能由年龄自动推定 |
| 估计对象 | `metric, numerator_definition, denominator_definition, value, unit, status, horizon, comparison_group, uncertainty` | status区分R-admin/R-survey/A-retro/E/X；区分水平、变化、相对差距与对数系数 |
| 用工 | `headcount_start, headcount_end, fte, hires, separations, within_firm_transfers, cohort_transitions, panel_entry_exit` | 同一范围/周期才能核算；招聘需求/职位发布另列，不能当实际入职 |
| 培训与能力 | `training_offered, participants, completions, hours, mentored_practice, unaided_score, delayed_score, qualification_date` | 至少分“投入、参与、独立结果”；专业再生须能跟踪新人达到事先定义的胜任门槛 |
| 可审计性 | `evidence_or_inference, missing_fields, selection_limits, linkage_access` | 区分公开可复算、受限微数据可连接、仅方法锚接 |

**可以直接合并的字段：** 来源日期/版本、国家、观测窗口、指标单位及状态，可进入以上证据长表；S1同工作簿同年/行业行动边际、S2同问卷国别/过去未来结果可作有标签的并列整理。此处“合并”只指元数据与已公布估计项，不指合并样本或计算一个净效果。

**只能锚接的字段：** S4/S5的职业暴露—年龄—流量可通过明确版本的职业映射和统一风险集做重新估计；当前只能比较方向与定义。S3已展示企业采用与行政结果的内部连接，须取得受限数据及完整方法后才可扩展。S1/S6为培训供给和员工获得感提供问卷设计，S7为独立能力结果提供测验设计，均不能直接接成同一批人的路径。

**无法合并的字段：** 行动企业占比与净岗位数、FTE与headcount、月度新工作率与滚动年度人企流入率、回溯归因与未来预期、不同青年/初级定义、培训可得性/支付意愿与技能保持；缺共同ID的来源不能拼成个人或企业面板。[对应证据：S1](https://libertystreeteconomics.newyorkfed.org/2026/09/businesses-are-using-ai-to-transform-work-not-cut-jobs/)、[S3](https://www.bankofengland.co.uk/-/media/boe/files/events/2026/s-darougheh-slides.pdf)、[S4](https://www.anthropic.com/research/labor-market-impacts)、[S5](https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf)、[S6](https://libertystreeteconomics.newyorkfed.org/2026/04/use-of-gen-ai-in-the-workplace-and-the-value-of-access-to-training/)、[S7](https://arxiv.org/html/2601.20245v2)

# 可证伪方向

- **推翻“尚不能四层联测”：** 找到截止日前公开的2026一手研究，明确在同一企业—员工面板中测量采用、职业暴露、实际青年招聘/离职及培训后的能力结果，并公开足以审计的字典、时间窗和连接方法。仅宣称用了四类数据不满足条件。
- **检验“青年招聘而非离职是主要调整边际”：** 在同一职业映射、年龄定义、国家、样本与时间窗下重算H/S；若差异主要来自年龄跨档、职业重编码、企业退出或分母收缩，应收窄S4/S5的解释，不能保留宽泛机制结论。
- **检验培训代理是否有效：** 同一入职队列中培训提供/完成增加，但无AI测验、延迟保持及达到独立胜任门槛的人数不变或下降，则“再培训比例上升＝能力再生”被否证。
- **检验暴露锚接能否迁移：** 使用统一职业权重分别套理论暴露、Claude使用暴露、企业实际采用，若排序/青年结果方向随平台与映射大幅改变，应停止合成一个通用暴露效应。

# Source 需求

| 优先级 | 下一份最有价值的来源 | 要补的字段／通过条件 |
|---|---|---|
| P0 | S3《Prompting Change》的2026正式公开稿、方法附录或官方微数据说明 | 精确采用时点、person/firm连接方法、职业量表及crosswalk、FTE与人数分解、H/S定义；确认培训题是否确实进入同企分析，不能拿旧问卷代替结果 |
| P0 | 含采用模块与年龄/职级分层的企业—员工招聘、离职、培训面板 | 原始人数、共同ID、风险集、培训参加/完成/小时、缺失和权重；若只能公布聚合，至少给相同企业样本的联合cell而非各自边际 |
| P1 | S4/S5对应2026版本的可复算职业—年龄流量表及代码 | 明确CPS末月/匹配风险集、SOC版本、暴露vintage、分母与面板进出；公众可得性须单独证明 |
| P1 | 同一企业新入职队列的训练与独立能力随访 | 入职前基线、训练分配、工具版本、30/90日无AI迁移测验、晋升/离职；与工资单连接，避免只观察留下来的员工 |

这些需求仅保存在本日志，未写入 agenda，未发送给任何外部机构。

# 最小实验

**已完成的最小公开证据校准：** 核对上述来源正文/方法、2026版本身份与S1官方工作簿，逐列检查是否存在共同单位、窗口、分母和键。可直接读取S1的四种行动边际；没有企业行和人数，故净headcount保持缺失，不作相减。本轮没有执行微数据合并或估计四层因果模型。

**下一步最小可执行研究设计（提案，未执行）：** 先选一个愿意提供匿名联表的企业、一个能定义技能测验的职业族，以月为单位接入采用前后各六个月工资单与招聘记录；把22–25岁和事先定义的初级职级分别标记，同时保留更年长/更高职级对照。采用/暴露版本固定，记录所有入职、离职、内部转岗和岗位取消；同一人企键接上培训提供、参加、完成、时长及指导练习。

在该职业族内，对合格的新入职者随机安排普通工具培训或增加独立练习/复核的培训，测量培训前、结束时、30日和90日的无AI能力及新任务迁移；离职者仍记录随访可得性与缺失，不只分析留任者。两组都使用相同工具，工具熟练度与专业判断能力分别评分。样本量由预设最小重要差异与统计功效决定；一个企业只用于验证数据闭合与局部训练效果，不能识别全国就业或企业采用的总因果效应。

**验收条件：** 同企同月人数变化能用H/S及范围调整解释；青年招聘的分子/风险集可追溯；培训结果能接回同一入职队列；独立能力得分与生产输出分别观测。若任一关键连接失败，保留分层证据表并报告缺口，不能声称完成四层联测。企业采用效应还需增加未采用/稍晚采用企业及采用前趋势检查；本提案的培训随机化不替它提供识别。

# Result

**能否同一框架：能共享schema，能做局部连接，当前不能直接形成四层共同估计。**

- **事实层：** 2026一手材料已分别支持企业采用与用工/培训行动、采用与行政FTE/青年招聘、职业暴露与青年流入流出、培训可得性，以及短期独立技能实验。没有一份本轮核验来源公开闭合全部四层。[S1](https://libertystreeteconomics.newyorkfed.org/2026/09/businesses-are-using-ai-to-transform-work-not-cut-jobs/)、[S3](https://www.bankofengland.co.uk/-/media/boe/files/events/2026/s-darougheh-slides.pdf)、[S4](https://www.anthropic.com/research/labor-market-impacts)、[S5](https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf)、[S6](https://libertystreeteconomics.newyorkfed.org/2026/04/use-of-gen-ai-in-the-workplace-and-the-value-of-access-to-training/)、[S7](https://arxiv.org/html/2601.20245v2)
- **推断层：** 最小共同单位应从“企业总体变化”下沉到可连接的企业—职业—职业阶段—时期，并另接个人培训/能力记录；公开结果先采用带分母与状态的估计项长表。既不能因总体用工影响有限否定青年入口变化，也不能因入口变化推定培训或专业能力再生已经恶化。
- **缺口层：** 最紧缺的是同一队列的实际H/S与培训后独立能力，而不是更多不同分母的采用率。优先补S3完整方法与一组企业内纵向联表；在此之前，保持“可直接整理、只能锚接、不可合并”的区分，不产出单一AI就业/能力再生指数。

本轮交叉校准判定：**refined；联合测量缺口仍在。**
