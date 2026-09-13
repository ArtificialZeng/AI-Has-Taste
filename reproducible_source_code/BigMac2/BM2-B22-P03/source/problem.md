# Precise problem reading

## Frozen claim

Let

\[
V_4=\{0,1\}^4,
\qquad
F_{i,\varepsilon}=\{v=(v_1,\ldots,v_4)\in V_4:v_i=\varepsilon\},
\]

for $i\in\{1,2,3,4\}$ and $\varepsilon\in\{0,1\}$, and let

\[
\mathcal F_4=\{F_{i,\varepsilon}:1\le i\le4,
\ \varepsilon\in\{0,1\}\}.
\]

Thus \(\mathcal F_4\) consists of the eight facets of the 4-cube, each
containing eight vertices. For an unordered five-element subset
$S=\{v_0,\ldots,v_4\}\subset V_4$, define

\[
\operatorname{Vol}(S)
=4!\operatorname{vol}_4(\operatorname{conv}S)
=\left|\det\begin{pmatrix}
v_0&v_1&v_2&v_3&v_4\\
1&1&1&1&1
\end{pmatrix}\right|.
\]

The absolute value makes this independent of the displayed ordering. It is a
nonnegative integer and is zero exactly when $S$ is affinely dependent.

For $x=(x_v)_{v\in V_4}\in\mathbb R_{\ge0}^{16}$, put

\[
P_4(x)=\sum_{S\in\binom{V_4}{5}}
 \operatorname{Vol}(S)\prod_{v\in S}x_v,
\quad
\sigma(x)=\sum_{v\in V_4}x_v,
\quad
Q_4(x)=\prod_{F\in\mathcal F_4}\left(\sum_{v\in F}x_v\right).
\]

The original claim is precisely

\[
\boxed{\quad \forall x\in\mathbb R_{\ge0}^{16},\qquad
P_4(x)\,\sigma(x)^3\le Q_4(x).\quad} \tag{HC4}
\]

Equivalently, the homogeneous degree-eight polynomial

\[
H_4(x)=Q_4(x)-P_4(x)\sigma(x)^3
\]

is copositive. This is a universal real inequality, not merely a statement for
strictly positive variables or for symmetric assignments.

## Normalization and boundary

Both sides have total degree eight. The zero vector satisfies equality. For
$x\ne0$, setting $y=x/\sigma(x)$ shows that (HC4) is equivalent to its
restriction to the closed simplex

\[
\{y\in\mathbb R_{\ge0}^{16}:\sum_v y_v=1\}.
\]

The normalization does not remove boundary supports. If all variables on some
facet $F_{i,\varepsilon}$ vanish, then $Q_4=0$; the remaining support lies in
the opposite three-dimensional facet, so every five-vertex determinant is zero
and $P_4=0$. Hence every facet-vanishing point is an equality point. No
converse equality classification is assumed for $d=4$.

For $T=\operatorname{supp}(x)=\{v:x_v>0\}$:

- if $|T|\le4$, then $P_4(x)=0$;
- if $|T|=5$ and $T$ is affinely dependent, then $P_4(x)=0$;
- if $|T|=5$ and $T$ is affinely independent, the only nonzero term
  in $P_4$ is $\operatorname{Vol}(T)\prod_{v\in T}x_v$.

Thus the five-point-support layer is an exact finite family of five-variable
degree-eight inequalities. Verification of that layer, of six-point supports,
or of a symmetric subspace would be a subsidiary result only and would not
settle the displayed universal claim without an additional coverage theorem.

## Parameter convention and nearest established result

In Averkov--von Dichter--Soprunov, the cube parameter is $d=n-1$.
Consequently this $d=4$ question corresponds to their geometric parameter
$n=5$. Their $n=4$ theorem is the $d=3$ hypercube inequality, not (HC4).
The formal definition is equation (16) in Section 4.4; Theorem 5.1 proves the
$d=3$ case, and Theorem 6.2 classifies equality there. Section 7.5 explicitly
states that the hypercube inequality remains open for $d\ge4$, describing the
$d=4$ case as 16 variables and degree eight. This resolves an inconsistent
dimension phrase in the introduction by following the paper's formal
$d=n-1$ convention and its explicit Section 7.5 statement.

Source inspected: G. Averkov, K. von Dichter, and I. Soprunov, *On the
Log-submodularity for zonoids: from Mixed Volume inequalities to the
Hypercube*, arXiv:2608.14909v1, submitted 2026-08-14,
<https://arxiv.org/abs/2608.14909>. The arXiv record was retrieved on
2026-09-09 and listed only v1. The local PDF actually located at
`/Users/mac/4prove-or-disprove-math/batches/literature/bigMac-22/2608.14909v1.pdf`
has SHA-256
`5880c0a7e8de2cf4e4ceef40b482eda7722fae68ca321576099c096b9a6518e5`,
matching the frozen source record. Targeted searches for the exact title and
the phrase “Hypercube inequality” with $d=4$ found no separate primary-paper
resolution as of 2026-09-09. This is evidence for the intake label
`open-supported`, not proof of priority or continued open status.

## Admitted research scope

The full target remains proof of (HC4), or a rational counterexample whose 16
coordinates, determinant-derived simplex contributions, and strictly negative
rational value of $H_4$ are reproducible. The bounded first subsidiary target
is complete resolution of all five-point supports modulo the 4-cube symmetry
group, followed only if warranted by the six-point layer. All coefficient data
must be regenerated from $V_4$ and the integer determinant definition.
Floating-point optimization may locate candidates but cannot certify either
truth or falsity.
