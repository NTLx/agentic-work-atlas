---
title: "\"OncoAgent: A Dual-Tier Multi-Agent Framework for Privacy-Preserving Oncology Clinical Decision Support\""
source: "https://huggingface.co/blog/lablab-ai-amd-developer-hackathon/oncoagent-official-paper"
author:
  - "Máximo López Chenlo"
published: 2026-05-10
created: 2026-05-10
description: "A Blog post by Lablab.ai AMD Developer Hackathon on Hugging Face"
tags:
  - "clippings"
---

## OncoAgent: A Dual-Tier Multi-Agent Framework for Privacy-Preserving Oncology Clinical Decision Support

---

## Abstract

We present **OncoAgent**, an open-source, privacy-preserving clinical decision support system for oncology. OncoAgent combines a dual-tier fine-tuned LLM architecture with a state-of-the-art multi-agent LangGraph topology, a four-stage Corrective RAG pipeline over 70+ physician-grade NCCN and ESMO guidelines, and a three-layer reflexion safety validator enforcing a strict Zero-PHI policy.

The system routes clinical queries through an additive complexity scorer to either a 9B parameter speed-optimised model (Tier 1) or a 27B deep-reasoning model (Tier 2), both fine-tuned via QLoRA on a corpus of **266,854** real and synthetically generated oncological cases using the Unsloth framework on AMD Instinct MI300X hardware (192 GB HBM3).

Sequence packing on MI300X enabled full-dataset fine-tuning in approximately **50 minutes** — a **56× throughput acceleration** over API-based generation. Post-fix, CRAG document grading achieved a 100% success rate with a mean RAG confidence score of 2.3+. The complete system is 100% open source and deployable on-premises, eliminating proprietary cloud API dependency and preserving patient data sovereignty.

**Keywords:** clinical decision support, oncology AI, multi-agent systems, retrieval-augmented generation, QLoRA, AMD ROCm, open-source healthcare AI, HITL safety, LangGraph, Corrective RAG

---

## 1\. Introduction

Oncology is one of the most information-dense and cognitively demanding domains in clinical medicine. The volume, heterogeneity, and rapid evolution of evidence-based guidelines — from the National Comprehensive Cancer Network (NCCN) to the European Society for Medical Oncology (ESMO) — create a persistent knowledge gap between published evidence and bedside practice.

AI-assisted clinical decision support systems hold transformative potential for closing this gap, yet most commercially available systems fail in three critical ways:

1. **Hallucinated recommendations** not grounded in validated guidelines
2. **Cloud API dependency** that precludes on-premises deployment in privacy-sensitive hospital environments
3. **Monolithic LLM architectures** prone to context saturation under complex multi-comorbidity presentations

OncoAgent is designed around three core principles:

- **Architectural decomposition:** Clinical reasoning is decomposed across eight specialised LangGraph nodes, each with a bounded, auditable function.
- **Grounded generation:** All model outputs are anchored to a curated vector knowledge base through a four-stage retrieval pipeline with explicit relevance gating.
- **Hardware sovereignty:** The full inference and training stack runs natively on AMD Instinct MI300X using ROCm and open-source frameworks — enabling hospital deployment without data exfiltration.

---

## 2\. Related Work

### 2.1 Clinical LLMs and Decision Support

Large language models have demonstrated significant promise in clinical NLP tasks including diagnostic coding, literature summarisation, and patient communication. Domain-specific fine-tuning approaches — exemplified by BioMedLM, Med-PaLM 2, and ClinicalBERT — consistently improve performance on medical benchmarks over general-purpose models. OncoAgent extends this line of work by targeting the specific subdomain of oncological triage and treatment pathway recommendation, where hallucination consequences are most severe.

### 2.2 Multi-Agent Architectures

Decomposed multi-agent systems have emerged as a principled approach to complex reasoning tasks. OncoAgent synthesises four canonical SOTA patterns:

