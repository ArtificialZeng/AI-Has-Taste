# Exact re-derivation and zero-set classification

All parameters below satisfy (p,q>0).  Put

\[
x=\sqrt p,\qquad S=\sinh x,\qquad C=\cosh x,
\qquad A=xC-S,\qquad B=A+qS.
\]

Equation (57) of the frozen source, with (R=D=1), is

\[
 \phi(p,q)=\frac{3qA}{x^2B}.
\tag{1}
\]

Here \(\phi=\Pr(\tau<\delta)\).  Since \(A(0)=0\) and
\(A'(x)=x\sinh x>0\), we have \(A>0\); hence also \(B>0\).
The raw-moment identities (D6) and (D8) are linear in \(\phi\) and its
derivatives.  Consequently they remain valid after averaging over the
uniform initial point (differentiation commutes with this finite spatial
average).  Direct differentiation of (1) gives

\[
 \phi_q=\frac{3A^2}{x^2B^2},\qquad
 \phi_p=\frac{3q\{xq(SC-x)-2AB\}}{2x^4B^2}.
\tag{2}
\]

Substitution into (D6) and (D8) gives all five requested moments:

\[
\begin{aligned}
 \mathbb E T&=\frac{x^2B-3qA}{x^4B},
&\mathbb E L&=\frac{3A}{x^2B},\\
 \mathbb E T^2&=\frac{2x^2B^2-12qAB+3q^2x(SC-x)}{x^6B^2},
&\mathbb E L^2&=\frac{6AS}{x^2B^2},\\
 \mathbb E(TL)&=\frac{3\{2A(A+B)+qx(x-SC)\}}{2x^4B^2}.
\end{aligned}
\tag{3}
\]

In particular, (D8) first gives the useful unsimplified identity

\[
 \operatorname{Cov}(T,L)
 =\frac{-p\phi_p+q\phi_q+(\phi-1)\phi}{pq}.
\tag{4}
\]

Using (1)--(2) in (4), and using
\(AC-xS^2=x-SC\), yields

\[
 \boxed{\operatorname{Cov}(T,L)
 =\frac{3}{4x^6B^2}\bigl(\xi_1(x^2)+q\xi_2(x^2)\bigr)},
\tag{5}
\]

where

\[
 \xi_1(x^2)=4x^2A^2,
 \qquad
 \xi_2(x^2)=2x^3(x-SC)+12A^2.
\tag{6}
\]

Expanding the right side of (6) with
\(2SC=\sinh(2x)\), \(2C^2=\cosh(2x)+1\), and
\(2S^2=\cosh(2x)-1\) gives exactly the printed (F5b):

\[
 \xi_2(x^2)=2x^2(x^2+3)-x(x^2+12)\sinh(2x)
 +6(x^2+1)\cosh(2x)-6.
\tag{7}
\]

## Exact sign of the numerator

Taylor expansion of (7) is exact (the series are entire).  The coefficients
of \(x^0,x^2,x^4,x^6,x^8\) cancel.  For \(n\ge3\), the coefficient of
\(x^{2n}\), before the cancellations at \(n=3,4\), is

\[
 \frac{2^{2n-3}}{(2n)!}
 \{-m(m-1)(m-2)-48m+12m(m-1)+48\},\quad m=2n.
\]

The polynomial in braces is
\(-(m-1)(m-6)(m-8)\).  Therefore

\[
 \xi_2(x^2)=-\sum_{n=5}^{\infty}
 \frac{2^{2n-3}(2n-1)(2n-6)(2n-8)}{(2n)!}x^{2n}<0
 \quad(x>0).
\tag{8}
\]

Also \(\xi_1(x^2)>0\) because \(x,A>0\).  Every factor outside the
parentheses in (5) is positive.  Hence the complete zero set in the open
positive quadrant is the single analytic graph

\[
 \boxed{q=q_0(p):=-\frac{\xi_1(p)}{\xi_2(p)},\qquad p>0.}
\tag{9}
\]

For each fixed \(p>0\), the covariance is positive for
\(0<q<q_0(p)\), zero at \(q=q_0(p)\), and negative for \(q>q_0(p)\).
There are no other zeros.

## Variance audit

Both variables have finite second moments: \(0\le T\le\delta\) and
\(0\le L\le\widehat\ell\), while the two upper bounds are exponential.
They are also nonconstant.  For every fixed \(t>0\),
\(\Pr(T<t)\ge\Pr(\delta<t)>0\), whereas

\[
 \Pr(T>t)=\mathbb E[e^{-pt-q\ell_t}]>0
\]

because finite-time reflected-Brownian local time is finite almost surely.
Thus \(\operatorname{Var}(T)>0\).  If \(H_\Gamma\) is the first boundary
hitting time, then the volume-uniform starting point lies in the interior
and continuity gives \(H_\Gamma>0\) almost surely.  Independence of \(\delta\)
therefore gives
\(\Pr(\delta<H_\Gamma)=\mathbb E[1-e^{-pH_\Gamma}]>0\); on this event
\(L=0\).  On the other hand, (3) gives
\(\mathbb E L=3A/(x^2B)>0\), so \(\Pr(L>0)>0\).  Hence
\(\operatorname{Var}(L)>0\).  This also validates the sign equivalence with
the Pearson correlation throughout the open quadrant.

## Exact counterexample

Take \((p,q)=(1,200)\).  Then \(A=e^{-1}\).  With \(y=e^2\), exact
algebra gives

\[
 2y\{\xi_1(1)+200\xi_2(1)\}=8-200(y^2-4y-25).
\tag{10}
\]

The positive-term exponential series supplies the rational certificate

\[
 e^2>\sum_{n=0}^{11}\frac{2^n}{n!}
 =\frac{164591}{22275}
 =\frac{7389}{1000}+\frac{41}{891000}.
\]

Since \(f(y)=y^2-4y-25\) is strictly increasing for \(y>2\),

\[
 f(e^2)>f(7389/1000)=\frac{41321}{10^6}>\frac1{25}.
\]

Thus the right side of (10) is strictly negative.  Equation (5) proves the
exact conclusion
\(\operatorname{Cov}_{1,200}(T,L)<0\), disproving the frozen universal
positivity assertion.

