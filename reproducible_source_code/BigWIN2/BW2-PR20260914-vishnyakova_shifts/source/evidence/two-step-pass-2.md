# Two-step recurrence: obstruction, finite strips, and a revised kernel

Job: primary-20260914-vishnyakova-shifts-research-2008cf198145.
Reproduce the exact certificates with `python3 evidence/two-step-pass-2.py`.
The output is `evidence/two-step-pass-2.json`. No statement below resolves
the frozen even-degree conjunction. No novelty or independent review is asserted.
The separate `two-step-sturm-check.py` recomputes all three generic-operator
counterexamples using only Python's Fraction class, the coefficient recurrence,
and Euclidean polynomial division. Its output `two-step-sturm-check.json`
agrees with the symbolic implementation's root counts. This is a second
implementation, not a fresh mathematical referee.

## The assigned infinite claim

Write b=1-1/sqrt(2) and

    T_t p = z(1+z)p' + (z+t)p.

The auxiliary assertion O says that every odd Q_(m,t), -b<t<0, has m-1
simple roots in (-1,0) and one simple positive root. It is still unproved
in all degrees. The original recurrence gives Q_(m+2,t)=T_t^2 Q_(m,t), with

    T_t^2 p = a^2 p'' + a(1+4z+2t)p'
              + [2z^2+(1+2t)z+t^2]p,   a=z(1+z).

This identity alone does not propagate the root configuration.

## Exact obstruction to a configuration-only induction

At t=-29/100 (strictly inside (-b,0)), take

    p=(z+51/100)(z+49/100)(z-1/2).

Its two negative roots and positive root are simple and in the specified
regions. Nevertheless

    T_t^2 p = 20z^5 + (792/25)z^4 + (24947/2000)z^3
              + (833/500000)z^2 - (17855441/100000000)z
              - 2101659/200000000

has exactly two roots in (-1,0), one positive root, and two nonreal roots.
The JSON contains its exact negative discriminant and its rational Sturm
sequence sign variations at -infinity, -1, 0, and infinity. The polynomial
is squarefree. Thus this is an exact counterexample to the assertion that
T_t^2 preserves the mixed root configuration for arbitrary inputs.

There is also a witness of the degree specified in the assigned test:

    p_7=(z-1/1000) product_(j=995)^1000 (z+j/10^6),   t=-29/100.

All seven input roots are simple, with six in (-1,0) and one positive.
T_t^2 p_7 is a squarefree degree-nine polynomial with exactly six roots in
(-1,0), one positive root, and two nonreal roots. Full rational coefficients,
discriminant, and Sturm signs are serialized. These witnesses have negative
linear coefficients. Neither is Q_(m,t), so neither refutes O or the original
conjecture. The proved obstruction concerns only the stated unrestricted
root-configuration preservation claim; it excludes no stronger induction.

## A uniform fact specific to the powers

**Proposition.** For every odd m>=1 and -1<t<0, all nonconstant coefficients
of Q_(m,t) are strictly positive. Consequently it has exactly one positive
root, that root is simple, and it has no real root at or below -1.

**Proof.** The coefficient c_j of z^j is the jth forward difference of x^m
at t. Repeated use of the fundamental theorem of calculus gives, for 1<=j<=m,

    c_j = m!/(m-j)! integral_[0,1]^j (t+u_1+...+u_j)^(m-j) du.

If m-j is even, the integral is strictly positive. If m-j is odd, then j
is even and j>=2. Put A=t+j/2>0 and V=sum u_i-j/2. The distribution of V
under uniform integration is symmetric. Expanding (A+V)^(m-j), only even
powers of V survive integration; their coefficients are positive, and the
constant term is strictly positive. Again c_j>0. Also c_0=t^m<0.

Hence Q_(m,t)'(z)>0 for z>=0. The value at zero is negative and the leading
coefficient is m!>0, giving exactly one simple positive root. Finally the
reflection identity is

    Q_(m,t)(-1-z)=(-1)^m Q_(m,1-t)(z).

At 1-t>1, every coefficient of the latter polynomial is positive by the same
integral formula, now with a positive integrand. For odd m this makes the
left side negative for every z>=0, excluding all roots at or below -1. QED.

In particular, within O's strip, O is equivalent to simple real-rootedness
of Q_(m,t): the locations and the unique positive root then follow from this
proposition and Q_(m,t)(0)=t^m. This equivalence concerns only O, not the
original even-degree conjecture.

## Four new whole-strip finite results

For each m in {7,9,11,13}, O holds on the larger strip [-1/3,0). The script
assembles Q_m by the recurrence and independently checks it against the original
Newton finite-difference formula. The primitive discriminants in t have degrees
42, 72, 110, and 156, respectively. Each has exactly zero roots in [-1/3,0]
by exact Sturm counting. The JSON includes the full primitive discriminants
and endpoint sign variations, rather than only a Boolean success indicator.

