# Fresh mathematical audit

## Frozen scope

I reviewed the `result-note` claim bound to snapshot
`a394b5c8b22ba19b8f205f5f2d9f689baa73b728c5876f78bc38b305a625f5e6`.
The claim is only the definition-closed branch \(\ell=1\): for every integer
\(m\ge2\),
\[
\operatorname{OPT}_{m,1}=\max\{2m+2,5m/2\},
\]
and hence \(J_{m,1}\) is fractionally Hamiltonian exactly for
\(2\le m\le4\).  The frozen claim explicitly leaves the original
all-\((m,\ell)\) problem unresolved.  I used the mathematical argument and
certificates listed in the snapshot as decisive evidence; `checkpoint.md` was
not used as a substitute for them.

## Reconstruction of the proof

The graph \(J_{m,1}\) has \(2m+2\) vertices.  Summing all singleton-cut
constraints in the primal LP counts every edge twice, so
\[
2\sum_e x_e\ge 2(2m+2),
\]
giving the universal lower bound \(\operatorname{OPT}_{m,1}\ge2m+2\).

There is also a feasible cut-dual solution supported, for each \(i\), on
\(\{b_i\}\), \(\{x_i\}\), and \(\{b_i,x_i\}\), with respective weights
\(1/4,3/4,1/4\).  Direct recomputation gives dual edge loads
\[
1\ (b_i b_j),\quad 1\ (a x_i),\quad 1\ (b_i x_i),\quad
1\ (u x_i),\quad \tfrac12\ (u b_i),\quad 0\ (ua).
\]
Thus every dual constraint is satisfied and the dual objective is
\(2m(1/4+3/4+1/4)=5m/2\).  Weak duality therefore yields the matching combined
lower bound
\[
\operatorname{OPT}_{m,1}\ge\max\{2m+2,5m/2\}.
\]

For \(m\ge4\), assign primal weights
\[
x_{b_i b_j}=\frac1{m-1},\qquad
x_{a x_i}=x_{u x_i}=\frac12,\qquad x_{b_i x_i}=1,
\]
and set \(x_{ua}=x_{u b_i}=0\).  Their total is
\(\binom m2/(m-1)+2m=5m/2\).  To check all cuts, let
\(A,U,B_i,X_i\in\{0,1\}\) be shore indicators and put
\(k=\sum_iB_i\).  The cut weight is exactly
\[
C(S)=\frac{k(m-k)}{m-1}+\sum_i|B_i-X_i|
+\frac12\sum_i|X_i-A|+\frac12\sum_i|X_i-U|.
\]
If \(A\ne U\), the last two sums together contribute \(m/2\ge2\).
If \(A=U\), complementing the shore preserves the cut and permits
\(A=U=0\).  When \(k=0\), nontriviality forces some \(X_i=1\), whose three
incident positive-weight edges contribute \(2\).  When \(k\ge1\), each index
with \(B_i=1\) contributes exactly \(1\) through the last three terms, while
all remaining contributions are nonnegative.  Hence
\[
C(S)\ge k+\frac{k(m-k)}{m-1}\ge2;
\]
for \(k=1\) this is equality, and for \(k\ge2\) it is immediate.  This covers
every nonempty proper shore and proves primal feasibility for all \(m\ge4\).

For the remaining parameters, the displayed vertex sequences
\[
a,x_1,b_1,b_2,u,x_2,a
\]
for \(m=2\), and
\[
a,x_2,b_2,u,x_1,b_1,b_3,x_3,a
\]
for \(m=3\), use only graph edges and visit every vertex once.  Their cycle
incidence vectors are feasible primal solutions of objectives \(6\) and \(8\).
Together with the two lower bounds, this proves the asserted optimum for every
integer \(m\ge2\).

Finally, the graph order is \(2m+2\), and the frozen LP equivalence says that
fractional Hamiltonicity is equivalent to equality of the optimum with this
order.  Since \(5m/2=2m+2\) at \(m=4\) and exceeds it exactly when \(m\ge5\),
the stated if-and-only-if classification follows.  In particular,
\(\operatorname{OPT}_{5,1}=25/2>12\), so the asserted boundary counterexample
is exact.

## Checks and attacks performed

- I checked the domain and degeneracies: \(m\ge2\), and the only denominator
  \(m-1\) is used in the all-cut construction for \(m\ge4\).  All dual shores
  are nonempty and proper.
- I checked the graph edge types against `problem.md`; no absent edge is used by
  either Hamiltonian cycle or either certificate.
- I checked the complementary-shore reduction and both cut cases, including
  \(k=0,1,m\), \(A\ne U\), and the equality value \(m=4\).
- I reran `evidence/cut_lp_certify.py` with exact rational arithmetic.  It
  verified all \(31,127,511,2047,8191\) complementary cut representatives for
  \(m=2,3,4,5,6\), respectively, with minimum cut weight \(2\), matching primal
  and dual objectives, and maximum dual edge load \(1\).
- I also used a separately written in-session enumerator with a different
  vertex/edge ordering to reconstruct the primal cuts and advertised dual
  loads from the serialized certificate.  It reproduced the same exact five
  objective values and independently validated both small Hamiltonian cycles.
  These finite checks audit the certificates; the quantified conclusion rests
  on the symbolic argument above.
- The primal program has no explicit upper bounds, but this causes no gap.  At
  \(m=4\) the exhibited equality solution already has all weights at most one;
  for \(m=2,3\) the cycle vectors do as well.  On the negative branch only
  \(\operatorname{OPT}>|V|\) is needed.

## Source comparison and contribution

The frozen comparison in `problem.md` records only a previously known
non-fractional-Hamiltonicity implication for \(m\ge2\ell+4\) (via the stated
RN/RP implication chain), plus a remote sufficient positive regime.  At
\(\ell=1\), that negative implication starts at \(m=6\).  The audited theorem
instead gives the exact LP value for the entire infinite \(\ell=1\) branch and
locates the negative threshold at \(m=5\).  Thus it supplies both an exact
definition-closed branch classification and a counterexample one integer below
the recorded proposed sharp boundary.  This is not a corollary of the prior
parameter ranges described in the frozen evidence, and it meets the minimum
partial-result scope explicitly permitted by the original problem.

The literature screen recorded in `problem.md` is expressly limited and does
not prove priority.  Accordingly, this audit accepts the bounded mathematical
contribution and source-relative delta, not an absolute novelty or open-status
claim.  Any manuscript must preserve that limitation and must state that the
full all-\((m,\ell)\) problem remains unresolved.

## Verdict

**Accept.**  The exact frozen `result-note` scope, its symbolic proof, its
boundary certificate, and its nontrivial partial contribution all pass.  No
substantive claim revision is needed.
