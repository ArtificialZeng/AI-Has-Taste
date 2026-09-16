# Triage verification for `win-00079-p01-triage-226b85b4cb78`

This is screening evidence, not a proof or a novelty certificate.

## Frozen input and recovery material

- `source.md` has SHA-256
  `0106369cec2d01113c6dc3c4ff452985dbc82e092b29df12ad49a776946f7201`.
- Enumeration on 2026-09-10 found no `literature/*handoff*.md` file.
- The PDF path written in `source.md` is not present relative to this project.
  The mathematical source claims were therefore rechecked against the official
  arXiv v1 HTML rather than treating the earlier checkpoint as evidence.

## Primary-source check

Official source inspected on 2026-09-10:
<https://arxiv.org/html/2609.04258v1>.

- Proposition 2.1 says that at
  \(\alpha_0=\arccos(1/3)\) every vertex is ideal.
- Proposition 2.3 constructs the regular endpoint cube, proves uniqueness only
  for \(\alpha>\alpha_0\), and explicitly says endpoint uniqueness is not
  needed.
- Proposition 5.1 and Remark 5.2 again restrict isometric uniqueness to
  \(\alpha>\alpha_0\).
- Searches for the exact assertion and nearby ideal/Lorentz-Gram rigidity
  terminology did not identify an explicit primary-source endpoint theorem.
  This limited negative search does not establish openness or novelty.

## Independent exact check

For facet order \((1+,1-,\ldots,4+,4-)\), the candidate forced matrix has
diagonal entries \(1\), opposite entries \(-5/3\), and all remaining entries
\(-1/3\).  An exact SymPy recomputation returned

\[
\operatorname{rank}G=5,\qquad
\operatorname{spec}G=\{8/3^{(4)},-8/3^{(1)},0^{(3)}\}.
\]

A kernel basis is

\[
(-1,-1,1,1,0,0,0,0),
(-1,-1,0,0,1,1,0,0),
(-1,-1,0,0,0,0,1,1).
\]

Direct multiplication also verifies that this is the Gram matrix of
\(w_i^\pm=(1/\sqrt3,\,\pm(2/\sqrt3)e_i)\) in signature \((4,1)\).

## Cheapest geometric discrimination

The missing sign condition is tractable.  The non-obtuse face criterion rules
out \(|x_i|<1\) for nonincident opposite facets.  If instead \(x_i>1\), a
Lorentz normal form for the two unit spacelike normals is

\[
u=(0,1,0,\ldots),\qquad
v=(\pm\sinh t,\cosh t,0,\ldots),\quad t>0.
\]

On the future hyperboloid, one of the oriented halfspaces
\(\langle\cdot,u\rangle\le0\) and
\(\langle\cdot,v\rangle\le0\) contains the other.  For \(x_i=1\), the
distinct-normal parabolic form
\(u=(0,1,0,\ldots)\), \(v=(a,1,a,0,\ldots)\) gives the same nesting (and
\(a=0\) gives duplicate hyperplanes).  Hence the positive branch would make
one of the two alleged facets redundant.  Irredundancy forces \(x_i\le-1\).

Together with the calculation in `evidence/triage-gram-check.md`, this forces
all \(x_i=-5/3\).  What remains for a research proof is a fully written
well-defined spanning-Gram isometry, its time orientation, and equality of the
eight oriented halfspace intersections.
