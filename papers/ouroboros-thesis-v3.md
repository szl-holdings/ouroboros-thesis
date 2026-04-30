---
title: "The Ouroboros Thesis: Looped Computation as an Auditable Governance Surface for AI Systems"
author:
  - name: "Stephen P. Lutar Jr."
    affiliation: "Independent Researcher; SZL Consulting Ltd"
    email: "stephenlutar2@gmail.com"
date: "April 2026"
abstract: |
  Recent work on looped and recurrent language models — Universal Transformers, PonderNet, and end-to-end looped LM recipes — suggests that recursive computation can improve reasoning efficiency without relying solely on increased parameter counts or training data. Most of that work treats the loop as a *model-internal* device. This paper takes a different position: the loop should be lifted out of the model and treated as a **system primitive** for AI runtimes, with explicit state deltas, hash-chained traces, decision receipts, adaptive depth allocation, and replay-grade audit. Reframed this way, looped computation is not just a compute pattern — it is a **governance surface** that aligns naturally with EU AI Act Article 12 record-keeping obligations and NIST AI RMF MEASURE/MANAGE controls. We define three sub-primitives — `LoopKernel`, `EntropyDepthAllocator`, `CrossStepConsistency` — and three engineering contracts — typed traces, append-only proof ledgers, and validator-gated commits. We map the primitive to three deployed runtimes (A11oy agent orchestration, Sentra recursive threat modeling, Terra distressed-asset analytics) and ship a reference implementation (`@workspace/codex-kernel`) with a continuously-verified Dresden Codex Venus replay fixture. This is a position-and-systems-design preprint with a working reference implementation; capability-gain experiments are deferred to future work and clearly scoped as such.
keywords: ["looped computation", "AI governance", "EU AI Act", "NIST AI RMF", "auditable AI", "agent runtimes", "PonderNet", "Universal Transformers"]
---

# 1. Introduction

Scaling AI systems by model width and dataset size has produced large gains, but recent evidence points to diminishing returns: high-quality data is finite [@villalobos2022], retrieval and reinforcement-learning improvements do not always translate into durable capability jumps, and inference-time compute is increasingly the lever that determines reasoning quality [@snell2024scaling]. Looped computation offers a different axis: re-applying a shared kernel over an evolving state until convergence or a bounded stop condition is reached.

Most existing work on loops sits inside the model: Universal Transformers [@dehghani2018ut] introduce recurrence over depth; PonderNet [@banino2021pondernet] formalizes adaptive computation time with probabilistic halting; ACT [@graves2016act] preceded both with a learned halting signal. Recent end-to-end looped language model training recipes show that this recurrence can be trained directly. These results are valuable, but they share an assumption: the loop is a property of the model artifact.

This paper's claim is that the loop should also exist *outside* the model, as a runtime primitive owned by the agent system itself. When it is, three things become possible that are not possible inside the model:

1. **Auditability.** Every iteration emits a typed trace event and a decision receipt; every commit appends to a hash-chained proof ledger. Regulators, auditors, and operators can replay any decision deterministically.
2. **Composition.** The same kernel runs across heterogeneous workloads — agent orchestration, threat modeling, asset valuation — because the contract is on traces and validators, not on model weights.
3. **Governance.** Validators (drift bounds, evidence provenance, human gates) are first-class hard-stops, not soft constraints buried in prompts. The kernel cannot complete a non-trivial step without satisfying them.

The contribution of this paper is therefore an architectural one. We do not claim new capability gains over Universal Transformers or PonderNet; we claim that lifting their core idea — bounded recursion with adaptive depth — into the runtime layer creates a governance surface that one-pass pipelines and prompt-only chain-of-thought scaffolding do not.

# 2. Prior work

## 2.1 Universal Transformers
Universal Transformers [@dehghani2018ut] introduce recurrence over depth, enabling a single set of parameters to be applied repeatedly across steps. Under suitable conditions this yields models with increased computational expressivity at parameter parity.

## 2.2 Adaptive Computation Time and PonderNet
ACT [@graves2016act] introduced a learned halting signal that allocates depth per input. PonderNet [@banino2021pondernet] formalizes adaptive computation time with probabilistic halting, optimizing an ELBO that trades off additional computation against accuracy.

## 2.3 End-to-End Looped LM Recipes
Recent work demonstrates end-to-end training recipes for looped language models that can match larger non-looped baselines on reasoning tasks by leveraging iterative refinement at inference. We treat these as model-internal precedents for the runtime-level primitive proposed here.

