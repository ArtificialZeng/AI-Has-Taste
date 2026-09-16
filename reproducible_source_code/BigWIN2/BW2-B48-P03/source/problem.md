# Precise problem statement

## Provenance and frozen source

Triage job: `win-00048-p03-triage-dadbdbe9b617`.

The immutable statement is `source.md`. This file fixes its mathematical
reading; it does not replace or modify the source.

## Definitions

For an integer \(n\geq 1\), write \([n]=\{1,\ldots,n\}\) and define the path

\[
P_n=\bigl([n],\{\{i,i+1\}:1\leq i<n\}\bigr).
\]

For finite simple graphs \(G=(V_G,E_G)\) and \(H=(V_H,E_H)\), their Cartesian
product \(G\square H\) has vertex set \(V_G\times V_H\), with distinct
\((u,x)\) and \((v,y)\) adjacent exactly when either \(u=v\) and
\(\{x,y\}\in E_H\), or \(x=y\) and \(\{u,v\}\in E_G\).

An orientation of a finite simple graph chooses exactly one direction for every
edge. It is *acyclic* if the resulting directed graph has no directed cycle.
Let \(\mathcal{AO}(G)\) be the set of all acyclic orientations and

\[
\psi(G)=|\mathcal{AO}(G)|.
\]

For every integer \(k\geq1\), put

\[
G_k=P_3\square P_{2k+1}.
\]

Thus \(V(G_k)=[3]\times[2k+1]\), and explicitly

\[
\begin{aligned}
E(G_k)={}&\{\{(i,j),(i+1,j)\}:i\in\{1,2\},\ j\in[2k+1]\}\ \\
&\cup\{\{(i,j),(i,j+1)\}:i\in[3],\ 1\leq j<2k+1\}.
\end{aligned}
\]

It has \(6k+3\) vertices and \(10k+2\) edges; in particular, its edge count
is even.

## Frozen claim, with quantifiers

Determine the truth of

\[
\boxed{\forall k\in\mathbb Z\ (k\geq1\Longrightarrow
       \psi(G_k)\equiv2\pmod4).}
\]

Equivalently, for every odd integer \(m\geq3\), the number of acyclic
orientations of \(P_3\square P_m\) lies in \(4\mathbb Z+2\). The case \(k=1\)
is the \(3\times3\) grid; \(k=0\) and all even lengths are outside the claim.

By Stanley's acyclic-orientation evaluation,

\[
\psi(G)=(-1)^{|V(G)|}\chi_G(-1).
\]

Here \(|V(G_k)|=6k+3\) is odd, so \(\psi(G_k)=-\chi_{G_k}(-1)\). Since
\(-2\equiv2\pmod4\), the frozen claim is equivalently
\(\chi_{G_k}(-1)\equiv2\pmod4\) for every \(k\geq1\).

## Scope and success conditions

The target is only this width-3 infinite family. It does not assert the cited
conjecture for all odd widths, and it says nothing about even grid dimensions.
Non-Hamiltonicity of \(\mathcal{AO}(G_k)\) follows from the congruence and the
even edge count, but proving non-Hamiltonicity by another route would not prove
the frozen claim.

A proof must cover every integer \(k\geq1\). A disproof requires one explicit
\(k\geq1\) and an exact, independently reproducible count showing
\(\psi(G_k)\not\equiv2\pmod4\). By the cited Lemma 3.1, every value is even, so
an exact residue \(0\) is the only possible counterexample residue; an odd
residue signals a counting error.

## Source status and nearest prior work

Retrieved 2026-09-06 from the official arXiv v1 record:

- L. Mühlherr and G. Poullot, *Hamiltonicity of graphs of acyclic orientations
  and acyclic polynomials*, [arXiv:2609.02249v1](https://arxiv.org/abs/2609.02249v1),
  submitted 2026-09-02. Lemma 3.1 says \(\psi(G)\) is even for every graph;
  Lemma 3.2 gives the stated non-Hamiltonicity consequence. Example 3.13(8)
  labels \((3,3),(3,5),(3,7)\) as computer experiments with residue \(2\).
  Conjecture 1(1) states the containing assertion for every odd
  \(m,n\geq3\). Section 3.2, immediately after the conjecture, records
  \(\psi(G)=\psi(G/e)+\psi(G\setminus e)\).
- J. Salas and A. D. Sokal, *Transfer Matrices and Partition-Function Zeros for
  Antiferromagnetic Potts Models I. General Theory and Square-Lattice Chromatic
  Polynomial*, [arXiv:cond-mat/0004330](https://arxiv.org/abs/cond-mat/0004330),
  studies chromatic polynomials for free-boundary \(m\times n\) square-lattice
  strips with \(m\leq8\) and arbitrary \(n\) using transfer matrices. This is a
  relevant technical antecedent, but the inspected abstract does not state the
  present modulo-4 claim; its width-3 formulas/data still require direct
  inspection before any novelty claim.

Accordingly, the source status is **open-supported relative to the inspected
2026 source**, while priority of a width-3 resolution is not yet established.
The nearest explicit statement is the broader Conjecture 1(1), and the proposed
delta is a proof or counterexample for its complete width-3 odd-length subfamily.

## Bounded verification route

The first falsification test is an exact count for the first unreported member
\(G_4=P_3\square P_9\), cross-checked by (i) deletion--contraction and (ii) an
independently implemented chromatic-polynomial evaluation at \(-1\). If its
residue is \(0\), the frozen claim is disproved. If it is \(2\), the proof route
is to derive a complete finite boundary-partition transfer system, reduce it
modulo \(4\), and certify the odd-length orbit and output map for all iterates.
