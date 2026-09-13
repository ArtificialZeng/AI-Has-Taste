# Proof of the exact Lipschitz constant

## Theorem

For every \(L>0\), the canonical monotone transport \(T_L\) from the
standard Gaussian measure to
\[
 d\nu_L(t)=Z_L^{-1}e^{L|t|}\,d\gamma_1(t)
\]
satisfies
\[
 \operatorname{Lip}(T_L)=T_L'(0)=Z_L
 =2e^{L^2/2}\Phi(L).
\]
Its continuous derivative attains its maximum only at \(x=0\). Moreover,
as \(L\to\infty\),
\[
 \log \operatorname{Lip}(T_L)
 =\frac{L^2}{2}+\log 2
 -\frac{\varphi(L)}{L}
   \left(1-\frac1{L^2}+\frac3{L^4}+O(L^{-6})\right).
\]

## Proof

Completing the square gives
\[
 Z_L=2\int_0^\infty e^{Lt}\varphi(t)\,dt
     =2e^{L^2/2}\Phi(L).
\]
Both source and target densities are positive and continuous, so the
quantile transport is strictly increasing and \(C^1\). Symmetry makes it
odd. In particular, \(T_L(0)=0\), \(T_L(x)\geq0\) for \(x\geq0\), and
\[
 T_L'(x)=\frac{\varphi(x)}{q_L(T_L(x))},\qquad T_L'(0)=Z_L.
\]

Fix \(x\geq0\) and set
\[
 y=T_L(x)-L.
\]
For \(t\geq0\), completing the square also gives
\[
 q_L(t)=\frac{\varphi(t-L)}{2\Phi(L)}.
\]
Matching upper-tail probabilities under the monotone transport, and then
differentiating the quantile identity, yields the exact formulas
\[
 \overline\Phi(y)=2\Phi(L)\overline\Phi(x),
 \qquad
 T_L'(x)=2\Phi(L)\frac{\varphi(x)}{\varphi(y)}.
\]
Consequently
\[
 \frac{T_L'(x)}{Z_L}
 =\exp\!\left(\frac{y^2-x^2-L^2}{2}\right).                 \tag{1}
\]

It remains to bound the exponent. Since \(T_L(x)\geq0\), one has
\(y\geq-L\). If \(-L\leq y\leq0\), then
\[
 y^2-x^2\leq y^2\leq L^2.
\]
For \(x>0\), strict monotonicity gives \(T_L(x)>0\), hence \(y>-L\),
so the last inequality is strict. If instead \(y\geq0\), then
\(2\Phi(L)>1\), and the tail identity gives
\[
 \overline\Phi(y)>\overline\Phi(x).
\]
Because \(\overline\Phi\) is strictly decreasing, \(y<x\). Thus
\(y^2-x^2<0<L^2\). At \(x=0\), one has \(y=-L\), so equality holds in
the exponent. Equation (1) therefore proves
\[
 T_L'(x)\leq Z_L\quad(x\geq0),
 \qquad T_L'(x)=Z_L\Longleftrightarrow x=0.
\]
Oddness of \(T_L\) makes \(T_L'\) even, so the same statement holds on
all of \(\mathbb R\).

The continuous derivative is bounded by \(Z_L\), so the mean value theorem
gives \(\operatorname{Lip}(T_L)\leq Z_L\). Conversely, difference
quotients at zero give
\(\operatorname{Lip}(T_L)\geq T_L'(0)=Z_L\). This proves the asserted
global equality and shows that the full continuous-derivative maximizer set
is exactly \(\{0\}\).

Finally, write \(r_L=\overline\Phi(L)\). Repeated integration by parts in
the Gaussian tail gives
\[
 r_L=\frac{\varphi(L)}{L}
 \left(1-\frac1{L^2}+\frac3{L^4}+O(L^{-6})\right).
\]
Since \(\log\Phi(L)=\log(1-r_L)=-r_L+O(r_L^2)\), with \(r_L^2\)
smaller than the displayed remainder scale, substitution into
\[
 \log Z_L=\frac{L^2}{2}+\log2+\log\Phi(L)
\]
gives the claimed sharp logarithmic expansion. \(\square\)

## Gap list

No mathematical gap is known in the argument above. The claim still requires
a fresh referee audit under the project release workflow.
