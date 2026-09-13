# Formal statement

## Formal-series setting

Let (t) be an indeterminate and let

\[
s=(1-2t)^{1/2}\in \mathbb Q[[t]]
\]

denote the unique formal square root with (s(0)=1).  Formal exponentiation is
used throughout.  Define

\[
F(t)=\frac{1+s}{s}\exp(-1-t+s)-(2-t)e^{-t}
     =\sum_{n\ge 0}a_n\frac{t^n}{n!}.
\]

Equivalently, on the analytic disk (|t|<1/2), take the square-root branch
with value (1) at (t=0).  Thus (a_n=n![t^n]F(t)) is unambiguous for every
integer (n\ge0).

## The assertion to prove

For every integer (n\ge4),

\[
\begin{aligned}
0={}&(2-n)a_n+(2n^2-8n+7)a_{n-1}
 +(6n^2-18n+11)a_{n-2}\\
&+(n-1)(6n-11)a_{n-3}
 +2(n-1)(n-2)a_{n-4}.
\end{aligned}
\]

The required initial values in the formal-series normalization are

\[
(a_0,a_1,a_2,a_3)=(0,0,1,1).
\]

The recurrence at (n=4) then gives (a_4=21).  In the native OEIS offset
(1), one may instead state the recurrence for (n\ge5), with
((a_1,a_2,a_3,a_4)=(0,1,1,21)).  The displayed equation is also true at
(n=4) after the canonical EGF extension (a_0=F(0)=0).

## D-finiteness endpoint

It is enough to exhibit a nonzero operator

\[
L=\sum_{j=0}^r p_j(t)D^j,\qquad p_j(t)\in\mathbb Q[t],\quad D=d/dt,
\]

such that (L(F)=0), and then extract coefficients exactly.  No minimality of
the differential order or recurrence order is claimed.  The proof will give
both a third-order annihilator and a fifth-order left multiple whose
coefficient equation is exactly the four-step OEIS recurrence.

## Endpoints and degeneracies

- The branch condition (s(0)=1) is essential; the other algebraic branch is
  not the stated EGF.
- Any rational-function denominators used during elimination have nonzero
  constant term, so the manipulations are valid in (mathbb Q[[t]]).
- The recurrence is not used at (n=2), where its leading coefficient
  (2-n) vanishes.
- Negative-index coefficients are neither needed nor defined.
- The combinatorial interpretation is inherited from Krasko--Omelchenko's
  EGF theorem; the new mathematical endpoint is the formal implication from
  that EGF to the recurrence.
