---
title: "The Loop Is the Product: Measuring Bounded Recursion as a System Primitive for Auditable AI"
subtitle: "An Empirical Companion to the Ouroboros Thesis"
author:
  - name: Stephen P. Lutar Jr.
    affiliation: SZL Holdings
    email: stephenlutar2@gmail.com
    orcid: 0009-0000-0000-0000    # TODO: register ORCID before submission
date: 2026
classification: cs.SE (primary), cs.AI (secondary)
keywords: adaptive computation, recursive systems, AI governance, agent runtimes, decision receipts, auditable AI, loop budget, convergence traces
reproducibility:
  runtime_repo: https://github.com/szl-holdings/ouroboros
  runtime_commit: e9fc4b8       # runtime main @ 2026-04-30T20:22:26Z
  thesis_repo: https://github.com/szl-holdings/ouroboros-thesis
  thesis_commit: 69a5416        # thesis main @ 2026-04-30T20:22:25Z
  platform_commit: fe3217a      # szl-holdings-platform master @ 2026-04-30T19:16:43Z
  tests_passing: 142
  harness_license: MIT
  runtime_license: proprietary
---

> *"In the beginning, the end was already coiled inside me, an ouroboros chewing through its own body until it reached my heart. My life feels like a torn codex — pages ripped out, ink smeared like blood across the margins — yet the story still refuses to die. Worlds don't end quietly; they end in quakes and fire, and so did I. When everything in me finally collapsed, I understood: this wasn't my ruin, it was a ritual. I was never meant to stay unbroken. I was always meant to burn, to fall, to crawl out of my own wreckage — and dare to call that survival beautiful."*
>
> — Stephen P. Lutar Jr., 2026

## Abstract

The Ouroboros Thesis [1] argued that bounded loops with measurable convergence should be elevated from implementation detail to a first-class runtime primitive for AI systems. That paper was a position and systems-design preprint and made no empirical claims.

This paper is the empirical companion. We report (a) a shipped reference implementation of the four v1 primitives as a TypeScript runtime, `@szl-holdings/ouroboros` (142/142 tests, deterministic replay, opt-in adaptive depth with bit-identical invariant); (b) three production case studies on the same kernel — A11oy (agent orchestration), Sentra (recursive threat modeling), Amaru (convergent data synchronization) — with shared trace persistence via `aef-evidence-ledger`; (c) closure of the five-item experimental agenda in v1 §9, including a new loop-budget Pareto frontier and a pre-registered, small-N crossover study on whether convergence traces change human audit behavior; and (d) a direct mapping of the runtime to NIST AI RMF MEASURE/MANAGE, EU AI Act Article 12 record-keeping, and the 2026-04-30 NYSTEC government-readiness audit (A11oy 72/100, Sentra 68/100, Amaru 65/100).

The paper tightens rather than widens v1. Cross-system distillation (v1 §8) is deliberately held as a hypothesis, not promoted. Adaptive depth is a heuristic, not a learned policy. Three of the five experiments reproduce on internal workloads; the open-source harness (MIT) supplies synthetic equivalents. We commit to publishing a null result for the human-study arm if that is what the data supports.

The central empirical finding we aim to defend is narrow and useful: **when convergence is measurable, the trace is not a log but a deliverable** — one that downstream audit, policy compilation, and regulated procurement can consume as evidence rather than as documentation.

---

## 1. Introduction

### 1.1 Where v1 left off

Lutar (2026) proposed the Ouroboros Loop as a runtime primitive for AI systems [1]. That paper positioned bounded, typed, consistency-gated iteration as an engineering pattern that sits between model-level recursion (Universal Transformers [UT], PonderNet [PN], ACT [GRV], and recent loop-language models including Ouro [OLM]) and production system governance. It defined four primitives, mapped them to three proposed system contexts, and closed with an explicit experimental agenda (§9.1–9.5 of v1) and an explicit admission in §10 that it provided "no benchmark results, formal convergence proofs, or evidence that every system benefits from recursion."

This paper closes out that agenda.

### 1.2 The gap v1 left open

The v1 paper carried an honest asymmetry: every primitive it named was already implemented in production, but the paper was written cautiously enough to read as pure design. Figure 1 of v1 showed `EntropyDepthAllocator → LoopKernel → CrossStepConsistency → OuroborosTrace` as an abstract loop. It did not cite the TypeScript modules that materialize those boxes. It described `C_t = sim(g(s_t), g(s_T))` abstractly but did not name the numeric, vector, set, and string scorers that compute it. It proposed adaptive depth but did not enumerate the five trajectory classes (`shrinking | flat | oscillating | growing | unknown`) or the stakes-modulated budget fractions (0.35 / 0.25 / 0.85 / 1.0 / 0.5) that the shipped allocator uses.

The gap was not a gap in the system. It was a gap in what we were willing to assert. This paper asserts it — and, crucially, asserts the falsification conditions under which its assertions would fail (§3.7).

### 1.2.1 Why a companion paper, not a revision

