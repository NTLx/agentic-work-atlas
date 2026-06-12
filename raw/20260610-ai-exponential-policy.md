---
type: raw
source:
  - "https://darioamodei.com/post/policy-on-the-ai-exponential"
  - "https://www.anthropic.com/policy-on-the-ai-exponential"
  - "https://www-cdn.anthropic.com/files/4zrzovbb/website/0a58d567024a8b448ff15158ebc3625328dfcc1f.pdf"
author:
  - "[[Dario-Amodei]]"
  - "Anthropic"
published: "2026-06-10"
created: "2026-06-12"
tags:
  - clippings
  - AI-policy
  - regulation
  - frontier-AI
  - Anthropic
  - Dario-Amodei
  - safety
---

# Policy on the AI Exponential

> 三个来源合并：Dario Amodei 个人长文（主体）、Anthropic 官方公告（概述）、Advanced AI Framework PDF（完整政策框架）。三者为同一次发布的不同形式。

---

## Part A: Dario Amodei 个人长文

In one of the side plots to _The Lord of the Rings_, two of the Hobbits attempt to rouse Treebeard—a wise but ponderous sentient tree—to defend his forest from an army that is cutting it down. The problem is that Treebeard operates at a very different speed than the Hobbits. It takes him a full day simply to say hello to another tree, so getting him and his peers to act fast enough is nearly impossible.

The intersection of AI and our political institutions feels a bit like the Hobbits and Treebeard. AI is advancing at a lightning pace—in only four years, AI models have gone from barely being able to write a coherent line of code to writing most of the code at major AI companies. Similar gains have been made in biology, physics, math, finance, law, translation, and many other fields. AI's scaling laws, which predict an exponential increase in general cognitive capabilities with increasing computing power, now have over a decade of empirical evidence behind them. If these scaling laws continue for only a year or two longer, we are likely to get what I've called _Powerful AI,_ or "a country of geniuses in a datacenter".

By contrast, policy—and especially legislation—moves very slowly. Often this is for good reasons: governments have grave powers, and it's usually for the best that they aren't used too hastily. But the mismatch in timescale is nevertheless very painful: in the several years that it can take Congress to act, AI can go from an amusing toy to the full country of geniuses.

Over the last few years since AI has become a major commercial technology, those of us who wanted to handle it responsibly have faced a dilemma. We could see clearly where the exponential was going: we strongly suspected that within a few years AI would be one of the rare technologies that fundamentally reshapes the entire policy landscape, in the same way that nuclear weapons reshaped geopolitics and the industrial revolution fundamentally reshaped every economic and social issue. But to those looking only at what AI could do _at the time_, it looked like a much more mundane technology—similar perhaps to the latest consumer app or cryptocurrency. It was hard to convince most policymakers and companies that anything other than a _laissez faire_ attitude made sense. And to be fair, the fact that AI's radical effects were not yet present, and that we didn't know exactly what shape they might take, made it difficult to design the right policies even if there had been the will to act.

Given the limits imposed by this situation, many safety advocates (including Anthropic) have so far been focused on advocating for policy actions that preserve optionality, tee up a fast reaction in the future, or give the world better insight into what is coming down the pike – things like transparency legislation, export controls on chips, and data collection on AI's labor effects. These are not enough, but they have felt like all that was possible.

In the last few months, however, the evidence of AI's incredible power, as well as its risks, has become undeniable. Perhaps the most emblematic example is Claude Mythos Preview and the discovery that frontier models pose very real risks to cybersecurity, creating the potential for disruption of the financial sector, critical infrastructure, and national security. Mythos Preview scrambled the global cybersecurity landscape. But its broader significance is that it proves beyond doubt that AI models are now tools of global and national strategic consequence. The cyber risks that Mythos-class models present will not be the last that we must face. I believe that biological risks may soon follow, and that serious AI autonomy risks may not be far behind.