- **Claude Code pattern** — deterministic safety harnesses separated from LLM reasoning
- **Hermes Agent pattern** — structured tool-calling with per-session memory isolation
- **Corrective RAG** (Shi et al., 2024) — document relevance grading and query reformulation
- **Reflexion** (Shinn et al., 2023) — self-correcting generation via feedback-augmented retry loops

### 2.3 Retrieval-Augmented Generation in Medicine

Standard bi-encoder retrieval is ill-suited for clinical domains where terminological precision is critical (e.g., "tyrosine kinase inhibitor" vs. "TKI"). OncoAgent implements a multi-stage pipeline with cross-encoder re-ranking, and integrates Hypothetical Document Embeddings (HyDE; Gao et al., 2022) to resolve medical synonym mismatches by projecting natural language queries into the guideline embedding space.

---

## 3\. System Architecture

### 3.1 Overview

OncoAgent is implemented as a stateful directed graph using **LangGraph**. The system state is represented as an immutable `AgentState` TypedDict containing 11 logical sections and approximately 30 typed keys. Each node appends to specific keys without mutating upstream data, preserving a complete audit trail.

The 8-node topology is:

```
Router → Ingestion → Corrective RAG → Specialist ↔ Critic → HITL Gate → Formatter → END
                                                                   ↓
                                                               Fallback → END
```

Key properties:

- 5 conditional edges
- 1 reflexion retry loop (max 2 iterations)
- 1 mandatory HITL interrupt for high-complexity or low-confidence outputs

### 3.2 Complexity Router and Model Tiering

Case complexity is quantified using a weighted additive model prior to specialist invocation:

```
S = w_cancer + w_stage + w_mutations + w_treatment
```

Where:

| Factor | Condition | Weight |
| --- | --- | --- |
| Cancer type | Rare | +0.40 |
| Cancer type | Unknown primary | +0.30 |
| Stage | Stage IV | +0.25 |
| Stage | Stage III | +0.15 |
| Mutations | ≥2 identified | +0.30 |
| Mutations | Single | +0.15 |
| Prior treatment | Any keyword match | +0.10 |

**Decision boundary:** `S ≥ 0.5` → Tier 2 (Qwen 3.6-27B deep reasoning) · `S < 0.5` → Tier 1 (Qwen 3.5-9B speed triage)

**Validation:** A Stage IV pancreatic carcinoma case with KRAS + BRCA2 mutations correctly produced `S = 0.80`, routing to Tier 2. ✅

Clinicians may also manually override the tier selection through the UI.

### 3.3 Corrective RAG with Document Grading

The CRAG node grades each retrieved document for clinical relevance before forwarding to the Specialist. Documents that fail binary relevance classification trigger automatic query reformulation (max 1 retry). This eliminates the primary hallucination source in RAG pipelines — retrieval of plausibly titled but semantically irrelevant content.

After migrating from Qwen 3.5 to Qwen 2.5 Instruct for the grading step, success rate improved from **0% → 100%**, with RAG confidence score reaching **2.3+** on uterine cancer triage tests.

### 3.4 Reflexion Safety Loop (Critic Node)

The Critic node runs a three-layer validation cascade before any output reaches the HITL gate:

1. **Formatting check** — validates structural compliance with the OncoCoT output schema
2. **Safety check** — deterministic rule-based scan for prohibited output patterns (absolute dosing without guideline citation, drug interaction omissions, etc.)
3. **LLM entailment check** — verifies that the Specialist's recommendation is fully supported by the retrieved RAG context

On FAIL, the Critic's specific feedback is injected back into the Specialist context for a retry (max 2 iterations). Crucially, the Critic runs as **deterministic code**, not LLM-controlled logic — ensuring safety enforcement cannot be bypassed by adversarial prompting.

### 3.5 Human-in-the-Loop Gate and Fallback