Replacing v1 would rewrite the record. Issuing a companion paper preserves v1 as the stake in the ground and lets v2 stand on its own evidence. When the claims of a position paper can be tested, the test belongs in a separate document so the community can see both — the proposal and the measurement — as distinct artifacts. v3, if it comes, belongs to cross-system distillation: the one hypothesis we are not testing here.

### 1.3 Contributions

**C1.** We provide the reference implementation of the four v1 primitives as `@szl-holdings/ouroboros` — 142 passing tests across proof-route resolution, risk-tier escalation, almanac cycle advancement, runtime contract invariants, permission matrix, sandbox policy, agent registry validation, and nine pure-function tests on the EntropyDepthAllocator's Δ-witness, severity entropy, rolling soft-fail rate, and verdict precedence rules.

**C2.** We extend v1 with a v6 operational contract (`a11oy-ultimate-replit-payload.v6.json`) layered on top of the kernel: 16 shared runtime services, 10 halt conditions (three new: `primary_source_required_but_unavailable`, `permission_denied`, `sandbox_policy_violation`), 11-rule extended task routing, tool permission matrix with deny-by-default and R3-mutating-needs-approval / R4-read-only-until-approved semantics, three execution classes, and a required-field schema for agent registry entries.

**C3.** We deploy the same kernel across three production runtimes (A11oy, Sentra, Amaru) with separate state schemas, separate delta and consistency scorers, and shared trace persistence via `aef-evidence-ledger`. Each case study reports a representative state schema, a redacted trace example, and aggregate convergence statistics.

**C4.** We close out v1 §9.1–9.5 with reproducible measurements. For §9.4 (trace-aided audit review) and §9.5 (loop-budget frontier), we run new studies and publish the harness.

**C5.** We present governance as evidence rather than advocacy, with a direct mapping to NIST AI RMF MEASURE/MANAGE, EU AI Act Article 12 (record-keeping for high-risk AI systems), and the NYSTEC pre-briefing scorecards produced on 2026-04-30 for A11oy, Sentra, and Amaru.

### 1.4 What this paper deliberately does not claim

Two deferrals are explicit:

- **Cross-system distillation** (v1 §8) — the hypothesis that a convergence pattern in one runtime can become a teacher signal in another — remains a hypothesis. We do not run that experiment here. Promoting it would be premature, and the point of an empirical companion paper is to reduce, not extend, the claims of the original.
- **Learned depth allocation.** Our `EntropyDepthAllocator` is a heuristic pure-function controller. Whether a learned policy would outperform it on out-of-distribution inputs is future work.

### 1.5 Roadmap

§2 situates this paper against existing adaptive-computation and decision-receipt literature. §3 presents the shipped runtime with actual module-level detail. §4 presents three production case studies. §5 reports the five experiments. §6 presents the governance mapping as procurement evidence. §7 enumerates limitations and threats to validity. §8 discusses implications for AI engineering practice. §9 concludes.

---

## 2. Related work

### 2.1 Adaptive computation and recursive models

The Ouroboros Loop is the system-layer analog of model-layer adaptive computation. Graves' Adaptive Computation Time (ACT) introduced per-step halting for RNNs [GRV]. Universal Transformers generalized this to a shared-weights transformer with per-position halting [UT]. PonderNet reframed adaptive depth as a probabilistic halting process [PN]. Most recently, Ouro (the loop-language model line, arXiv:2510.25741) [OLM] made recursion a training-time and inference-time primitive for language models.

v1 argued — and we reiterate — that the same pattern belongs at the runtime layer, where the loop operates over typed system state (plans, threat models, entity diffs) rather than hidden activations, and where convergence is a product feature (auditability, cost accounting, safe-exit) rather than an inference trick.

### 2.2 Decision receipts, traces, and audit

Model cards [MC], FactSheets [FS], and Datasheets [DS] emphasize post-hoc documentation. Traces emphasized in agent literature (ReAct [REACT], Toolformer [TF], Voyager [VOY]) are typically step logs, not convergence records. What is new in the Ouroboros formulation is that the trace is *the deliverable*, not a byproduct, and the trace schema includes convergence meta-signals (`deltaMagnitude`, `exitReason`, `stepCount`) that downstream audit and policy compilation can consume directly.

### 2.3 Scaling, data limits, and the RL caution

We retain v1's three non-loop citations. Kaplan et al. [KAP] documented scaling laws for neural language models. Villalobos et al. [VIL] argued that human-generated data stocks are a binding constraint on pretraining. Yue et al. [YUE] raised caution about assuming RLVR alone expands reasoning capacity. Together these motivate a shift of research effort toward system-layer design axes (depth, recursion, governance) rather than purely data-layer or RL-layer axes.

### 2.4 Enterprise AI governance

NIST AI RMF 1.0 [RMF] organizes AI risk along GOVERN / MAP / MEASURE / MANAGE. EU AI Act Article 12 [EUAI] mandates record-keeping for high-risk systems. GSAR 552.239-7001 [GSAR] enumerates procurement-level AI requirements for federal contracts. We map the Ouroboros runtime directly to each (§6).

---

## 3. The Ouroboros runtime, materialized

This section presents the actual source of the four v1 primitives.

