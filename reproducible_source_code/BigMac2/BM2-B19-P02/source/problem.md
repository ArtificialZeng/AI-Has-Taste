# Precise problem statement

## Frozen original assertion

The assertion to be proved or disproved is, verbatim from `source.md`:

> 证明或反驳：每个恰有 24 个顶点且最小度至少 3 的有限简单图，都含有长度为
> `4`、`8` 或 `16` 的简单圈。

No correction or weakening of this assertion is adopted here.

## Formal reading

Let \(G=(V,E)\) be a finite simple undirected graph.  For an integer
\(\ell\geq 3\), say that \(G\) contains a simple cycle of length \(\ell\) if
there are pairwise distinct vertices
\(v_0,\ldots,v_{\ell-1}\in V\) such that
\(\{v_i,v_{(i+1)\bmod \ell}\}\in E\) for every
\(i\in\{0,\ldots,\ell-1\}\).

The frozen claim is

\[
\forall G\;\Bigl(
  \bigl[G\text{ is finite, simple, and undirected},\quad
  |V(G)|=24,\quad
  \delta(G):=\min_{v\in V(G)}\deg_G(v)\geq 3\bigr]
  \Longrightarrow
  \exists \ell\in\{4,8,16\}\;
  \bigl[G\text{ contains a simple cycle of length }\ell\bigr]
\Bigr).
\]

Equivalently, its negation asks for one finite simple undirected graph \(G\)
with exactly 24 vertices and minimum degree at least 3 that has no simple
cycle of length exactly 4, exactly 8, or exactly 16.

## Definitions, quantifiers, and boundary scope

- “Simple graph” excludes loops and parallel edges.  Edges are undirected.
- “Exactly 24 vertices” is not “at most 24 vertices.”  Vertex labels, if used
  in a certificate, carry no mathematical significance.
- The minimum-degree condition is vertexwise: every vertex has degree at least
  3.  The graph need not be 3-regular.
- “A cycle of length 4, 8, or 16” is an inclusive existential alternative: at
  least one cycle of one of those exact lengths suffices.
- A simple cycle need not be induced; chords do not invalidate it.
- No connectedness, planarity, bipartiteness, regularity, or other unstated
  hypothesis is imposed.  Cycles of all other lengths are allowed.

## Nearest supplied result and proposed delta

According to the literature description in `source.md` (not independently
re-audited in this bounded statement-normalization job), Garcia,
*Small graphs without power-of-two cycles: a lower bound of 24, a correction
to a construction of Exoo, and explicit bounds for f(k)*,
arXiv:2609.04686v1, certifies the corresponding general-graph range through
23 vertices and covers the 24-vertex cubic subclass, while leaving the full
24-vertex \(\{4,8,16\}\) decision incomplete.

Thus the nearest supplied prior result is the 23-vertex general case together
with the 24-vertex 3-regular case.  The proposed delta is to settle all
remaining 24-vertex graphs with minimum degree at least 3 (necessarily the
non-cubic cases, hence with at least one vertex of degree at least 4).

## Required resolution evidence

A disproof must provide a complete adjacency list or graph6 string and an
independent verification of simplicity, order 24, minimum degree at least 3,
and absence of cycles of each of the three exact lengths.  Under the supplied
task specification, a positive computational resolution must provide a
complete, independently checkable UNSAT certificate for the full quantified
class.  These certificate requirements govern acceptance of a resolution;
they do not alter the logical statement above.
