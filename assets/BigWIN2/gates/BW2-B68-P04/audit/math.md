# Fresh mathematical referee report

**Verdict: accept.** The frozen `resolution-paper` claim is correct at its
stated scope and resolves the full literal problem in `source.md`. This report
is bound to snapshot
`45ea55287a8aa3de8430189c951f93920f92dcb941e5ff56ce1735d2cf0d6588`
and referee job `win-00068-p04-referee-99e13bd8a59f`.

## Scope reconstructed

I treated the denominator in the frozen curvature definition literally as the
edge length, not silently as the induced endpoint distance. Thus an edge that
is longer than its alternate two-edge path is a genuine non-finiteness case.
The candidate covers every positive normalized triangle, including all
shortest-path ties, all transport/order walls, and all initial data on which
the three curvatures are finite. It also distinguishes a zero-edge limit from
a point at which the inverse-weight measures are defined.

## Transport calculation

For `e_12`, put `epsilon=1-alpha` and write the lengths as `(a,b,c)`.
Directly from the inverse-weight measures, the signed imbalance
`Delta=m_1^(1-epsilon)-m_2^(1-epsilon)` is

\[
\Delta_1=1-\epsilon-\frac{\epsilon b}{a+b},\quad
\Delta_2=-1+\epsilon+\frac{\epsilon c}{a+c},\quad
\Delta_3=\frac{\epsilon a(b-c)}{(a+b)(a+c)}.
\]

For sufficiently small positive `epsilon`, the first coordinate is a source,
the second a sink, and the sign of the third is the sign of `b-c`. When
`a<=1/2`, the endpoint distance is `a`. If `b>=c`, diagonal cancellation and
the shipments `1->2` and `3->2` give cost

\[
a\Delta_1+B\Delta_3,\qquad B=d(v_2,v_3).
\]

The potential `(a,0,B)` has the same value and is 1-Lipschitz because its only
non-immediate constraint is `|a-B|<=C`, the metric triangle inequality. This
is an exact primal/dual certificate. If `c>=b`, the analogous shipments
`1->2` and `1->3` have cost `a(-Delta_2)+C(-Delta_3)` and the potential
`(a,0,a-C)` is dual feasible, with the remaining constraints again supplied
by metric triangle inequalities. Hence all possible optimal-basis changes,
including `b=c`, are covered.

On the simultaneous geodesic region, cycling the resulting formula gives, for
an edge of length `x` and other lengths `y,z`,

\[
\kappa_x=1+\frac{M(x+2m-M)}{(x+y)(x+z)},\qquad
M=\max(y,z),\quad m=\min(y,z).
\]

At `x=1/2` the two routes tie and the formula remains finite; for example
`kappa_x=1+3yz/((x+y)(x+z))`. If `x>1/2`, continuity of finite-space
Wasserstein distance gives `W_1 -> 1-x`, so the curvature quotient has the
positive constant numerator `(2x-1)/x` divided by `epsilon` and tends to
`+infinity`. Therefore all three curvatures are finite exactly when every
coordinate is at most `1/2`, as claimed.

## ODE and boundary audit

With `K=sum_x x kappa_x`, direct summation gives `sum_x F_x=0` on the
normalized simplex. The min/max curvature formula is Lipschitz on the compact
closed geodesic triangle: all pair-sum denominators are at least `1/2` there.
It therefore has a Lipschitz neighborhood extension suitable for the ODE
uniqueness argument.

Permutation equivariance makes each equality wall invariant. On a geodesic
wall, say `a=1/2` and `b+c=1/2`, the exact identity

\[
b(\kappa_b-\kappa_a)+c(\kappa_c-\kappa_a)=0
\]

gives `K=kappa_a` and hence `F_a=0`. Uniqueness prevents a trajectory starting
off an invariant ordering or geodesic wall from first hitting it in finite
time. Each coordinate satisfies `dot x=x(K-kappa_x)` with a bounded
multiplier on the compact extension, so a positive coordinate cannot vanish
in finite time. These facts establish forward invariance, uniqueness, and
global existence for every datum in the claimed region, and rule out
finite-time arrival at a new nondifferentiability or non-finiteness locus.

## Exhaustive dynamics

After a label permutation, assume `a>=b>=c`. Independent algebra recovers

\[
\frac{d}{dt}\log\frac ab=
\frac{(a-b)(2ab+3c-1)}{(a+b)(a+c)(b+c)},\qquad
\frac{d}{dt}\log\frac bc=
\frac{2a(b-c)}{(a+b)(a+c)}.
\]

At equilibrium the second identity forces `b=c=s`; equality of the remaining
curvatures then has factor `(1-3s)(4s-1)`, giving only the equal point and
`(1/2,1/4,1/4)` up to labels.

The trajectory trichotomy is exhaustive. If all coordinates are equal, the
solution is constant. If `a>b=c=s`, the scalar equation has negative sign for
`1/4<s<1/3` and its only possible lower limiting zero is `s=1/4`, yielding
`(1/2,1/4,1/4)`. If `b>c`, then `R=log(b/c)` is strictly increasing. Were it
bounded, its initial ratio above one, `b+c>=1/2`, `a>=1/3`, and
`(a+b)(a+c)<=1` would give a fixed positive lower bound for `dot R`, a
contradiction. Thus `b/c -> infinity`, so `c -> 0`; since `a+b -> 1` and both
are at most `1/2`, `(a,b,c) -> (1/2,1/2,0)`. This proves the stated singleton
omega-limit sets and exhausts all boundary-degeneration regimes without
asserting curvature at a zero edge.

## Reproducibility and source comparison

All seven snapshot hashes were independently checked and matched. Running
both frozen SymPy scripts produced their stated PASS results. The scripts
confirm the rational identities; the optimality, quantifier, and limiting
arguments above were checked separately rather than inferred from script
success.

The cited Bai--Hua arXiv v1 paper is explicitly restricted to finite trees and
states that the behavior of this inverse-weight flow on graphs with cycles
remains open. The cited Bai--Lin--Lu--Wang--Yau general-graph definition
normalizes by the induced distance `d(x,y)`, and its flow procedure deletes an
edge when the edge length ceases to realize that distance. It therefore does
not contain the frozen literal non-geodesic extension or this exact triangle
classification. A targeted current search found no primary source stating
the same `C3` classification; this is bounded negative search evidence, not a
claim of priority.

I found no circular use of tree formulas, no missing equality case, no division
by a vanishing quantity on the asserted positive domain, and no material gap
requiring revision. The exact frozen candidate scope is accepted.
