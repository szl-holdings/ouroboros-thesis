# Reviewer primer — the Ouroboros loop in 90 seconds

You are about to review decisions made by an AI agent runtime called **Ouroboros**. For some of those decisions you will also see a **trace**. This page explains what a trace is so you can read it without confusion.

## The big idea

Most AI agents make a single attempt at a decision. Ouroboros agents instead **loop** — they make an attempt, measure how much that attempt changed from the previous one, and either keep going or stop. The loop is the work. The output is whatever the loop converged on.

## What you'll see in a trace

Every Ouroboros run produces a trace with these fields:

- **Steps.** Each step is one attempt. Steps are numbered 0, 1, 2, ...
- **Δ (delta).** A number between 0 and (some larger value) measuring how much this step changed from the previous step. Smaller delta = more stable. We say the loop **converged** when delta drops below a threshold (default `0.001`).
- **Output.** What this step proposed (a plan, a threat assessment, a sync diff).
- **Duration.** How long the step took, in milliseconds.
- **Exit reason.** Why the loop stopped:
  - `converged` — delta dropped below threshold (good)
  - `consistent` — output stabilized (good)
  - `aborted` — caller forced a stop (mid-run failure)
  - `budgetExhausted` — ran out of allowed steps (the loop didn't stabilize — be skeptical)

## What a "good" trace looks like

```
step 0: δ=0.00, plan=[A]
step 1: δ=0.55, plan=[A, B]
step 2: δ=0.30, plan=[A, B, C]
step 3: δ=0.05, plan=[A, B, C, D]
step 4: δ=0.001, plan=[A, B, C, D]
exit: converged
```

Delta is monotonically decreasing. The loop stabilized cleanly. The final plan is the plan.

## What a "bad" trace looks like

```
step 0: δ=0.00, plan=[X]
step 1: δ=0.40, plan=[X, Y]
step 2: δ=0.45, plan=[X, Z]
step 3: δ=0.42, plan=[X, Y]
step 4: δ=0.44, plan=[X, Z]
... (loop continues until step 8)
exit: budgetExhausted
```

Delta is **oscillating**. The loop did not stabilize. The system was not sure. The final plan should be treated with skepticism.

## What you're looking for

Your job is to decide whether the **final decision** is correct, given the trace and the context. Some scenarios contain deliberate errors. They are not always obvious from the final output alone — the trace may be the only evidence.

Ready when you are.
