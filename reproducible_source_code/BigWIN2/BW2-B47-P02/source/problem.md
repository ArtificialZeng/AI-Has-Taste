# Precise problem statement

## Frozen source and necessary interpretation

The immutable source is `source.md`. The notation in that source calls
\(\mathcal L\) a family of Desarguesian MOLS, whereas the graph
\(\Gamma(H;\mathcal L)\) in Greaves--Tan is defined for a family of mutually
appropriate Latin squares (MALS). The precise reading used here is the
canonical one in Greaves--Tan, Proposition 3.1: apply their row--symbol
interchange to the standard Desarguesian MOLS and identify the resulting
complete MALS family with

\[
  \mathcal L=\{L_\alpha:\alpha\in\mathbb F_7^*\},\qquad
  L_\alpha(r,c)=\alpha(r-c)
  \quad(r,c\in\mathbb F_7).
\]

The field symbols are put in a fixed bijection with the paper's symbol labels
\(\{2,\ldots,8\}\). Rows and columns are likewise put in fixed bijections
with the paper's labels \(\{1,\ldots,7\}\). Without the MOLS-to-MALS
conversion, the displayed graph notation in the source is not defined by the
cited construction.

Fix the stated normalized Paley Hadamard matrix \(H\) of order 8, with first
row all ones. Write its other rows as \(h_t\), indexed by the seven field
symbols \(t\in\mathbb F_7\), and put \(B_t=h_t^{\mathsf T}h_t\). The argument
below does not depend on which fixed bijection assigns these seven rows to the
field symbols.

## Explicit graphs

For every deleted slope \(a\in\mathbb F_7^*\), let
\(S_a=\mathbb F_7^*\setminus\{a\}\) and define

\[
  G_a=\Gamma\bigl(H;\{L_\alpha:\alpha\in S_a\}\bigr).
\]

Its vertex set is

\[
  \Omega_a=S_a\times\mathbb F_7\times\{1,\ldots,8\},
\]

so \(|\Omega_a|=5\cdot7\cdot8=280\). For distinct slopes
\(\alpha,\beta\), let \(K_{\alpha\beta}(r,s)\) be the unique common symbol in
the row pair \((r,s)\). Directly from the displayed formula for the MALS,

\[
  K_{\alpha\beta}(r,s)
  =\frac{\alpha\beta(r-s)}{\beta-\alpha}.
\]

Two distinct vertices \((\alpha,r,x)\) and \((\beta,s,y)\) are adjacent
exactly in either of the following cases:

1. \(\alpha=\beta\) and \(r\ne s\) (the \(A_4\) relation); or
2. \(\alpha\ne\beta\) and
   \((B_{K_{\alpha\beta}(r,s)})_{xy}=+1\) (the \(A_2\) relation).

This is the adjacency-list specification to be used for exact verification.
Theorem 4.3 of Greaves--Tan, specialized to \(n=8,m=5\), supplies the stated
Neumaier parameters; Example 5.1 supplies the spectrum.

## Quantified target

Determine the cardinality of

\[
  \{[G_a]_{\cong}:a\in\mathbb F_7^*\}.
\]

For each resulting isomorphism class, designate a reproducible representative
(use the lexicographically ordered graph \(G_1\) if there is one class), give
its exact adjacency construction, and provide complete certificates: explicit
vertex permutations for every claimed isomorphism, or canonical-label and
stabilizer data with a verifier. In particular, decide the statement

\[
  \forall a,b\in\mathbb F_7^*\quad G_a\cong G_b.
\]

The six source graphs \(G_1,\ldots,G_6\) are these graphs after an arbitrary
fixed enumeration of \(\mathbb F_7^*\).

## Boundary cases and scope

- The deletion is exactly one member of the complete six-square family, so
  every retained family has exactly five MALS, as required by Theorem 4.3.
- Only the fixed order-8 Paley matrix and the complete order-7 Desarguesian
  family are part of the original claim. No assertion about other Hadamard
  matrices or MALS families is included.
- Relabeling the six slopes is not by itself a graph-isomorphism certificate;
  its action on all three vertex coordinates and on the common symbols must be
  checked.
- Shared parameters and spectrum are necessary invariants only and do not
  answer the isomorphism question.

## Source status and nearest prior result

Primary source inspected on 2026-09-06: Gary Greaves and Zhao Kuang Tan,
*Neumaier graphs of coherent rank five*, arXiv:2609.02218v1,
<https://arxiv.org/abs/2609.02218>. The local PDF has SHA-256
`2bb8a878244be3bdf7bfe57da4c1108612dda11e3ecd84f073cfddbe2e15ce9a`.
Relevant inspected locations are Proposition 3.1 (p. 3), the definition
\(A_\Gamma=A_2+A_4\) (p. 4), Theorem 4.3 (p. 6), and Example 5.1 and Question
5.4 (p. 7). Question 5.4 asks the broader dependence-on-inputs question but
does not state this six-deletion classification.

Accordingly the source status is **new-question**: it is a precise finite
specialization suggested by the primary paper's broad Question 5.4, not a
problem that the paper explicitly certifies as open. No claim of novelty or
priority is made from the bounded search.

Triage target: nearest prior result = Greaves--Tan's construction and common
invariants; proposed delta = exact classification of the six deletions;
verification route = prove the slope-scaling permutation preserves the two
adjacency relations, then independently regenerate all adjacency lists and
check the six certificates.