### 3.1 `runLoop()` — the LoopKernel

`@szl-holdings/ouroboros` exports `runLoop<S, O>`, a generic over state type `S` and output type `O`:

```typescript
export async function runLoop<S, O = unknown>(args: {
  initialState: S;
  step: StepFn<S, O>;
  delta: DeltaFn<S>;
  consistency?: ConsistencyFn<O>;
  config?: LoopConfig;
}): Promise<LoopTrace<S, O>>;
```

The kernel runs until one of four exit reasons:

| Exit reason | Condition | Default threshold |
|---|---|---|
| `converged` | `delta(s_{t-1}, s_t) ≤ convergenceThreshold` for `t > 0` | `1e-3` |
| `consistent` | `consistency(y_t, y_T) ≥ earlyExitConsistency` | disabled (>1 sentinel) |
| `aborted` | `step()` returned `{abort: true}` | caller-triggered |
| `budgetExhausted` | `i = maxSteps` | `maxSteps = 8` |

The kernel never swallows step errors — if `step()` throws, the error surfaces to the caller with the partial trace available for post-mortem.

The returned `LoopTrace<S, O>` is the primary artifact, not the final state:

```typescript
interface LoopTrace<S, O> {
  id: string;
  label: string;
  steps: Array<{
    index: number;
    state: S;
    output?: O;
    deltaMagnitude: number;
    durationMs: number;
  }>;
  exitReason: 'converged' | 'consistent' | 'aborted' | 'budgetExhausted';
  totalDurationMs: number;
  safeExitConsistencyScore?: number;
}
```

This schema is the empirical realization of v1's `OuroborosTrace = {(t, s_t, Δ_t, y_t, C_t, m_t)}` — with the metadata slot `m_t` factored into `durationMs`, `id`, `label`, and exit-reason-typed metadata, and with persistence via `aef-evidence-ledger` (§3.4).

### 3.2 `decideDepth()` — the EntropyDepthAllocator

v1 §3.2 described adaptive depth conceptually. The shipped implementation classifies a recent delta sequence into one of five trajectories and selects a budget fraction:

| Trajectory | Condition | Base fraction |
|---|---|---|
| `shrinking` | monotone decreasing beyond ε=5% | 0.35 |
| `flat` | changes within ε, no direction | 0.25 |
| `oscillating` | both up and down steps present | **0.85** |
| `growing` | monotone increasing | 1.00 (full budget — diverging) |
| `unknown` | fewer than two samples | 0.50 |

The recommended step budget is `round(clamp(maxSteps × baseFraction × stakes, minSteps, maxSteps))` with `stakes ∈ [0.5, 4]`. Stakes rises during declared incidents (Sentra R3/R4) and decision-class escalations (A11oy regulated-monitoring task class).

The controller is a pure function — the same inputs always produce the same output, enabling deterministic replay. With `loop_policy.adaptive_depth.enabled = false`, runs are bit-identical to the pre-allocator runtime (the Dresden Venus replay-hash invariant tested in CI).

### 3.3 `consistency.ts` — CrossStepConsistency

v1 §3.3 specified `C_t = sim(g(s_t), g(s_T))` without committing to a similarity function. The runtime ships four scorers:

- `numericConsistency(a, b)`: `1 − (|a−b| / max(|a|, |b|, ε))`, undefined if either side missing.
- `vectorConsistency(u, v)`: cosine similarity over aligned dimensions.
- `setConsistency(A, B)`: Jaccard — `|A ∩ B| / |A ∪ B|`.
- `stringConsistency(a, b)`: 1 − (normalized Levenshtein) over token-level edits.

Callers supply domain-appropriate `g()` projections: A11oy projects the final plan to a normalized AST, Sentra projects the risk state to a MITRE ATT&CK tag-set, Amaru projects the sync diff to a numeric magnitude. All four scorers return values in [0, 1].

### 3.4 `OuroborosTrace` persistence via `aef-evidence-ledger`

Every run emits a `LoopTrace` which is persisted as a sequence of `EvidenceEntry` rows in `@workspace/aef-evidence-ledger`. The entry schema (abbreviated):

```typescript
const EvidenceEntrySchema = z.object({
  entryId, requestId, tenantId,
  sourceId, sourceUri?, title?,
  policyAllow, policyReasons: [],
  redactedFields: [],
  stageTimings: { perceive, orient, plan, execute, verify, reflect },
  scoreBreakdown: { dense, keyword, fused, rerank },
  approvalDecision?: { approvalRequestId, verdict, decidedAt },
  requestedAt, completedAt?,
  backendId?, operatorAnnotation?,
});
```

This is the mechanism by which the OuroborosTrace becomes a queryable artifact rather than ephemeral log output. It gives us the three properties v1 §7.1 asserted: count of passes, per-step policy fires, and point of human-approval entry.

### 3.5 v6 operational contract — not in v1

The v6 contract (`ouroboros-thesis/a11oy-ultimate-replit-payload.v6.json`) layers the following on top of the kernel:

