# Precise problem

## Frozen original claim

The immutable statement is `source.md` (SHA-256
`ebbe264caf080f8158cce54870acfd5a01eddf57ddb0a704f6da2eaa51da5eab`). Its
claim is

\[
\bar\chi_{\ge}(H(3,3))=4.
\]

No correction or weakening of that claim is made here.

## Definitions and quantifiers

- Let \([3]=\{1,2,3\}\), and let \(H(3,3)\) be the finite simple undirected
  graph with vertex set \(V=[3]^3\). Distinct vertices \(x=(x_1,x_2,x_3)\)
  and \(y=(y_1,y_2,y_3)\) are adjacent exactly when
  \(\lvert\{j:x_j\ne y_j\}\rvert=1\). Thus
  \(H(3,3)=K_3\square K_3\square K_3\), and every vertex has exactly six
  neighbors.
- For an integer \(p\ge 1\), a majority \(C\) \(p\)-coloring is a
  **surjection** \(\phi:V\to[p]\) such that, for every \(v\in V\),
  \[
  \bigl|\{u\in V:u\sim v\text{ and }\phi(u)=\phi(v)\}\bigr|\ge 3.
  \]
  “Majority” is therefore read weakly: exactly half of the six neighbors is
  allowed. This is not a proper-coloring condition.
- Define
  \[
  \bar\chi_{\ge}(H(3,3))=
  \max\{p\in\mathbb Z_{\ge1}:\text{a majority \(C\) \(p\)-coloring exists}\}.
  \]
  The maximum is well-defined: the all-one coloring is valid, while
  surjectivity forces \(p\le27\).

Equivalently, the color classes form a partition
\(V=S_1\sqcup\cdots\sqcup S_p\) into nonempty sets satisfying
\(\delta(H(3,3)[S_i])\ge3\) for every \(i\).

## Exact proof-or-disproof target

To prove the displayed equality, one must establish both:

1. there exists such a partition into four nonempty color classes; and
2. no such partition into five nonempty color classes exists.

Excluding five colors excludes every \(p\ge5\): merging two nonempty color
classes preserves the same-color-neighbor inequalities and surjectivity, so
any coloring with more than five colors could be merged repeatedly to a
five-coloring. A disproof requires either a valid coloring using at least five
colors or a proof that even four colors are impossible.

The scope is only this 27-vertex graph and this weak-majority, surjective
definition. No assertion about other Hamming graphs, non-surjective maps, or
proper/list colorings is included.

## Source-status baseline

The immutable source attributes the bounds
\(3\le\bar\chi_{\ge}(H(3,3))\le5\) and the open status of the equality to
Bujtás--Dettlaff--Furmańczyk--Laskowska, arXiv:2608.27669v1, Proposition 6(ii)
and Open Problem 3. Those literature assertions have not been independently
checked in this bounded interpretation job, so the original claim remains
unresolved at triage.
