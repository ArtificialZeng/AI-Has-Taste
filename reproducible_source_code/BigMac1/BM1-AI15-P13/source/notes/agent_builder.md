# Builder notes: fixed-precision SM iterative refinement

Date: 2026-08-29 (Asia/Shanghai)

Role: proof builder, restarted from the definitions of Algorithms SM and
SM--IR in `sources/2510.01696_src/manuscript.tex`.  These notes deliberately
separate exact identities, IEEE certificates, conditional theorems, and open
gaps.  No numerical experiment is used as a proof.

## 1. Statement defect that matters

Write

\[
  B=A+uv^T.
\]

The source conjecture does not quantify the floating-point format, rounding
mode, exponent range, treatment of exceptional values, implementation of the
backward-stable `A`-solver, order of residual evaluation, stopping test, or
the constant hidden in "safely away" and "backward stable".  More seriously,
the two conditions

\[
  \kappa_2(A),\ \kappa_2(B)\ll \epsilon_M^{-1}
\]

control neither the scale ratio \(\|A\|_2/\|B\|_2\), the rank-one scalar
\(t=v^TA^{-1}u\), nor the computed Sherman--Morrison denominator
\(\widehat\beta=\operatorname{fl}(1+v^T\widehat z)\).  This is fatal, not
merely expository.

## 2. Exact IEEE counterexamples (already decisive for the broad conjecture)

### 2.1 Format and exact input

Use any radix-2 floating-point format of precision \(p\geq 2\), with enough
exponent range to contain \(2^p\), round-to-nearest with ties-to-even, and no
overflow/underflow in the operations below.  Its unit roundoff is
\(\epsilon_M=2^{-p}\).  Take the one-dimensional, exactly representable data

\[
  A=[1],\qquad u=[1],\qquad v=[2^p],\qquad b=[1].
\]

The mathematical updated coefficient is

\[
  B=A+uv^T=[2^p+1].
\]

It need not itself be stored as one floating-point number because the paper's
algorithm represents it by \(A,u,v\) and evaluates the residual in that
representation.  Both nonzero scalar matrices have exactly

\[
  \kappa_2(A)=\kappa_2(B)=1.
\]

Thus they satisfy every interpretation of being safely below
\(\epsilon_M^{-1}\) that includes condition number one.

### 2.2 The tie

In the binade starting at \(2^p\), adjacent floating-point numbers are
\(2^p\) and \(2^p+2\).  Therefore \(2^p+1\) is exactly halfway between them.
The low candidate \(2^p\) has even least significand bit, so

\[
  \operatorname{RN}_{\rm even}(2^p+1)=2^p.
\]

### 2.3 Initial SM solve

Every line below is exact except the displayed halfway rounding:

\[
\begin{aligned}
 \widehat y&=\operatorname{fl}(A\backslash b)=1,\\
 \widehat z&=\operatorname{fl}(A\backslash u)=1,\\
 \widehat\alpha&=\operatorname{fl}(v^T\widehat y)=2^p,\\
 \widehat\beta&=\operatorname{fl}
    (1+\operatorname{fl}(v^T\widehat z))
    =\operatorname{fl}(1+2^p)=2^p,\\
 \widehat\theta&=\operatorname{fl}
    (\widehat\alpha/\widehat\beta)=1,\\
 \widehat x_0&=\operatorname{fl}
    (\widehat y-\widehat\theta\widehat z)=0.
\end{aligned}
\]

The exact solution is \(x_*=1/(2^p+1)\), but the algorithm returns zero.

### 2.4 Every fixed-precision refinement step is stationary

Suppose \(\widehat x_k=0\).  Algorithm SM--IR computes, in its stated
separated form,

\[
 \widehat r_k=\operatorname{fl}
   (b-A\widehat x_k-(v^T\widehat x_k)u)=1.
\]

The correction solve has the same right-hand side as the initial solve, hence

\[
 \widehat y_{r,k}=1,\qquad
 \widehat\alpha_{r,k}=2^p,\qquad
 \widehat\theta_{r,k}=1,
\]

and its SM correction is exactly

\[
 \widehat y_{r,k}-\widehat\theta_{r,k}\widehat z=1-1=0.
\]

Whether the final line is associated as
\(\operatorname{fl}(\widehat x_k+
\operatorname{fl}(\widehat y_{r,k}-\widehat\theta_{r,k}\widehat z))\)
or as the paper's left-to-right expression, all intermediates are 0 or 1 and
the output is \(\widehat x_{k+1}=0\).  Induction gives

\[
  \widehat x_k=0\quad\hbox{for every }k\geq0.
\]

The normwise Rigal--Gaches backward error, and also the one-component
componentwise relative backward error, is exactly

\[
 \eta(\widehat x_k)
 =\frac{|b-B\widehat x_k|}{|B|\,|\widehat x_k|+|b|}=1.
\]

