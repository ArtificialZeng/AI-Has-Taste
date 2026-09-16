# Fresh mathematical referee report

Referee job: `win-00079-p01-referee-ae670a98f803`  
Frozen snapshot: `a2a0fa64f58d30e90df13ae7c112ac08fa73e1858cab17587a0a9b3956ee78a6`

## Scope and integrity

I reviewed the exact `resolution-paper` claim in `claim.json`, without changing
its hypotheses or conclusion.  It is the full assertion in `source.md`: every
finite-volume convex hyperbolic 4-polytope with the complete face lattice of a
4-cube, finite or ideal vertices only, and common dihedral angle
`arccos(1/3)` is isometric to the regular ideal cube.  Thus this is not a
subsidiary statement or a restriction of the frozen problem.

I recomputed every SHA-256 entry in `audit/snapshot.json` and recomputed the
canonical snapshot digest.  All entries agree, and the digest is the value
displayed above.  The immutable `source.md` hash remains
`0106369cec2d01113c6dc3c4ff452985dbc82e092b29df12ad49a776946f7201`.

## Reconstruction of the decisive argument

Let `u_i^+` and `u_i^-` be the outward unit spacelike normals of the four
opposite facet pairs.  For different indices, cube incidence and the outward
normal angle formula give

\[
 \langle u_i^\varepsilon,u_j^\delta\rangle=-1/3.
\]

For each cube sign vector `sigma`, the four incident normals have Gram matrix

\[
 H=\frac43 I_4-\frac13 J_4.
\]

This matrix has rank 3, positive spectrum `4/3,4/3,4/3`, and kernel spanned by
the all-ones vector.  Hence
`r_sigma=sum_i u_i^{sigma_i}` is null and orthogonal to all four incident
normals.  It is nonzero because an interior future timelike point `q` satisfies
`<q,r_sigma><0`.  Any linear relation among those four normals first lies in
the kernel of `H` and hence is a multiple of their sum; nonvanishing of
`r_sigma` then makes that multiple zero.  Thus the normals are independent.

A finite vertex would have a timelike representative whose orthogonal
4-space is positive definite, contradicting singularity of `H`.  Hyperideal
vertices are excluded by the frozen hypotheses, so the corresponding vertex
is ideal.  The common orthogonal complement of the four independent normals
is one-dimensional, and therefore its ideal ray is precisely the ray of
`r_sigma`.  The strict inequality against `q` selects the future ray.

Put

\[
 d_i=u_i^+-u_i^-,\qquad s_i=u_i^++u_i^-.
\]

Two cube vertices differing only in coordinate `i` are distinct geometric
vertices because the assumed face lattice is the cube face lattice.  Their
`r`-vectors are consequently nonproportional future null vectors.  The
Lorentzian null-cone inequality is then strict, so

\[
 d_i^2=(r_+-r_-)^2=-2\langle r_+,r_-\rangle>0.
\]

Direct expansion of the fixed cross-pair entries gives

\[
 \langle d_i,d_j\rangle=0\ (i\ne j),\quad
 \langle s_i,d_j\rangle=0\ (i,j),\quad
 \langle s_i,s_j\rangle=-4/3\ (i\ne j).
\]

The four nonzero mutually orthogonal spacelike vectors `d_i` span a positive
4-space in signature `(4,1)`.  Its orthogonal complement is a negative line,
and every `s_i` lies on it.  Writing `s_i=a_i tau` with `tau^2=-1` gives
`a_i a_j=4/3` for every distinct pair.  These equations force all four
coefficients to have the same value and square `4/3`.  Therefore
`s_i^2=-4/3`.  Since

\[
 s_i^2=2+2\langle u_i^+,u_i^-\rangle,
\]

all four previously unknown opposite-facet entries equal `-5/3`.

The proposed model normals

\[
 w_i^\pm=(1/\sqrt3,\,\pm 2e_i/\sqrt3)
\]

have exactly these diagonal, cross-pair, and opposite-pair products.  Both
ordered systems span the five-dimensional Lorentz space: their four
difference vectors span a positive 4-space and any sum vector supplies its
negative orthogonal line.  Equality of the full Gram matrices respects all
linear relations.  Explicitly, if a coefficient vector gives zero in the
`u`-system, Gram equality makes the corresponding model combination
orthogonal to every spanning model normal, so it is zero.  The induced map is
therefore a well-defined surjective Lorentz isometry sending each `u_i^pm` to
`w_i^pm`.

For the interior point `q`, all eight transformed inequalities are strict.
Adding either opposite pair yields
`-(2/sqrt(3))(Tq)_0<0`, hence `(Tq)_0>0`; the isometry preserves the future
sheet.  It consequently carries the complete oriented halfspace intersection,
not merely the supporting hyperplanes, to the model intersection.  In Klein
coordinates its inequalities are exactly `-1/2 <= y_i <= 1/2`.  This entire
Euclidean cube lies in the closed unit ball and its sixteen vertices have
squared norm one, so its Klein closure is the asserted regular ideal cube.

## Independent checks and attacks

I independently recomputed the vertex Gram rank and spectrum, the eight model
normals' complete Gram matrix, its rank 5 and spectrum
`{-8/3,0,0,0,8/3,8/3,8/3,8/3}`, and all snapshot hashes using a fresh
`python3`/SymPy calculation.  These agree with the submitted exact check.

I specifically tested the possible failure points in the proof:

- the null sums cannot vanish because every facet inequality is strict at an
  interior point;
- distinct adjacent cube vertices cannot give the same ideal ray under the
  assumed geometric face lattice, so each `d_i` is strictly spacelike rather
  than merely nonnegative;
- no division by a possibly zero coefficient occurs, since every pairwise
  product of the line coefficients is `4/3`;
- equality of Gram matrices is used only after checking spanning and relation
  compatibility;
- time orientation and the signs of all eight halfspaces are retained; and
- the argument covers every finite/ideal configuration allowed by the frozen
  claim and does not assume compactness at the endpoint.

No unresolved mathematical gap remained in these attacks.

## Source comparison and contribution

I inspected the listed primary PDF itself.  Proposition 2.1 proves endpoint
ideality.  Proposition 2.3 constructs the Klein cube but applies compact
non-obtuse rigidity only for `alpha>alpha_0` and explicitly says endpoint
uniqueness is not needed.  Proposition 5.1 and Remark 5.2 likewise state
isometric uniqueness only above the endpoint.  Thus the cited source does not
already contain the frozen endpoint resolution.  The submitted proof is
self-contained, closes exactly that stated gap by a Lorentz-Gram argument,
and makes only bounded, appropriately qualified literature claims; it does
not claim priority or a comprehensive openness result.

## Verdict

**Accept.**  The frozen argument proves the original assertion in its full
scope, the realization and oriented-halfspace step are complete, and the
claimed contribution is accurately delimited.
