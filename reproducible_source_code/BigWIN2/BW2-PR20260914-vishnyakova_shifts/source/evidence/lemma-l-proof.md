# A two-step sign lemma and all-even interval shape

Proposer job: primary-20260914-vishnyakova-shifts-research-1d29f50c8dec.
This is a proof submitted for a fresh mathematical referee, not an accepted
audit. The original conjunction remains unresolved because successive nesting
is not proved. No manuscript or output PDF is prepared in this research pass.

## 1. Precise operator theorem (includes the assigned equality case)

Let -3/10 <= t < 0 and let h have even degree d >= 2, positive leading
coefficient, and d distinct zeros in (-1,0). Define

    T_t p = z(1+z)p' + (z+t)p,
    S = h'(0)/h(0),  delta = (1+2t)/(1+t)^2,  Lambda = 1/(S+delta).

For every 0 < lambda <= Lambda, the polynomial

    q = T_t^2 p,  p = (z-lambda)h

has exactly d+2 distinct zeros in (-1,0) and one distinct positive zero.
All its zeros are simple. In particular this proves lemma L on its original
strip -b<t<0, b=1-1/sqrt(2), since b<3/10. The enlargement to -3/10 is
proved here; no assertion is made on the already refuted interval (-1/3,0).

The coefficient hypothesis has the exact form

    q_1 = (1+t)^2 h(0) [1-lambda(S+delta)] >= 0.

It is not replaced by a strict inequality in the argument below.

### 1.1 The extra sign to the right of all negative input zeros

Write h(z)=c product_i(z+a_i), where c>0 and 0<a_i<1. Put

    y = Lambda/2,  r_i = y/a_i,  R = sum_i r_i = yS = 1/2-delta*y,
    w_i = r_i/(1-r_i),  W = sum_i w_i,  V = sum_i w_i^2,
    eta = y/(y+lambda).

The following bounds are strict where indicated:

    40/49 <= delta <= 1,
    0 < y < Y := 1/[2(2+delta)] < 5/28,
    0 < R < 1/2,  0 < r_i < 1,  eta >= 1/3.

Indeed S=sum_i 1/a_i>d>=2, and y<1/(2S)<a_i/2. In particular -y lies
strictly between the largest negative zero of p and zero, and p(-y)<0.
Since r_i>y,

    W >= R/(1-y).

Cauchy--Schwarz, applied with weights r_i, gives the key bound

    W^2 = (sum_i r_i/(1-r_i))^2
        <= (sum_i r_i)(sum_i r_i/(1-r_i)^2) = R(W+V).

Consequently

    W^2-V <= W - ((1-R)/R)W^2.                         (1)

Set B=1-4y+2t and C=2y^2-(1+2t)y+t^2. Direct differentiation yields

    q/p = a^2 p''/p + a(1+4z+2t)p'/p
                         +2z^2+(1+2t)z+t^2,  a=z(1+z),

and, on evaluating at z=-y,

    q(-y)/p(-y)
      = (1-y)^2(W^2-V-2*eta*W) -(1-y)B(W-eta)+C.      (2)

The coefficient of eta in (2) is negative: by the bound on W,

    B-2(1-y)W <= B-2R = 2t+2(delta-2)y < 0.

Thus replacing eta by 1/3 gives an upper bound, including when
lambda=Lambda. Write

    K=(1-y)[5/3-14y/3+2t] > 0.

For completeness, the bracket is greater than
5/3-(14/3)(5/28)-3/5=7/30. By (1) and (2),

    q(-y)/p(-y) <= F(W)+(1-y)B/3+C,
    F(W)=(1-y)^2[W-((1-R)/R)W^2]-K W.

For W>=R,

    F'(W) <= (1-y)^2(2R-1)-K < 0.

We may therefore substitute the lower bound W=R/(1-y) into this last
upper bound. Expansion, using R=1/2-delta*y, gives

    q(-y)/p(-y) <= U_t(y),
    U_t(y) = t^2-t/3-1/4
       + (2*delta*t+2*delta/3-8*t/3-5/6)y
       + (delta^2-11*delta/3+10/3)y^2.                 (3)

Here U_t is convex in y, because its quadratic coefficient is
(delta-5/3)(delta-2)>0. At y=0,

    U_t(0)=t^2-t/3-1/4 <= -3/50 < 0

for -3/10<=t<=0. At the other endpoint Y=1/[2(2+delta)],

    U_t(Y) = N(t)/[3(2t^2+6t+3)^2],
    N(t)=12t^6+60t^5+89t^4+12t^3-60t^2-40t-7.        (4)