Across the family of precisions, \(\eta/\epsilon_M=2^p\) is unbounded.  Thus
this is not a hidden-constant \(O(\epsilon_M)\) result.  The broad conjecture
is disproved even in dimension one and even though the residual is computed
exactly at every iteration.  Higher residual precision alone cannot repair
this example: the correction solver itself is the zero map on this right-hand
side.

For IEEE binary64 specifically, set \(p=53\), so \(v=2^{53}\) and
\(\epsilon_M=2^{-53}\).  All required numbers and operations are far from
the exponent limits.

### 2.5 Nondegenerate 2-by-2 lift with both condition numbers far below the
### reciprocal unit roundoff

If dimension one is thought too degenerate, the same obstruction persists in
dimension two while both condition numbers are of order only
\(\epsilon_M^{-1/2}\).  For \(p\geq4\), put

\[
 m=\lfloor p/2\rfloor,\qquad s=2^m,
\]

and take the exactly representable data

\[
 A=\begin{bmatrix}1&0\\0&s\end{bmatrix},\qquad
 u=b=\begin{bmatrix}1\\0\end{bmatrix},\qquad
 v=\begin{bmatrix}2^p\\0\end{bmatrix}.
\]

Then the update has rank exactly one and

\[
 B=A+uv^T=
 \begin{bmatrix}2^p+1&0\\0&s\end{bmatrix}.
\]

Since these are positive diagonal matrices,

\[
 \kappa_2(A)=2^m,
 \qquad
 \kappa_2(B)=\frac{2^p+1}{2^m}
             =2^{p-m}+2^{-m}.
\]

Thus

\[
 \epsilon_M\kappa_2(A)=2^{m-p},\qquad
 \epsilon_M\kappa_2(B)=2^{-m}+2^{-p-m},
\]

both of which tend to zero exponentially like \(2^{-p/2}\).  This is a
literal, quantitative meaning of "safely away" from
\(\epsilon_M^{-1}=2^p\).

All vectors generated by SM--IR lie in the first coordinate.  The diagonal
\(A\)-solves are exact there, and the scalar trace from Sections 2.3--2.4
applies coordinate for coordinate.  Hence

\[
 \widehat x_k=(0,0)^T,\qquad \eta(\widehat x_k)=1
 \quad\hbox{for every }k\geq0.
\]

For binary64, \(p=53\), \(m=26\), and

\[
 \kappa_2(A)=2^{26},\qquad
 \kappa_2(B)=2^{27}+2^{-26},\qquad
 \epsilon_M^{-1}=2^{53}.
\]

The 2-by-2 lift is therefore the preferred release counterexample; the
one-dimensional family remains the shortest explanation of the rounding
mechanism.

## 3. Exact structural explanation: denominator error controls a rank-one mode

This subsection is an exact-arithmetic lemma about an idealized corrector.  It
explains the certificate and gives a sharp positive condition for that model.

Assume the solves with \(A\), all inner products involving the right-hand
side, and all vector operations are exact, but reuse a fixed nonzero scalar
\(\widehat\beta\) in place of

\[
 z=A^{-1}u,\qquad t=v^Tz,\qquad \beta=1+t.
\]

The correction operator is

\[
 M=A^{-1}-\frac{zv^TA^{-1}}{\widehat\beta}.
\]

Put \(d=\widehat\beta-\beta\).  Direct multiplication, without a norm
inequality, gives

\[
\begin{aligned}
 BM
 &=I+uv^TA^{-1}-\frac{(Bz)v^TA^{-1}}{\widehat\beta}\\
 &=I+\frac{d}{\widehat\beta}\,uv^TA^{-1},\\
 R:=I-BM
 &=-\frac{d}{\widehat\beta}\,uv^TA^{-1}.
\end{aligned}
\]

Hence \(R\) has rank at most one and its only possibly nonzero eigenvalue is

\[
 \lambda=-\frac{dt}{\widehat\beta}.
\]

With exact residual and update, refinement obeys

\[
 r_{k+1}=Rr_k,\qquad R^2=\lambda R.
\]

Consequently, after the first step,

\[
 r_{k+1}=\lambda^k r_1.
\]

Except for the exceptional initial subspace \(Rr_0=0\), convergence is
equivalent to \(|\lambda|<1\); divergence occurs for \(|\lambda|>1\), and
nonzero stagnation/oscillation can occur when \(|\lambda|=1\).

In the exact counterexample,

\[
 t=2^p,\quad \beta=2^p+1,\quad \widehat\beta=2^p,\quad d=-1,
 \quad \lambda=1,
\]

indeed \(M=0\) and \(R=I\).

This lemma also shows why mere relative accuracy of the denominator is not
enough.  If \(|d|\leq\sigma|\beta|\) with \(0\leq\sigma<1\), then

