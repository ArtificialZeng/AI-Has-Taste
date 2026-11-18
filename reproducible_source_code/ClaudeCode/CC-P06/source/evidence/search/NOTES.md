# Fully clued slitherlink with five or more solutions (TAOCP 7.2.2.1-411, errata 4b.535 of 28 Aug 2023)

Question (Knuth, errata to answer 411; Beluhov arXiv:2308.08798 Sec. 10): is there a fully clued slitherlink
diagram (a "signature") with exactly five solutions? With at least five?
Known: multiplicities 1, 2, 3, 4 occur (4 on (4k+3)x(4k+3) vertex grids, 3 on (4k+4)x(4k+4)); smallest square
grids: 7x7 vertices for 4 and 8x8 vertices for 3 (Beluhov's exhaustive search).
Grid sizes below are VERTEX counts (W x H vertices = (W-1) x (H-1) cells), as in Beluhov.

## Method
- slither.py: exact solution counter for a fully clued grid (SAT enumeration with lazy loop cuts).
  Checks: Knuth's 6x6-cell example -> 4, his three 5x5 examples -> 2 each, Beluhov Fig. 10 -> 3, "32/23" -> 2.
- Two cycles with the same signature differ by a totally even set E (Beluhov Sec. 4); these form a space T of
  dimension gcd(W,H)-1 (computed by F2 elimination in teven.py; agrees with Beluhov: n-1 for n x n).
- teven.py W H K: (1) for every nonzero E in T test whether some pseudocycle C has C xor E a pseudocycle with the
  same signature ("pseudo-feasible"); (2) build the graph on feasible E's with E~F iff E xor F feasible;
  (3) every signature of multiplicity >= K gives a (K-1)-clique {E_1..E_{K-1}} (differences from one solution C1);
  enumerate all such cliques and solve the joint model (one copy of variables for C1; the other copies are C1 xor E_t)
  first for pseudocycles, then with lazy single-loop cuts; exact counter on any hit. Complete; iteration limits are
  logged as LIMIT (none so far).
  Validation: K=4 on 7x7 and K=3 on 8x8 immediately return Beluhov's/Knuth's signatures.
- satk.py: independent generic K-copy SAT model (5 copies, equal clues, pairwise distinct, lazy loop cuts).

## Results so far (K = 5, i.e. multiplicity >= 5)
| grid (vertices) | dim T | method | result |
|---|---|---|---|
| 7x7 | 6 | satk | none (UNSAT) |
| 8x8 | 7 | satk + teven | none |
| 9x9 | 8 | teven (6825 cliques) | none |
| 10x10 | 9 | teven (14875 cliques) | none |
| 8x12, 12x8 | 3 | satk + teven | none |
| 9x12 | 2 | satk | none (dim T = 2 allows at most 4) |
| 8x16 | 7 | teven | none |
| 10x15, 12x16, 12x18 | 4, 3, 5 | teven | none |

## RESULT (2026-11-18): signatures with exactly SIX solutions exist
- 13x13 vertices (12x12 cells): found/m6_12x12.txt; 14x14 vertices (13x13 cells): found/m6_13x13.txt.
- Exact multiplicity 6 confirmed by two independent counters: SAT enumeration (slither.py) and plain backtracking
  over edges with a union-find single-loop check (bcount.c; also gives 4 for Knuth's 6x6 example).
  The six loops: found/m6_12x12_solutions.txt.
- Structure (analyze.py, diamond decomposition of differences from solution 1): {0, B} x {0, A, A+C} with
  B = B(2), A = B(7)+B(9), C = B(11): a two-way switch times a three-way switch, 2 x 3 = 6.
- This answers Beluhov's question (arXiv:2308.08798, Sec. 10) whether a signature of multiplicity >= 5 exists.
  Knuth's errata question (exactly five?) remains: a product of switches cannot give 5.
- No multiplicity >= 5 on 7x7..11x11 square vertex grids (complete clique search; 11x11: 194775 cliques).

## RESULT (2026-11-18): a fully clued slitherlink with EXACTLY FIVE solutions
found/m5_13x13.txt (13x13 cells = 14x14 vertices; every cell clued):
3222222122223 / 2222222221122 / 2222122223232 / 2222221222112 / 2212222222222 / 2222222222221 / 2221122211222 /
1222222222222 / 2222222222122 / 2112221222222 / 2323222212222 / 2211222222222 / 3222212222223
- 5 single-loop solutions by SAT enumeration (slither.py) and by plain backtracking (bcount.c); pictures in
  found/m5_13x13_solutions.txt.
- Differences from solution 1 (diamond decomposition): 0, B12, B7+B11, B3+B5+B7+B11, B3+B5+B7+B11+B12,
  i.e. {0, X, Y, Y+Z, Y+Z+X} -- not a product of switches.
- Several other inequivalent five-solution signatures on the same grid (logs/ex5_14x14.log).
- Answers Knuth's question in the 4B errata to answer 7.2.2.1-411 (amendment of 28 Aug 2023, still in the
  16 Apr 2026 errata): "It's currently unknown whether or not exactly five loops are possible."
- Novelty checks (2026-11-18): Beluhov arXiv:2308.08798 has only v1 (Aug 2023) and lists >= 5 as open;
  no citing papers on Semantic Scholar; Gong arXiv:2410.19078 is about triangular grids; web searches found nothing.
- 2026-11-18 21:40: complete search on 12x12 vertices (11x11 cells): 205 feasible of 2047, 520320 4-cliques, no
  signature of multiplicity >= 5, no LIMIT. So no fully clued n x n diagram with n <= 11 cells has >= 5 solutions.
  Paper updated (Proposition: n <= 11).
