# Adversarial rebuttal of the proposed \(r\in(3.233,3.234)\) candidate

Date: 2026-08-29  
Conclusion: **the proposed point is not critical for the cube-section volume,
and its correct spherical tangent Hessian is indefinite.**  The displayed
polynomial

\[
 p(r)=r^6-21r^4+48r^3-48r^2+32
\]

is exactly the critical polynomial obtained after omitting the four active
three-small-coordinate subsets from the box-spline sum.

An exact executable reconstruction is in
`src/builder_check_rebuttal.py`.

## 1. Rebuild the active subsets from the original formula

Write the sum-normalized proposed vector as

\[
 a=(x,y,y,y,y),\qquad
 x={2r\over r+4},\quad y={2\over r+4},\quad \sum_i a_i=2.
\]

Thus the half-sum threshold is \(T=1\).  Throughout

\[
 I=\left[{3233\over1000},{1617\over500}\right]
  =[3.233,3.234]
\]

we have \(2<r<4\).  The active subsets \(S\), meaning
\(1-\sum_{i\in S}a_i>0\), are exactly:

* the empty subset;
* all five singletons;
* the six pairs of small coordinates;
* the four triples of small coordinates.

The last class is decisive:

\[
 1-3y=1-{6\over r+4}={r-2\over r+4}>0.
\tag{1.1}
\]

High-small pairs are inactive because
\(1-x-y=(2-r)/(r+4)<0\), and the four-small subset is inactive because
\(1-4y=(r-4)/(r+4)<0\).

Therefore the exact fourth-degree numerator in the truncated-power formula is

\[
\begin{aligned}
 P_{\rm true}
 &=1-(1-x)^4-4(1-y)^4+6(1-2y)^4-4(1-3y)^4\\
 &=-{2\bigl(r^4-16r^3+96r^2-256r+64\bigr)\over(r+4)^4}.
\end{aligned}
\tag{1.2}
\]

Equivalently, before sum-normalization, at \((r,1,1,1,1)\) it is

\[
 \widetilde P_{\rm true}
 =-{r^4-16r^3+96r^2-256r+64\over8}.
\tag{1.3}
\]

The section volume is scale invariant, so either normalization gives

\[
 F(r)=-{\sqrt{r^2+4}\,
 (r^4-16r^3+96r^2-256r+64)\over192r}.
\tag{1.4}
\]

Differentiation gives

\[
 F'(r)=-{h(r)\over48r^2\sqrt{r^2+4}},
\qquad
 h(r)=r^6-12r^5+51r^4-96r^3+96r^2-64.
\tag{1.5}
\]

The standard Sturm chain of \(h\) has zero roots on \([2,4]\), and
\(h(2)=48>0\).  Hence \(h(r)>0\) on \(I\), so \(F'(r)<0\) there.
In particular, the unique root of \(p\) in \(I\) is not a critical point.

For a direct full-gradient check at the unnormalized vector
\(b=(r,1,1,1,1)\), set \(S=r^2+4\).  Exact differentiation of the
five-variable formula gives

\[
 \partial_1F(b)=-{h(r)\over48r^2\sqrt S},\qquad
 \partial_jF(b)={h(r)\over192r\sqrt S}\quad(2\le j\le5).
\tag{1.6}
\]

Euler's identity \(r\partial_1F+\sum_{j=2}^5\partial_jF=0\) holds, but the
gradient is nonzero.  Scaling to the stated sum-normalized vector multiplies
the gradient by the nonzero factor \((r+4)/2\), so cannot restore
criticality.

## 2. Exact location of the erroneous polynomial \(p\)

If the four active three-small subsets are accidentally omitted, the wrong
numerator becomes

\[
\begin{aligned}
 P_{\rm omit}
 &=1-(1-x)^4-4(1-y)^4+6(1-2y)^4\\
 &={2(r^4-48r^2+192r-32)\over(r+4)^4}.
\end{aligned}
\tag{2.1}
\]

The corresponding wrong scale-invariant objective is

\[
 F_{\rm omit}(r)
 ={\sqrt{r^2+4}(r^4-48r^2+192r-32)\over192r},
\]

and now

\[
 \boxed{F_{\rm omit}'(r)
 ={p(r)\over48r^2\sqrt{r^2+4}}.}
\tag{2.2}
\]

Thus \(p\) is not merely inconsistent with the correct calculation: it
pinpoints the missing terms.  Those terms carry a minus sign because their
cardinality is three.  In complement-paired notation they are the negative
contributions paired with the four high-small pairs.

For additional diagnosis, the wrong Hessian is indeed positive definite at
the isolated root of \(p\).  Its small-block and block-contrast eigenvalues
are

\[
 {\sqrt{r^2+4}\over192r}
 (r^6-19r^4+96r^3-272r^2+576r-544)
\]

and

\[
 {\sqrt{r^2+4}\over192r^3}
 (5r^8-47r^6+96r^5-216r^4+192r^3-32r^2-256),
\]

respectively.  Both parenthesized polynomials have zero Sturm roots on \(I\)
and are positive at \(3233/1000\).  Hence both advertised features of the
proposed candidate—its polynomial and positive Hessian—are internally
consistent with the same omission, but not with the cube-section formula.

## 3. Correct tangent Hessian at the proposed algebraic point

Although noncriticality already rules out a local extremum, the correct
Hessian also contradicts the claim of positive definiteness.  The stabilizer
\(S_4\) splits the four-dimensional tangent space at the unit normalization
of \((r,1,1,1,1)\) into:

* the three-dimensional subspace of small-coordinate differences;
* the block-contrast line spanned by \((4,-r,-r,-r,-r)\).

Since \(F\) is homogeneous of degree zero, \(a\cdot\nabla F=0\), and the
spherical Hessian is the restriction of the ambient Hessian even at this
noncritical point.  Its two eigenvalues are

\[
\begin{aligned}
 \lambda_{\rm small}
 &=-{\sqrt{r^2+4}\over192r}\,A(r)
 &&\text{(multiplicity 3)},\\
 \lambda_{\rm block}
 &=-{\sqrt{r^2+4}\over192r^3}\,B(r),
\end{aligned}
\tag{3.1}
\]

where

\[
\begin{aligned}
 A(r)&=r^6-16r^5+101r^4-336r^3+736r^2-1280r+1088,\\
 B(r)&=5r^8-48r^7+169r^6-336r^5+504r^4-384r^3
       +64r^2+512.
\end{aligned}
\tag{3.2}
\]

Exact Sturm counts give no zero of either \(A\) or \(B\) in \(I\).  At the
left rational endpoint,

\[
 A(3233/1000)=
 -{186652210824644674431\over10^{18}}<0,
\]

whereas

\[
 B(3233/1000)=
 {8892209130475653778370241\over2\cdot10^{23}}>0.
\]

Consequently

\[
 \lambda_{\rm small}>0>\lambda_{\rm block}
\]

at the unique root of \(p\) in \(I\).  The correct tangent Hessian is
indefinite.

## 4. Exact isolation and reproducibility

The executable checker verifies, using rational arithmetic and Sturm root
counts, all of the following:

1. every one of the 32 subset signs on \(I\), failing closed if a sign is not
   constant;
2. equations (1.2)--(1.6) and (2.1)--(2.2);
3. exactly one real root of \(p\) in \(I\);
4. no root of \(h,A,B\) in \(I\), with the stated signs;
5. the two exact Hessian eigenvalue formulas (3.1).

Run:

```bash
python src/builder_check_rebuttal.py
```

Expected output:

```text
rebuttal exact checks: PASS
```

No floating-point arithmetic or proof assistant is used by the checker.
