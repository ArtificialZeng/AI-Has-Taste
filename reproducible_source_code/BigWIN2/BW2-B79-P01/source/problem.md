# Precise problem reading

## Frozen claim and provenance

The immutable statement is `source.md` (SHA-256
`0106369cec2d01113c6dc3c4ff452985dbc82e092b29df12ad49a776946f7201`).
This triage record was independently rechecked for job
`win-00079-p01-triage-a8d6f4f2a5c7`; it does not modify, correct, or replace
that statement.

Let

\[
\alpha _0=\arccos(1/3)\in(0,\pi/2).
\]

The claim quantifies over every full-dimensional, finite-volume, convex
hyperbolic polytope (P\subset\mathbb H^4) with the following properties.

1. Its face lattice is isomorphic to that of the Euclidean (4)-cube, so in
   particular it has eight irredundant facets and sixteen vertices. After
   choosing such an isomorphism, its facets are labelled
   (F_i^+,F_i^-) for (i=1,\ldots,4).  The only nonincident pairs of facets
   are (F_i^+,F_i^-); for (i\ne j), every (F_i^\varepsilon) and
   (F_j^\delta) meet in a codimension-two face.  Each sign choice
   ((\varepsilon_1,\ldots,\varepsilon_4)\) specifies the corresponding
   four-facet vertex incidence.
2. Every codimension-two dihedral angle is the interior angle (\alpha _0).
3. Vertices are points of (\mathbb H^4) or its ideal boundary.  Hyperideal
   vertices, polar truncations, and changes of face lattice are excluded.

The conclusion is that some isometry of (mathbb H^4) maps (P) onto the
regular ideal cube (C^4_{\alpha _0}).  Concretely, in the Klein ball the
target model is

\[
[-1/2,1/2]^4\subset\overline{\mathbb B^4};
\]

its sixteen vertices lie on (\partial\mathbb B^4).  The desired isometry
need not preserve a preselected facet labelling.

## Lorentzian normalization

Use (mathbb R^{4,1}) with

\[
\langle x,y\rangle=-x_0y_0+x_1y_1+\cdots+x_4y_4,
\qquad
\mathbb H^4=\{x:\langle x,x\rangle=-1,\ x_0>0\}.
\]

Write (u_i^\pm) for the outward unit spacelike normals to the labelled
facet hyperplanes, so (P) is the intersection of their oriented
halfspaces.  Cube incidence and the angle condition mean

\[
\langle u_i^\varepsilon,u_j^\delta\rangle=-\cos\alpha _0=-1/3
\quad(i\ne j),
\]

whereas the four unknown opposite-facet entries are
(x_i=\langle u_i^+,u_i^-\rangle).  Thus the assertion is equivalently that
the oriented facet configuration is forced, up to a time-orientation
preserving Lorentz isometry, to have (x_i=-5/3) for every (i), and that
the corresponding halfspace intersection is the stated Klein cube.

## Source status and nearest result

Source status at triage: **new-question**, not an authoritatively certified
open problem. On 2026-09-10 this job rechecked the official arXiv v1 HTML for Andrey Egorov,
*Minimal-Volume Equiangular Hyperbolic 4-Polytopes*,
<https://arxiv.org/html/2609.04258v1>, was inspected directly:

- Proposition 2.1 proves that at (\alpha_0) every vertex of any such
  finite-volume equiangular (4)-polytope is ideal.
- Proposition 2.3 constructs (C^4_\alpha) and proves cube uniqueness only
  for (\alpha>\alpha_0); it expressly makes no endpoint uniqueness claim.
- Proposition 5.1 and Remark 5.2 likewise restrict their equality uniqueness
  statement to (\alpha>\alpha_0).

The nearest cited rigidity result is E. M. Andreev, *On convex polyhedra in
Lobachevskii spaces*, Math. USSR-Sb. 10 (1970), 413--440,
<https://doi.org/10.1070/SM1970v010n03ABEH001677>: its bounded acute-angled
rigidity theorem covers the compact case, not this all-ideal endpoint.
Searches of the exact assertion, Lorentz-Gram formulations, ideal-polytope
rigidity, and Stoker/Andreev terminology found no explicit prior endpoint
theorem in the inspected primary sources.  This limited search is not a
priority or openness proof.

## Proposed contribution and verification route

Nearest prior result: compact cube rigidity above the endpoint.  Proposed
delta: rigidity of precisely the ideal endpoint.  The complete proposer
argument is `evidence/research-152f05b9d7a8-proof.md`, with exact matrix and
kernel corroboration in
`evidence/research-152f05b9d7a8-exact-check.md`.

The research proof replaces the earlier disjoint-hyperplane sign route by a
more intrinsic vertex argument.  For every cube sign vector, the sum of its
four incident normals is the future null representative of that ideal vertex.
Two sign vectors differing in coordinate (i) give distinct future null rays,
so their difference (d_i=u_i^+-u_i^-) is spacelike.  The four mutually
orthogonal (d_i) therefore span a positive four-space.  Their orthogonal
negative line contains all (s_i=u_i^++u_i^-), and the pairwise products force
(s_i^2=-4/3), hence (x_i=-5/3).  Equality of the two spanning Gram systems is
then shown to define a well-defined Lorentz isometry; an interior point fixes
its time orientation, and all eight oriented inequalities map to the Klein
cube inequalities.

This is a proposed resolution awaiting a fresh mathematical referee.  No
volume bound, Coxeter classification, right-angled statement,
higher-dimensional extension, or uniqueness for a different combinatorial
type is included.
