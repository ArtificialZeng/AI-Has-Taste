# Fixed-sum Schur (2,2) reconstruction

Immutable source.md SHA256: 08e71a9e52f039251c1c05f8a22310eb23c909494da046a0a0ca716d20f1de10.

For every integer N>=2, let P_(>=2)(N) be the nonincreasing finite sequences lambda=(lambda_1,...,lambda_l) of positive integers with l>=2 and sum_i lambda_i=N. Repeated parts are allowed. Define s_(2,2) in l indexed variables by the semistandard Young tableaux of the two-by-two diagram: rows weakly increase and columns strictly increase in the variable indices. If

s_(2,2)(x)=sum_alpha c_alpha*x^alpha,

then S22(lambda) contains prod_i lambda_i^(alpha_i) with multiplicity c_alpha, added over all alpha producing the same value. Thus equality means equality of every numerical multiplicity, not equality of the polynomial's scalar value or distinct support.

Frozen target: for every N>=2 and every lambda,mu in P_(>=2)(N),

S22(lambda)=S22(mu) implies lambda=mu.

The lengths are not assumed equal, but equality forces them equal since |S22(lambda)|=l^2(l^2-1)/12. The positivity and fixed-N hypotheses are retained. Length two is included; (4,1) and (2,2) have equal S22 but different sums and are outside the target. A disproof requires an exact complete multiplicity certificate for distinct partitions of the SAME N. No correction to source.md is proposed.

## Source and nearest prior results

The live Thomas–Tung preprint arXiv:2606.19796v1 places the general two-row assertion in Conjecture 6.3 and the known (2,1) case in Theorem 1.7. The source's journal URL was inaccessible, so its cited numbering is unverified. Crucially, Theorem 5.7 already proves largest-part-conditional recovery for two-row shapes, including the previous proposed prefix formula. It is a rediscovery. Source status is open-supported within the inspected literature; no global priority assurance is given. See literature/triage-20260912.md for exact URLs and positions.

## Research subsidiary result; original scope unchanged

Job newwin-00001-p10-research-b1ee08dba39b provides a proposer proof in
evidence/research-moment-proof.md of the following sufficient condition:
for fixed length l>=2, S22 determines every positive real multiset whenever

c_j(l)=l/3 * (l^2-1+3*2^(j-1)-3^j)

is nonzero for every 1<=j<=l. Its first l logarithmic power sums and cardinality
already suffice, using triangular recovery and Newton identities. Positivity,
indexed multiplicities and repeated values are treated explicitly.

The proof establishes nonvanishing for l>=3, l!=4, outside the four residue
classes 14,26,34,46 modulo 60. This includes every odd length and every multiple
of four at least eight. Separate self-contained fixed-sum proofs handle l=2,4.
Consequently the frozen fixed-N conjecture is proved by the proposed subsidiary
argument for every length outside those four residue classes. The all-length
claim, including l=14, remains unresolved. These are sufficient conditions;
excluded residue classes and zero coefficients are not noninjectivity claims.

The general moment method is prior art (Fomin). The coefficient c_j(l) is a
specialization of the Chern shadows in D'Andrea--Fatighenti--Onorati,
arXiv:2508.03568v2, Definition 3.2 and Appendix A. The proposed contribution is
the reconstruction application and explicit length criterion, with bounded
novelty screening in literature/research-20260912.md. Fresh mathematical and
novelty review remains required. The boundary cases are not separate novelty
claims. The prior known-prefix route is not part of the proposed contribution.

The decisive original primary text is now included in the project evidence as
evidence/external/thomas-tung-2606.19796v1.html, copied byte-for-byte from the
existing literature cache and compared to the live theorem/conjecture statements.
Its journal counterpart's numbering remains unverified.

Fresh exact verification: evidence/check-research-moments.py, independent of
earlier scripts, produces evidence/research-moment-check.json. It checks 1281
exhaustive small integer-log lists, 60 held-out structured samples through
length 61, 2079 Mobius coefficient evaluations, and 85 fixed-sum boundary
recoveries. It records 1252 complete moment/Newton recoveries and correctly
stops at a zero coefficient in the other 89 cases. No numerical logarithms are
used. The finite coefficient certificate covers every length 2<=l<=10^6 and
finds zeros only at (l,j)=(2,2),(4,3),(14,5), using the strict increase of
1+3^j-3*2^(j-1) to stop the search. No unbounded classification is claimed.

One next test: a fresh referee should verify Theorems A--C in the proof dossier
and determine whether the reconstruction application is already implied by an
explicit existing result beyond the acknowledged general formalisms. This
research pass does not supply its own independent acceptance.
