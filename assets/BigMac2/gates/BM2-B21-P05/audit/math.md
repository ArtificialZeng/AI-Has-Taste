# Fresh mathematical referee report

## Frozen scope and review boundary

I reviewed the `resolution-paper` claim frozen by snapshot digest
`9e7842d90ed58979a2ede4784ab0fc050c002d8ad19c4f615af4742d6e1ba13f`:
for the graph on `[3]^3` in which two vertices are adjacent exactly when they
differ in one coordinate, every color must be used and every vertex must have
at least three same-color neighbors, and the claimed maximum number of colors
is four.  I reconstructed the argument from `source.md`, `problem.md`, and the
decisive proof and computation files named by the snapshot.  As required by
the job boundary, I did not read `checkpoint.md`.

The primary-source PDF mentioned in `source.md` is not a snapshot-listed
evidence file, so I did not inspect it.  The source comparison below is
therefore limited to the frozen account in `source.md`; this report makes no
claim of priority beyond that account.

## Reconstruction of the proof

A color class `S` is nonempty by surjectivity.  The same-color-neighbor
condition is exactly

\[
\delta(H(3,3)[S])\mathrel{\geq}3.
\]

I first checked the local graph facts used to bound `|S|`.  If adjacent
vertices `x,y` differ in coordinate `i`, a common neighbor cannot differ from
`x` in another coordinate, since it would then differ from `y` in two
coordinates.  It must agree with both outside `i`, and its `i`-th coordinate
is the unique third value.  Thus every adjacent pair has exactly one common
neighbor.  Also, the six neighbors of any vertex split into three pairs by
the changed coordinate; vertices in a pair are adjacent and vertices in
different pairs are not.  Hence every clique has order at most three.

Now let `S` have induced minimum degree at least three.  Sizes at most three
are immediately impossible.  At size four the induced graph would be `K_4`,
contradicting the clique bound.  At size five, its complement has maximum
degree at most one, so its missing edges form a matching.  With zero or one
missing edge, four vertices induce `K_4`.  With two missing edges `ab` and
`cd`, the fifth vertex `e` is adjacent to `a`, and both `c` and `d` are common
neighbors of `e,a`.  This contradicts the unique-common-neighbor fact.
Therefore every color class has at least six vertices.

If a coloring has `p` colors, its nonempty classes partition all 27 vertices,
so `6p <= 27` and hence `p <= 4`.  This directly excludes every larger `p`;
no monotonicity or merging assumption is needed.

For the reverse inequality, the four sets

\[
C_0=\{1\}\times[3]\times[3],\qquad
C_j=\{2,3\}\times\{j\}\times[3]\quad(j=1,2,3)
\]

are nonempty, pairwise disjoint, and cover `[3]^3`.  A vertex of `C_0` has
the four class-neighbors obtained by changing its second or third coordinate.
A vertex of `C_j` has the one class-neighbor obtained by changing its first
coordinate and the two obtained by changing its third coordinate.  Their
induced degrees are therefore respectively four and three.  Assigning a
distinct color to each set is a surjective valid four-coloring, so `p >= 4`.
Together the two bounds prove the frozen equality.

## Independent checks and attacks

I performed a fresh exact check using a separately written 27-by-27 Boolean
adjacency matrix, rather than importing the submitted verifier.  It found 27
vertices, ambient degree six, 81 edges, and exactly one common neighbor for
each of the 81 adjacent pairs.  Exhausting all subsets of sizes one through
five gave zero subsets with induced minimum degree at least three; the maximum
induced minimum degrees at those sizes were `0,1,2,2,2`.  The proposed four
classes formed an exact cover of sizes `9,6,6,6`, with induced degree sets
`{4},{3},{3},{3}`.  I also reran `evidence/verify_resolution.py`; its output
matched `evidence/verify_resolution.out` byte for byte.

The proof has no limiting operations, division, compactness assumptions,
external theorem hypotheses, or computationally approximate steps.  The
potential edge cases are accounted for: surjectivity makes every class
nonempty, the weak threshold allows equality at three, and the construction
uses all four colors exactly as required.

## Source comparison, contribution, and verdict

The frozen `source.md` reports only the bounds `3 <= bar_chi_>= <= 5` and poses
the equality with four as an open problem.  Relative to that frozen baseline,
the candidate supplies both missing bounds and settles the original claim at
its full stated scope by a short self-contained argument.  This is a
substantive resolution, not a restriction or subsidiary result.  Verification
of the external bibliographic/open-status attribution remains outside this
snapshot-bounded mathematical review.

**Verdict: accept.**  The exact frozen `resolution-paper` claim is proved;
scope, correctness, evidence, and contribution all pass.  I found no
mathematical gap requiring revision.
