# A unicyclic degree-transform identity

This note is a Builder derivation. It is not promoted to a final theorem
until the separate Referee reconstruction and novelty pass are recorded.

## Notation

Let \(G=(V,E)\) be a connected unicyclic graph of order \(n\), with unique
cycle \(C\) of length \(c\). Write the power-sum expansion as
\[
X_G=\sum_{\lambda\vdash n} a_\lambda(G)p_\lambda.
\]
Let \(m_1(\lambda)\) and \(\ell(\lambda)\) denote the number of parts equal
to one and the number of parts, respectively. Put
\[
s_b(G)=(-1)^{n-b}\sum_{\lambda\vdash n}
 a_\lambda(G)m_1(\lambda)
 \binom{n-\ell(\lambda)}{n-b},
\]
with out-of-range binomial coefficients interpreted as zero, and define
\[
\mathcal S_G(z)=\sum_{b\ge0}s_b(G)z^b.
\]
Define the cycle and off-cycle degree polynomials
\[
A_G(z)=\sum_{v\in V(C)}z^{\deg_G(v)},\qquad
O_G(z)=\sum_{v\notin V(C)}z^{\deg_G(v)},
\]
and \(D_G(z)=A_G(z)+O_G(z)\).

## Identity

The claimed exact identity is
\[
\boxed{\mathcal S_G(z)=
A_G(z)+\bigl(1-(1-z)^{c-1}\bigr)O_G(z).}
\tag{1}
\]

### Proof

Stanley's spanning-subgraph formula gives
\[
a_\lambda(G)=
\sum_{\substack{F\subseteq E\\\operatorname{type}(V,F)=\lambda}}
(-1)^{|F|}.
\]
Write \(\kappa(F)\) for the number of components of \((V,F)\). Expanding
the definition of \(s_b\), and using the fact that \(m_1(\operatorname{type}
(V,F))\) counts isolated vertices, the contribution of a fixed vertex
\(v\) is
\[
\sum_{F\subseteq E(G-v)}
(-1)^{|F|+q}\binom{n-\kappa(F)}q,
\qquad q=n-b. \tag{2}
\]
It is enough to take \(0\le b\le n-1\), hence \(q\ge1\). For \(b=n\)
both sides of (1) have zero coefficient because a connected simple graph of
order at least three has no vertex of degree \(n\), while the alternating
sum in (2) vanishes.

If \(v\in C\), every \(F\subseteq E(G-v)\) is a forest, so
\(n-\kappa(F)=|F|\). Since
\(|E(G-v)|=n-\deg(v)\), the binomial identity
\[
\sum_{F\subseteq P}(-1)^{|F|+q}\binom{|F|}q
=\mathbf1_{\{|P|=q\}}
\]
shows that (2) equals \(\mathbf1_{\{\deg(v)=b\}}\). Thus a cycle
vertex contributes \(z^{\deg(v)}\) to \(\mathcal S_G(z)\).

Now suppose \(v\notin C\). The same forest calculation supplies the base
term \(\mathbf1_{\{\deg(v)=b\}}\), but it treats incorrectly those
\(F\) that contain every edge of \(C\). For such \(F\),
\(n-\kappa(F)=|F|-1\). Put \(d=\deg(v)\) and
\(h=|E(G-v)\setminus E(C)|=n-d-c\). The correction to (2) is
\[
\begin{aligned}
&\sum_{\substack{F\subseteq E(G-v)\\E(C)\subseteq F}}
(-1)^{|F|+q}
\left[\binom{|F|-1}q-\binom{|F|}q\right]\\
&\quad=-(-1)^{c+q}
\sum_{j=0}^h(-1)^j\binom hj\binom{c+j-1}{q-1}\\
&\quad=(-1)^{b+d+1}\binom{c-1}{d+c-b-1}.
\end{aligned}
\]
Here the last step is the standard finite-difference identity
\[
\sum_{j=0}^h(-1)^j\binom hj\binom{r+j}{k}
=(-1)^h\binom r{k-h}.
\]
Consequently a fixed off-cycle vertex of degree \(d\) contributes
\[
z^d\left(\sum_{j=1}^{c-1}
(-1)^{j+1}\binom{c-1}{j}z^j\right)
=z^d\bigl(1-(1-z)^{c-1}\bigr).
\]
The missing constant term reflects the exact cancellation between the
forest base term and the \(j=0\) cyclic correction.
Summing over vertices proves (1).

