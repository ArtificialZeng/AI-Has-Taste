# Mathematical referee report

## Frozen scope and verdict

I reviewed the `resolution-paper` claim frozen by snapshot digest
`9868a3eb2740290dc708e4528f7e54404c1458ffbbef59697af2fb3104fe83f6`:
for the Frobenius metric on the (3\times3) Birkhoff polytope,

\[
\Phi(\mathcal B_3)=1/\sqrt2,
\]

and the minimizing faces are exactly the single size-six orbit of edges whose
two vertices have relative permutation a 3-cycle.  The verdict is **accept**.
The proof settles both parts of the immutable statement: the exact value and
the complete classification under the specified 72-element action.

I did not consult `checkpoint.md`, owner confidence, an earlier verdict, or a
research transcript.  The canonical SHA-256 recomputation of the `files`
mapping in `audit/snapshot.json` equals the recorded snapshot digest.  Every
inspected frozen file has its recorded hash, and `source.md` retains SHA-256
`cd3816be23cb9ea4e13e3d90a94a11e269dd00751965f0452803922c9bb96ca1`.

## Independent face reconstruction

Inside the affine hull given by the row- and column-sum equations,
\(\mathcal B_3\) is cut out by the nine coordinate inequalities
\(x_{ij}\geq0\).  Hence every face is obtained by imposing a collection of
coordinate zeros.  I independently intersected the six permutation vertices
with each of the (2^9=512) possible coordinate-zero sets, removed duplicates,
and excluded the empty and whole faces.  This gives exactly 48 faces, with

\[
(f_0,f_1,f_2,f_3)=(6,15,18,9).
\]

I also independently generated the permutations of the six vertices induced
by all row permutations, column permutations, and optional transposition.
There are 72 distinct induced actions.  Quotienting the 48 faces gives exactly
the following five orbits:

| dimension | orbit size | representative |
|---:|---:|---|
| 0 | 6 | \(\{123\}\) |
| 1 | 6 | \(\{123,231\}\) |
| 1 | 9 | \(\{123,132\}\) |
| 2 | 18 | \(\{123,132,213\}\) |
| 3 | 9 | \(\{123,132,213,231\}\) |

This agrees with the frozen enumeration, but uses direct enumeration of all
coordinate-zero intersections rather than closure of vertex subsets.  It also
shows that no vertex, edge, two-face, or facet orbit has been omitted.  Each
action is visibly a Frobenius isometry and preserves complementary vertex
hulls, so distance is constant on these orbits.

## Exact distance reconstruction

For each representative (G=\operatorname{conv}\{A_i\}), with complementary
vertices (B_j), I rederived

\[
\delta(G)^2=
\min_{\mathbf1^T\alpha=1,\;\beta\geq0,\;\mathbf1^T\beta=1}
\left\|\sum_i\alpha_iA_i-\sum_j\beta_jB_j\right\|_F^2.
\]

I enumerated every nonempty active support of \(\beta\), solved the associated
equality-constrained stationary system over the rationals, and checked the
inactive KKT gradient inequalities.  I also checked the supplied certificates
directly: the affine coefficients sum to one, the simplex coefficients are
feasible, each residual is orthogonal to the direction space of
\(\operatorname{aff}G\), active gradients agree, inactive gradients are no
smaller, and the squared residual has the asserted value.  Convexity makes
these KKT certificates global.  The exact results are:

| representative | orbit size | \(\delta(G)^2\) | supplied affine \(\alpha\) lies in (G)? |
|---|---:|---:|:---:|
| \(123\) | 6 | \(2\) | yes |
| \(123,231\) | 6 | \(1/2\) | yes, \((1/2,1/2)\) |
| \(123,132\) | 9 | \(9/4\) | yes |
| \(123,132,213\) | 18 | \(9/10\) | no, \((-1/5,3/5,3/5)\) |
| \(123,132,213,231\) | 9 | \(9/4\) | yes |

Alternative active sets can give different closest coefficient vectors in
some nonminimal cases, but they give the same residual norm; this harmless
nonuniqueness does not affect the orbit comparison.

There is a short direct passage from this table to the claimed facial
distance.  Since (G\subseteq\operatorname{aff}G), for every face

\[
d(G)\geq\delta(G).
\]

The table therefore gives (d(G)\geq1/\sqrt2) for all 48 faces.  For the
representative (G=\operatorname{conv}\{P_{123},P_{231}\}), the exact points

\[
x=\frac{P_{123}+P_{231}}2\in G,
\qquad
y=\frac{P_{132}+P_{213}+P_{321}}3
 =\frac13\mathbf1\mathbf1^T\in\mathcal B_3[G]
\]

are feasible.  Their difference has six entries (1/6) and three entries
\(-1/3), and hence

\[
\|x-y\|_F^2=6(1/6)^2+3(1/3)^2=1/2.
\]

Thus this orbit has (d(G)=1/\sqrt2).  Every other orbit has
\(\delta(G)^2>1/2\), hence (d(G)>1/\sqrt2).  This proves both the global
minimum and the complete equality classification without needing to assume
that every individual affine projection lies in its face.  It is also
consistent with, and stronger than, the general bound (1/\sqrt8) cited for
this case.

## Source comparison and limitations

The inspected Peña--Wirth source defines the same facial distance in
Definition 2.1, gives the global affine-hull reduction in Lemma 3.3, and in
Example 6.4 proves only
\(\Phi(\mathcal B_n)\geq1/\sqrt{n^2-1}\).  Its closing discussion says that
its separate general conjecture was not proved for the Birkhoff polytope.  The
candidate neither claims that general conjecture nor claims that the specified
72-element group is the full isometry group.  It also makes no literature
priority or certified-open-status assertion.  Those cautions should remain in
any manuscript, but they are not gaps in this exact frozen finite theorem.

## Final assessment

**Accept.**  The exhaustive face/orbit certificate is complete, the five
exact convex quadratic certificates are valid, the minimizing affine point is
feasible in the asserted edge, and the strict values for the other four
orbits establish orbit completeness.  I found no unresolved mathematical gap
in the frozen candidate scope.
