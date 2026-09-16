# Ishii positivity for the two-parameter double-twist family

## Statement

Let \(D(p,q)=D(b_1,b_2)\), with \(p,q\geq1\), be the alternating
2-bridge knot in the notation of Kohli, §2.3.2.  Equivalently, this is the
standard double-twist subfamily with two positive full-twist parameters.
Then

\[
  LG(D(p,q);-x,-y)\in
  \mathbb Z_{\geq0}[x^{\pm1},y^{\pm1}].
\tag{T}
\]

Consequently the coefficients of \(LG(D(p,q);t_0,t_1)\) satisfy Ishii's
alternating-sign conjecture.  The case \(p=q=1\) is the figure-eight knot.

## Published input

For

\[
 a_1(n)=\frac{(t_0t_1)^n-1}{t_0t_1-1},\qquad
 a_3(n)=(t_0-1)(t_1-1)a_1(n)+1,
\]

and

\[
 a_2(n)=\frac{2n(t_0-1)(t_1-1)}{t_0t_1-1}
 -a_1(n)\left(
 \frac{(t_0t_1+1)(t_0-1)(t_1-1)}{t_0t_1-1}+1\right),
\]

Kohli's Corollary 2.12 and the proof of Theorem 2.15 give

\[
\begin{aligned}
 LG(D(p))&=\widetilde a_1(p)+\widetilde a_2(p),\\
 LG(D(p,q))&=a_1(q)LG(D(p-1))+a_2(q)LG(D(p))+a_3(q),
\end{aligned}
\tag{K}
\]

where \(\widetilde f(t_0,t_1)=f(t_0^{-1},t_1^{-1})\),
\(D(0)\) is split and hence has invariant zero, and the last term in the
second line uses \(LG(\bigcirc)=1\).

## Positive finite sums

Put \(U=xy\), \(H^+=(1+x)(1+y)\), and
\(H^-=(1+x^{-1})(1+y^{-1})\).  For \(n\geq0\), put

\[
 A_n^\pm=\sum_{k=0}^{n-1}U^{\pm k},\qquad
 E_n^\pm=\sum_{k=0}^{n-1}(2(n-k)-1)U^{\pm k},
\]

with empty sums equal to zero.  Direct algebra in the Laurent polynomial
ring gives

\[
\begin{aligned}
 a_1(n)(-x,-y)&=A_n^+,\\
 -a_2(n)(-x,-y)&=A_n^++H^+E_n^+,\\
 a_3(n)(-x,-y)&=1+H^+A_n^+.
\end{aligned}
\tag{1}
\]

For completeness, the only quotient hidden in the displayed definition of
\(a_2\) is removed by

\[
 \frac{(U+1)A_n^+-2n}{U-1}=E_n^+.
\]

Indeed, multiplying the asserted identity by \(U-1\) and telescoping proves
it term by term.  In particular, every polynomial on the right of (1) has
nonnegative coefficients.  Inverting \(x,y\) gives the analogous formulas
with superscript minus.

Let \(G_p=-LG(D(p);-x,-y)\).  The first line of (K) and (1) give

\[
 G_p=H^-E_p^-.
\tag{2}
\]

Moreover,

\[
 E_p^- -E_{p-1}^-
 =U^{-(p-1)}+2A_{p-1}^-.
\tag{3}
\]

## Proof of (T)

Substitute (1)--(3) into the second line of (K).  Since the one-block links
have the opposite global sign, one obtains the exact identity

\[
\boxed{\begin{aligned}
LG(D(p,q);-x,-y)={}&
A_q^+H^-\bigl(U^{-(p-1)}+2A_{p-1}^-\bigr)\\
&+H^+E_q^+H^-E_p^-+1+H^+A_q^+.
\end{aligned}}
\tag{4}
\]

Every factor and every summand on the right of (4) belongs to
\(\mathbb Z_{\geq0}[x^{\pm1},y^{\pm1}]\).  This proves (T), including
\(p=1\) or \(q=1\), because the empty-sum convention handles those
boundaries.  Finally, if
\(LG(D(p,q);t_0,t_1)=\sum a_{ij}t_0^it_1^j\), (T) is exactly
\((-1)^{i+j}a_{ij}\geq0\) for every \(i,j\), which implies Ishii's pairwise
condition.  No limiting, division-by-zero, or floating-point step remains.
