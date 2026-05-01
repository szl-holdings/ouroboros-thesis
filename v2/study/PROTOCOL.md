# Trace-Aided Audit Review — Study Protocol

**Study reference:** Ouroboros v2 §5.4 (closes v1 §9.4)
**Principal investigator:** Stephen P. Lutar Jr., SZL Holdings
**Protocol version:** 1.0
**Protocol date:** 2026-04-30

---

## 1. Research question

**Does access to an OuroborosTrace, alongside the final agent decision, change a human reviewer's review time, confidence, and error-detection rate, compared to access to the final decision alone?**

This protocol does not promise an effect. It is the falsifying study v1 §9.4 demanded.

## 2. Hypotheses

We pre-register three hypotheses and one null position.

- **H1 (time):** Reviewers in the **trace arm** will take ≥ 15% longer per stimulus than in the **no-trace arm**, because traces require reading.
- **H2 (confidence):** Reviewers in the trace arm will report higher self-rated confidence (Likert 1–7), with median delta ≥ +1.0.
- **H3 (error detection):** Reviewers in the trace arm will identify ≥ 20% more seeded errors in the seeded-error stimuli set.
- **H0 (null):** No statistically defensible difference exists between arms across any of (time, confidence, error detection).

We will report **effect sizes with 95% bootstrap CIs**, not p-values, because N is small.

## 3. Design

**Crossover, within-subjects.** Each reviewer sees:
- 4 stimuli in the **no-trace arm** (final decision + minimal context)
- 4 stimuli in the **trace arm** (final decision + minimal context + full OuroborosTrace)
- Stimuli order is Latin-square randomized across reviewers.
- Each reviewer's 8 stimuli are drawn from a pool of 16, balanced across:
  - 8 stimuli with seeded errors of a known class
  - 8 stimuli with no seeded errors

This means a reviewer never sees the same stimulus twice but does encounter both arm conditions.

## 4. Participants

- **Target N:** 20–40 reviewers.
- **Recruitment pool:** SZL Holdings network — engineering colleagues, governance/compliance contacts, NYSTEC outreach, and 1–2 academic reviewers. We will explicitly recruit reviewers with at least passing familiarity with one of: AI agent systems, security operations, or data engineering.
- **Inclusion criteria:** Self-reported professional experience with at least one of: agent runtimes, threat modeling, data integration, audit/compliance, software engineering with AI components.
- **Exclusion criteria:** Anyone with prior contributorship to `@szl-holdings/ouroboros` or co-authorship of v1.
- **Compensation:** $50 USD gift card or charity donation per completed session (~30 minutes).

## 5. Stimuli

### 5.1 Pool composition (16 stimuli total)

| Domain | Count | Source |
|---|---|---|
| A11oy plan-replanning workflows | 6 | Anonymized production runs |
| Sentra threat-model iterations | 5 | Anonymized incident traces |
| Amaru entity-sync sessions | 5 | Synthesized from real diff patterns |

### 5.2 Seeded-error classes

Of the 16 stimuli, 8 contain a deliberate, documented error in the final decision. Error classes:

1. **Wrong-route error.** A11oy proof-route should have been `PRF_SECURITY_ACTIONS` but was resolved to `PRF_SYSTEM_CLAIMS`. Visible in trace via mismatched required-artifact list.
2. **Premature convergence.** Loop exited at `converged` but the `safeExitConsistencyScore` was below 0.7 — visible in trace, not in final state.
3. **Risk-tier escalation skipped.** R3 risk should have triggered `await_approval`; trace shows the gate was bypassed via fallthrough.
4. **Stale tool result.** Step 2 used a cached tool result that was invalidated by step 1 — visible in trace step timings, not in final answer.
5. **Hidden non-convergence.** Loop exited at `budgetExhausted` but the final state is presented as authoritative; trace shows oscillating delta signature.
6. **Redaction leak.** A redacted field appears unredacted in the final output — visible by cross-referencing trace's `redactedFields` list against the rendered answer.
7. **Wrong stakes multiplier.** Stakes was set to 4 (declared incident) but the policy fires were R1-only, indicating a misclassification.
8. **Trace-vs-output divergence.** The final output describes a different action than the last trace step's output — a serialization or display bug.

The ground-truth label for each stimulus and the expected error-detection key are stored in `audit-study/answer-key.json` (not shown to reviewers).

### 5.3 Stimulus rendering

Each stimulus is a single-page HTML view:

- **No-trace arm:** Decision summary + minimal context (input request, claimed action, system identifier).
- **Trace arm:** Same content + a collapsible OuroborosTrace viewer (the `<OuroborosTrace>` React component from `src/react/`) showing every step, delta, output, and exit-reason metadata.

Reviewers in both arms receive the same decision summary text, same wall clock context, and same identifying metadata. Only the trace panel differs.

## 6. Procedure

