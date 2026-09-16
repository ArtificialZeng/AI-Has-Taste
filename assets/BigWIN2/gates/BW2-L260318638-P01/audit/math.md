# Fresh mathematical referee report

Verdict: **accept**.

Job: `lit-260318638-p01-referee-8569d3d8ee55`  
Frozen snapshot: `1da216e17f600af5b3e7cd608dee41b0b7705ffc99ad85271bf205274989b640`

## Scope and integrity

I reviewed the frozen `resolution-paper` claim in its full scope: nonexistence
of an edge-connected 16-tile, two-hole polyform in the regular
\(\{4,5\}\)-tessellation, and hence (with the source paper's 17-tile example)
\(g_{4,5}(2)=17\). I recomputed the SHA-256 digest of every file named by the
snapshot; all eight file hashes agree with `audit/snapshot.json`.

The 2026 source paper defines holes as bounded complementary components,
states the 17-tile upper-bound construction in Theorem 1.2/Table 1, and gives
the relevant row
\(M(15,2)=1.5, M(16,2)=2.0, M(17,2)=2.0\) in Table 2. The 2021 source's
Theorem 6.4 says, at exactly the required subsequence sizes, that
\(C_{p,q}(k)\) is the unique extremal animal up to isometry. Its preceding
definition starts \(C_{p,q}(1)\) with an edge-adjacent domino and forms later
members by the same perimeter-saturation construction. Thus the cited theorem
does apply to \(C_{4,5}(2)\); the candidate does not incorrectly extrapolate
uniqueness to arbitrary spiral sizes.

## Reconstruction of the decisive argument

Assume that \(A\) has 16 tiles and two holes. With \(b\) the number of shared
edges and \(p_o,p_h\) its outer and hole perimeters, Lemma 2.1 gives the
identities and bounds
\[
 p_h=64-2b-p_o,\qquad b\ge 15,\qquad
 p_o=P(\overline A)\ge P_{\min}(|\overline A|)
       \ge P_{\min}(18)=26.
\]
Here \(|\overline A|\ge18\) because filling each of two holes adds at least one
tile, and monotonicity of minimum perimeter for \(p=4\) is one of the cited
isoperimetric facts. Also each hole has boundary length at least four, so
\(p_h\ge8\). Consequently
\[
 8\le p_h\le64-30-26=8.
\]
Both endpoint inequalities are equalities: \(b=15\), \(p_o=26\), and
\(p_h=8\). In particular each hole has perimeter four. A hole containing at
least two edge-connected absent tiles has perimeter at least
\(P_{\min}(2)=6\), by the same monotonicity, so each hole is exactly one tile.
It follows that \(|\overline A|=18\), and \(\overline A\) is an 18-tile
minimum-perimeter animal.

I separately checked the local count for \(C_{4,5}(2)\). Saturating the six
vertices of the central domino adds the six tiles across its boundary edges
and ten vertex-only tiles, for 18 tiles total. The frozen exact Coxeter
certificate confirms in the actual \(\{4,5\}\) tessellation that this animal
has 23 shared edges and perimeter
\(4\cdot18-2\cdot23=26\). Therefore Theorem 6.4 identifies every 18-tile
extremal animal, including \(\overline A\), with \(C_{4,5}(2)\).

The same exact incidence data show that the only tiles of
\(C_{4,5}(2)\) with all four edge-neighbours present are the two central
domino tiles, and those tiles share an edge. But a deleted tile representing
a singleton bounded hole must have all four edge-neighbours remaining, and
the two deleted singleton holes must be non-edge-adjacent. Thus no choice of
two tiles in \(C_{4,5}(2)\) can yield the hypothesized two singleton holes.
This contradiction covers every 16-tile candidate through the published
uniqueness theorem, rather than through an incomplete search.

## Exact-certificate and adversarial checks

I ran `evidence/verify_c45_domino_layer.py` under ordinary assertion-enabled
Python. It completed and verified the Coxeter relations, exact
\(\mathbb Q(\sqrt2,\sqrt5)\) tile identifiers, shell counts
\(1,4,12,28,64\), five selected tiles at each old vertex, 18 selected tiles,
23 shared edges, perimeter 26, and exactly the central domino as the set of
zero-exposure tiles. I then traversed the serialized adjacency lists with a
separate check: adjacency is symmetric, all 18 vertices are connected, the
16 noncentral tiles induce one connected 16-cycle, and all edge, exposure,
and interior-tile counts recompute correctly.

Some summary booleans emitted by the certificate are literal output values
rather than themselves being assertions (notably the residual-connectivity
label). This does not create a mathematical gap: residual connectivity was
independently recovered from the full adjacency lists, while the decisive
nonexistence step needs only the asserted facts that the central pair is the
entire set of fully surrounded tiles and is edge-adjacent.

I also checked the likely failure points: no empty-domain or division issue
occurs; all quantities are finite integers; no limit or compactness argument
is used; filling holes preserves the outer boundary; the singleton inference
uses the actual tile-connected hole convention; and the conclusion does not
treat the authors' heuristic generator as exhaustive. Vertex-only tile
contacts are allowed throughout but are never used as edge connectivity.

## Source comparison and limitations

The precise delta from the 2026 paper is the single unresolved endpoint
between its 15-tile obstruction and 17-tile construction. The proof combines
the equality case of that paper's bound with the 2021 unique-extremal theorem
at the specific \(C_{4,5}(2)\) size. The frozen bounded literature screening
found no later primary source resolving this cell as of 2026-09-10; that
non-detection supports the stated context but is not a claim of priority.

There is no unresolved mathematical gap in the frozen claim. The exact
scope, correctness/evidence, and resolution contribution therefore pass.