## 2.4 Agentic loops in deployed systems
Production agent frameworks (ReAct, AutoGPT-style scaffolds, plan-and-execute architectures) implement loops, but as ad-hoc orchestration code. They typically lack: typed step traces, hash-chained state, validator hard-stops, and replay verifiers. The thesis of this paper is that those properties should be the *minimum bar* for any agentic loop, not optional add-ons.

## 2.5 Governance frameworks
The EU AI Act, Regulation (EU) 2024/1689, requires in **Article 12** that "high-risk AI systems shall technically allow for the automatic recording of events ('logs') over the lifetime of the system" [@euaiact2024]. The NIST AI Risk Management Framework 1.0 [@nistairmf2023] specifies MEASURE and MANAGE functions covering traceable decisions, evidence trails, and severity-bound governance. We map our primitive to both frameworks in §6.

# 3. The Ouroboros Loop as a system primitive

We propose a runtime component, the *Ouroboros Loop*, defined by three sub-primitives.

## 3.1 LoopKernel

A deterministic or stochastic transition function:

$$S_{k+1} = f(S_k; \theta, y_k)$$

where $S_k$ is the loop state at step $k$, $\theta$ is the policy version, and $y_k$ is an optional intermediate product. The kernel commits each transition by computing:

$$h_{k+1} = H(h_k \,\|\, \Delta_{k} \,\|\, S_{k+1})$$

where $\Delta_k$ is the proposed delta, $H$ is a chain hash, and $\|$ denotes serialization concatenation. The hash chain is the audit substrate.

## 3.2 EntropyDepthAllocator

A controller that allocates step budget based on two signals:

**Delta convergence.** Define the normalized state-change witness as:

$$d_k = \frac{1}{L}\,\mathrm{Hamming}\!\big(h_{k-1},\, h_k\big)$$

over the $L$-character hex representation of the chain hash. When $d_k \le \varepsilon_\Delta$ for $W_\Delta$ consecutive steps, the loop early-exits with reason `converged`.

**Validator entropy.** For the per-step validator severity distribution over $\{\text{pass}, \text{soft\_fail}, \text{hard\_fail}\}$, define:

$$H_k = -\sum_{s} p_s \log_2 p_s$$

where $p_s$ is the fraction of validators returning severity $s$ at step $k$. When $H_k \le \varepsilon_H$ and the step is fully clean (no soft fails) for $W_H$ consecutive steps, the loop early-exits with reason `entropy_settled`.

**Budget extension.** When the rolling soft-fail rate exceeds threshold $\rho$ and the step counter approaches the configured ceiling, the controller may extend the ceiling up to a hard maximum, emitting a `budget_extension` verdict that is recorded on the trace.

The allocator is a pure function of inputs: no clocks, no PRNG, no I/O. Replay reproduces every verdict bit-for-bit. Reference implementation: `packages/codex-kernel/src/depth-allocator.ts`.

## 3.3 CrossStepConsistency

A test gating early exit on agreement between intermediate outputs and the (current best) final output, or between consecutive outputs. In the reference implementation this manifests as the canonical-equality check `canonicalize(S_{k+1}) === canonicalize(S_k)`, which produces the explicit stop reason `no_state_change_needed`. Validators (`stateTransitionRule`, `driftBounds`, `evidenceProvenance`, `humanGate`) extend this with severity-bound checks.

# 4. Engineering contracts

A system primitive is only credible if it ships with the contracts that make it auditable. We identify five.

1. **Typed step traces.** Each step emits a `TraceEvent` with `pipeline_stage`, `observation`, `proposed_delta`, `validator_results[]`, `decision_receipt`, `state_prev_hash`, `state_next_hash`, and `stop_reason`.
2. **Append-only proof ledger.** A JSONL stream of `{ts, step, state_hash, delta_hash, receipt_id, policy_version, approval_ref}` entries. Single-writer, deterministic, replay-verifiable.
3. **Validator hard-stops.** A non-trivial step cannot commit without passing `state_transition_rule`, `evidence_provenance`, and (when configured) `drift_bounds` and `human_gate`. Hard fails halt the loop with a recorded reason.
4. **Replay verifier.** Given an initial state and a trace, a verifier reconstructs the chain and asserts every transition. This is the third-party-runnable proof surface.
5. **Determinism guarantees.** Two independent runs with identical `(initial_state, steps, policy_version)` produce identical final state hashes. The CI workflow `codex-kernel-verify` enforces this on every commit to the reference implementation [@szlcodexkernel2026].