The denominator is positive: 2t^2+6t+3=(1+t)^2(2+delta)>0.
Here is an explicit finite identity establishing the sign of the numerator
on the entire required interval, rather than a numerical sample. For
u=1+(10/3)t in [0,1],

    N((3/10)(u-1)) = sum_(j=0)^6 B_j binom(6,j) u^j(1-u)^(6-j),

where, in order j=0,...,6,

    (B_j) = (-17519/125000, -273/500, -58837/50000,
             -10481/5000, -84/25, -5, -7).

Every coefficient is strictly negative, so (4) is negative, including both
t endpoints. Convexity and (3) now give q(-y)/p(-y)<0 for 0<=y<=Y.
Since p(-y)<0, we have proved the strict sign

    q(-y)>0.                                         (5)

No limiting argument in lambda was used; (5) holds at lambda=Lambda.

### 1.2 Completing the exact root count

Order the negative zeros of p as beta_1<...<beta_d. Put g=T_t p. Off the
zeros and endpoints,

    g/[z(1+z)p] = H(z)
       = sum_i 1/(z-beta_i) + 1/(z-lambda)
                                +t/z+(1-t)/(1+z).

For -1<z<beta_d away from the poles, H'(z)<0. In fact the only positive
term in H' is -t/z^2, and it is strictly dominated by
-1/(z-beta_d)^2 since |z-beta_d|<|z| and -t<1.

It follows that each of the d intervals

    (-1,beta_1), (beta_1,beta_2), ..., (beta_(d-1),beta_d)

contains exactly one simple zero xi_i of g: H decreases from positive to
negative infinity there. At that zero,

    g'(xi_i)=xi_i(1+xi_i)p(xi_i)H'(xi_i),

so sign g'(xi_i)=sign p(xi_i)=(-1)^i. Therefore

    sign q(xi_i)=(-1)^(i+1).

Also q(-1)=(t-1)^2 p(-1)<0, q(0)=t^2 p(0)<0, and xi_d<beta_d<-y<0.
These signs and (5) give one zero of q in each of the following disjoint
intervals:

    (-1,xi_1), (xi_1,xi_2), ..., (xi_(d-1),xi_d),
    (xi_d,-y), (-y,0), (0,infinity).

The first d+2 are negative; the last exists because q has positive leading
coefficient. Its degree is d+3, so these d+3 distinct roots exhaust its
degree and all are simple. This proves the operator theorem.

## 2. Odd shifted powers on a full parameter interval

Define Q_(n,t) exactly as in source.md. The binomial identity
x binom(x,j)=j binom(x,j)+(j+1)binom(x,j+1) gives

    Q_(0,t)=1,  Q_(n+1,t)=T_t Q_(n,t).

Parameter differentiation, endpoint evaluation and the leading coefficient
give, for all n>=1,

    partial_t Q_(n,t)=n Q_(n-1,t),
    Q_(n,t)(0)=t^n,  Q_(n,t)(-1)=(t-1)^n,  [z^n]Q_(n,t)=n!,
    [z]Q_(n,t)=(1+t)^n-t^n.

The endpoint at -1 also follows immediately from the recurrence. Reflection
is Q_(n,t)(-1-z)=(-1)^n Q_(n,1-t)(z), obtained by substituting in that same
recurrence and starting with Q_0=1.

**Odd-degree theorem.** For every odd m>=1 and -3/10<=t<0, Q_(m,t) has
m-1 distinct roots in (-1,0) and one distinct positive root.

For m=1 this is Q_1=z+t. For m=3,

    Q_3=6z^3+6(1+t)z^2+(3t^2+3t+1)z+t^3,
    disc_z Q_3=-12(18t^6-54t^5+36t^4+18t^3-12t^2-6t-1).

The discriminant has the following strictly positive degree-six Bernstein
coefficients after t=(3/10)(u-1):

    (495087/125000, 103179/25000, 11616/3125,
     10209/2500, 708/125, 42/5, 12).

Thus Q_3 has three distinct real roots throughout [-3/10,0]. For t<0,
its positive nonconstant coefficients give exactly one positive root, and
its constant term is nonzero. Reflection excludes roots at or below -1:
all coefficients of Q_(3,1-t)(z) are positive when 1-t>1. This proves the
base m=3 with precisely the stated locations.

Suppose the result holds for an odd m>=3 and factor Q_m=(z-lambda)h.
The h hypotheses of Section 1 hold. For q=Q_(m+2,t),

    q_1=(1+t)^(m+2)-t^(m+2)>0,

because 1+t>0 and m+2 is odd. The coefficient identity in Section 1 then
gives lambda<1/(S+delta). The operator theorem applies and completes the
induction. This proves the all-degree assertion O, and a slightly larger
strip, rather than a new finite discriminant prefix.

## 3. Consequence for the original even-degree sets

