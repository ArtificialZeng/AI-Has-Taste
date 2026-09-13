# Fresh mathematical referee report

## Scope and provenance

This is a fresh review of the frozen `resolution-paper` candidate for the
original statement in `source.md`.  The review is bound to snapshot digest
`88b8da6cf3406cbce4a63a50d7f7d7deefd0954c36c9f5cd4ff70fc98a7fd8d5`
and referee job `bigMac-00005-p04-referee-aac2f3a4fe40`.

I read `source.md`, `problem.md`, `claim.json`, `audit/snapshot.json`, and the
decisive proof `evidence/facet-classification.md`.  In accordance with the
job-specific prohibition, I did not read `checkpoint.md`, even though it is
among the frozen files.  The proof under review is self-contained without it.
Fresh SHA-256 computations for the four consulted frozen files agree with the
snapshot:

- `source.md`: `22a14216f9374c837488416f68108a80987295e36c90137e98e25ff0619a2105`;
- `problem.md`: `88f22196dadb46ba6e1b32cef1ef564958c9ff825e09cd849c95109e4e486d34`;
- `claim.json`: `c10274e3c1d98ceb4f34024d82ac3a672fc48704795fc6b884ceb15a1559d1d1`;
- `evidence/facet-classification.md`:
  `c942a1cadbff1668bd658e148b0c60820077aacbee9aafc652503563591db8e3`.

The exact candidate scope is the full biconditional for every field, every
integer (n\geq 6), and every integer (r\geq0).  I found no silent change of
quantifiers, parameter range, or field dependence.

## Reconstruction of the argument

Put

\[
L=r+2,\qquad U=n-2,\qquad m=n+r=L+U.
\]

First, the graph translation in `problem.md` is correct.  If (a<b) is the
image of a consecutive cycle edge under an increasing injection, the (n-2)
other images must lie outside the open interval between (a) and (b), which
forces (b-a\leq r+1); conversely, that counting inequality permits the
needed images to be placed before (a) and after (b).  A pair is the image
of the wrap edge \(\{1,n\}\) exactly when (b-a\geq n-1), since precisely
(n-2) intermediate images are needed.  Thus nonedges have gaps exactly in
([L,U]), and a face of the independence complex is a set all of whose
pairwise gaps lie in that interval.

Let (S=\{s_0<\cdots<s_q\}), set (g_i=s_i-s_{i-1}), and set
(D=s_q-s_0).  The face condition reduces to (g_i\geq L) and (D\leq U).
The claimed facet criterion

\[
L\leq g_i\leq2L-1,\qquad U-L+1\leq D\leq U \tag{1}
\]

is both necessary and sufficient:

- if an internal gap is at least (2L), inserting a vertex at distance (L)
  from its left endpoint enlarges the face;
- if (D\leq U-L), one can insert (s_0-L) when (s_0>L), and otherwise
  insert (s_q+L\leq U+L=m);
- under (1), an internal insertion would require an old gap at least (2L),
  while an exterior insertion would produce diameter at least
  (D+L\geq U+1).

This also checks the boundary of the ambient interval rather than assuming an
unavailable exterior vertex.  Sums of (q) integers from
([L,2L-1]) fill the entire integer interval
([qL,q(2L-1)]).  Therefore a dimension-(q) facet exists exactly when

\[
qL\leq U,\qquad q(2L-1)\geq U-L+1, \tag{2}
\]

including (q=0).  Hence the facet dimensions form the asserted integer
interval.

### The range (2L\leq U)

Write (U=QL+s), with (Q\geq2) and (0\leq s<L).  Condition (2) always
gives a dimension-(Q) facet.  It gives a dimension-(Q-1) facet exactly
when

\[
(Q-1)(L-1)\geq s+1. \tag{3}
\]

If (3) fails, then
((Q-1)(L-1)\leq s\leq L-1).  Since (L\geq2), this forces
(Q=2) and (s=L-1), or (U=3L-1).  Outside that exceptional family there
are facets in two dimensions, so Cohen--Macaulayness is impossible over every
field by purity.

