# A uniform positive band of Newton coefficients

Job: `primary-20260913-subsum-denominator-research-983c87564404`.
This is a proved auxiliary lemma and its application, not a resolution of K,
H, or the original denominator claim. It has not received a fresh referee
or novelty clearance. The argument uses exact algebra, not fitted data.

For a symmetric bivariate series W with nonnegative powers, define

\[
\mathcal L_j(W)=[x^jy^j]W-[x^{j-1}y^{j+1}]W.
\]

Only its homogeneous component of total degree 2j contributes.

**Binomial smoothing lemma.** Suppose V(x,y) is a symmetric homogeneous
polynomial of degree d with nonnegative real coefficients. If N>=0,
N+d=2j, and N+2>=d^2, then
\(\mathcal L_j((x+y)^N V)\ge0\).

Proof. Decompose V into nonnegative multiples of symmetric monomial pairs
\(x^a y^{d-a}+x^{d-a}y^a\), allowing half a pair when a=d-a. Put k=j-a.
The hypotheses imply N>=d except for d=0 (where this is also true), so
0<=k<=N. The functional on this pair is

\[
2\binom Nk-\binom N{k-1}-\binom N{k+1}
=\binom Nk\frac{N+2-(N-2k)^2}{(k+1)(N-k+1)}.
\]

Since |N-2k|=|2a-d|<=d, the numerator is nonnegative.
Here binomial coefficients outside [0,N] are zero. This also covers
N=d=0. For d=1, parity forces N odd and hence N>=1.

**Uniform band lemma.** Let B(x,y) and R(x,y) be symmetric formal power
series with nonnegative real coefficients. Suppose R has constant term 0
and degree-one part x+y. For integers j,k>=0 with h=2j-k>=0, if

\[
 j\ge 2k^2+k-1,
\]

then \(\mathcal L_j(B R^h)\ge0\).

Proof. Put L=x+y and S=R-L, which is symmetric, nonnegative and has no
terms below degree 2. Expand
\(BR^h=\sum_{r=0}^h\binom hr L^{h-r}BS^r\).
In the term indexed by r, only the homogeneous component of BS^r of
degree d=2j-(h-r)=k+r matters. It vanishes unless d>=2r, hence r<=k
and d<=2k. For every remaining term, N=h-r=2j-d and

\[
 N+2-d^2=2j+2-d(d+1)\ge 2j+2-2k(2k+1)\ge0.
\]

Apply the smoothing lemma term by term. The reasoning involves only
finitely many homogeneous components even for formal infinite series.

**Application to the frozen K.** Take m=j+1,
\(P_m(x)=\prod_{i=1}^m(1+x^i)\), \(R=P_m(x)P_m(y)-1\), and

\[
 B=A(x)A(y)(1+2x^s+2y^s+(xy)^s),\quad A=a_{s,t_0}.
\]

All hypotheses hold. The pass-1 identity gives
\(c_{s,j,h}=\Delta^h F_{s,j}(t_0)=\mathcal L_j(BR^h)\).
Consequently, for every j>=0 and every actual stage, the highest Newton
orders with deficit k=2j-h satisfying j>=2k^2+k-1 are nonnegative.
The conclusion holds for arbitrary A with nonnegative coefficients; it
does not need the special exponent profile. It leaves low and middle h
uncontrolled and does not settle K or any of the interior-index gap.

There are two sharper explicit rows. With \(C_j=\binom{2j}j/(j+1)\),
A(0)=1, and a_1=[x]A, one has

\[
 c_{s,j,2j}=C_j,
\]
\[
 c_{s,j,2j-1}=(a_1+2\mathbf1_{s=1})C_j
 +(2j-1)(C_j-C_{j-1})\quad(j\ge1).
\]

Indeed, the degree-two part of R is
\(x^2+xy+y^2=(x+y)^2-xy\); the degree-one part of B is
\((a_1+2\mathbf1_{s=1})(x+y)\). Evaluating the two relevant homogeneous
terms gives these formulas. They are nonnegative for every stated j.
The independent verifier checks the formulas against all 4,289 applicable
rows in the certificate through j=64.

The remaining signs cannot follow from coefficient positivity alone.
Take A=1, s=3, j=2, m=3. The same construction has
\(\mathcal L_2(BR)=-3\) and \(\mathcal L_2(BR^2)=-1\).
This A is not an actual recurrence stage. These exact counterexamples
refute only a generic positivity argument without the actual A hypotheses.
They do not refute K, H, or the original denominator conjecture.
