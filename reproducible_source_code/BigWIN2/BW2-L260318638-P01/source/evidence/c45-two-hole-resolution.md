# Resolution dossier for the 16-tile endpoint

Provenance: `lit-260318638-p01-research-f9d48755ee84` (research pass 1,
2026-09-10).

## Exact claim

There is no edge-connected 16-tile polyform with exactly two holes in the
regular \(\{4,5\}\) tessellation.  Together with the 17-tile construction in
Table 1 of Eldridge--Prabha--Roger--Roger--Roldan--Toala-Enriquez,
*Holey Hyperbolic Polyforms*, arXiv:2603.18638v1, this gives
\[
g_{4,5}(2)=17.
\]

## Proof

Suppose that \(A\) has 16 tiles and two holes.  Use the notation of Lemma 2.1
of arXiv:2603.18638v1: \(b(A)\) is the number of shared tile edges,
\(p_o(A)\) is the outer perimeter, \(p_h(A)\) is the total hole perimeter,
and \(\overline A\) is obtained by filling the holes.  From
\[
M_{4,5}(16,2)=\frac{16(4-2)+2-\mathcal P_{\min}^{4,5}(18)}4=2
\]
(Table 2), one gets \(\mathcal P_{\min}^{4,5}(18)=26\).  Lemma 2.1 then gives
\[
  8\le p_h(A)=64-2b(A)-p_o(A)
     \le64-2(15)-26=8.
\]
Consequently every inequality is an equality.  In particular \(b(A)=15\),
\(p_h(A)=8\), and \(p_o(A)=26\).  Each of the two holes has perimeter four.
The minimum perimeter is nondecreasing for \(p>3\), and a two-tile square
animal already has perimeter six, so both holes consist of one tile.  Hence
\(|\overline A|=18\), and \(\overline A\) is an 18-tile minimum-perimeter
animal.

We now identify that extremal animal.  In the notation of Section 6 of Malen,
Roldan, and Toala-Enriquez, *Extremal \(\{p,q\}\)-Animals*,
arXiv:2109.05331v1, let \(C_{4,5}(1)\) be two squares joined along an edge and
let \(C_{4,5}(2)\) be obtained by adding all tiles incident to its perimeter
vertices.  The boundary of the initial domino has six edges.  Across them lie
six new tiles.  Four boundary vertices are incident to one old tile, and the
two endpoints of the common edge are incident to two old tiles.  In a cyclic
star of five squares, after the two across-edge tiles are counted, saturation
therefore requires
\[
  4(5-1-2)+2(5-2-2)=10
\]
additional vertex-only tiles.  Thus \(|C_{4,5}(2)|=2+6+10=18\).

The sixteen new tiles form an edge-adjacency cycle.  Each of the six
across-edge tiles has three neighbours in \(C_{4,5}(2)\), each of the ten
vertex-only tiles has two, and each old domino tile has four.  It follows that
there are 23 shared edges, the perimeter is \(4\cdot18-2\cdot23=26\), and the
only fully edge-surrounded tiles are the two old domino tiles.  Theorem 6.4 of
arXiv:2109.05331v1 says that \(C_{p,q}(k)\) is the unique extremal animal at
its tile count.  Therefore \(\overline A\) is isometric to
\(C_{4,5}(2)\).

Finally, the two singleton holes of \(A\) are precisely the two tiles of
\(\overline A\setminus A\).  A deleted tile can be a singleton hole only if
all four of its edge-neighbours remain, so the two deleted tiles must be
distinct, non-edge-adjacent, fully surrounded tiles of \(\overline A\).  But
the only fully surrounded tiles of \(C_{4,5}(2)\) are the two central tiles,
and they share an edge.  Deleting both leaves one connected two-tile cavity,
not two holes.  This contradiction proves nonexistence at 16 tiles, and the
published 17-tile example proves the asserted value.

## Exact finite-incidence replay

Run:

```text
python3 evidence/verify_c45_domino_layer.py
```

The script uses only rational arithmetic in
\(\mathbb Q(\sqrt2,\sqrt5)\) and the faithful geometric representation of the
Coxeter group \([4,5]\).  Tile words and exact centre coordinates identify
the actual tessellation tiles, rather than an arbitrary planar graph.  It
checks the Coxeter relations, generates a held-out radius-four patch, selects
all tiles incident to the six vertices of a central domino, and returns the
complete tile adjacency and old-vertex incidence lists.  Its assertions give:

```text
tile_count = 18
interior_edge_count = 23
perimeter = 26
interior_tiles = [F, F0]
new_layer_is_16_cycle = true
only_interior_pair_is_edge_adjacent = true
deleting_only_interior_pair: remaining connected, one bounded hole
```

The exact BFS shell sizes through radius four are \(1,4,12,28,64\), and every
one of the six old vertices has exactly five incident selected tiles.  The
radius-four shell is not used to choose the result; it checks that the
radius-three incidence selection is closed as prescribed.

## Source and literature scope

The decisive primary-source statements are Lemma 2.1, Table 1, and Table 2 of
arXiv:2603.18638v1, and the definition preceding Theorem 6.4 plus Theorem 6.4
of arXiv:2109.05331v1.  A live exact-notation/title search on 2026-09-10 again
found the source paper but no later primary resolution; details of the broader
bounded screening are in `evidence/triage-literature.md`.  Search
non-detection is not a priority claim.  The proof above uses the cited
uniqueness theorem; the exact program independently replays only the finite
\(C_{4,5}(2)\) incidence calculation.
