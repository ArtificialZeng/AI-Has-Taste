# Precise frozen problem and proposed resolution scope

Provenance: interpretation fixed at triage; research update
newwin-00001-p08-research-23519ac79811, 2026-09-12.
The verbatim original remains in immutable source.md (SHA256
`e6b61e96d2298cfd85d301038ae9142fc908f4efaee7c7ab1638993c5cbf7696`).
No correction or weakening is proposed.

For every integer m>=2 and n>=1, let D_m(n) consist of words
D=d_1...d_L in {N,E}, with L=(m+1)n, exactly mn letters N and n letters E,
and, for every prefix length 0<=r<=L,

    #{i<=r : d_i=N} >= m #{i<=r : d_i=E}.

Equivalently these are N=(0,1), E=(1,0) paths from (0,0) to (n,mn)
that stay in y>=mx. Define

    pk(D)  = sum_(i=1)^(L-1) 1{d_i d_(i+1)=NE},
    nne(D) = sum_(i=1)^(L-2) 1{d_i d_(i+1) d_(i+2)=NNE}.

These are consecutive factors, with every starting position counted.
They are not subsequences or cyclic occurrences. In particular, each
maximal north run of length at least two contributes one NNE occurrence.
For every integer 1<=k<=n set

    W^(m)_(n,k)(t) = sum_(D in D_m(n), pk(D)=k) t^nne(D) in Z[t].

The frozen assertion is: for every such triple (m,n,k), every complex alpha
satisfying W^(m)_(n,k)(alpha)=0 belongs to R. Repeated roots and zero roots
are allowed. The polynomial is nonzero: the valid word
N^(mn-k+1) E (NE)^(k-1) E^(n-k) has exactly k peaks. In fact every
nonempty valid path begins with at least m north steps, so nne(D)>=1;
t=0 is necessarily a root. The auxiliary empty path has weight 1 only
when constructing a generating function; n=0 is outside the source claim.

Keep the given rectangular orientation and the fixed peak condition.
The ordinary m=1 theorem is a comparison result outside the assigned range.
An exact counterexample must use legitimate coefficients from this domain
and certify a nonreal root; finite successful checks do not prove universality.

Source status: **open-supported**, in the limited sense that Alexandersson's
maintained [Catalan families page](https://www.symmetricfunctions.com/realRootedCatalan.htm),
under the NNE example and immediately following 2023 conjecture, still lists
the Fuss extension when inspected on 2026-09-12. The page abbreviates the
rectangle convention; the user source fixes our exact interpretation.
No prior resolution of this exact statement was verified in this bounded search;
this does not establish global novelty or current open status conclusively.

Nearest proved result: Bóna et al.'s ordinary-Dyck coefficient formula and
real-rootedness, explicitly reproduced as Theorems 1.1 and 1.2 in
[Wang--Zhang, arXiv:2309.05903v1](https://arxiv.org/html/2309.05903v1).
Their Theorems 2.4 and 2.7 further treat ordinary interlacing. The actual
relevant theorem statements were inspected, not inferred from snippets.
See literature/triage-verification.md and the saved primary HTML.

Proposed contribution for fresh review: prove the Fuss counting identity

    W^(m)_(n,k)(t)=(1/n)C(n,k) sum_(j=1)^k C(k,j)C(mn-k,j-1)t^j.

It implies a positive-scalar reduction to the known ordinary polynomial:

    W^(m)_(n,k)=C(n-1,k-1)/C(mn+1,k-1) * V_(mn+1,k).

The all-parameter proof is now in evidence/research-proof.md. It supplies
the unique last-departure decomposition, all cross-boundary factor counts,
and the Lagrange extraction, then applies the cited ordinary theorem.
A separate self-contained Rodrigues/orthogonality argument proves the
stronger conclusion that W has degree k, one simple zero at 0, and k-1
distinct strictly negative zeros. In that argument W/t is a positive
multiple of

    (1-t)^(k-1) P_(k-1)^(1,mn-2k+1)((1+t)/(1-t)),

where the Jacobi parameter mn-2k+1>=1. Neither argument changes the source
statement or assumes an empirical extrapolation.

The exact standalone checker evidence/check-research.py uses a different
run-block enumeration and checks 66 polynomials beyond the inherited
table, 3176 additional valid words, exact Sturm counts, and the Jacobi
and scalar identities. Output and limitations are in
evidence/research-check.json and evidence/research-audit-notes.md.
The triage evidence remains available as earlier corroboration.

Current literature comparison: literature/research-comparison.md verifies
the 2025 Bóna et al. version as well as the original source page and
Wang--Zhang. No equivalent Fuss resolution was found in the primary
sources inspected; this is not a global priority assertion. Known ordinary
formulas, standard first-return decomposition, Lagrange inversion, and
Jacobi theory are not claimed as new. The proposed benefit is their exact
Fuss identification and the full-scope resolution of source.md.

Decisive full local primary texts have been copied byte-for-byte into
evidence/external/wang-zhang-2309.05903v1.html and
evidence/external/alexandersson-realRootedCatalan-20260912.html.
The Bóna primary browser extract is separately labeled as an extract in
evidence/external/bona-et-al-2212.10586v2-web-extract.txt.

Research disposition: **resolution-paper candidate**, with original_status
`proved` denoting the submitted proof claim. This requests fresh review;
no independent mathematical acceptance or manuscript is asserted here.
