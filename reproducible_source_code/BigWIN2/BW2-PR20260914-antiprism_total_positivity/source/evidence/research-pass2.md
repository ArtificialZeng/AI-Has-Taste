# Fourth-order flags and a stronger coefficient test

Job: `primary-20260914-antiprism-total-positivity-research-1f8d7876bdf3`.
This is a research dossier. The original all-order, all-dimension matrix
question is unresolved here; no mathematical acceptance is asserted.

## Completed fourth-order assertion

For every integer d>=4 and 4<=j<=d,

`det H_d[{1,2,3,4},{j-3,j-2,j-1,j}] > 0`.             (1)

In particular this settles the previous next test, whose range began at
d=5. The extra case d=j=4 is valid and equals 2925.

Use the generating identity derived directly from the frozen formula in
`research-pivots.md`:

`G(x,y,z)=exp(zx+y)/(1-(exp(z(x+y))-1)(exp(x+y)-1))`.

Let `T_(r,l)=[z^r c^l]exp(zx)/(1-(exp(z(x+y))-1)(c-1))`.
The fourth coefficient has the terms below multiplying
`exp(l*x+(l+1)*y)`:

```
T_(4,0) = y^4/24,
T_(4,1) = -x^4/24-x^3*y/3-x^2*y^2-4*x*y^3/3-5*y^4/8,
T_(4,2) = 7*x^4/12+10*x^3*y/3+7*x^2*y^2+19*x*y^3/3+25*y^4/12,
T_(4,3) = -3*x^4/2-7*x^3*y-12*x^2*y^2-9*x*y^3-5*y^4/2,
T_(4,4) = (x+y)^4.
```

The lower-row polynomials are recorded in the earlier dossier and all
four rows are serialized in `research_fourth_flag.json`. The independent
verifier derives them by the recurrence

`f_0=1; f_r=x^r/r!+(c-1)sum_(h=1)^r (x+y)^h/h!*f_(r-h)`.

This is obtained by multiplying the denominator of the generating series.
The producer instead uses Stirling-number coefficient extraction. Thus the
row identities have two exact derivations/implementations.

Write a=j-4>=0 and n=d-j>=0. For r=1,...,4 and s=-3,-2,-1,0, form

`M_(r,s) = sum_(l=1)^r b_l(l/(l+1))^s
 sum_(p+q=r) [x^p y^q]T_(r,l) (a+4+s)_p(n-s)_q/[l^p(l+1)^q]`.

At `b_l=l^j(l+1)^n` these entries are exactly H_d(r,j+s), by coefficient
extraction. The l=0 term is a multiple of y^r exp(y), so vanishes in all
columns used, whose indices are at least 1. This explains why column-zero
flags are outside the result.

The polynomial D=det M has 14 base monomials and 643 nonzero coefficients
in a,n,b_1,...,b_4. Several base groups have negative coefficients. Put

```
u=b_1,
v=b_2=16u+V,
w=b_3=(81/16)v+W,
t=b_4=(256/81)w+T.
```

After this substitution D has exactly 924 nonzero coefficients in
a,n,u,V,W,T; every one is positive. The coefficient of u^4 is 2925.
The full rational coefficient list is in `research_fourth_flag.json`.
For the required specialization,

`b_(l+1)/b_l=((l+1)/l)^j*((l+2)/(l+1))^n
 >=((l+1)/l)^4`.

Consequently u>0 and V,W,T>=0, and D>=2925u^4>0. This proves (1),
including the boundary a=n=0 where all three differences vanish.

## Complete algebraic verification and finite checks

Run `python3 evidence/research_fourth_flag.py`, followed by
`python3 evidence/verify_fourth_flag.py`, from the project root.
The first uses SymPy exact polynomials. The second uses standard-library
integers and `Fraction` throughout the certificate check. It verifies:

- the complete row-generating identities by the denominator recurrence;
- D and the claimed 14-group expansion at all 14,520 points of the product
  interpolation grid with sizes (11,11,5,4,3,2);
