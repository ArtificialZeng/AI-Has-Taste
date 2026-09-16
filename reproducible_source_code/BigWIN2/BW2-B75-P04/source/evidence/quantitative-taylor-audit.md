# Quantitative endpoint classification for condition (3.38)

Provenance: `win-00075-p04-research-1d4946398a68`.  Audit date:
2026-09-09.

## Scope and source locator

This note concerns only the sufficient hypothesis (3.38) in Corollary 3.5 of
Li--Li--Pan--Wulan--Zhou, arXiv:2609.04833v1.  In the official HTML v1,
Corollary 3.5 and (3.38) occur at lines 969--977; Theorem 3.4 and its phrase
"only depending on alpha" at lines 1003--1009; and (3.41)--(3.42) and the
intermediate-value step at lines 1012--1038.  The arXiv record still listed
only v1 on 2026-09-09.  Searches for the identifier/title together with
`correction`, `erratum`, and the displayed threshold found no independent
correction; that dated negative search is not a priority guarantee.

Put

\[
 A=\alpha+2\geq2,\qquad h=p-A>0,\qquad
 C_A=B\left(A-1,1+\frac A2\right).
\]

The exact left side of (3.38), with no estimate applied, is

\[
 L_{A,b}(h)=\frac{Ab+(b+1)h}{h^2}
 \left\{1-\frac1{2hB(A/(A+h),2h)}\right\}.                 \tag{1}
\]

For a fixed `b`, points arbitrarily close to `h=0` remain in the source
domain `0 <= b < A/(A+h)` exactly when `0 <= b < 1`.

## Quantitative expansion

Define

\[
 \Phi(h)=\log\Gamma(x)+\log\Gamma(1+2h)-\log\Gamma(x+2h),
 \qquad x=\frac A{A+h}.
\]

Then `2h B(x,2h)=exp(Phi(h))`, so (1) is

\[
 L_{A,b}(h)=\frac{Ab+(b+1)h}{h^2}(1-e^{-\Phi(h)}).          \tag{2}
\]

Here is an explicit Taylor bound.  Set

\[
 c_2=\frac{\pi^2}{3A},\qquad
 c_3=-\frac{\pi^2}{3A^2}+\zeta(3)\left(\frac2{A^2}-\frac4A\right),
\]

\[
 K_\Phi=\frac{\pi^2}{3A^3}+\frac{\zeta(3)}2+\frac{897}{28}.
\]

For every `0 < h <= 1/4`,

\[
 |\Phi(h)-c_2h^2-c_3h^3|\leq K_\Phi h^4.                  \tag{3}
\]

To prove (3), write `d=-h/(A+h)`, `u=2h`, and
`F(z)=log Gamma(1+z)`.  Since `|d| <= h/2`, `0 <= d+u <= 2h`, and
`u <= 1/2`, the absolutely convergent expansion

\[
 F(z)=-\gamma z+\sum_{n=2}^{\infty}\frac{(-1)^n\zeta(n)}n z^n
 \quad(|z|<1)
\]

may be used in `Phi=F(d)+F(u)-F(d+u)`.  Its quadratic term is exactly

\[
 -\zeta(2)du=\frac{\pi^2h^2}{3(A+h)}
 =\frac{\pi^2h^2}{3A}-\frac{\pi^2h^3}{3A^2}+R_2,
 \qquad |R_2|\leq\frac{\pi^2}{3A^3}h^4.
\]

Its cubic term is

\[
 \zeta(3)(d^2u+du^2)
 =\zeta(3)h^3\left(\frac2{(A+h)^2}-\frac4{A+h}\right).
\]

The derivative of `2/s^2-4/s` has absolute value at most `1/2` for
`s >= 2`, giving a cubic-term remainder at most `zeta(3)h^4/2`.
Finally, using `zeta(n)<2` for `n>=4`,

\[
\begin{split}
 |R_{\geq4}|
 &\leq\frac12\sum_{n=4}^{\infty}left[(h/2)^n+2(2h)^n\right]\\
 &\leq\left(\frac1{28}+32\right)h^4=\frac{897}{28}h^4,
\end{split}
\]

which proves (3).

For fully explicit control of (2), put