\[
 |\lambda|\leq\frac{\sigma|t|}{1-\sigma}.
\]

A sufficient contraction condition is

\[
 \sigma(1+|t|)<1.
\]

Thus a relative denominator error of order \(\epsilon_M\) must generally be
paired with a scale condition of the form
\(\epsilon_M|v^TA^{-1}u|<c<1\).  Neither condition number in the conjecture
implies this; in dimension one both condition numbers are identically one
while \(|t|\) is arbitrary.

There is also a useful dimension-\(n\geq2\) comparison.  Choose a unit vector
\(q\in\ker(v^T)\).  Since \(Aq=Bq\),

\[
 \frac{\|B\|_2}{\|A\|_2}\leq\kappa_2(B),\qquad
 \frac{\|A\|_2}{\|B\|_2}\leq\kappa_2(A).
\]

Moreover, \(\beta\) is the exceptional eigenvalue of
\(BA^{-1}=I+uv^TA^{-1}\), while \(\beta^{-1}\) is the exceptional eigenvalue
of its inverse.  Consequently

\[
 \frac1{\kappa_2(A)\kappa_2(B)}
 \leq |\beta|\leq
 \kappa_2(A)\kappa_2(B).
\]

The 2-by-2 certificate saturates the upper bound:
\(\beta=\kappa_2(A)\kappa_2(B)=2^p+1\).  Hence a product hypothesis such as
\(\epsilon_M\kappa_2(A)\kappa_2(B)\ll1\) would exclude this particular
large-\(t\) mechanism, whereas the two separate hypotheses
\(\epsilon_M\kappa_2(A)\ll1\) and
\(\epsilon_M\kappa_2(B)\ll1\) do not.  This product condition alone is not
claimed sufficient for the full algorithm: dot-product cancellation and
componentwise residual growth still require separate control.

## 4. General refinement identity: residual precision, corrector quality, and update precision are distinct

Let \(x_k\) be the stored iterate and define its *exact* residual

\[
 r_k=b-Bx_k.
\]

Represent one implemented step without hiding any source of error as

\[
 \widehat r_k=r_k+f_k,\qquad
 c_k=\widehat r_k-Bd_k,\qquad
 x_{k+1}=x_k+d_k+s_k.
\]

Here \(f_k\) is residual-evaluation error, \(c_k\) is the residual left by
the (possibly unstable) SM correction solver, and \(s_k\) is update-rounding
error.  Substitution gives the exact identity

\[
 \boxed{\ r_{k+1}=-f_k+c_k-Bs_k\ }.
\]

If a correction solver has the uniform residual contraction property

\[
  \|c_k\|_2\leq\rho\|\widehat r_k\|_2,
  \qquad 0\leq\rho<1,
\]

then

\[
 \boxed{
 \|r_{k+1}\|_2\leq
 \rho\|r_k\|_2+(1+\rho)\|f_k\|_2
       +\|B\|_2\|s_k\|_2. }
\]

This is the clean recurrence sought in the prompt.  It is a theorem from the
definitions and makes clear that:

1. `fixed precision` controls the forcing terms \(f_k,s_k\), not the
   contraction factor by itself;
2. the same unstable SM solver can be reused only if it has an actual
   contraction factor \(\rho<1\) on correction right-hand sides;
3. condition numbers alone do not imply that property, as Section 2 shows.

For example, suppose for a fixed solution-scale \(D>0\) one has the verified
uniform bounds

\[
 \|f_k\|_2\leq C_r\epsilon_M D,
 \qquad
 \|B\|_2\|s_k\|_2\leq C_a\epsilon_M D.
\]

Then \(\zeta_k=\|r_k\|_2/D\) satisfies

\[
 \zeta_{k+1}\leq \rho\zeta_k+C\epsilon_M,
 \qquad C=(1+\rho)C_r+C_a,
\]

and therefore

\[
 \zeta_k\leq \rho^k\zeta_0+
 \frac{C}{1-\rho}\epsilon_M.
\]

To turn this into the usual backward error, take

\[
 D_*=\|B\|_2\|x_*\|_2+\|b\|_2,
 \qquad x_*=B^{-1}b.
\]

Since \(x_k-x_*=-B^{-1}r_k\),

\[
 \|B\|_2\|x_k\|_2+\|b\|_2
 \geq D_*-\kappa_2(B)\|r_k\|_2.
\]

Thus whenever \(\kappa_2(B)\zeta_k\leq1/2\), the backward error satisfies

\[
 \eta(x_k)
 =\frac{\|r_k\|_2}
 {\|B\|_2\|x_k\|_2+\|b\|_2}
 \leq 2\zeta_k.
\]

In particular, contraction to \(O(\epsilon_M D_*)\), together with
\(\epsilon_M\kappa_2(B)\ll1\), gives normwise backward stability.  This is a
conditional positive theorem, not a proof of the original conjecture.

