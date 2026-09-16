# Exact solution and verification

Fix \(n\geq 1\) and \(0\leq\alpha<1\), and write \(c=1-\alpha>0\).
For a feasible ladder put \(R_{n+1}=1\) and
\[
\Delta_i=R_{i+1}-R_i\quad(0\leq i<n),\qquad
\Delta_n=1-R_n.
\]
The ladder conditions are equivalent to
\(\Delta_0,\ldots,\Delta_{n-1}>0\), \(\Delta_n\geq0\), and
\(\sum_{i=0}^n\Delta_i=1\). In particular, \(\Delta_n=0\) is allowed
and means \(R_n=1\); a zero among the first \(n\) gaps is not allowed.

For the continuous part, the client uses \(R_i\) on
\([R_i,R_{i+1})\), so
\[
\int_{R_i}^{R_{i+1}}(B-R_i)\,dB=\frac{\Delta_i^2}{2}.
\]
At the atom, the client uses \(R_n\), including when \(R_n=1\), and
the loss is \(1-R_n=\Delta_n\). Hence the expected loss is exactly
\[
F(\Delta)=\frac c2\sum_{i=0}^n\Delta_i^2+\alpha\Delta_n. \tag{1}
\]

Set \(t=\Delta_n\). The feasible range is \(0\leq t<1\). At fixed
\(t\), Cauchy--Schwarz gives
\[
\sum_{i=0}^{n-1}\Delta_i^2\geq \frac{(1-t)^2}{n},
\]
with equality if and only if all first \(n\) gaps equal
\((1-t)/n>0\). It remains to minimize the strictly convex quadratic
\[
g(t)=\frac c2\left(\frac{(1-t)^2}{n}+t^2\right)+\alpha t,
\qquad 0\leq t<1. \tag{2}
\]
Its derivative is
\[
g'(t)=\frac c n((n+1)t-1)+\alpha.
\]
The unconstrained critical point is
\[
t_0=\frac{1-(n+1)\alpha}{(n+1)(1-\alpha)}. \tag{3}
\]
If \(0\leq\alpha<1/(n+1)\), then \(0<t_0<1\) and it is the unique
minimum. The other gaps then equal
\[
s=\frac{1-t_0}{n}=\frac1{(n+1)(1-\alpha)}. \tag{4}
\]
If \(\alpha\geq1/(n+1)\), then \(g'(0)\geq0\), so strict convexity
makes \(t=0\) the unique constrained minimum, and the other gaps all
equal \(1/n\). Every listed first gap is positive, so the minimizers
are feasible in the original strict ladder set; the infimum is always
attained.

Substitution in (2) gives
\[
L^*_{n,\alpha}=
\begin{cases}
\displaystyle\frac{1-(n+1)\alpha^2}
 {2(n+1)(1-\alpha)},&0\leq\alpha\leq\dfrac1{n+1},\\[6pt]
\displaystyle\frac{1-\alpha}{2n},&\dfrac1{n+1}\leq\alpha<1.
\end{cases} \tag{5}
\]
The two expressions agree at the transition. Strict convexity and the
equality condition above show that the only attaining ladder is
\[
(R_1,\ldots,R_n)=
\begin{cases}
\displaystyle\left(\frac1{(n+1)(1-\alpha)},\ldots,
\frac n{(n+1)(1-\alpha)}\right),
 &0\leq\alpha\leq\dfrac1{n+1},\\[8pt]
\displaystyle\left(\frac1n,\ldots,\frac nn\right),
 &\dfrac1{n+1}\leq\alpha<1.
\end{cases} \tag{6}
\]
At equality in the transition the two descriptions coincide.

## Direct low-dimensional checks

For \(n=1\), with \(R_1=r\), direct integration gives
\[
F_1(r)=\frac c2\{r^2+(1-r)^2\}+\alpha(1-r),\qquad0<r\leq1.
\]
Its derivative is \(c(2r-1)-\alpha\). Thus the unique minimizer is
\(r=1/(2c)\) for \(0\leq\alpha\leq1/2\), and \(r=1\) for
\(1/2\leq\alpha<1\). The values are respectively
\((1-2\alpha^2)/(4c)\) and \(c/2\), agreeing with (5), including at
\(\alpha=1/2\).

For \(n=2\), put \(R_1=x,R_2=y\). Directly,
\[
F_2(x,y)=\frac c2\{x^2+(y-x)^2+(1-y)^2\}+\alpha(1-y).
\]
The interior stationarity equations are \(2x-y=0\) and
\(c(2y-x-1)-\alpha=0\), yielding
\((x,y)=(1/(3c),2/(3c))\). This is feasible with \(y\leq1\) exactly
when \(\alpha\leq1/3\). For \(\alpha\geq1/3\), strict convexity and
the active boundary \(y=1\) give the unique solution \(x=1/2\).
The respective values \((1-3\alpha^2)/(6c)\) and \(c/4\) agree with
(5), including at \(\alpha=1/3\).

## Endpoint checks

At \(\alpha=0\), (3)--(6) give all \(n+1\) gaps equal to
\(1/(n+1)\), the unique ladder \(R_i=i/(n+1)\), and value
\(1/(2(n+1))\). At every active-set transition the last gap reaches
zero continuously, the two ladder formulas coincide at \(R_i=i/n\),
and the two value formulas both give \(1/(2(n+1))\). As
\(\alpha\uparrow1\), the unique optimizer remains \(R_i=i/n\) and
the value \((1-\alpha)/(2n)\) tends to zero. The excluded case
\(\alpha=1\) is not part of the theorem; separately, its loss would be
\(1-R_n\), so it would have many minimizers with \(R_n=1\), unlike
the unique minimizer for every \(\alpha<1\).

## Scope and gap list

This proves only the frozen uniform-plus-endpoint-atom problem, not the
general problem for atomic bandwidth distributions. Mathematical gap list for
the frozen claim: empty. Novelty and priority are not claimed; the existing
literature screen is limited as recorded in `problem.md`.
