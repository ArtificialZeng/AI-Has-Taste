# Frozen interpretation

Job: `newwin-00001-p12-triage-3ebebbace8a4`; triage, 2026-09-12.
The verbatim source is `source.md`, unchanged. Its SHA-256 is
`f13440b8f2b246d10391b74172f52aeb59243c453e4684992a1c29cac3f8cacd`.

For every prime power q=p^e, with p prime and e a positive integer, let F_q
be the field with q elements. Let lambda and mu be triples of integers such
that lambda_1 >= lambda_2 >= lambda_3 >= 0 and
mu_1 >= mu_2 >= mu_3 >= 0, with mu_j <= lambda_j,
lambda_j <= 4-j, and mu_j <= 3-j for j=1,2,3.

Count ordered pairs (A,B) of 4-by-3 matrices over F_q, with row indices
i=1,2,3,4 and column indices j=1,2,3, subject to
A_ij=0 if i>4-lambda_j and B_ij=0 if i>4-mu_j. All other entries
are arbitrary, including zero. Arrays are counted individually, not modulo
any group action. Nondegeneracy means that the boundary-format
hyperdeterminant of the 2-by-4-by-3 tensor (A,B) is nonzero.
Equivalently, rank(sA+tB)=3 for every nonzero pair (s,t) over the
algebraic closure of F_q (Lemma 2.5 of the primary paper). Checking only
F_q-rational pairs (s,t) would be a different condition.

The exact target is the identity

N_(lambda,mu)(q) = q^9 (q-1)^6
  product_(j=1)^3 [5-j-lambda_j]_q
  product_(j=1)^3 [4-j-mu_j]_q,

simultaneously for every permitted pair (lambda,mu) and every prime power q,
where [r]_q = sum_(a=0)^(r-1) q^a. All six r are positive.
The empty shape and maximal shape ((3,2,1),(2,1,0)) are included.
No statement for k>3, q=1 as a field, or other zero patterns is requested.

The definitions and formula agree with the k=3 specialization of
[Koprowski–Lewis, arXiv:2602.22129v1](https://arxiv.org/html/2602.22129v1),
Definitions 2.9 and 2.11 and Conjecture 3.1. Nearest prior results:
Theorem 3.7 treats mu=0, Theorem 3.8 treats the maximal shape,
and Theorem 4.1 gives polynomial positivity. Section 5.1 supplies a
permutation sum whose evaluation is the proposed delta for k=3.
The general conjecture is explicitly left open in that version. The
journal version was successfully retrieved during research pass 1 via its
index link and retains the same relevant scope and sum; see the addendum
below. Global priority is not certified.

Verification route: enumerate all permitted shapes and the 4!3!=144 pairs
of permutations; calculate the exponent in the established Section 5.1
sum and compare integer coefficient lists. Finite-field evaluations alone
do not establish the universal identity. No correction of the source is needed.

Exact enumeration gives 55 shapes, including 14 with mu=0 and the maximal
shape. The 40 remaining shapes are the proposed special-case contribution.

Research pass 1 addendum, job `newwin-00001-p12-research-79bff11d6956`,
2026-09-12: the original quantifiers and interpretation above are unchanged.
`evidence/proof.md` now gives a proposed complete proof, with an explicit
unit-pivot elimination order valid in every characteristic and a complete
55-row integer polynomial certificate. `evidence/verify_sparse.py`
reconstructs every augmented matrix independently of the earlier Boolean
calculation. A separate exhaustive binary pencil computation verifies all
55 counts at q=2 using the algebraic-closure rank criterion.

The journal source is ECA 7:1 (2027), Article S2R3, published 2026-08-21,
DOI 10.54550/ECA2027V7S1R3. Its retrieved primary text is archived locally
as `evidence/external/koprowski-lewis-eca2027-web.txt`; the inspected arXiv
primary text is `evidence/external/koprowski-lewis-2602.22129v1-web.txt`.
Journal Theorems 3.2/3.3 treat the two known families; Corollary 4.2,
Theorem 4.4, and Section 5.1 provide the counting framework. Section 3.3
retains the 40-shape k=3 census without their product evaluation.
`literature/research-screen.md` records the precise version mapping and
bounded current comparison. No equivalent later resolution was found in
that search; no global priority claim is made.

Proposed outcome: resolution-paper candidate for this k=3 statement only,
pending fresh mathematical review. The general k conjecture remains
outside scope. No mathematical acceptance or manuscript exists.