We now, globally and collectively, need to activate a slow and rickety policy apparatus to deal with risks and opportunities that are going to compound surprisingly quickly from here. Many policymakers are showing increased openness to taking action, and it's been encouraging to see our peers come around to the same positions we've been advocating for over the past few years. This is good, but I worry that these early actions are at least a year out of step with AI's rapid progress. This essay is an attempt to close that gap: to lay out where the exponential is now, and the collective action needed to meet the moment.

I will focus on five perennial policy areas that need re-imagining in an AI world: regulation and public safety, macroeconomics and tax policy, scientific innovation, the balance of power between state and society, and geopolitics.

### 1. Regulation and public safety

Every new technology or product has both beneficial and harmful uses, and therefore presents a dilemma between innovation and safety. Regulating products makes them less likely to cause harm and has played an important role in improving lives around the world, but it can also directly reduce their benefits and indirectly disincentivize innovation. There is also the Hayekian point that regulators often lack the information needed to make the right decisions about complicated economic tradeoffs, so that regulation is often both ineffective _and_ burdensome. A related idea is the Collingridge dilemma, which states that the impacts of a technology are often hard to anticipate until it is too late to easily manage them.

Ultimately, we concluded that the right approach at that time was _transparency_. Developers of AI models should have to _disclose_ their safety procedures and the tests that they run on their models and report on any critical safety incidents, so that the public and the scientific community could gain better visibility into risks as they emerge. However, now the risks are clearly here. It is time to go beyond transparency to more serious and binding regulation of AI.

I believe the best analogy, at least at the current stage of the exponential, is to cars, airplanes, or drugs—powerful technologies essential to the modern economy, but capable of killing large numbers of people if designed or operated poorly. I therefore believe we should model AI regulation on agencies like the Federal Aviation Administration (FAA). **Frontier AI models, like airplanes, should be required to go through technical testing and auditing, and their release should be blocked or reversed as a threat to public safety if they do not meet high standards of safety.**

Our proposal includes the following elements:

- Models above a threshold of compute should undergo mandatory testing by a qualified third party for their level of risk in four specific areas: cybersecurity, biological weapons, loss of control of AI systems, and automated R&D that could accelerate these other risks.
- The government should have the power to block or deter deployment of the model if it is determined, in light of third-party assessment, to present unacceptable risks.
- Third-party evaluation could be done by a government agency (similar to the FAA) or a set of private organizations that are authorized and inspected by the government to evaluate models according to certain standards (a "regulatory markets" approach).
- AI companies that develop advanced AI models must have strong security standards that protect their model weights, should conduct regular red teaming and penetration testing, and should work with the government to defend against major threat actors.
- Safety incidents in the four critical areas must be reported promptly.

### 2. Macroeconomics and tax policy

Governments have long faced the problem of how to encourage economic growth while also providing important public services and ensuring that the least fortunate are taken care of. An important (and generally correct) premise of these debates has been that _economic growth is fragile and difficult to achieve_—that while reducing inequality might provide important benefits, it has to be traded off against the economic drag of increased taxes or deficits.

I suspect that powerful AI may scramble this assumption. If AI achieves the ability to do most cognitive tasks far better than humans, it stands to reason that it could result in extremely rapid and robust economic growth via the acceleration of science, technology, and operational efficiency. But for exactly the same reasons, AI may also act as a more general economic substitute for human cognitive abilities than previous technologies have, while also altering the economy far faster than previous technologies have. Thus, it's reasonable to think that AI could produce much larger disruptions to the labor market than previous technologies have, and, potentially, more _enduring_ disruptions. We risk ending up in a world where the economic tradeoff dial is stuck on the hypergrowth, hyper-inequality setting, and is potentially very hard to unstick from that setting. _The key challenge in such a world won't be incentivizing growth, but finding a way for everyone to share in the benefits._

Two key points:

