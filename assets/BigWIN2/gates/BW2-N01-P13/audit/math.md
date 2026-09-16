# Mathematical referee report

**Verdict: accept the exact frozen candidate.**

Job: `newwin-00001-p13-referee-2c5006881c02`.
Snapshot digest: `83424893dbe79ac62570cb8872367e3214fedd92702526faa64aab6e96f471b7`.
Review date: 2026-09-12. Candidate kind: `resolution-paper`.
Frozen original status: `proved`.

The argument establishes nonnegativity of the quadratic residue coefficient
for every square board, every size n >= 1, and every hit index 0 <= d <= n,
with the all-prime-power congruence interpretation in `source.md` and
`problem.md`. This acceptance does not replace the statement by an n <= 4
claim. The finite computation is sufficient because the submitted universal
locality argument is valid. No substantive claim revision was made in this
review, and no mathematical gap remains identified in the frozen proof.

## Scope and integrity

I read the original source, interpretation, claim, snapshot, the listed proof
and computational evidence, and the cited primary results. I did not read an
owner checkpoint, scheduling state, earlier audit, or job transcript. This is
a fresh referee context using the supplied job identity; it is not external
journal peer review or a formal proof-assistant certification. No agents or
other model processes were used.

All 27 snapshot file hashes and the canonical digest of the file mapping were
checked at the beginning and end of the independent computation. Every hash
matched. `source.md`, `problem.md`, `claim.json`, the snapshot and its evidence
were left unchanged. Source SHA-256:
`0c3d6a331f21956d134bb27a6ff8976d1803f2b3f2496bef501535f72df0d9aa`.

The residue is an integer congruence on the unbounded set of prime powers
q=x+1, not an assumed Taylor expansion of a globally polynomial counting
function. Uniqueness follows by dividing a difference of degree at most two
by x^3: an integer tending to zero is eventually zero. Existence is supplied
by the cited residue theorem and is also sufficient for the coefficient
manipulations used here.

## Reconstruction of the decisive argument

Write z=t-1 and h_n(B;t)=per(J+zB). Its t coefficients count permutations by
their number of entries in B, so they are nonnegative integers. In balanced
restriction convolution, both row and column sets split into subsets of the
same size. Associativity and commutativity follow from ordered disjoint
partitions of the two vertex sets. A permutation counted in
h*((-1)^n h) has binomial(n,k) decompositions at size k, giving the binomial
cancellation and the claimed inverse of h.

If E multiplies degree n by n and L=z*d/dz, both are derivations of this
convolution. The identities Eh=h*U and Lh=h*V are obtained by marking one
permutation edge, with U_1([b])=1+zb and V_1([b])=zb. It follows that E or L
raises the support bound of a convolution kernel by at most one. Scalar
multiplication in Q(z) leaves the support bound unchanged. The submitted
operators apply their rational scalar factors after differentiation; they do
not incorrectly commute those factors through L.

For an exact support, a connected component having r rows, c columns and
rank D contributes x^(r+c-D-1) times its diagonal-orbit count. Ranks and
defects add over components. Since D <= min(r,c), its defect is at least
max(r,c)-1. Defect zero occurs only for a single nonzero edge, with orbit
count one. Components with more than three vertices on either side make no
contribution modulo x^3.

Fix an actual labelled collection of k nonedge components, with total row
count r, column count c, rank D and defect e=r+c-D-k. A coefficient of order
a <= 2 can receive its contribution only when e <= a. Each of these k
components has defect at least one, so k <= e and

    s = r+c-D = e+k <= 2a.

The remaining support is an arbitrary matching outside all the core's rows
and columns. Therefore, after the ordinary rook-to-hit weighting, this core
contributes a scalar multiple of

    z^D sum_j r_j(B outside the core) (n-D-j)! z^j.

No factorial with a negative argument occurs: D <= min(r,c), and a matching
outside the core has j <= min(n-r,n-c) <= n-D. Ranks have been specified on
the components, and the core is counted as an actual support, rather than
once for each isomorphism, so there is no missing automorphism divisor.

