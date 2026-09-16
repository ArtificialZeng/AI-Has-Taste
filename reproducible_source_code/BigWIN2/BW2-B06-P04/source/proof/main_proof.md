# Certified eleven-vertex theorem

## Theorem

For every 11-vertex Laman graph \(G\),
\(\operatorname{NAC}_{\#}(G)=1\) if and only if either

1. \(G\in\mathcal G_{sc}\) and \(G\) contains exactly one triangular-prism
   subgraph, or
2. \(G\) is a 0-extension graph with exactly one open step.

## Lemma 1: connectivity test for NAC-colourings

For a surjective red--blue edge-colouring, the NAC cycle condition is
equivalent to both of the following:

- no blue edge has endpoints joined by a red path;
- no red edge has endpoints joined by a blue path.

Indeed, an offending edge together with a shortest opposite-colour path is an
almost-monochromatic cycle. Conversely, deleting the unique exceptional edge
from an almost-monochromatic cycle leaves such an opposite-colour path. This
is the exact condition used by both certificate implementations, once through
disjoint sets and once through bitset transitive closure.

## Lemma 2: open steps are an invariant

In any 0-extension construction from \(K_2\), every closed step creates exactly
one new triangle and every open step creates none. Conversely, every triangle
of the final graph has a unique last-added vertex; the step adding that vertex
was closed and created that triangle. Hence closed steps are in bijection with
triangles. Since an \(n\)-vertex construction has \(n-2\) steps,
\[
  \#\{\text{open steps}\}=n-2-t(G).
\]
Thus “exactly one open step” is independent of the construction order. At
\(n=11\), it is equivalent to a reverse 0-extension ordering together with
exactly eight triangles.

## Lemma 3: the family-B graphs have a unique NAC-colouring

Before the sole open step, all steps are closed, so the current graph is a
2-tree. Every triangle in a NAC-colouring is monochromatic, and the closed
construction propagates this colour across all edges of the 2-tree. Say this
colour is blue. The open step adds a vertex \(x\) adjacent to two non-adjacent
vertices \(u,v\). The new edges cannot both be blue, since all later closed
steps only propagate existing colours and the final colouring must be
surjective. Exactly one new red edge is also impossible: a blue \(u\)-\(v\)
path in the connected 2-tree, together with \(xu,xv\), would be an
almost-blue cycle. Therefore both new edges are red.

This colouring is NAC: a cycle through \(x\) contains its two red edges and a
blue \(u\)-\(v\) path of length at least two; all other cycles are blue. Each
subsequent closed step attaches a triangle along an old edge, which forces and
uniquely determines the two new edge colours. The standard cycle replacement
argument shows that this extension preserves the NAC property. Hence the
final graph has exactly one NAC-colouring modulo global colour swap.

If there is no open step, the same triangle propagation makes every edge the
same colour. Thus a 2-tree has no NAC-colouring.

## Lemma 4: the family-A graphs have a unique NAC-colouring

For the recursive class \(\mathcal G_{sc}\), include the two monochromatic
colourings temporarily and fix the colour of an interface edge. Gluing a
triangle along an edge or a triangle introduces no choice, since its triangle
is forced monochromatic. Gluing a triangular prism introduces exactly one
binary choice: the prism is either monochromatic or takes its unique
NAC-colouring compatible with the fixed interface colour. Cycles meeting both
pieces split along the clique interface, so these compatible choices preserve
the no-almost-monochromatic-cycle condition. Induction gives
\[
  \operatorname{NAC}_{\#}(G)=2^p-1,
\]
where \(p\) is the number of prism attachments. This is also the positive
calculation recorded immediately after Conjecture 6.1 in the primary paper.

Every attached prism remains a prism subgraph, and different prism attachments
have new vertices and hence give distinct copies. A construction using no
prism is a 2-tree and cannot contain a prism (a 2-degenerate graph has no
subgraph of minimum degree three). Consequently, a member of
\(\mathcal G_{sc}\) with exactly one prism subgraph has \(p=1\), and its
\(\operatorname{NAC}_{\#}\) value is one.

## Exhaustive converse at order eleven

The independent universe cross-check in
`certificates/generation_crosscheck.txt` establishes 2,039,273 nonisomorphic
11-vertex Laman graphs. The exact four-way certificate contains one row for
each graph. The independent verifier checked the following exhaustive
partition:

| certificate case | number of graphs | exact implication |
|---|---:|---|
| `A` | 1,196 | no stable cut and one prism; hence family A and unique NAC |
| `B` | 22,303 | 0-extension graph, one open step; hence unique NAC |
| `T` | 2,171 | 2-tree; hence zero NAC |
| `2` | 2,013,603 | two literal inequivalent NAC-colourings; hence at least two |
| **total** | **2,039,273** | all isomorphism classes |

For an `A` row, direct stable-cut enumeration plus the published corrected
characterization of graphs with \(2n-3\) edges and no stable cut establishes
membership in \(\mathcal G_{sc}\); the verifier also directly counts exactly
one triangular-prism subgraph. For a `2` row, the two red-edge masks are
checked independently by Lemma 1 and checked not to be global colour swaps.
Every row therefore proves either the right-hand family condition and
uniqueness, or failure of uniqueness. This proves the finite theorem.

No proof assistant was used.
