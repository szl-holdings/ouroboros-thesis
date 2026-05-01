/**
 * Smoke tests for the frontier sweep harness.
 *
 * These tests do NOT require the runtime to be installed — they exercise
 * the Pareto extractor and fixture loader in isolation.
 */

import { describe, it, expect } from 'vitest';
import { computePareto } from './analysis/pareto';

describe('computePareto', () => {
  it('returns the lower-x / higher-y frontier', () => {
    const cells = [
      { avgSteps: 2, avgQuality: 0.4, label: 'cheap-bad' },
      { avgSteps: 4, avgQuality: 0.7, label: 'middle' },
      { avgSteps: 6, avgQuality: 0.85, label: 'good' },
      { avgSteps: 5, avgQuality: 0.6, label: 'dominated' },
      { avgSteps: 8, avgQuality: 0.9, label: 'expensive-best' },
    ];

    const frontier = computePareto(cells, 'avgSteps', 'avgQuality');
    const labels = frontier.map((p) => (p.meta as { label: string }).label);

    expect(labels).toEqual(['cheap-bad', 'middle', 'good', 'expensive-best']);
  });

  it('handles a single cell', () => {
    const cells = [{ avgSteps: 3, avgQuality: 0.5 }];
    const frontier = computePareto(cells, 'avgSteps', 'avgQuality');
    expect(frontier).toHaveLength(1);
  });

  it('returns empty for empty input', () => {
    expect(computePareto([], 'a', 'b')).toEqual([]);
  });
});
