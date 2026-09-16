# Mathematical referee report

## Frozen scope and integrity

I reviewed the exact `result-note` claim bound to snapshot
`aaf9ac5e9000085b347226c33f5a8e8145d705fd861e6455d55c881d864cbb50`.
All five recorded file hashes match the snapshot.  The claim is explicitly a
subsidiary obstruction for a 13-layer, four-vertices-per-layer model; it does
not purport to settle the frozen unrestricted `K_7`-free diameter conjecture,
whose status therefore remains unresolved.

## Reconstruction of the reduction

Write the layer sizes as `c_0,...,c_12` and rotate the unique boundary with
sum at least seven to `{0,1}`.  Since every size is in `{1,2,3,4}`, reflection
reduces its ordered sizes to `3+4` or `4+4`.  A clique in this 13-cycle locality
model is contained in one layer or in two consecutive layers.  Consequently,
completing all allowed edges away from `{0,1}` cannot create a `K_7`, because
every other consecutive-layer union has at most six vertices.  Edge completion
only enlarges weighted open neighborhoods, so a lower bound for the completed
graph is a lower bound for the original graph.

For a `3+4` junction, an edge-maximal admissible completion is `K_7` with one
edge deleted.  Under permutations within the two layers, the deleted edge is
inside the 3-layer, inside the 4-layer, or crossing.  For a `4+4` junction, let
`F` be the missing-edge set in `K_8`.  The graph is `K_7`-free exactly when for
each vertex some edge of `F` avoids that vertex, equivalently when the edges of
`F` have empty common intersection.  An inclusion-minimal such family is
either two disjoint edges or the three edges of a triangle.  The program
enumerates all 266 labeled families of these two forms and verifies that their
orbits under `S_4 x S_4` are exactly the ten listed representatives.  Thus every
permitted junction is a subgraph of one of the tested completions.

It is also sound to retain only coordinatewise-maximal ordinary layer-size
patterns.  Increasing an ordinary layer without violating the one-high-boundary
condition and assigning weight zero to each new vertex preserves feasibility:
the new vertex sees the old neighborhood of an existing same-layer vertex,
as well as that old vertex.  Hence the minimum total feasible weight cannot
increase under such an enlargement.  A pattern is maximal precisely when each
ordinary coordinate below four is incident with an ordinary boundary of sum
six.  Direct enumeration gives 60 anchored `3+4` patterns and 51 anchored
`4+4` patterns; reflection fixing the high boundary reduces the latter to 30.
The ten topology types are closed under the induced layer swap, so this
reflection reduction loses no topology-size pairing.  The resulting total is
`60*3 + 30*10 = 480` cases.

## Exact optimization check

For each completed adjacency matrix `A`, the relevant primal program is
`min 1^T w` subject to `Aw >= 1`, `w >= 0`; its dual is `max 1^T y` subject to
`A^T y <= 1`, `y >= 0`.  I checked the implementation against these programs,
including cyclic adjacency, junction labels, symmetry actions, and the
direction of the dominance and dual inequalities.  Although HiGHS discovers
candidate dual vectors numerically, every coordinate is converted to a
rational number and nonnegativity, every dual inequality, and the objective
bound are then asserted using `fractions.Fraction`.  Thus successful execution
provides exact rational lower-bound certificates rather than relying on the
floating-point optimum.

I reran the frozen program successfully.  It regenerated the stated pattern
and topology counts and exactly checked all 480 certificates.  The least value
among the checked feasible duals was `4154/851`, attained for sizes
`(3,4,2,3,3,3,3,3,3,3,3,3,3)` with the missing edge inside the 3-layer.
The claimed strict comparison is exact:

`4154/851 - 39/8 = 43/6808 > 0`.

Taking the minimum of the 480 certified dual objectives proves the asserted
uniform lower bound for the entire reduced class, and the preceding completion
and dominance arguments lift it to every graph in the frozen claim.

## Contribution and limits

The nearest prior result identified in the frozen dossier is the even-case
layered construction for `r >= 4`; the supplied problem statement records that
it does not settle the `r=3` (`k=6`) boundary.  The present theorem supplies a
precise, exact obstruction at that boundary: within the stated four-slot
13-layer model, any prospective mass witness must use at least two high
boundaries.  This is a nontrivial finite classification and exact LP-certificate
result with a credible use in narrowing the proposed counterexample route.
No claim of exhaustive bibliographic priority is justified by the supplied
snapshot; that limitation does not affect the theorem's mathematical validity
or its honestly stated subsidiary scope.

The result gives no information about two-or-more-high-boundary patterns,
larger layers, nonlocal edges, or arbitrary `K_7`-free graphs.  Those are limits,
not gaps in the submitted theorem.  I found no missing case, quantifier defect,
degenerate-weight problem, or unsupported numerical inference within the exact
frozen scope.

## Verdict

**Accept.**  The precise result-note claim is proved, its strict bound is backed
by exhaustively checked exact rational dual certificates, its relationship to
the unresolved original problem is explicit, and its contribution is substantive
within the identified layered-construction program.
