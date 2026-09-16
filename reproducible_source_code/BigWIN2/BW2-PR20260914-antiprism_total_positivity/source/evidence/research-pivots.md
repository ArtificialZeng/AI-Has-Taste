# Uniform positivity of the first nontrivial Neville minors

Research job: `primary-20260914-antiprism-total-positivity-research-7e4c6a3e5254`.
This is a research dossier, not an accepted contribution or a manuscript.
The all-order total-nonnegativity problem remains unresolved here.

## Exact statements

For the frozen matrix H_d, put

`Delta(d,j) = det H_d[{1,2},{j-1,j}]`.

For every d>=3 and 2<=j<=d, writing n=d-j and t=d+j, one has

```
Delta(d,j) = 2^(d-4) 3^(n-2)
              [(t+2d-2)t(t-1) + d(d+1)(t-4)]
           + 2^(2n-3) [t(t-1)-2d] > 0.                 (1)
```

Negative exponents in this formula denote positive rational powers, including
n=0,1 and d=3. The complete expression is an integer. The omitted boundary is

```
Delta(d,1) = d(d-1) [(d+1)(2^(d-2)-2)3^(d-3)
                     + 2^(2d-5) + d 2^(d-4)] > 0.    (2)
```

Consequently every order-two minor using rows {1,2} and any two distinct
increasing columns in {0,...,d} is strictly positive for d>=3. Reflection
gives the same statement for rows {d-2,d-1}.

## Derivation from the frozen entry formula

Let L_r(z) be the polynomial whose coefficient of z^a is
`C(r,a) sum_l (l!)^2 S(a,l) S(r-a,l)`. Its exponential generating function is

```
sum_{r>=0} L_r(z) u^r/r!
  = sum_{l>=0} (exp(zu)-1)^l (exp(u)-1)^l
  = 1/[1-(exp(zu)-1)(exp(u)-1)].
```

These are formal power series; at each total degree only finitely many terms
contribute. Set P_{d,j}(z)=sum_i H_d(i,j)z^i. Substituting t=d-r-s in the
frozen definition gives

```
P_{d,j}(z) = sum_{s=0}^j sum_{t=0}^{d-j}
              C(j,s) C(d-j,t) z^s L_{d-s-t}(z).
```

Hence, with w=x+y,

```
G(x,y,z) := sum_{j,n>=0} P_{j+n,j}(z) x^j y^n/(j! n!)
          = exp(zx+y)/[1-(exp(zw)-1)(exp(w)-1)].        (3)
```

In particular, direct expansion to second order in z yields

```
[z]G   = (x+y) exp(x+2y) - y exp(y),
[z^2]G = (x+y)^2 exp(2x+3y)
          - (x+y)(x+3y) exp(x+2y)/2 + y^2 exp(y)/2.
```

Taking j!n! times the coefficient of x^j y^n proves, for d>=3, 0<=j<=d,

```
H_d(1,j) = (d+j) 2^(d-j-1) - d [j=0],
H_d(2,j) = 2^(j-2) 3^(d-j-2) [(2d+j)^2-4d-5j]
            + 2^(d-j-3) [(d+j)^2-(d+3j)-4(d-1)(d+j)]
            + C(d,2) [j=0].                          (4)
```

No face-vector identity or experimental extrapolation is needed for (3)-(4).
The separate face-vector construction in `problem.md` is useful for checks.

For j>=1, division gives the particularly simple expression

```
R_j := H_d(2,j)/H_d(1,j)
 = (3/2)^d (4/3)^j /18 [3d+j-5+d(d+1)/(d+j)]
    + [j-3d+1+2d/(d+j)]/4.
```

For j>=2, t=d+j, its difference is

```
R_j-R_{j-1}
 = (3/2)^d (4/3)^(j-1) /54
     [t+2d-2+d(d+1)(t-4)/(t(t-1))]
    + [1-2d/(t(t-1))]/4.                             (5)
```

Multiplying (5) by
`H_d(1,j-1) H_d(1,j)=t(t-1)2^(2(d-j)-1)` proves (1).
Here t>=d+2>=5, so each square bracket in (1) is strictly positive:
`t(t-1)>2d` and `t-4>0`. At j=1 the indicator corrections in (4) must
be retained. Substitution and collection give (2); its first term is
nonnegative for d>=3 and its other two terms are strictly positive.

