# Root proof audit

Audit date: 2026-09-01. Verdict: PASS for the stated finite theorem.

- Recomputed the displayed witness directly: it has 12 elements in `[1,38]`
  and exactly 65 distinct sums.
- Inspected the CNF generator. It imposes exactly 12 selected elements,
  translation normalization `x_1`, the full equivalence between pair and
  selection variables, the full equivalence between sum and representation
  variables, and at least 66 represented sums.
- Regenerated the target CNF independently from the checked source. It is
  byte-for-byte identical to `certificates/no_66.cnf` and has 2,034 variables
  and 5,419 clauses.
- Replayed the complete 35,331,788-byte refutation with the bundled
  `drat-trim` binary. The checker returned `s VERIFIED`; backward checking
  retained 3,854 input clauses and 59,494 lemmas and performed 6,690,497
  resolution steps.
- Re-ran the transparent exhaustive comparison for all 55 cells
  `1 <= k <= n <= 10` at the optimum and adjacent thresholds. Every check
  passed.

The theorem therefore follows from an explicit lower-bound witness and a
replayable exact finite upper-bound certificate. No proof-assistant
formalization was used.
