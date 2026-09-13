# Exact exclusion of active grade six

## Claim

Let \(A\) be a real diagonal positive-definite matrix and apply exact-arithmetic
restarted conjugate gradients with restart length four.  If the initial residual
has at most six active distinct eigenvalues, then the iteration either terminates
or both normalized residual parities converge.  In particular, no counterexample
in the frozen problem can have dimension at most six, so the currently certified
range sharpens to

\[
                    7\leq n_{\min}(4)\leq 8.
\]

The same argument works after orthogonal spectral reduction for a general real
symmetric positive-definite matrix.  The statement above stays within the
diagonal scope of `source.md`.

## Imported degree-independent facts

The proof uses Proposition 1.4 and equations (G.7)--(G.10) of Colbrook,
Stepaniants, and Townsend, *A Complete Resolution of Forsythe's Conjecture for
Restarted Conjugate Gradients*, arXiv:2609.04659v1.  In the notation used below,
for every nonterminating orbit they give:

1. The monic degree-four residual polynomials \(P_k\), their squared norms
   \(H_k>0\), and the products \(q_k=P_kP_{k+1}\) satisfy
   \(H_k\uparrow h>0\), \(P_{2j}\to P_e\), \(P_{2j+1}\to P_o\), and
   \(q_k\to q_\infty=P_eP_o\) coefficientwise.
2. The same-parity signed recurrence is
   \[
   y_{k+2,i}=\frac{q_k(\lambda_i)}{\sqrt{H_kH_{k+1}}}\,y_{k,i},
   \]
   and \(\lVert y_{k+2}-y_k\rVert\to0\).
3. Every omega-limit state is fixed by the signed two-block map, has at least
   five active nodes, and is supported on nodes satisfying
   \(q_\infty(\lambda_i)=h\).

These facts are proved in the cited source for arbitrary restart length.  No
minimum-dimension conclusion is imported from it.

## Six-node algebra

Assume first that six distinct nodes
\(0<\lambda_1<\cdots<\lambda_6\) remain active.  Put

\[
 \Delta(t)=\prod_{i=1}^6(t-\lambda_i),\qquad
 D_i=\Delta'(\lambda_i),\qquad w_{k,i}=y_{k,i}^2.
\]

The vector \((w_{k,i}P_k(\lambda_i))_i\) annihilates
\(1,t,t^2,t^3\).  The nullspace of this four-by-six Vandermonde matrix consists
of vectors
\((c_0+c_1\lambda_i)/D_i\).  Since

\[
 \langle P_k,t^4\rangle_{w_k}=H_k,
 \quad \sum_i\frac{\lambda_i^j}{D_i}=0\ (0\le j\le4),
 \quad \sum_i\frac{\lambda_i^5}{D_i}=1,
\]

its linear coefficient is \(c_1=H_k\).  Thus there is a unique real \(a_k\)
such that

\[
  w_{k,i}P_k(\lambda_i)
       =H_k\frac{\lambda_i-a_k}{D_i}.                 \tag{1}
\]

The weight update immediately becomes

\[
  w_{k+1,i}=\frac{(\lambda_i-a_k)P_k(\lambda_i)}{D_i}. \tag{2}
\]

If all six next weights are positive, the monic quintic
\((t-a_k)P_k(t)\) has alternating signs at the six nodes.  Hence it has exactly
one simple root in each gap \((\lambda_i,\lambda_{i+1})\).  Its four \(P_k\)-roots
occupy four gaps and \(a_k\) occupies the remaining one.

Apply (1) at two consecutive times.  The following polynomial identity holds
for a monic cubic \(B_k\):

\[
 (t-a_k)P_kP_{k+1}-H_{k+1}(t-a_{k+1})=\Delta B_k.      \tag{3}
\]

Divide \(B_k=(t-a_k)L_k+u_k\), where \(L_k\) is monic quadratic.  With

\[
 K_a(t)=\frac{\Delta(t)-\Delta(a)}{t-a},
\]

evaluation and cancellation in (3) give the exact drift and product formulas

\[
 a_{k+1}-a_k=\frac{\Delta(a_k)}{H_{k+1}}u_k,           \tag{4}
\]
\[
 P_kP_{k+1}=H_{k+1}+\Delta L_k+u_kK_{a_k}.             \tag{5}
\]

The general energy identity also specializes to the useful exact equality

\[
 H_{k+1}-H_k=\frac{u_k^2}{H_{k+1}}
       \sum_i w_{k,i}K_{a_k}(\lambda_i)^2.             \tag{6}
\]

## Sign transport

Suppose a full-support omega-limit point exists.  Then
\(q_\infty(\lambda_i)=h\) at all six nodes, and therefore

\[
             P_eP_o=h+\Delta L                              \tag{7}
\]

for a monic quadratic \(L\).  At a full-support limit, (1)--(2) show that the
same parameter \(a\) occurs in the two phases.  It lies in one node gap
\(I=(\lambda_g,\lambda_{g+1})\); both \(P_e\) and \(P_o\) have one root in each
of the other four gaps and no root in the closed interval
\(\bar I=[\lambda_g,\lambda_{g+1}]\).  Factor convergence and the interlacing
observation after (2) consequently imply \(a_k\in I\) for every sufficiently
large \(k\).