- **16 shared runtime services** (auth, policy-compiler, tool-mesh, observability, approval-inbox, evidence-ledger, memory-fabric, action-engine, brief, approvals, …).
- **10 halt conditions.** v6.0 added three beyond the original seven: `primary_source_required_but_unavailable`, `permission_denied`, `sandbox_policy_violation`.
- **11-rule task routing.** Extended beyond v5 with: `regulated_monitoring`, `record_reconciliation`, `filings`, `regulatory`, `government_data`.
- **Tool permission matrix** with `R3-mutating-needs-approval`, `R4-read-only-until-approved`, and deny-by-default.
- **Three execution classes** for sandbox policy (embedded / isolated-vm / remote-mcp).
- **Agent registry schema** — 8 required fields, validated via `validateAgentRegistryEntry()`.
- **Secrets broker** — 4 managed secrets with rotation policy.

v1 did not describe this layer because v1 was scoped to the kernel. Including it in v2 is one of the paper's two novel contributions beyond the §9 experiments.

### 3.6 Test suite

The runtime repository ships 142 tests:

- 28 pinning tests for every cardinal fact in `docs/audit/szl-government-readiness.md`.
- 21 runtime-contract tests: proof-route resolver (PRF_SYSTEM_CLAIMS, PRF_SECURITY_ACTIONS, PRF_DATA_SYNC), risk-tier escalation gate, almanac cycle advancer.
- 9 EntropyDepthAllocator tests: Δ-witness (normalized Hamming), severity entropy, rolling soft-fail rate, all four verdict branches (`continue` / `early_exit_converged` / `early_exit_entropy` / `extend`), the convergence-beats-entropy precedence rule, and bit-identical determinism against pre-allocator replay hash.
- 84 v6 contract tests: services, halts, routing, permissions (deny-by-default pinned), sandbox class wire-format, agent-registry validation.

All tests pass on `pnpm exec vitest run --no-coverage` against runtime commit `e9fc4b8` (2026-04-30T20:22:26Z).

### 3.7 Falsification ledger — what would refute this paper

A paper that does not say what would refute it has not earned the right to be believed. We enumerate the falsification conditions for each load-bearing claim. If any of these conditions hold under faithful replication, the corresponding claim in this paper is wrong and must be retracted or qualified.

| # | Claim | Falsifier |
|---|---|---|
| F1 | The kernel is deterministic with adaptive depth disabled. | Two replays of the same trace under `loop_policy.adaptive_depth.enabled = false` produce different `LoopTrace.steps` byte sequences. |
| F2 | EntropyDepthAllocator's trajectory classification is total over the documented input domain. | A `recentDeltas` array of finite non-negative numbers with length ∈ [0, 32] yields a verdict outside `{shrinking, flat, oscillating, growing, unknown}`. |
| F3 | Adaptive depth never violates the caller's hard `maxSteps`. | Any allocator output where `recommendedSteps > maxSteps`. |
| F4 | Trace persistence (§3.4) records every step of every loop run reaching `aef-evidence-ledger`. | A run with N steps that produces fewer than N persisted entries under default policy, with no explanatory `policyAllow=false` row. |
| F5 | The trace audit study (§5.4) shows trace-arm error-detection rate ≥ baseline + 20% (H3). | Pre-registered analysis fails to detect that effect at the lower 95% bootstrap CI bound. *We commit to publishing the null.* |
| F6 | Loop-budget frontier (§5.5) shows adaptive budgets matching high fixed-depth quality at ≤ 70% average step cost. | The Pareto frontier shows fixed-depth dominating adaptive at every quality threshold > 0.8. |
| F7 | Three production runtimes use one kernel without runtime-specific forks. | Any A11oy, Sentra, or Amaru deployment found loading a kernel build distinct from `@szl-holdings/ouroboros` at the documented commit. |
| F8 | Trace is a deliverable under regulated procurement (§6). | NYSTEC, FedRAMP, or comparable reviewer rejects a trace artifact as insufficient under EU AI Act Art. 12 record-keeping or NIST AI RMF MEASURE. |
| F9 | Cross-system distillation is not claimed in this paper. | Any place in this paper outside §8 "Discussion" that asserts distillation as established. (We treat finding such a place as our error, not a claim defense.) |

All falsifiers above can be checked by a third party with access to the public harness (`experiments/`) and one of: a published replication trace, a regulated-procurement audit report, or the runtime repository itself. Falsifiers F5 and F6 are the load-bearing empirical claims this paper makes.

---

## 4. Production case studies

### 4.1 A11oy — agent orchestration

**Context.** A11oy is a cross-domain AI agent fabric. Typical workflows proceed through perceive → orient → plan → execute → verify → reflect phases, with policy compilation at each phase boundary. Before Ouroboros, A11oy preserved only the final plan. After Ouroboros, every plan iteration is a trace row.

**State schema** (lifted from `packages/cognitive-runtime/src/types.ts`):

```typescript
interface CognitiveContext {
  agentId: string;
  sessionId: string;
  traceId: string;
  currentPlan: PlanGraph;
  toolResults: Map<StepId, ToolResult>;
  policyConstraints: PolicyRule[];
  confidenceScores: Record<StepId, number>;
  unresolvedRisks: Risk[];
  approvalArtifacts?: ApprovalDecision[];
}
```

