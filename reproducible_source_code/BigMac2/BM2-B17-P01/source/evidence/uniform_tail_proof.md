# Uniform proof for the infinite tail

This note proves the analytic part of the frozen claim.  It uses no
floating-point estimates.  Together with the exact finite computation in
`resolution_check.py`, it proves the claim for every integer \(n\ge496\).

## 1. Localization and the only bound on the maximizer that is needed

Write
\[
 q_n(a)=\frac{R_n(a-1)}{R_n(a)},\qquad
 t=n-2a+1,
\]
for \(2\le a<n/2\).  Directly from the supplied adjacent-ratio identity,
\[
 \operatorname{sgn}(q_n(a)-1)=\operatorname{sgn}H_n(t),
 \qquad
 H_n(t)=n^2-n(2t^2+3t)-t-1.
\]
Moreover
\[
 H_n(t+2)-H_n(t)=-n(8t+14)-2<0.
\]
Thus \(H_n(n-2a+1)\) increases strictly with \(a\).  For \(n\ge100001\)
it is negative at \(a=2\), and it is positive at the last admissible
\(a\) (use \(H_n(2)=n^2-14n-3\) for odd \(n\), and
\(H_n(3)=n^2-27n-4\) for even \(n\)).  Let \(a_0\) be the first index at
which it is nonnegative.  Then \(a_*=a_0-1\) is a row maximizer; if the
value at \(a_0\) is zero, \(a_0\) is the only other maximizer and has the
same value.

Put
\[
 x=n-2a_*.
\]
The two adjacent signs give
\[
 H_n(x+1)<0\le H_n(x-1).
\]
In particular,
\[
 0\le n^2-n(2x^2-x-1)-x,
\]
so \(2x^2-x-1<n\).  Here \(x\ge2\), and hence
\[
 \boxed{x^2<n.}\tag{1}
\]

## 2. Explicit binomial bounds

The following consequence of the classical one-sided Stirling bounds will be
used.  If \(m\ge1\), \(0<k<m\), \(p=k/m\), then
\[
 \binom mk
 <\frac{\exp(mh(p)+1/(12m))}{\sqrt{2\pi m p(1-p)}}.\tag{2}
\]
Indeed, apply
\[
 \sqrt{2\pi r}(r/e)^r<r!
 <\sqrt{2\pi r}(r/e)^r e^{1/(12r)}
\]
to the numerator and denominator factorials.  If
\(k=(m-x)/2\), then
\[
 \log2-h(p)
 =\tfrac12\big((1-x/m)\log(1-x/m)
 +(1+x/m)\log(1+x/m)\big)
 \ge \frac{x^2}{2m^2};
\]
the last inequality follows by differentiating, since
\(\operatorname{artanh}u\ge u\) for \(u\ge0\).  Therefore (2) gives
\[
 \binom m{(m-x)/2}
 <2^m\sqrt{\frac{2}{\pi m(1-x^2/m^2)}}
   \exp\!\left(-\frac{x^2}{2m}+\frac1{12m}\right).\tag{3}
\]
The same Stirling bounds, now lower-bounding the numerator factorial and
upper-bounding both denominator factorials, give for \(M\ge1\)
\[
 \binom{2M}{M}>
 \frac{4^M}{\sqrt{\pi M}}\exp\!\left(-\frac1{6M}\right).\tag{4}
\]

## 3. A uniform majorant

Since \(a_*=(n-x)/2\), the defining expression becomes
\[
 R_n(a_*)=\frac{2n(x+1)}{n+x}
 \frac{\binom n{(n-x)/2}\binom{n-2}{(n-2-x)/2}}
      {\binom{2n-2}{n-1}}.\tag{5}
\]
Apply (3) with \(m=n,n-2\), apply (4) with \(M=n-1\), and set
\[
 A_n=\frac{n-1}{n(n-2)},\qquad
 E_n=\frac1{12n}+\frac1{12(n-2)}+\frac1{6(n-1)}.
\]
Using \(n/(n+x)<1\) in (5) yields
\[
 R_n(a_*)<\frac{4\sqrt{A_n}}{\sqrt\pi}\,
 \frac{(x+1)e^{-A_nx^2+E_n}}
 {\sqrt{(1-x^2/n^2)(1-x^2/(n-2)^2)}}.\tag{6}
\]
For \(A>0\) and \(x\ge0\),
\[
 (x+1)e^{-Ax^2}
 \le \frac1{\sqrt{2eA}}+1,\tag{7}
\]
because \(xe^{-Ax^2}\le1/\sqrt{2eA}\) and \(e^{-Ax^2}\le1\).
By (1), the remaining denominator in (6) is bounded below using
\[
 C_n=\left((1-1/n)\left(1-\frac{n}{(n-2)^2}\right)\right)^{-1/2}.
\]
Consequently
\[
 R_n(a_*)<
 \frac4{\sqrt\pi}\left(\frac1{\sqrt{2e}}+\sqrt{A_n}\right)
 C_ne^{E_n}.\tag{8}
\]
Each of \(A_n,E_n,C_n\) decreases for real \(n>2\): for \(C_n\), note
that both \(1/n\) and \(n/(n-2)^2\) decrease.  Hence the right side of
(8) is at most its endpoint bound at \(N=100001\).

Here is a wholly rational certification of that endpoint.  The elementary
bounds \(\pi>3\) and
\(e>\sum_{j=0}^6 1/j!=1957/720>2718/1000\), together with direct integer
cross-multiplication, give
\[
\begin{aligned}
 \frac4{\sqrt\pi}&<\frac{231}{100},&
 \frac1{\sqrt{2e}}&<\frac{429}{1000},\\
 \sqrt{A_N}&<\frac{3163}{10^6},&
 C_N&<\frac{1000011}{10^6},\\
 e^{E_N}&<\frac{1000004}{10^6}.&&
\end{aligned}\tag{9}
\]
For the last inequality use \(e^u\le(1-u)^{-1}\) for \(0\le u<1\).
All cross-products in (9) are serialized and rechecked by
`resolution_check.py`.  Substitution in (8) gives the exact rational bound
\[
 R_n(a_*)<
 \frac{231}{100}\frac{432163}{10^6}
 \frac{1000011}{10^6}\frac{1000004}{10^6}
 =\frac{24957787612296876183}{25000000000000000000}<1.\tag{10}
\]
Thus every row maximum is strictly below one for every \(n\ge100001\),
including both parities and any possible adjacent maximizing tie.

## 4. Scope

Equation (10) is an infinite-tail theorem, not a numerical extrapolation.
The separate exact scan verifies every row \(496\le n\le100000\).  These
two disjoint ranges exhaust the frozen target \(n\ge496\).
