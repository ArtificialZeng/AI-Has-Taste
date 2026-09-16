# Fixed-column sign transition: precise original and candidate scope

Research pass 1, 2026-09-14.
Job: `primary-20260914-stirling-transition-research-d94530e09967`.

Frozen input: `source.md`, SHA-256
`4a37fe8a21f41aac0b72c9da83e28e1aff2ce19676fe24c5d93befb9e2d99594`.
The source is unchanged. No correction or weakening is proposed.

For integers n>=0 and k, let c(n,k) count permutations of {1,...,n}
having exactly k disjoint cycles. Thus c(0,0)=1, c(n,0)=0 for n>0,
and c(n,k)=0 when k<0 or k>n. For n>=1 define

    D_k(n)=c(n,k)^2-c(n-1,k)c(n+1,k).

The original assertion is

    for every integer k>=1 there exists an integer N_k such that
    for every integer n with 1<=n<N_k, D_k(n)>=0, and
    for every integer n>=max(1,N_k), D_k(n)<=0.

The inequalities are centered at n. Equality is allowed on either side;
neither uniqueness nor a numerical formula for N_k is requested. Here k is
fixed and n varies. The coefficients are unnormalized permutation counts.
Row log-concavity or eventual column log-convexity alone would not suffice.

Boundaries: D_k(n)=0 for 1<=n<k, D_k(k)=1, N_1=2 works, and the
optional k=0 boundary has D_0(n)=0 for all n>=1.

## Primary source and closest inspected results

Liang and Sagan, *Log-Concavity and Log-Convexity via Distributive Lattices*,
Order 43, article 21 (2026), Section 8.2, Conjecture 8.8, printed p.31,
states this transition and reports tests through 100. Its arXiv v1 labels
it Conjecture 8.9. Theorem 7.2 concerns second-kind column log-concavity.
[Published primary PDF](https://users.math.msu.edu/users/bsagan/Papers/Old/lclc%20-%20pub.pdf);
[arXiv v1 primary text](https://arxiv.org/html/2408.02782v1).
The actual local primary text is now bound in
`evidence/external/2408.02782v1.html`.

Salas, [arXiv:2607.04217v1](https://arxiv.org/html/2607.04217v1),
Theorems 1.4/1.5 concern rows and products of row-generating polynomials.
Their statements were inspected and are distinct from the column transition.
The actual local primary text is `evidence/external/2607.04217v1.html`.

Fan and Wang, [Advances in Applied Mathematics 178 (2026), 103092](https://www.sciencedirect.com/science/article/pii/S0196885826000643),
report related elementary-symmetric ratio convexity in their publisher-indexed
abstract. The exact theorem and full text were not verified. The present
argument is self-contained and claims no priority for that general property.
This close lead and all access/search limits are documented in
`literature/research-pass1-review.md`. No equivalent transition resolution
was found in inspected sources; global novelty is not certified.

## Proposed full resolution and its review status

`evidence/ratio-convexity-proof.md` provides a complete proposed proof of the
original statement. It first proves that multiplication by a positive linear
factor preserves convexity of adjacent coefficient ratios. Applying this to
elementary symmetric coefficients makes the entire numerator (2) of
`evidence/ratio-reduction.md` nonnegative, proving

    q_k(n)-2q_k(n+1)+q_k(n+2)>=0, n>=k>=1,
    q_k(n)=c(n,k-1)/c(n,k).

The inequality is strict for k>=2. The recurrence then gives
D_k(n)/[c(n-1,k)c(n,k)]=q_k(n-1)-q_k(n)-1 on n>=k+1.
Monotonicity and telescoping construct a finite N_k, proving the original
inequalities and a strict negative tail. This is a proposed full resolution,
not a finite-prefix claim or a narrower replacement problem.

The current worker submits `kind=resolution-paper`, `original_status=proved`
as the scope to be checked by a fresh referee. It does not assert mathematical
acceptance. Known mathematical gaps identified by the proposer: none.
`evidence/verify_ratio_proof.py` and its JSON output supply exact algebra and
finite error-detection checks; these are not the infinite proof or a novelty
certificate. No manuscript is produced in this phase.
