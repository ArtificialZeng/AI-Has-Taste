# Exact computational lower bound for the frozen problem

## Claim and scope

For the interpretation in `problem.md`,
\[
m_2(4)\ge 18.
\]
Equivalently, no width-exactly-two poset on at most 17 elements has chain
gap greater than 4 on every inclusion-maximal chain.  This does **not**
determine `m_2(4)`, test order 18, classify any minimizer, or provide the
canonical whole-domain census required for a complete answer to `source.md`.

## Exhaustive two-chain encoding

Fix positive integers `a<=b` with `a+b=n`, and write two covering chains as
`A_0<...<A_(a-1)` and `B_0<...<B_(b-1)`.  For every `i`, define

- `L_i = |{j:B_j<A_i}|`; and
- `U_i = min({j:A_i<B_j} union {b})`.

The cross-relations are then exactly
`B_j<A_i` for `j<L_i`, `A_i<B_j` for `j>=U_i`, and incomparability for
`L_i<=j<U_i`.  Transitivity implies, and is implied by,

```
0 <= L_0 <= ... <= L_(a-1) <= b,
0 <= U_0 <= ... <= U_(a-1) <= b,
L_i <= U_i for every i.
```

The recursion in `evidence/enumerate_width2.py` emits every such pair once.
Every width-at-most-two poset has a partition into two chains by Dilworth's
theorem; swapping the chains ensures `a<=b`, so every width-two isomorphism
class occurs in this enumeration, possibly many times.  A presentation has
width one exactly when `L_i=U_i` for all `i`; otherwise its displayed
two-chain cover and an incomparable cross-pair prove width exactly two.
Deduplication is unnecessary for the asserted nonexistence result.

## Exact expected ranks

A linear extension is a lattice path through states `(i,j)`, meaning that its
prefix contains the first `i` A-elements and first `j` B-elements.  From such
a state one may add `A_i` iff `j>=L_i`, and may add `B_j` iff
`i>=K_j`, where `K_j=|{i:U_i<=j}|`.  Integer prefix and suffix path counts
`F(i,j)` and `G(i,j)` therefore give `e(P)=F(a,b)` exactly.  The rank sum of
`A_i` is
\[
\sum_{j=L_i}^b F(i,j)G(i+1,j)(i+j+1),
\]
and the analogous formula for `B_j` sums over `i>=K_j`.  Thus every expected
rank is represented by the exact fraction `rank_sum/e(P)`; no floating-point
arithmetic is used.  For `n<=19`, every count and rank sum is at most `n*n!`,
which is below `2^64`, justifying the program's unsigned 64-bit arithmetic.

## Universal maximal-chain test

In a finite poset, inclusion-maximal chains are precisely the saturated paths
from a minimal element to a maximal element in the cover graph.  After
multiplying all expected ranks by `e(P)`, such a chain has gap at most 4 iff
its initial spacing, every cover-edge spacing, and its final spacing are all
at most `4e(P)`.  Hence a label-independent reachability search using only
these allowed vertices and cover edges exists iff some maximal chain violates
the frozen universal `gap>4` condition.  The program marks a presentation as
qualifying exactly when there is no such path.

## Complete runs and result

`evidence/search-through-16.json` exhausts orders 4 through 16.
`evidence/search-order-17.json` separately exhausts order 17.  Across them the
program tested 346,907,798 presentations, of which 346,767,961 have width
exactly two.  The order-17 presentation count is 238,819,349, agreeing with
the generator recurrence, and every order from 4 through 17 has
`qualifying_presentations: 0`.  Orders 1 through 3 are disposed of exactly in
`problem.md`.  This proves the claimed lower bound.

## Independent small-order audit and replay

`evidence/verify_width2.py` independently enumerates all forward labeled
relations, tests transitivity and width directly, and canonicalizes under all
permutations for `n<=6`.  Its canonical domains equal those obtained from the
two-chain generator, with unlabeled width-two counts `1,3,9,25,74` for
`n=2,...,6`.  On every width-two presentation in that range it also recomputes
linear extensions/rank sums by generic ideal-subset DP and explicitly lists
all maximal cover paths.  All exact counts, all rank sums, and all chain
decisions agree; the closed output is
`evidence/independent-audit-through-6.json`.

Replay from the project directory (Python 3 with NumPy and Numba):

```sh
python3 evidence/enumerate_width2.py 16 > /tmp/search-through-16.json
python3 evidence/enumerate_width2.py 17 --min-n 17 > /tmp/search-order-17.json
(cd evidence && python3 verify_width2.py > /tmp/independent-audit-through-6.json)
```

SHA-256 at handoff:

```
bfbbb49e3e48aa870975ad736b19c9015a62acb5e0c087fa3feda5c1343089c4  evidence/enumerate_width2.py
00cde65d60ba31e74747ca8762446af178fe45f54b9854b7a5358d6fbd9c6c97  evidence/search-through-16.json
aeaa7574fe92bbf42a66906f85e7285fe2674389d6e463d7e231b38378634b2a  evidence/search-order-17.json
8ff2b6cd3672639f4418a2fbc21bf5738bd49a449001575ab5b8e4e364e2ae37  evidence/verify_width2.py
97a264709b1b0d43b602d04f3d3521638b0d4cecf6a8a4713e896afca9cb11e1  evidence/independent-audit-through-6.json
```