At t=-1/3, the squarefree specialized polynomial has m-1 roots in (-1,0)
and one positive root, certified by Sturm counting. A fixed leading coefficient
m! prevents escape to infinity. In the parameter interval a real pair cannot
become nonreal without a discriminant zero, and a root cannot cross 0 or -1
because Q_m(0)=t^m and Q_m(-1)=(t-1)^m are nonzero for -1/3<=t<0.
Therefore the sample root counts persist throughout that half-open strip.
The endpoint t=0 is excluded from O and is not silently added.

Combined with the complete conditional collision argument in
`odd-strip-reduction.md`, these finite statements imply interval shape for
M_8, M_10, M_12, and M_14, with 0<c_n<b. They do not prove nesting between
these degrees, and do not prove the infinite assertion O.

## Revised sufficient induction lemma L (unproved, version 1)

The counterexamples above omit an exact coefficient constraint satisfied by
the power family. This motivates the following distinct, stronger-input claim:

For every -b<t<0, every even integer d>=2, and every real polynomial h of
degree d with positive leading coefficient and d simple roots in (-1,0), put

    S=h'(0)/h(0),    delta=(1+2t)/(1+t)^2.

If 0<lambda<=1/(S+delta), then

    T_t^2[(z-lambda)h]

has d+2 simple roots in (-1,0) and one simple positive root. This includes
the equality case in the coefficient constraint. There is no claim that L
has been proved, is optimal, or is equivalent to O.

**Why L would suffice.** Let p=(z-lambda)h, and write p_j and q_j for the
coefficients of p and q=T_t^2 p. Direct coefficient extraction gives

    q_1=(1+t)^2 p_1+(1+2t)p_0
       =(1+t)^2 h(0)[1-lambda(S+delta)].

Thus L's additional hypothesis is exactly q_1>=0. For p=Q_(m,t) already
satisfying O, the factor h has even degree m-1. The proposition above applied
to Q_(m+2,t)=q gives q_1>0, so L's hypothesis holds strictly. Starting from
the previously certified degree-three whole strip, L would prove O in all
odd degrees by induction (degree one is immediate). The prior collision
reduction would then give interval shape in all even degrees. Successive
even-degree nesting would remain a separate gap.

For additional clarity, within this strip q_1>=0 also forces all the other
nonconstant coefficients of q to be positive when p has the stated roots.
Indeed p_1>0 since delta>0; real-rootedness and interlacing then put every
root of p' below zero, so every p_j with j>=1 is positive. The coefficient
formula

    q_j=(j+t)^2 p_j+j(2j+2t-1)p_(j-1)+j(j-1)p_(j-2)

is positive for j>=3. For j=2, use p_1>=(1+2t)(-p_0)/(1+t)^2 to obtain

    q_2 >= (t+2)^2 p_2
            + [2(3(1+t)^2-1)/(1+t)^2](-p_0)>0,

since (1+t)^2>1/2. This is a coefficient consequence, not a proof of L.

## Exact attacks on L and their limits

The statement of L was fixed before the saved exact tests. All 639 tests pass.
Parameters were -1/10000, -29/100 and -292893/1000000; the last is strictly
inside and close to -b, verified by (1+t)^2>1/2. Negative input roots use
all subsets of sizes 2,4,6 of a seven-point rational grid, plus separately
clustered families of sizes 2,4,6,8 near zero and near -1. The positive root
is 1/1000, 3/4, or 1 times its allowed upper bound. Thus tests include the
coefficient-equality boundary q_1=0. Every case has exact root counts and a
squarefreeness check in the JSON. This is finite support only: no parameter
interval or arbitrary degree is covered by these tests of L.

The extension of L to the larger interval -1/3<t<0 is exactly false. At

    t=-333/1000,  p=(z+9/10)(z+99/100)(z-1/3),

L's root and strict coefficient hypotheses hold, including
q_1=16918029/1000000000>0. But q=T_t^2 p has only two negative roots and one
positive root, with a nonreal pair and negative discriminant. Full certificates
are in the JSON. This parameter is outside (-b,0), so it does not refute L
as stated. It also does not refute the observed larger strip for the actual
power family, since p is a different polynomial.

The one next test is to prove or exactly refute L on its stated strip. A
counterexample must satisfy the coefficient inequality and have simple input
roots in (-1,0); the unrestricted obstructions do not suffice. If L fails,
record which additional power-family property is absent, without treating the
failure as a disproof of O. No infinite real-rootedness or nesting result is
claimed in this pass.