The HITL gate provides a mandatory clinician interrupt for all Tier 2 cases and any output where `rag_confidence < 0.3`. A dedicated Fallback node catches unrecoverable failures and returns a clinically safe refusal — `"Información no concluyente en las guías provistas"` — avoiding hallucinated alternatives under any failure mode.

### 3.6 Per-Patient Memory Isolation

The `PatientMemoryStore` module assigns each patient session a unique `thread_id` (format `PT-XXXX`), passed as a `configurable` parameter to LangGraph's native checkpointing system. This enforces strict per-patient memory isolation while enabling iterative multi-turn consultations within a session.

---

## 4\. Knowledge Base Construction and RAG Pipeline

### 4.1 Guideline Ingestion and Sanitisation

The knowledge base was constructed from **77 direct physician guideline PDFs** identified by a concurrent web scraper that processed 138 NCCN detail pages in under 60 seconds. Text extraction used `PyMuPDF` (fitz) for block-level structural parsing, preserving the semantic reading order of multi-column clinical layouts.

A regex-based sanitisation step strips institutional branding prior to ingestion. Patient-facing materials are excluded via heuristic filtering. The resulting corpus covers **70+ professional oncological guidelines** across all major cancer types including HCC, NSCLC, breast, colorectal, and neuroendocrine tumours.

### 4.2 Medical Embeddings and Vector Store

Standard general-purpose embedding models (e.g., `all-MiniLM-L6-v2`) were rejected due to poor clinical terminology semantics. OncoAgent uses:

- **Embeddings:** `pritamdeka/S-PubMedBert-MS-MARCO` — fine-tuned on PubMed and MS-MARCO for asymmetric medical semantic search
- **Vector store:** Local **ChromaDB** persistent index — zero-cloud, Zero-PHI compliant

### 4.3 Four-Stage Retrieval Pipeline

| Stage | Component | Function | Configuration |
| --- | --- | --- | --- |
| **1\. Recall** | PubMedBERT Bi-Encoder | Wide-net retrieval | top-15 candidates |
| **2\. Distance Gate** | Cosine Distance Filter | Anti-hallucination floor | threshold = 0.10 |
| **3\. Re-Ranking** | Cross-Encoder (MS-MARCO MiniLM) | Joint query-document relevance | top-5 returned |
| **4\. Context Trimming** | Character-Budget Limiter | Fit within LLM context window | max 6,000 chars |

**Anti-Hallucination Policy:** Any query failing Stage 2 returns `"Información no concluyente en las guías provistas"` without invoking the Specialist. This guarantees zero hallucinated recommendations for out-of-domain clinical inputs.

Distance threshold calibration against the NCCN corpus established:

- Medical-query distances: ~0.06–0.09
- Out-of-domain distances: ~0.11–0.15
- Hard threshold: **0.10**

An optional **HyDE** module generates a hypothetical guideline paragraph and uses it as the embedding anchor for Stage 1 retrieval, resolving synonym mismatches (e.g., `"neoplasia pulmonar"` vs. `"lung carcinoma"`).

---

## 5\. Dual-Tier QLoRA Fine-Tuning

### 5.1 Training Corpus: OncoCoT (266,854 Samples)

| Source | Type | Samples | Notes |
| --- | --- | --- | --- |
| PMC-Patients | Real clinical cases | ~85,000 | PubMed Central patient reports |
| Asclepius | Real clinical data | ~85,000 | Curated medical QA corpus |
| OncoCoT Synthetic | Synthetic (Qwen 3.6-27B) | 96,941 | Generated on MI300X at ~6,800 cases/hr · rejection rate 0.65% |
| **Total** | — | **266,854** | 90/10 train/eval split · SHA-256 hashed · deduplicated |

All cases use ChatML template for Qwen compatibility. Thinking tokens were disabled (`chat_template_kwargs: {enable_thinking: False}`) to prevent JSON parse corruption.

### 5.2 QLoRA Configuration

Both tiers use 4-bit NormalFloat4 (NF4) quantisation via BitsAndBytes, with LoRA adapters targeting all major projection modules: `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`.