## Equal-CSF divisibility

If \(X_G=X_H\), the source paper implies that \(G,H\) have the same
order and cycle length \(c\). Equality in (1) gives
\[
D_G(z)-D_H(z)
=(1-z)^{c-1}\bigl(O_G(z)-O_H(z)\bigr). \tag{3}
\]
Both off-cycle degree polynomials have zero constant term and value \(n-c\)
at \(z=1\). Therefore
\[
\boxed{z(1-z)^c\mid D_G(z)-D_H(z).} \tag{4}
\]
If \(G,H\) have equally many leaves, then the coefficient of \(z\) in
\(O_G-O_H\) also vanishes, and
\[
\boxed{z^2(1-z)^c\mid D_G(z)-D_H(z).} \tag{5}
\]

## Consequences

1. If \(\max\{\Delta(G),\Delta(H)\}\le c\), then (4) forces
   \(D_G=D_H\). Thus the degree sequences agree. The identity
   \(k=n-n_1\) gives equal internal-edge counts, and published Corollary 15
   then gives equal rooted-tree counts. This proves all three structural
   conclusions, without a parity hypothesis.

2. More generally, if the leaf counts agree and both maximum degrees are at
   most \(c+1\), then (5) forces \(D_G=D_H\).

3. For every connected \(c\)-unicyclic graph of order \(n\),
   \(\Delta(G)\le n-c+2\).

4. Suppose \(c\ge4\) and \(n\le2c-1\). The exceptional published hook
   alternative \(r=1\) versus \(r=c\) is infeasible because \(r=c\)
   requires at least \(c\) off-cycle vertices, hence \(n\ge2c\). Thus
   equal CSFs force equal \(r,k\), and hence equal leaf counts. Now
   \(\Delta\le n-c+2\le c+1\), so item 2 gives equal degree sequences.
   Therefore Conjecture 9.1/63 holds throughout this infinite parameter
   range.

5. The endpoint \(n=2c\), \(c\ge4\), also closes. In the non-exceptional
   hook case, (5) and \(\Delta\le c+2\) imply
   \[
   D_G-D_H=a z^2(1-z)^c
   \]
   for an integer \(a\). If \(c\ge5\) and \(a\ne0\), its coefficient
   \(\ell^1\)-norm is at least \(2^c>4c=2n\), whereas a difference of two
   \(n\)-vertex degree polynomials has coefficient \(\ell^1\)-norm at most
   \(2n\), a contradiction. For \(c=4\), \(a=\pm1\) is the only remaining
   norm possibility; equality in the norm bound would force one degree
   sequence to be \((6,4,4,4,4,4,4,2)\), whose degree sum is \(32\), not
   \(2n=16\).

   In the exceptional case, the \(r=c\) graph must be the cycle with one
   leaf at each cycle vertex. The \(r=1\) graph has \(c-1\) leaves and one
   off-cycle internal vertex. Divisibility (4), together with the leaf
   difference, forces \(D_G-D_H=-z(1-z)^c\). Matching the coefficient of
   \(z^2\) forces that off-cycle internal vertex to have degree two and the
   cycle root to have degree \(c+1\). The actual difference is then
   \[
   -z+c z^2-cz^3+z^{c+1},
   \]
   which equals \(-z(1-z)^c\) only for \(c=3\), not for \(c\ge4\).
   Hence Conjecture 9.1/63 holds for \(c\ge4,\ n\le2c\).

The last endpoint argument deliberately excludes \(c=3,n=6\): there the
displayed polynomials do agree and recover the smallest parity-excluded
phenomenon rather than contradicting it.
