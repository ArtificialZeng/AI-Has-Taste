# Fresh mathematical referee report

## Frozen scope and integrity

I reviewed the exact `resolution-paper` claim frozen in `claim.json`: for every
integer \(r\geq 1\) and every \(n\geq 2^{r-1}\binom{r+1}{2}\), one has
\(\lambda(r,n)=\lambda(r)\) over the real field.  This is the full assertion in
`source.md`, not a subsidiary or weakened statement.  I independently compared
the SHA-256 digests of `claim.json` and all four listed evidence files with
`audit/snapshot.json`; every digest matched.  The snapshot digest is
`7bfb0b28c55d1470cd55ad3c0fe5642790ad29190ac4e282a81cfc91794a5c3d`.

## Reconstruction of the decisive argument

Let \(d=\dim \mathbb S^r=\binom{r+1}{2}\).  For any maximizing feasible pair
\((U,w)\) in Theorem 2.1 of the cited paper, write \(x_i^T\) for row \(i\) and
choose \(\varepsilon_i=1\) when \((x_i)_1\geq0\), and \(-1\) otherwise.  With
\(D=\operatorname{diag}(\varepsilon_i)\), the pair \((DU,w)\) is feasible and
maximizing because
\[
 (DU)^T(DU)=U^TU,
 \qquad
 |\langle \varepsilon_i x_i,\varepsilon_j x_j\rangle|
   =|\langle x_i,x_j\rangle|.
\]
Thus every normalized row has nonnegative first coordinate.  With the source's
convention \(\operatorname{sgn}(0)=+1\), only the \(2^{r-1}\) sign orthants
whose first sign is positive can occur.

The source's Claims 2.1--2.3 apply to this new maximizing pair without any
switching assertion about the old graph.  Defining a new graph from the signs
of the normalized inner products gives the Ky--Fan equality and a symmetric
\(H\) satisfying \(M(G,w)DU=(DU)H\), followed by
\(y_i^THy_i=\lambda(r,n)w_i^2\).  Hence the hypotheses and proof of the source's
Cloning Claim 2.4 remain available after normalization and after every later
cloning step.

For one occupied half-orthant \(C_s\), coordinatewise sign agreement implies
\(\langle y_i,y_j\rangle\geq0\) for all \(i,j\in C_s\), including boundary
coordinates equal to zero.  In \(\mathbb S^r\), conic Caratheodory represents
\[
  \sum_{i\in C_s}y_i y_i^T
    =\sum_{i\in I_s}\beta_i y_i y_i^T,
  \qquad |I_s|\leq d,\quad \beta_i\geq0.
\]
Taking the cloning coefficients to be \(\beta_i\) on \(I_s\), zero on the
remaining indices of \(C_s\), and one elsewhere satisfies Claim 2.4 exactly.
It produces a maximizing pair with at most \(d\) nonzero rows in that cell.
Empty cells and a zero conic sum cause no exception: zero generators can be
omitted and the empty representation can be used.

Repeating this operation over the \(2^{r-1}\) half-orthants is legitimate.
Positive cloning scalars preserve the complete sign vector of every nonzero
row, rows outside the processed cell are fixed, and a zero scalar creates only
a zero row.  Such a zero row is assigned to the all-positive cell by the sign
convention but remains zero forever, so it cannot increase any nonzero-support
count, even if the all-positive cell was processed earlier.  The final
maximizing pair therefore has at most \(2^{r-1}d\) nonzero rows.

For completeness, a zero row has zero weight: its row in the absolute Gram
matrix \(B\) is zero, while Claim 2.1 gives
\(Bw=\lambda(r,n)w\), and the source proves \(\lambda(r,n)\geq1\).  Deleting all
zero rows consequently preserves feasibility, the unit norm of \(w\), and the
objective.  If \(k\) rows remain, then rank gives
\(r\leq k\leq 2^{r-1}d\), and Theorem 2.1 plus monotonicity yields
\[
  \lambda(r,n)\leq\lambda(r,k)
    \leq\lambda\!\left(r,2^{r-1}d\right).
\]
Taking the supremum over every \(n\geq r\), using the source's identity
\(\lambda(r)=\sup_{n\geq r}\lambda(r,n)\), proves equality at the new threshold;
monotonicity proves equality for every larger \(n\).  The threshold is at least
\(r\), and \(r=1\) gives \(d=1\), so no endpoint is omitted.

## Adversarial checks performed

I checked the universal quantifiers, maximizer existence, the feasibility and
objective under independent row signs, zero first coordinates, zero inner
products in the signed graph, empty orthants, nonnegative conic coefficients,
repeated cloning order, migration of zero rows, deletion of zero rows, rank,
padding/monotonicity, and the final supremum passage.  The proof uses no division
by a possibly empty cell size and no limiting exchange beyond the stated
supremum identity.  I found no circular dependence: Claims 2.1--2.3 are
re-established from maximality before each use of Claim 2.4.

## Source comparison and contribution

I inspected the cited primary PDF itself.  Its Theorem 2.1 states the required
optimization maximum; Claims 2.1--2.4 provide exactly the eigenvector,
invariant-subspace, quadratic identity, and cloning facts used above; Claim 2.5
uses all \(2^r\) coordinate orthants; and Theorem 1.3 consequently states the
larger threshold \(2^r\binom{r+1}{2}\).  The paper says that minor improvements
may be possible but does not state the frozen factor-two bound.  The candidate's
precise delta is therefore the valid projective row-sign normalization followed
by the same conic reduction on half as many orthants.  This review does not
assert literature priority beyond that direct comparison; the candidate itself
also makes no such claim.

## Verdict

**Accept.**  The candidate proves the frozen original assertion in its full
scope.  The evidence supports every decisive step, the factor-two delta is
precisely identified, and no mathematical gap requiring revision remains.
