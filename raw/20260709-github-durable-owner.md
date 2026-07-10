---
type: raw
source: "https://github.blog/security/application-security/how-github-gave-every-repository-a-durable-owner/"
author:
  - "Michael Recachinas"
published: "2026-07-09"
created: "2026-07-10"
tags:
  - clippings
  - organization-systems
  - security
  - governance
---

# How GitHub Gave Every Repository a Durable Owner

GitHub hosts more than 14,000 repositories across its primary internal organization. As of early 2025, over 11,000 remained unarchived, yet fewer than half had identifiable owners. While production services historically maintained clear ownership mappings, repositories without associated services lacked a reliable ownership pathway.

This gap created significant friction during a recent secret scanning remediation initiative. Rotating secrets without knowing who managed a repository introduced risk and operational disruption, with no structured mechanism to route remediation tasks. Within six weeks, the team validated ownership for every active repository, archived roughly 8,000 inactive ones, and made ownership a mandatory field during creation going forward.

## The original ownership model

For years, GitHub tracked ownership through an internal Service Catalog. Each service entry captured metadata linking deployed services to their backing repositories, documenting the owning team, executive sponsor, and support channels. However, the mapping was inherently one-to-many in reverse: a single service tied to only one repository, meaning starting from a repository required a lookup that only succeeded if the repo was already cataloged as a service.

Team repos, documentation hubs, internal tools, experimental projects, and personal forks fell through the cracks. Locating owners for these "unowned" repositories relied on guesswork, Slack pings, README reviews, or commit history audits. During the secret scanning cleanup, engineers wasted valuable time hunting down owners before triaging alerts.

## Designing the new ownership model

The solution required making repository ownership a first-class data property. After evaluating options like per-repository config files or centralized databases, the team selected **GitHub Custom Properties**. This native approach offered organization-wide queryability, structured validation, and seamless integration with enterprise policies and rulesets.

Two custom properties were introduced:

- **`ownership-type`**: A restricted field accepting three values: "Service Catalog," "Hubber Handle," or "Team."
- **`ownership-name`**: A validated text field. A background GitHub App verified Hubber handles against active membership, confirmed teams existed with at least two members, and cross-referenced Service Catalog entries.

## Day-one coverage

Before asking users to submit data, the team scheduled a periodic sync between the Service Catalog and repository custom properties. Every repository backing a known service automatically received an `ownership-type` of "Service Catalog" and a populated `ownership-name`. This initial sweep addressed roughly 1,500 service-backed repositories.

## The rollout

A custom GitHub App powered by a Kubernetes CronJob handled enforcement. The enforcement pipeline: scan repositories for missing ownership → open a warning issue → allow a 30-day grace period → archive unresolved repositories → auto-close issues once resolved.

The first automated run triggered on a Saturday morning. The assumption that few would be online backfired instantly, as distributed teams across time zones flagged newly created warning issues on Slack. After the grace period, unclaimed repositories were archived. Archiving was chosen because it's reversible and non-destructive.

## Sharp edges

Two minor incidents revealed important edge cases:

1. **Notification gaps:** Early ownership issues landed silently inside repositories, causing delays. Resolution involved directly @-mentioning repository administrators and assigning all users with write access.

2. **Data reliability risks:** Malformed data could falsely indicate that valid repositories lost their service bindings, risking mass archiving of healthy repos. Mitigation included a conservative low-water-mark threshold: each run tallied pending archives and issues beforehand, halting execution and alerting monitors if thresholds were breached.

## Results

The initiative concluded in under 45 days:

- Active repositories stabilized around **3,000**
- Archived inventory grew to approximately **11,000**
- Every active repository now carries a verified owner, or it gets archived automatically

## Making ownership stick

Ownership types were designed with inherent durability:

- **Service Catalog** entries track service lifecycles; decommissioned services trigger matching repository archival
- **Teams** require minimum two-member validation, ensuring stable accountability even if individuals rotate off-staff
- **Individual handles** only fail upon employee departure, which typically warrants archival anyway

## Replication guide

Organizations can replicate this model using GitHub Custom Properties:

1. Establish an ownership taxonomy tailored to your structure
2. Configure organization-level custom properties
3. Sync existing assets from service catalogs or CMDBs
4. Mandate fields at creation
5. Implement grace-period automation with archival
6. Plan for scale guardrails with fallback notifications and threshold-based run limits
