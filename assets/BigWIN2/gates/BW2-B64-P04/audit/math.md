# Fresh mathematical referee report

## Frozen scope and verdict

I reviewed the exact `result-note` claim frozen by snapshot
`47a3007ed87b11e0299bdb4d0d916a48170cac1fa0855982032752001332c4a6`.
The claim is the uniform equality
\(\deg f_{\rm raw}^{(n,p)}=3(n-1)\) for every \(n\geq3\) and every
degree-\(n\) irreducible reference polynomial, on the complete Boolean
matrix domain including singular matrices.  It does not claim to settle the
joint-ANF-leap equality or the original conjunction.

**Verdict: accept.**  The submitted argument proves the stated degree result
at its frozen scope, and the result is a nontrivial partial advance over the
cited source's upper bound.

## Snapshot and checks performed

I recomputed SHA-256 for `claim.json` and every file in the snapshot.  All
seven digests agree with `audit/snapshot.json`, including the cited PDF digest
`adccdaad3014a91760fe1af9686e7d75cd2c647a637dc9a3d69cc1476a5aa6bc`.
I reconstructed the coefficient proof from the definitions, inspected the
relevant statements in the cited PDF, and reran
`python3 evidence/verify_degree_certificate.py`.  The rerun reproduced all 11
exact Boolean Moebius checks, covering every monic irreducible polynomial of
degrees 3, 4, and 5.  These finite checks are corroboration only; acceptance
rests on the uniform proof below.

## Reconstruction of the decisive argument

Let \(E=(e_0,\ldots,e_{n-1})\) be the polynomial basis, let
\(G_{ij}=\operatorname{Tr}(e_i e_j)\), and put \(B=G^{-1}\).  If
\(\lambda_r\) is trace-dual to \(e_r\), its coordinate column is
\(B_{\bullet r}\).

For the Boolean inversion map, the coefficient vector of
\(\prod_{i\ne r}x_i\) is
\[
 \sum_{x\in H_r}x^{-1},\qquad
 H_r=\ker\bigl(x\mapsto\operatorname{Tr}(\lambda_r x)\bigr).
\]
Writing \(H_0=\ker\operatorname{Tr}\), the monic linearized polynomial with
root set \(H_0\) is
\(\prod_{h\in H_0}(z+h)=\operatorname{Tr}(z)\).  After division by \(z\),
the constant and linear coefficients show
\(\sum_{h\in H_0\setminus\{0\}}h^{-1}=1\).  Scaling
\(H_r=\lambda_r^{-1}H_0\) therefore makes the displayed coefficient
\(\lambda_r\).  The degree-\(n\) coefficient is
\(\sum_{x\in F}x^{-1}=0\) for \(n\geq2\).  Hence the complete highest layer
of \(J_n\) is exactly
\[
 \sum_r [\lambda_r]_E\prod_{i\ne r}x_i.
\]

The matrix \(B\) necessarily has an off-diagonal 1.  Otherwise its
nonsingularity over \(\mathbb F_2\) would force \(B=G=I\).  If \(M\) is
multiplication by \(\alpha\), trace-pairing invariance gives
\(M^TG=GM\), so \(G=I\) would make \(M\) symmetric.  But in a polynomial
basis with \(n\geq3\), \(Me_0=e_1\) gives \(M_{1,0}=1\), whereas
\(Me_1=e_2\) gives \(M_{0,1}=0\).  Thus there are \(a\ne r\) with
\(B_{ar}=1\), uniformly for every permitted irreducible polynomial.

Fix distinct columns \(s,k\) and form the submitted support \(Q\).  In its
bipartite row-column graph, \(Q\) is the disjoint union of the edge
\(s-r\) and the path
\[
 k=c_0-\rho_0-c_1-\rho_1-\cdots-c_{n-2}-a.
\]
To produce the target monomial in output coordinate \(k\), a top-layer
inversion term supplies a perfect matching from all but one row to the
columns other than \(s\), while an adjugate minor supplies a perfect matching
from all but one row to the columns other than \(k\).  Since the target has
all \(2(n-1)\) distinct matrix variables, those matchings must be
edge-disjoint with union \(Q\).  The first matching cannot use column \(s\),
so the isolated edge is in the adjugate matching.  The adjugate matching
cannot use column \(k\), so the first path edge is in the inversion matching;
matching constraints then force alternation along the entire path.  This is
the unique decomposition, with omitted rows \(r\) and \(a\), respectively.
The target coefficient is consequently \(B_{ar}=1\).

The target contains \(2(n-1)\) distinct matrix variables and \(n-1\)
distinct vector variables, so it has degree \(3(n-1)\).  Lower layers of
\(J_n\) cannot contribute to a monomial of this degree: a degree-\(d\)
input monomial becomes degree at most \(2d\) under \(x=Pu\), and an
adjugate entry adds at most \(n-1\).  Conversely, every adjugate entry has
degree at most \(n-1\) and \(J_n\) has degree \(n-1\), yielding the uniform
upper bound \(3(n-1)\).  Thus equality follows.

## Adversarial scope checks

- The proof is a polynomial/Boolean-ANF calculation on all independent
  entries of \((P,u)\); it never assumes \(P\) invertible and therefore does
  not replace the complete raw extension by its restriction to basis
  matrices.
- The construction works at the boundary \(n=3\): there are distinct
  columns \(s,k\), the path and isolated edge are well-defined, and the
  multiplication-matrix contradiction uses the available basis vector
  \(e_2\).
- Boolean multilinear reduction creates no hidden collision at the decisive
  degree.  Repeated selected \(u\)-columns or overlapping matching edges
  would strictly reduce the support size and cannot yield the target
  monomial.
- Determinant signs cause no issue over \(\mathbb F_2\), and distinct
  perfect matchings give distinct products in the independent matrix
  variables.
- The location \((a,r)\) may depend on the reference polynomial, but the
  off-diagonal argument establishes existence separately in every permitted
  polynomial basis.  The claim's universal polynomial quantifier is met.

## Source comparison, contribution, and remaining limits

The cited Zhang--Zhang PDF defines the same full-domain extension in
Definition 11 and proves only
\(\deg f_{\rm raw}\leq3(n-1)\) in Proposition 12.  Its Conclusion reports
attainment for \(n=3,4\) and explicitly leaves exact raw ANF values for
general \(n\) as future work.  The present result supplies a uniform nonzero
top-degree coefficient, converting that bound into equality for every
allowed polynomial reference basis.  This is not a routine restatement of
the bound: the trace-dual coefficient computation and unique matching
certificate provide the missing lower bound and a reusable exact witness.
It exactly resolves the algebraic-degree half and isolates the joint leap as
the remaining part of the original problem.

The literature conclusion is deliberately limited to comparison with the
supplied 2026 v1 and the bounded search account in `problem.md`; this audit
does not assert global priority or journal acceptance.  The equality
\(L_{\rm ANF}^{\rm joint}(f_{\rm raw})=n\) for general \(n\) remains
unproved, so the frozen original problem correctly remains `unresolved`.
