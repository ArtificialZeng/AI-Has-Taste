# Exact diagonal counterexample and its Q-order

All statements below use the residual convention and update in `problem.md`:

\[
 R^+=-\nu R^2+(1+\nu)R^4,
 \qquad \nu={\|R^2\|_F^2\over\|R\|_F^2}.
\]

## 1. Exact one-step counterexample

For \(R=t\operatorname{diag}(1,2,3)\),
\(\nu=7t^2\), and coordinatewise substitution gives

\[
 R^+=t^4\operatorname{diag}(-6,-12,18)
      +7t^6\operatorname{diag}(1,16,81).                 \tag{1}
\]

Consequently

\[
 {\|R^+\|_F\over \|R\|_F^6}
 ={t^4\|(-6+7t^2,-12+112t^2,18+567t^2)\|_2
    \over 14^3t^6}\longrightarrow\infty
\]

as \(t\downarrow0\). Thus no uniform sixth-order local residual estimate
holds for general matrices under the stated update. With \(A=I_3\), residual
and inverse error have the same Frobenius norm, so this also refutes the
corresponding uniform local error estimate. Moreover, for
\(0<t\le10^{-2}\), \(\|R_0\|_F=\sqrt{14}t<1\), so every member of the family
satisfies the source theorem's initial-residual hypothesis (and also its
proof's stronger, unstated bound \(\|R_0\|_F<3^{-1/3}\)).

## 2. Exact projective recurrence

Fix \(0<t\le10^{-2}\), and put \(u=t^2\).  After (1), and at every later
step as proved below, write

\[
 R_k=c_k\operatorname{diag}(-a_k,-b_k,1),\qquad
 c_k>0,quad a_k,b_k>0,quad q_k=c_k^2.                 \tag{2}
\]

Set

\[
 m(a,b)={a^4+b^4+1\over a^2+b^2+1},\qquad
 d(a,b,q)=1-m+qm.
\]

The exact recurrence induced by the matrix update is

\[
\begin{aligned}
 a^+&={a^2(m-a^2-qma^2)\over d},\\
 b^+&={b^2(m-b^2-qmb^2)\over d},\\
 q^+&=q^4d^2.                                           \tag{3}
\end{aligned}
\]

At \(q=0\), denote the first two maps by \(P_1,P_2\). Direct expansion
gives the retraction identities

\[
 P_1(a,b)+P_2(a,b)=1,                                  \tag{4}
\]

and \(P(a,b)=(a,b)\) whenever \(a+b=1\).  Thus the
leading homogeneous quartic map sends every point in this sign chart to the
fixed-direction line \(a+b=1\).  This is the structural reason that the
neutral projective direction does not prevent convergence.

More precisely, if \(e=1-a-b\), then exact algebra gives

\[
 1-a^+-b^+
 ={q(a^4+b^4+1)^2\over
   a^2-a^4+b^2-b^4+q(a^4+b^4+1)}.                      \tag{5}
\]

## 3. Rational orbit enclosure

Consider the rational box (with the additional displayed defect condition)

\[
 \mathcal B:\quad {3\over10}\le a\le {2\over5},\quad
 {3\over5}\le b\le {3\over4},\quad
 0\le e=1-a-b\le {1\over100},\quad 0<q\le10^{-12}.
                                                                  \tag{6}
\]

This box is an invariant enclosure for the particular one-parameter family:
every orbit initialized by \(0<t\le10^{-2}\) enters it at \(k=1\) and never
leaves. Here is a rational no-exit proof.

For \((a,b,q)\in\mathcal B\), let
\(L=a^2-a^4+b^2-b^4\). The bounds in (6) give

\[
 L\ge {153\over500},\qquad
 1+a^2+b^2\le {689\over400},\qquad
 d\ge {L\over1+a^2+b^2}>{1\over6}.                    \tag{7}
\]

They also make both numerators in (3) positive, so the signs in (2) persist.
Indeed \(b^2>a^2\), hence \(m-a^2>0\), while
\[
 m-b^2={1-b^2+a^2(a^2-b^2)\over1+a^2+b^2}
 \ge {139\over689};
\]
subtracting the terms containing \(q\le10^{-12}\) preserves strict
positivity. Since \(a^4+b^4+1<27/20\), equations (3) and (5) imply

\[
 0\le e^+\le6q,qquad q^+\le2q^4.                     \tag{8}
\]

The factorizations

\[
 P_1-a={-a(a+1)(a-b^2)(a-b-1)(a+b-1)\over
              a^4-a^2+b^4-b^2},
\]

\[
 P_2-b={-b(b+1)(a^2-b)(a-b+1)(a+b-1)\over
              a^4-a^2+b^4-b^2}
\]

