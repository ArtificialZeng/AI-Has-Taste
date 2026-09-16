# Fresh mathematical referee report

Job: `win-00082-p02-referee-7cbf8fcd4718`  
Frozen snapshot: `999a4d7b27c6e655ee55e8e4a455c9b8d7abf10be472a01da16ee07f57fbe6b9`

## Scope reviewed

I reviewed the exact `resolution-paper` claim frozen in `claim.json`: for the
same arbitrary integer \(g\geq3\), equality of \(\Psi_{H,g}\) for two rooted
trees of the same order and root height at most two implies rooted
isomorphism.  This is the whole claim in `source.md`, including \(N=1\), and
not Conjecture 9.10 for unrestricted rooted trees.

All seven hashes recorded in `audit/snapshot.json` agree with the current
frozen files.  I reconstructed the proof from the definition rather than
treating the committed computation as proof.

## Reconstruction of the decisive argument

For \(N\geq2\), deleting the root leaves \(r\) components.  Height at most two
and acyclicity force each component to be a star whose center was adjacent to
the root.  Let its order be \(b_i\geq1\), and put \(d_i=b_i-1\geq0\).  Thus

\[
 \sum_{i=1}^r b_i=N-1,
\]

and the multiset of the \(b_i\)'s is exactly the rooted-isomorphism datum.

For \(0\leq k\leq\lfloor(N-1)/2\rfloor\), consider

\[
 A_k=[z_gz_2^kz_1^{N-1-2k}]\Psi_{H,g}.
\]

The distinguished root-component factor has index at least \(g\).  In the
target monomial its only factor whose index is at least \(g\) is \(z_g\), also
when \(g=3\).  Hence the root component is a singleton and every root edge is
absent.  In branch \(i\), if \(q\) leaf edges are present, the nonsingleton
component has order \(q+1\).  Matching the target forces \(q\in\{0,1\}\).
Choosing \(q=1\) in precisely \(k\) distinct branches gives one size-two
component per chosen branch, with \(d_i\) choices in branch \(i\).  The
remaining singleton count is automatically \(N-1-2k\).  Therefore

\[
 A_k=\sum_{|S|=k}\prod_{i\in S}d_i=e_k(d_1,\ldots,d_r).
\]

There is no commutative-monomial collision hidden here: an additional
nonroot component of order \(g\) would add a second \(z_g\), and any component
order outside \(\{1,2\}\) would introduce a factor absent from the target.

Let \(m=|\{i:d_i>0\}|\).  Every such branch uses at least two of the \(N-1\)
nonroot vertices, so \(m\leq\lfloor(N-1)/2\rfloor\).  Consequently all
nonzero coefficients of

\[
 Q_H(t)=\prod_{i=1}^r(1+d_it)
\]

are among the extracted \(A_k\)'s.  The nonzero \(d_i\)'s are recovered with
multiplicity from the roots \(-1/d_i\) of \(Q_H\), equivalently by unique
factorization of its normalized linear factors.  This step does not assume
that the \(d_i\)'s are distinct and involves no division inside the original
polynomial.

The zero entries are recovered separately.  For \(N\geq2\),

\[
 B=[z_{g+1}z_1^{N-2}]\Psi_{H,g}=r.
\]

Indeed, the target's only possible root factor is \(z_{g+1}\), so the root
component has order two; all other vertices must be isolated.  The selected
edge set is therefore exactly one of the \(r\) root edges.  Knowing \(r\) and
the \(m\) positive entries appends exactly \(r-m\) zeros to recover the full
multiset of \(d_i\)'s, and hence the full multiset of \(b_i=d_i+1\).

Thus equal polynomials at the same \(g\) yield equal branch-order multisets
and rooted-isomorphic trees.  For \(N=1\), the only rooted tree has
\(\Psi=z_g\), so the omitted normal-form argument has no exceptional case.
Height-one trees are covered by the zero \(d_i\)'s, and the lower endpoint
\(g=3\) was explicitly checked above.  The proof is uniform in \(N\) and
\(g\), with no limiting, compactness, or computational extension step.

## Computational and source checks

I reran `evidence/audit_height_two.py --max-n 14 --max-g 14`; its fresh
output was byte-for-byte equal to `evidence/audit_height_two.json`.  I also
implemented a separate in-memory verifier using adjacency lists and
depth-first component searches rather than the committed union-find code.  It
enumerated all branch partitions for \(1\leq N\leq10\) and all
\(3\leq g\leq9\): 97 rooted types, 679 type/parameter instances, and 23,955
forest masks per fixed \(g\).  It independently checked polynomial mass, both
coefficient formulas, and full-polynomial injectivity, with no failure.  These
finite checks are corroboration only; the quantified conclusion rests on the
argument above.

The supplied primary PDF has the frozen SHA-256 digest and states Conjecture
9.10 for all rooted trees, Remark 9.12's exhaustive verification through 13
vertices and automatic range \(g\geq N\), and Theorem 9.14's branch-size
restricted mechanism via a uniquely identifiable distinguished factor.  The
candidate removes the branch-size restriction only for height-at-most-two
trees and does not assert the unrestricted conjecture.  The PDF does not
state this height-two resolution.  Its citation to reconstruction from the
fully pointed rooted polynomial is not a dependency of the submitted proof.
The title discrepancy already disclosed in `problem.md` is bibliographic and
does not change the statement.  Given the deliberately bounded source search,
this review does not certify priority, and `claim.json` makes no priority
claim.

## Verdict

**Accept.**  The elementary coefficient extraction is correct, handles all
quantifiers and degenerate cases in the frozen statement, and reconstructs
exactly the rooted-isomorphism datum.  It proves the full frozen original
claim at its stated scope.  I found no mathematical gap requiring revision;
the unrestricted all-rooted-tree conjecture remains outside the accepted
scope.