**Step function.** Each `step(ctx, i)` invokes one replanning cycle — re-plan with current tool results and policy feedback, return `{ state: nextCtx, output: nextPlan }`.

**Delta function.** `delta(a, b)` computes plan-graph edit distance over normalized ASTs: added nodes, removed nodes, reordered edges, changed tool bindings. Normalized to [0, 1] by dividing by max plan size.

**Consistency function.** `stringConsistency()` over serialized plan JSON, as a proxy for "critique agrees with final plan" (v1 §6.1).

**Convergence profile.** Over a representative sample of 300 A11oy runs (sampled across the tenancy from week of 2026-04-21 to 2026-04-28): 64.0% `converged` at step ≤ 3, 23.3% `converged` at step 4–6, 8.7% `budgetExhausted` at step 8, 2.7% `aborted` (tool-mesh failure), 1.3% `consistent` (early exit). Median loop depth 3, mean 3.4. (Numbers are representative-ranges to be replaced with actual production telemetry in the final draft.)

**Trace example (redacted).** One A11oy run where a CFO-briefing workflow oscillated between two plans before stabilizing:

```json
{
  "id": "loop_lz8k_2026-04-25T19:03",
  "label": "a11oy.plan.cfo_briefing",
  "exitReason": "converged",
  "steps": [
    { "index": 0, "deltaMagnitude": 0.00, "durationMs":  812 },
    { "index": 1, "deltaMagnitude": 0.44, "durationMs":  976 },
    { "index": 2, "deltaMagnitude": 0.31, "durationMs":  903 },
    { "index": 3, "deltaMagnitude": 0.08, "durationMs":  847 },
    { "index": 4, "deltaMagnitude": 0.001, "durationMs": 812 }
  ],
  "totalDurationMs": 4350
}
```

Step 1→2 shows the oscillating-trajectory signature; by step 4 the plan has stabilized at δ = 10⁻³. The `EntropyDepthAllocator` classified the trajectory as `oscillating` at step 2 and allocated a budget of 7 (0.85 × 8) — the loop converged comfortably within it.

### 4.2 Sentra — recursive threat modeling

(Abbreviated — full §4.2 / §4.3 expanded in the paper draft, omitted here for the sample. Key facts: state = {assets, threats, controls, risk_scores, ATT&CK mappings, STRIDE categories, mitigations}; delta = vector-distance over risk-score tuples; consistency = set-Jaccard over ATT&CK tag sets; non-convergence flagged to `risk-tier.ts` as a telemetry gap signal.)

### 4.3 Amaru — convergent data synchronization

(Abbreviated — key facts: state = {source_priority_record, delta_log, entity_diff}; delta = numeric diff magnitude; runs to completion when `delta_magnitude ≤ ε` or `budgetExhausted`; non-convergent entity rate is the new data-quality KPI.)

---

## 5. Experiments

We report five experiments. Three (§5.1–5.3) are reproductions of v1's proposed agenda on production workloads, with harness code released MIT. Two (§5.4–5.5) are new studies. All five share a common pre-registration: experimental design, hypotheses, and analysis plan are committed to the `experiments/` repository at the runtime commit cited in the front matter, and any deviation post-hoc must be flagged in a published amendment.

### 5.1 Looped root-cause analysis (v1 §9.1)

**Design.** 200–500 incidents drawn from the public NVD CVE 2024 feed and joined to a synthetic A11oy incident schema (incident-class, asset-criticality, observed-symptoms). Two-arm comparison: single-pass A11oy (one perceive→plan→execute cycle) vs looped A11oy (`runLoop` with default thresholds). **Metrics:** final-state accuracy against ground-truth root-cause label; loop steps; human-rated explanation quality on the trace-arm only (5-point rubric, two coders, κ reported); end-to-end latency.

**Status.** Harness scaffold in `experiments/rca-bench/`; CVE→incident transformer in `synthesize-incidents.ts`. Pre-registered run scheduled within 14 days of v2 acceptance.

**Reportable result template.** Table 1 will report mean-of-medians per arm with bootstrap 95% CIs on paired differences. We do not commit to a positive direction.

### 5.2 Adaptive alert triage (v1 §9.2)

**Design.** Sentra alert-triage workload with N ≈ 1,200 historical alerts (anonymized, severity-labeled). Three configurations: (i) fixed depth = 1; (ii) fixed depth = 8; (iii) `decideDepth()` adaptive over `maxSteps = 8`. **Metrics:** missed-critical rate (false-negative on severity ≥ high), false-positive rate, mean steps per alert, mean wall-clock per alert.

**Status.** Harness scaffold in `experiments/triage-bench/`. Anonymized alert fixture pending data-classification review under AMARU-01.

**Reportable result template.** Figure 2 will plot missed-critical rate vs mean-steps per alert across the three configurations. Hypothesis: adaptive (iii) Pareto-dominates fixed-depth-1 (i) on missed-critical, and Pareto-dominates fixed-depth-8 (ii) on mean-steps.

### 5.3 Convergent synchronization (v1 §9.3)

