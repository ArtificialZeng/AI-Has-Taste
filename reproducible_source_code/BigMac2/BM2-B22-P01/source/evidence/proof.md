# Exact resolution of the frozen horizon-two FGM claim

## Theorem

With the notation fixed in `source.md` and `problem.md`, for every integer
\(d\geq 1\), \(L>0\), and \(R\geq0\),

\[
 W_2(L,R,d)=c_2^2L^2R^2,
 \qquad
 c_2=\frac1{3+\beta},\qquad
 \beta=\frac{\sqrt5-1}{1+\sqrt{7+2\sqrt5}}.
\]

The lower bound is the projection-envelope construction frozen in the source.
The missing upper bound follows from the exact dimension-free PEP certificate
below.

## Normalized interpolation PEP

It is enough first to take \(L=R=1\), translate \(x_*=0\), and normalize
\(f_*=0\).  Put

\[
 a:=1+\beta,\qquad c:=\frac1{a+2}=c_2.
\]

Differentiable optimality gives \(g_*:=\nabla f(x_*)=0\), and the two FGM
updates reduce exactly to

\[
 x_1=x_0-g_0,\qquad x_2=x_0-g_0-a g_1.
\]

For \(i,j\in I:=\{*,0,1,2\}\), \(i\ne j\), define

\[
 h_{ij}:=f_i-f_j-\langle g_j,x_i-x_j\rangle
                 -\frac12\lVert g_i-g_j\rVert^2.
\]

Every convex differentiable 1-smooth function satisfies \(h_{ij}\geq0\).
For completeness, apply the descent lemma to
\(z\mapsto f(z)-\langle g_j,z\rangle\), whose global minimizer is \(x_j\),
at the unit gradient step from \(x_i\).  This gives precisely the displayed
inequality.

Let \(\Gamma\succeq0\) be the Gram matrix of the ordered family
\((x_0,g_0,g_1,g_2)\).  In its coordinate space set

\[
\begin{array}{c|rrrr|rrrr}
i&\multicolumn{4}{c|}{X_i}&\multicolumn{4}{c}{G_i}\\ \hline
*&0&0&0&0&0&0&0&0\\
0&1&0&0&0&0&1&0&0\\
1&1&-1&0&0&0&0&1&0\\
2&1&-1&-a&0&0&0&0&1
\end{array}
\]

and \(\operatorname{sym}(u,v)=(uv^\mathsf T+vu^\mathsf T)/2\).  Thus the
Gram coefficient in \(h_{ij}\) is

\[
 H_{ij}=-\operatorname{sym}(G_j,X_i-X_j)
        -\tfrac12\operatorname{sym}(G_i-G_j,G_i-G_j).
\]

For \(\tau:=\min_k\lVert g_k\rVert^2\), also put

\[
 r=1-\lVert x_0\rVert^2\geq0,
 \qquad p_k=\lVert g_k\rVert^2-\tau\geq0.
\]

## Exact dual certificate

All omitted interpolation multipliers are zero; in particular
\(\lambda_{0*}=\lambda_{1*}=0\).  The ten nonzero multipliers are

\[
\begin{array}{c|c@{\qquad}c|c}
ij&\lambda_{ij}&ij&\lambda_{ij}\\ \hline
01&\dfrac{399a^2-201a+2}{500(a+2)}
&02&\dfrac{996-456a-227a^2}{500(a+2)}\\[5pt]
10&\dfrac{172a^2-485a+342}{500(a+2)}
&12&\dfrac{227a+229}{500}\\[5pt]
20&\dfrac2{25}&21&\dfrac{153}{250}\\[5pt]
*0&\dfrac{144-53a}{125(a+2)}
&*1&\dfrac{93}{500}\\[5pt]
*2&\dfrac{119}{500}&2*&\dfrac2{a+2}.
\end{array}
\]

The performance multipliers are

\[
 (\mu_0,\mu_1,\mu_2)=
 \left(\frac1{1000},\frac1{1000},\frac{499}{500}\right),
 \qquad \sum_k\mu_k=1,
\]

and the radius multiplier is \(\rho=c^2\).  Direct exact expansion gives
function-value flow conservation and the slack

\[
 S=\rho E_{00}-\sum_{k=0}^2\mu_kE_{k+1,k+1}
                 -\sum_{i\ne j}\lambda_{ij}H_{ij}
\]

equal to the following symmetric matrix:

\[
\scriptsize
S=\begin{pmatrix}
\dfrac1{(a+2)^2}&\dfrac{53a-144}{250(a+2)}&-\dfrac{93}{1000}&-\dfrac{119}{1000}\\[5pt]
\dfrac{53a-144}{250(a+2)}&\dfrac{46-17a}{40(a+2)}&\dfrac{-106a^2+249a-78}{500(a+2)}&\dfrac{79}{1000}\\[5pt]
-\dfrac{93}{1000}&\dfrac{-106a^2+249a-78}{500(a+2)}&\dfrac{186a^2-829a+1598}{1000(a+2)}&\dfrac{119a^2+703a-1070}{1000(a+2)}\\[5pt]
-\dfrac{119}{1000}&\dfrac{79}{1000}&\dfrac{119a^2+703a-1070}{1000(a+2)}&\dfrac{694-153a}{500(a+2)}
\end{pmatrix}.
\]

