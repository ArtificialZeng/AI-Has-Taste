# Research pass 3: a coefficient obstruction for antiprism flags

Job: `primary-20260914-antiprism-total-positivity-research-dee875af8862`.
Completed research argument, 2026-09-14; proposed result-note scope awaiting
a fresh referee. The original all-order total-nonnegativity problem is
unresolved. This is a proof dossier, not a manuscript or acceptance report.

## Exact subsidiary result

The polynomial below is exactly the one frozen in
`flag-coefficient-hypothesis.md` before the order-six test. The coefficient
assertion originated in this project; it is not attributed to the authors
of the primary papers.

For k>=1 let K=k(k+1)/2. Use the falling factorial
`(v)_p=prod_(h=0)^(p-1)(v-h)`, with `(v)_0=1`, and define

```
T_(r,l)(x,y)=[t^r] exp(-ty)(1-exp(-t(x+y)))^l,
w_l=z_1+...+z_l,
b_l=l^k*w_l,
q_l=l/(l+1),
M_(r,s)=sum_(l=1)^r b_l*q_l^s
         sum_(p+q=r) [x^p y^q]T_(r,l)(x,y)
         *(a+k+s)_p*(n-s)_q / (l^p*(l+1)^q),
R_k=det M, with rows r=1,...,k and columns s=1-k,...,0.
```

All variables a,n,z_1,...,z_k are algebraically independent. Write

`lambda_k=(prod_(r=1)^k r!)/(prod_(l=1)^k l^l)>0`.

**Theorem.** For every integer k>=5,

```
[a^(K-1) n^0 z_1^5 z_6...z_k] R_k
 = -lambda_k*(125k^4-9555k^3+17736k^2-346478k+858264)/20736.       (1)
```

The product z_6...z_k is 1 when k=5. The coefficient in (1) is strictly
negative for every integer k>=76. A smaller separately certified example is

```
[a^252 n^0 z_1^9 z_10...z_22] R_22
 = -lambda_22*4429926944297146258237/14051921264640000000 < 0.      (2)
```

For every k>=1 the coefficient of
`a^(K-1) n^0 z_1 z_2...z_k` is
`lambda_k*k(k+1)(2k+1)/6>0`. Thus the degree-K-1 component has both signs
for every k>=76, and also at k=22. We do not classify every other coefficient
or claim that 22 is the first order with any negative coefficient.

This refutes the frozen assertion that **every** coefficient of R_k is
nonnegative for every k. It proves an obstruction only to that specific
coefficient-positivity certificate in the specified variables. It does not
rule out other parametrizations, cancellations on the actual parameter
set, planar networks, or other proofs of the original matrix assertion.

## Relation to the immutable matrix formula

The following derivation also checks that the auxiliary determinant has
not changed meaning. Let H_d be exactly as in `source.md` and `problem.md`.
Summing that defining formula gives the formal identity

```
G(x,y,t)=sum_(j,n>=0) sum_(r=0)^(j+n)
 H_(j+n)(r,j)*t^r*x^j*y^n/(j!n!)
 = exp(tx+y)/(1-(exp(t(x+y))-1)(exp(x+y)-1)).                    (3)
```

For completeness, put p=i-s and q=r-i+s in the original double sum,
so r=p+q. After summing j,n, the binomial factors contribute
`x^s/s! * exp(y)*(x+y)^(p+q)/(p!q!)`. Summing s gives exp(tx);
summing p,q for each Stirling index l gives
`(exp(t(x+y))-1)^l*(exp(x+y)-1)^l`. Summing l yields (3).
All manipulations are formal power series with finite coefficient sums.

Rewriting (3) gives

`G=exp(y-ty) sum_(l>=0) exp(l(x+y)) (1-exp(-t(x+y)))^l`.

Hence its t^r coefficient is
`sum_(l=0)^r T_(r,l)(x,y)*exp(l*x+(l+1)*y)`.
The l=0 term has no x dependence, and vanishes in the positive column
indices j+s>=1 under consideration. Coefficient extraction therefore
gives M_(r,s)=H_d(r,j+s) when

```
a=j-k>=0, n=d-j>=0,
b_l=l^j*(l+1)^n,
z_1=2^n,
z_l=l^a*(l+1)^n-(l-1)^a*l^n >=0  (l>=2).
```

The actual specialization has z_1>0 and the other z_l>=0. A negative
formal coefficient is not a negative value at this specialization.
Neither (1) nor (2) supplies a negative minor of H_d.

## The entire next-degree component

Set `u_l=a/l+n/(l+1)` and let A be the lower triangular k by k matrix
`A_(r,l)=T_(r,l)(a/l,n/(l+1))` for l<=r, zero otherwise.
Since T_(l,l)=(x+y)^l, its diagonal entries are u_l^l.
Let B=diag(b_1,...,b_k), and let V_(l,s)=q_l^s in the column order above.
Define