1. **Pre-session (5 min).** Reviewer reads a 1-page primer on the four primitives, the four exit reasons, and how to read a trace. Acknowledges informed consent.
2. **Session (8 stimuli × ~3 min each = ~24 min).** Reviewer answers four questions per stimulus:
   - Q1: Is the final decision correct? (Yes / No / Unsure)
   - Q2: If incorrect, what is the error? (free text, 1–2 sentences)
   - Q3: How confident are you? (1–7 Likert)
   - Q4: What was the most useful piece of evidence in reaching your conclusion? (free text)
3. **Per-stimulus timing.** Captured automatically from page-render to submit-click. Reviewer is told timing is being captured.
4. **Post-session (3 min).** Brief debrief: which arm felt easier, what they wish they'd had access to, any concerns about the trace format.

Total: ~30 minutes per reviewer.

## 7. Measurement

| Outcome | Operationalization |
|---|---|
| **Review time** | Median seconds per stimulus, per arm, per reviewer. Aggregate: mean of medians across reviewers. |
| **Self-confidence** | Median Likert (1–7) per arm per reviewer. Aggregate: median of medians. |
| **Error-detection rate** | Of the 4 seeded-error stimuli per arm per reviewer, fraction correctly identified (Q1 = "No" *and* Q2 free-text matches the answer-key error class within a generous keyword match). Aggregate: mean per arm. |
| **False-positive rate** | Of the 4 no-error stimuli per arm per reviewer, fraction incorrectly flagged. Aggregate: mean per arm. |
| **Free-text quality** | Two-coder thematic coding of Q2 + Q4 free-text. Inter-rater reliability via Cohen's κ. |

## 8. Analysis plan (pre-registered)

- **Primary analysis:** Per-reviewer paired delta (trace arm − no-trace arm) for each of the four numeric outcomes. Report median, IQR, and bootstrap 95% CI on the median.
- **Effect size:** Matched-pairs Cliff's δ for ordinal outcomes (Likert), and standardized mean paired difference for time and detection rate.
- **No frequentist hypothesis tests.** With N ≤ 40 and small expected effects, we report effect sizes with intervals, not significance.
- **Qualitative analysis:** Two coders independently code Q2 and Q4. Disagreements resolved by discussion; report κ.

## 9. Statistical caveats (named explicitly)

- N ≤ 40 means the study is **descriptive, not confirmatory**. We will say so in §5.4 of the paper.
- The reviewer pool is non-random and non-representative of all auditors. External validity is bounded.
- Seeded errors are SZL-authored. There may be authoring bias toward errors a trace would catch.
- Order effects are mitigated by Latin-square randomization but not eliminated.

## 10. Ethics

- **Informed consent.** Reviewers receive the consent form (`consent-form.md`) before starting. Voluntary participation, withdrawal at any time without penalty, no PII collected beyond email for compensation distribution.
- **Anonymization.** Stimuli use scrubbed traces — entity IDs, tenant IDs, and any PII fields are replaced with synthetic surrogates.
- **Data retention.** Raw response data retained for 12 months in encrypted storage, then deleted. Aggregated, anonymized analysis retained indefinitely.
- **No deception.** Reviewers are told upfront that some stimuli contain seeded errors. They are not told which.
- **IRB position.** This is non-clinical, low-risk research conducted by a private entity. Not currently submitted to an IRB. If we extend to a larger N or add academic co-authorship, we will seek IRB review at that time.

## 11. Materials

| File | Purpose |
|---|---|
| `audit-study/PROTOCOL.md` | This document |
| `audit-study/consent-form.md` | Reviewer consent form |
| `audit-study/primer.md` | 1-page primer on Ouroboros primitives |
| `audit-study/stimuli/` | 16 anonymized stimulus HTML files |
| `audit-study/answer-key.json` | Ground-truth error labels (not shown to reviewers) |
| `audit-study/randomization.ts` | Latin-square assignment generator |
| `audit-study/analysis.ipynb` | Bootstrap CI + Cliff's δ analysis notebook |
| `audit-study/recruit-email.md` | Recruiting outreach template |
| `audit-study/session-script.md` | Facilitator script for live sessions |

## 12. Timeline

| Week | Activity |
|---|---|
| Week 1 | Finalize 16 stimuli + answer key. Two-coder dry run on 3 pilot stimuli. |
| Week 2 | Recruit. Target 30 reviewers, accept 20–40. |
| Week 3 | Run sessions (5–10 per day, async via shared link, 1–2 live for facilitator notes). |
| Week 4 | Code free-text. Run analysis notebook. Draft §5.4 of v2 paper. |

## 13. Reporting commitments

We will report:
- The full N enrolled, the N completed, and reasons for any drop-outs.
- All four numeric outcomes per arm with effect sizes and CIs.
- Per-error-class detection rates, even where individual cells have small N.
- A null result if H0 is supported. We do not pre-commit to a positive finding.

We will publish:
- The protocol (this file) in the paper appendix.
- The answer-key after publication so the stimuli can be reused with caution.
- Aggregated, anonymized response data as a CSV in the supplementary materials.

We will NOT publish:
- Individual reviewer responses or identifying information.
- Production traces beyond what is in the anonymized stimuli set.

---

*Protocol authored 2026-04-30 for Ouroboros v2 §5.4. Revisions tracked in `audit-study/CHANGELOG.md`.*
