# Fresh mathematical referee report

**Verdict: accept** the exact frozen scope as a `result-note`. The original
order-seven existence problem remains unresolved.

## Scope and integrity

I reviewed the claim bound to snapshot
`03b845ec58a7905569232434df9916db9fa04acfc1b7f8c3492e96b90ec16afe`.
The hashes of `source.md`, `problem.md`, `claim.json`, and all decisive scripts
and JSON certificates agree with `audit/snapshot.json`. In accordance with the
job instruction, I did not use `checkpoint.md`. The immutable source retained
SHA-256
`db3a6a3a46749c29054363b03ef7f9b7acf3eb1989ca3278ee21038f2454a714`.

The submitted statement is strictly subsidiary. It asserts local rigidity in
a specified collection of three-coordinate Cayley families through unsigned
permutation anchors; it neither constructs a proper order-seven matrix nor
excludes general rational Euler points.

## Reconstruction of the decisive argument

Let the permutation underlying (P) be (p). Exactly one diagonal 1 means
that (p) has exactly one fixed point. A permutation matrix has eigenvalue
(-1) exactly when its permutation has an even cycle. Thus all remaining
cycles have odd length at least 3. After the one fixed point is removed, the
remaining 6 symbols can only have cycle lengths (3+3). This proves the first
sentence of the claim.

The assumptions on diagonal and antidiagonal hits give (D(P)=A(P)=1).
Since (I+P) is invertible,

\[
 S_P=(I-P)(I+P)^{-1},\qquad
 Q(S_P)=P.
\]

The matrix (S_P) is skew-symmetric. Put (B=(I+P)/2=(I+S_P)^{-1}) and
(E=xF_{su}+yF_{vw}+zF_{st}). Direct algebra gives

\[
 Q(S_P+E)=2(I+BE)^{-1}B-I
          =P-2BEB+2BEBEB+O(\lVert E\rVert^3).
\]

The cycle decomposition (\{s\}\sqcup C_1\sqcup C_2) makes (B) block
diagonal, while every selected edge of (E) joins two different blocks.
Consequently the linear term (-2BEB) has no entry in the support of (P).
In particular the linear terms of both (D(Q)-1) and (A(Q)-1) vanish.

Expanding the selected squares through degree two gives the coefficient
formula used by both checkers:

\[
 [D-1]_2=\sum_i L_{ii}^2+2\sum_iP_{ii}H_{ii},\qquad
 [A-1]_2=\sum_i L_{i,8-i}^2+2\sum_iP_{i,8-i}H_{i,8-i},
\]

where (L=-2BEB) and (H=2BEBEB). Exhaustion over all qualifying anchors
and all component-triangle edge choices yields

\[
 [D-1]_2=-2x^2-2z^2,
\]

and the coefficient of (y^2) in ([A-1]_2) is always nonzero. Its possible
values in the independent certificate are

\[
 -\tfrac12,-\tfrac14,\tfrac14,\tfrac12,\tfrac34,1.
\]

These initial forms prove isolation, not merely infinitesimal rigidity.
Indeed, if distinct common real zeros converged to the origin, normalize them
by their Euclidean norms and take a convergent subsequence of directions. The
degree-two part of (D-1) first forces the limiting (x)- and (z)-coordinates
to vanish. The nonzero (y^2) coefficient of the degree-two part of (A-1)
then forces the limiting (y)-coordinate to vanish, contradicting that the
limiting direction is a unit vector. Thus the origin is an isolated real
common zero. The stated consequences for continuous solution germs and
rational parametrizations defined at a real parameter value follow because
rational maps are continuous wherever defined.

## Independent checks performed

I inspected the exact enumeration and Taylor-coefficient implementations. The
anchor loop exhausts all (7!) permutations and filters the exact hypotheses;
the edge loops exhaust (3\cdot9\cdot3=81) choices for every anchor. Hence the
reported scope is exhaustive rather than sampled: 112 anchors and 9,072
families.

I reran `evidence/verify_cayley_triangle_tangents.py`, which uses only Python's
standard-library `fractions.Fraction` and does not import the SymPy search
implementation. The fresh output reported 112 anchors, 9,072 families, and
zero certificate failures. Its bytes had SHA-256
`e1682df6664a77708fcc78f64afd27a7c91cc6aa17b2ef40473e2645dd189777`,
exactly matching the frozen
`evidence/cayley_triangle_fraction_check.json`. I also checked that the 35
quadratic-type counts in `evidence/cayley_triangle_slices.json` sum to 9,072
and that its failure list is empty. The bounded resultant/grid experiment is
not needed for, and was not promoted into, the local theorem.

## Contribution and limits

The comparison frozen in `problem.md` identifies the nearest routes as the
known improper permutation examples and mirror-pair rotations. Within that
bounded comparison, the submitted delta is an exact obstruction to the
natural component-triangle enlargement at every eligible permutation anchor.
It is not a routine single-example calculation: the antidiagonal placement
varies with the anchor, and the nonvanishing needed for isolation is certified
across every case by two exact implementations. A credible use is immediate:
any local construction from such an anchor must leave these three-coordinate
families (or use a different seed), so the result prunes a precisely described
sparse-seed strategy.

The literature statement remains appropriately limited to the sources and
search described in `problem.md`; I do not interpret it as proof of priority.
The result does not resolve the original problem, does not rule out deformations
using additional Cayley coordinates, and does not rule out a positive-dimensional
complex or rational algebraic component on which the anchor is an isolated real
point. Those limitations are explicit in the frozen claim. Scope, correctness,
exact evidence, and the modest claimed contribution therefore pass.
