/**
 * Compute the Pareto frontier (lower-x, higher-y) over a set of cells.
 *
 * For the loop-budget frontier, x = avgSteps (lower better) and y = avgQuality
 * (higher better). A cell is Pareto-optimal if no other cell has both lower x
 * and higher-or-equal y, AND no other cell has lower-or-equal x and higher y.
 */

export interface ParetoPoint {
  cellIndex: number;
  x: number;
  y: number;
  meta: Record<string, unknown>;
}

export function computePareto<T extends Record<string, unknown>>(
  cells: T[],
  xKey: keyof T,
  yKey: keyof T,
): ParetoPoint[] {
  const points: ParetoPoint[] = cells.map((cell, i) => ({
    cellIndex: i,
    x: Number(cell[xKey]),
    y: Number(cell[yKey]),
    meta: cell as Record<string, unknown>,
  }));

  // Sort by x ascending, then y descending — a cell is on the frontier if its
  // y exceeds the running max y across all earlier cells.
  const sorted = [...points].sort((a, b) => a.x - b.x || b.y - a.y);

  const frontier: ParetoPoint[] = [];
  let maxYSoFar = -Infinity;

  for (const p of sorted) {
    if (p.y > maxYSoFar) {
      frontier.push(p);
      maxYSoFar = p.y;
    }
  }

  return frontier;
}
