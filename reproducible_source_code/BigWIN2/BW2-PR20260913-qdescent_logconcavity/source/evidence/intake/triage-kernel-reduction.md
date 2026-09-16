# Frozen kernel target and exact reduction

Job: primary-20260913-qdescent-logconcavity-triage-178cb0fc6742.
Frozen 2026-09-13 during triage, after discovery checks m <= 8 and before
holdouts m = 9,10,11,12. This is a proposed sufficient lemma, NOT a proved
inequality, candidate paper, or novelty assertion.

Write G(n,k) = [n choose k]_q, zero outside 0 <= k <= n. For m >= 1,
1 <= r <= m, and 1 <= k <= m, set

    K(m;k,r) = q^(k^2) (G(m,k) - G(m-r,k)),
    K(m;0,r) = K(m;m+1,r) = 0.

The q-Pascal identity G(t+1,k)-G(t,k) = q^(t+1-k) G(t,k-1)
gives the positive formula

    K(m;k,r) = sum_{h=1}^{min(r,m-k+1)}
                   q^(k(k-1)+m+1-h) G(m-h,k-1).

In particular all K(m;k,r) are nonzero nonnegative polynomials for
1 <= k,r <= m (the h=1 summand suffices).

## Exact reduction from actual descent polynomials

For a fixed original S, let m=max S, T=S without m, and

    x_r = sum_{sigma in Sym(m), Des(sigma)=T, sigma_m=r} q^inv(sigma).

Deleting and standardizing the last entry i of a permutation of size m+1
contributes exactly m+1-i inversions. Its last descent requires the last
standardized prefix value r to satisfy r >= i. Consequently

    b_i(S;q) = q^(m+1-i) sum_{r=i}^m x_r.

Substituting this into the source Remark's a-to-b formula and exchanging the
finite sums proves the identity

    a_k(S;q) = sum_{r=1}^m K(m;k,r) x_r.

This uses the actual suffix recurrence in the proof of source Theorem 6,
not the false arbitrary-b preservation claim in its Remark. At least one x_r
is nonzero: every prescribed ascent/descent pattern is realized by a linear
extension of the oriented path of positions. Thus all a_1,...,a_m are nonzero.
These identities and support reasoning are elementary deductions, with no
claim that they are new publishable results.

## Target K: coefficientwise quadratic positivity (unproved)

For all m >= 1, 1 <= i <= j <= m, and 1 <= r <= s <= m, claim:

If r=s,

    K(m;i,r) K(m;j,r) - K(m;i-1,r) K(m;j+1,r) >=_q 0.

If r<s,

    K(m;i,r) K(m;j,s) + K(m;i,s) K(m;j,r)
    - K(m;i-1,r) K(m;j+1,s) - K(m;i-1,s) K(m;j+1,r) >=_q 0.

Here >=_q means that every coefficient is nonnegative. These are exactly the
coefficients of x_r^2 and x_r*x_s in the formal determinant
(sum K_i,r x_r)(sum K_j,r x_r) - (sum K_i-1,r x_r)(sum K_j+1,r x_r).
If Target K holds, substitution of arbitrary nonnegative polynomial x_r proves
the determinant inequalities; descent-derived x_r give the original strict
i<j target and the separately identified stronger diagonal i=j target.

A failure of Target K need not refute the original: arbitrary independent x_r
are a strengthening of the realizable last-value vectors. A diagonal-only
failure of the original a-sequence also does not refute frozen literal scope.

Next decisive test: seek a coefficient-preserving injection or positive
q-Pascal decomposition of these mixed quadratic expressions uniformly in
m,r,s,i,j. A proof would resolve the stated sufficient lemma; a negative
coefficient would invalidate this proposed proof route and require testing
realizability before making any claim about S.
