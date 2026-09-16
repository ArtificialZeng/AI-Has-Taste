# win-00069-p04 — Octahedral tilings of ideal right-angled \(\mathrm{SW2}\)-polyhedra

## Immutable primary-source record

- Primary source: Daniel Allcock, Pat Devlin, Anna Felikson, Alex Kontorovich, and Ian Whitehead, *Arithmetic Polyhedra*, arXiv:2609.05349v1 [math.MG; cross-listed math.NT].
- Official abstract: <https://arxiv.org/abs/2609.05349v1>.
- Official HTML: <https://arxiv.org/html/2609.05349v1>.
- Definition location: §2.1, Definition 2.1.
- Nearest-result location: §7.4, Proposition 7.10 and its proof.
- Frozen conjecture location: §7.4, Conjecture 7.11; §8 item 1 repeats it as a natural next step.
- Source-stated status: Conjecture 7.11 explicitly states the frozen tiling assertion.
- Access record: the official arXiv abstract and HTML were read directly. No PDF, figures, Coxeter data, or other source file was downloaded into staging.

## Exact definitions and frozen assertion

The source always takes a hyperbolic polyhedron to be convex and, unless otherwise specified, finite-volume. For a hyperbolic Coxeter polyhedron \(\mathcal P\), its reflection group \(\Gamma(\mathcal P)\) tiles \(\mathbb H^3\) by reflected copies of \(\mathcal P\).

Definition 2.1 says that \(\mathcal Q\) is a \(\mathcal P\)-polyhedron when \(\mathcal Q\) is a convex hyperbolic polyhedron that is a finite union of copies of \(\mathcal P\) in this reflective tiling. The source distinguishes this from a general, potentially non-reflective tiling by isometric copies.

Fix
\[
\mathcal P=\mathrm{SW2},
\]
the indicated Scharlau–Walhorn Coxeter polyhedron, and let
\(\mathcal O\) be the ideal, right-angled hyperbolic octahedron. Prove or disprove Conjecture 7.11:

> Every ideal, right-angled \(\mathcal P\)-polyhedron is tiled by \(\mathcal O\).

The conclusion uses the source's more general notion of tiling: a union of isometric copies with disjoint interiors; it does not silently add a face-to-face or reflective requirement absent from the conjecture.

An acceptable disproof is one explicit convex finite-volume ideal right-angled \(\mathcal P\)-polyhedron, given as a finite union of chambers in the reflective \(\mathcal P\)-tiling, together with a proof that no tiling by isometric copies of \(\mathcal O\) exists.

## Nearest source result and precise delta

The source constructs \(\mathcal O\) from \(\mathcal P=\mathrm{SW2}\). Cutting \(\mathcal O\) by two specified symmetry planes yields
\(\frac12\mathcal O\) and
\(\frac14\mathcal O\); the quarter-octahedron is a right-angled triangular bipyramid with two finite vertices and three ideal vertices.

Proposition 7.10 proves:

1. \(\mathcal O\) is a \(\mathcal P\)-polyhedron.
2. Every ideal, right-angled \(\mathcal P\)-polyhedron \(\mathcal Q\) is tiled by \(\frac14\mathcal O\).
3. Depending on its face types, \(\mathcal Q\) has canonical decompositions into copies of \(\frac14\mathcal O\), \(\frac12\mathcal O\), and \(\mathcal O\).

Immediately after Conjecture 7.11, the authors state that Proposition 7.10 reduces the conjecture to showing that every ideal polyhedron tiled by
\(\frac14\mathcal O\) is in fact tiled by \(\mathcal O\).

The proposed delta is exactly this quarter-to-full-octahedron grouping assertion in the \(\mathrm{SW2}\) case. It does not address the square antiprism or rhombicuboctahedron cases, arbitrary right-angled polyhedra, or arbitrary abstract gluings of triangular bipyramids.

## Cheapest decisive counterexample search

Work first in the chamber adjacency structure of the reflective tiling by
\(\Gamma(\mathcal P)\)-images of \(\mathcal P\), not with free abstract tile gluings.

1. Enumerate finite connected chamber sets up to the reflection-group symmetries and increasing chamber or quarter-tile count.
2. Retain only unions that are convex hyperbolic polyhedra in the source's sense.
3. Check that every boundary vertex is ideal, every boundary dihedral angle is \(\pi/2\), and the volume is finite. Use exact Coxeter/Gram data or a rigorously applicable Andreev-type combinatorial certificate.
4. Recover the quarter-octahedron decomposition promised by Proposition 7.10 and independently verify that each block is a valid copy of \(\frac14\mathcal O\).
5. As a first screen, form an exact-cover instance whose vertices are the canonical quarter blocks and whose hyperedges are the four-block unions proved isometric to \(\mathcal O\). Test whether all quarter blocks can be covered by disjoint hyperedges.

A retained \(\mathcal P\)-polyhedron with a machine-checkable proof that this first hypergraph has no exact cover is only a candidate counterexample. It becomes decisive only after either:

1. proving an alignment lemma that every octahedral tiling of this union can be replaced by one respecting the canonical quarter decomposition; or
2. enumerating, with a completeness proof, every geometrically possible embedded copy of \(\mathcal O\), including non-reflective copies whose faces cross canonical quarter blocks, and proving that no disjoint collection covers \(\mathcal Q\).

Without one of these gates, the exact-cover model may omit noncanonical tilings allowed by the source.

## Proof route suggested by the finite search

If exhaustive small assemblies always admit an octahedral cover, record which local choices force it. The two symmetry cuts defining
\(\frac14\mathcal O\) suggest encoding exposed cut faces by colors, parity classes, or a perfect-matching problem. A successful invariant must prove globally that quarter blocks pair into halves and halves into octahedra, including non-face-to-face tilings permitted by Definition 2.1's broader tiling convention.

Proposition 3.1 may support a minimal-counterexample induction because every
\(\mathcal P\)-polyhedron can be built by gluing smaller
\(\mathcal P\)-polyhedra along a common face. Any induction must prove that an octahedral tiling can be repaired across the gluing face; merely knowing both pieces tile separately is insufficient.

## Mandatory checks and falsification risks

- An abstract quarter-octahedron complex need not be convex or realizable in the reflective \(\mathcal P\)-tiling and is not automatically a \(\mathcal P\)-polyhedron.
- Ideal right-angled boundary conditions must be checked geometrically. A finite boundary vertex, wrong angle, infinite-volume cusp, or self-overlap invalidates a candidate.
- The source allows tilings whose tile faces need not match. An exact-cover model restricted to one canonical quarter decomposition may miss a valid noncanonical octahedral tiling.
- Failure to find a counterexample below a tile bound proves nothing without a theorem bounding a minimal counterexample or a complete local invariant.
- A volume divisible by \(\operatorname{vol}(\mathcal O)\) is necessary but not sufficient for tilability.
- A combinatorial parity pattern observed experimentally must be derived from the Coxeter/quarter-tile geometry before it is used universally.
- The figures are explanatory, not machine-readable definitions. Recover all face labels, reflection relations, and symmetry cuts from audited source data.

## Semantic neighbors and contribution boundary

Exact-ID and semantic searches for \(\mathrm{SW2}\), ideal right-angled octahedra, and octahedral tilings in the current registry, historical registry, and Batch68 found no duplicate or registered neighbor.

A small census, a shortest non-coverable abstract complex, or a parity conjecture is exploratory unless it satisfies the geometric gates above. A partial theorem for reflective face-to-face octahedral tilings must be labelled as such and cannot be presented as Conjecture 7.11, whose conclusion uses the source's broader tiling convention.
