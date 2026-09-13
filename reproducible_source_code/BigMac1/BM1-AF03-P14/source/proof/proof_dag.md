# Proof dependency graph (target)

`T0` is the full \(Q_5\) classification endpoint.

- `L1` (proved): signed permutations and scaling reduce directions to the
  ordered positive simplex, stratified by support.
- `L2` (proved and independently reconstructed): coarea plus inclusion–exclusion gives
  the exact truncated-power formula and \(C^3\) regularity across full-support
  pair-sum walls.
- `L3` (proved and independently checked): every support \(<5\)
  critical direction is in the exact \(n\le4\) list.  The \(Q_3\) elimination
  is serialized and independently verified.  The complete \(Q_4\) exhaustion
  is the rational branch proof in `proof/agent_builder_report.md` §3.1--§3.2;
  `results/breaker_q4_baseline_certificate.json` certifies only the tangent
  saddle form at the surviving non-diagonal point.  Ambient local types then
  follow from inherited tangent directions and exact transverse/cubic tests.
- `L4` (proved): every nontrivial full-support critical direction satisfies
  \(\max a_i<\sum_{j\ne i}a_j\), so after \(\sum a_i=2\) all singletons are
  active and the formula is determined by the pair graph
  \(E=\{ij:a_i+a_j<1\}\).
- `L5` (proved and independently checked): shiftedness and intersection exhaust the six
  realizable strict high-pair graphs; generic approach plus \(C^3\) regularity
  assigns every pair wall to a certified chamber closure.
- `L6(G)` (certified and independently reconstructed for all six graphs): empty has only the diagonal root;
  star1 has exactly the stated quadratic orbit; star2, star3, star4, and
  triangle have no other closure-admissible critical point.  Each endpoint is
  reconstructed from exact serialized data and exercised by mutations.
- `L7(root)` (proved exactly): every non-diagonal root from `L6` has an
  exact positive and an exact negative tangent variation; any degenerate root
  is resolved at higher order.
- `T0` is assembled from `L1`–`L7`: the only local extrema are the diagonal
  orbits \(d_1,d_2,d_5\).  A single non-diagonal root with a certified
  definite local form would instead disprove `T0`; none survives the exact
  classification.  The hostile referee independently accepted the complete
  Q4/chamber/wall/support splice with 20/20 endpoints PASS and no findings.
  Hence `T0` is proved.
