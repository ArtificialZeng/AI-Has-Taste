# Research pass 1: a differential-operator proof

Job: `win-00045-p02-research-b314c402433a`  
Date: 2026-09-06

## Exact operator identity

Let $f=L_a(P_2)=\sum_{k=0}^n b_kx^k$.  After harmless independent
rescaling, a degree-one input whose transformed zero is in $[-1,0]$ has
the form $P_1=e_1+r$, where $0\le r\le1$.  The supplied product formula
specialized to $m=1$ gives

\[
 e_1e_k=\frac{a+k}{a}e_{k+1}+\frac{k}{a}e_k.
\]

Consequently

\[
\boxed{\quad L_a((e_1+r)P_2)
 =(x+r)f(x)+\frac{x(x+1)}a f'(x).\quad}                 \tag{1}
\]

This identity is valid for every degree $n$.

## Root-location lemma

**Lemma.** Fix $a>0$ and $0\le r\le1$.  If all roots of a nonzero real
polynomial $f$ lie in $[-1,0]$, then every root of

\[
T_rf=(x+r)f+\frac{x(x+1)}a f'
\]

also lies in $[-1,0]$.

**Proof.** First suppose that $f$ is monic of degree $n$, its roots are
distinct and strictly inside the interval, and $0<r<1$.  Write

\[
 f(x)=\prod_{i=1}^n(x+s_i),\qquad 0<s_1<\cdots<s_n<1.
\]

Away from the roots of $f$, polynomial division gives

\[
\begin{aligned}
H(x):=\frac{T_rf(x)}{f(x)}
 &=x+r+\frac{x(x+1)}a\sum_{i=1}^n\frac1{x+s_i}\\
 &=\left(1+\frac na\right)x+r+\frac{n-\sum_i s_i}{a}
   -\sum_{i=1}^n\frac{s_i(1-s_i)}{a(x+s_i)}.             \tag{2}
\end{aligned}
\]

Therefore, on every interval separated by its poles,

\[
 H'(x)=1+\frac na+
 \sum_{i=1}^n\frac{s_i(1-s_i)}{a(x+s_i)^2}>0.            \tag{3}
\]

Every pole has negative residue.  Also
$T_rf(-s_i)=-s_i(1-s_i)f'(-s_i)/a\ne0$, so no root of the polynomial
is hidden at a pole.  Thus $H$ tends to $+\infty$ from
the left of a pole and to $-\infty$ from its right.  Together with
$H(x)\to-\infty$ as $x\to-\infty$ and
$H(x)\to+\infty$ as $x\to+\infty$, strict monotonicity puts exactly
one zero in every one of the $n+1$ pole-separated intervals.  The two
outer zeros are still inside the desired interval because

\[
 H(-1)=r-1<0,\qquad H(0)=r>0.                            \tag{4}
\]

Hence all $n+1$ zeros of $T_rf$ are distinct and lie in $(-1,0)$.

Multiplying $f$ by a nonzero real scalar only multiplies $T_rf$ by that
scalar, so monicity causes no loss.  For arbitrary $r\in[0,1]$, repeated
roots, and roots at the endpoints,
choose $r_m\in(0,1)$ and pairwise distinct $s_{i,m}\in(0,1)$ converging
to the given parameters, and put $f_m=\prod_i(x+s_{i,m})$.  The resulting
polynomials $T_{r_m}f_m$ converge
coefficientwise to $T_rf$, and their common degree is $n+1$, with fixed
positive leading coefficient $1+n/a$.  After division by that leading
coefficient, order their $n+1$ roots.  Compactness of $[-1,0]^{n+1}$
and continuity of the elementary symmetric functions show that the limit
polynomial factors into $n+1$ roots in $[-1,0]$.  This proves the lemma.

## Consequence for the frozen claim

Apply the lemma with $n=2$ and
$f(x)=(x+s)(x+t)$, where $s,t\in[0,1]$.  Identity (1) expands to the
cubic in `source.md`, so every one of its roots lies in $[-1,0]$ for all
$a>0$ and $r,s,t\in[0,1]$.  Thus the frozen universally quantified
claim is proved.

The same argument establishes the stronger degree-$(1,n)$ statement for
every finite $n\ge0$.  That strengthening is an internal mathematical
consequence of the displayed proof; no novelty or priority claim is made.

## Adversarial boundary checks

- At $r=0$, formula (1) has the exact factorization
  $T_0f=x[f+(x+1)f'/a]$, exposing the permitted root at $0$.
- At $r=1$, it has the exact factorization
  $T_1f=(x+1)[f+xf'/a]$, exposing the permitted root at $-1$.
- For the maximally collided endpoint families,
  $T_r(x^n)=x^n[(1+n/a)x+r+n/a]$ and
  $T_r((x+1)^n)=(x+1)^n[(1+n/a)x+r]$; their remaining roots are
  respectively $-(ar+n)/(a+n)$ and $-ar/(a+n)$, both in $[-1,0]$.
- No compactness in $a$ is used: equations (2)--(3) have the required signs
  separately for every $a>0$, including arbitrarily small or large values.

## Gap audit

- Operator identity: exact and independently machine-checked in
  `evidence/research_check.py`.
- Generic root count: accounts for all $n+1$ roots because the leading
  coefficient is $1+n/a>0$.
- Boundary/repeated-root cases: covered by a degree-preserving compact limit.
- Dependence on computation: none; the script checks algebra only.
- Known gaps: none found in this pass.
