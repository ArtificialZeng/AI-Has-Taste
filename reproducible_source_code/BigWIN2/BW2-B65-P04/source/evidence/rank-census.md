# Exact rigidity-rank census through 28 vertices

For every nonnegative pair \((s,t)\) with
\(4\le n=3s+4t\le 28\), `rigidity_rank_scan.py` constructs three
deterministic integral placements in
\(d=M(G)=n-1-a_n\), where \(a_n(a_n+1)\ge 2n\) minimally.  Vertices and
edges are ordered as specified in `rigidity_rank_results.json`; coordinates
are obtained by a fully specified SHA-256 map into \([-1000,1000]\).

All 41 feasible pairs have affine rank \(d+1\) and rigidity-matrix rank
\[
dn-\binom{d+1}{2}
\]
over \(\mathbb F_{65521}\) at all three placements.  For trial 0 of each
pair, the results file retains the row and column indices of a square maximal
minor and its nonzero determinant residue modulo 65521.  (For the trivial
case \((s,t)=(0,1)\), this is the empty minor, whose determinant is 1.)

These modular calculations are exact certificates, not floating-point rank
estimates.  A nonzero determinant modulo 65521 implies that the corresponding
integer determinant is nonzero.  Affine spanning supplies the usual
\(\binom{d+1}{2}\)-dimensional trivial-motion kernel, so the rational rank is
at most the displayed target; the certified minor gives the reverse
inequality.  Existence of this placement proves that the generic rank is the
target.  Consequently
\[
\operatorname{rig}(\overline{sC_3\sqcup tC_4})=M(G)
\quad\text{for every feasible pair with }n\le 28.
\]

`verify_rigidity_certificates.py` independently reconstructs every graph and
placement from the serialized specification, checks affine spanning, and
recomputes every stored determinant.  Its recorded successful invocation is:

```text
verified 41 affine-span and nonzero-maximal-minor certificates modulo 65521
```

This is an exhaustive finite theorem only.  It neither proves the universal
claim nor excludes a first counterexample at \(n\ge29\).
