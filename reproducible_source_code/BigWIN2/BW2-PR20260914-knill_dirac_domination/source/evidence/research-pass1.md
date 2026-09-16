# Reproducible research evidence, pass 1

Job: `primary-20260914-knill-dirac-domination-research-6e957123a5e9`.
Date: 2026-09-14. Primary proposed result:
`graph-domination-proof.md`. This dossier is supplementary and does not
replace that argument or a fresh referee.

## Five-vertex census: complete finite scope

Run from the project root:

```
OPENBLAS_NUM_THREADS=1 python3 evidence/five_vertex_census.py
OPENBLAS_NUM_THREADS=1 python3 evidence/certify_five_vertex.py
```

A face is a nonzero five-bit integer. A complex mask uses bit (face-1) for
membership. Thus the saved masks reconstruct every face without an external
catalogue. Unused vertices are permitted; embeddings in the five-vertex
universe are counted separately.

The first generator decides faces in increasing cardinality. It always
allows exclusion, and allows inclusion precisely when all codimension-one
nonempty subfaces have been included. Those subfaces precede the face, so
induction gives downward closure. Conversely, every downset has exactly one
sequence of these membership decisions. This proves completeness and no
duplicates without relying on a precomputed count.

The second generator recursively chooses increasing-index pairwise
incomparable facets and takes all their nonempty subsets. Every finite
downset is the closure of its unique maximal-face antichain, so this is
another complete, duplicate-free enumeration. The two actual output sets
were asserted equal: 7,580 masks, of which exactly one is empty.

All 7,579 nonempty complexes and their 113,716 admissible partial sums were
screened in float64. No negative candidate appeared. The minimum observed
gap was 0.9999999999999996; the minimum over 2<=k<n was
1.9999999999999991. Numerical values near integers are not exact equality
certificates.

The full group of 120 vertex permutations splits this domain into 208
orbits. The code checks orbit membership and total size. A vertex relabeling
permutes the connection basis and induces an orthogonal signed permutation
on oriented face chains. Thus the spectra of both matrices, and every gap,
are constant on each orbit. This justifies certifying one representative.

`certify_five_vertex.py` reconstructs every representative's matrices by an
independent tuple/subset implementation, checks downward closure and d^2=0
over integers, computes integer characteristic polynomials, and isolates
their real roots with rational endpoints of width at most 10^-9.
Multiplicities are expanded in decreasing order. For each k it subtracts
the sum of the upper Dirac endpoints from the sum of the lower connection
endpoints. All these rational lower bounds are positive. The smallest is
1583407980/1583407981. Coefficients, matrices, intervals, and lower bounds
are saved in `five-vertex-exact.json`.

This establishes the original inequality on the finite five-vertex domain.
It does not establish an infinite-dimensional theorem, an additive-one
certificate for every five-vertex complex, or a publishable finite census.
It is exact symbolic computation using SymPy, without a separate referee.

## Checks chosen after the graph statement was fixed

Run:

```
OPENBLAS_NUM_THREADS=1 python3 evidence/graph_proof_checks.py
```

The code records the SHA-256 of the already-written proof. All simple graphs
on each full labeled vertex set of size 1 through 6 are visited by edge-mask
enumeration: 33,867 graphs, 453,098 partial sums, including 5,604 bipartite
and 28,263 non-bipartite examples. This range was not used to design the
graph theorem. It is an adversarial implementation check from the same
researcher/context, not independent confirmation in a statistical or
refereeing sense.

Exact integer checks compare the face-intersection matrix with the block
formula, verify Q+H=2 Delta and the bipartite conjugation, and check the
endpoint entrywise bound. Float64 checks (tolerance 10^-6) compare the entire
computed positive connection spectrum with f(Q), confirm Dirac zero padding,
test both variational inequalities and every lower bound in the proof,
and screen the asserted additive-one conclusion. All passed.

Thirty-two specified larger or structured tests include paths, odd and even
cycles, stars and matchings at orders 7,8,15,16,31,32; complete graphs at
orders 7,10,16; complete bipartite graphs with part sizes (2,9),(3,8),(8,8),
(16,16); and a disjoint union of an odd cycle, a path, an edge and four
isolates. The largest matrix has 288 faces. All tests passed.

Seven small named cases additionally satisfy the exact characteristic-polynomial
identity

\[
\det(xI_{v+e}-L)=(x+1)^{e-v}
\det((x^2-1)I_v-xQ),
\]

with exact cancellation when e<v. Their matrices and polynomials are saved
in `graph-proof-checks.json`. The single-edge case verifies the claimed
sharpness example exactly. These checks supplement the uniform SVD proof;
floating-point tests have not been relabeled as exact spectral certificates.

## Scope and useful failure diagnosis

The initial unstructured five-vertex counterexample search was all-positive.
It was not expanded without a structural reassessment. The signed/unsigned
distinction in the graph block form then led to the proposed theorem.
Directly substituting signed H into the unsigned hydrogen relation is not
justified outside bipartite graphs; the proof explicitly uses a different
degree-and-cycle argument there. No impossibility theorem for other proof
methods is claimed. No larger-dimensional proof or counterexample was found.

The candidate requests fresh scrutiny of the graph theorem's spectral
multiplicities, min-max directions, non-bipartite step, all-k coverage, and
literature value. No manuscript, acceptance report, or hidden worker was
created in this pass.
