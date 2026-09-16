# General-\(n\) sign audit and proof

Job: `win-00075-p02-research-d85b870a7583`  
Date: 2026-09-09

This note proves the claim frozen in `source.md` and interpreted in
`problem.md`. The source formulas were checked against arXiv:2609.05051v1,
Definition 7.1, equations (7.1)--(7.3), and Example 8.7, equations
(8.31)--(8.32). No novelty or priority assertion is made.

## 1. Exact specialization of Definition 7.1

Let \(p_i:\mathfrak g\to K\) be the \(x_i\)-coordinate functional and let
\(\varepsilon=u_n^*:V\to K\). Put

\[
 \delta(y_1,\ldots,y_{n-1})
 :=\det\bigl(p_a(y_b)\bigr)_{1\leq a,b\leq n-1}.
\]

Because (8.31) is the only nonzero basis value of the alternating action,
multilinearity gives, for arbitrary \(y_1,\ldots,y_{n-1}\in\mathfrak g\) and
\(q\in V\),

\[
 \rho_{\mathfrak g}(y_1,\ldots,y_{n-1})q
 =\delta(y_1,\ldots,y_{n-1})\,\varepsilon(q)u_n. \tag{1}
\]

Similarly, the sole bracket value
\([x_1,\ldots,x_n]_{\mathfrak g}=x_n\) implies

\[
 [y_1,\ldots,y_n]_{\mathfrak g}
 =\det\bigl(p_a(y_b)\bigr)_{1\leq a,b\leq n}\,x_n. \tag{2}
\]

In Example 8.7, \(V\) is abelian and
\(\vartheta_V=\rho_V=\vartheta_{\mathfrak g}=0\). Thus every term of
(7.1)--(7.2) except the bracket in \(G_r\) and the
\(\rho_{\mathfrak g}\)-sum in \(H_r\) vanishes, leaving

\[
\begin{aligned}
G_r(q_1,\ldots,q_n)
 &= [r(q_1),\ldots,r(q_n)]_{\mathfrak g},\\
H_r(q_1,\ldots,q_n)
 &=\sum_{i=1}^n(-1)^{n-i}
 \rho_{\mathfrak g}(r(q_1),\ldots,\widehat{r(q_i)},\ldots,r(q_n))q_i.
\end{aligned} \tag{3}
\]

## 2. Alternation and the signs

For \(q_1,\ldots,q_n\in V\), form the \(n\times n\) matrix

\[
B(q_1,\ldots,q_n)=
\begin{pmatrix}
p_1(r(q_1))&\cdots&p_1(r(q_n))\\
\vdots&&\vdots\\
p_{n-1}(r(q_1))&\cdots&p_{n-1}(r(q_n))\\
\varepsilon(q_1)&\cdots&\varepsilon(q_n)
\end{pmatrix}.
\]

Substitution of (1) into (3) shows that the scalar multiplying \(u_n\) in
\(H_r\) is

\[
\sum_{i=1}^n(-1)^{n-i}\varepsilon(q_i)
 \det\!\left(B(q_1,\ldots,q_n)_{\widehat n,\widehat i}\right),
\]

This is exactly the Laplace expansion of \(\det B\) along its last row: the
subscript denotes deletion of the indicated row and column, the cofactor sign
is \((-1)^{n+i}\), and
\((-1)^{n+i}=(-1)^{n-i}\) because the exponents differ by \(2i\).
Consequently

\[
H_r(q_1,\ldots,q_n)=\det B(q_1,\ldots,q_n)u_n. \tag{4}
\]

Equation (4) proves directly, including in the sign convention of (7.2), that
\(H_r\) is alternating and \(n\)-linear. Equation (2) proves the same for
\(G_r\). Thus neither alternation assertion is being inferred from the desired
deformation equation.

## 3. Ordered-basis values

Use the column convention from `problem.md`. On
\((u_1,\ldots,u_n)\), the coordinate matrix in (2) is \(R\), so

\[
G_r(u_1,\ldots,u_n)=\det(R)x_n. \tag{5}
\]

For clarity, one may also audit (3) term by term. If \(i<n\), the \(i\)-th
summand is zero because (1) contains \(\varepsilon(u_i)=0\). For \(i=n\), the
sign is \((-1)^{n-n}=+1\) and the first \(n-1\) coordinate columns of
\(r(u_1),\ldots,r(u_{n-1})\) form \(A\). Hence

\[
H_r(u_1,\ldots,u_n)=\det(A)u_n. \tag{6}
\]

Equivalently, (4) uses

\[
B(u_1,\ldots,u_n)=
\begin{pmatrix}A&v\\0&1\end{pmatrix},
\]

whose determinant is \(\det A\). This also checks that the last column \(v\)
introduces no omitted action term.

## 4. Classification

Both sides of (7.3), namely \(G_r\) and \(r\circ H_r\), are alternating
\(n\)-linear maps on the \(n\)-dimensional space \(V\). They agree on every
tuple if and only if they agree on the ordered basis tuple. By (5)--(6),
Definition 7.1 is therefore equivalent to

\[
 \det(R)x_n=\det(A)r(u_n)
 =\det(A)\left(\sum_{j=1}^{n-1}v_jx_j+\alpha x_n\right). \tag{7}
\]

Comparing the \(x_1,\ldots,x_n\) coordinates in (7) gives precisely

\[
 \det(A)v=0,
 \qquad
 \det(R)=\alpha\det(A). \tag{8}
\]

Conversely, (8) makes (7) hold, and alternation then makes (7.3) hold on all
tuples. This proves both directions of the frozen claim for every \(n\ge4\)
and every characteristic-zero field \(K\).

If \(\det A\ne0\), (8) forces \(v=0\); with this block zero,
\(\det R=\alpha\det A\) automatically, and \(w,\alpha\) are arbitrary.
If \(\det A=0\), the first equation is automatic and the second is exactly
\(\det R=0\). There are no further conditions.

Gap list: empty. The exact independent \(n=4\) polynomial expansion in
`evidence/n4_symbolic_check.py` is a finite sign/coordinate check, not a
substitute for the general proof above.
