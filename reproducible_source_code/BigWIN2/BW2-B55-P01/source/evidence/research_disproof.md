# Exact open-box obstruction and threshold determination

## Claim

For the colored five-cycle in `source.md`,

\[
\operatorname{mlt}(G_5)=2.
\]

In particular, the frozen assertion `mlt(G_5)=1` is false.  The failure for one
observation occurs throughout the explicit open box

\[
U=(9/10,11/10)^5,
\]

not merely at an exceptional observation.

## Exact construction on the open box

For \(x=(x_0,\ldots,x_4)^T\), fix the common diagonal parameter at \(a=2\).
Writing the five equations \(K(2,b)x=0\) as \(B(x)b=-2x\) gives

\[
B(x)=\begin{pmatrix}
x_1&0&0&0&x_4\\
x_0&x_2&0&0&0\\
0&x_1&x_3&0&0\\
0&0&x_2&x_4&0\\
0&0&0&x_3&x_0
\end{pmatrix},\qquad
\det B(x)=2x_0x_1x_2x_3x_4.
\]

Thus \(B(x)\) is invertible on \(U\).  Exact solution of the system gives

\[
\begin{aligned}
b_0&=-\frac{x_0^2+x_1^2-x_2^2+x_3^2-x_4^2}{x_0x_1},\\
b_1&= \frac{x_0^2-x_1^2-x_2^2+x_3^2-x_4^2}{x_1x_2},\\
b_2&=-\frac{x_0^2-x_1^2+x_2^2+x_3^2-x_4^2}{x_2x_3},\\
b_3&= \frac{x_0^2-x_1^2+x_2^2-x_3^2-x_4^2}{x_3x_4},\\
b_4&=-\frac{x_0^2-x_1^2+x_2^2-x_3^2+x_4^2}{x_4x_0}.
\end{aligned}
\]

All denominators are positive on \(U\).  Each bracket preceded by a minus sign
is a sum of three positive squares minus two positive squares, and hence is
strictly greater than

\[
3(9/10)^2-2(11/10)^2=1/100.
\]

Each numerator without an external minus sign is a sum of two positive squares
minus three positive squares, and hence is strictly less than

\[
2(11/10)^2-3(9/10)^2=-1/100.
\]

Consequently \(b_i(x)<0\) for every \(i\) and every \(x\in U\).

Set \(w_i=-b_i x_i x_{i+1}>0\), with indices modulo five.  Multiplying the
\(i\)-th equation of \(K(2,b)x=0\) by \(x_i\) yields

\[
2x_i^2=w_{i-1}+w_i.
\]

Therefore, for every \(y\in\mathbb R^5\),

\[
y^TK(2,b)y
=\sum_{i=0}^4 w_i
 \left(\frac{y_i}{x_i}-\frac{y_{i+1}}{x_{i+1}}\right)^2.
\]

This proves \(K(2,b)\succeq0\).  Because all five weights are positive and the
cycle is connected, equality holds exactly when \(y_i/x_i\) is constant for
all \(i\).  Hence \(\ker K(2,b)=\mathbb R x\) and \(\operatorname{rank}K=4\).
In particular, every \(x\in U\) is annihilated by a nonzero matrix in
\(L_{G_5}\cap\operatorname{PSD}(5)\).

The box \(U\) has Lebesgue measure \((1/5)^5>0\), so Theorem 3.4(2) of the
primary source rules out \(\operatorname{mlt}(G_5)=1\).  Corollary 3.7 and
Proposition 3.26 of that source give

\[
\operatorname{mlt}(G_5)\leq \operatorname{gcr}(G_5)=2.
\]

Since the threshold is a positive integer, these two facts give
\(\operatorname{mlt}(G_5)=2\), completing the disproof in the full frozen
scope.

## Reproduction and dependency scope

Run `python3 evidence/research_disproof.py`.  The script independently constructs
the coefficient matrix from the five kernel equations, checks its determinant,
checks the displayed rational solution, verifies the congruence with a weighted
cycle Laplacian, verifies the exact box margin, and rechecks the all-ones
specialization.  Symbolic computation is used only to replay displayed exact
identities; the proof above does not infer a theorem from sampled data.

The threshold upper bound and the PSD-kernel characterization are external
dependencies, found respectively in Corollary 3.7, Proposition 3.26, and
Theorem 3.4(2) of the copied primary source
`evidence/external/2609.02382.pdf`.