Here is the crucial patch decomposition. Delete any D core rows and any D
core columns. On the remaining square set of n-D rows and columns, put
weight 1+zB_ij when both endpoints are outside the core and weight 1
otherwise. Expanding the permanent in marked B entries gives exactly the
preceding factorial sum. The retained core vertices are dummy vertices.
If a permutation on this auxiliary matrix has u dummy-to-dummy edges,
include in its patch all core vertices and the outside endpoints of every
edge touching a dummy. The patch has

    r + (c-D-u) = c + (r-D-u) = s-u

vertices on each side. Every outside vertex added to this patch is already
used by an edge touching a dummy. Consequently all remaining permutation
edges have both endpoints in the complementary row/column sets, and form
an unrestricted permutation there. This proves the required factorization
into a local patch weight and the complementary h polynomial.

Conversely, the core, deleted vertex sets, the partial permutation touching
dummy vertices, and any complementary permutation reconstruct a unique
auxiliary permutation. The patch contains no unused outside vertex. Thus
the decomposition is bijective and introduces no ambient-size dependence
or overcounting. Averaging over the positive number
binomial(r,D)*binomial(c,D) of deletion choices is legitimate: each choice
has the same rook expansion, and the average makes the local rule invariant
under row and column relabelling. This factor depends on the core, not on
the ambient board. Cases s>n are harmless: a permutation can then occur
only with enough dummy-to-dummy edges to keep s-u <= n.

It follows that the transformed rook residue F[a] has a convolution kernel
supported at sizes at most 2a; in particular F[0]=h. The argument allows
signed orbit coefficients, so no unproved positivity assertion has entered
this locality step.

The ambient q-hit transform has the submitted expansion (5). It follows
by multiplying the expansions of the q-factorial and the factors
t(1+x)^(-j)-1. The polynomials a(n,i), I(i) have total degree at most two;
b(n,i), J(i)-a(n,i)I(i), K(i) have total degree at most four. Substituting
E and L for n and i yields exactly equation (6). Its three terms have
locality bounds 4, 2+2 and 0+4. Hence

    K[2] = h^(-1) * C[2]

vanishes identically in every size greater than four, for every board.

There is no arithmetic-congruence problem from negative q powers. In the
original transform each entire weight can be written as the integer
polynomial

    q^(binomial(n,2)-binomial(i,2)) [n-i]!_q
        product_{j=0}^{i-1}(t-q^j).

Its exponent is nonnegative because i <= n. Replacing M_i by its integer
residue therefore preserves congruence modulo x^3 for every prime power.
The rational expressions in z are only an intermediate algebraic device.
The inverse convolution has integer-polynomial values because C[2] and h
do, so no singular specialization at t=1 is needed.

At size zero C[2]=0 by the auxiliary convention, and at size one the hit
polynomial is independent of q, so K[2,1]=0. The remaining finite kernels
at sizes 2,3,4 were independently verified to be coefficientwise
nonnegative, as detailed below. Thus the submitted identity (7), convolving
these kernels with h, proves the original inequality for every n and d.

## Independent exact computation

The new standard-library verifier `audit/referee_verify.py` imports none of
the submitted computational modules. It was executed successfully with
assertions enabled:

    python3 audit/referee_verify.py

Its durable results are `audit/referee_verification.json`, and its fresh
labelled orbit table is `audit/referee_orbits.json`.

The verifier enumerates all 253 connected labelled support graphs with
1 <= r,c <= 3, without quotienting the enumeration by symmetry. It fixes a
spanning tree starting from the last vertex, counts ranks by explicit
minors, and uses exact rational Vandermonde elimination to reconstruct
orbit polynomials. It checks every graph over fields of sizes
2,3,4,5,7,8,11,13, totaling 83,919 normalized assignments. The two extension
fields use the irreducible polynomials u^2+u+1 and u^3+u+1. Every reconstructed
polynomial agrees with the frozen orbit data, and the 28 submitted classes
cover precisely the fresh labelled enumeration.

The interpolation is justified, rather than assumed: the cited small-board
result gives polynomiality of the orbit count, and spanning-tree
normalization bounds it between 0 and x^beta, where
beta=number of edges-r-c+1 <= 4. Its polynomial therefore has degree at most
beta on the unbounded prime-power domain. The first beta+1 distinct field
sizes determine it exactly; the remaining field sizes are extra checks.