When (U=3L-1), (2) shows that the complex is pure of dimension two.  The
proof's integral cochain is well-defined on every increasing edge by assigning
value (1) to gaps in ([L,2L-1]) and value (2) to gaps in
([2L,3L-1]).  In any triangle, each consecutive gap is in the first interval
and their sum is in the second, so the coboundary is (1+1-2=0).

The proposed chain

\[
z=[1,L+2]-[2,L+2]+[2,2L+1]-[1,2L+1]
\]

uses four valid edges with gaps (L+1,L,2L-1,2L), respectively.  Direct
boundary cancellation gives \(\partial z=0\), whereas evaluation of the
cocycle gives (1-1+1-2=-1).  If (z) were a boundary, every cocycle would
evaluate to zero on it.  Thus (H_1(\Delta_{n,r};k)\neq0) over every field;
in characteristic two the same pairing is (1\neq0).  Reisner's criterion
therefore excludes Cohen--Macaulayness in this remaining two-dimensional
family.  The arithmetic identity (U=3L-1\iff n=3r+7) is correct.

### The range (2L>U)

If (L<U), condition (2) says that all facets are edges.  The graph is
connected: for every (1\leq i<U), the two valid edges

\[
\{i,i+L+1\},\qquad \{i+1,i+L+1\}
\]

join (i) to (i+1); the inequalities (L+1\leq U) and
(i+L+1\leq L+U=m) verify the endpoints.  Thus vertices (1,\ldots,U) lie
in one component.  Every (j>U) is joined by a gap-(L) edge to
(j-L\in[1,U]).  A pure one-dimensional simplicial complex is
Cohen--Macaulay over a field exactly when it is connected, so this case works
over every field.

If (L=U), then (m=2L) and the complex is the disjoint union of the (L)
edges \(\{i,i+L\}\), hence is not Cohen--Macaulay.  If (L>U), no
two-vertex face exists, and the resulting nonempty zero-dimensional complex
is Cohen--Macaulay over every field.

Finally,

\[
2L>U\iff r\geq\left\lfloor\frac{n-4}{2}\right\rfloor,
\]

while (L=U\iff r=n-4), (L<U\iff r\leq n-5), and
(L>U\iff r\geq n-3).  These cases are exhaustive and yield exactly the
frozen biconditional.  In particular, the (n=6) boundary is covered: the
cases (r=0,1,2,geq3) fall respectively into the nonpure, connected
one-dimensional, disconnected matching, and zero-dimensional cases.

## Independent checks

I also implemented a fresh direct enumeration, used only as a check rather
than as proof.  For all 91 pairs (2\leq L\leq8), (4\leq U\leq16), I
enumerated faces, tested maximality by trying every omitted vertex, and found
exact agreement with (1) and (2).  For every (2\leq L\leq12) with
(U=3L-1), I independently enumerated all triangles, checked the cocycle on
each, checked \(\partial z=0\), and obtained pairing (-1).  For 170 pairs
with (2\leq L< U<2L) (and (L<20)), direct graph traversal found all
(L+U) vertices connected.  All assertions passed.  These finite tests are
corroboration only; the preceding symbolic argument supplies the universal
proof.

## Source comparison, contribution, and gaps

Within the frozen source record, the cited Theorem 3.14 supplies only the
(r\geq n-3) complete-graph range, while the full classification is stated as
Conjecture 3.15.  The candidate adds exact facet classification, proves the
remaining positive one-dimensional range, and supplies purity or integral
homology obstructions for every negative range.  This is precisely the delta
needed to resolve the frozen original claim, rather than a subsidiary or
weakened result.  The source record appropriately limits its literature claim
to a dated search and does not claim guaranteed priority.  This review was
restricted to the frozen evidence and makes no broader novelty assertion.

I found no unresolved mathematical gap, missing parameter case,
characteristic exception, or mismatch between the proof and the frozen scope.

## Verdict

**ACCEPT.**  The candidate proves the original biconditional in its full
quantified scope over every field, and the claimed resolution-level
contribution passes mathematical review.