# 5. System mapping — three runtimes

The primitive is meaningful only if it is reused. We describe three production runtimes in the SZL Holdings monorepo that consume `@workspace/codex-kernel` directly.

## 5.1 A11oy — agent orchestration with cognitive refinement

A11oy is the agent runtime that drives perceive → orient → plan → execute → verify → reflect → update_self_model → update_memory cycles (`packages/cognitive-runtime`). The verify→reflect→update sub-loop, which is responsible for revising plans and outputs after a verifier score, is wrapped in `runLoop()` with adaptive depth enabled. Each refinement step proposes a delta to the draft output and emits a decision receipt of type `cognitive_refinement` citing the verifier evidence. The kernel halts on convergence (`d_k \le \varepsilon_\Delta`) or on validator hard-fails (e.g., `humanGate` triggered by an approval-required policy). The result: every refinement decision in A11oy is replay-verifiable, and the depth of refinement is adapted to the difficulty of the input rather than fixed at run time.

Concrete artifacts: `packages/cognitive-runtime/src/phases/refine.ts`, `packages/codex-kernel`, `packages/trace-graph` for the wider trace substrate.

## 5.2 Sentra — recursive threat modeling and replay attestation

Sentra is the security and replay-attestation surface (`artifacts/sentra`). It uses the kernel for two roles. First, threat modeling sessions iterate over a threat-graph state — each step proposes a hypothesis delta (new attacker capability, new vulnerable asset, new mitigation), runs `driftBounds` against a configured value-at-risk ceiling, and commits with a receipt citing the upstream signals consumed. Second, Sentra exposes a public `/replay-attestation` page where any third party can paste a `trace.jsonl` and `initial_state.json` and receive a step-by-step verdict from `replay()`. Tamper detection is demonstrated by a one-click bundle: a single byte changed in any trace event produces a `chain_hash_mismatch` failure with the offending step number.

Concrete artifacts: `artifacts/sentra/src/lib/codex-replay.ts`, `artifacts/api-server/src/routes/sentra-replay.ts`.

## 5.3 Terra — distressed-asset analytics with auditable encumbrance loops

Terra is the real-estate intelligence runtime (`artifacts/terra`). Distressed-asset scoring requires iterative refinement: each pass over a parcel re-estimates encumbrance (liens, secondary mortgages, mechanic claims) using newly-fetched evidence. Wrapping `terra-distress-encumbrance-estimator.ts` in `runLoop()` makes every iteration auditable: each step's `decision_receipt` cites the source records consumed (CSV ingestion paths, county recorder pulls), and `drift_bounds` enforces the configured value-at-risk ceiling. The adaptive-depth allocator stops the loop once the estimate stabilizes (delta convergence) or escalates with a `human_gate` hard-stop when uncertainty stays high.

Concrete artifacts: `artifacts/api-server/src/lib/terra-distress-loop.ts`.

# 6. Standards alignment

The primitive is aligned with two reference frameworks in detail; the full mapping lives at `docs/codex-kernel-standards-map.md` in the reference implementation.

**EU AI Act, Article 12 (record-keeping).** Automatic logging over the lifetime of the system is satisfied by `runLoop()` emitting one `TraceEvent` per step unconditionally. Tamper-evidence sufficient to support audit is satisfied by the chain hash. Period of use, evidence references, and the natural persons involved in verification are captured in the `DecisionReceipt` (`timestamp`, `evidence[]`, `approval_ref`, `ApprovalEvent.approved_by`).

**NIST AI RMF 1.0 (MEASURE and MANAGE).** Per-step `ValidatorResult[]` with severity satisfies MEASURE 2.5 and MEASURE 3.1; the `governance_enabled = false` A/B mode (which demotes the `evidence_provenance` and `human_gate` validators from hard- to soft-fail) satisfies MEASURE 3.2 by letting operators compare governance postures without disabling instrumentation. The append-only proof ledger satisfies MANAGE 4.1; explicit `StopReason` values satisfy MANAGE 2.3.

What the kernel does **not** address: log retention, log access control, log deletion procedures, distributed consensus, cryptographic non-repudiation against motivated adversaries (the 128-bit FNV-1a chain hash is a replay primitive, not a signature), and data-subject erasure rights under GDPR. These are deployment-time concerns that wrap the kernel.

# 7. Limitations and future work

