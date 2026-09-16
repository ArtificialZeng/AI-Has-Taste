# Fresh mathematical referee report

**Job:** `win-00040-p03-referee-9675a6c1972e`  
**Frozen snapshot:** `bfe481b5d2c7e1ab07682d05730d47e8c7a9103013c3df9f5b71e2e85b5248cb`  
**Verdict:** accept

## Scope reviewed

The frozen candidate is a `result-note`, not a resolution of the original
problem. Its exact assertion is that the degree-eight polynomial

\[
H_4(x)=\prod_F\sum_{v\in F}x_v-
\left(\sum_{|S|=5}\operatorname{Vol}(S)\prod_{v\in S}x_v\right)
\left(\sum_vx_v\right)^3
\]

is nonnegative when the sixteen nonnegative coordinates take at most two
distinct values. The original unrestricted copositivity problem remains
unresolved. I reviewed this exact scope and did not replace it by a smaller
claim.

All five hashes in `audit/snapshot.json` were recomputed before review and
matched the frozen files.

## Reconstruction of the decisive argument

For a subset \(U\) of cube vertices, assign \(a\) to vertices of \(U\) and
\(b\) to its complement. For \(a,b\geq0\), direct grouping by
\(j=|S\cap U|\) gives

\[
A=\sum_{j=0}^5 c_j(U)a^j b^{5-j},\qquad
T^3=(|U|a+(16-|U|)b)^3,
\]

where \(c_j(U)\) is the exact integer sum of the normalized volumes of the
five-subsets meeting \(U\) in \(j\) vertices. Each of the eight facet factors
is

\[
q_F(U)a+(8-q_F(U))b,
\]

so the substitution gives a homogeneous bivariate polynomial

\[
H_4=\sum_{k=0}^8h_k(U)a^k b^{8-k}
\]

with integer coefficients. If all nine coefficients are nonnegative, the
claimed inequality follows for all nonnegative \(a,b\).

Every assignment with exactly two distinct values determines a nontrivial
unordered bipartition \(\{U,V\setminus U\}\). Exactly one side omits the fixed
vertex \((1,1,1,1)\), producing one of the \(2^{15}-1=32767\) nonempty masks
used by the certificate. Swapping the sides merely swaps \(a,b\). Constant
assignments are covered by setting \(a=b\) in any one of these substitutions.
Thus there is no missing empty, full, constant, zero, or boundary case.

The supplied standard-library verifier computes all \(\binom{16}{5}=4368\)
normalized volumes by exact integer determinants, forms every coefficient,
and checks all \(32767\times9=294903\) positions. I reran it successfully. Its
reported invariants were

```
volume_distribution={0: 1360, 1: 2672, 2: 320, 3: 16}
negative_coefficients=0
zero_coefficients=2040
smallest_positive_coefficient=1
invariant_h_at_one=3014656
certificate_sha256=cd479d1e958d79bcd9580697f4c4fa2a932f18448174226026ecdeffcfdbbd19
```

I also wrote and ran `audit/referee_verify.py`, which does not call the
candidate code. It uses a different vertex ordering, fraction-free
elimination instead of the Leibniz determinant, and direct enumeration of the
\(2^8\) choices in the product of facet factors instead of the candidate's
polynomial multiplication. It independently reproduced the volume
distribution, 32767 case count, 294903 coefficient count, 2040 zeros, least
positive coefficient 1, and \(H_4(1,\ldots,1)=3014656\), again with no
negative coefficient. As a further consistency check, the volume distribution
has weighted sum \(2672+2(320)+3(16)=3360\), and
\(8^8-16^3(3360)=3014656\), agreeing with the invariant.

The computations are exhaustive integer computations; no floating-point or
sampling assertion is used in the proof of the frozen theorem. The separate
numerical searches described in the evidence are explicitly excluded from
the theorem and play no role in this verdict.

## Source comparison and contribution

The cited primary preprint, arXiv:2608.14909v1, defines the same hypercube
inequality, proves the full \(d=3\) case, and in Section 7.5 explicitly leaves
\(d=4\) open. Its Section 4 statement that certain rows can be reduced to two
possible entries concerns the precursor matrix variables, not the sixteen
weights \(x_v\) in the candidate theorem. I found no theorem in that source
covering all two-valued \(x\)-vectors. Bounded arXiv searches for the named
hypercube inequality together with `d=4`, `two-valued`, and `two values` found
the cited preprint but no equivalent primary result. This is an honest limited
comparison, not proof of priority.

The delta from the nearest result is precise: global validity is known in
dimension \(d=3\), while in the first open dimension \(d=4\) this result proves
validity on every one of the 32767 two-level cones. It is a natural and broad
subsidiary family rather than a single toy specialization, and it gives the
credible structural consequence that any strict counterexample to the
original problem must use at least three distinct coordinate values. The
exact, compact, reproducible certificate makes the partial result independently
checkable. These facts are sufficient for a `result-note`; they do not imply
that the original conjecture is proved or that publication priority is
guaranteed.

## Gaps and verdict

I found no correctness or scope gap in the frozen subsidiary theorem. The only
remaining gap is deliberately outside its scope: vectors with three or more
coordinate values are untreated, so the original problem remains unresolved.
The frozen scope, exact proof, and contribution all pass. **Verdict: accept.**
