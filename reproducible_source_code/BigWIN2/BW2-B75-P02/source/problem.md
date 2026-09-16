# Precise problem statement

## Frozen source and scope

The immutable source is `source.md` (SHA-256
`6e3f9b3bbf507ff922c08b00a9ba2a36fb4be5f070ec53cb1f4c9273425495af`).
The statement below fixes its mathematical reading; it does not alter the source.

- Quantifiers: let \(n\ge 4\) be an integer and let \(K\) be an arbitrary field of
  characteristic zero. The restriction \(n>3\) comes from Section 8 of the cited
  source. The ternary case \(n=3\) and positive-characteristic fields are outside
  the frozen scope.
- All vector spaces and maps are over \(K\), and all brackets are alternating and
  \(K\)-multilinear.
- Let
  \[
  \mathfrak g=\operatorname{span}_K\{x_1,\ldots,x_n\},\qquad
  [x_1,\ldots,x_n]_{\mathfrak g}=x_n,
  \]
  with all other bracket values fixed by alternation and multilinearity. Let
  \(V=\operatorname{span}_K\{u_1,\ldots,u_n\}\) be the abelian \(n\)-Lie algebra.
- The only nonzero basis value of
  \(\rho_{\mathfrak g}:\bigwedge^{n-1}\mathfrak g\to\operatorname{End}(V)\)
  is
  \[
  \rho_{\mathfrak g}(x_1,\ldots,x_{n-1})u_n=u_n.
  \]
  Thus it kills \(u_1,\ldots,u_{n-1}\), and every other basis value of the
  alternating map is zero. All other matched-pair structure maps in Definition
  7.1 are zero. This is exactly the semidirect product in Example 8.7.

For a linear map \(r:V\to\mathfrak g\), the specialized Definition 7.1 says that
\(r\) is a deformation map precisely when, for every
\(q_1,\ldots,q_n\in V\),
\[
[r(q_1),\ldots,r(q_n)]_{\mathfrak g}
=r\!\left(\sum_{i=1}^n(-1)^{n-i}
\rho_{\mathfrak g}(r(q_1),\ldots,\widehat{r(q_i)},\ldots,r(q_n))q_i\right).
\tag{DM}
\]

## Matrix convention and claim

Use the column convention
\[
r(u_j)=\sum_{i=1}^n R_{ij}x_i,
\qquad
R=\begin{pmatrix}A&v\\ w^{\mathsf T}&\alpha\end{pmatrix},
\]
where \(A=(R_{ij})_{i,j<n}\in M_{n-1}(K)\),
\(v=(R_{1n},\ldots,R_{n-1,n})^{\mathsf T}\),
\(w=(R_{n1},\ldots,R_{n,n-1})^{\mathsf T}\), and \(\alpha=R_{nn}\).
This convention is material: under a row-matrix convention the displayed block
condition would be transposed.

The frozen claim to prove or disprove is
\[
r\text{ satisfies (DM)}
\quad\Longleftrightarrow\quad
\det(A)v=0\quad\text{and}\quad\det(R)=\alpha\det(A).
\tag{C}
\]
Equivalently, the full solution set is the disjoint union of:

1. \(\det(A)\ne0\): \(v=0\), while \(w\) and \(\alpha\) are arbitrary;
2. \(\det(A)=0\): \(\det(R)=0\), with no further asserted condition.

## Triage reduction and prior-result boundary

Both sides of (DM) are alternating maps on the \(n\)-dimensional space \(V\), so
it is enough to evaluate the ordered basis tuple. Directly from the displayed
structure maps,
\[
G_r(u_1,\ldots,u_n)=\det(R)x_n,
\qquad
H_r(u_1,\ldots,u_n)=\det(A)u_n.
\]
Consequently the basis-tuple equation is
\[
\det(R)x_n=\det(A)r(u_n)
=\det(A)\left(\sum_{j<n}v_jx_j+\alpha x_n\right),
\]
which yields exactly the coordinate equations in (C). This is an exact triage
reduction, not an independently refereed resolution.

The source paper supplies Definition 7.1 and one deformation map in Example 8.7,
but does not state the full matrix classification (C); Corollary 8.8 classifies
only isomorphism types of complements. The paper identifies Zhang's 2022
ternary paper as the prior deformation-map framework and says Example 8.7
generalizes its ternary examples. The accessible abstract of that earlier paper
does not determine whether it contains the exact \(n=3\) matrix classification.
Accordingly the source status is **new-question / literature status uncertain**,
not a source-certified open problem, and no novelty claim is made.