Since every H_d(1,j)>0 for d>=3, (1)-(2) say that the ratios R_j, including
R_0, increase strictly. Summing consecutive ratio differences proves the
claim for arbitrary two columns. The original formula also gives
`H_d(i,j)=H_d(d-i,d-j)`: use L_r(z)=z^r L_r(1/z), and swap the roles of
s and t in the expression for P_{d,j}. Reversing both two-element index
lists leaves determinant sign unchanged, proving the reflected statement.

## Consequence and remaining gap

In no-swap Neville elimination of H_d^T, the first active multipliers are
`(d+j)/(2(d+j-1))`, j>=2. The next pivots are
`p_(j,2)=Delta(d,j)/H_d(1,j-1)>0`, j>=2. Thus the following multipliers
`p_(j,2)/p_(j-1,2)` are positive for every d>=3, 3<=j<=d.
This proves only these initial stages, not the general-order signs or the
second triangular elimination stage. Positive two-row minors do not imply
total nonnegativity of H_d.

The d=2 case is outside the strict statement: its rows {1,2} have zero
minor in columns {0,1}. There is no omitted counterexample to (1)-(2).

## Three-row flags: a further uniform positive family

Define

`F_3(d,j)=det H_d[{1,2,3},{j-2,j-1,j}]`.

Then **F_3(d,j)>0 for every d>=4 and 3<=j<=d**. This statement concerns
consecutive columns starting at 1 or later; it does not include columns
{0,1,2}, nor assert positivity of every order-three minor of H_d.

Here is an exact polynomial certificate and its sign argument. Write
`a=j-3`, `n=d-j`, and introduce formal independent variables u,v,w, to be
specialized at the end to

```
u=2^n,  v=2^j 3^n,  w=3^j 4^n.
```

The next coefficient of (3) is

```
[z^3]G = (x+y)^3 exp(3x+4y)
          -(x+y)^2(x+2y) exp(2x+3y)
          +(x+y)(x^2+5xy+7y^2) exp(x+2y)/6
          -y^3 exp(y)/6.                             (6)
```

For r=1,2,3 let T_(r,l)(x,y) be the degree-r polynomial multiplying
`exp(l*x+(l+1)*y)` in (3)'s coefficient of z^r, as explicitly displayed
above. In columns with positive index the l=0 term vanishes. For
`s=-2,-1,0`, replace H_d(r,j+s) by the polynomial

```
M_(r,s) = sum_{l=1}^r b_l (l/(l+1))^s
            sum_{p+q=r} [x^p y^q]T_(r,l)
              (a+3+s)_p (n-s)_q / [l^p(l+1)^q],       (7)
```

where b_1=u,b_2=v,b_3=w and `(x)_p=x(x-1)...(x-p+1)` is a falling
factorial. Formula (7) is just coefficient extraction from (6) and the
preceding two row formulas, so specialization recovers H_d exactly.

Expand D=det[M_(r,s)] in its three independent base variables. It has
precisely five groups:

```
D = u^3 P300 + u^2 v P210 + u^2 w P201
     + u v^2 P120 + u v w P111,                       (8)
```

where the P's are rational polynomials in a,n. Their complete coefficient
lists are in `research_third_flag.json`; the extraction and exact symbolic
expansion are reproducible with `research_third_flag.py`. Every coefficient,
including the constant, of P300, P201, P120, P111, and
`Q=P210+2P120` is positive. For orientation, the first and the repaired
polynomial are

```
P300=(2a+n+4)(4a^2+4an+16a+n^2+5n+12)/48,

20736 Q = 54a^5 + 261a^4 n + 2106a^4
 +429a^3 n^2 +5925a^3 n +16038a^3
 +324a^2 n^3 +5994a^2 n^2 +30627a^2 n +48438a^2
 +116a n^4 +2604a n^3 +18697a n^2 +56523a n +62964a
 +16n^5 +412n^4 +3656n^3 +15428n^2 +32760n +28512.
```