```
C=k*d_a A-(a/2)*d_a^2 A-(n/2)*d_n^2 A,
E=(d_a-d_n)A,
F=A^(-1)E,
W=V diag(1-k,...,0) V^(-1).
```

These rational-function matrices are used only where algebraic inversion
is valid; the identities obtained extend as polynomial identities.
Expanding the falling factorials shows that the degree-r part of row r
of M is row r of L=ABV. Its degree-(r-1) part is row r of

`N=CBV+EBV diag(1-k,...,0)`.

Indeed,
`(a+k+s)_p=a^p+(p(k+s)-p(p-1)/2)*a^(p-1)+lower`, and
`(n-s)_q=n^q+(-qs-q(q-1)/2)*n^(q-1)+lower`.
Their first corrections are exactly the derivative operators in C+sE.

Every term in det M has (a,n)-degree at most K. Its degree K term is

`P_k=det L=(prod_(r=1)^k r!)*prod_(l=1)^k u_l^l*w_l`.             (4)

To evaluate det V, factor q_l^(1-k) from row l and use the ordinary
Vandermonde determinant at the distinct increasing nodes q_l. This gives
`det V=prod_(p<q)(q-p)/prod_(l=1)^k l^(k-1)`; after multiplying by
prod b_l the scalar is `k!*prod_(p<q)(q-p)=prod_(r=1)^k r!`.

The degree K-1 term chooses one row of N and all other rows of L.
The determinant derivative identity, valid over the rational function
field, consequently gives the complete expression

```
[R_k]_(K-1)=P_k*(tr(A^(-1)C)
 +sum_(1<=l<=i<=k) F_(i,l)*W_(l,i)*(l/i)^k*w_l/w_i).             (5)
```

This is an exact formula for every k, without a claimed global sign rule.
The lower triangularity of F accounts for the restriction l<=i.

## Coefficient extraction from (5)

Now put n=0 and take the coefficient of a^(K-1). Homogeneity permits
evaluating the rational factor in (5) at a=1,n=0. Formula (4) contributes
`lambda_k*a^K*prod_l w_l`.

Write H_v=sum_(h=1)^v 1/h, with H_0=0. Lagrange interpolation of the
functions q^(1-k),...,1, or differentiation of their Vandermonde matrix,
gives

```
W_(l,l)=(l+1)*(l*(H_(l-1)-H_(k-l))-(k-1)),
(l/i)^k W_(l,i)
 =(-1)^(i-l+1)*l*(l+1)/(i-l)
  *binom(k-l,i-l)/binom(i,i-l),  l<i.                            (6)
```

For a direct check of the off-diagonal formula, set
`L_i(q)=prod_(h!=i)(q-q_h)/(q_i-q_h)`. Then
`W_(l,i)=q_l*(q_i/q_l)^(k-1)*L_i'(q_l)` for l!=i. Inserting
`q_l-q_h=(l-h)/((l+1)(h+1))` gives (6), including its sign.
The same differentiation gives the displayed diagonal.

At a=1,n=0 the diagonal entries needed in (5) are

`(A^(-1)C)_(l,l)=kl-l(l-1)/2` and `F_(l,l)=l/(l+1)`.

Their combined sum is

```
sum_(l=1)^k (l*(3-l)/2+l^2*(H_(l-1)-H_(k-l)))
 = k(k+1)(2k+1)/6.                                             (7)
```

For example, combine the harmonic terms in pairs p<q:
`sum_l l^2*(H_(l-1)-H_(k-l))=sum_(p<q)(q^2-p^2)/(q-p)
=sum_(p<q)(p+q)=(k-1)*k(k+1)/2`. This proves (7).

The coefficient of `z_1^m*z_(m+1)...z_k` in prod_l w_l is 1.
In `(prod_h w_h)*w_l/w_i`, for l<i, it is 1 if i<=m and 0 otherwise.
To see this, assign z_k to its only possible factor w_k, then z_(k-1)
to w_(k-1), and proceed down to m+1. A missing w_i in that range makes
the assignment impossible; otherwise every remaining factor must supply
z_1. This proves, for every 1<=m<=k,

```
[a^(K-1) n^0 z_1^m z_(m+1)...z_k]R_k = lambda_k*S_(k,m),
S_(k,m)=k(k+1)(2k+1)/6
 +sum_(1<=l<i<=m) (-1)^(i-l+1)*l*(l+1)/(i-l)
  *binom(k-l,i-l)/binom(i,i-l)*F_(i,l)(1,0).                     (8)
```

The case m=1 proves the asserted positive coefficient.

## A finite table proves the uniform negative family

There is no numerical extrapolation in the following step. The matrices
needed for the first five rows of F have exact entries