1. Enduring job displacement is undesirable and dangerous, and we should do everything we can to minimize or prevent it, not to bring it about.
2. Any response to AI-driven job displacement needs to address _both_ the need to provide for everyone economically, _and_ the need for people to find meaning, purpose, and agency.

Policy interventions:

- **Measurement and tracking.** Governments could greatly expand their economic statistics to more carefully track AI job displacement.
- **Pro-employment incentives.** Wage insurance policies, retention tax incentives, workforce training grants, or infrastructure to facilitate matching of employers to employees.
- **Long-term macroeconomic support.** If AI-driven labor displacement ends up being large in magnitude and permanently drives down the demand for labor, mechanisms such as universal basic income could be financed through taxes on relevant companies or raising the capital gains tax.

### 3. Accelerating AI's positive impact

For downstream applications of AI—in contrast to AI itself—I am more worried about the regulatory apparatus _slowing down_ progress (because it can't handle the increased pace of change) than I am about it failing to address important risks. The last thing we want is for the benefits of AI to be slowed while its risks loom large.

Regulatory agencies should consider developing standards _now_ for what it would take to accept AI-based methods. This includes:

- AI-based pharmacodynamics and pharmacokinetics (PD/PK) modeling
- Prediction of toxicology to avoid the need for multiple species animal toxicology
- More accurate dose selection
- Biomarker validation via analysis of large datasets
- Synthetic control arms in clinical trials
- Developing surrogate endpoints (particularly important in aging and neurodegeneration)

### 4. The state and civil liberties

AI threatens to upset the balance between state power and civil liberties while also dramatically raising its stakes. Powerful AI in the wrong hands could be the ultimate tool of autocracy, and our existing legal and constitutional protections are not fully equipped to counter this threat.

Policy ideas:

- Create reliable accountability rules for fully autonomous weapons
- Ban the domestic use of fully autonomous weapons
- Close the bulk collection / data broker loophole
- Public rights to AI advice during adverse government action

### 5. Securing leadership by democracies

If AI really will soon be "a country of geniuses in a datacenter", or anything remotely close to it, then **AI is likely to be the dominant source of military and economic power for any nation**. A nation that possesses powerful AI facing one without it—or even facing one that is behind in AI by 3 years—could be the equivalent of an army of World War II Marines facing an army of medieval swordsmen.

Democracies should seek to form a global coalition centered on building AI according to their common values. Principles:

- Managing the AI supply chain (export controls, chips sharing within coalition)
- Coordinate to address AI's risks (international harmonization)
- Share AI's benefits (trade and regulatory policy for diffusion)
- Mutual defense (AI-led cyberdefenses, drones, intelligence)
- Rejection of AI-powered repression
- Macroeconomic cooperation

---

## Part B: Anthropic 官方公告概述

We are publishing our proposal for how governments should address catastrophic risks from the most powerful AI models, including granting them the legal authority to block or deter dangerous deployments.

AI capabilities are on a sharp upward trend. A few years ago, AI models could barely write code. This year, Claude Mythos Preview discovered thousands of high-severity vulnerabilities, including in every major operating system and browser. Evidence strongly suggests this trend will continue—and with it, the risk of catastrophic harm will increase, too.

This calls for government action and for regulation—regulations that are carefully designed to prevent government overreach and protect innovation. When a model poses risks of this kind, the government should have the legal authority to block or deter its deployment—beyond what exists in current law or in existing proposals in Congress–with civil penalties tied to global annual revenue that escalate with repeated violations.

These rules should apply only to models trained using more than 10²⁵ FLOPs, developed by companies earning more than $500M in AI-related revenue or spending more than $1 billion on AI R&D. They would address four kinds of catastrophic risk:

- **Biological risk** — AI could make it substantially easier to develop biological weapons
- **Cyber risk** — Frontier AI models can find critical software vulnerabilities at large scale
- **Loss of control risk** — As AI systems improve, it could become much harder to control systems that act outside of their developers' control
- **Automated R&D** — AI systems are automating the research and development of AI itself

### Key recommendations

**For frontier developers:**

- **Transparency:** Test models, publish results, publish safety framework, system cards, and regular risk reports
- **Independent evaluation:** At least one qualified independent evaluator to publish a review
- **Security:** Secure model weights and training infrastructure against external and insider threats
- **Enforcement:** Government authority to block or deter deployment of dangerous models, with civil penalties tied to global annual revenue

**Societal resilience:**

- On biology: prevention (gene synthesis screening), detection (biosurveillance), preparedness (stockpiling, air filtration)
- On cyber: hardened infrastructure, forward-deployed support for under-resourced operators, AI-enabled breach remediation
- On loss of control and automated R&D: still needs more work

---

## Part C: Advanced AI Framework (PDF) 核心条款

> 以下为 PDF 中的关键政策条款摘要

### Scope: Covered Developers

- Develop AI models requiring more than 10²⁵ training FLOP
- Earn more than $500M in annual AI-derived revenue, or spend more than $1B per year on AI R&D

### Catastrophic Risk Definition

"Foreseeable and material risk that a Covered Developer's development, storage, use, or deployment of a covered model will materially contribute to significant death, injury, or damage."

### Enumerated Risk Categories

1. Biological weapons
2. Offensive cyber operations
3. Loss of control of AI systems
4. Automated R&D that could accelerate risks (a)–(c)

### Transparency Requirements

- Develop and publish a safety framework
- Annual certification of compliance
- Risk reports every six months
- System cards when deploying materially more capable models
- Critical Safety Incidents reported within 15 days

### Independent Evaluation

- Within six months of enactment, engage at least one qualified independent evaluator
- Evaluator publishes review of risk report
- Build government capacity to eventually fulfill evaluator function

### Security Requirements

- Full development environment security program
- Monitoring for distillation attacks
- Regular penetration testing
- Privileged-access parties must maintain security protections

### Enforcement

- False statements prohibited
- Civil penalties escalating with repeated violations, scaling with global annual revenue
- Whistleblower protections
- Possible government agency review with power to:
  - Fine for deployment with inadequately mitigated risks
  - Prohibit further model deployment until violations corrected
  - In extreme cases, restrict usage of already-deployed models

### Safeguards Against Overreach

- Court enforcement (agency must initiate lawsuit)
- Cabined discretion (only based on specific listed violations)
- Consistent treatment and judicial review
- No developer advantaged/disadvantaged on unrelated grounds

### Biological Resilience Measures

**Prevention:**
- Modernize biosafety/biosecurity standards
- Close oversight gaps for privately funded research
- Gene synthesis screening
- Threat monitoring and intelligence sharing

**Detection:**
- Pathogen-agnostic biosurveillance
- Microbial forensics and attribution

**Preparedness:**
- Public health infrastructure and planning
- Protective equipment stockpiles
- Airborne transmission suppression
- AI-accelerated countermeasure development
- Broad-spectrum antivirals
- Responsive medical countermeasures
- After-action institutionalization

### Cyber Resilience Measures

**Prevention:**
- Open-source and legacy software security
- Phishing-resistant identity and provenance
- Forward-deployed support for under-resourced operators

**Measurement:**
- Track frontier-model cyber capability
- Threat intelligence on AI-enabled cyber operations
- Safe harbor for defensive coordination

**Defender Advantage:**
- Designing for breach
- AI-enabled breach remediation
- Safeguards for broad release of defensive capability

**Security Modernization:**
- End-of-life and legacy system replacement
- Experimental research into new security paradigms

---

## Footnotes

1. Anthropic's Long-Term Benefit Trust is an independent governance body designed to hold the company to its mission.
2. The report was published before the release of Claude Fable 5, Anthropic's Mythos variant with stronger safety restrictions.
3. Mythos 5 (without the preview tag) is still only available to institutions Anthropic has selected.
4. Reference essay: _The Adolescence of Technology_ by Dario Amodei.
