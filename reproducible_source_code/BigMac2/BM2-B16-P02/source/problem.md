# Precise reading of the problem

## Parameters and conventions

- Quantifiers: let `n,m` be arbitrary integers with `n,m >= 2`, and let `K`
  be an arbitrary field. Any claimed formula depending only on `n,m` must
  therefore either hold in every characteristic or explicitly identify and
  prove any characteristic dependence.
- Let
  \[
  V=\{x_1,\ldots,x_n,y_1,\ldots,y_m\}
  \]
  and let `B(n,m)` be the finite simple graph with edges
  \[
  \{\{x_i,y_1\}:1\le i\le n\}\ \cup\
  \{\{y_j,y_{j+1}\}:1\le j<m\}.
  \]
  Write `d_B` for ordinary shortest-path distance in this graph.
- The notation `B(n,m)^3` means the **third graph power**, not the third
  ordinary or symbolic power of an ideal: it is the simple graph `H` on `V`
  in which distinct vertices `u,v` are adjacent exactly when
  `d_B(u,v) <= 3`.
- The ring
  \[
  S=K[x_1,\ldots,x_n,y_1,\ldots,y_m]
  \]
  has its standard grading, with every variable of degree one.

## The ideal

For `v in V`, set
\[
N_H[v]=\{w\in V:d_B(v,w)\le 3\},\qquad
q_v=\prod_{w\in N_H[v]}w,
\]
and define
\[
I_{n,m}=NI(B(n,m)^3)=(q_v:v\in V)\subseteq S.
\]
“Take the minimal monomial generating set” is read as deleting duplicate
generators and every `q_v` divisible by another one; it does not define a
different ideal.

For clarity, put `X=x_1\cdots x_n` and
`Y[a,b]=y_a y_{a+1}\cdots y_b`. Directly from the distance definition,
\[
q_{x_i}=X\,Y[1,\min(m,3)]
\]
for every `i`, while
\[
q_{y_j}=
\begin{cases}
X\,Y[1,\min(m,j+3)],&1\le j\le 3,\\
Y[j-3,\min(m,j+3)],&4\le j\le m.
\end{cases}
\]
Consequently the inclusion-minimal generating set is
\[
G(I_{n,m})=
\begin{cases}
\{X\,Y[1,m]\},&2\le m\le3,\\
\{X\,Y[1,3]\}\cup
\{Y[a,a+6]:1\le a\le m-7\}\cup
\{Y[m-3,m]\},&m\ge4,
\end{cases}
\]
where the middle set is empty when `m <= 7`. Indeed, the first generator
divides the closed-neighborhood monomials for `y_1,y_2,y_3`; among the
right-end truncated path neighborhoods, `q_{y_m}=Y[m-3,m]` divides the
other three; the displayed seven-variable windows and the four-variable
tail have no remaining divisibility relations. In particular, for `m=2,3`
the graph cube is complete and `I_{n,m}` is principal. This structural
description is part of the frozen mathematical reading and must be checked
by any subsequent computation.

## Requested theorem

Determine finite, explicit, piecewise closed-form expressions (not merely an
algorithm or recurrence) for every `n,m >= 2` and every field `K` for
\[
\operatorname{pd}_S(S/I_{n,m}),\qquad
\operatorname{reg}_S(S/I_{n,m}),\qquad
\operatorname{ht}(I_{n,m}).
\]
Here `pd` is the length of a minimal graded free resolution,
`reg(S/I)=max{j-i: beta_{i,j}(S/I) != 0}`, and `ht` is the minimum height of
a prime containing `I`. The formula must explicitly list every exceptional
small value of `m` not covered by its eventual cases, with the cutoff and
all residue classes stated rather than inferred from examples.

Also determine exactly the set of pairs `(n,m)` for which `S/I_{n,m}` is
Cohen--Macaulay, meaning
\[
\operatorname{depth}_S(S/I_{n,m})=
\dim(S/I_{n,m}).
\]
By Auslander--Buchsbaum in this polynomial ring, this is equivalently the
equality
`pd_S(S/I_{n,m}) = ht(I_{n,m})`; this equivalence does not replace the need
to prove the two invariant formulas.

The requested proof must cover all endpoints and exceptional cases. Finite
Betti tables may motivate a formula but are not a proof; if a mapping-cone
recursion is used, its exact colon ideals and minimality/no-cancellation at
every step must be established.

## Scope and nearest prior result

The cited paper by Anda Olteanu and Oana Olteanu, *On the closed neighborhood
ideal of the square of broom and double broom graphs*, arXiv:2609.04831v1
(4 September 2026), defines the same broom family and treats `NI(B(n,m)^2)`,
not the graph cube above. Its Theorem 2.3 supplies square-of-path invariants;
Theorems 3.7--3.8 and Corollary 3.9 give the square-of-broom invariants and
Cohen--Macaulay classification. Thus the nearest identified result is the
radius-two/square case; the proposed delta is the radius-three/cube family,
whose minimal path windows have length seven and whose terminal generator
has length four.

As of 8 September 2026, narrowly targeted searches for the exact cube/third
graph-power assertion located the cited square paper and general closed
neighborhood-ideal papers, but no primary source settling this cube family.
This is a limited literature screen, not a claim of novelty or proof that the
problem is open. Source status remains `status-uncertain`.

