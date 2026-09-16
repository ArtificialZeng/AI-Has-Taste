# A two-vertex-component edge transform

## Notation

Let \(G\) be a connected unicyclic graph of order \(n\), with unique cycle
\(C\) of length \(c\), and write
\[
X_G=\sum_{\lambda\vdash n}a_\lambda(G)p_\lambda.
\]
For \(0\le b\le n\), put
\[
t_b(G)=(-1)^{n-b}\sum_{\lambda\vdash n}a_\lambda(G)
m_2(\lambda)\binom{n-\ell(\lambda)}{n-b},
\qquad
\mathcal T_G(z)=\sum_{b=0}^n t_b(G)z^b.
\]
Define
\[
P_G(z)=\sum_{uv\in E(G)}z^{\deg(u)+\deg(v)-2}
\]
and let \(Q_G(z)\) be the same sum restricted to edges whose two endpoints
both lie off \(C\).

## Identity

The exact identity is
\[
\boxed{\mathcal T_G(z)=(1-z)P_G(z)-(1-z)^cQ_G(z).}
\tag{6}
\]

### Proof

In Stanley's spanning-subgraph expansion, \(m_2(\lambda(V,F))\)
counts the two-vertex components of \((V,F)\). Such a component is specified
by an edge \(e=uv\): the edge \(e\) is selected, every other edge incident
with \(u\) or \(v\) is absent, and an arbitrary edge set \(R\) is selected
from \(G-\{u,v\}\). Put
\[
d_e=\deg(u)+\deg(v)-2,
\qquad M=|E(G-\{u,v\})|=n-d_e-1,
\]
and let \(q=n-b\). If \(R\) is a forest, its contribution for the fixed
edge \(e\) is
\[
(-1)^{|R|+1+q}\binom{|R|+1}{q}.
\]
The generating-function calculation
\[
\sum_{r=0}^{M}(-1)^r\binom Mr(1+x)^{r+1}
=(1+x)(-x)^M
\]
shows that the sum of these forest contributions over all \(R\) is
\(z^{d_e}(1-z)\).

If at least one endpoint of \(e\) lies on \(C\), then
\(G-\{u,v\}\) is a forest, so this is the complete contribution. Suppose
instead that both endpoints lie off \(C\). The only non-forest sets \(R\)
are those containing every edge of \(C\). For them the actual value of
\(n-\ell(\lambda(V,\{e\}\cup R))\) is \(|R|\), one less than the forest
value \(|R|+1\). Writing
\(h=|E(G-\{u,v\})\setminus E(C)|=n-d_e-c-1\), the correction is
\[
\begin{aligned}
&\sum_{j=0}^{h}(-1)^{c+j+q}\binom hj
  \binom{c+j}{q-1}\\
&\qquad=(-1)^{b+d_e+1}\binom c{d_e+c-b},
\end{aligned}
\]
by finite differences. As a polynomial in \(z\), this correction is
\(-z^{d_e}(1-z)^c\). Summing the fixed-edge contributions proves (6).

## Equal-CSF consequence

The quotient \(\mathcal T_G(z)/(1-z)\) is determined by \(X_G\), and (6)
gives
\[
\frac{\mathcal T_G(z)}{1-z}=P_G(z)-(1-z)^{c-1}Q_G(z).
\]
Consequently, if \(X_G=X_H\), then
\[
\boxed{P_G(z)-P_H(z)=(1-z)^{c-1}
       \bigl(Q_G(z)-Q_H(z)\bigr).}
\tag{7}
\]
No edge with both endpoints off the cycle can have two degree-one
endpoints. Hence \(Q_G(0)=Q_H(0)=0\), and
\[
\boxed{z(1-z)^{c-1}\mid P_G(z)-P_H(z).}
\tag{8}
\]

The first attempted version of (6) omitted the factor \(1-z\) in the
forest term. Exact testing on a cycle exposed the error before promotion.
After repair, two independent calculations from the integer power-sum CSF
agree on 20 boundary examples and on every connected unicyclic graph of
orders \(3\) through \(10\) (1,040 isomorphism classes).
