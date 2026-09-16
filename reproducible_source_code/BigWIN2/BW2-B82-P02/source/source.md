# Source statement: loopy-polynomial injectivity at root height two

Source id: ARXIV-2609.07728-B82

Primary source: Kirillov, Nenashev, Shapiro, and Vaintrob, *The Loopy
Polynomial of a Graph: Contraction Identity, Random Maps, and
Reconstruction Problems*, arXiv:2609.07728v1, Conjecture 9.10,
Remark 9.12, and Theorem 9.14.

Local source PDF:
\`batches/inbox/bigWin-82-materials/2609.07728.pdf\`, SHA-256
\`f3d4ae846384717ecce1c31261f021f172dad47443c7dd635d1d15b64ddd8f12\`.

## Frozen claim

Let \(g\ge3\), and let \((H,\rho)\) be a finite rooted tree. For every
\(J\subseteq E(H)\), let \(c(J)\) be the components of the spanning
forest \((V(H),J)\), and let \(R_J\in c(J)\) be the component containing
\(\rho\). Define
\[
\Psi_{H,g}(\mathbf z)=
\sum_{J\subseteq E(H)}
z_{g-1+|V(R_J)|}
\prod_{\substack{D\in c(J)\\D\ne R_J}}z_{|V(D)|}.
\]

Prove or disprove the following quantified statement:

> For every integer \(g\ge3\), every \(N\ge1\), and every two rooted
> trees \((H,\rho)\), \((H',\rho')\) on \(N\) vertices whose maximum
> root distance is at most two,
> \[
> \Psi_{H,g}=\Psi_{H',g}
> \quad\Longrightarrow\quad
> (H,\rho)\cong(H',\rho').
> \]

## Verified source boundary

Conjecture 9.10 asks injectivity on all rooted trees for every \(g\ge3\).
Remark 9.12 reports exhaustive verification through \(N=13\), and the
map is automatic for \(g\ge N\). Theorem 9.14 covers a branch-size
restricted regime. Any contribution must clearly identify the remaining
range it adds and must not present the full conjecture as solved.

## Required verification route

For a height-two rooted tree, write the root branches as rooted stars of
orders \(b_1,\ldots,b_r\). Derive the relevant homogeneous component of
\(\Psi\) from the definition, prove that it recovers the multiset
\(\{b_i\}\), and prove that this multiset determines rooted isomorphism.
Use an exact integer-partition enumerator only as an independent audit,
not as the proof of the quantified infinite statement.
