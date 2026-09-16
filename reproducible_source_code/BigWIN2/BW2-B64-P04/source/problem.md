# Precise problem statement

## Frozen interpretation

For each integer \(n\ge 3\), let \(p(t)\in\mathbb F_2[t]\) be an
irreducible polynomial of degree \(n\), set
\[
F=\mathbb F_2[t]/(p(t))\cong\mathbb F_{2^n},\qquad
\alpha=t\bmod p(t),
\]
and fix the polynomial reference basis
\(E=(1,\alpha,\ldots,\alpha^{n-1})\).  Put \(V=\mathbb F_2^n\).  The
reference inversion map is
\[
J_n:V\to V,\qquad J_n([x]_E)=[x^{-1}]_E,
\]
with the convention \(0^{-1}=0\).

Let \(P=(p_{ij})_{0\le i,j<n}\in\mathbb F_2^{n\times n}\) and
\(u=(u_0,\ldots,u_{n-1})^T\in V\).  All \(n^2+n\) entries of \((P,u)\)
are independent Boolean variables.  The **complete raw polynomial
extension** is the map on the full Boolean matrix space
\[
f_{\rm raw}^{(n,p)}:\mathbb F_2^{n\times n}\times V\to V,
\qquad
f_{\rm raw}^{(n,p)}(P,u)=\operatorname{adj}(P)J_n(Pu),
\]
where the adjugate and matrix products are over \(\mathbb F_2\).  This
definition includes singular \(P\).  For \(P\in\operatorname{GL}_n(\mathbb
F_2)\), \(\det P=1\), so \(\operatorname{adj}(P)=P^{-1}\); nevertheless,
the object whose ANF is studied is the displayed function on **all**
\(2^{n^2+n}\) Boolean inputs.  It must not be replaced by its restriction
to invertible matrices.

For a Boolean scalar function \(g:\mathbb F_2^d\to\mathbb F_2\), write
its unique multilinear algebraic normal form as
\[
g(x)=\bigoplus_{A\subseteq[d]}c_A\prod_{i\in A}x_i.
\]
Its algebraic degree is \(\deg g=\max\{|A|:c_A\ne0\}\), with
\(\deg0=-\infty\).  For a vector map \(G=(G_0,\ldots,G_{m-1})\),
\[
\deg G=\max_j\deg G_j.
\]

Writing the vector ANF as
\[
G(x)=\bigoplus_{A\subseteq[d]}c_A\prod_{i\in A}x_i,
\qquad c_A\in\mathbb F_2^m,
\]
define the joint support
\(\mathcal A(G)=\{A:c_A\ne0\}\).  If \(G\ne0\) and
\(q=|\mathcal A(G)|\), its **joint ANF leap** is
\[
L_{\rm ANF}^{\rm joint}(G)
=\min_{(A_1,\ldots,A_q)}\ \max_{1\le r\le q}
\left|A_r\setminus\bigcup_{s<r}A_s\right|,
\]
where the minimum ranges over all orderings of the joint support.

The claim to decide is the conjunction
\[
\deg f_{\rm raw}^{(n,p)}=3(n-1)
\quad\text{and}\quad
L_{\rm ANF}^{\rm joint}(f_{\rm raw}^{(n,p)})=n
\tag{C}
\]
for every integer \(n\ge3\).  The paper begins with an arbitrary
irreducible \(p\) and then fixes its polynomial basis; accordingly, the
unqualified uniform reading of (C) is: **for every permitted degree-\(n\)
irreducible \(p\)**.  If either invariant depends on this choice, that
dependence is a material scope issue and must be reported rather than
silently selecting a favorable reference basis.

If (C) is false, determine the least \(n\ge3\) for which there is a
permitted reference polynomial \(p\) at which one of the equalities
fails, and compute both exact invariants at the failing pair \((n,p)\),
identifying which equality fails.  A result under a different
reference-basis quantifier must be labeled as a proposed variant, not as
a resolution of this frozen reading.

## Boundary cases and established baseline

- The original quantifier starts at \(n=3\).  Results in the primary
  paper are stated from \(n=2\), but \(n=2\) cannot be the requested
  least failure.
- Zhang--Zhang, Proposition 12, proves for every \(n\ge2\)
  \(\deg f_{\rm raw}\le3(n-1)\).
- Zhang--Zhang, Theorem 17, proves every supported monomial has degree at
  least \(n\), hence \(L_{\rm ANF}^{\rm joint}(f_{\rm raw})\ge n\).
- Their exhaustive full-domain Boolean computations give
  \((\deg,L)=(6,3)\) for \(n=3\) and \((9,4)\) for \(n=4\) (Section 4.2,
  Table 1).  These are exact finite observations for the implemented
  reference fields, not a proof for general \(n\).

Thus the exact missing statements are a matching degree lower bound and
a matching leap upper bound.  For the degree, a sufficient certificate
is a nonzero ANF coefficient of degree \(3(n-1)\).  For the leap, a
sufficient certificate is an ordering (or a supported-set cover followed
by the remaining support) in which no step introduces more than \(n\)
new variables.

## Source and status audit

Primary source: Zheng Zhang and Na Zhang, *Representation Redundancy and
Structural Complexity in Finite-Field Inversion*, arXiv:2609.04583v1,
submitted 2026-09-04, <https://arxiv.org/abs/2609.04583>.  The inspected
30-page PDF has SHA-256
`adccdaad3014a91760fe1af9686e7d75cd2c647a637dc9a3d69cc1476a5aa6bc`,
matching `source.md`.  Relevant locations inspected on 2026-09-07 are
Definitions 8, 11, 13, and 14; Proposition 12; Theorem 17; Section 4.2
and Table 1; and the Conclusion (pp. 8--17 and 24 in the PDF).

The Conclusion explicitly names proving the exact raw ANF values for
general \(n\) as future work.  Exact-phrase/title searches on 2026-09-07
for `"Proving the exact raw ANF values for general n"`, `"deg(fraw)"
"3(n - 1)" inversion`, `"joint ANF leap" "complete raw"`, and the full
paper title found no distinct primary source resolving (C).  This is an
`open-supported` lead relative to the inspected very recent v1, not a
claim of priority or a guarantee that no equivalent result exists.

## Triage target

Nearest prior result: Proposition 12 and Theorem 17 give the two
one-sided bounds, and Table 1 attains them at \(n=3,4\).  Proposed delta:
prove both matching bounds uniformly, or find the least exact
counterexample (including any reference-polynomial dependence).
Verification route: express selected ANF coefficients by the exact
Möbius formula
\(c_A=\bigoplus_{C\subseteq A}f_{\rm raw}(1_C)\), first seek a symbolic
family of top-degree coefficients, and separately generalize or falsify
the supported-set leap certificates in Appendix A, Table 7.
