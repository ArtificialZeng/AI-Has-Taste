# Exact chamber dynamics and complete qualitative classification

This note continues the exact transport calculation in `edge12_lp.md`.  Write

\[
 a=w_{12},\qquad b=w_{23},\qquad c=w_{31},\qquad a+b+c=1,
\]

and let

\[
 \mathcal G=\{(a,b,c)>0:a+b+c=1,\ \max(a,b,c)\leq\tfrac12\}.
\]

The earlier primal/dual certificates prove that this is exactly the set on
which all three literal curvatures are finite.  The purpose here is to analyze
the normalized vector field on all of `G`, including its ordering and
geodesic walls.

## Exact vector field on the chambers

For an edge of length `x` whose other two lengths are `y,z`, put
`M=max(y,z)` and `m=min(y,z)`.  On `G`, the certified cyclic formula is

\[
 k_x=1+\frac{M(x+2m-M)}{(x+y)(x+z)},\qquad
 K=xk_x+yk_y+zk_z,\qquad F_x=-x(k_x-K).       \tag{1}
\]

Equation (1), with the choices of `M,m`, is an exact piecewise-rational
formula for the normalized vector field.  It covers all six weak ordering
chambers and their walls.  In particular, in the representative chamber
`a>=b>=c`,

\[
\begin{aligned}
k_a&=1+\frac{b(a+2c-b)}{(a+b)(a+c)},\\
k_b&=1+\frac{a(b+2c-a)}{(a+b)(b+c)},\\
k_c&=1+\frac{a(c+2b-a)}{(a+c)(b+c)}.          \tag{2}
\end{aligned}
\]

The vector field is equivalently determined by `F_a+F_b+F_c=0` and

\[
\begin{aligned}
\frac{d}{dt}\log\frac ab
 &=k_b-k_a
 =\frac{(a-b)(2ab+3c-1)}{(a+b)(a+c)(b+c)},\\
\frac{d}{dt}\log\frac bc
 &=k_c-k_b
 =\frac{2a(b-c)}{(a+b)(a+c)}.                 \tag{3}
\end{aligned}
\]

For later use, the maximum coordinate has the factorization

\[
 F_a=\frac{a(1-2a)(a^2+2ab+3b^2-2b)}{(a+b)(a+c)}. \tag{4}
\]

All formulas for the other chambers follow by permuting the labels.  The
companion SymPy replay checks (2)--(4) over the exact rational-function field.

## Well-posedness and invariant walls

Let

\[
 \overline{\mathcal G}=\{(a,b,c)\geq0:a+b+c=1,\ \max(a,b,c)\leq\tfrac12\}.
\]

Formula (1) has a Lipschitz extension to a neighborhood of this compact
triangle.  Indeed,
`min` and `max` are Lipschitz, while each pair sum is at least `1/2` on
`bar(G)`, so none of the denominators can vanish there or in a sufficiently
small neighborhood.  Therefore (1) is Lipschitz on `bar(G)` and the standard
local existence and uniqueness theorem applies through a neighborhood
extension.  This extension is used only for the ODE argument; curvature at a
zero edge is not asserted to be defined by the original inverse-weight
measure.

If two coordinates are equal, permutation equivariance gives equal curvature
and equal vector-field coordinates.  Thus every ordering wall is invariant.
Lipschitz uniqueness then implies that a trajectory starting in a strict
ordering chamber cannot meet an ordering wall at finite time.

If `a=1/2`, write `b+c=1/2` and, without loss, `b>=c`.  Directly from (1),

\[
 k_a=1+\frac{3bc}{(a+b)(a+c)},\qquad
 k_b=1+\frac{c}{a+b},\qquad
 k_c=1+\frac{b}{a+c}.                         \tag{5}
\]

The exact identity

\[
 b(k_b-k_a)+c(k_c-k_a)=0
\]

shows that `K=k_a`, and hence `F_a=0`.  Every geodesic wall is consequently
invariant.  Formula (4) also displays the factor `1-2a` on its interior side.
Lipschitz uniqueness (or the bounded logarithmic equation for
`1/2-a`) shows that an interior trajectory cannot reach such a wall in finite
time.

