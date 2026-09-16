# Precise problem: `SDS(9,8,1,C_3^2)`

Provenance: `win-00086-p05-triage-6a25ad865982`  
Frozen statement: `source.md` (SHA-256
`d75270377823488dfaa65912e4a0a2bd57b396960d1b0ebb4865216db77bfb7f`)

## Objects and quantifiers

Let (G=(\mathbb F_3^2,+)), with identity (0). In the integral group ring
write

\[
 D=\sum_{x\in G}a_x[x],\qquad a_x\in\{0,1,-1\}.
\]

The support is (\operatorname{supp}(D)=\{x:a_x\ne0\}). The question is
whether there exists a coefficient function (a:G\to\{0,1,-1\}) such that

1. (|\operatorname{supp}(D)|=8), and
2. (DD^{(-1)}=7[0]+\sum_{x\in G}[x]), where
   (D^{(-1)}=\sum_xa_x[-x]).

Equivalently, with periodic autocorrelation

\[
C_D(t)=\sum_{x\in G}a_xa_{x-t},
\]

the quantified requirements are (C_D(0)=8) and
(C_D(t)=1) for every (t\in G\setminus\{0\}). Thus existence means one
assignment satisfying all eight nonzero-shift equations; nonexistence means
that every one of the (9\cdot2^8=2304) choices of the unique zero and the
eight signs fails at least one equation.

## Exact normalizations

Translation of all indices, multiplication of every coefficient by (-1),
and an automorphism in (GL(2,3)) preserve the defining identity. The
principal character gives

\[
\left(\sum_x a_x\right)^2=(8-1)+1\cdot9=16.
\]

Consequently, after a global sign change there are exactly six positive and
two negative coefficients. Translation puts the unique zero at (0). Hence
every candidate then has the form

\[
D=\sum_{x\ne0}[x]-2([a]+[b])
\]

for distinct (a,b\in G\setminus\{0\}). Such an unordered pair is of exactly
one of two types: (b=-a), or (a,b) are linearly independent. These are the
two (GL(2,3))-orbits (of sizes 4 and 24, respectively).

## Nearest prior result and proposed delta

He--Wu, arXiv:2608.22936v1, Lemma 2.1, proves the necessary character
equation (|\chi(D)|^2=k-\lambda=7) for every nonprincipal character. Their
Theorem 4.4 supplies a near-full-support congruence, but here it permits
(9-1+1(3-1)=10\equiv3-1\pmod 8), so it does not decide this case. The frozen
official data snapshot labels the exact group-specific entry open.

The proposed delta is nonexistence for this one entry. A short candidate
route is already visible. Put (\omega^2+\omega+1=0) and
(\chi_u(x)=\omega^{u\cdot x}). Since
(\sum_{x\ne0}\chi_u(x)=-1),

\[
\chi_u(D)=-1-2(\chi_u(a)+\chi_u(b)).
\]

If (b=-a), choose nonzero (u) with (u\cdot a=0); then
(|\chi_u(D)|^2=|-5|^2=25\ne7). If (a,b) are independent, choose the unique
dual vector (u) with (u\cdot a=u\cdot b=1); then
(|\chi_u(D)|^2=|-1-4\omega|^2=13\ne7). This is a complete-looking proof
candidate, not a triage certification. Its scope and every normalization must
be checked in a fresh mathematical review.

## Scope

Only (G=C_3^2), support size 8, and (lambda=1) are in scope. Other groups
of order 9, other parameters, numerical character approximations, and a
database status label do not decide this claim.