**Partial resolution.** For every even n>=2 there is a constant c_n with

    M_n=[-c_n,1+c_n],
    (sqrt(2)-1)/2 <= c_n < b=1-1/sqrt(2).

At t=-c_n the polynomial Q_(n,t) has exactly one double zero r in (-1,0),
all other zeros are simple and smaller than r, and

    partial_z^2 Q_(n,t)(r)>0,
    partial_t Q_(n,t)(r)<0.

The reflected endpoint has the corresponding reflected configuration.
This proves interval shape, closed endpoint membership, and the bound in
the original conjunction. It does not prove c_n<=c_(n+2).

Here are all the dependencies and the interval argument. The TP equivalence
with all zeros of Q in [-1,0], reflection, the quadratic value
c_2=(sqrt(2)-1)/2, and polynomial multiplication closure are given in the
original primary source (equations (3)--(8), Statement 2.1, Example 5.3,
and Theorem C). The full versioned primary text is frozen as
`evidence/external/2607.06207v1.html`. Multiplication closure gives M_2
contained in M_n for even n. The interior [0,1] assertion also follows
directly from the recurrence: for 0<t<1 all endpoint residues in H are
positive when the input zeros are in (-1,0), giving one simple zero in
each successive interval; start from Q_1=z+t. Continuity includes t=0,1.

For completeness, the elementary outer restriction from
`evidence/triage-exact.md` is repeated here. Admissibility of Q for even n
implies [z]Q=(1+t)^n-t^n>=0, hence t>=-1/2. The Toeplitz minor with rows
(0,1) and columns (1,2) is nonnegative only if

    (1+t)^(2n) >= t^n(2+t)^n.

For -1/2<=t<0 this requires (1+t)^2>=-t(t+2), or t>=-b.
At t=-b, put a_j=(j-b)^n. Then a_1^2=a_0*a_2>0, and the minor with
rows (0,1,2) and columns (1,2,3) equals a_0^2*a_3-a_1^3<0. The strict
inequality follows from a_1*a_3<a_2^2, since (1-b)(3-b)<(2-b)^2.
Reflection gives

    M_n subset (-b,1+b).

The set M_n is closed (either use its defining minors or continuity of the
roots with fixed leading coefficient), and therefore compact.

Fix even n>=4, -b<t<0, and suppose f=Q_n is admissible with a multiple
root. The odd-degree theorem gives g=Q_(n-1) with n-2 simple negative
zeros beta_i and one positive zero lambda. The logarithmic derivative H
in Section 1.2, now for f=T_t g, gives n-2 simple roots of f, one in
each interval to the left of beta_(n-2). The endpoint evaluations are
nonzero, and f cannot vanish at a beta_i because g'(beta_i) is nonzero.
Thus every multiple root must be in (beta_(n-2),0). Only two degrees
remain: there is exactly one double root r and all other roots are simple
and smaller than r. Factoring f gives

    f''(r)=2*n! product_(other roots gamma)(r-gamma)>0,
    partial_t f(r)=n*g(r)<0.

The second inequality follows because all negative-root factors of g are
positive at r and its positive-root factor is negative. For n=2 these
facts follow from the displayed quadratic formula in the primary source.

The local quadratic factor at such a collision has two simple real roots
immediately to the right in t, and a nonreal conjugate pair immediately
to the left, since its squared root displacement has leading coefficient
-2*partial_t f(r)/f''(r)>0. The other simple roots persist in (-1,0).
Consequently an admissible multiple-root parameter is a left endpoint,
never an isolated point or a right endpoint, of exterior admissibility.
An admissible parameter with only simple roots is an interior point.

There are finitely many collision parameters: the discriminant in t is a
polynomial not identically zero, since Q_(n,1/2) has simple roots by the
interior recurrence just proved. Thus on (-b,0] there is exactly one
admissible component, of the form [-c_n,0]. Closedness and the excluded
endpoint -b give c_n<b; M_2 subset M_n gives c_n>=c_2>0. Reflection
and [0,1] complete the interval assertion. The left boundary must be a
multiple-root parameter, so the stated endpoint configuration follows too.

## 4. Verification and scope

`lemma-l-check.py` and `lemma-l-check.json` verify the rational algebraic
identities, both full-interval Bernstein certificates, and separately
specified rational operator inputs. The finite root counts are regression
tests of the argument, not a replacement for its quantified proof. No
agents or additional model processes were used. The proposer has no known
gap in the statements proved above; a fresh referee is still required.

Novelty is assessed only against the primary sources and search scope in
`literature/research-pass-3.md`. The claimed payoff is the all-degree
interval part of Conjecture 5.8, not the already known quadratic case or
the elementary minor bound alone. Successive even-degree nesting remains
the explicit unresolved part of the immutable original problem.
