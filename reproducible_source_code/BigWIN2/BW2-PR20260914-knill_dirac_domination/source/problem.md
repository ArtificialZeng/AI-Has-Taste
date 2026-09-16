# Precise problem: connection–Dirac partial-sum domination

Original input: `source.md`, retained byte-for-byte; SHA-256
`090d0d1a2566ee0740d33fd1791b7e36c2778e5122f1ca41d48aaf008101ae83`.
Triage date: 2026-09-14. Job:
`primary-20260914-knill-dirac-domination-triage-809fb2a0f8af`.

Let (V) be any finite set and let (G\subseteq 2^V\setminus\{\varnothing\})
be a family such that (x\in G) and (\varnothing\ne y\subseteq x) imply
(y\in G). Remove unused vertices without changing (G), and set (n=|G|).
Faces, rather than vertices, index the matrices. There are no assumptions of
connectedness, purity, bounded dimension, flagness, or a geometric realization.

Choose a total order on the vertices and orient every face by that order. For
(x=(v_0<\cdots<v_p)), define the real (n\times n) matrix

\[
d_{x,y}=\begin{cases}(-1)^i,&p\ge1,\ y=x\setminus\{v_i\},\\0,&\text{otherwise.}\end{cases}
\]

This is the exterior derivative convention (rows are larger faces); its
transpose is the boundary convention and gives the same (D=d+d^{\mathsf T}).
The complex is unaugmented: the empty face has no matrix index. Define

\[
L_{x,y}=\mathbf1_{x\cap y\ne\varnothing},\qquad D=d+d^{\mathsf T}.
\]

For any real symmetric (n\times n) matrix (A), order its eigenvalues with
multiplicity as (\lambda_1(A)\ge\cdots\ge\lambda_n(A)) and put
(S_k(A)=\sum_{j=1}^k\lambda_j(A)), with (S_0(A)=0).

**Frozen assertion.** For every such finite (G) and every integer
(1\le k\le |G|),

\[
S_k(L_G)\ge S_k(D_G).
\]

For (G=\varnothing) there is no admissible (k). The assertion concerns
eigenvalues, not singular values or squared eigenvalues. Reorienting faces
conjugates (D) by a diagonal matrix with entries (\pm1), so its spectrum is
unchanged; reordering faces conjugates both matrices by a permutation matrix.

## Interpretation and current source status

The frozen input quotes Knill's awkward wording involving (L-D). Its displayed
comparison, and the explicit instruction in `source.md`, fix the assertion
above. It is neither positive semidefiniteness of (L-D) nor a claim about
(S_k(L-D)). No correction to `source.md` has been made.

