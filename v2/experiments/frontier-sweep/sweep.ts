/**
 * frontier-sweep/sweep.ts
 *
 * v2 §5.5 — Loop-budget Pareto frontier.
 *
 * Replays a corpus of production traces against a grid of (maxSteps,
 * convergenceThreshold) configurations and reports the quality-vs-compute
 * Pareto frontier per workload.
 *
 * Quality is workload-defined and supplied by `WorkloadSpec.scoreOutcome`.
 * Compute is the average step count across the corpus.
 *
 * Determinism: the sweep is pure — given the same fixture + grid + seeds,
 * outputs are bit-identical.
 *
 * License: MIT (harness only).
 */

import { runLoop } from '@szl-holdings/ouroboros/loop-kernel';
import { allocateDepth } from '@szl-holdings/ouroboros/depth-allocator';
import { writeFileSync, mkdirSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { createHash } from 'node:crypto';
import { parseArgs } from 'node:util';

import { loadWorkload, type WorkloadSpec, type WorkloadInstance } from '../shared/trace-loader';
import { computePareto, type ParetoPoint } from './analysis/pareto';

interface SweepConfig {
  maxStepsGrid: number[];
  convergenceGrid: number[];
  adaptiveDepthFlag: boolean;
}

const DEFAULT_GRID: SweepConfig = {
  maxStepsGrid: [2, 3, 4, 5, 6, 8, 12],
  convergenceGrid: [1e-1, 1e-2, 1e-3, 1e-4],
  adaptiveDepthFlag: false,
};

interface SweepResult {
  workload: string;
  fixtureSha256: string;
  runtimeVersion: string;
  config: SweepConfig;
  cells: Array<{
    maxSteps: number;
    convergenceThreshold: number;
    adaptiveDepth: boolean;
    avgSteps: number;
    avgQuality: number;
    convergedRate: number;
    budgetExhaustedRate: number;
    abortedRate: number;
    consistentRate: number;
    nInstances: number;
  }>;
  pareto: ParetoPoint[];
}

async function runSweep(workload: WorkloadSpec, cfg: SweepConfig): Promise<SweepResult> {
  const cells: SweepResult['cells'] = [];

  for (const maxSteps of cfg.maxStepsGrid) {
    for (const convergenceThreshold of cfg.convergenceGrid) {
      for (const adaptiveDepth of [false, ...(cfg.adaptiveDepthFlag ? [true] : [])]) {
        const cell = await runCell(workload, maxSteps, convergenceThreshold, adaptiveDepth);
        cells.push({
          maxSteps,
          convergenceThreshold,
          adaptiveDepth,
          ...cell,
        });
      }
    }
  }

  const pareto = computePareto(cells, /* x = */ 'avgSteps', /* y = */ 'avgQuality');

  return {
    workload: workload.name,
    fixtureSha256: workload.fixtureSha256,
    runtimeVersion: workload.runtimeVersion,
    config: cfg,
    cells,
    pareto,
  };
}

async function runCell(
  workload: WorkloadSpec,
  maxSteps: number,
  convergenceThreshold: number,
  adaptiveDepth: boolean,
): Promise<Omit<SweepResult['cells'][number], 'maxSteps' | 'convergenceThreshold' | 'adaptiveDepth'>> {
  const exitCounts = { converged: 0, consistent: 0, aborted: 0, budgetExhausted: 0 };
  let totalSteps = 0;
  let totalQuality = 0;
  let n = 0;

  for (const instance of workload.instances) {
    const config = adaptiveDepth
      ? deriveAdaptiveConfig(instance, maxSteps, convergenceThreshold)
      : { maxSteps, convergenceThreshold };

    const trace = await runLoop({
      initialState: instance.initialState,
      step: instance.step,
      delta: instance.delta,
      consistency: instance.consistency,
      config,
    });

    exitCounts[trace.exitReason]++;
    totalSteps += trace.steps.length;
    totalQuality += workload.scoreOutcome(trace, instance.groundTruth);
    n++;
  }

  return {
    avgSteps: totalSteps / n,
    avgQuality: totalQuality / n,
    convergedRate: exitCounts.converged / n,
    budgetExhaustedRate: exitCounts.budgetExhausted / n,
    abortedRate: exitCounts.aborted / n,
    consistentRate: exitCounts.consistent / n,
    nInstances: n,
  };
}

function deriveAdaptiveConfig(
  instance: WorkloadInstance,
  hardCap: number,
  convergenceThreshold: number,
) {
  // Use first 3 deltas if available as probe
  const probe = instance.probeDeltas ?? [];
  const allocation = allocateDepth({
    recentDeltas: probe.slice(-3).reverse(),
    maxSteps: hardCap,
    minSteps: 1,
    stakes: instance.stakes ?? 1,
  });
  return {
    maxSteps: allocation.recommendedSteps,
    convergenceThreshold,
  };
}

// CLI entry
async function main() {
  const { values } = parseArgs({
    options: {
      workload: { type: 'string', short: 'w' },
      output:   { type: 'string', short: 'o' },
      adaptive: { type: 'boolean' },
    },
  });

  if (!values.workload) {
    console.error('Usage: pnpm sweep -- --workload <a11oy|sentra|amaru> [--adaptive] [--output <dir>]');
    process.exit(2);
  }

  const workload = await loadWorkload(values.workload);
  const cfg: SweepConfig = {
    ...DEFAULT_GRID,
    adaptiveDepthFlag: !!values.adaptive,
  };

  const result = await runSweep(workload, cfg);

  const outDir = resolve(values.output ?? `./results/${values.workload}`);
  mkdirSync(outDir, { recursive: true });
  const outPath = resolve(outDir, `sweep-${Date.now()}.json`);
  writeFileSync(outPath, JSON.stringify(result, null, 2));

  // Manifest with reproducibility metadata
  const manifest = {
    workload: result.workload,
    runtimeVersion: result.runtimeVersion,
    fixtureSha256: result.fixtureSha256,
    config: result.config,
    resultPath: outPath,
    resultSha256: createHash('sha256').update(JSON.stringify(result)).digest('hex'),
    generatedAt: new Date().toISOString(),
  };
  writeFileSync(resolve(outDir, 'manifest.json'), JSON.stringify(manifest, null, 2));

  console.log(`Sweep complete: ${result.cells.length} cells, ${result.pareto.length} Pareto-optimal`);
  console.log(`Output: ${outPath}`);
  console.log(`Manifest: ${dirname(outPath)}/manifest.json`);
}

if (import.meta.url === `file://${process.argv[1]}`) {
  main().catch((err) => {
    console.error(err);
    process.exit(1);
  });
}

export { runSweep, type SweepConfig, type SweepResult };
