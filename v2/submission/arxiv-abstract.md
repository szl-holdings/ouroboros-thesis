# arXiv-ready abstract (≤250 words)

**Title:** The Loop Is the Product: Measuring Bounded Recursion as a System Primitive for Auditable AI

**Subtitle:** An Empirical Companion to the Ouroboros Thesis

**Primary category:** cs.SE
**Secondary categories:** cs.AI

---

The Ouroboros Thesis (Lutar, 2026) argued that bounded loops with measurable convergence should be elevated from implementation detail to a first-class runtime primitive for AI systems. That paper was a position and systems-design preprint and made no empirical claims. This is the empirical companion.

We report (a) a shipped reference implementation of the four v1 primitives as a TypeScript runtime, `@szl-holdings/ouroboros` (142/142 tests passing, deterministic replay, opt-in adaptive depth with bit-identical invariant); (b) three production case studies on the same kernel — A11oy (agent orchestration), Sentra (recursive threat modeling), Amaru (convergent data synchronization) — with shared trace persistence via `aef-evidence-ledger`; (c) closure of the five-item experimental agenda in v1 §9, including a new loop-budget Pareto frontier and a pre-registered, small-N crossover study on whether convergence traces change human audit behavior; and (d) a direct mapping of the runtime to NIST AI RMF MEASURE/MANAGE and EU AI Act Article 12 record-keeping.

The paper tightens rather than widens v1. Cross-system distillation is deliberately held as a hypothesis. A falsification ledger names the observations that would refute each load-bearing claim, including a commitment to publish a null result for the audit-study arm.

The narrow claim we defend: when convergence is measurable, the trace is not a log but a deliverable.

*(248 words)*