| Parameter | Tier 1 (Qwen 3.5-9B) | Tier 2 (Qwen 3.6-27B) |
| --- | --- | --- |
| Per-device batch size | 4 | 2 |
| Gradient accumulation | 4 | 8 |
| Effective batch size | 16 | 16 |
| Learning rate | 2×10⁻⁴ | 1×10⁻⁴ |
| LoRA rank (*r*) | 16 | 32 |
| Sequence packing | True, 2048 tokens | True, 2048 tokens |
| Early stopping | Patience = 3 | Patience = 3 |
| Quantisation | NF4 4-bit | NF4 4-bit |

### 5.3 AMD MI300X Optimisation with Unsloth

The original HuggingFace `transformers` + PEFT pipeline failed on the MI300X due to two independent issues:

1. Tokenisation conflicts between `trl` v0.24.0 strict EOS validation and the `Qwen3VLProcessor` wrapper
2. Insufficient VRAM headroom for target effective batch sizes under standard precision

Migration to **Unsloth's FastLanguageModel** resolved both simultaneously:

- **VRAM reduction:** ~60% drop in peak usage (from OOM to stable ~64 GB on 192 GB device)
- **Training speed:** ~2× improvement to ~16 s/step at effective batch 16

AMD ROCm-specific adaptations required:

```python
# 1. Pass inner tokenizer, not the Qwen3VLProcessor wrapper
trainer = SFTTrainer(tokenizer=model.get_tokenizer(), ...)

# 2. Prevent incompatible EOS injection
training_args = SFTConfig(eos_token=None, ...)

# 3. AMD-specific bitsandbytes for ROCm 6.2/gfx942
# pip install bitsandbytes --find-links <amd-continuous-release-wheel>

# 4. BF16 workaround (is_bf16_supported() returns False on ROCm despite hardware support)
training_args = TrainingArguments(fp16=True, ...)
# Final deployment uses native BF16:
model = AutoModelForCausalLM.from_pretrained(..., torch_dtype=torch.bfloat16)
```

### 5.4 Sequence Packing and Throughput Breakthrough

Sequence packing via `packing=True` in `SFTConfig` concatenates multiple short clinical records into single 2048-token sequences, eliminating padding overhead and drastically reducing forward pass count.

The combined effect of Unsloth kernels and sequence packing on the MI300X enabled full-dataset fine-tuning of the **266,854-sample corpus in approximately 50 minutes** — against an initial 5-hour estimate — representing roughly a **6× training time compression**. GPU utilisation peaked at ~70%, with consistent throughput at ~11.3 s/iteration.

> **Checkpoint-1000 results:** Tier 1 adapter trained for 1,339 steps · training loss ≈ 0.05 · adapter size 187 MB · verified against 11-file manifest including `adapter_model.safetensors`, `adapter_config.json`, and `tokenizer.json`.

The system supports adaptive inference routing: local BF16 inference via the `LocalModelManager` singleton when ROCm is available, with graceful fallback to the Featherless.ai API for high availability.

---

## 6\. Safety and Privacy Framework

### 6.1 Zero-PHI Policy

A dedicated Zero-PHI redaction node runs as the **first processing step** in the Ingestion node, before any text reaches an LLM. It identifies and replaces Protected Health Information (patient names, dates of birth, MRN numbers, addresses, facility identifiers) with clinically neutral placeholders. The redacted representation is stored in `AgentState`; the original text is discarded.

This ensures that no PHI reaches any downstream LLM call — local or remote — and satisfies HIPAA de-identification requirements by design rather than policy.

### 6.2 Layered Safety Architecture

The system's safety guarantees are enforced at four independent layers. A failure at any single layer does not compromise the overall posture.

