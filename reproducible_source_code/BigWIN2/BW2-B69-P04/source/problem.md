# Precise problem interpretation

Provenance: `win-00069-p04-triage-c70d87e1861a`  
Frozen input: `source.md`, SHA-256 `dca4196df34842036dd339b43038065ab16b1f0d9d39ac60f956cdaeec3c7e92`.

## Objects and conventions

- The ambient space is hyperbolic three-space \(\mathbb H^3\). A “hyperbolic polyhedron” means, as in the source, a convex intersection of finitely many closed hyperbolic half-spaces and has finite volume unless explicitly stated otherwise.
- \(\mathcal P=\mathrm{SW2}\) is the fixed Scharlau–Walhorn hyperbolic Coxeter polyhedron with that label and face numbering in Appendix B of Allcock–Devlin–Felikson–Kontorovich–Whitehead, *Arithmetic Polyhedra*, arXiv:2609.05349v1. Its face reflections generate \(\Gamma(\mathcal P)\), whose images of \(\mathcal P\) form the fixed reflective chamber tiling of \(\mathbb H^3\).
- A \(\mathcal P\)-polyhedron \(\mathcal Q\) is a convex hyperbolic polyhedron that is a finite union of chambers \(\gamma\mathcal P\), \(\gamma\in\Gamma(\mathcal P)\), in that reflective tiling (Definition 2.1). This is stronger than merely being tiled by isometric copies of \(\mathcal P\).
- “Ideal” means every vertex of \(\mathcal Q\) lies on \(\partial_\infty\mathbb H^3\). “Right-angled” means every boundary dihedral angle of \(\mathcal Q\) is \(\pi/2\).
- \(\mathcal O\) denotes the ideal, right-angled hyperbolic octahedron, uniquely determined up to isometry by its octahedral combinatorics and prescribed ideal/right-angle data.
- In the conclusion, “tiled by \(\mathcal O\)” uses the source's general definition: \(\mathcal Q\) is a union of isometric copies of \(\mathcal O\) with pairwise disjoint interiors. The copies need not be chambers for a reflection group, need not respect the \(\mathcal P\)-chamber decomposition, and need not meet face-to-face. Because \(\mathcal Q\) has finite volume and every copy of \(\mathcal O\) has the same positive volume, such a tiling is necessarily finite.

## Frozen assertion with quantifiers

Prove or disprove the following universal statement:

\[
\forall\,\mathcal Q\;\Bigl[
  \mathcal Q\text{ is an ideal, right-angled }\mathrm{SW2}\text{-polyhedron}
  \Longrightarrow
  \exists m\ge 1,\ \exists g_1,\ldots,g_m\in\operatorname{Isom}(\mathbb H^3):
  \mathcal Q=\bigcup_{i=1}^m g_i\mathcal O,
  \ \operatorname{int}(g_i\mathcal O)\cap\operatorname{int}(g_j\mathcal O)=\varnothing\ (i\ne j)
\Bigr].
\]

A disproof must therefore give one explicit convex finite-volume union of chambers in the fixed reflective \(\mathrm{SW2}\)-tiling, certify that its boundary vertices are all ideal and its boundary dihedral angles are all \(\pi/2\), and prove that no tiling allowed by the preceding broad definition exists.

## Scope and logical boundary

The assertion concerns only \(\mathcal P=\mathrm{SW2}\). It does not quantify over arbitrary Coxeter polyhedra, arbitrary members of the octahedral commensurability class, or arbitrary abstract gluings of quarter-octahedra. It does not impose a reflective or face-to-face condition on the desired octahedral tiling.

The sentence after Conjecture 7.11 says it would *suffice* to prove that every ideal polyhedron tiled by \(\tfrac14\mathcal O\) is tiled by \(\mathcal O\). That is a stronger sufficient target, not an equivalent reformulation unless one additionally proves that every ideal quarter-octahedron-tiled polyhedron lies in the frozen \(\mathrm{SW2}\)-polyhedron class.

## Nearest primary result and source status

The official arXiv v1 was checked on 2026-09-08:

- Definition 2.1 gives the two distinct tiling conventions: <https://arxiv.org/html/2609.05349v1#S2.SS1>.
- Proposition 7.10 proves that \(\mathcal O\) is an \(\mathrm{SW2}\)-polyhedron and every ideal, right-angled \(\mathrm{SW2}\)-polyhedron is tiled by \(\tfrac14\mathcal O\); it also gives more structured canonical decompositions in two face-type cases: <https://arxiv.org/html/2609.05349v1#S7.SS4>.
- Conjecture 7.11 states the frozen assertion, and §8 item 1 calls it a natural next step: <https://arxiv.org/html/2609.05349v1#S7.SS4> and <https://arxiv.org/html/2609.05349v1#S8>.

Thus the nearest prior result is Proposition 7.10 and the proposed delta is exactly the passage from quarter-octahedral tilability to full-octahedral tilability for the frozen class. Exact-phrase and equivalent-language searches on 2026-09-08 found no primary source claiming a proof or counterexample. This supports the label **open-supported (source-stated)**, not a claim of exhaustive priority or proof that no resolution exists.

Ian Whitehead, *A note on right-angled, ideal hyperbolic polyhedra*, arXiv:2609.05389v1, Theorems 1–2, gives equivalent combinatorial criteria for an abstract polyhedron to admit an ideal right-angled realization: <https://arxiv.org/html/2609.05389v1>. It does not address octahedral tilings and does not settle the conjecture. Its criteria can screen boundary combinatorics in a finite search, but they do not by themselves certify that a proposed union of fixed \(\mathrm{SW2}\) chambers is convex or has the asserted embedded geometry.

## Admitted target and first discriminating test

Nearest prior result \(X\): Proposition 7.10 (quarter-octahedral tiling). Proposed delta \(Y\): a proof of Conjecture 7.11 or a geometrically certified counterexample. Verification route \(Z\): exact chamber geometry plus exact finite covering or a tiling-invariant proof.

The cheapest initial attack is a volume-obstruction census. The source constructs each relevant \(\tfrac14\mathcal O\) from 12 \(\mathrm{SW2}\) chambers and \(\mathcal O\) from four such quarters, hence from 48 chambers. Enumerate, up to \(\Gamma(\mathcal P)\)-symmetry, connected unions of both source-realized 12-chamber quarter-octahedron types using at most seven quarters. Retain only unions certified from exact Coxeter half-spaces to be convex, ideal, and right-angled; use Whitehead's criterion only as an independent combinatorial screen. Any retained union with a number of quarters not divisible by four is an immediate counterexample by volume, regardless of noncanonical or non-face-to-face octahedral tilings. If none exists, preserve the exact census and use its forced local groupings to formulate the next invariant; the finite negative search alone does not prove the conjecture.
