# A stronger algebraic assertion, frozen before the order-six attack

Job: `primary-20260914-antiprism-total-positivity-research-1f8d7876bdf3`.
Research hypothesis version 1, 2026-09-14. This is not a candidate or an
accepted conjectural contribution. Orders four and five motivated it; order
six is the first held-out order in this pass.

For each integer k>=1, write

`T_(r,l)(x,y)=[z^r c^l] exp(zx)/(1-(exp(z(x+y))-1)(c-1))`.

For r=1,...,k and s=1-k,...,0 define

`M_(r,s) = sum_(l=1)^r b_l (l/(l+1))^s
 sum_(p+q=r) [x^p y^q]T_(r,l) (a+k+s)_p (n-s)_q/[l^p(l+1)^q]`.

The falling factorial convention is `(v)_p=prod_(h=0)^(p-1)(v-h)`.
Let R_k be the polynomial det M after making the simultaneous substitution

`b_l=l^k(z_1+...+z_l)`, l=1,...,k.

**Working hypothesis:** Every coefficient of R_k in the independent
variables a,n,z_1,...,z_k is nonnegative, and the coefficient of z_1^k is
strictly positive. Its falsifier is a negative exact coefficient at any k,
or a nonpositive coefficient of z_1^k. It is stronger than positivity only
at actual matrix parameters.

Structural motivation: at a=j-k>=0, n=d-j>=0, the required specialization
is z_1=2^n and
`z_l=l^a(l+1)^n-(l-1)^a*l^n >=0` for l>=2. Thus the asserted algebraic
property implies positivity of the consecutive flags in rows 1,...,k and
columns j-k+1,...,j for all d>=j>=k. These are the successive numerators
in the first Neville stage. This implication is only a partial route to
the original problem: the column-zero boundaries and second elimination
stage require separate arguments.

The first four orders have low-row or exact coefficient evidence; order
five was calculated while formulating this version and is discovery data.
The order-six polynomial is to be calculated without modifying the
assertion. No literature-screened novelty or general proof is claimed.

Post-freeze outcome, same pass: the order-six attack passed with 33,396
positive coefficients in 132 base monomials, as recorded in
`research_flag_order_6.json`. `verify_flag_order_6.json` records a complete
separate arithmetic verification. This assertion was not revised after that
test. `research-pass2.md` also proves product formulas for the constant and
highest (a,n)-degree components for every k. The intermediate degrees for
general k remain unproved; no conjecture-note candidate is proposed here.
