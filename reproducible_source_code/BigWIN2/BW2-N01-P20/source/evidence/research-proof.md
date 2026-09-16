# Uniform central-window expansion: proof submitted for review

Proposer job: `newwin-00001-p20-research-f42a5d965fef`, 2026-09-12.
This is a research proof dossier, not an accepted audit or a manuscript.
The original definitions and quantifiers are those of `source.md` and
`problem.md`. No changed target is used.

## Statement

For real x, put x_+=max(x,0) and
\[
H(x)=\frac{\sqrt\pi}{2}e^{x^2}\operatorname{erfc}(|x|)
     =e^{x^2}\int_{|x|}^{\infty}e^{-t^2}\,dt,
\]
where erfc(u)=(2/sqrt(pi)) integral from u to infinity of exp(-t^2) dt.
Define, on all real x and -1<delta<=0,
\[
F_0(x)=H(x)+2x_+,\qquad
F_1(x,\delta)=(2\delta+1)xH(x)+\delta+1-2x_+^2. \tag{1}
\]
For every A>0 there are constants C_A<infinity and an integer M_A such
that, for every integer m>=M_A and every real |x|<=A, the frozen index
k=m+floor(x sqrt(m)) is admissible and
\[
\left|E_{m,k}-\sqrt m F_0(x)-F_1(x,\delta_m(x))\right|
\le C_A m^{-1/2},\qquad
\delta_m(x)=\lfloor x\sqrt m\rfloor-x\sqrt m. \tag{2}
\]
The proof below gives one explicit, nonoptimized choice of both constants.
It includes x=0, all floor jumps, and m-dependent real x.

## 1. Exact reductions

Let h=m^{-1/2}, d=k-m, and, for admissible indices, set
\[
p_{m,j}=2^{-(2m-1)}\binom{2m-1}{m+j},\quad
q_{m,j}=4^{-m}\binom{2m}{m+j}.
\]
Let S_{m,d} be the CDF of Bin(2m-1,1/2) at m+d, with the usual zero
and one extensions outside its support. Factorials give
\[
p_{m,j}=(1-j/m)q_{m,j},\quad q_{m,j}=q_{m,-j},\quad
p_{m,j}=p_{m,-j-1}. \tag{3}
\]
The odd center has no atom at its midpoint, so S_{m,-1}=1/2 and
\[
S_{m,d}=\begin{cases}
\tfrac12+\sum_{j=0}^{d}p_{m,j},&d\ge0,\\
\tfrac12-\sum_{j=d+1}^{-1}p_{m,j},&d\le-1.
\end{cases} \tag{4}
\]
Reflection of the binomial variable also gives S_{m,-d-2}=1-S_{m,d}.
Consequently the exact definition in the source becomes
\[
E_{m,m+d}=\begin{cases}
S_{m,d}/p_{m,d},&d<0,\\
(1-S_{m,d})/p_{m,d}+2m(d+1)/(m+d+1),&d\ge0.
\end{cases} \tag{5}
\]
Indeed, the upper-branch partial sum stops at m-d-2, and
binom(2m,m+d+1)/binom(2m-1,m+d)=2m/(m+d+1).
All these identities hold before taking any limit.

## 2. Uniform local mass estimate, with constants

Fix B>=1 and define
\[
K=\frac14+\frac{5B^2}{6}+\frac{B^4}{3},\quad
M=\left\lceil\max\{4,4B^2,K\}\right\rceil,\quad
L=\frac32 eK. \tag{6}
\]
Here and below e is the base of the natural logarithm. Assume m>=M and
|j|<=B sqrt(m), and write t=jh and f(t)=exp(-t^2)/sqrt(pi).
We shall prove
\[
p_{m,j}=h f(t)(1-th+\rho_{m,j}),\qquad
|\rho_{m,j}|\le Lh^2,\qquad
\frac{p_{m,j}}{h f(t)}\ge\frac1{2e}. \tag{7}
\]

First obtain the central bound without an asymptotic theorem. Put
I_n=integral from 0 to pi/2 of sin(t)^n dt. Integration by parts gives
I_n=(n-1)I_{n-2}/n for n>=2, with I_0=pi/2 and I_1=1. Thus
\[
I_{2m}=\frac\pi2q_{m,0},\qquad
I_{2m+1}=\frac1{(2m+1)q_{m,0}},\qquad
I_{2m-1}=\frac1{2m q_{m,0}}.
\]
Since 0<=sin(t)<=1, I_{2m+1}<=I_{2m}<=I_{2m-1}. Hence
\[
\frac1{\sqrt{\pi(m+1/2)}}\le q_{m,0}\le\frac1{\sqrt{\pi m}},
\qquad
\left|\log\frac{q_{m,0}}{h f(0)}\right|\le\frac1{4m}. \tag{8}
\]
The last inequality uses log(1+v)<=v for v>=0.