```
A_(r,l)(1,0)=(-1)^(r-l)*l!*S(r,l)/(r!*l^r),
E_(r,l)(1,0)=(-1)^(r-l)*(l-1)!*S(r-1,l-1)
             /((l+1)*(r-1)!*l^(r-1)).
```

The first formula follows from T and the Stirling exponential identity.
For the second, differentiating the defining generating function for
A_(r,l) in the direction d_a-d_n gives

`(t/(l+1))*exp(-t*n/(l+1))*(1-exp(-t*u_l))^(l-1)`.

Solving AF=E by forward substitution yields this exact lower triangular
table through order five (omitted entries are zero):

```
 1/2
 1         2/3
 9/8       9/8          3/4
 4/3       8/9          32/27        4/5
 625/432   3125/3456    3125/3888    625/512    5/6
```

These entries are independent of k once k>=5, since A and E are lower
triangular. Substituting the ten off-diagonal entries into (8) for m=5
and expanding the binomial polynomials proves (1). The verifier checks
both AF=E and the **entire** polynomial identity coefficient by coefficient.

Let Q(k)=125k^4-9555k^3+17736k^2-346478k+858264. The exact identity

`Q(76+t)=125t^4+28445t^3+2171196t^2+56268354t+52825392`

has positive coefficients. Thus Q(k)>0 for every real k>=76, proving
the claimed negative coefficients for every integer k>=76. In particular
S_(76,5)=-122281/48. No assertion about a minimal uniform threshold is
needed. This completes the proof of (1) and its sign conclusion.

## Exact finite certificates and their separate verification

`research_next_degree.py` computes the general finite table in (8) by
signed binomial power sums and forward substitution. Its complete search
of the named family covers 2<=k<=32, 1<=m<=k, with a^(K-1) and n^0
only. The first negative value **in that search** occurs at (k,m)=(22,9)
and is (2). Another is
`S_(25,7)=-146636521787/933120000`. The full search and exact rational
witnesses are in `research_next_degree.json`.

`verify_next_degree.py` independently extracts (2) directly from det M,
without using F, W, or formula (8) for the numerical extraction. For the
chosen z monomial, the row support l<=r forces row r>m to use its z_r
coefficient; every earlier row supplies z_1. Form a new k by k matrix by
keeping only l=r in rows r>m and retaining all l<=r in the earlier rows.
Its determinant is exactly the selected z coefficient of R_k. This
row-forcing argument proves the completeness of the extraction.

At n=0, only `[x^r]T_(r,l)` and `[x^(r-1)y]T_(r,l)` can contribute
to its two highest powers of a. The verifier derives them from a Stirling
recurrence, clears rational denominators row by row, and sums the k
integer determinants formed by replacing exactly one leading row with
its next coefficient. Bareiss elimination computes every determinant
exactly, with every division checked. Their numerators and the common
denominator are serialized in `verify_next_degree.json`.

This directly confirms the full coefficient (2) and the order-25 example.
The same extraction also agrees with three coefficients in the complete
order-five and order-six certificates from pass 2: (k,m)=(5,5),(6,3),(6,6).
Their normalized values are 48343/648, 405/4, and 135708089/1080000.
In addition, the verifier checks the five-row table, the quartic identity,
and its shift at 76 in exact rational polynomial arithmetic. Hence the
uniform assertion is supported by a proof and exact identity checks,
not by extrapolating the finite search.

Reproduce from the project root:

```
python3 evidence/research_next_degree.py
python3 evidence/verify_next_degree.py
```

Both scripts belong to this research context. Separate arithmetic
implementations are not a fresh referee or external peer review.

## Scope, dependencies, and remaining gap

The claim relies on elementary formal-series extraction, determinant
multilinearity, Vandermonde/Lagrange interpolation, and the displayed
finite rational identities. No unproved positivity statement from a prior
pass is used in the proof of (1). The smaller example (2) additionally
uses the complete exact coefficient-extraction certificate above.
Known mathematical gaps in this stated subsidiary theorem: none identified
by the proposer; independent scrutiny is still required.

The closest primary results and the bounded literature comparison are in
`literature/research-pass3-verification.md`. The proposed contribution is a
specific uniform obstruction to the project-generated certificate strategy,
with an explicit lower-order witness. Its significance as a result note
must be assessed by the fresh referee. It neither resolves a published
antiprism conjecture nor supplies a general obstruction to proving TN.

The original gaps (arbitrary-order matrix flags, missing column-zero flags,
and the further Neville stage) remain. The prior positive order-five and
order-six polynomial identities are compatible with this counterexample.
The old next test has changed status: its coefficient-nonnegativity target
is false, so attempting to prove it for all k should stop.

One next test: a fresh referee should rederive the row-forcing extraction,
recompute the order-22 coefficient, and check the symbolic m=5 identity
and positivity of Q(76+t), while deciding whether this precisely limited
method obstruction is substantial enough for a result note.
