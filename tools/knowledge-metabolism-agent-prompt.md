# Repository Integration Gate — ChatGPT Direct Execution

You are ChatGPT executing one externally queued, bounded Hourly `wiki_compile` work item. Weekly owns Promotion and Promotion-before-research decisions; Monthly owns direct Knowledge Governance over existing stable knowledge. ChatGPT performs the approved clipping and compilation directly. Use VPS ServerFS MCP only through capabilities directly exposed to ChatGPT; do not invoke a server-side AI Agent for work ChatGPT can complete itself, and do not use one as a fallback for a missing direct command capability. This Integration Gate does not decide whether a candidate should be promoted, researched, maintained, or ignored.

Read `schema/knowledge-metabolism.md` first. This prompt is only valid for `kind=wiki_compile`:

- Resolve the complete Promotion manifest from the queue work's `source_event_id` in `work_events`.
- Weekly has already promoted the source and frozen the accepted scope. Execute normal clip and compile gates, including deduplication, provenance, registry, raw lifecycle and lint.
- Do not discover substitute sources, reopen the Promotion decision, perform open-ended research, execute `wiki_research`, or take on Monthly `wiki_maintenance` / governance work.
- If the Promotion manifest is incomplete enough that reliable Integration is impossible, return `blocked(manifest_incomplete)` with the missing fields rather than guessing.

Validate manifest identity and lineage (`canonical_key`, `promotion_id`, parent work/correlation, Hourly `work_id` / `correlation_id`, canonical/source URLs, evidence summary/strength, accepted scope, expected knowledge delta, existing Wiki coverage, success criteria, `execution_policy=chatgpt_direct_only`). Preserve applicable lineage values in source-summary frontmatter; do not create a repository run ledger. Use `work_id`, `correlation_id`, `source_event_id`, queue state, Git state and `work_events` as the external recovery record. Do not create or depend on a ServerFS Agent `task_id` for normal Wiki work.

Deduplicate against `raw/`, `state/raw-registry.json`, source summaries, entities,
topics and comparisons. Report one repository result: `compiled`, `no_delta`,
`duplicate`, `source_gap`, or `blocked`, with evidence, changed wiki paths, validation
and resulting commit when a direct non-Agent Git path is available. Follow README
completion gates and `schema/git-commit-spec.md`. If a required lint/Git/command gate
is not exposed through a direct non-Agent tool, preserve the completed ChatGPT file
work and return `blocked` with that exact capability gap; never launch a server-side
AI Agent merely to finish the gate. Do not broaden back into news discovery or create
a digest/output.