## 5. One sufficient condition for a reusable *linear* approximate A-solver

The following idealized result isolates another missing scale condition.  Let
the reusable solve operator be exactly

\[
 H=(A+E)^{-1}

\]

for one fixed perturbation \(E\), and perform the Sherman--Morrison formula
around \(H\) exactly.  The resulting correction operator is, by the exact
Sherman--Morrison identity,

\[
 M=H-\frac{Hu\,v^TH}{1+v^THu}=(B+E)^{-1},

\]

provided the displayed inverses exist.  Therefore

\[
 I-BM=E(B+E)^{-1}.

\]

If

\[
 \vartheta=\|B^{-1}\|_2\|E\|_2<1,

\]

then the Neumann bound gives

\[
 \|I-BM\|_2
 \leq\frac{\vartheta}{1-\vartheta}.

\]

This is a contraction when \(\vartheta<1/2\).  A backward-stable factorization
model \(\|E\|_2\leq C_S\epsilon_M\|A\|_2\) would require

\[
 C_S\epsilon_M\|A\|_2\|B^{-1}\|_2
 =C_S\epsilon_M\frac{\|A\|_2}{\|B\|_2}\kappa_2(B)<\frac12.

\]

Again, \(\kappa_2(A)\) and \(\kappa_2(B)\) do not control the scale ratio
\(\|A\|_2/\|B\|_2\).  Actual rounded triangular solves also have
right-hand-side-dependent errors, and the SM scalar/vector operations add
further perturbations, so this lemma must not be presented as a theorem for
the full implementation.  Its value is to identify a sufficient parameter
that any full proof must replace or control.

## 6. Same-precision residual bounds require a representation-growth factor

If the residual were evaluated as one matrix-vector product with a stored
\(B\), the usual normwise model has a floor comparable to
\(\epsilon_M(\|b\|+\||B|\,|x_k|\|)\).  Algorithm SM--IR instead evaluates

\[
 b-Ax_k-(v^Tx_k)u.

\]

Its first-order absolute error naturally involves

\[
 |b|+\bigl(|A|+|u||v|^T\bigr)|x_k|,

\]

as the source paper itself derives.  Normwise conversion introduces a growth
ratio such as

\[
 \chi=
 \frac{\|\,|A|+|u||v|^T\,\|_2}{\|B\|_2},

\]

which is also not bounded by \(\kappa_2(A)\) and \(\kappa_2(B)\).  Thus even
after repairing the correction-solver contraction, a clean same-precision
theorem needs either a bound on this representation growth, a componentwise
hypothesis matching the chosen backward error, or a more accurate residual.

## 7. Maximal conclusions of this Builder branch

### Exact result

The broad condition-number-only conjecture is false under standard IEEE-like
fixed precision.  Section 2 is an exact, all-iteration, dimension-one
counterexample; no limiting argument or numerical evidence is involved.

### Conditional positive result

The exact recurrence in Section 4 proves eventual backward stability if all
of the following are independently verified:

1. the SM correction residual contracts uniformly, \(\rho<1\);
2. residual and update rounding contribute \(O(\epsilon_M)\) at the solution
   scale;
3. \(\epsilon_M\kappa_2(B)\) is small enough that the stored iterate's
   backward-error denominator remains comparable with the exact-solution
   scale;
4. no overflow, underflow, NaN, or zero computed SM denominator occurs.

Useful sufficient controls include a denominator condition involving
\(\epsilon_M|v^TA^{-1}u|\), a fixed-factor perturbation condition involving
\(\epsilon_M\|A\|_2\|B^{-1}\|_2\), and a residual representation-growth
bound involving \(\chi\).  None follows from the two proposed condition
numbers alone.

## 8. Gap ledger for any stronger positive endpoint

- **Fatal for original conjecture:** Section 2.  No repair is possible without
  changing the hypotheses or algorithm.
- **Major:** a real QR/LU solve is not exactly one fixed linear map \(H\) once
  rounded substitutions are included.  Any positive theorem must bound the
  per-right-hand-side correction residual directly or account for these
  nonlinear errors.
- **Major:** an \(O(\epsilon_M)\) fixed-precision residual floor relative to
  the *desired* backward-error denominator requires componentwise growth
  control; two spectral condition numbers do not provide it.
- **Local:** exact treatment of gradual underflow and signed zeros is
  unnecessary for the certificate because all nonzero values used there are
  normal and far from exponent limits.
- **Local:** a release certificate should implement an independent exact
  radix-2 rounding verifier from serialized \(p,A,u,v,b\), rather than trust
  host binary64 evaluation.

## 9. Proof-assistant disclosure

No proof assistant was used in this Builder branch.  The certificate and
identities are elementary exact arithmetic; an independent finite-format
verifier is still appropriate for the project release.