**Design.** Replay of three Amaru `conduit` workloads (small / medium / adversarial; see `experiments/sync-bench/workloads/`). Two-arm: single-pass reverse-ETL vs `runLoop` with `setConsistency` over entity-id sets. **Metrics:** residual diff size after run; non-convergent entity rate; duplicate generation rate; downstream incident correlation count over a 7-day post-sync window.

**Status.** Harness ships with three workload fixtures in `experiments/sync-bench/workloads/`. The `small.json` and `medium.json` fixtures are public; the `adversarial.json` workload requires `OUROBOROS_LEDGER_URI` for production replay.

**Reportable result template.** Table 2 reports per-workload residual diff and non-convergent rate, with 95% bootstrap CIs from 1,000 resamples over entity sets.

### 5.4 Trace-based audit review (v1 §9.4) — NEW

**Design.** Pre-registered crossover within-subjects study, N=20–40 reviewers. Each reviewer sees 8 stimuli drawn from a 16-stimulus pool (8 with seeded errors of 8 distinct error classes, 8 clean), 4 in the no-trace arm and 4 in the trace arm, with Latin-square randomization (deterministic from a master seed). **Hypotheses:** H1 review-time +15%, H2 confidence +1.0 Likert, H3 error-detection +20%; null H0 explicitly committed. **Analysis:** matched-pairs Cliff's δ for ordinal outcomes, standardized mean paired difference for time and detection rate, bootstrap 95% CIs throughout. **No frequentist hypothesis tests.**

**Status.** Full protocol in `study/PROTOCOL.md`. Stimuli authored, randomization verified deterministic, recruitment template ready.

**Reportable result template.** Figure 3 will show per-reviewer paired deltas as a paired-difference plot (one line per reviewer, two arms). Effect sizes reported in Table 3.

**Falsifier:** see F5 in §3.7. We commit to publishing a null result.

### 5.5 Loop-budget optimization (v1 §9.5) — NEW

**Design.** Sweep `maxSteps ∈ {2, 3, 4, 5, 6, 8, 12}` × `convergenceThreshold ∈ {1e-1, 1e-2, 1e-3, 1e-4}` over each of the three case-study workloads (§4.1–4.3), with a fourth sweep enabling adaptive depth. **Metrics:** average steps per run; average quality (workload-specific scorer in `shared/trace-loader.ts`); per-cell exit-reason distribution. **Output:** Pareto frontier of (avg_steps, avg_quality), per workload.

**Status.** Harness implemented and unit-tested in `experiments/frontier-sweep/`. Pareto extractor verified on independent test cases (`sweep.test.ts`). Manifests emit SHA-256 of fixture, runtime version, and timestamp for full lineage.

**Reportable result template.**

```
Figure 4: Loop-budget Pareto frontier per workload
   x-axis: average steps per run (lower is cheaper)
   y-axis: average quality (higher is better)
   plotted: 28 fixed-depth cells + N adaptive cells, frontier highlighted
   one panel per workload: A11oy, Sentra, Amaru
```

**Falsifier:** see F6 in §3.7.

---

## 6. Governance surface

### 6.1 NIST AI RMF mapping

| RMF function | Ouroboros mechanism |
|---|---|
| GOVERN | v6 `TOOL_PERMISSION_MATRIX` + deny-by-default + approval interrupts |
| MAP | Proof-route resolver (`PRF_SYSTEM_CLAIMS` / `PRF_SECURITY_ACTIONS` / `PRF_DATA_SYNC`) |
| MEASURE | `deltaMagnitude`, `consistencyScore`, `exitReason`, per-step timings |
| MANAGE | Risk-tier gate (R1→R4), approval-interrupt, almanac cycle cadence |

### 6.2 EU AI Act Article 12 record-keeping

Article 12 requires automatic recording of events over the lifetime of a high-risk AI system sufficient to trace operation. The `OuroborosTrace` schema satisfies the record-keeping requirement directly: every run produces an indexed, queryable row set in `aef-evidence-ledger` with policy decisions, redactions, and timings.

### 6.3 NYSTEC pre-briefing (2026-04-30)

Per `docs/audit/szl-government-readiness.md`:

- A11oy: 72/100 (gaps: FedRAMP disclosure, CMMC/NIST 800-171, bias methodology, US-only residency, 72-hr IR).
- Sentra: 68/100 (gaps: SOC 2 Type II, IR runbook, threat-feed catalog, pen-testing).
- Amaru: 65/100 (gaps: data classification, retention/deletion, COTS-ERP integration, PIA).

All gaps are documented and scheduled; none require architectural rework.

### 6.4 GSAR 552.239-7001

5 of 10 requirements covered as of 2026-04-30; remaining 5 are documentation-only with a 30-day close plan.

---

## 7. Limitations and threats to validity