\[
 P=c_2+\frac{|c_3|}{4}+\frac{K_\Phi}{16},\qquad
 E=\frac12 e^{P/16}P^2,\qquad K_N=K_\Phi+E,
\]

and

\[
 D(A,b)=\frac{\pi^2}{3A}-2b\zeta(3)\left(2-\frac1A\right),             \tag{4}
\]

\[
 K_L(A,b)=AbK_N+(b+1)|c_3|+\frac{b+1}{4}K_N.                          \tag{5}
\]

The elementary estimate
`|1-exp(-y)-y| <= exp(|y|)y^2/2`, combined with (3), gives

\[
 \boxed{\left|L_{A,b}(h)-\frac{\pi^2b}{3}-D(A,b)h\right|
 \leq K_L(A,b)h^2}\qquad(0<h\leq1/4).                 \tag{6}
\]

This also supplies an inspectable quantitative remainder rather than only an
asymptotic `o(h)`.

## Exact local classification, including equality

Let

\[
 b_*(A)=\frac{3C_A}{\pi^2}.
\]

It lies in `(0,1)`: the beta-integral gives `C_A <= 1/2`, and
`pi^2 > 9`.  For `0 <= b < 1`, define the admissibility cap

\[
 \rho(A,b)=
 \begin{cases}
  1/4,&b=0,\\
  \min\{1/4,A(1-b)/(2b)\},&b>0.
 \end{cases}                                                     \tag{7}
\]

For `0<h<rho(A,b)`, both `b<A/(A+h)` and the small-`p` restriction of
Corollary 3.5 hold.  Put

\[
 J(A,b)=|D(A,b)|+K_L(A,b)/4.
\]

If `b != b_*(A)`, let

\[
 \varepsilon_{\ne}=
 \min\left\{\rho(A,b),
 \frac{|C_A-\pi^2b/3|}{2J(A,b)}\right\}.                         \tag{8}
\]

By (6), throughout `0<h<epsilon_ne`,

\[
 \begin{cases}
 L_{A,b}(h)<C_A,&0\leq b<b_*(A),\\
 L_{A,b}(h)>C_A,&b_*(A)<b<1.
 \end{cases}                                                     \tag{9}
\]

At equality, the constant terms alone do not decide the direction.  Formula
(4) gives

\[
 D(A,b_*)=\frac{\pi^2}{3A}
 -\frac{6C_A\zeta(3)}{\pi^2}\left(2-\frac1A\right)>0.            \tag{10}
\]

For completeness, (10) has an elementary global proof.  The beta integral
gives `C_A <= 1/(A-1)`.  Also `zeta(3)<5/4` by the integral test and
`pi^4>81`.  For `A>=2`,

\[
 18C_A\zeta(3)(2A-1)
 \leq\frac{45}{2}\frac{2A-1}{A-1}<81<\pi^4,
\]

which is precisely (10) after clearing positive factors.  Therefore, with

\[
 \varepsilon_{=}=\min\left\{\rho(A,b_*),
 \frac{D(A,b_*)}{2K_L(A,b_*)}\right\},                            \tag{11}
\]

equation (6) yields

\[
 L_{A,b_*}(h)-C_A>\frac12D(A,b_*)h>0
 \quad(0<h<\varepsilon_=).                                      \tag{12}
\]

Consequently the exact endpoint-neighborhood classification is

\[
 \boxed{\exists\varepsilon>0\ \forall h\in(0,\varepsilon):
 L_{A,b}(h)\leq C_A
 \quad\Longleftrightarrow\quad 0\leq b<\frac{3C_A}{\pi^2}.}     \tag{13}
\]

Thus equality belongs to the failing side.  Corollary 3.5 proves the norm
identity on a punctured endpoint neighborhood for every fixed `b<b_*(A)`;
for `b>=b_*(A)`, that corollary cannot do so because its own sufficient
hypothesis is false near the endpoint.  This is a sharp repair of the local
Corollary-3.5 route.  It is **not** a counterexample to the norm identity or
to Theorem 3.4, because (3.38) is sufficient and has not been shown necessary.

The accompanying `quantitative-taylor-audit.py` independently checks the
algebraic coefficients, the source Beta expression versus (2), and (6) on a
finite high-precision stress grid.  Those computations support error detection;
the inequalities above are the proof.
