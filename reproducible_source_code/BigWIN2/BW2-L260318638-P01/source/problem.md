# Precise problem reading

Provenance: `lit-260318638-p01-triage-b202d0ab48c6`.

## Ambient tessellation and definitions

Let \(\mathcal T\) be the tile set of the regular hyperbolic
\(\{4,5\}\)-tessellation: every tile is a regular geodesic square and exactly
five tiles meet at every tessellation vertex. The ambient space is the
hyperbolic plane \(\mathbb H^2\).

For a finite set of tiles \(A\subset\mathcal T\), write
\(U(A)=\bigcup_{T\in A}T\), and let the edge-dual graph \(G_A\) have vertex set
\(A\), with two vertices adjacent exactly when their tiles share a complete
tessellation edge. In the reading used here, a `polyform` is such a finite
\(A\) for which \(G_A\) is connected (equivalently, its interior is connected
under the convention of the source paper). Extra vertex-only contacts are
allowed, but do not supply connectivity.

A `hole` of \(A\) is a bounded connected component of
\(\mathbb H^2\setminus U(A)\). Let \(h(A)\) be the number of these components.
Each hole is regarded as the connected polyform of absent tessellation tiles
that it contains, and its area is its number of tiles. Define, for positive
integers \(h\),

\[
g_{4,5}(h)=\min\{|A|:A\subset\mathcal T\text{ is a polyform and }h(A)=h\}.
\]

## Quantified assertion

Decide the proposition

\[
\exists A\subset\mathcal T\quad
\bigl(A\text{ finite},\ |A|=16,\ G_A\text{ connected},\ h(A)=2\bigr).
\]

Thus a disproof has the universal scope: every edge-connected set of exactly
16 tiles in the actual \(\{4,5\}\) tessellation has a number of holes different
from two. The primary paper supplies a 17-tile two-hole construction and its
perimeter obstruction excludes 15 tiles. Consequently the frozen decision is
equivalent to deciding between \(g_{4,5}(2)=16\) and \(g_{4,5}(2)=17\).

## Necessary equality structure at 16 tiles

For a polyform \(A\), let \(b(A)=|E(G_A)|\), let \(p_o(A)\) and \(p_h(A)\)
be its outer and total hole perimeters, let \(\overline A\) be the polyform
obtained by filling every hole, and let \(\mathcal P_{\min}(N)\) be the minimum
perimeter of an \(N\)-tile \(\{4,5\}\)-polyform. Table 2 of
arXiv:2603.18638v1 gives \(M_{4,5}(16,2)=2\); by the definition of \(M\), this
is equivalent to \(\mathcal P_{\min}(18)=26\).

If a 16-tile, two-hole \(A\) exists, Lemma 2.1's counting inequalities give

\[
2\leq \frac{p_h(A)}4
=\frac{64-2b(A)-p_o(A)}4
\leq \frac{64-2(15)-26}{4}=2.
\]

Here \(b(A)\geq15\), while
\(p_o(A)=p_o(\overline A)\geq
\mathcal P_{\min}(|\overline A|)\geq\mathcal P_{\min}(18)=26\).
All inequalities must therefore be equalities. It follows that:

- \(b(A)=15\), so the connected graph \(G_A\) is a tree;
- \(p_h(A)=8\), so both holes have perimeter four and hence each consists of
  one tile; and
- \(|\overline A|=18\) and \(p_o(\overline A)=26\), so \(\overline A\) is an
  18-tile extremal animal.

Accordingly, the existence branch can be tested by finding an 18-tile
minimum-perimeter animal and deleting two suitable interior tiles, followed
by exact checks that the remaining 16 tiles are edge-connected and that the
two deleted tiles form exactly two distinct bounded complementary components.

## Scope and certificate standard

The target is only this endpoint decision, not a general formula for
\(g_{p,q}(h)\). An existence certificate must identify tiles in an exact
finite incidence patch of the \(\{4,5\}\) tessellation and permit independent
replay of tile count, edge connectivity, and complementary-component count.
A nonexistence certificate must cover every 16-tile polyform, through a proved
complete classification or exhaustive canonical augmentation with replayable
certificates. A search in a square grid, an arbitrary planar graph, a bounded
patch without a boundary-completeness proof, or the failure of a heuristic
generator does not decide the proposition.

