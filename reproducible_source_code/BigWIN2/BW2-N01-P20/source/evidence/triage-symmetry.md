# Independent algebraic screen

Job: newwin-00001-p20-triage-041b4cdafc30; 2026-09-12.
This records exact reductions and a conditional coefficient calculation.
It is not an independently refereed proof of the requested uniform bound.

Put \(n=2m-1\), \(d=k-m\), \(h=m^{-1/2}\),
\(p_{m,j}=2^{-n}\binom n{m+j}\), and
\(S_{m,j}=\Pr\{\operatorname{Bin}(n,1/2)\le m+j\}\).
The exact symmetry \(p_{m,j}=p_{m,-j-1}\) implies
\(S_{m,-1}=1/2\). Thus
\[
S_{m,d}=\begin{cases}
1/2+\sum_{j=0}^{d}p_{m,j},&d\ge0,\\
1/2-\sum_{j=d+1}^{-1}p_{m,j},&d\le-1.
\end{cases}
\]
In a fixed central window these sums contain only \(O_A(\sqrt m)\) terms.
The frozen expectation becomes exactly
\[
E_{m,m+d}=\begin{cases}
S_{m,d}/p_{m,d},&d<0,\\
S_{m,-d-2}/p_{m,d}+2m(d+1)/(m+d+1),&d\ge0.
\end{cases}
\]
The final rational term follows directly by taking the ratio of two
binomial coefficients; it is essential to the constant term.

## Local lemma to establish in research

Let \(f(t)=e^{-t^2}/\sqrt\pi\). The proposed sufficient estimate, uniformly
for integer \(|j|\le B\sqrt m\), is
\[
p_{m,j}=h f(jh)\{1-(jh)h+O_B(h^2)\}. \tag{L}
\]
It can be approached from the exact identity
\[
p_{m,j}=(1-j/m)\,4^{-m}\binom{2m}{m+j}.
\]
A Stirling expansion for the even central binomial coefficient should have
relative error \(O_B(m^{-1})\), since its first displacement correction is
quadratic and its exponent correction \(j^4/m^3\) is \(O_B(m^{-1})\).
Research must supply explicit uniform remainder inequalities, not merely
pointwise formal series.

Assuming (L), a trapezoidal estimate on the above finite interval gives
\[
S_{m,d}=\Phi(\sqrt2\,dh)+h f(dh)+O_B(h^2). \tag{C}
\]
Indeed the endpoint contribution \(h(f(0)+f(dh))/2\), combined with
\(-h\int_0^{dh}t f(t)\,dt=h(f(dh)-f(0))/2\), is \(h f(dh)\).
Signed finite sums give the same calculation when \(d<0\). Bounded
derivatives on a fixed compact interval suffice for the quadrature error.
This route avoids a global Berry--Esseen or Edgeworth citation and avoids
estimating far tails.

For \(d=x/h+\delta\), \(-1<\delta\le0\), (L)--(C) give, conditionally,
\[
\begin{aligned}
p_{m,d}&=h f(x)\{1-(2\delta+1)xh+O_A(h^2)\},\\
S_{m,d}&=\Phi(\sqrt2 x)+(\delta+1)h f(x)+O_A(h^2),\\
S_{m,-d-2}&=\Phi(-\sqrt2 x)-(\delta+1)h f(x)+O_A(h^2),\\
\frac{2m(d+1)}{m+d+1}&=\frac{2x}{h}+2(\delta+1)-2x^2+O_A(h).
\end{aligned}
\]
Here \(\Phi(z)=(2\pi)^{-1/2}\int_{-\infty}^z e^{-t^2/2}\,dt\).
Consequently the independently recovered coefficients agree with the
handoff proposal. With
\(H_-(x)=\sqrt\pi e^{x^2}\Phi(\sqrt2 x)\) and
\(H_+(x)=\sqrt\pi e^{x^2}\Phi(-\sqrt2 x)\), they are
\[
F_0(x)=
\begin{cases}H_-(x),&x<0,\\H_+(x)+2x,&x\ge0,\end{cases}
\]
\[
F_1(x,\delta)=
\begin{cases}
(2\delta+1)xH_-(x)+\delta+1,&x<0,\\
(2\delta+1)xH_+(x)+\delta+1-2x^2,&x\ge0.
\end{cases}
\]

## Exact boundary checks

\[
E_{m,m-1}=\frac{2^{2m-1}}{\binom{2m}{m}},\qquad
E_{m,m}=E_{m,m-1}+\frac{m-1}{m+1}.
\]
Both hold also at \(m=1\). Thus the one-step central jump tends to 1.
It is consistent with \(F_0(0)=\sqrt\pi/2\), \(F_1(0,0)=1\), and the
left-cell limit \(\delta\to-1\), for which \(F_1\to0\) as \(x\to0-\).
Continuity of \(F_1\) after ignoring the floor is not a valid requirement.
At the global finite endpoints \(E_{m,0}=1\) and \(E_{m,2m-1}=m\).

The remaining decisive mathematical test is (L), with a bound uniform on
each compact interval, followed by the signed quadrature error in (C).
Only then can the conditional calculation become a proof of the original
two-term statement.
