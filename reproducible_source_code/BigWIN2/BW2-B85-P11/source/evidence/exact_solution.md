# Exact primal--dual certificate for the finite problem

All algebra in this file is independently executable in
`evidence/verify_exact_solution.py`.  The decimals below only identify the
algebraic branch; none is used as a certificate.

## Algebraic parameter and claimed value

Let
\[
 P(U)=256U^7+256U^6-96U^5-80U^4+40U^3+30U^2-15U-5.
\]
There is a unique root (u) of (P) in
\[
 I=[533/1000,267/500].
\]
Indeed, exact evaluation gives
\[
 P(533/1000)=-\frac{14387903930821523}{3906250000000000000}<0,
 \qquad
 P(267/500)=\frac{2066305610212673}{30517578125000000}>0,
\]
and termwise rational interval arithmetic gives, throughout (I),
\[
 P'(U)\geq
 \frac{275284068057136783}{3906250000000000}>0.
\]
Numerically, only for orientation,
\[
 u=0.533051836754696420611138454885\ldots.
\]

The exact proposed value is
\[
 \boxed{
 T_{\mathbb R}(\Omega_{5/2})=
 \frac{(2u+1)^2(4u^2-6u+1)^2}{128u^6-20u^2+5}}
 =2.135307178876397432237676\ldots .
\]
It is also the branch specified above of the algebraic equation
\[
 28900000Y^7-131750000Y^6+120730000Y^5+214615000Y^4
 -355902050Y^3-31494803Y^2+238257375Y-82156250=0.
\]

## Exact primal certificate

Put
\[
 q(X)=X^3+uX^2+(2u^2-5/4)X-2u^3.
\]
Writing (q(X)^2=\sum_{k=0}^6 A_kT_k(X)), direct exact expansion gives
\[
 A_2=A_3=0,
 \qquad
 A_0=\frac{128u^6-20u^2+5}{32}>0.
\]
(The last inequality also follows because (A_0) is the arcsine mean of the
nonzero square (q^2).)  Consequently (p=q^2/A_0) is a nonnegative
polynomial on ([-1,1]), has constant Chebyshev coefficient (1), and has
only the permitted nonconstant frequencies (1,4,5,6).  Its finite objective
is
\[
 p(1)=\frac{2(2u+1)^2(4u^2-6u+1)^2}{128u^6-20u^2+5}.
\]

## Exact positive atomic dual certificate

Set
\[
 D=5(2u-1)(32u^4+8u^2+1)
\]
and define
\[
\begin{aligned}
 m_0&=-\frac{512u^4-256u^3-32u^2+6u-3}{D},\\
 m_1&=-1,\\
 m_2&=-\frac{256u^6-128u^5+48u^4-44u^3+42u^2-23u-1}{D}.
\end{aligned}
\]
For (n=0,1,2,3), define the remaining moments by reduction modulo (q):
\[
 m_{n+3}=-u m_{n+2}-(2u^2-5/4)m_{n+1}+2u^3m_n.
\]
Let (L(X^j)=m_j) for (0\leq j\leq6).  Exact substitution gives
\[
 L(T_1)=L(T_4)=L(T_5)=L(T_6)=-1.
\]
The (T_1,T_4,T_6) identities hold directly; the residual in the (T_5)
identity is
\[
 -\frac{4(4u^2-6u+1)P(u)}{5(2u-1)(32u^4+8u^2+1)}=0.
\]

It remains to certify that (L) is a positive atomic functional supported in
the feasible interval.  Uniform exact interval evaluation for every (U\in I)
gives the following signs:
\[
\begin{array}{c|rrrrrr}
 x&-23/25&-91/100&-21/50&-41/100&79/100&4/5\\ \hline
 q_U(x)&-&+&+&-&-&+
\end{array}
\]
For example, the six enclosing rational intervals are printed by the verifier.
Thus the cubic (q) has one root in each of
\[
 (-23/25,-91/100),\quad(-21/50,-41/100),\quad(79/100,4/5),
\]
so all three roots are real, distinct, and lie in ((-1,1)).

The leading principal minors of the moment matrix
\[
 H=(m_{i+j})_{0\leq i,j\leq2}
\]
are
\[
\begin{aligned}
 \Delta_1={}&\frac{-512u^4+256u^3+32u^2-6u+3}
 {5(2u-1)(32u^4+8u^2+1)},\\
 \Delta_2={}&\frac{(4u^2-6u+1)(64u^4-32u^3-24u^2+32u-11)
 (112u^4+112u^3+46u^2+3u+2)}
 {25(2u-1)^2(32u^4+8u^2+1)^2},\\
 \Delta_3={}&\frac{(2u+1)(4u^2-6u+1)^2
 (64u^4-32u^3-24u^2+32u-11)^2}
 {2000(2u-1)^3(32u^4+8u^2+1)^3}\\
 &\qquad\times(512u^5+1024u^4+864u^3+328u^2+32u-11).
\end{aligned}
\]
Exact rational Horner enclosures on (I) show respectively that the unfixed
sign factors in these formulas have signs
\[
 (+);\qquad(-)(-)(+);\qquad(+),
\]
and all denominator factors are positive.  Hence all three minors are positive
and (H\) is positive definite.

For completeness, divide any polynomial of degree at most six by (q).  The
moment recurrence makes (L(qs)=0) for every (s) of degree at most three.
Since (q) has three distinct real roots (r_i), interpolation in
\(\mathbb R[X]/(q)\) therefore writes
\[
 L(f)=\sum_{i=1}^3 w_i f(r_i).
\]
Positive definiteness of (H) forces every (w_i>0): apply
\(L(h^2)>0\) to the degree-two Lagrange polynomial that is (1) at (r_i)
and (0) at the other two roots.  This proves that (L) is the required
positive atomic dual measure, not merely a formal moment vector.

## Equality and conclusion

For every feasible
\(f=1+2\sum_{k\in\{1,4,5,6\}}c_kT_k\), positivity of the atomic measure gives
\[
 0\leq L(f)=m_0-2\sum_kc_k,
 \qquad f(1)\leq1+m_0.
\]
For the primal square (p=q^2/A_0), all three dual atoms are zeros, so
\(L(p)=0\) and equality holds.  Algebraically,
\[
 p(1)-(1+m_0)=
 -\frac{16u(4u^2-6u+1)P(u)}
 {5(2u-1)(32u^4+8u^2+1)(128u^6-20u^2+5)}=0.
\]
Thus the finite optimum is (M=p(1)=1+m_0).  Using the frozen reduction
\(T_{\mathbb R}(\Omega_{5/2})=M/2\) proves the boxed value.

## Scope and literature caution

This resolves the frozen exact finite optimization and hence the frozen Turán
value, conditional only on the source reduction already recorded in
`problem.md`.  It does not classify all extremizers.  The targeted literature
screen in `evidence/triage.md` found no later primary treatment, but that search
does not establish priority or a formal open-problem status.
