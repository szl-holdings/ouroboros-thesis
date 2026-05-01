/**
 * Load a workload corpus from either:
 *   1. an aef-evidence-ledger instance (production replay), or
 *   2. a JSON fixture file under `workloads/` (replication / CI).
 *
 * Workloads expose:
 *   - instances:     concrete (initialState, step, delta, [consistency]) tuples
 *   - scoreOutcome:  (trace, groundTruth) -> [0, 1] quality score
 *   - probeDeltas:   optional pre-computed first-3 deltas for adaptive runs
 *   - stakes:        optional stakes multiplier per instance
 *
 * License: MIT.
 */

import { readFileSync, existsSync } from 'node:fs';
import { resolve } from 'node:path';
import { createHash } from 'node:crypto';
import type { LoopTrace, StepFn, DeltaFn, ConsistencyFn } from '@szl-holdings/ouroboros/types';

export interface WorkloadInstance<S = unknown, O = unknown> {
  id: string;
  initialState: S;
  step: StepFn<S, O>;
  delta: DeltaFn<S>;
  consistency?: ConsistencyFn<O>;
  groundTruth?: unknown;
  probeDeltas?: number[];
  stakes?: number;
}

export interface WorkloadSpec<S = unknown, O = unknown> {
  name: string;
  description: string;
  runtimeVersion: string;
  fixtureSha256: string;
  instances: WorkloadInstance<S, O>[];
  scoreOutcome: (trace: LoopTrace<S, O>, groundTruth?: unknown) => number;
}

export async function loadWorkload(
  name: string,
  opts: { ledgerUri?: string; fixturePath?: string } = {},
): Promise<WorkloadSpec> {
  // Prefer ledger if env var set, otherwise fall back to fixture.
  const ledgerUri = opts.ledgerUri ?? process.env.OUROBOROS_LEDGER_URI;

  if (ledgerUri) {
    return loadFromLedger(name, ledgerUri);
  }

  const fixturePath =
    opts.fixturePath ?? resolve(__dirname, `../workloads/${name}.fixture.json`);
  if (!existsSync(fixturePath)) {
    throw new Error(`Workload fixture not found: ${fixturePath}`);
  }

  return loadFromFixture(name, fixturePath);
}

async function loadFromLedger(name: string, _uri: string): Promise<WorkloadSpec> {
  // Implementation pending — will use @workspace/aef-evidence-ledger query API
  // to pull anonymized traces matching workload tag, reconstruct (state, step,
  // delta) closures from persisted intermediate states + recorded outputs.
  //
  // For replication, fixtures under `workloads/` are sufficient.
  throw new Error(
    `Ledger replay not implemented in OSS harness — use fixture under workloads/${name}.fixture.json`,
  );
}

interface FixtureFile {
  name: string;
  description: string;
  runtimeVersion: string;
  scorer: 'plan-edit-distance' | 'risk-tag-jaccard' | 'sync-diff-magnitude';
  instances: Array<{
    id: string;
    initialState: unknown;
    transitions: Array<{ output: unknown; nextState: unknown }>;
    groundTruth?: unknown;
    probeDeltas?: number[];
    stakes?: number;
  }>;
}

function loadFromFixture(name: string, path: string): WorkloadSpec {
  const raw = readFileSync(path, 'utf-8');
  const sha256 = createHash('sha256').update(raw).digest('hex');
  const file = JSON.parse(raw) as FixtureFile;

  const instances: WorkloadInstance[] = file.instances.map((inst) => {
    let cursor = 0;
    return {
      id: inst.id,
      initialState: inst.initialState,
      step: async (_state: unknown, i: number) => {
        const transition = inst.transitions[Math.min(i, inst.transitions.length - 1)];
        cursor = i;
        return { state: transition.nextState, output: transition.output };
      },
      delta: deltaFor(file.scorer),
      consistency: consistencyFor(file.scorer),
      groundTruth: inst.groundTruth,
      probeDeltas: inst.probeDeltas,
      stakes: inst.stakes,
    };
  });

  return {
    name: file.name ?? name,
    description: file.description,
    runtimeVersion: file.runtimeVersion,
    fixtureSha256: sha256,
    instances,
    scoreOutcome: scorerFor(file.scorer),
  };
}

function deltaFor(scorer: FixtureFile['scorer']): DeltaFn<unknown> {
  switch (scorer) {
    case 'plan-edit-distance':
      return (a, b) => {
        const sa = JSON.stringify(a);
        const sb = JSON.stringify(b);
        // Cheap normalized symbol-level diff; replace with proper AST distance in production.
        const max = Math.max(sa.length, sb.length, 1);
        let d = 0;
        for (let i = 0; i < Math.min(sa.length, sb.length); i++) if (sa[i] !== sb[i]) d++;
        d += Math.abs(sa.length - sb.length);
        return d / max;
      };
    case 'risk-tag-jaccard':
      return (a, b) => {
        const A = new Set((a as { tags?: string[] }).tags ?? []);
        const B = new Set((b as { tags?: string[] }).tags ?? []);
        const inter = [...A].filter((x) => B.has(x)).length;
        const union = new Set([...A, ...B]).size || 1;
        return 1 - inter / union;
      };
    case 'sync-diff-magnitude':
      return (a, b) => {
        const da = (a as { diff?: number }).diff ?? 0;
        const db = (b as { diff?: number }).diff ?? 0;
        return Math.abs(da - db) / Math.max(Math.abs(da), Math.abs(db), 1);
      };
  }
}

function consistencyFor(_scorer: FixtureFile['scorer']): ConsistencyFn<unknown> | undefined {
  return undefined;
}

function scorerFor(
  scorer: FixtureFile['scorer'],
): (trace: LoopTrace<unknown, unknown>, groundTruth?: unknown) => number {
  switch (scorer) {
    case 'plan-edit-distance':
      // Quality = 1 if final plan equals ground-truth plan (token-equality), else
      // graded by Levenshtein normalized.
      return (trace, gt) => {
        if (gt === undefined) return trace.exitReason === 'converged' ? 1 : 0.5;
        const last = trace.steps[trace.steps.length - 1];
        const a = JSON.stringify(last?.output ?? last?.state);
        const b = JSON.stringify(gt);
        const max = Math.max(a.length, b.length, 1);
        let edits = 0;
        for (let i = 0; i < Math.min(a.length, b.length); i++) if (a[i] !== b[i]) edits++;
        edits += Math.abs(a.length - b.length);
        return 1 - edits / max;
      };
    case 'risk-tag-jaccard':
      return (trace, gt) => {
        if (!gt) return trace.exitReason === 'converged' ? 1 : 0.5;
        const last = trace.steps[trace.steps.length - 1]?.state as { tags?: string[] };
        const A = new Set(last?.tags ?? []);
        const B = new Set((gt as { tags?: string[] }).tags ?? []);
        const inter = [...A].filter((x) => B.has(x)).length;
        const union = new Set([...A, ...B]).size || 1;
        return inter / union;
      };
    case 'sync-diff-magnitude':
      return (trace) => {
        const last = trace.steps[trace.steps.length - 1];
        const d = (last?.state as { diff?: number })?.diff ?? 1;
        return 1 / (1 + Math.abs(d)); // diff → 0 maps to quality → 1
      };
  }
}