Thus (8) can be regrouped as

```
D = u^3 P300 + u^2 w P201 + u v w P111
     + u^2 v Q + u v (v-2u) P120.                    (9)
```

For a,n>=0 all five coefficient polynomials in (9) are strictly positive.
At the required specialization u,v,w>0 and
`v/u=2^j(3/2)^n>=8`, so every summand in (9) is positive. This proves
the stated infinite family. In particular, a mixed-sign coefficient in
P210 is not a negative minor; treating the base variables as unconstrained
positive numbers would lose the useful relation v>=8u.

The coefficient identity has a separate standard-library verifier in
`verify_third_flag.py`. Each side of (8), using (7), has separate degree
bounds (6,6,3,2,1) in (a,n,u,v,w). The verifier compares both sides at
every point of a full 7-by-7-by-4-by-3-by-2 integer grid, using rational
arithmetic. The 1,176 equalities prove the polynomial identity by repeated
univariate interpolation, since each grid size exceeds its degree bound.
The verifier also checks the coefficient identity Q=P210+2P120 and all
five positive coefficient lists, including their positive constants. Its
output is `verify_third_flag.json`. This finite verification is complete
for the specified polynomial identity; it is distinct from extending a
table of matrix dimensions by extrapolation. Both implementations belong
to the same research pass and do not constitute a fresh referee review.

The standard adjacent-minor identity, or a direct expansion of the next
Neville row operation, gives the subsequent pivot as
`p_(j,3)=F_3(d,j)/Delta(d,j-1)`. It is therefore positive for the stated
range; the ratios `p_(j,3)/p_(j-1,3)` are positive for j>=4. No assertion
about higher stages follows from this calculation alone.

## A precisely failed neighboring factorization

Let E_3 be the barycentric h-vector transformation in dimension 3, obtained
from its face-vector matrix `R(i,k)=i! S(k,i)` by the same h/f conjugation.
Then

```
E_3 = [[1,0,0,0], [4,4,2,1], [1,2,4,4], [0,0,0,1]],
E_3^(-1) H_3 = H_3 E_3^(-1)
 = [[1,0,0,0], [4/3,11/6,1/3,-1/6],
    [-1/6,1/3,11/6,4/3], [0,0,0,1]].
```

Both factor identities are checked exactly in `research_pivots.py` and
serialized in `research_pivots.json`. Since these residuals are unique and
have negative entries, a factorization H_d=E_d T_d or H_d=T_d E_d with
T_d TN for every d is impossible. This is an exact counterexample to those
specific subsidiary assertions. It neither refutes the frozen assertion
nor rules out other factorizations involving barycentric matrices.

## Verification status and limits

An initial exact check against the frozen double Stirling sum passed for
every d=3,...,16 and every j=1,...,d, including j=d and d=3. A reproducible
expanded check is recorded in `research_pivots.py` and `research_pivots.json`:
both rows and all adjacent minors agree with independent integer face-vector
sums for d=17,...,64 and d=96,128,192,256. All column pairs for the first
and reflected row pairs were checked directly for d=3,...,16.

The third-flag formula additionally agrees with the frozen definition for
all d=4,...,16 and with independent integer face-vector sums for
d=17,...,32 and d=64,128, in every allowed column position. The exact
polynomial-identity verification above is a separate, complete algebraic
check. No floating-point signs are used. An initial implementation of the
independent two-row face sum accidentally used 2^(r-1)-1 instead of
2^(r-1)+1; the mismatch assertion detected it, and the corrected script
was rerun successfully. This was an implementation error, not contrary
mathematical evidence.

No fresh referee has audited this dossier and no novelty or publishability
claim is attached to these low-row facts. Higher-order flag signs and the
second Neville elimination stage remain unproved. A concrete next test is
the analogous four-row flag for d>=5 and 4<=j<=d: expand using a=j-4,
n=d-j and b_l=l^j(l+1)^n, then seek a positive regrouping using the
rigorous ratios b_(l+1)/b_l>=((l+1)/l)^4 for l=1,2,3. A failed regrouping
would only be a failure of that certificate, not a negative determinant.