For r=|j|<=m/2, factorial cancellation gives
\[
R_{m,r}=\frac{q_{m,r}}{q_{m,0}}
=\prod_{\ell=1}^r\frac{1-(\ell-1)/m}{1+\ell/m}.
\]
For |u|<=1/2 the logarithmic power series yields
\[
|\log(1+u)-u+u^2/2|
\le\sum_{s=3}^{\infty}|u|^s/s\le\tfrac23|u|^3.
\]
Applying this separately to the numerator and denominator factors gives
\[
\left|\log R_{m,r}+\frac{r^2}{m}-\frac{r^2}{2m^2}\right|
\le\frac{r^2(r^2+1)}{3m^3}. \tag{9}
\]
The sums used here are sum(2ell-1)=r^2,
sum(ell^2-(ell-1)^2)=r^2, and
sum((ell-1)^3+ell^3)=r^2(r^2+1)/2, over ell=1,...,r.
Since r<=B sqrt(m), the absolute value of log(R_{m,r})+r^2/m
is at most (5B^2/6+B^4/3)/m. Together with (8), this shows
\[
q_{m,j}=h f(t)e^{\xi_{m,j}},\qquad |\xi_{m,j}|\le Kh^2\le1.
\]
Now |exp(xi)-1|<=e|xi|, and |th|=|j|/m<=1/2.
Equation (3) gives (7), with
rho=(1-th)(exp(xi)-1). The same representation gives its positive
lower bound. This proves the local estimate with uniform inequalities.

## 3. Signed quadrature and the CDF remainder

For any C^2 function g on [-B,B], put y=dh and define
\[
\mathcal T_d(g)=\begin{cases}
h\sum_{j=0}^{d}g(jh),&d\ge0,\\
-h\sum_{j=d+1}^{-1}g(jh),&d\le-1.
\end{cases}
\]
The composite trapezoidal estimate, with orientation retained, is
\[
\left|\mathcal T_d(g)-\int_0^y g(t)\,dt
-\frac h2(g(0)+g(y))\right|
\le\frac{|y|h^2}{12}\sup_{|t|\le B}|g''(t)|. \tag{10}
\]
For d>=1 this follows by adding the endpoint half-weights to the
ordinary trapezoidal sum; for d<=-1, negate the trapezoidal sum on
[dh,0] and then add the same endpoint half-weights. For d=0 it is
exact. On each mesh interval the integrated linear-interpolation
error is at most sup|g''| times h^3/12, proving the stated bound.
In particular, the empty sum at d=-1 is covered by the same formula.

Let c=1/sqrt(pi), g(t)=t f(t), and define
\[
D=c\left[(B+1)L+\frac{B(2+4B^2)}{12}
                    +\frac B2+\frac{B(6B+4B^3)}{12}\right]. \tag{11}
\]
For |d|<=B sqrt(m), substitute (7) into (4). There are at most
B/h+1 terms, each local error having absolute value at most cLh^3.
Therefore
\[
S_{m,d}=\tfrac12+\mathcal T_d(f)-h\mathcal T_d(g)+\eta,
\qquad |\eta|\le c(B+1)Lh^2.
\]
We have |f''|<=c(2+4B^2), |g(y)|<=cB, g(0)=0, and
|g''|<=c(6B+4B^3) on [-B,B]. Apply (10) to f and to g. The
endpoint correction in h T_d(g) costs at most cBh^2/2, and its
quadrature remainder costs at most cB(6B+4B^3)h^3/12, bounded
by the corresponding h^2 term in (11). Since f'=-2tf,
\[
\frac h2(f(0)+f(y))-h\int_0^y t f(t)\,dt=hf(y).
\]
It follows that
\[
S_{m,d}=P(y)+hf(y)+\varepsilon_{m,d},\qquad
|\varepsilon_{m,d}|\le Dh^2,\qquad
P(y)=\frac12+\int_0^y f(t)\,dt. \tag{12}
\]
The elementary Gaussian integral gives P(y)=erfc(-y)/2 and
0<=P(y)<=1. Thus no remote binomial tail estimate is a dependency.

## 4. Division by the local mass and the two exact branches

