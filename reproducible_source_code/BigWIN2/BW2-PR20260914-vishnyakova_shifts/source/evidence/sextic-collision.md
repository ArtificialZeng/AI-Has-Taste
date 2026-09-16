# Exact degree-six collision and cell certificate

Job: primary-20260914-vishnyakova-shifts-research-77f35a690f9a.
Reproduce with `python3 evidence/sextic-collision.py`. All decisions in that
script use exact integers/rationals, polynomial remainders, Sturm isolation,
and rational interval arithmetic. The decimal descriptions below are only
readable approximations. This is a finite-degree result without a novelty
claim or independent mathematical review.

## Result of the assigned test

There is exactly one parameter alpha in (-b,0), b=1-1/sqrt(2), for which
Q_(6,alpha) has a multiple root. Its six roots all belong to (-1,0).
There is exactly one repeated root r, its multiplicity is two, and

    -0.255 < alpha < -0.254,
    -0.00325753388855 < r < -0.00325753388854,
    -0.009966252267 <= partial_t Q_(6,alpha)(r) <= -0.009966252266,
    49.277174437920 <= partial_z^2 Q_(6,alpha)(r) <= 49.277174437970,
    0.000202248858 <= sigma <= 0.000202248859,

where sigma=-(partial_t Q)/(partial_z^2 Q). In particular sigma>0. All
displayed decimal bounds are finite decimals, interpreted as exact rationals.
No higher multiplicity or second repeated root occurs in this parameter range.

## Algebraic representation and completeness

The polynomial Q_6 is assembled independently from the degree recurrence and
the original finite-difference definition. The full coefficient list and the
primitive polynomial F are serialized in `sextic-collision.json`, with

    discriminant_z Q_(6,t) = -71663616000 F(t).

The degree-30 polynomial F has positive leading coefficient, is squarefree,
and has exactly six real roots. Exact disjoint isolating rational intervals
for all six are in the JSON; their approximate locations are -0.9704,
-0.6539, alpha=-0.2546881563814337, 1-alpha, 1.6539, and 1.9704.
The recorded Sturm sequence sign variations certify that precisely two are
in [-1/2,3/2], namely alpha and 1-alpha. In particular there is precisely one
in (-b,0). The bound alpha>-b is checked by (1+alpha)^2>1/2 and alpha>-1.

The penultimate subresultant of Q_6 and partial_z Q_6 is, up to a positive
constant, A(t)z+B(t), where A and B are written in the JSON. Its last
subresultant is -720 times the discriminant. Interval arithmetic proves
A(alpha)>0. Thus the specialized greatest common divisor has degree one.
In addition, substitution of r=-B/A into Q_6 and partial_z Q_6, clearing
denominators and reducing modulo F, gives two exact zero remainders.
The certified interval for r follows by interval evaluation of -B/A on the
isolating interval for alpha. Evaluating both partial derivatives on the
resulting rational rectangle proves the displayed sign bounds. The positive
second derivative separately rules out multiplicity greater than two.

## Consequence for M_6

The elementary coefficient restriction and reflection give
M_6 subset [-1/2,3/2], as explained in `triage-exact.md`. The discriminant is
nonzero throughout (alpha,1-alpha). At t=1/2, exact Sturm counting gives six
simple roots in (-1,0), so all roots remain real throughout this connected
open parameter interval: a real pair could cease to be real only at a
multiple root, and the fixed leading coefficient 720 prevents escape to
infinity. A root can meet z=0 only at t=0, since Q_(6,t)(0)=t^6, and can meet
z=-1 only at t=1, since Q_(6,t)(-1)=(t-1)^6. To avoid assuming that roots do
not cross at these two parameters, the script counts six roots in [-1,0]
separately at t=-1/4, 1/2 and 5/4, one in each of the three open cells split
by t=0,1. The exact counts at t=0,1 are also six. Consequently all six roots
are in [-1,0] on the entire central open interval. Continuity includes its
two endpoints; the endpoint evaluations show their roots are strictly inside
(-1,0).

On the left remaining cell [-1/2,alpha), the discriminant never vanishes and
no root crosses either z endpoint. A sample at t=-13/50 has exactly four
roots in [-1,0], so this entire cell is excluded. Reflection excludes
(1-alpha,3/2]. Hence

    M_6 = [alpha, 1-alpha].

Combined with the earlier exact brackets for M_2 and M_4, this verifies
c_2<c_4<c_6 in these three degrees. It is not an all-degree result.

## Interpretation and remaining gap

Near the collision the two roots have squared displacement
2 sigma (t-alpha) to first order. Thus they become real as t increases
through alpha. This verifies the proposed direction for n=6 and excludes
all degeneracies in that degree. It supplies no uniform sign argument for
n>=8, no all-degree connectedness proof, and no successive-degree nesting
proof. The finite classification by itself has no established publication
value. No claim.json or research manuscript is asserted on this basis.