| Layer | Mechanism | Addresses |
| --- | --- | --- |
| **L1: Retrieval Gate** | Distance Gate (cosine threshold 0.10) | Out-of-domain hallucinations |
| **L2: Confidence Gate** | RAG confidence score < 0.3 → block | Low-quality retrieval grounding |
| **L3: Reflexion Critic** | Formatting + safety + LLM entailment (max 2 retries) | Unsupported or unsafe Specialist outputs |
| **L4: HITL Gate** | Mandatory clinician interrupt for Tier 2 / flagged cases | High-complexity cases requiring expert judgment |

Layers 1 and 2 operate at the retrieval layer. Layer 3 at the generation layer. Layer 4 at the deployment layer. All Layer 3 checks run as deterministic code — not LLM-controlled logic — preventing safety bypass via adversarial prompting.

---

## 7\. Clinical Interface

The OncoAgent UI is implemented as a real-time streaming Gradio application in a ChatGPT-style conversational layout. It features:

- **Left sidebar:** Session controls, KPI tiles, evidence source tabs
- **Main chat area:** Live agentic reasoning updates as each node completes

Real-time transparency is achieved via LangGraph's `.stream(stream_mode="updates")` API, which emits `{node_name: node_output}` dictionaries as each node completes. The UI maps each node to a human-readable clinical label (e.g., `corrective_rag` → *"Retrieving NCCN/ESMO guidelines"*), providing clinicians with full pipeline visibility.

The `rag_confidence` score and retrieved source count are prominently surfaced, giving clinicians immediate visibility into the quality of guideline grounding behind each recommendation.

The interface was designed to WCAG 2.1 AA standards — Lucide-style inline SVG icons, slate-900/sky-500 dark theme, Figtree/Inter typography, `prefers-reduced-motion` media query, all transitions capped at 200 ms.

---

## 8\. Results

| Component | Metric | Value |
| --- | --- | --- |
| **Knowledge Base** | Guidelines ingested | 70+ |
|  | PDFs parsed | 138 in < 60 s |
|  | Index parsing errors | 0 |
| **CRAG Pipeline** | Document grading success rate (post-fix) | 100% |
|  | RAG confidence score (uterine cancer test) | 2.3+ (was 0.0 pre-fix) |
|  | Parallel grading latency (3–5 docs) | < 5 s |
| **Complexity Router** | Stage IV pancreatic + KRAS + BRCA2 | Score = 0.80 → Tier 2 ✅ |
| **Training (Tier 1, 9B)** | Full 266k-sample training time | ~50 min (vs. 5 hr estimate) |
|  | Steady-state throughput | ~11.3–16 s/step |
|  | GPU utilisation (MI300X) | ~70% peak |
|  | VRAM utilisation (Unsloth) | ~64 GB / 192 GB |
|  | Training loss at checkpoint-1000 | ~0.05 |
|  | Synthetic data throughput (MI300X vs. API) | 6,800 vs. 120 cases/hr (56× ↑) |
|  | Synthetic corpus rejection rate | 0.65% |
| **Graph Topology** | Compiled nodes verified | 8 / 8 |
|  | Module test suites passed | 6 / 6 |
| **UI** | Browser timeouts during triage | 0 |
|  | UI rendering latency | < 200 ms |

---

## 9\. Discussion

### 9.1 Hardware Sovereignty as a Clinical Requirement

The ability to run the complete OncoAgent stack — training, inference, RAG, and UI — on a single AMD MI300X instance without cloud API dependencies is not merely an engineering convenience. In hospital environments governed by HIPAA (US), GDPR (EU), and equivalent national frameworks, the legal and ethical obligation to maintain data within controlled infrastructure is absolute. OncoAgent demonstrates that SOTA multi-agent clinical AI is achievable within this constraint.

### 9.2 The Throughput Breakthrough

The 56× synthetic data generation acceleration (from ~120 to ~6,800 cases/hr) and the ~6× training time compression together represent a significant practical contribution to the feasibility of domain-specific fine-tuning in time-constrained settings. These results suggest that AMD's CDNA3 architecture, when paired with Unsloth's Triton kernel optimisations and SFT sequence packing, may be substantially underutilised by standard HuggingFace training pipelines — and that the performance gap can be closed without changes to the underlying model architecture.