The verifier then recomputes every exact-support residue, sums over
supports by a subset transform, and evaluates the integral hit-weight form
above. It calculates each classical hit polynomial by direct permutation
enumeration. It obtains the quadratic kernel using the direct alternating
inverse h^(-1)*C[2], instead of the submitted kernel recursion.

| n | Boards | Quadratic kernel coefficients | Minimum | Maximum | Negative |
|---|---:|---:|---:|---:|---:|
| 1 | 2 | 4 | 0 | 0 | 0 |
| 2 | 16 | 48 | 0 | 1 | 0 |
| 3 | 512 | 2,048 | 0 | 41 | 0 |
| 4 | 65,536 | 327,680 | 0 | 162 | 0 |

All 989,340 constant/linear/quadratic hit residue entries and all 329,780
quadratic kernel entries agree with the frozen archives. These comparisons
cover all 66,066 boards of sizes 1--4. The new size-four kernel stream digest
is `ec74936ef83f8d6fb5024cf0bc2f48a814d5cec77d551ace24b10d8400c2e872`.
Nonnegativity was checked directly on the new coefficients, not inferred
from a digest or a submitted success flag.

Two additional checks were performed. First, 2,907 coefficients in the
submitted ambient-weight expansion were compared with direct integral
product expansion for every 0 <= i <= n <= 16. Second, every n by n matrix
over F_2,F_3,F_4 was enumerated for n=1,2,3, totaling 282,701 matrices.
Gaussian elimination, different from the orbit minor calculation, gave
6,300 exact support/rank-count comparisons with zero discrepancies. These
are exact counts, not just congruences modulo one at q=2.

The submitted supplementary tests on larger boards are not needed for
acceptance and were not rerun. Neither those finite tests nor the new
small-board checks substitute for the universal locality proof above.

## Sources and contribution

The nearest prior result is Jeffrey Chen and Jesse Selover, *Positivity
properties of q-hit numbers in the finite general linear group*, ECA 6:3
(2026), S2R22, DOI 10.54550/ECA2026V6S3R22. The frozen
[primary journal source](https://ecajournal.haifa.ac.il/Volume2026/ECA2026_S2A22.pdf)
was checked at equation (3.2), Remark 2.3, Theorem 3.12, Corollary 3.13,
Conjecture 4.1, Theorem 4.10 and Section 5. The stated dependencies match
those results: orbit decomposition, small-board polynomiality, and integer
residue existence. The established universal positivity theorem treats
the linear coefficient. Section 5 explicitly discusses the still-needed
quadratic calculation. The balanced convolution reduction and its positive
quadratic kernels are a substantive delta from this prior work, with the
direct use of settling the frozen quadratic question.

I also re-extracted text from the frozen PDF with `pdftotext -layout`.
It is byte-identical to the frozen text, SHA-256
`1bf0d52bd590b5b34d1c530af082a49403e5adbad296fcf5fd42a1607af3249d`;
the extracted copy is `audit/referee_primary_extract.txt`.

The live [arXiv record](https://arxiv.org/abs/2504.09300) was inspected on
2026-09-12 and listed only v1, dated 12 April 2025. Its abstract states
linear positivity. Bounded fresh searches included the exact query strings
`"q-hit" "quadratic" positivity`, `"q-hit" "locality"`,
`"Positivity properties" "q-hit" Chen Selover quadratic`,
`"matrix" "q-hit" "quadratic coefficient"`, and
`"quadratic positivity" "hit numbers"`. No equivalent primary-source
quadratic theorem or locality proof was identified. Search snippets were
not used as mathematical dependencies. The live journal PDF request
returned an internal error; the complete frozen primary PDF was available
and verified as described above. The novelty assessment is limited to
these inspected sources and searches and does not certify historical
priority or journal acceptance.

## Disposition

Scope, correctness, computational evidence, and contribution pass. No
unresolved mathematical repair is required for the frozen candidate.
The accepted result is the universal quadratic inequality and its stated
local-kernel identity; it asserts neither global polynomiality nor
positivity of higher residue coefficients. Subsequent drafting should
retain the explicit patch bijection, the interpolation justification,
the reproducible finite certificate, and these literature limits.
The next workflow step is the runner's structural `check-math`, followed
by manuscript preparation at exactly this accepted scope.
