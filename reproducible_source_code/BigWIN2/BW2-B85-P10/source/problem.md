# Precise interpreted problem

## Frozen claim and definitions

For every integer `k >= 1` and every vector
`a = (a_1,...,a_k) in Z_{>=0}^k`, define the finite simple tree `T(a)` as
follows.  Its spine vertices are `v_1,...,v_k`, with spine edges
`v_i v_{i+1}` for `1 <= i < k`; for each `i`, add `a_i` new degree-one
vertices adjacent only to `v_i`.  Thus

`N = |V(T(a))| = k + sum_{i=1}^k a_i`.

A set `S subseteq V(T(a))` is dominating when every vertex `u` satisfies
`S intersection N[u] != empty`, where `N[u]` is its closed neighborhood.  For
`0 <= j <= N`, let

`d_j(T(a)) = #{S subseteq V(T(a)) : |S|=j and S is dominating}`

and set `D_{T(a)}(x) = sum_{j=0}^N d_j(T(a)) x^j`.

The immutable source asks for a proof or disproof of the universal claim

`d_j(T(a))^2 >= d_{j-1}(T(a)) d_{j+1}(T(a))`

for every `k >= 1`, every `a in Z_{>=0}^k`, and every integer
`1 <= j <= N-1`.  Vacuous index ranges are allowed.  Coefficients include
zeros; no positivity, strictness, normalization, canonical-spine, or
fixed-spine-length assumption is implicit.  A disproof must exhibit one
admissible vector and index with a strictly negative minor; a proof must cover
every displayed quantifier.

## Exact reductions and remaining scope

For `k >= 2`, an endpoint with no attached leaf can be absorbed exactly:

`T(0,a_2,...,a_k) ~= T(a_2+1,a_3,...,a_k)`

and analogously at the right endpoint.  This is a graph isomorphism: the old
zero-leg endpoint becomes one additional leaf at its neighbor.  Repeatedly
applying it, plus reversal of the spine, preserves the domination polynomial.
Together with the already proved all-positive case, the genuinely uncovered
normalized cores therefore have `k >= 3`, `a_1,a_k >= 1`, and at least one
internal `a_i=0`.  This is a search/proof reduction of the full claim, not a
change to its quantifiers.  The exceptional singleton `T(0)` has domination
polynomial `x` and no tested index.

## Nearest verified prior result and proposed delta

Du--Heilman--Panova, arXiv:2605.02193v1, Theorem 3.3, proves the claim when
every `a_i >= 1`, using the product

`D_T(x) = product_i (x^{a_i} + x(1+x)^{a_i})`.

Their Remark 3.4 says they believe the conclusion also holds when some
`a_i=0`; it is not a proof.  The arXiv record still contained only v1 on
2026-09-11, and targeted searches found no later primary resolution; this is
only provisional open-status evidence.

The full target delta is either (i) an exact internal-zero counterexample,
with its full coefficient list and a negative log-concavity minor, or (ii) a
proof handling arbitrary internal zero blocks.  Two analytic subfamilies are
now proved.  `evidence/base-family-inequality-proof.md` proves `T(p,0,q)` for
all `p,q>=1` by reducing its only new minor to a monic quadratic in `pq` with
negative discriminant.  `evidence/two-zero-family-proof.md` proves
`T(p,0,0,q)` for all `p,q>=1`: an endpoint-state formula is reversed into
three nested binomial convolutions with sparse perturbations, and all ten
affected minors have exact coefficientwise-nonnegative certificates.  These
proper subfamilies do not resolve the frozen claim.  Exact tree dynamic
programming, independently checked against subset enumeration, remains the
bounded verifier.  A full positive route must ultimately justify a uniform
zero-block transfer and interactions among multiple separated zero blocks.
