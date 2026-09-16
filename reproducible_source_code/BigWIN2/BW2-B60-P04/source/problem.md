# Precise reading of win-00060-p04

## Frozen source and interpretation

The immutable statement is `source.md`.  The reading used here follows Definitions 3.1--3.3 and Theorem 3.7 of Jeronimo--Lanciano, arXiv:2609.03828v1.  The coefficient field has characteristic zero.  “Generic dense” means that every monomial permitted by the degree data has its own algebraically independent, derivation-constant coefficient.  Equivalently, the conclusion is required on a nonempty Zariski-open subset of the corresponding affine coefficient space.  This interpretation does **not** treat the model coefficients themselves as time-varying differential indeterminates.

Put
\[
 R=\mathbb Q[a_{11},a_{12},a_{21},a_{22},b_1,b_2,c_1,c_2,p_1,p_2,q],
 \qquad F=\operatorname{Frac}(R),
\]
with zero derivation on $F$.  Write
\[
 A=\begin{pmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{pmatrix},\quad
 b=\binom{b_1}{b_2},\quad c=\binom{c_1}{c_2},\quad
 p^T=(p_1,p_2).
\]
The degree data in the source then give precisely the generic affine-linear system
\[
 x'=Ax+bu+c,\qquad y=p^Tx+q,                         \tag{1}
\]
where $x=(x_1,x_2)^T$, $u$ is one differential indeterminate, and $y$ is the output.  Thus each $f_i$ has dense support \(\{1,x_1,x_2,u\}\), while $g$ has dense support \(\{1,x_1,x_2\}\).  The exact degree equalities are
\[
 [D_x,D_u,D]=[1,1,1],\qquad[d_x,d_u,d]=[1,0,1].
\]

As in the cited paper, $\nu$ is the least nonnegative integer for which \(y,y',\ldots,y^{(\nu)}\) are algebraically dependent over \(\operatorname{Frac}(F\{u\})\) modulo (1).  The eliminant is the primitive irreducible defining polynomial of the Zariski closure of the input-output image, unique up to a scalar.  We remove that scalar ambiguity by making it monic in $y''$.

## Exact target statement

Let
\[
 \tau=\operatorname{tr}(A),\qquad \delta=\det(A),\qquad
 \Omega=\det\!\begin{pmatrix}p^T\\p^TA\end{pmatrix}.
\]
Define
\[
 P=\Omega\,\tau\,\delta\,(p^Tb)\bigl(p^T(\tau I-A)b\bigr)
   \bigl(p^T(\tau I-A)c-\delta q\bigr),
 \qquad \mathcal U=\{P\ne0\}.
\]
The polynomial $P$ is to be verified nonzero, so $\mathcal U$ is a nonempty Zariski-open subset of coefficient space.  The quantifier “generic” below means every coefficient tuple in $\mathcal U$ over any algebraically closed characteristic-zero extension field.  Equivalently, one may prove the universal statements over $F$.  Prove all of the following:

1. The generic order is \(\nu=2\).  In particular, the observability minor $\Omega$ is not the zero polynomial, so $y,y'$ remain algebraically independent after eliminating $x$, whereas $y,y',y''$ satisfy one irreducible relation.

2. With coefficient indeterminates fixed by the derivation, the monic eliminant is
   \[
   \boxed{
   E=y''-\tau y'+\delta y
     +p^T(\tau I-A)b\,u-p^Tb\,u'
     +p^T(\tau I-A)c-\delta q.}                    \tag{2}
   \]
   It must be shown that (2), rather than merely a finite-field specialization, is the primitive irreducible defining equation specified by Definition 3.3.

3. Each of the six displayed coefficient polynomials attached to
   \[
   1,\ u,\ u',\ y,\ y',\ y''
   \]
   is generically nonzero.  Consequently the exact generic support is
   \[
   \operatorname{supp}(E)=\{1,u,u',y,y',y''\}.       \tag{3}
   \]

For comparison, write a candidate monomial as
\[
 u^{\ell_0}(u')^{\ell_1}(u'')^{\ell_2}
 y^{e_0}(y')^{e_1}(y'')^{e_2}.
\]
Here \(\Delta=\Delta_x=1\), \(D_u=1\), and Theorem 3.7 specializes to
\[
\begin{aligned}
 \ell_0+\ell_1+\ell_2+e_0+e_1+e_2&\le1,\\
 e_0+e_1+e_2&\le1,\\
 \ell_0+\ell_1+\ell_2+e_1+2e_2&\le3,\\
 \ell_1+e_1+2e_2&\le3,\\
 \ell_2+e_2&\le1.
\end{aligned}
\]
Its nonnegative integer points are exactly the seven monomials
\[
 \{1,u,u',u'',y,y',y''\}.
\]
Thus the requested missing monomial is $u''$, and the additional exact support constraint to prove is
\[
 \boxed{\ell_2=0\quad\text{for every monomial of }E}
 \qquad\text{equivalently}\qquad \deg_{u''}E=0.      \tag{4}
\]
Equations (2)--(4), including the generic nonvanishing needed for equality rather than containment, are the precise scope.  No statement is made here for nonlinear systems, more state/input variables, sparse coefficient patterns, positive characteristic, or time-varying model coefficients.

## Prior-result and status triage

- Primary source inspected 2026-09-07: G. Jeronimo and L. Lanciano, *New bounds for the support of input-output equations in differential-algebraic systems*, [arXiv:2609.03828v1](https://arxiv.org/abs/2609.03828).  Definitions 3.1--3.3 define the eliminant; Theorem 3.7 gives the support inequalities; §4.1's Algorithm 1 gives the evaluation-interpolation reconstruction; the first differential-parameter row of §4.2 reports $7\to6$; §5 says sharper differential-parameter support descriptions remain open.  The frozen locator's “Algorithm 4.1” is read as the algorithm in §4.1; this label mismatch does not affect the mathematical target.  The local PDF hash matches the source locator: `411966bc69ecd16606dc726047355d145a5a34c83a3404ae45b80aab71809a00`.
- Nearest prior support-bound paper inspected at abstract/metadata level 2026-09-07: Y. Mukhina and G. Pogudin, *Support bound for differential elimination in polynomial dynamical systems*, [arXiv:2506.08824v2](https://arxiv.org/abs/2506.08824).  It concerns unknown symbolic parameters (constant parameters), not freely differentiating inputs.
- Earlier neighboring result inspected at abstract/metadata level 2026-09-07: Y. Mukhina and G. Pogudin, *Projecting dynamical systems via a support bound*, [arXiv:2501.13680v4](https://arxiv.org/abs/2501.13680), for projection to a coordinate in the non-input setting.

A targeted exact-phrase/degree-pattern search located the reported $7\to6$ row only in the primary source.  This is not a priority or novelty proof.  At triage, the source claim is `status-uncertain`: formula (2) is a short preliminary symbolic reduction using Cayley--Hamilton, but it has not yet passed an independent mathematical audit or a full-text literature comparison.

## Proposed contribution and verifier

Nearest prior result X: Theorem 3.7 supplies the seven-point candidate support and §4.2 supplies stable finite-field evidence.  Proposed delta Y: prove the coefficient-generic formula (2), exact support equality (3), and structural constraint (4).  Verification route Z: differentiate (1) twice, reduce $A^2$ by Cayley--Hamilton, verify the identity over $R[x,u,u']$, prove \(\Omega\ne0\) and irreducibility/order two, and exhibit coefficient specializations showing every claimed coefficient polynomial is nonzero.