- the entire affine-substitution identity coefficient by coefficient;
- positivity of all 924 coefficients and the exact u^4 coefficient 2925.

Each side of the determinant identity has separate degree bounds
(10,10,4,3,2,1) in (a,n,b_1,b_2,b_3,b_4). The 14,520 equalities therefore
prove that identity by repeated univariate interpolation; they are not
dimension extrapolation. The group coefficients' degree bounds are checked
from their complete lists. The determinant bounds follow from row degrees
1,2,3,4 and the triangular base support l<=r.

As additional tests, the verifier compares with the original double
Stirling definition for every d=4,...,16 and every allowed j. It also
compares with the independent face-vector formula for every d=17,...,64
and d=96,128,192,256, in every allowed column. These dimension tests are
finite observations, separate from the algebraic infinite-domain proof.
Output, certificate hash, and exact small flags are in
`verify_fourth_flag.json`. A separate arithmetic implementation in the same
context is not a fresh referee.

## Fifth and sixth orders: complete coefficient certificates

`flag-coefficient-hypothesis.md` freezes a stronger general algebraic
assertion: for order k, after `b_l=l^k(z_1+...+z_l)`, det M has
nonnegative coefficients in a=j-k,n=d-j,z_1,...,z_k. The actual
specialization satisfies z_1=2^n>0 and
`z_l=l^a(l+1)^n-(l-1)^a*l^n>=0` for l>=2.

`research_flag_hierarchy.py 5` found 5,712 positive coefficients and no
negative coefficients, in 42 base groups. This is discovery data for the
general assertion. Order six, the first held-out order after version 1 was
written, has 33,396 positive coefficients in 132 base groups. Its positive
coefficient of z_1^6 is 7,410,496,275. The respective exact coefficients are
in `research_flag_order_5.json` and `research_flag_order_6.json`.

`verify_flag_hierarchy.py 5` and `verify_flag_hierarchy.py 6` independently
verify both complete polynomial identities using only standard-library
integers and fractions. They derive T from

`T_(r,l)=[z^r]exp(-zy)(1-exp(-z(x+y)))^l`

by a signed binomial power sum, rather than the producer's Stirling sum.
The displayed identity follows directly by rewriting the denominator as
`exp(z(x+y))-(exp(z(x+y))-1)c` and expanding in c.

At every point (a,n) with a,n>=0 and a+n<=K=k(k+1)/2, the verifier forms
the **entire** determinant polynomial in z_1,...,z_k after clearing row
denominators, and compares all its coefficients. There are 136 grid points
for k=5 and 253 for k=6. Every a,n coefficient polynomial has total degree
at most K: each row has degree at most its index. The triangular grid is
unisolvent for that space. Indeed, a polynomial vanishing on it vanishes
identically at n=0 (K+1 distinct a values), so is divisible by n. Its
quotient vanishes identically at n=1, so is divisible by n-1. Continuing
would force divisibility by a polynomial in n of degree K+1, unless the
original polynomial is zero. This proves the claimed identities exactly.
Outputs are `verify_flag_order_5.json` and `verify_flag_order_6.json`.

Supplementary direct-definition checks are reproducible with
`verify_flag_values.py` and recorded in `verify_flag_values.json`: 78 flags
of order five (d=5,...,16) and 66 of order six (d=6,...,16), including
every allowed j in those dimensions. These finite tests are distinct from
the complete polynomial-identity verification.

Therefore, in addition to (1), the same coefficient-extraction and slack
argument proves

`det H_d[{1,...,k},{j-k+1,...,j}]>0`

for k=5,6 and every d>=j>=k. The boundary d=j=k is included.
This is a uniform statement in d,j at two fixed orders, not extrapolation
in k. Both implementations are in the same research context and do not
constitute a fresh referee.

## Uniform formulas at the two extreme degrees

For every k>=1, the constant-in-a,n component of R_k is