This paper is a position-and-systems-design preprint. It is **not** an empirical capability-gains paper. The reference implementation is deterministic and standards-aligned, but:

1. We do not benchmark adaptive depth against fixed depth on reasoning tasks. Doing so requires a held-out benchmark suite and is left as future work.
2. We do not characterize convergence properties of the entropy-allocator on adversarial inputs. The current rule is a sufficient signal for production governance; it is not a theoretical guarantee.
3. The reference hash is FNV-1a, sufficient for replay determinism but not for tamper-resistance against motivated adversaries; production deployments requiring the latter should wrap with SHA-256 or Ed25519 signatures.
4. Distillation of loop traces into smaller models (Section 6.6 of the v2 manuscript) is removed from the body of this paper and re-scoped as future work, because no distillation experiments have been run.

The empirical research agenda we propose, in order: (i) implement adaptive-depth ablations on a public reasoning benchmark; (ii) characterize the relationship between validator-entropy decay and downstream answer quality; (iii) study trace-distillation as a transfer mechanism between runtimes; (iv) extend the chain-hash to Ed25519-signed receipts for non-repudiation.

# 8. Conclusion

Treating bounded recursive computation as a runtime primitive — with typed traces, hash-chained state, validator hard-stops, adaptive depth, and replay verification — turns inference-time scaling into something operators and auditors can trust. The contribution of this paper is not novelty in compute pattern; it is a claim about the right *architectural layer* for the loop to live at, together with a reference implementation that proves the architecture compiles, runs deterministically, and aligns by construction with EU AI Act Article 12 and NIST AI RMF 1.0.

# References

Dehghani, M., Gouws, S., Vinyals, O., Uszkoreit, J., & Kaiser, Ł. (2018). *Universal Transformers*. arXiv:1807.03819. https://arxiv.org/abs/1807.03819

Banino, A., Balaguer, J., & Blundell, C. (2021). *PonderNet: Learning to Ponder*. arXiv:2107.05407. https://arxiv.org/abs/2107.05407

Graves, A. (2016). *Adaptive Computation Time for Recurrent Neural Networks*. arXiv:1603.08983. https://arxiv.org/abs/1603.08983

Snell, C., Lee, J., Xu, K., & Kumar, A. (2024). *Scaling LLM Test-Time Compute Optimally Can Be More Effective Than Scaling Model Parameters*. arXiv:2408.03314. https://arxiv.org/abs/2408.03314

Villalobos, P., Sevilla, J., Heim, L., Besiroglu, T., Hobbhahn, M., & Ho, A. (2022). *Will We Run Out of Data? An Analysis of the Limits of Scaling Datasets in Machine Learning*. arXiv:2211.04325. https://arxiv.org/abs/2211.04325

European Parliament and Council. (2024). *Regulation (EU) 2024/1689 of the European Parliament and of the Council laying down harmonised rules on artificial intelligence (Artificial Intelligence Act)*. Official Journal of the European Union. https://eur-lex.europa.eu/eli/reg/2024/1689/oj

National Institute of Standards and Technology. (2023). *AI Risk Management Framework 1.0* (NIST AI 100-1). https://doi.org/10.6028/NIST.AI.100-1

Lutar, S. P. (2026). *@workspace/codex-kernel — replay-grade governed-loop primitive*. SZL Holdings Platform. https://github.com/stephenlutar2-hash/szl-holdings-platform/tree/main/packages/codex-kernel

# Appendix A — Reference implementation pointer

```
packages/codex-kernel/
├── src/
│   ├── kernel.ts             # runLoop()
│   ├── types.ts              # KernelConfig, TraceEvent, RunSummary, StepProposal
│   ├── depth-allocator.ts    # EntropyDepthAllocator (§3.2)
│   ├── validators.ts         # state_transition_rule, drift_bounds, evidence_provenance, human_gate
│   ├── ledger.ts             # ProofLedger (append-only)
│   ├── replay.ts             # replay verifier
│   ├── hash.ts               # chainHash, canonicalize
│   ├── receipts.ts           # DecisionReceipt finalization
│   └── dresden-venus.ts      # canonical regression fixture
├── runner/payload.json       # CLI payload (executable spec)
└── README.md                 # CI badge: codex-kernel-verify
```

Reproduce the canonical Dresden Venus run:

```bash
pnpm --filter @workspace/codex-kernel codex:run
pnpm --filter @workspace/codex-kernel codex:replay
# expected: verdict: ATTESTED
```
