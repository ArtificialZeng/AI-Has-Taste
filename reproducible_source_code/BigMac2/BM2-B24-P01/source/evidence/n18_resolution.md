# Exact resolution certificate for \(C_{18}\)

## Claim

For
\[
F(z)=C_{18}(z)=
\frac{z^{19}(12654z^{36}-684z^{18}-306)}
     {2(19z^{18}-1)^3},
\]
every Fatou component is contained in the attracting basin of one of
\(0\) or the eighteen roots of unity. Thus the frozen claim in `source.md`
is true.

The only general complex-dynamical inputs used below are the standard facts
recorded on PDF pp. 5--6 of `literature/2609.02884v1.pdf`: Sullivan's
no-wandering-domain theorem, the classification of periodic Fatou components,
and Lemma 2.4 (critical-point capture for attracting/parabolic basins and the
postcritical-boundary property for rotation domains).

## 1. Exact free-critical orbit

Put
\[
Q(x)=\frac{x^{19}(12654x^{36}+684x^{18}-306)}
              {2(19x^{18}+1)^3}=xq(x^{18}),\qquad
q(t)=\frac{t(12654t^2+684t-306)}{2(19t+1)^3}.
\]
Direct substitution shows that if
\(\lambda=\exp(\pi i/18)\) and \(k\) is odd, then
\(F(\lambda^k x)=\lambda^kQ(x)\) for real \(x\). The free critical
points are precisely \(\lambda^k\widetilde c\), for odd \(k\), where
\[
\widetilde c^{18}=t_0=\frac{17}{703}.
\]
If \(x_{j+1}=Q(x_j)\) and \(t_j=x_j^{18}\), then
\[
t_{j+1}=t_jq(t_j)^{18}.
\]

Exact reduction gives
\[
q(t_0)=-\frac{10693}{9747},\qquad
t_1=\frac{17\,10693^{18}}{703\,9747^{18}}.
\]
The two integer cross-product gaps are
\[
\begin{aligned}
125(17)10693^{18}-16(703)9747^{18}
 &=6509250070784751692384879424159087472754312233670749508990922543077280853,\\
13(703)9747^{18}-100(17)10693^{18}
 &=83439327875066059753403827793076796853295339472208955993979384424711909671.
\end{aligned}
\]
Both are positive, so
\[
\frac{16}{125}<t_1<\frac{13}{100}. \tag{1}
\]

Let \(A(t)=12654t^2+684t-306\). It is increasing for \(t>0\), and
\[
A(13/100)=-\frac{16137}{5000}<0,
\]
so (1) gives \(q(t_1)<0\). Expanding the other desired inequality gives
\[
q(t)+\frac1{50}=\frac{H(t)}{50(19t+1)^3},\qquad
H(t)=323209t^3+18183t^2-7593t+1.
\]
Now
\[
H(16/125)=\frac{9423189}{1953125}>0,
\quad
H'(16/125)=\frac{202315887}{15625}>0,
\]
and \(H''(t)=1939254t+36366>0\) for \(t\ge0\). Hence \(H\) is
positive throughout the interval in (1), proving
\[
-\frac1{50}<q(t_1)<0. \tag{2}
\]
Consequently
\[
0<t_2=t_1q(t_1)^{18}
 <\frac{13}{100}\left(\frac1{50}\right)^{18}
 <\frac1{100}. \tag{3}
\]
All calculations in this subsection are independently executable, using only
integer/rational arithmetic, in `evidence/verify_orbit_threshold.py`.

## 2. The exact capture threshold

Set
\[
P(t)=13186t^3+1425t^2-96t+1.
\]
The identities
\[
q(t)+1=\frac{P(t)}{(19t+1)^3},\qquad
q(t)-1=-\frac{532t^3+741t^2+210t+1}{(19t+1)^3} \tag{4}
\]
hold by expansion. Moreover
\[
P'(t)=6(6593t^2+475t-16).
\]
The quadratic in parentheses is increasing for \(t\ge0\), and its value at
\(1/100\) is \(-105907/10000\). Thus \(P\) decreases on
\([0,1/100]\), while
\[
P(1/100)=\frac{97843}{500000}>0.
\]
There is no root in that interval. Since
\[
P(1/70)=-\frac{1808}{42875}<0,
\]
there is a positive root. If \(t_*\) denotes the smallest positive root,
then
\[
\frac1{100}<t_*<\frac1{70}. \tag{5}
\]