Here “direct exact expansion” includes all twelve ordered interpolation
inequalities, including the two with zero multipliers.  The accompanying
`verify_exact_dual.py` constructs those twelve matrices from their definition
and checks every function-value and Gram coefficient symbolically.

## Exact sign and PSD audit

The radical \(a\) obeys

\[
 a^4-8a^3+10a^2-a-1=0,
 \qquad \frac{1281}{1000}<a<\frac{641}{500}.
\]

The enclosure uses only rational square comparisons:

\[
 \frac{559}{250}<\sqrt5<\frac{2237}{1000},\qquad
 \frac{3387}{1000}<\sqrt{7+2\sqrt5}<\frac{847}{250}.
\]

They imply \(281/1000<\beta<282/1000\).  On this interval all displayed
\(\lambda_{ij}\) and all \(\mu_k\) are positive.  The closest numerator is
that of \(\lambda_{10}\); it is decreasing throughout the interval and at the
upper endpoint equals

\[
 172(641/500)^2-485(641/500)+342=\frac{91129}{31250}>0.
\]

For the other nonconstant numerators, monotonic endpoint bounds give

\[
 996-456(641/500)-227(641/500)^2=\frac{9582013}{250000}>0,
 \qquad
 144-53(641/500)=\frac{38027}{500}>0,
\]

while \(399a^2-201a+2>0\) is immediate from \(a>1\).

To prove \(S\succeq0\), first note the exact identity

\[
 S(1,c,c,c)^\mathsf T=0.
\]

Let \(B=S[1{:}4,1{:}4]\).  Its three leading principal minors are

\[
 \Delta_1=\frac{46-17a}{40(a+2)},
 \quad
 \Delta_2=\frac{R_2(a)}{10^6(a+2)^2},
 \quad
 \Delta_3=\frac{R_3(a)}{2\cdot10^8(a+2)^2},
\]

where reduction by the displayed minimal polynomial gives

\[
\begin{aligned}
R_2(a)&=-227450a^3+701517a^2-1522068a+1768420,\\
R_3(a)&=4682448a^3+24778142a^2-115934851a+124473901.
\end{aligned}
\]

Writing \(\ell=1281/1000\), \(u=641/500\), outward rational bounds give

\[
\begin{aligned}
R_2(a)&>-227450u^3+701517\ell^2-1522068u+1768420
       =\frac{2445271097527}{5000000}>0,\\
R_3(a)&>4682448\ell^3+24778142\ell^2-115934851u+124473901
       =\frac{205845508080081}{7812500}>0.
\end{aligned}
\]

Also \(\Delta_1>0\), so Sylvester's criterion gives \(B\succ0\).  If
\({\bf1}=(1,1,1)^\mathsf T\), the kernel identity implies, for every scalar
\(u\) and vector \(z\in\mathbb R^3\),

\[
 (u,z)^\mathsf T S(u,z)=(z-cu{\bf1})^\mathsf T B(z-cu{\bf1})\geq0.
\]

Hence \(S\succeq0\) exactly (indeed it has rank three).

## Upper bound and matching lower bound

Cancellation of the \(f_i\), \(\Gamma\), and \(\tau\) coefficients now yields
the exact identity

\[
 c^2-\tau
 =c^2r+\sum_{k=0}^2\mu_kp_k
       +\sum_{i\ne j}\lambda_{ij}h_{ij}
       +\langle S,\Gamma\rangle.
\]

Every term on the right is nonnegative: in particular
\(\langle S,\Gamma\rangle\geq0\) for two PSD matrices.  Therefore
\(\min_k\lVert g_k\rVert^2=\tau\leq c^2\), uniformly in the dimension.

For equality, choose a unit vector \(e\), \(K=[0,ce]\),

\[
 f(x)=\max_{g\in K}\{\langle x,g\rangle-\tfrac12\lVert g\rVert^2\},
 \qquad x_*=0,\qquad x_0=e.
\]

Then \(\nabla f=\operatorname{Proj}_K\), so \(f\) is convex and 1-smooth.
Since \(c<1/2\),

\[
 x_1=(1-c)e,\qquad
 x_2=x_1-ac e=(1-(a+1)c)e=ce,
\]

and all three queried gradients equal \(ce\).  This proves equality for
\(L=R=1\) in every \(d\geq1\).

For \(R>0\), translating and applying
\(f_{L,R}(x)=LR^2f((x-x_*)/R)\) proves the stated formula.  If \(R=0\), then
\(x_0=x_*\), all queried gradients vanish, and both sides are zero.  This
completes every quantifier of the frozen claim.

## Reproduction

Run:

```text
python evidence/verify_exact_dual.py
```

The script uses exact SymPy expressions and rational comparisons.  It checks
the radical polynomial/enclosure, all twelve interpolation matrices, multiplier
flow, the complete slack identity, the kernel, the three exact PSD minors, and
the lower-witness recurrence.  The earlier `full_dual_search.py` is explicitly
floating-point discovery code and is not needed for certification.
