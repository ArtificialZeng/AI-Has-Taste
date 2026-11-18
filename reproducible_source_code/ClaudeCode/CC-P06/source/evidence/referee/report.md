# Referee report (independent AI referee, 2026-11-18) on "A fully clued Slitherlink diagram with exactly five solutions"
(Saved by the author from the referee's final message; the referee could not write .md files itself.)

## Counts (own code, written before reading the authors' programs)
| Diagram | Claimed | rdp.py (frontier DP) | kernel_count.py (ker A, from every solution) |
|---|---|---|---|
| (a) 13x13 | 5 | 5 | 5 |
| (b) 12x12 | 6 | 6 | 6 |
| (c) 13x13 | 6 | 6 | 6 |
| Knuth 6x6 | 4 | 4 | 4 |
| 32/23 | 2 | 2 | 2 |
rdp.py was validated against brute-force cycle enumeration (OEIS A140517 totals) on all small grids; every solution
rechecked (degrees, connectivity, clues).

## Proposition 3 (independent search, msearch*.c: backtracking over all loops with a live set of totally even sets)
- 5x5, 6x6 full enumeration (1,222,363 and 487,150,371 loops): multiplicities 1, 2 (and 4 on 6x6: Knuth's, 1 class).
- n = 3..11: no multiplicity >= 5 (11x11: 78,801,308 nodes). 12x12 not finished (partial: only the note's
  multiplicity-6 class, no multiplicity 5).
- Multiplicity 3 / 4 classes: 7x7: 2 / 3; 8x8: 9 / 19; 9x9: 314 / 146.
- All 35 non-square grids with <= 171 cells and gcd(m+1,n+1) >= 4 (rect/): no multiplicity >= 5.
  Hence every diagram with fewer than 144 cells has multiplicity <= 4.
- teven.py completeness argument checked: correct; no bug found; LIMIT should be mentioned.

## Required corrections (all addressed in the revision)
1. "For n <= 2 there is no ambiguity" is false (32/23 has 2); use multiplicity <= 2^dim T.
2. Diamond sets: use Beluhov's frame (corners half a unit outside) or Lemma 3 characterization; note Beluhov counts vertices.
3. "Not a coset" is vacuous; state the structure {0,Y,Y+Z} u (X+{0,Y+Z}).
4. Fig. 2 decomposition relative to loop 1 (figure order): {0,B2}+{0,B11,B7+B9+B11}.
5. Remove "still running"; state minimum area; give exact or no counts; mention LIMIT and independent confirmation;
   add logs for n = 3..6 (teven: feasible 2/7, 7/15, 8/31, 20/63; cliques 0, 0, 0, 140).
Suggestions: ker A proof (self-contained), figure in two rows, machine-readable loops.