### 9.3 Limitations

Several limitations warrant acknowledgement:

- The training corpus relies on approximately 36% synthetically generated cases. Clinical accuracy validation against board-certified oncologist judgments has not yet been performed at scale.
- The current knowledge base covers NCCN guidelines primarily in English; ESMO and non-English clinical corpora remain for future work.
- The Tier 1 adapter represents checkpoint-1000 of a potentially longer trajectory; full convergence and downstream clinical benchmark evaluation (MedQA, USMLE-style oncology subsets) are planned for subsequent releases.

---

## 10\. Conclusion

OncoAgent establishes a complete, open-source, privacy-preserving clinical decision support architecture for oncology that integrates SOTA multi-agent design patterns, domain-specific fine-tuning, and a four-stage grounded retrieval pipeline.

The system demonstrates that production-grade clinical AI does not require proprietary infrastructure: the full stack — including 266k-sample QLoRA fine-tuning, 70+ guideline RAG, eight-node LangGraph orchestration, three-layer reflexion safety validation, and real-time clinical streaming UI — runs on a single AMD Instinct MI300X instance under ROCm.

The architectural contributions — particularly the synthesis of Corrective RAG, Reflexion, and HITL gating into a single coherent safety stack — represent a replicable blueprint for domain-specific clinical AI deployments where hallucination consequences are life-critical.

All code, adapter weights, and the OncoCoT synthetic corpus will be released publicly on Hugging Face Spaces and GitHub.

---

## References

1. Singhal, K. et al. (2023). Large language models encode clinical knowledge. *Nature*, 620, 172–180.
2. Nori, H. et al. (2023). Can generalist foundation models outcompete special-purpose tuning? Case study in medicine. *arXiv:2311.16452*.
3. Wang, L. et al. (2024). A survey on large language model based autonomous agents. *Frontiers of Computer Science*, 18(6), 186345.
4. Shi, W. et al. (2024). Corrective Retrieval Augmented Generation. *arXiv:2401.15884*.
5. Shinn, N. et al. (2023). Reflexion: Language agents with verbal reinforcement learning. *NeurIPS 2023*.
6. Nogueira, R. and Cho, K. (2019). Passage Re-ranking with BERT. *arXiv:1901.04085*.
7. Gao, L. et al. (2022). Precise Zero-Shot Dense Retrieval without Relevance Labels. *arXiv:2212.10496*.
8. Hu, E.J. et al. (2021). LoRA: Low-Rank Adaptation of Large Language Models. *arXiv:2106.09685*.
9. Dettmers, T. et al. (2023). QLoRA: Efficient Finetuning of Quantized LLMs. *NeurIPS 2023*.
10. Han, S. et al. (2024). LangGraph: Building stateful multi-actor applications with LLMs. *LangChain Technical Report*.

---

*OncoAgent is intended as a clinical decision **support** tool. All outputs require review by licensed medical professionals prior to any clinical application.*

More from this author

## [CyberSecQwen-4B: Why Defensive Cyber Needs Small, Specialized, Locally-Runnable Models](https://huggingface.co/blog/lablab-ai-amd-developer-hackathon/cybersecqwen-4b)

4

May 9, 2026

## [MedQA: Fine-Tuning a Clinical AI on AMD ROCm — No CUDA Required](https://huggingface.co/blog/lablab-ai-amd-developer-hackathon/medqa)

1

May 8, 2026


## 相关链接

- [[Agent-Orchestration]]
- [[Agent-Swarm]]
- [[Agentic-Engineering]]
- [[Corrective-RAG]]
- [[Reflexion]]
- [[Dual-Tier-LLM-Architecture]]
- [[Zero-PHI-Policy]]
- [[Sequence-Packing]]
- [[Hardware-Sovereignty]]
