# Primary-source and bounded literature screen

Screen date: 2026-09-08.

## Original problem source

The local official arXiv PDF is
`evidence/external/2609.04554.pdf`, SHA-256
`f73a5cf3fa71f1c5f387de7cf1d881214831d557a2b46ba43e2e2518bac37480`.
It is Adityo Mamun, Jonathan Nalikka, and Eric Ramos, *Universality in the
algebra and topology of cographs*, arXiv:2609.04554v1 (3 September 2026).

- Definition 4.13, PDF p.26, is exactly the anchored space used in the proof:
  the subcomplex of (G^n) in which every element of (K) occurs among the
  labelled coordinates.
- Corollary 4.18, PDF pp.27--28, gives finite generation and uniform exponent
  bounds over cographs, but not torsion-freeness.
- PDF p.28 explicitly says that it was not known whether anchored
  configuration spaces can have integral torsion and identifies trees and
  cycles as the known torsion-free families.

The official records checked were
<https://arxiv.org/abs/2609.04554v1> and
<https://arxiv.org/html/2609.04554v1> (especially HTML lines 576--630).

## Decisive prior theorem used

Dmitry N. Kozlov, *Stirling complexes*, Journal of Applied and Computational
Topology **7** (2023), 57--74,
<https://doi.org/10.1007/s41468-022-00096-4>, Definition 2.4 and Theorem 2.5,
was checked on the publisher's open-access article page.  It states that for a
tree (T), an arbitrary vertex subset (S), and (m\geq |S|), the anchored
complex is homotopy equivalent to a wedge of spheres of dimension
(m-|S|).  The proof artifact uses only the resulting torsion-freeness, after
identifying a compatibility nerve with such a tree space.

The nearby circle computation was also located at Dmitry N. Kozlov,
*Homology and Euler characteristic of generalized anchored configuration
spaces of graphs*, J. Appl. Comput. Topol. **8** (2024), 1053--1067,
<https://doi.org/10.1007/s41468-024-00167-8> and
<https://arxiv.org/abs/2309.17149>.  It is not needed by the proof.

## Resolution/duplicate search

Exact-phrase and equivalent-term searches of arXiv/web records on 2026-09-08
for "anchored configuration spaces" with "torsion", "integral homology", and
"Stirling complexes", together with inspection of the references and
discussion in arXiv:2609.04554v1, returned the source paper and Kozlov's known
tree/circle papers, but no theorem equivalent to the Cech/tree-nerve
decomposition in `evidence/torsion_free_proof.md` and no later resolution of
the source-stated question.

This is a bounded search finding, not proof of priority, exhaustiveness, or
journal novelty.  The candidate claim is the mathematical resolution itself;
any eventual novelty statement must retain this limitation and undergo fresh
citation review.