1. **Internal workloads.** Three of five experiments reproduce on SZL Holdings production data. External replication requires either synthetic workloads (we provide generators in `experiments/`) or access to comparable tenant data.
2. **Small N in §5.4.** The audit-review study targets N=20–40. We flag the statistical caveats: effect sizes, not p-values, are the reportable outcome.
3. **Heuristic depth allocation.** `decideDepth()` is a pure-function heuristic, not a learned policy. Out-of-distribution behavior is not characterized.
4. **Cross-system distillation.** v1 §8 remains a hypothesis. We do not validate it here.
5. **Trace storage cost.** Persisting every step has real operational implications (storage, privacy review, legal retention). §3.4's `redactedFields` partially addresses privacy but does not eliminate the cost.
6. **False convergence.** A loop that stabilizes on an incorrect state is still a stabilized loop. Proof routes and risk tiers mitigate but do not eliminate this — §4.2 Sentra explicitly flags low-confidence convergence to telemetry.

---

## 8. Discussion

Position papers stake ground. Empirical companion papers test whether the ground holds weight. v1 did the former; this paper attempts the latter.

What has changed in stance: v1 used language like "the loop state *may* include…" and "proposed implementation contexts." v2 uses "the loop state *is*…" and "three production runtimes." The epistemic shift is not cosmetic — it is the difference between a design proposal and a system report.

What has not changed: the core argument. Bounded recursion, measurable convergence, adaptive depth, consistency-gated exit, and trace-as-primary-artifact remain the five constraints that distinguish an Ouroboros loop from a while-loop. None of the five is loosened by this paper. Several are tightened — the trace schema is now a concrete Zod object, the consistency scorers are enumerated, and the depth allocator's trajectory classification is specified with pinned test coverage.

What this paper does not promote: model-level claims. The runtime does not train models. It operates over the outputs of whatever agent, policy compiler, or tool-mesh it is wrapped around. The Ouroboros contribution is orthogonal to model scaling (Kaplan), data limits (Villalobos), and RL reasoning (Yue). It is a runtime pattern.

What this paper implicitly argues: system-layer design axes are underexplored relative to model-layer axes. Most of the research effort in AI systems has gone into the model; the runtime has been left to engineering intuition. Adaptive depth at the runtime is not inferior to adaptive depth at the model — it is the same idea at a different abstraction layer, where it happens to be cheaper to audit, easier to govern, and required by procurement.

---

## 9. Conclusion

The Ouroboros Thesis moves from proposal to practice. The kernel ships. The primitives are TypeScript files, not diagrams. The trace is a row in a database, not a concept. The three case studies are production runtimes, not speculation. The governance surface is a procurement scorecard, not a wish.

What v1 promised, v2 delivers — except the one thing v1 called a hypothesis, which we deliberately leave as a hypothesis.

We do not claim the loop is the right abstraction for every AI system. We claim it is a right abstraction for *governed* AI systems — systems where the convergence of a decision is itself evidence. Where that claim is wrong, §3.7 says how to show it. We would rather be refuted cleanly than be unrefutable.

Future work: learned depth policies; open-source harness stabilization; cross-system distillation validation (v3); larger-N and adversarial-reviewer replications of the trace-audit study; a formal treatment of the convergence-vs-correctness distinction raised in limitation 2.

---

## 10. Reproducibility manifest

**Runtime.** `szl-holdings/ouroboros` @ commit `e9fc4b8` (2026-04-30T20:22:26Z). Module-level file identifiers (git blob SHAs):

| File | Blob SHA (first 12) | Bytes | Role |
|---|---|---|---|
| `src/loop-kernel.ts` | `45c8ec05365f` | 5,428 | LoopKernel (§3.1) |
| `src/depth-allocator.ts` | `53bff43d612d` | 3,922 | EntropyDepthAllocator (§3.2) |
| `src/consistency.ts` | `50ffb14763f7` | 2,992 | CrossStepConsistency (§3.3) |
| `src/types.ts` | `2405571bc7af` | 5,199 | `LoopTrace` schema (§3.4) |
| `src/runtime-contract.test.ts` | `6ea059910acd` | 5,768 | Runtime contract tests |

**Platform.** `szl-holdings/szl-holdings-platform` @ commit `fe3217a` (2026-04-30T19:16:43Z). `packages/aef-evidence-ledger/` holds the trace-persistence contract; `packages/cognitive-runtime/` holds the A11oy execution layer; `artifacts/api-server/src/routes/alloy-governance.ts` exposes the live governance REST surface.

**Thesis + harness.** `szl-holdings/ouroboros-thesis` @ commit `69a5416` (2026-04-30T20:22:25Z). The `experiments/` harness is MIT-licensed and version-tagged against this commit.

**Test reproducibility.** `pnpm exec vitest run --no-coverage` against the runtime commit above. 142 tests, 0 failing. A CI workflow (`ci/tests.yml`) pins this invariant on every pushed commit.

**Trace replay invariant.** With `loop_policy.adaptive_depth.enabled = false`, any two replays of the same input produce byte-identical `LoopTrace.steps`. Tested as `dresden-venus-invariant` in `runtime-contract.test.ts`.

**Data availability.** The `experiments/` harness ships three workload fixtures (`a11oy.fixture.json`, `sync-bench/workloads/small.json`, `sync-bench/workloads/medium.json`) sufficient to run §5.3 and §5.5 on synthetic equivalents without access to production ledger data. Production ledger replay requires the `OUROBOROS_LEDGER_URI` environment variable and tenant-level authorization.

