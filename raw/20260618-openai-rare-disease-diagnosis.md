---
type: raw
source: "https://openai.com/index/diagnose-rare-childhood-diseases/"
author:
  - "OpenAI"
  - "Boston Children's Hospital"
  - "Harvard University"
published: "2026-06-18"
created: "2026-06-18"
tags:
  - clippings
  - medical-AI
  - rare-disease
  - genomic-reanalysis
  - NEJM
  - openai-o3
---

# Using AI to help physicians diagnose rare genetic diseases affecting children

In an NEJM AI study, experts used an OpenAI reasoning model to reanalyze 376 previously unsolved cases and surface leads for 18 diagnoses.

## Why an old case can contain a new answer

Even with genomic sequencing, many people with rare diseases never receive a clear genetic diagnosis. Roughly half remain undiagnosed after extensive testing and specialist review. Their medical data may contain clues but finding them can require sifting through thousands to millions of possible genetic variants, fragmented clinical records, and rapidly changing scientific literature.

As new gene-disease relationships, case reports, and classification evidence accumulate, unsolved cases can become newly interpretable.

## How the reanalysis worked

Researchers from Boston Children's Hospital's Manton Center for Orphan Disease Research, Harvard University, and OpenAI used the OpenAI o3 Deep Research reasoning model to analyze de-identified clinical and genomic information from 376 previously analyzed cases that remained unsolved.

For each case, the team assembled a de-identified packet containing standardized Human Phenotype Ontology terms, clinician notes, metadata such as age and gender, and a filtered variant table. The team asked the model to propose the most plausible molecular explanation and to show its work.

Before analyzing unsolved cases, the team refined the workflow on cases with established diagnoses:
- Recovered the correct gene and variant in duplicate runs for 48 of 51 cases (rare conditions)
- In 57 neuromuscular cases, returned the correct diagnosis for 45 cases
- In a 15-case long-read genome set, named the correct gene in every case

The model's self-reported confidence scores tracked with correct diagnoses: mean minimum score 85.6 for consistently correct calls vs 42.1 for incorrect/unknown calls.

## What the researchers found

| Cohort | Cases | Diagnoses surfaced | Yield |
|--------|-------|-------------------|-------|
| Neurodevelopmental | 100 | 10 | 10.0% |
| Neuromuscular disease | 61 | 4 | 6.6% |
| Sudden unexpected death in pediatrics | 200 | 2 | 1.0% |
| Early psychosis | 15 | 2 | 13.3% |
| **Total** | **376** | **18** | **4.8%** |

Of the 18 diagnoses, 7 were rediscoveries: diagnoses established outside the local research workflow but absent from the record the team reviewed. In several cases, the variants were already listed as pathogenic in public databases, highlighting the operational challenge of synthesizing information across data sources.

## Demonstrating flexibility when identifying variants

In one early-psychosis case, the model inferred a structural event not listed in input data. It connected low-quality calls on chromosome 22 with cardiac, immune, neurodevelopmental, and psychiatric features, hypothesizing a 22q11.2 deletion associated with DiGeorge syndrome. This was confirmed with follow-up genome sequencing.

Although the prompt asked for one monogenic cause, the model sometimes surfaced two genes that better explained a complex presentation. Variants in LAMA2 and FOXP1 together helped account for muscle and neurodevelopmental features in one case; another had a previously unrecognized digenic explanation involving TTN and SRPK3.

## Producing a testable, biologically coherent hypothesis

The model identified a possible novel mechanistic explanation for vitiligo: an 11-amino-acid deletion in S1PR1 in a person with vitiligo. The model integrated evidence suggesting the deletion could alter receptor structure and signaling in ways that reduce pigment production while helping immune cells persist in the skin.

## Case study: Kyra's diagnosis after nearly two decades

Kyra's case was one of the four diagnoses surfaced in the neuromuscular cohort. The team linked her condition to a frameshift variant in HSPB8 and diagnosed a form of myofibrillar myopathy. A genetic counselor called Kyra about a week before her 28th birthday. She had spent much of her life adapting to the disease, dependent on a ventilator and in a wheelchair by age 13.

## Limitations

- Retrospective study, heterogeneous cohorts, reviewers not blinded to model confidence
- Did not measure time saved, cost, clinician effort, false-positive workload
- Did not systematically evaluate structural variants, repeat expansions, deep-intronic changes, or mosaicism
- Model did not diagnose any participant; all diagnoses through established clinical processes

## What comes next

- Prospective, multi-center studies comparing LLM-assisted reanalysis with standard practice
- The Manton Center will lead next stage through a grant from the OpenAI Foundation
- Goal: platform-agnostic, low-cost genetics AI copilot for clinical teams
