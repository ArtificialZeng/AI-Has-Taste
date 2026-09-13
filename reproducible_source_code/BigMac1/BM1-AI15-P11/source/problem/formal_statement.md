# Formal statement

## Objects and notation

A **graph** below is finite, simple, and undirected. For every graph
\(G=(V,E)\) and integer \(k\ge 0\),

\[
i_k(G)=\#\{S\subseteq V: |S|=k\text{ and no edge of }G\text{ has both
endpoints in }S\}.
\]

The empty graph has polynomial \(I_{\varnothing}(x)=1\). For a nonempty
graph, the independence number is
\(\alpha(G)=\max\{|S|:S\subseteq V\text{ is independent}\}\), and in both
cases the independence polynomial is

\[
I_G(x)=\sum_{S\subseteq V\text{ independent}}x^{|S|}.
\]

When \(G\) is nonempty this equals
\(\sum_{k=0}^{\alpha(G)}i_k(G)x^k\). The object in the conjecture is a
nonempty connected acyclic graph, called a **tree** \(T\). Thus
\(i_0(T)=1\), \(i_k(T)>0\) for \(0\le k\le\alpha(T)\), and
\(i_k(T)=0\) for \(k>\alpha(T)\).

## Conjecture (Erdős problem #993)

For every finite tree \(T\), the finite coefficient sequence

\[
(i_0(T),i_1(T),\ldots,i_{\alpha(T)}(T))
\]

is weakly unimodal: there exists an index \(p\),
\(0\le p\le\alpha(T)\), such that

\[
i_0(T)\le\cdots\le i_p(T)\quad\text{and}\quad
i_p(T)\ge\cdots\ge i_{\alpha(T)}(T).
\]

Plateaux are allowed.  Equivalently, the sequence is not unimodal exactly
when there are indices \(0\le k<\ell<m\le\alpha(T)\) for which
\(i_k(T)>i_\ell(T)<i_m(T)\).  Hence the integer violation statistic

\[
\Delta(T)=\max_{k<\ell<m}\min\{i_k(T)-i_\ell(T),
                                  i_m(T)-i_\ell(T)\}
\]

is positive exactly for a counterexample (with \(\Delta(T)=-\infty\) when
fewer than three coefficients exist).

## Exact recurrences

For every vertex \(v\), with \(N[v]\) its closed neighbourhood,

\[
I_T(x)=I_{T-v}(x)+xI_{T-N[v]}(x),
\]

where the independence polynomial is multiplicative over disjoint unions.
For a rooted tree \((T,r)\), define explicitly

\[
A_T(x)=\sum_{\substack{S\subseteq V(T)\text{ independent}\\r\notin S}}
x^{|S|},\qquad
B_T(x)=\sum_{\substack{S\subseteq V(T)\text{ independent}\\r\in S}}
x^{|S|}.
\]

If the rooted child subtrees are \(T_1,\ldots,T_d\), then

\[
A_T=\prod_{j=1}^d(A_{T_j}+B_{T_j}),\qquad
B_T=x\prod_{j=1}^d A_{T_j},\qquad I_T=A_T+B_T.
\]

These identities hold in \(\mathbb Z_{\ge0}[x]\) and are the basis of both
discovery evaluators and exact verification.

## Scope and edge cases

- The conjecture concerns labelled or unlabelled trees equally, because the
  coefficient sequence is invariant under graph isomorphism.
- The one-vertex tree has sequence \((1,1)\) and is included.
- Forests are not part of Erdős #993 as formalized here.  Any forest
  enumeration is recorded only as adjacent evidence unless it yields a
  theorem used in the tree case.
- Log-concavity means \(i_k^2\ge i_{k-1}i_{k+1}\) at every internal index.
  Every positive finite log-concave sequence is unimodal. The implication is
  strict for tree independence sequences as witnessed by the exact order-26
  examples recorded in `literature/claim_ledger.md`; log-concavity is never
  silently substituted for the conjecture.
- A serialized tree certificate must specify an integer \(n\ge1\), vertex set
  \(\{0,\ldots,n-1\}\), and an edge list. An empty edge list alone does not
  distinguish the one-vertex tree from a missing vertex set.
