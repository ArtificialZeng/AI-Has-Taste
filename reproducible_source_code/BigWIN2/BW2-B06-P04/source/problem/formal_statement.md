# Formal statement

Status: **locked, version 1 (2026-08-30), before computational discovery**.

## Definitions

All graphs below are finite, undirected, and simple. A graph \(G=(V,E)\) is
**Laman** if
\[
 |E|=2|V|-3
 \quad\text{and}\quad
 |E(G[X])|\le 2|X|-3
 \quad(2\le |X|\le |V|).
\]
By the Pollaczek--Geiringer--Laman theorem, this is equivalent to generic
minimal rigidity in the Euclidean plane.

A red--blue edge-colouring \(c:E\to\{r,b\}\) is a **NAC-colouring** if it is
surjective and every cycle is monochromatic or contains at least two edges of
each colour. Let
\[
  \operatorname{NAC}_{\#}(G)
  :=\frac{\#\{\text{NAC-colourings of }G\}}2.
\]
The division only identifies a colouring with its global red--blue swap; graph
automorphisms are **not** quotiented.

Let \(P_3=C_3\square K_2\) be the triangular prism. A \(P_3\)-subgraph means
an ordinary (not necessarily induced) subgraph isomorphic to \(P_3\). In a
Laman graph such a copy is automatically induced, because it already has nine
edges on six vertices.

Define \(\mathcal G_{sc}\) recursively as follows: \(K_2\in\mathcal G_{sc}\);
from a member of \(\mathcal G_{sc}\), glue a triangle or a triangular prism
along an edge or along a triangle. Repeated vertices and edges in the gluing
interface are identified, and the result is required to be a simple graph.

A **0-extension** adds a new vertex adjacent to exactly two old vertices. It is
**open** when those two old vertices are non-adjacent at that step. A graph is
a 0-extension graph if it can be obtained from \(K_2\) by 0-extensions. The
phrase “with exactly one open step” means that such a construction exists with
exactly one open step. The research will separately prove that the number of
open steps is construction-independent and equals
\((|V|-2)-t(G)\), where \(t(G)\) is the number of triangles.

## Locked finite proposition

For every simple graph \(G\) with \(|V(G)|=11\), if \(G\) is Laman (hence
\(|E(G)|=19\)), then
\[
\operatorname{NAC}_{\#}(G)=1
\quad\Longleftrightarrow\quad
\begin{cases}
G\in\mathcal G_{sc}\text{ and }G\text{ has exactly one }P_3\text{-subgraph},
\\[2mm]
\text{or }G\text{ is a 0-extension graph with exactly one open step}.
\end{cases}
\]

The quantifier is over labelled graphs, but an exhaustive computation may use
one representative of each isomorphism class because every predicate above is
isomorphism-invariant.

## Conventions and edge cases

- Empty and monochromatic edge-colourings are not NAC-colourings.
- A cycle is a simple cycle.
- A stable cut \(S\) means an independent vertex set for which \(G-S\) has at
  least two connected components. It will be used only through the published
  characterization of \(\mathcal G_{sc}\) for graphs with \(2|V|-3\) edges.
- No floating-point calculation is relevant to the locked proposition.
- The full infinite Conjecture 6.1 is not the endpoint of this project; the
  endpoint is its complete, exact \(n=11\) instance.

## Source repair

The source wording says the primary item is an arXiv paper and calls the
11-vertex case the first unverified order. The current primary record is now a
published Journal of Graph Theory article (online 2026-06-01,
DOI 10.1002/jgt.70064). It still explicitly reports verification only through
10 vertices, so 11 remains the first order for which the classification itself
is not claimed. However, that article already reports NAC-count distributions
for all 11- and 12-vertex minimally rigid graphs; our finite classification
must therefore distinguish a new family-membership certification from an
already reported NAC-count computation.
