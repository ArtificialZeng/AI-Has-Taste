# Exact parametric transport certificate for `e_12`

Write `a=w_12`, `b=w_23`, `c=w_31`, with `a+b+c=1`, and put
`epsilon=1-alpha`.  This note solves the limiting transport problem for
`e_12` on its entire geodesic domain `a<=1/2`, including all shortest-path
and transport equality walls.  All displayed identities are exact.

## Measures and signed imbalance

Let `mu=m_1^(1-epsilon)` and `nu=m_2^(1-epsilon)`.  In vertex order
`(v_1,v_2,v_3)`,

\[
 \mu=\left(1-\epsilon,{\epsilon c\over a+c},
                    {\epsilon a\over a+c}\right),\qquad
 \nu=\left({\epsilon b\over a+b},1-\epsilon,
                    {\epsilon a\over a+b}\right).
\]
Thus, for `Delta=mu-nu`,

\[
\begin{aligned}
 \Delta _1&=1-\epsilon-\frac{\epsilon b}{a+b},\\
 \Delta _2&=-1+\epsilon+\frac{\epsilon c}{a+c},\\
 \Delta _3&=\frac{\epsilon a(b-c)}{(a+b)(a+c)},
 \qquad \Delta _1+\Delta _2+\Delta _3=0.
\end{aligned}
\]

For

\[
0<\epsilon<\epsilon_0:=
\min\left\{{a+b\over a+2b},{a+c\over a+2c}\right\},
\]

one has `Delta_1>0` and `Delta_2<0`; the sign of `Delta_3` is exactly the
sign of `b-c`.  This neighborhood is enough for the LLY limit.

Let

\[
A=d(v_1,v_2)=a,\quad
B=d(v_2,v_3)=\min\{b,a+c\},\quad
C=d(v_3,v_1)=\min\{c,a+b\}.
\]

The equality `A=a` uses precisely `a<=1/2`.

## Cell `b>=c`

Cancel common mass on the diagonal and use the only residual shipments
`v_1 -> v_2` of mass `Delta_1` and `v_3 -> v_2` of mass `Delta_3`.
Equivalently, an explicit primal coupling is

\[
 \pi_{11}=\nu_1,\quad \pi_{22}=\mu_2,\quad \pi_{33}=\nu_3,
 \quad \pi_{12}=\Delta_1,\quad \pi_{32}=\Delta_3,
\]

with all other entries zero.  Its cost is `a Delta_1+B Delta_3`.
The Kantorovich potential

\[
(\phi_1,\phi_2,\phi_3)=(a,0,B)
\]

is dual feasible: the two used arcs are tight, and the remaining constraint
`|a-B|<=C` is a triangle inequality for the shortest-path metric.  Its dual
value is the same primal cost.  Hence

\[
 W_1=a\Delta_1+B\Delta_3,
 \qquad
 \kappa_{12}=1+{b\over a+b}
 -{B(b-c)\over(a+b)(a+c)}.                 \tag{1}
\]

This includes `b=c`, where the second residual shipment has zero mass.

## Cell `c>=b`

After diagonal cancellation, ship `-Delta_2` from `v_1` to `v_2` and
`-Delta_3` from `v_1` to `v_3`.  An explicit primal coupling is

\[
 \pi_{11}=\nu_1,\quad \pi_{22}=\mu_2,\quad \pi_{33}=\mu_3,
 \quad \pi_{12}=-\Delta_2,\quad \pi_{13}=-\Delta_3.
\]

The potential `(a,0,a-C)` is dual feasible and tight on both used arcs;
its only remaining constraint is `|a-C|<=B`, again a metric triangle
inequality.  Primal and dual values coincide, giving

\[
 W_1=a(-\Delta_2)+C(-\Delta_3),
 \qquad
 \kappa_{12}=1+{c\over a+c}
 -{C(c-b)\over(a+b)(a+c)}.                 \tag{2}
\]

At `b=c`, (1) and (2) both equal `1+b/(a+b)`.

## Complete shortest-path subdivision

For `a<1/2`, equations (1)--(2) specialize as follows.

* If `b,c<=1/2` and `b>=c`, then

  \[
  \kappa_{12}=1+{b(a+2c-b)\over(a+b)(a+c)}.       \tag{3}
  \]

* If `b,c<=1/2` and `c>=b`, then

  \[
  \kappa_{12}=1+{c(a+2b-c)\over(a+b)(a+c)}.       \tag{4}
  \]

* If `b>=1/2` (which forces `b>c`), then `B=a+c` and

  \[
  \kappa_{12}=1+{c\over a+b}.                     \tag{5}
  \]

* If `c>=1/2` (which forces `c>b`), then `C=a+b` and

  \[
  \kappa_{12}=1+{b\over a+c}.                     \tag{6}
  \]

The formulas agree at `b=1/2`, `c=1/2`, and `b=c`, so the equality walls
are certified rather than discarded.

If `a=1/2`, then `b+c=1/2`, hence `B=b`, `C=c`.  Substitution into either
ordering branch gives the single formula

\[
 \boxed{\ \kappa_{12}=1+{3bc\over(a+b)(a+c)}\ },\qquad a=\tfrac12. \tag{7}
\]

Although the optimal residual coupling changes at `b=c`, the curvature in
(7) does not: the difference of the algebraic expressions (3) and (4) is

\[
{(b-c)(a-b-c)\over(a+b)(a+c)},
\]

which vanishes identically on `a=b+c=1/2`.

## Consequences for the three-edge problem

For an edge of length `x<=1/2`, the same argument (cyclically relabelled)
proves finiteness of its literal curvature, even if another edge is longer
than `1/2`.  If `x>1/2`, its quotient instead has positive constant term
`(2x-1)/x` and tends to `+infinity`.  Therefore

\[
\boxed{\text{all three literal curvatures are finite exactly when }
       \max\{a,b,c\}\leq\tfrac12.}
\]

On this closed geodesic region, if `y,z` are the other two edge lengths,
`M=max(y,z)`, and `m=min(y,z)`, the cyclic curvature formula is

\[
\boxed{
 \kappa_x=1+{M(x+2m-M)\over(x+y)(x+z)}.           \tag{8}
}
\]

Thus the simultaneous transport partition consists of the six weak ordering
chambers of `(a,b,c)` and their equality strata, together with the three
geodesic boundary walls `x=1/2`.  Finally, wherever these formulas define the
flow, `K=sum_x x kappa_x` gives
`sum_x dot x=-K+K sum_x x=0`, so the simplex sum is preserved.

The companion script `verify_edge12_lp.py` checks every algebraic identity in
this certificate over the exact rational-function field.
