# Fresh mathematical referee report

## Frozen scope and provenance

I reviewed the exact `resolution-paper` statement in `claim.json`, bound to snapshot
`221293b70b3dea6cbbdb9ef71866793dcc84fb27b32af05e7b4b2d7d358d1f48`.
The SHA-256 values of `claim.json` and every listed evidence file agree with
`audit/snapshot.json`.  The claim addresses the full universal assertion in
`source.md`: every integer pair \(m\ge 2\), \(\ell\ge1\), \(m\le2\ell+3\).
There is no restriction or silently weakened substitute claim.

## Reconstruction of the proof

Write \(L=\ell\).  For \(m\le2L+2\), the proposed cyclic constructions are valid.
For even \(m=2r\), there are \(L+1\) positions around the cyclic list
\(a,u_1,\ldots,u_L,a\), and \(r\le L+1\); inserting a block
\(c,x_{2j-1},b_{2j-1},b_{2j},x_{2j},c'\) uses only valid edges and all vertices
exactly once.  For odd \(m=2r+1\), \(r\le L\).  The exceptional \(L=1,m=3\)
list is a valid cycle.  For \(L\ge2\), the initial three-\(b\) block, the
\(u_1x_2u_2\) block, and the remaining \(r-1\) pair blocks fit in the remaining
\(L-1\) positions, again with all consecutive pairs adjacent and all vertices
used exactly once.  Hence these graphs are Hamiltonian.  Uniform deletion of a
cycle edge gives expected tree degree \(2-2/n\) at every vertex; mixing in a
sufficiently small positive full-support spanning-tree distribution preserves
the strict inequalities and gives full support.  Thus the spanning-tree
characterization proves RP throughout this range.

It remains to review the boundary \(m=2L+3\).  Put
\(A=3L+4\) and \(D=(L+2)A\).  Direct exact substitution in the seven orbit
marginals of (1) gives total mass \(|V|-1=2m+L\).  The four orbitwise incident
sums are respectively
\[
2-D^{-1},\quad 2-D^{-1},\quad 2-(L+2)^{-1},\quad 2-D^{-1},
\]
so all are strictly below two.  Every edge marginal is positive.

For a vertex set described by \((\alpha,k,h,z,d)\), the internal weight is
exactly (4).  Since the coefficient of \(d\) is \(1-D^{-1}>0\), its maximum over
feasible paired indices occurs at \(d=\min(k,h)\), and this value is attainable.
After multiplying the rank slack by \(D\), I independently recovered formulas
(5) and (6).  If \(k\le h\), the coefficient of \(h\) is
\[
D-(A+1)\alpha-Az\ge A-1>0,
\]
so the minimum is at \(h=k\), apart from the three lower-size boundary cases.
If \(h\le k\), the coefficient is \(1-(A+1)\alpha-Az\): it forces \(h=0\)
when \(\alpha=z=0\), and \(h=k\) otherwise, except for the point adjacent to
the excluded full vertex set.  On the diagonal, and on the exceptional
\(\alpha=z=h=0\) branch, the resulting expression is concave in \(k\); after
taking its interval endpoints it is concave in \(z\).  Thus the listed endpoint
families are exhaustive.

Independent substitution reproduced every value in table (7).  The one endpoint
suppressed there as a larger copy is \((\alpha,z,k,h)=(0,0,m,0)\), where
\[
\Phi=\frac{6L^3+25L^2+29L+8}{2}.
\]
It exceeds the displayed \(k=2\) endpoint by
\[
\frac{L(L+2)(2L+1)(3L+5)}{2(L+1)}>0.
\]
All remaining endpoint expressions in (7) are positive for their stated ranges,
and their minimum is \(1\), attained at
\((\alpha,z,k,h)=(0,0,1,1)\).  Consequently every proper nontrivial vertex set
satisfies
\[
x(E[S])\le |S|-1-D^{-1}<|S|-1.
\]
Together with positivity and total mass \(|V|-1\), these strict rank inequalities
place the marginal vector in the relative interior of the spanning-tree
polytope.  The strict incident bounds then establish RP at \(m=2L+3\).

## Checks actually performed

- Recomputed the snapshot file hashes and obtained exact agreement.
- Recomputed symbolically the total mass, all four incident sums, formulas
  (5)--(6), every endpoint value in (7), and the additional exceptional endpoint
  above.
- Enumerated vertex subsets directly from the graph edge definition, without
  using the descriptor loop, for \(L=1,2\).  The minimum rank slacks were exactly
  \(1/21\) and \(1/40\), each at \(\{b_i,x_i\}\).
- Independently instantiated and adjacency-checked every Hamiltonian construction
  for \(1\le L\le20\) and \(2\le m\le2L+2\).
- Inspected the supplied exact verifier and its recorded run for \(1\le L\le30\).
  That regression is corroborative; the infinite conclusion rests on the
  endpoint proof above.

## Source comparison, contribution, and limitations

Within the frozen evidence, Wang's Theorem 3 supplies the spanning-tree
characterization and Proposition 16 supplies non-RN for \(m\ge2\ell+4\).  The
candidate proves the complementary positive range, including the previously
untreated boundary, so it is a substantive full resolution of the frozen claim;
combined with Proposition 16 as recorded in the source dossier, it yields the
stated exact threshold.  The evidence describes the literature status as
new-question/status-uncertain and makes no priority claim.  This mathematical
verdict does not upgrade that bounded literature statement; any publication
still requires the separate citation/source audit.

I found no unresolved mathematical gap in the frozen candidate scope.

## Verdict

**Accept.**  The exact candidate scope, proof, and claimed contribution pass
mathematical review.