Define the following constants, all depending only on B:
\[
a=ce^{-B^2},\qquad J=2e(B^2+3L/2),\qquad
Q=\frac{J+2eD}{a}+B+J,\qquad
T=4B+2+2(B+1)^3. \tag{13}
\]
Let z=p_{m,d}/(hf(y))=1-yh+rho. By (7), z>=1/(2e), and
\[
z^{-1}=1+yh+\theta,\qquad
\theta=\frac{y^2h^2-\rho(1+yh)}{z},\qquad
|\theta|\le Jh^2. \tag{14}
\]
Using f(y)>=a and 0<=P(y)<=1 in (12)--(14) gives
\[
\left|\frac{S_{m,d}}{p_{m,d}}
-\left(\frac{P(y)}{hf(y)}+\frac{yP(y)}{f(y)}+1\right)\right|
\le Qh. \tag{15}
\]
For clarity, the errors are bounded respectively by
(J/a)h from P theta/(hf), Bh+Jh^2 from z^{-1}-1,
and (2eD/a)h from epsilon/(hf z). This accounts for all errors.
The same calculation, replacing P by 1-P and +hf by -hf, gives
\[
\left|\frac{1-S_{m,d}}{p_{m,d}}
-\left(\frac{1-P(y)}{hf(y)}+\frac{y(1-P(y))}{f(y)}-1\right)\right|
\le Qh. \tag{16}
\]
For y>=0, put v=y+h. The rational term in (5) has the exact expansion
\[
\frac{2m(d+1)}{m+d+1}
=\frac{2v}{h(1+hv)}
=\frac{2y}{h}+2-2y^2
  -4yh-2h^2+\frac{2h(y+h)^3}{1+h(y+h)}.
\]
Its last three terms have absolute value at most Th, since h<=1,
0<=y<=B, and the denominator is at least one.

For y<0, P(y)/f(y)=H(y); for y>=0, (1-P(y))/f(y)=H(y).
Combine (5), (15), (16), and the rational estimate. With
\[
V(y)=yH(y)+1-2y_+^2,
\]
both branches satisfy the single inequality
\[
\left|E_{m,m+d}-h^{-1}F_0(y)-V(y)\right|\le(Q+T)h
\quad (|d|\le B\sqrt m). \tag{17}
\]
This bound applies at d=0 through the upper branch and at d=-1 through
the lower branch. No continuity between discrete expectation values
has been assumed.

## 5. Floor correction and the uniform constants

Let b=sqrt(pi)/2. The representation
\[
H(x)=\int_0^\infty e^{-u^2-2|x|u}\,du
\]
shows 0<H(x)<=b. For x<0, H'=2xH+1, and for x>0,
H'=2xH-1. Although H has a corner at zero, F_0=H+2x_+ is C^2:
\[
F_0'(x)=2xH(x)+1\quad\hbox{for all real }x,\qquad
F_0''(0)=2b.
\]
For x!=0, F_0''=2H+2xH', which tends to 2b at zero.
On [-B,B], its absolute value is at most
\[
U=(2+4B^2)b+2B.
\]
Also V is C^1, with V'(0)=b and, away from zero,
V'=H+xH'-4x_+. Thus on [-B,B],
\[
|V'|\le W=(1+2B^2)b+5B. \tag{18}
\]

Given the original A>0, take B=A+1 and M_A=M from (6).
For m>=M_A, |x|<=A, d=floor(x/h), delta=d-x/h and y=dh,
we have -1<delta<=0, y=x+delta h, and |y|<=B. Moreover
|d|<=B sqrt(m)<=m/2, so 0<=m+d<=2m-1 (m>=4).
All previous estimates are therefore applicable. Taylor's theorem
and (18), on the interval joining x and y in [-B,B], give
\[
|h^{-1}F_0(y)-h^{-1}F_0(x)-\delta F_0'(x)|\le Uh/2,
\qquad |V(y)-V(x)|\le Wh.
\]
Since V(x)+delta F_0'(x) is exactly F_1(x,delta) in (1), (17)
proves (2) with the explicit choice
\[
C_A=Q+T+U/2+W,\qquad B=A+1, \tag{19}
\]
and the other constants as in (6), (11), (13), and (18).
They are finite for every fixed A; no uniformity for growing A is asserted.
All bounds hold for every allowed x separately with these same constants,
so arbitrary floor-cell endpoints and x varying with m are included.
This completes the argument for the full frozen statement.

## Checks, dependencies, and remaining review questions

At x=0, (1) gives F_0(0)=sqrt(pi)/2 and F_1(0,0)=1. Directly,
E_{m,m-1}=2^(2m-1)/binom(2m,m), and
E_{m,m}-E_{m,m-1}=(m-1)/(m+1). The two lattice cells therefore
need different constant terms; delta in (1) supplies them. More generally
F_1(x,0)-lim_{delta down to -1} F_1(x,delta)=F_0'(x).
Here the limit is from within (-1,0]; it describes the left side of a
floor jump. The endpoint delta=-1 is only a continuous extension of (1).

Dependencies: the frozen finite binomial formula; factorial algebra;
integration by parts; the convergent logarithm series on |u|<=1/2;
the trapezoidal interpolation bound proved above; the Gaussian integral;
and elementary differentiation and Taylor's theorem. No external
asymptotic theorem, numerical fit, or unproved uniformity lemma is used.
Known mathematical gaps in the submitted argument: none identified by
the proposer. A fresh referee still has to check correctness and scope.

Contribution is this explicit application to the bounded-capacity,
fixed-red-count central window, answering the precise problem frozen by
the user. The methods are classical. The bounded primary-literature
comparison and its limits are recorded separately; priority and the
value of a short publication are not certified by this proof.
