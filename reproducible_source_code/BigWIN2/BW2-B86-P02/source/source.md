# Frozen source problem: the first disconnected counterexample to Pan's automorphism conjecture

Canonical id: win-00086-p02
Frozen on: 2026-09-10 (Asia/Shanghai)
Primary source:
- Junyao Pan, *Automorphism group of the graph A(n,k,r)*,
  arXiv:2407.19745v1, definition and Question 1.1 on PDF p.1,
  Theorem 1.2 on PDF p.2, Proposition 2.7 on PDF pp.5--6, and
  Conjecture 3.1 on PDF p.6.

## Definitions

For `0 <= t <= n-2`, let `F_t` be the set of permutations in `S_n` with
exactly `t` fixed points.  The Cayley graph `Cay(S_n,F_t)` is isomorphic to
the arrangement graph `A(n,n,n-t)`, whose vertices are permutations written
as ordered `n`-tuples and whose edges join tuples differing in exactly
`n-t` positions.

Pan's Conjecture 3.1 asserts, for every `n>2` and every such `t`, that

```
Aut(Cay(S_n,F_t)) = [R(S_n) semidirect Inn(S_n)] semidirect C_2,
```

with the final involution induced by inversion.

## Statement

Determine the graph and full automorphism group at the first parameter not
covered by the source's two proved extreme families, namely `n=4`, `t=1`:

```
A(4,4,3) is isomorphic to Cay(S_4,F_1).
```

In particular, prove or disprove Conjecture 3.1 at this parameter.  If the
graph decomposes as two copies of `K_{4,4,4}`, prove that decomposition and
derive the full automorphism group rather than merely exhibiting one extra
automorphism.

## Scope and contribution boundary

The source proves the derangement (`t=0`) and transposition (`t=n-2`)
families; it does not assume connectedness in Conjecture 3.1.  The proposed
fixed case must be checked against any erratum, later arXiv version, or later
paper before novelty is asserted.

A complete certificate consists of the eight three-cycles in `S_4`, the
parity components, the three cosets of the normal Klein four subgroup inside
each component, and an exact adjacency check showing that each component is
`K_{4,4,4}`.  The automorphism-group order and wreath-product structure must
then follow from the standard full automorphism group of a disjoint union of
two complete tripartite graphs.  A graph-software group order alone is not a
proof.

Any manuscript must cite the primary source and the relevant Cayley-graph
automorphism literature needed to support its context and group formula, in
addition to one or two genuinely relevant user-Excel papers when available.
The user-library minimum never limits the rest of the bibliography and must
not be met with unrelated references.

This file is immutable.  A modified conjecture restricted to connected
Cayley graphs or to connection sets generating `S_n` is a separate claim.