`R_k(0,0,z)=prod_(r=1)^k [sum_(l=1)^r l! S(r,l)(z_1+...+z_l)]`.       (2)

Here is a uniform proof, including the required weighted normalization.
For arbitrary weights w_l, with w_0=1, define an upper triangular matrix

`Q_d^w(i,t)=C(t,i)sum_(l=0)^i l! S(i,l)w_l*l^(t-i)`, i<=t.

Set `H_d^w=B_d Q_d^w B_d^(-1)`, with B as in `problem.md`. Summing its
column polynomials in x^j y^n/(j!n!) gives

`G_w=exp((1-z)y)sum_(l>=0)w_l(exp(z(x+y))-1)^l
                                  *exp(l(1-z)(x+y))`
`   =exp(y-zy)sum_(l>=0)w_l exp(l(x+y))(1-exp(-z(x+y)))^l`.

For example, the first expression follows by putting t=i+h in Q, summing
over j<=t and q=d-t, and using the Stirling exponential identity in i.
All sums are formal and locally finite by total degree. Extracting z^r
gives the same T_(r,l) formula, with b_l replaced by
`w_l*l^j(l+1)^n`. At d=j=k and w_l=z_1+...+z_l for l>=1, the minor
in R_k(0,0,z) is H_k^w with row and column zero removed. The full top row
is (1,0,...,0), so it has the same determinant as H_k^w. Triangular Q_k^w
then proves (2) by multiplying its diagonal entries.

The highest homogeneous component in a,n, of degree K=k(k+1)/2, is

`[R_k]_(degree K) = (prod_(r=1)^k r!)
 prod_(l=1)^k [(a/l+n/(l+1))^l*(z_1+...+z_l)]`.                    (3)

To prove this, retain the degree-r part of each row r in M. Put
`q_l=l/(l+1)` and `A_(r,l)=T_(r,l)(a/l,n/(l+1))` for l<=r, zero
otherwise. The resulting matrix is `A diag(b_l) V`, where
`V_(l,s)=q_l^s`, s=1-k,...,0. The matrix A is lower triangular with
diagonal `(a/l+n/(l+1))^l`. The generalized Vandermonde determinant is

`det V=prod_(p<q)(q-p)/prod_(l=1)^k l^(k-1)`.

After substituting b_l=l^k(z_1+...+z_l), the scalar becomes
`k! prod_(p<q)(q-p)=prod_(r=1)^k r!`, proving (3).
Both products have nonnegative coefficients for every k. Their base support
consists of the monomials z^alpha with sum alpha=k and
`sum_(l=1)^r alpha_l>=r` for r=1,...,k. These same constraints are forced
in every component by the row support l<=r. The endpoint identities are
also checked coefficient by coefficient at orders five and six by the
separate verifier.

In particular, the constant-in-a,n coefficient of z_1^k has a structural interpretation:
at a=n=0 and z_l=0 for l>=2, the determinant is
`det H_k[{1,...,k},{1,...,k}]=det H_k` because H_k(0,0)=1 and its
other top-row entries vanish. The face-vector conjugation gives
`det H_k=prod_(r=1)^k sum_(l=0)^r l! S(r,l)>0`.
This agrees with (2), and proves the strict witness uniformly in k,
independently of the remaining coefficient-sign assertion. The unresolved
part of the stronger algebraic hypothesis is the intermediate a,n degrees
1,...,K-1, for orders beyond those checked.

The original remaining gaps include arbitrary-order signs, the missing
column-zero boundary flags, and the second Neville elimination stage.
No unsupported transfer from initial flags to all minors is made.

## One next test

Determine the signs of every coefficient in the homogeneous component of
R_k of total (a,n)-degree K-1, for arbitrary k>=2. Retain the leading and
next-to-leading parts of each row in the factorization used for (3), and
derive a closed expression for this component. A negative exact coefficient
would refute the frozen stronger coefficient hypothesis; positivity would
establish the first uniform intermediate degree. Either outcome concerns
that explicitly stronger assertion, not automatically the original TN claim.