For \(0<t<t_*\), (4) and the definition of the first root give
\(-1<q(t)<1\). It follows that whenever \(0<|x|^{18}<t_*\),
\[
|Q(x)|=|x|\,|q(|x|^{18})|<|x|. \tag{6}
\]
Iteration preserves this interval. The decreasing nonnegative sequence
\(|Q^m(x)|\) has a limit \(L\). If \(L>0\), continuity and (6) give
\(L=L|q(L^{18})|<L\), a contradiction. Hence \(Q^m(x)\to0\).

Combining (3) and (5), the second iterate of \(\widetilde c\) satisfies
\(|Q^2(\widetilde c)|^{18}=t_2<t_*\), and therefore
\(Q^m(\widetilde c)\to0\). Oddness handles \(-\widetilde c\), and the
line conjugacies handle every free critical point of \(F\). Thus every free
critical point belongs to the full basin \(B(0)\). This conclusion concerns
the full basin, not necessarily the immediate component.

## 3. Exhaustion of all Fatou components

Direct differentiation gives
\[
F'(z)=\frac{18\cdot19\,z^{18}(z^{18}-1)^2(703z^{18}+17)}
              {2(19z^{18}-1)^4}.
\]
Together with the local degree three at each pole, this lists all critical
points (the multiplicities sum to \(108=2\deg(F)-2\), since \(\deg F=55\)):

1. \(0\), which is a superattracting fixed root;
2. the eighteen roots of unity, each a superattracting fixed root;
3. the eighteen poles \(z^{18}=1/19\), each mapped to \(\infty\);
4. the eighteen free critical points \(703z^{18}+17=0\), all in \(B(0)\)
   by Sections 1--2.

At infinity,
\[
F(z)=\frac{333}{361}z+O(z^{-17}),
\]
so in the coordinate \(w=1/z\) the multiplier is \(361/333>1\).
Thus \(\infty\) is repelling and the poles, as its preimages, lie in the
Julia set.

It remains to check that critical capture really implies the frozen global
statement. An attracting or parabolic periodic basin must contain a critical
point in its immediate basin cycle. The orbit of such a critical point must
converge to that attracting or parabolic cycle. The list above leaves only
the superattracting fixed root cycles: root critical points are fixed, free
critical points tend to \(0\), and pole critical points land on the repelling
fixed point \(\infty\). Hence no non-root attracting or parabolic periodic
Fatou component exists.

There is no rotation domain either. The closure of the postcritical set is a
finite union of convergent free-critical orbits (whose only limit is the Fatou
point \(0\)), fixed roots in the Fatou set, and the finite pole/\(\infty\)
set. Its intersection with the Julia set is therefore finite. Lemma 2.4 of
the supplied source would put the entire boundary of any Siegel disk or Herman
ring in this finite set. This is impossible: such a boundary is infinite.
(Indeed, a domain with finite boundary is the sphere minus that boundary; it
cannot be conformally a disk or a finite-modulus annulus.)

Finally, Sullivan's theorem makes every Fatou component periodic or
preperiodic. By the periodic-component classification and the preceding two
paragraphs, every eventual periodic component is an immediate basin of one of
the nineteen roots. Therefore every point of the original component tends
to that same root. This proves exactly the frozen claim.

## Audit boundary

The exact arithmetic and all map-specific implications are supplied above.
A fresh referee should recheck (i) the two cross-products and threshold signs,
(ii) the passage from (4) to contraction, (iii) completeness of the critical
list, and (iv) the use of the standard periodic-Fatou-component theorems. No
claim is made here for any \(n\ne18\), Julia topology, or convergence speed.