Finally, every coordinate obeys `dot x=x(K-k_x)`.  The multiplier is bounded
on `bar(G)`, so a positive coordinate cannot become zero in finite time.
Thus every initial point of `G` has one unique classical solution on
`[0,infinity)`, it stays in `G`, and no trajectory reaches either a new
transport nondifferentiability wall or the non-finiteness locus in finite
positive time.  Initial data already on an ordering or geodesic wall have a
unique tangent solution there.  Hence `G` is the full well-posed initial set
and is forward invariant.

## Equilibria

It suffices to work in `a>=b>=c`.  At an equilibrium all positive-coordinate
curvatures are equal.  The second equation of (3) first forces `b=c=s`.
Putting `a=1-2s`, the first equation becomes

\[
 k_b-k_a=\frac{(1-3s)(4s-1)}{2s(1-s)}.        \tag{6}
\]

On `1/4<=s<=1/3`, its only zeros are `s=1/4` and `s=1/3`.
Consequently the complete equilibrium list in `G` is

\[
 (\tfrac13,\tfrac13,\tfrac13),\qquad
 (\tfrac12,\tfrac14,\tfrac14)
\]

and the three labelled permutations of the second point.

## Every maximal trajectory and every omega-limit

Permute the labels of an arbitrary initial point so that `a>=b>=c`.  The
ordering remains fixed for all finite time.  There are three exhaustive
cases.

1. **All weights equal.**  The trajectory is the constant equilibrium
   `(1/3,1/3,1/3)`.

2. **The two smaller weights are equal:** `a>b=c=s`.  This equality wall is
   invariant.  For `1/4<s<1/3`, equation (6) is strictly positive, and

   \[
   \dot s=-\frac{(1-2s)(1-3s)(4s-1)}{2(1-s)}<0. \tag{7}
   \]

   Hence `s` decreases.  Its only possible limiting zero of the right-hand
   side below its initial value is `1/4`; if its limit were larger, the
   right-hand side would stay bounded away from zero, a contradiction.
   Thus

   \[
   (a,b,c)\longrightarrow(\tfrac12,\tfrac14,\tfrac14).
   \]

   At the endpoint `s=1/4` the trajectory is already this equilibrium.

3. **The middle weight is strictly larger than the smallest:** `b>c`
   (allowing either `a>b` or `a=b`).  Set `R=log(b/c)`.  The second equation
   of (3) gives

   \[
   \dot R=\frac{2a(b-c)}{(a+b)(a+c)}>0.        \tag{8}
   \]

   In fact `R` tends to infinity.  Otherwise `b/c` would remain bounded;
   because it is at least its initial value `r_0>1` and `b+c>=1/2`,

   \[
   b-c=\frac{b/c-1}{b/c+1}(b+c)
       \geq\frac{r_0-1}{2(r_0+1)}>0.
   \]

   Also `a>=1/3`, and the denominator in (8) is at most one, so (8) would
   be bounded below by a positive constant, contradicting boundedness of
   `R`.  Therefore `b/c` tends to infinity, whence `c` tends to zero.
   Since `a+b` tends to one and both are at most `1/2`,

   \[
   (a,b,c)\longrightarrow(\tfrac12,\tfrac12,0). \tag{9}
   \]

These cases also include all geodesic-wall data.  For example, on
`a=1/2`, `b+c=1/2`, the larger of `b,c` moves toward `1/2` and the smaller
toward zero; with `b` as the variable,

\[
 \dot b=\frac{b(2b-1)(4b-1)}{(b-1)(2b+1)}.    \tag{10}
\]

At `b=c=1/4` the wall point is the equilibrium already listed.  Equations
(7), (8), and (10) show that all degeneration occurs only as `t` tends to
infinity, consistently with the finite-time argument above.

Thus every maximal trajectory is global.  Every omega-limit set is a
singleton: it is the equal point in case 1, the appropriate permutation of
`(1/2,1/4,1/4)` in case 2, and the appropriate permutation of
`(1/2,1/2,0)` in case 3.  The last point lies on the closed-simplex boundary
and is a limit only; no curvature at its zero edge is invoked.

All strata of the required transport/order partition are invariant: these
are the six weak ordering chambers and their equality intersections, refined
by the three geodesic walls; the strict pieces never cross their incident
walls.  Within these strata the three cases above exhaust all positive
initial data.