and the rational bounds in (6)--(7) yield

\[
 |P_1-a|\le e,\qquad |P_2-b|\le3e.                    \tag{9}
\]

Finally, differentiation of (3) with respect to \(q\), with \(a,b\) held
fixed, gives

\[
 \left|{\partial a^+\over\partial q}\right|
 ={a^2m^2(1-a^2)\over d^2}\le6,
 \qquad
 \left|{\partial b^+\over\partial q}\right|
 ={b^2m^2(1-b^2)\over d^2}\le21.                     \tag{10}
\]

Hence

\[
 |a^+-a|\le e+6q,qquad |b^+-b|\le3e+21q.             \tag{11}
\]

For the first iterate, (1) gives

\[
 a_1={6-7u\over18+567u},\quad
 b_1={12-112u\over18+567u},\quad
 e_1={686u\over18+567u},\quad
 q_1=u^4(18+567u)^2.                                  \tag{12}
\]

For \(0<u\le10^{-4}\), these satisfy

\[
 {33\over100}\le a_1\le {1\over3},\quad
 {13\over20}\le b_1\le {2\over3},\quad
 0\le e_1\le {1\over250},\quad q_1<10^{-12}.          \tag{13}
\]

While the orbit is in \(\mathcal B\), (8) gives
\(\sum_{j\ge1}q_j<2q_1\) and

\[
 \sum_{j\ge1}e_j< {1\over250}+12q_1.
\]

Consequently (11) bounds the total variations by

\[
 \sum_{j\ge1}|a_{j+1}-a_j|< {1\over200},\qquad
 \sum_{j\ge1}|b_{j+1}-b_j|< {13\over1000}.            \tag{14}
\]

The margins in (13) show that none of the four ratio boundaries in (6) can
be the first exit; (5) and (8) exclude exits through the defect and scale
boundaries. This proves the claimed no-exit enclosure without assuming the
conclusion.

## 4. Two-sided quartic bounds and the Q-order limit

Let \(S_k=(1+a_k^2+b_k^2)^{1/2}\).  From (3), (6), and (7),

\[
 c_{k+1}=c_k^4d_k,qquad {1\over6}<d_k<1,qquad
 1<S_k<{4\over3}.                                      \tag{15}
\]

It follows, for every \(k\ge1\), that

\[
 {27\over512}\|R_k\|_F^4
 <\|R_{k+1}\|_F
 <{4\over3}\|R_k\|_F^4.                              \tag{16}
\]

In particular the nonzero quartic behavior is not a one-step artifact.

Equations (8), (11), and the summability used in (14) show that
\((a_k,b_k)\) is Cauchy. Write its limit as \((a_\infty,b_\infty)\).
Equation (5) implies
\(a_\infty+b_\infty=1\), and (6) keeps both coordinates away from zero.
Put

\[
 m_\infty={a_\infty^4+b_\infty^4+1\over
                 a_\infty^2+b_\infty^2+1},\qquad
 S_\infty=(1+a_\infty^2+b_\infty^2)^{1/2}.
\]

Taking the limit in the exact identity

\[
 {\|R_{k+1}\|_F\over\|R_k\|_F^4}
 ={d_kS_{k+1}\over S_k^4}
\]

gives

\[
 \boxed{\displaystyle
 \lim_{k\to\infty}{\|R_{k+1}\|_F\over\|R_k\|_F^4}
 ={1-m_\infty\over S_\infty^3}\in(0,\infty).}        \tag{17}
\]

Thus every orbit in the explicit interval \(0<t\le10^{-2}\) has Q-order
exactly four.  The limiting direction generally depends on \(t\); as
\(t\downarrow0\), it tends to
\((-1/3,-2/3,1)\), and (17) tends to
\(6/14^{3/2}\).

## 5. Exact defect in the source proof

The primary PDF, p.4, equation (2.7), replaces the quartic term by
\(\epsilon_k\|e_k\|^4\) with \(\epsilon_k\to0\).  The preceding estimate
establishes at most a bounded coefficient (a big-O quartic term), not a
vanishing normalized coefficient; (1) and (16) show that the latter claim is
false on this diagonal family.  The next sentence has a second quantifier
error: even if \(\epsilon_k\to0\) were granted, the definition only says that
for each *fixed* \(\epsilon>0\) there is an index after which
\(\epsilon_k\le\epsilon\).  Substituting the moving value
\(\epsilon=\|e_k\|^2\) does not provide one eventual index and would require
the unproved stronger estimate \(\epsilon_k=O(\|e_k\|^2)\).

This argument refutes the general order-six assertion in Theorem 2.1. It does
not assert that convergence fails, and it does not classify all CTM orbits.
