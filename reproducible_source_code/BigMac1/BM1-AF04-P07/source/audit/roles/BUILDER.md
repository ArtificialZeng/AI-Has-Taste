# Builder record

The Builder route begins from the formal 3-set-matching reduction and seeks a
complete lower-bound proof by canonical enumeration with a target-15 exact
search.  No conclusion is inherited from the 2026 discovery code.

## 2026-08-30 actions

- Wrote `code/builder_scan.c` from the definition.  It branches on a live
  unordered pair and covers it with each available transitive triple or marks
  it permanently uncovered.  Its only upper bound is the integer free-pair
  count divided by three.
- Reproduced the known target values on every canonical class for
  (n=3,\ldots,9), with targets (0,1,2,3,5,7,9).
- Reproduced (n=10): all 9,733,056 classes have a 12-packing; aggregate
  certificate `certificates/baseline_n10_builder_full.json`.
- Completed the 192-slice order-11 run `n11_builder_full_m192`.  Every process
  exited zero, all 192 strict summaries were present, and the counts summed to
  exactly 903,753,248.  The aggregate certificate is
  `certificates/n11_builder_full_m192.json`; it records 14,481,704,095 search
  nodes and a largest single-instance search of 90,842 nodes.

The Builder independently rechecks every witness it finds before accepting an
input tournament, but the full run stores fail-only summaries rather than 900
million witnesses.  Therefore the active independent Certifier rerun remains
a mandatory part of the release gate.
