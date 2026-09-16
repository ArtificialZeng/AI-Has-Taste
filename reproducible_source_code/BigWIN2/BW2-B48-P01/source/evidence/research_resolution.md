# Exact resolution dossier

All permutation labels below are one-line notation: (abc) denotes the
permutation matrix (P_\sigma) with
(sigma(1)=a,\sigma(2)=b,\sigma(3)=c).

## Theorem

For the frozen problem in `source.md`,

\[
\Phi(\mathcal B_3)=\frac1{\sqrt2}.
\]

Exactly six faces attain this value.  They form one orbit under the specified
row/column/transposition group: the edges whose two permutation vertices have
relative permutation a 3-cycle.  A representative is

\[
G=\operatorname{conv}\{P_{123},P_{231}\}.
\]

## Complete face and orbit reduction

The polytope is the intersection of its affine hull with the nine half-spaces
(x_{ij}\geq0).  Consequently every face is specified by requiring some
coordinates to vanish.  If a nonempty set (S) of permutation vertices is
given, let (E(S)) be the union of their matrix supports.  The smallest face
containing (S) has as vertices precisely all permutation matrices whose
supports are contained in (E(S)).  Thus (S) is the complete vertex set of a
face if and only if it is fixed by this closure operation.

`triage_face_enumeration.py` checks this criterion for all (2^6-2) nonempty
proper vertex subsets, computes affine dimensions exactly, constructs all
distinct actions induced by independent row and column permutations and
transposition, and quotients the faces.  Its replayed output
`triage_face_enumeration.txt` gives 48 nonempty proper faces and exactly these
five orbits:

| dimension | orbit size | representative vertex labels |
|---:|---:|---|
| 0 | 6 | (123) |
| 1 | 6 | (123,231) |
| 1 | 9 | (123,132) |
| 2 | 18 | (123,132,213) |
| 3 | 9 | (123,132,213,231) |

The induced action has exactly 72 elements.  Every action is a Frobenius
isometry and permutes the six vertices, so the distance defined in the frozen
problem is constant on each listed orbit.

## Exact affine-distance certificates

For one of the five faces (G=\operatorname{conv}\{A_i\}), write the
complementary vertices as (B_j).  Consider

\[
\delta(G)^2=\min_{\beta\geq0,\ \mathbf1^T\beta=1}
 \operatorname{dist}\!\left(\sum_j\beta_jB_j,
 \operatorname{aff}G\right)^2.
\]

The rational certificates in `exact_affine_distance.py` give coefficients
(\alpha), with (\mathbf1^T\alpha=1), and simplex coefficients (\beta).
For (x=\sum_i\alpha_iA_i), (y=\sum_j\beta_jB_j), and (e=x-y), the script
checks exactly that

1. (e) is orthogonal to every (A_i-A_0), hence (x) is the orthogonal
   projection of (y) onto (\operatorname{aff}G);
2. if (g_j=-2\langle B_j,e\rangle), then all (g_j) with
   (\beta_j>0) equal a common multiplier and all remaining (g_j) are at
   least that multiplier; and
3. the displayed value equals (\langle e,e\rangle).

Condition 2 is the KKT condition for minimizing the convex quadratic over the
simplex.  It is sufficient for a global minimum.  The resulting squared
affine distances, in the order of the table above, are

\[
2,\qquad \frac12,\qquad \frac94,\qquad \frac9{10},\qquad \frac94.
\]

All coefficients, orthogonality inner products, gradients, and comparisons are
replayed over `fractions.Fraction` in `exact_affine_distance.py`; its expected
output is recorded in `exact_affine_distance.txt`.  In particular the unique
smallest affine-distance orbit is the size-six 3-cycle edge orbit.

## Passage from affine distances to facial distance

For completeness, the global affine-hull reduction used here follows from the
standard argument recorded as Lemma 3.3 of Peña--Wirth.  Let (G) minimize
(\delta(G)) among all nonempty proper faces, and let (p\in\operatorname{aff}G)
and (q\in\mathcal B_3[G]) be closest points.  If (p\notin G), a facet
(\widetilde G) of (G) separates (p) from (G).  Choose a vertex
(v\in G\setminus\operatorname{aff}\widetilde G).  For some (0<\lambda<1),
(\widetilde p=\lambda p+(1-\lambda)v\) lies in
(\operatorname{aff}\widetilde G).  Also
(\widetilde q=\lambda q+(1-\lambda)v\) belongs to
(\mathcal B_3[\widetilde G]), because the latter complementary hull contains
both (\mathcal B_3[G]) and every vertex of (G\setminus\widetilde G).
Therefore

\[
\delta(\widetilde G)\leq
\|\widetilde p-\widetilde q\|_F
=\lambda\|p-q\|_F<\delta(G),
\]

a contradiction.  Hence a globally affine-minimizing face has (p\in G), and

\[
\min_G d(G)=\min_G\delta(G).
\]

The exact certificate also checks containment directly for the unique
minimizing representative: its affine coefficients are
(\alpha=(1/2,1/2)).  Thus no issue about the affine point lying outside the
face remains.  (The two-face certificate deliberately reports a negative
affine coefficient, illustrating why containment was not assumed orbitwise.)

## Equality witness and complete classification

For the representative 3-cycle edge, the certificate specializes to

\[
x=\frac{P_{123}+P_{231}}2\in G,
\qquad
y=\frac{P_{132}+P_{213}+P_{321}}3
=\frac13\mathbf1\mathbf1^T\in\mathcal B_3[G].
\]

The matrix (x-y) has six entries (1/6) and three entries (-1/3), so

\[
\|x-y\|_F^2=6\left(\frac16\right)^2+
3\left(\frac13\right)^2=\frac12.
\]

Since every other face orbit has affine distance squared strictly above
(1/2), its actual facial distance is at least its affine distance and cannot
equal (1/\sqrt2).  The enumerated orbit has size six, so the complete list of
minimizers is precisely the six edges of the stated relative-3-cycle type.

## Scope and literature caution

This dossier proves the frozen finite (3\times3) statement.  It does not
settle any general-(n) conjecture, claim that the stated 72-element group is
the full affine-isometry group, or establish literature priority.  The limited
literature screen recorded in `problem.md` remains only a screen.
