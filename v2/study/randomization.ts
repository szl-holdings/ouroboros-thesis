/**
 * Latin-square randomization for the §5.4 trace-audit study.
 *
 * Generates a per-reviewer assignment of:
 *   - 8 stimuli drawn from the 16-stimulus pool, balanced 4 seeded-error / 4 clean
 *   - Arm assignment (no-trace / trace) per stimulus, with order counter-balanced
 *
 * Determinism: with the same seed, this script produces identical assignments.
 *
 * License: MIT.
 */

import { writeFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { parseArgs } from 'node:util';
import { createHash } from 'node:crypto';

interface Stimulus {
  id: string;
  domain: 'a11oy' | 'sentra' | 'amaru';
  hasSeededError: boolean;
}

const POOL: Stimulus[] = [
  // 8 with seeded errors
  { id: 'a11oy_e1', domain: 'a11oy', hasSeededError: true },
  { id: 'a11oy_e2', domain: 'a11oy', hasSeededError: true },
  { id: 'sentra_e1', domain: 'sentra', hasSeededError: true },
  { id: 'sentra_e2', domain: 'sentra', hasSeededError: true },
  { id: 'amaru_e1', domain: 'amaru', hasSeededError: true },
  { id: 'amaru_e2', domain: 'amaru', hasSeededError: true },
  { id: 'a11oy_e3', domain: 'a11oy', hasSeededError: true },
  { id: 'sentra_e3', domain: 'sentra', hasSeededError: true },
  // 8 clean
  { id: 'a11oy_c1', domain: 'a11oy', hasSeededError: false },
  { id: 'a11oy_c2', domain: 'a11oy', hasSeededError: false },
  { id: 'a11oy_c3', domain: 'a11oy', hasSeededError: false },
  { id: 'sentra_c1', domain: 'sentra', hasSeededError: false },
  { id: 'sentra_c2', domain: 'sentra', hasSeededError: false },
  { id: 'amaru_c1', domain: 'amaru', hasSeededError: false },
  { id: 'amaru_c2', domain: 'amaru', hasSeededError: false },
  { id: 'amaru_c3', domain: 'amaru', hasSeededError: false },
];

interface Assignment {
  reviewerId: string;
  sessionSeed: string;
  stimuli: Array<{ stimulusId: string; position: number; arm: 'no-trace' | 'trace'; hasSeededError: boolean }>;
}

// Deterministic PRNG so the protocol is replicable.
function mulberry32(a: number) {
  return function () {
    let t = (a += 0x6d2b79f5);
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function shuffleInPlace<T>(arr: T[], rand: () => number): T[] {
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(rand() * (i + 1));
    [arr[i], arr[j]] = [arr[j]!, arr[i]!];
  }
  return arr;
}

function seedFromString(s: string): number {
  const h = createHash('sha256').update(s).digest();
  return h.readUInt32BE(0);
}

export function generateAssignment(reviewerId: string, masterSeed: string): Assignment {
  const seedString = `${masterSeed}::${reviewerId}`;
  const seed = seedFromString(seedString);
  const rand = mulberry32(seed);

  // Stratified draw: 4 errored + 4 clean
  const errored = shuffleInPlace([...POOL.filter((s) => s.hasSeededError)], rand).slice(0, 4);
  const clean = shuffleInPlace([...POOL.filter((s) => !s.hasSeededError)], rand).slice(0, 4);

  // Combine and shuffle position order
  const stimuli = shuffleInPlace([...errored, ...clean], rand);

  // Arm assignment: alternating, but starting arm is randomized per reviewer.
  const startWithTrace = rand() < 0.5;
  const armed = stimuli.map((s, i) => {
    const arm: 'no-trace' | 'trace' = (i % 2 === 0) === startWithTrace ? 'trace' : 'no-trace';
    return { stimulusId: s.id, position: i + 1, arm, hasSeededError: s.hasSeededError };
  });

  // Sanity: each arm should see 2 errored + 2 clean (not strictly guaranteed by
  // alternation; if violated, reshuffle starting-arm. Cheap retry.)
  const ensureBalanced = () => {
    const traceArm = armed.filter((a) => a.arm === 'trace');
    const traceErr = traceArm.filter((a) => a.hasSeededError).length;
    return traceErr === 2;
  };

  if (!ensureBalanced()) {
    // Swap one mismatched pair to restore balance (deterministic given seed).
    const traceArm = armed.filter((a) => a.arm === 'trace');
    const noTraceArm = armed.filter((a) => a.arm === 'no-trace');
    const traceErr = traceArm.filter((a) => a.hasSeededError).length;
    if (traceErr > 2) {
      // Move one errored from trace to no-trace
      const fromIdx = armed.findIndex((a) => a.arm === 'trace' && a.hasSeededError);
      const toIdx = armed.findIndex((a) => a.arm === 'no-trace' && !a.hasSeededError);
      armed[fromIdx]!.arm = 'no-trace';
      armed[toIdx]!.arm = 'trace';
    } else if (traceErr < 2) {
      const fromIdx = armed.findIndex((a) => a.arm === 'no-trace' && a.hasSeededError);
      const toIdx = armed.findIndex((a) => a.arm === 'trace' && !a.hasSeededError);
      armed[fromIdx]!.arm = 'trace';
      armed[toIdx]!.arm = 'no-trace';
    }
  }

  return {
    reviewerId,
    sessionSeed: seedString,
    stimuli: armed,
  };
}

// CLI
async function main() {
  const { values } = parseArgs({
    options: {
      n: { type: 'string', short: 'n', default: '30' },
      seed: { type: 'string', short: 's', default: 'ouroboros-v2-2026-04-30' },
      output: { type: 'string', short: 'o', default: './assignments.json' },
    },
  });

  const N = parseInt(values.n!, 10);
  const masterSeed = values.seed!;

  const assignments: Assignment[] = [];
  for (let i = 1; i <= N; i++) {
    const reviewerId = `R${String(i).padStart(3, '0')}`;
    assignments.push(generateAssignment(reviewerId, masterSeed));
  }

  writeFileSync(resolve(values.output!), JSON.stringify({ masterSeed, n: N, assignments }, null, 2));
  console.log(`Generated ${N} assignments → ${values.output}`);

  // Sanity report
  const allArmed = assignments.flatMap((a) => a.stimuli);
  const traceCount = allArmed.filter((s) => s.arm === 'trace').length;
  const traceErrors = allArmed.filter((s) => s.arm === 'trace' && s.hasSeededError).length;
  const noTraceErrors = allArmed.filter((s) => s.arm === 'no-trace' && s.hasSeededError).length;
  console.log(`Trace arm:    ${traceCount} stimuli, ${traceErrors} with errors`);
  console.log(`No-trace arm: ${allArmed.length - traceCount} stimuli, ${noTraceErrors} with errors`);
}

if (import.meta.url === `file://${process.argv[1]}`) {
  main().catch((err) => {
    console.error(err);
    process.exit(1);
  });
}
