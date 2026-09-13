# Breaker record

Date: 2026-08-30.  This audit did not trust the intended diameter.

- Replaced the Builder's four-block Pasch finder by a derived-cycle-graph
  enumerator.  It independently recovered all 1,390 occurrences.
- Ignored nauty labels and separated all 80 representatives using the
  exact sorted point-Pasch signature.  Every signature was distinct.
- For each switched system, required a full block-preserving bijection to
  the proposed target, constructed by exact Steiner-quasigroup
  backtracking.
- Checked every one of the 258 edges has switch witnesses in both
  directions.
- Recomputed the graph metric by a standalone all-pairs BFS program.
- Tried six corruptions: repeated point in a block, missing vertex, deleted
  edge, duplicate edge, wrong diameter, and wrong switch target.  The
  verifier rejected all six; see `certificate/negative_tests.json`.

No counterexample to the certified graph or diameter was found.
