# Exact triage evidence

Job: primary-20260914-vishnyakova-shifts-triage-b88a2e27f2c3.
Reproduce with `python3 evidence/triage-exact.py`; output is
`evidence/triage-exact.json`. All decisions use exact rational or symbolic
arithmetic. This is a local calibration and argument, without independent
referee acceptance or a novelty claim.

## Normalization and known quadratic calibration

Newton inversion gives Q_(n,t) as specified in problem.md. Directly summing the
generating series in the binomial basis gives
S_(n,t)(x)=(1-x)^n Q_(n,t)(x/(1-x)). The script independently assembles the
numerator coefficients and checks this identity symbolically for n=1,...,6.
The general identity follows from
sum_(k>=0) binomial(k,j)x^k=x^j/(1-x)^(j+1).

Q_(2,t)=2z^2+(2t+1)z+t^2, with discriminant 1+4t-4t^2.
Its real-rooted parameter interval is [(1-sqrt(2))/2,(1+sqrt(2))/2].
The roots there are in [-1,0]: the coefficient 2t+1 is positive, and reflection
gives the same assertion at 1-t. The repeated boundary roots are
-(2t+1)/4, strictly inside (-1,0). This is the known source Example 5.3 case.

## A useful elementary restriction

For even n, admissibility requires the coefficient of z in Q to be nonnegative:
(1+t)^n-t^n >= 0, hence t>=-1/2. Reflection requires t<=3/2.
The Toeplitz minor with rows (0,1) and columns (1,2) additionally requires
(1+t)^(2n) >= t^n(2+t)^n. On -1/2<=t<0 this is equivalent to
(1+t)^2 >= -t(t+2), or t>=-1+1/sqrt(2).
Thus, putting b=1-1/sqrt(2), M_n subset [-b,1+b] for every even n.

In fact both exterior endpoints are excluded. At t=-b the first minor vanishes,
so a_1^2=a_0 a_2 with a_0,a_1,a_2>0. The minor with rows (0,1,2) and columns
(1,2,3) equals a_0^2 a_3-a_1^3. It is strictly negative, since
a_1 a_3<a_2^2: indeed (1-b)(3-b)<(2-b)^2 and all bases are positive.
Reflection excludes 1+b. This is an elementary consequence of necessary minors;
no publication value or novelty is claimed for this bound.

## Complete quartic calibration

Write
Q_(4,t)=24z^4+(24t+36)z^3+(12t^2+24t+14)z^2
        +(4t^3+6t^2+4t+1)z+t^4.
Its discriminant is
24(4v-5)H(v), v=(t-1/2)^2,
where H(v)=3456v^5-9504v^4+11304v^3-7046v^2+2378v-361.

The exact Sturm variations for H at -infinity, 0, +infinity are 3,3,2.
Consequently H has precisely one real root v_*, and it is positive. The script
isolates it in (42488/77697,77417/141571), a subinterval of (1/4,1).
Define alpha=1/2-sqrt(v_*); then -240/1000<alpha<-239/1000.

Here is the completeness argument, beyond the sampled root counts. The necessary
restriction [-1/2,3/2] gives 0<=v<=1. On that range 4v-5 is negative, and the
unique-root assertion for H implies that the discriminant is positive precisely
on alpha<t<1-alpha and negative on the two exterior portions of [-1/2,3/2].
Negative discriminant excludes four real roots. At t=1/2, exact Sturm counting
gives four roots in [-1,0]. Throughout the connected central open interval the
discriminant never vanishes and the leading coefficient is the constant 24;
the four simple real roots therefore persist there.

Their locations follow without assuming a sign for the discriminant suffices:
all coefficients of Q_(4,t) are nonnegative for -1/2<=t<=3/2. In particular,
the linear coefficient is (1+t)^4-t^4>=0, the quadratic coefficient is
12(t+1)^2+2>0, and the cubic coefficient is positive. Thus no real root is
positive. Applying the same argument to 1-t and using
Q_(4,1-t)(z)=Q_(4,t)(-1-z) excludes roots below -1. Continuity of roots with
constant leading coefficient includes the two boundary values. Hence the
quartic calibration establishes M_4=[alpha,1-alpha].

This low-degree conclusion does not resolve the frozen all-degree conjunction.
Its stand-alone novelty and significance have not been established. The global
shortcut "positive discriminant implies admissible" fails already at t=-1:
the discriminant is positive but the exact count in [-1,0] is zero.

## A precise next mechanism to test

The binomial identity x*binomial(x,j)=j*binomial(x,j)+(j+1)*binomial(x,j+1)
and parameter differentiation give, for all n>=0,
Q_(n+1,t)=(z+t)Q_(n,t)+z(1+z) partial_z Q_(n,t),
and partial_t Q_(n,t)=n Q_(n-1,t) for n>=1. The script checks both through n=6.
These are structural identities, not evidence of the desired sign condition.

At a simple collision (t_0,r) with Q=partial_z Q=0 and partial_z^2 Q != 0,
Taylor expansion gives the leading squared root displacement
-2(partial_t Q)/(partial_z^2 Q) * (t-t_0).
The proposed next test is to isolate the admissible exterior double-root
configurations of Q_(6,t), -b<t<0, -1<r<0, and determine the sign of
sigma=-(partial_t Q)/(partial_z^2 Q), with multiplicities checked separately.
If sigma is positive at every such collision, it supports a specific uniform
one-direction boundary-crossing lemma; a zero or negative sign identifies a
failure of that proposed mechanism. Finite evidence does not prove the lemma.