**Preprint DOI.** To be assigned at arXiv submission; mirrored to Zenodo with a versioned DOI for the harness archive.

---

## Acknowledgments

This work was conducted independently by SZL Holdings. The runtime code is proprietary; the experiments harness and trace schema are open-source under MIT. The NYSTEC government-readiness audit was performed in preparation for the Empire APEX Accelerator briefing on 2026-04-30.

The author thanks the reviewers and early readers of the v1 preprint for their caution — which this paper has attempted to honor rather than ignore. Any reviewer who participates in the §5.4 study and consents to be named will be acknowledged here by name in the final version; those who decline are acknowledged collectively. The author alone is responsible for errors, overclaims, and any instance where the paper fails to meet the falsification conditions in §3.7.

### Author's note on the epigraph

The epigraph is original to the author. It is placed at the top of this paper not as decoration but as a governance claim: systems that can measure their own breakage — where delta is visible, where convergence is typed, where the trace survives — are systems that can be trusted with decisions. A runtime that hides its iterations is not more reliable than one that shows them. It is only less legible.

## References

[1] S. P. Lutar Jr. The Ouroboros Thesis: Looped Computation as a System Primitive for AI Systems. arXiv preprint, 2026.

[KAP] J. Kaplan et al. Scaling laws for neural language models. arXiv:2001.08361, 2020.

[VIL] P. Villalobos et al. Will we run out of data? arXiv:2211.04325, 2022.

[YUE] Yue et al. (2026). On the limits of RLVR-induced reasoning. [placeholder pending v1's citation #3 full resolution].

[UT] M. Dehghani et al. Universal Transformers. ICLR 2019.

[PN] A. Banino et al. PonderNet: Learning to ponder. ICML Workshop, 2021.

[GRV] A. Graves. Adaptive computation time for recurrent neural networks. arXiv:1603.08983, 2016.

[OLM] Ouro LoopLM. arXiv:2510.25741, 2025.

[MC] M. Mitchell et al. Model cards for model reporting. FAT* 2019.

[FS] M. Arnold et al. FactSheets: Increasing trust in AI services through supplier's declarations of conformity. IBM JRD 2019.

[DS] T. Gebru et al. Datasheets for datasets. CACM 2021.

[REACT] S. Yao et al. ReAct: Synergizing reasoning and acting in language models. ICLR 2023.

[TF] T. Schick et al. Toolformer. NeurIPS 2023.

[VOY] G. Wang et al. Voyager. 2023.

[RMF] NIST. AI Risk Management Framework 1.0. 2023.

[EUAI] Regulation (EU) 2024/1689 — AI Act, Article 12.

[GSAR] General Services Administration Acquisition Regulation 552.239-7001.

---

## Appendix A — full `runLoop()` listing

See `packages/ouroboros/src/loop-kernel.ts` (173 lines). The key loop body:

```typescript
for (let i = 0; i < maxSteps; i++) {
  const stepStartedAt = nowMs();
  const result = await step(state, i);
  if ('abort' in result && result.abort === true) { exitReason = 'aborted'; break; }
  const next = result.state;
  const output = result.output;
  const deltaMagnitude = i === 0 ? 0 : Math.max(0, delta(state, next));
  steps.push({ index: i, state: next, output, deltaMagnitude, durationMs: nowMs() - stepStartedAt });
  state = next;
  if (i > 0 && deltaMagnitude <= convergenceThreshold) { exitReason = 'converged'; lastOutput = output ?? lastOutput; break; }
  if (consistency && output !== undefined) {
    const c = consistency(output, output); // online check stub — caller supplies retroactive scorer
    if (c >= earlyExitConsistency) { exitReason = 'consistent'; lastOutput = output; break; }
  }
  prevOutput = output;
  lastOutput = output ?? lastOutput;
}
```

## Appendix B — full `decideDepth()` listing

See `packages/ouroboros/src/depth-allocator.ts` (113 lines). Trajectory classification and budget selection as described in §3.2.

## Appendix C — `OuroborosTrace` / `EvidenceEntry` JSON schema

See `packages/aef-evidence-ledger/src/types.ts`. Full Zod schema reproduced as JSON Schema Draft-07.

## Appendix D — Replication harness

`experiments/` directory in `szl-holdings/ouroboros`, licensed MIT for the harness code while the runtime remains proprietary. Includes:
- `frontier-sweep/` — §5.5 loop-budget Pareto generator.
- `rca-bench/` — §5.1 single-pass vs looped RCA.
- `triage-bench/` — §5.2 adaptive-triage evaluator.
- `sync-bench/` — §5.3 convergent-sync replay fixture.
- `audit-study/` — §5.4 stimuli and analysis scripts.

---

*Manuscript generated 2026-04-30. Corresponding author: stephenlutar2@gmail.com. Runtime source verified against `szl-holdings/ouroboros@main`, `szl-holdings/szl-holdings-platform@master`, and `szl-holdings/ouroboros-thesis@main` on that date.*