It remains to show that the defect \(u_k\) cannot keep changing sign.  For a
monic quartic \(P\) sufficiently close to \(P_e\) or \(P_o\), there is a unique
monic quadratic \(J_P\) for which the remainder of \(J_P\Delta\) modulo \(P\)
has degree at most one.  Indeed, this is a two-by-two linear system.  At either
limiting factor, \(J_P=L\) by (7).  Its homogeneous system has only the zero
solution: if \(d,e\in\mathbb P_1\), \(P\mid d\Delta-e\), then multiplication
by \(L\) and (7) gives \(P\mid eL+hd\); the latter has degree at most three, so
\(eL+hd=0\), which forces \(d=e=0\).  The system is therefore nonsingular at
the limits and \(J_P\) depends continuously on \(P\) nearby.

Define a linear functional

\[
 \mathcal L_P(f)=[t^3]\operatorname{rem}_P(J_Pf).
\]

It annihilates \(P\mathbb P_3\), constants, and
\(\Delta\mathbb P_1\).  Subtract (5) at times \(k+1\) and \(k\), use
\(P_{k+1}(P_{k+2}-P_k)\in P_{k+1}\mathbb P_3\), and apply
\(\mathcal L_{P_{k+1}}\).  This yields the exact transport identity

\[
 u_{k+1}\mathcal L_{P_{k+1}}(K_{a_{k+1}})
   =u_k\mathcal L_{P_{k+1}}(K_{a_k}).                  \tag{8}
\]

At a limiting factor \(P\), let \(Q\) be the opposite factor.  The four roots
\(z\) of \(P\) are simple, and Lagrange interpolation plus (7) gives, for every
\(a\in\bar I\),

\[
\begin{aligned}
 \mathcal L_P(K_a)
 &=\sum_{P(z)=0}\frac{L(z)}{P'(z)}
       \frac{\Delta(z)-\Delta(a)}{z-a}\\
 &=\frac{h+\Delta(a)L(a)}{P(a)}=Q(a).                 \tag{9}
\end{aligned}
\]

Neither limiting factor vanishes on \(\bar I\).  Equations (8)--(9), continuity,
and compactness therefore show that, for all sufficiently large \(k\), the two
functional values in (8) are nonzero and have the same sign.  Hence either the
defects thereafter vanish or \(u_{k+1}/u_k>0\).  Thus \(u_k\) has an eventual
fixed sign.  Since \(\Delta\) has a fixed sign on \(I\), (4) makes \(a_k\)
eventually monotone.  It is bounded in \(I\), so \(a_k\to a_\infty\).
Equation (2) and parity factor convergence now prove convergence of both parity
weight vectors.

## Boundary and signed cases

If no full-support omega-limit point exists, every omega-limit support has
exactly five nodes.  On any fixed five-node support, the Vandermonde annihilator
is one-dimensional: if \(D_i^S\) is the derivative of that support polynomial,
then \(w_iP(\lambda_i)=h/D_i^S\).  Thus the fixed limiting factor determines at
most one weight vector.  There are only six such supports.  The omega-limit set
of either parity is connected because its step size tends to zero; being a
finite set, it is a singleton.  Thus the parity weights converge in this case
as well.

If a coordinate is annihilated at a finite block, the active grade falls.  Grade
at most four terminates, while the same one-dimensional annihilator calculation
at grade five gives \(w_iP(\lambda_i)=H/D_i^S\), hence
\(w_i'=P(\lambda_i)/D_i^S\).  At the next block this implies
\(P(\lambda_i)P'(\lambda_i)=H'\) on every active node.  The energy identity then
gives \(H'=H\), so the signed two-block multiplier is exactly one:
\(y_{k+2}=y_k\).
Repeated eigenvalues and initially inactive coordinates reduce to these
active-grade cases.

Finally, once parity weights converge, every coordinate of positive limiting
weight has two-block signed multiplier tending to
\(q_\infty(\lambda_i)/h=1\), so its sign is eventually constant.  Coordinates
of zero limiting weight vanish in magnitude.  Hence the signed normalized even
and odd residual directions converge, completing the exclusion.

## Reproducible algebra check and gap list

`evidence/verify_grade6_identities.py` uses only Python's standard library and
exact rational arithmetic.  On nodes \(1,2,4,7,11,16\) and initial weights
\((2,3,5,7,11,13)/41\), it recomputes five blocks and verifies four instances of
(1), (3)--(6), three instances of (8), and four instances of the limiting
functional identity (9).  Its output is:

```
PASS: 5 blocks; 4 division/drift/energy checks; 3 exact sign-transport checks; 4 limiting-functional checks
nodes=1,2,4,7,11,16; initial_weights=2,3,5,7,11,13 / 41
largest polynomial-coefficient numerator+denominator bit length: 180723
```

This finite check is regression evidence only; the argument above is the proof.
Known mathematical gaps in the stated grade-six theorem: none identified in
this research pass.  The original problem remains open because active grade
seven is untreated.  The literature comparison is the focused primary-source
screen recorded in `problem.md`; it supports audit of this partial result but is
not a priority claim.