Live inspection of [Knill, arXiv:2601.18071v2](https://arxiv.org/html/2601.18071v2)
confirms the definitions in Section 1.1, decreasing spectral sums in Section
5.1, Conjecture 1 in Section 5.3, and the incidence code in Section 8.1.
The source reports printed p.9 for Conjecture 1; this worker verified the HTML
section location, not the PDF pagination. The
[version history](https://arxiv.org/abs/2601.18071) lists v2 dated 29 July 2026.
**Source status: open-supported within the inspected sources and bounded
search on 2026-09-14.** This is not an exhaustive priority or open-status claim.

Section 10.3 already attributes an inverse-matrix counterexample on the
two-skeleton of the five-vertex simplex to Robert J. George. It is a different
assertion and is not a new contribution here. The author's
[August 2025 post](https://www.quantumcalculus.org/connection-and-dirac-matrix/)
already proposes the stronger gap (S_k(L)\ge S_k(D)+1); that strengthening
would also be a rediscovered conjecture, not a new conjectural contribution.

## Nearest baseline, proposed delta, verifier

Nearest established tools are the variational characterization of spectral
sums and elementary matrix comparison. Direct arguments in
`evidence/baseline.md` give (S_1(L)\ge S_1(D)+1),
(S_n(L)-S_n(D)=n), and preservation under disjoint union. In dimension one,
Knill's [hydrogen identity](https://arxiv.org/abs/1803.01464) concerns the
**unsigned** incidence matrix and does not immediately compare every partial
sum with the signed Dirac spectrum. No full resolution follows from the
standard tools checked in this triage.

Proposed delta: an exact counterexample to the frozen universal comparison,
with a first search over all complexes on a five-vertex universe and all
intermediate (2\le k<n). This is a proposed resolution route, not an asserted
counterexample or new theorem. Verification: list every face, reconstruct
integral (L,D), compute exact characteristic polynomials, isolate their real
roots over the rationals with multiplicities, and certify
(\sum_{j\le k}\sup I_j(L)<\sum_{j\le k}\inf I_j(D)).
Numerical screening alone cannot resolve the source assertion.

The next census should recursively decide faces in increasing cardinality,
allowing a face only when all its nonempty proper faces are already present;
this avoids iterating over (2^{31}) arbitrary families. Negative candidates
require exact certification. An all-positive finite census is search evidence,
not a publishable contribution by itself.

## Triage evidence and deduplication

`evidence/tiny_complexes.py` exhaustively checks all 18 nonempty complexes
contained in a three-vertex universe using exact root intervals (all (k)
strictly positive gaps), and numerically screens all 166 nonempty complexes
contained in a four-vertex universe plus 29 specified structured cases.
`evidence/tiny-complexes.json` records the matrices and rational certificates
for the exact tier, and the faces and floating-point gaps for the numerical
tier. No negative numerical candidate was found; this makes no assertion
about larger complexes.

The current historical registry contains 692 entries. The independent scan
and inspected normalized neighbors are recorded in `evidence/registry-screen.json`;
none compares these two operators or their partial sums. The supervisor's
separate Excel comparison in `literature/dedup.json` is attributed evidence:
this worker did not independently access its Windows payloads or live chats.

Historical triage decision: **advance** to one bounded research test; candidate
kind **none**, original workflow status **unresolved**.

## Research pass 1: proposed partial theorem

Job: `primary-20260914-knill-dirac-domination-research-6e957123a5e9`.
The frozen universal assertion above and `source.md` remain unchanged.
The proposed **result-note** has the following strictly smaller scope:

For every nonempty finite abstract simplicial complex G whose faces all have
cardinality at most two, and every 1<=k<=|G|,

\[
 S_k(L_G)\ge S_k(D_G)+1.
\]

The constant 1 is sharp, already for a single edge at k=1. Disconnected
complexes, isolated vertices, and non-bipartite graphs are included. A graph
with a triangle here has only its vertices and edges; no filled triangle is
implicitly added. The original claim for arbitrary dimensions is unresolved.

`evidence/graph-domination-proof.md` gives the complete proposed argument.
For k up to the number of vertices it diagonalizes the unsigned incidence
block formula for L, uses signed/unsigned conjugacy only for bipartite graphs,
and uses degree majorization with an odd-cycle Rayleigh bound otherwise.
A trace/rank estimate handles all later partial sums. This is a uniform
proof candidate, not an inference from a census. No known gap was identified
by the proposer; fresh correctness and contribution review is required.

The assigned five-vertex search also completed: 7,579 nonempty labeled
complexes, 208 isomorphism classes, all k certified strictly positive using
integer characteristic polynomials and rational root intervals. These data
and their completeness argument are indexed in `evidence/research-pass1.md`.
They are finite supplementary evidence, not the proposed contribution.

`literature/research-verification.md` compares the candidate with current
primary material. The additive-one conjecture is already the author's 2025
proposal; the proposed delta is its proof for every graph complex. No
equivalent graph proof was found in the inspected sources and bounded search
on 2026-09-14, without a claim of exhaustive priority verification. The known
unsigned hydrogen identity is derived directly in the needed spectral form,
not presented as new or silently applied to signed incidence.

The decisive original primary HTML and its existing text extraction are
archived as `evidence/external/knill-2601.18071v2.html` and
`evidence/external/knill-2601.18071v2-local-text.txt`, respectively.
They are included in the proposed claim's evidence binding. No manuscript
or mathematical acceptance is authorized by this research decision.
