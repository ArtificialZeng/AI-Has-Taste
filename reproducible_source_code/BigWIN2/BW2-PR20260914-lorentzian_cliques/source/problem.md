# Precise problem

The immutable original is `source.md` (SHA256
`42cb787665ee3c401f92b773101e4d4daa27d30c0430cb71bae2e410a2393400`).
This project uses its explicitly connected formulation, not the disconnected
wording in the older conjecture display.

For every finite connected simple graph F=(V,E), with n=|V|>=1, decide whether

    F is K_n  iff  for every finite nonempty I and every real symmetric
    A in R^{I x I} with A_ij>=0 and at most one positive eigenvalue,
    Z_{F,A}(x) is Lorentzian.

Here

    Z_{F,A}(x) = sum_{sigma:V->I} product_{uv in E} A_{sigma(u),sigma(v)}
                               product_{v in V} x_{sigma(v)}.

All source vertices share the same spin variables. Assignments are labeled;
there is no factorial normalization. Target diagonal entries and zero entries
are allowed. F has no loops or multiple edges. Empty products equal 1.
Positive eigenvalues are counted with multiplicity.

For a nonzero homogeneous nonnegative polynomial f of degree n>=2, the
Lorentzian condition is: its exponent support S is M-convex, and for every
multi-index beta in N_0^I with |beta|=n-2, the symmetric constant Hessian
of partial^beta f has at most one positive eigenvalue. M-convex means that
for all a,b in S and each i with a_i>b_i, there is j with a_j<b_j and
a-e_i+e_j in S. This is equivalent to the recursive definition in the
primary paper. The zero polynomial and nonnegative homogeneous linear
polynomials are included. The n=1 case is sum_i x_i; zero targets give zero
for connected n>=2.

The unknown direction is: every connected noncomplete F admits an admissible
finite A for which this condition fails. A witness for one nonclique supports
this direction; a nonclique that works for every A would refute it.

## Literature and intended scope

Lee–Oh–Seo, arXiv:2506.13659v2, Section 2 defines the same polynomial and
spectral condition; Theorem 3.1 proves the clique direction. Section 7 gives
the known P3 witness and Conjecture 7.1. Lee–Seo, arXiv:2608.17920v1,
Section 6 explicitly gives the connected conjecture. The later clique-minimizing
inequality is a different statement. Source status: open-supported in these
inspected primary versions; no worldwide novelty claim follows.

Nearest prior result X: clique sufficiency and isolated nonclique witnesses.
Proposed delta Y: an explicit witness construction for a natural infinite
class of connected noncliques, ideally a source-localization lemma.
Verification Z: exact target inertia and a failed support exchange or exact
quadratic derivative inertia. Small tables alone do not qualify.

## Subsidiary claim proposed in research pass 1

The initial target probe and recovery triage are historical evidence. The
immutable original and all of its quantifiers above are unchanged. The
previous two-vertex-deletion next test is now completed by the following
strictly subsidiary claim, submitted for fresh review as a result-note.

For every integer k>=2, let F be a connected simple bipartite graph with
parts L,R of size k whose only maximum independent sets are L and R. This
standard class is called bistable. Set

    A=[[0,1,1],[1,0,1],[1,1,1]], f=Z_(F,A), beta=(k-1,k-1,0),
    c=[x_1^(k-1)x_2^(k-1)x_3^2]f.

Let q(u,v) count the connected components of F-{u,v}, including isolated
vertices. Let s count unordered pairs within L or within R whose deletion
disconnects F. The proposed theorem is

    c = sum_(u in L,v in R) 2^q(u,v) + 2s,
    Hessian(partial^beta f)
      = 2(k!)^2 [[0,1,1],[1,0,1],[1,1,c/k^2]].

It follows that c>=2k^2, with strict inequality exactly when F has a
2-vertex cut. Such F is already 2-connected. Thus the selected Hessian has
two positive eigenvalues exactly when F is not 3-connected; in that case f
is not Lorentzian. The fixed target is admissible, with eigenvalues
-1,1-sqrt(2),1+sqrt(2). For 3-connected F this Hessian has one positive,
one negative and one zero eigenvalue. That equality is a limitation of this
specific derivative, not a claim that f or all universal-target partition
functions are Lorentzian.

The formula includes C_(2k), k>=2, giving c=6k(k-1). For K_(k,k), k>=3,
it gives c=2k^2; K_(2,2)=C4 instead gives c=12. Equality is not confined to
complete bipartite graphs: the cube also gives equality.

The self-contained argument and exact scope are in
`evidence/separator-argument.md`. `evidence/separator-check.py` and its JSON
output verify all 6820 qualifying labeled graphs in the exhaustive fixed-part
domain k=2,3,4, and 22 structured cases up to k=7. Those finite checks are
supporting evidence rather than an infinite proof or independent audit.

Known background, including bistability and biconnectivity, is attributed in
`literature/separator-comparison.md`. The proposed delta is the coefficient
formula and its sharp derivative obstruction for a structural infinite
class. No equivalent was found in the inspected primary statements; priority
and significance remain provisional pending fresh review.

Complete primary HTML captures supporting the original conventions and
connected conjecture are bound locally as
`evidence/external/2506.13659v2.html` and
`evidence/external/2608.17920v1.html`; `evidence/source-bindings.json` records
byte-for-byte copying from the supervisor's primary captures. The independent
proof does not require unavailable optional PDFs.

The global connected-clique characterization remains unresolved. No
mathematical acceptance, manuscript, or released PDF is claimed.

One next test: a fresh referee should independently check the two-vertex
coefficient identity, especially the same-part deletion with singleton
components, and its exact Hessian inertia/equality criterion against the
bound evidence and cited prior results.
