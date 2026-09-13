# Precise problem and triage normalization

## Frozen claim

The immutable statement is `source.md` (SHA-256
`0af528efdf37ddabccc405621c5e04c5afca4ee0c7cd2939aaf2dd00de9133ab`).
Its precise reading is:

> For every `(u,v) in Z_{>0}^2`, define independent random variables
> `B_1,B_2,B_3` by `P(B_i=0)=p` and `P(B_i=1)=q:=1-p`, and set
> `X=1+B_1+uB_2+vB_3`. For all `p_0,p_1 in [0,1]` and all
> `lambda in [0,1]`, prove
> `h(lambda p_0+(1-lambda)p_1) >= lambda h(p_0)+(1-lambda)h(p_1)`,
> where `h(p)=H(X)` and `0 log 0=0`; or disprove this universal claim by
> an explicit positive-integer pair and a rigorous interval of failure.

Natural logarithms are used; changing the logarithm base only multiplies the
entropy by a positive constant. The additive shift by `1` has no effect on
entropy. Endpoint values are part of the claim. Since each exact profile below
is continuous on `[0,1]` and smooth on `(0,1)`, proving `h'' <= 0` throughout
the open interval suffices for concavity on the closed interval. Conversely,
a rigorously certified open interval on which `h''>0` disproves concavity.

Every prefix `2=a_1<a_2<a_3` gives exactly the positive increments
`u=a_2-a_1`, `v=a_3-a_2`, and every positive pair arises this way. Thus the
quantifiers really are the complete `n=3` layer, not a selected family.

## Exhaustive collision normalization

For a bit vector `b=(b_1,b_2,b_3)`, its unshifted support point is
`s(b)=b_1+u b_2+v b_3`. A collision between two distinct bit vectors, after
cancelling common summands, is an equality between two disjoint nonempty
subsets of the three positive weights `{1,u,v}`. Such an equality is either
one weight equal to another, or one weight equal to the sum of the other two.
Consequently a collision occurs if and only if

`u=1`, `v=1`, `u=v`, `v=u+1`, or `u=v+1`.

Indeed, these are all the one-versus-one and one-versus-two equalities; the
only omitted formal possibility, `1=u+v`, is impossible for positive `u,v`.
This proves exhaustiveness for all positive integers rather than extrapolating
from a finite scan.

Put

`A=p^3`, `B=p^2q`, `C=pq^2`, `D=q^3`, and `R=B+C=pq`.

The complete disjoint case split and the corresponding multiset of nonzero
atom probabilities is:

1. `(u,v)=(1,1)`: `[A,3B,3C,D]`.
2. `(u,v)=(1,2)` or `(2,1)`: `[A,2B,R,2C,D]`.
3. `u=1,v>=3`, or `v=1,u>=3`, or `u=v>=2`:
   `[A,B,2B,C,2C,D]`.
4. `v=u+1` with `u>=2`, or `u=v+1` with `v>=2`:
   `[A,B,B,R,C,C,D]`.
5. All remaining pairs: `[A,B,B,B,C,C,C,D]`.

For any displayed probability multiset `M`, the exact entropy profile is
`H_M(p)=-sum_{m in M} m log m`, with the endpoint convention from the source.
Thus nine labelled collision partitions reduce to five entropy profiles.
The earlier exact enumeration for `1<=u,v<=11` found precisely these nine
labelled partition types; it is corroboration only, while the subset-equality
argument above supplies completeness.

## Prior-result boundary and proposed delta

The nearest cited source is Neunhäuserer's Conjecture 3.1, which asserts the
all-`n` statement. Its Proposition 3.1 proves the binomial sequence and a
sufficient completely non-overlapping regime, but not every `n=3` collision
profile above. The targeted literature pass preserved in the recovery record
did not establish that this complete layer is already known; status therefore
remains `status-uncertain`, not a priority claim.

Proposed contribution: resolve the frozen universal `n=3` claim by proving
concavity of all five exact profiles, or disprove it with one explicit profile,
pair, and certified interval. The bounded verification route is symbolic
differentiation of the three nontrivial profiles (cases 2--4; cases 1 and 5
reduce to standard binomial/product entropy), followed by exact analytic or
interval sign control on `(0,1)`.
