# Mathematical referee report

## Verdict

**Accept** the exact frozen `result-note` claim.  The evidence proves the
bounded classification through 84 SW2 chambers.  It does not prove or
disprove Conjecture 7.11, and the original problem remains unresolved.

## Frozen scope and integrity

I reviewed the statement in `claim.json` against `source.md`, `problem.md`,
the snapshot, and every file enumerated by the snapshot.  All nine file
SHA-256 values agree with `audit/snapshot.json`.  Independently applying the
contract's sorted compact-JSON digest rule to the file-hash mapping gives

```text
f377f3bf358565be56a75f2b0c6664a41ad1d13a7d50004d2a66e2234e483396
```

which is the frozen snapshot digest used by the accompanying audit record.

The official arXiv v1 source was also checked at its versioned HTML on
2026-09-08.  Definition 2.1, Lemma 7.9, Proposition 7.10, and Conjecture 7.11
have the meanings recorded in the frozen inputs.  In particular, Lemma 7.9
gives the all-face-3/no-face-3 dichotomy; Proposition 7.10 gives the
reflective quarter-octahedron decomposition in the first branch and the
canonical quarter/half/full decomposition in the second; Conjecture 7.11 is
still stated as a conjecture.  Thus the proof uses the cited theorem with its
actual hypotheses and does not replace the original broad tiling convention
by a face-to-face one.

## Reconstruction of the decisive argument

Write one quarter-octahedron volume unit as 12 SW2 chambers.  Proposition
7.10 makes the chamber count of every polyhedron in the frozen hypothesis a
multiple of 12.  Therefore the bound of 84 chambers is exactly a bound of
seven canonical units, and Lemma 7.9 reduces the classification to two
exhaustive branches.

The supplied Lorentz model is internally exact.  With

```text
J = diag(-1,1,1,1)
n1=(0,-1,1,0), n2=(1,1,1,1),
n3=(0,0,0,-1), n4=(0,0,-1,1),
```

the normalized products give precisely the recorded SW2 Coxeter orders.
The 1-3-4 subgroup has order 48 and its orbit has the eight supporting
planes `(1,±1,±1,±1)`.  Exact triple intersections give six ideal
vertices, twelve orthogonal edges, and no finite vertices, so this orbit is
the standard ideal right-angled octahedron.  The two 12-chamber constructions
have isomorphic normalized facet Gram matrices and hence are isometric copies
of the same right-angled triangular bipyramid.

In the all-face-3 branch, the source makes the canonical quarter tiling
reflective.  After the preceding isometry it is therefore a chamber union in
the reflection tiling used by `sw2_quarter_census.py`.  Any connected union of
at most seven quarters containing a chosen root lies in the radius-six Cayley
ball.  Closure under the union of all minimal galleries is the
intersection-of-roots criterion for a convex Coxeter chamber subcomplex.
Adjoining a target-adjacent chamber and taking this closure stays inside any
convex target, so the breadth-first construction is exhaustive by induction.
It enumerates, by sizes 1 through 7,

```text
1, 6, 18, 57, 150, 450, 1218
```

rooted convex unions.  Exact half-space reconstruction leaves only three
rooted states, all of size four; their boundary data are those of an ideal
right-angled octahedron.  The three are rooted occurrences, not three
different polyhedral types.

In the no-face-3 branch, each SW2 chamber has one 1-3-4 center, so the source's
canonical blocks partition the chamber set by center.  At a fixed center the
long-root mirrors of types 1 and 4 give six unoriented, hence twelve oriented,
cut half-spaces.  The exact star calculation recovers all twelve halves from
one cut and all twelve quarters from the allowable orthogonal two-cut
sectors; together with the full star these are 25 local variants.  Their cut
signatures are distinct.  Among variants containing a specified chamber the
counts are three quarters, six halves, and one full octahedron, so the ten
choices used at every new center are complete.

The interface rejection is valid, not a heuristic pruning.  Across a type-2
facet the two adjacent star centers have exact oriented signs -1 and +1.  If
both centers occur but the adjacent chamber does not, the exposed facet is a
boundary patch while a point of the proposed union lies strictly beyond its
supporting half-space, contradicting convexity.  Also, the block graph of a
connected chamber union is connected: moves within a center use types 1, 3,
and 4, while exactly the type-2 moves change the center.  These observations
justify the block-by-block induction in `sw2_mixed_census.py`.

The mixed-state key loses no information.  A center together with its
oriented cut signature determines its local variant, and normalizing at each
member chamber considers every possible left translation in the SW2 Coxeter
group.  For a retained state, requiring every exposed chamber mirror to
support every chamber is also sufficient for geometric convexity: if a point
of the intersection of those inward half-spaces lay outside the chamber
union, a generic segment from an interior point would first exit across an
exposed facet into that facet's forbidden side.

The mixed enumeration gives compatible-state counts

```text
1, 2, 4, 17, 52, 235, 1054
```

and convex-state counts

```text
1, 2, 2, 10, 11, 35, 69.
```

Every convex nonsurvivor has an exactly detected finite boundary vertex.
There are exactly two ideal right-angled survivors, both at four units, with
block patterns `[4]` and `[1,1,1,1]`.  Each has eight facets, twelve edges,
and six four-valent ideal vertices.  More decisively, each ordered boundary
Gram matrix equals the standard octahedron Gram matrix.  The stored nonzero
4-by-4 normal minor has determinant -8, so the normals span Lorentz
four-space; Gram equality consequently extends to a Lorentz isometry of the
oriented half-space systems.  Both survivors are therefore copies of the
ideal right-angled octahedron.

Combining the two exhaustive branches proves that every polyhedron in the
frozen hypothesis has 48 chambers and is isometric to the octahedron.

## Checks and attacks actually performed

- I read both certificates rather than treating their JSON conclusions as
  proofs, and checked the group action direction, transformed normals,
  interval radius, closure induction, local-block completeness, interface
  signs, canonicalization, convexity test, vertex recovery, edge-angle test,
  and final Gram argument.
- I reran both programs with ordinary Python and exact integer arithmetic.
  Their newly generated JSON files were byte-for-byte equal to the frozen
  outputs, with SHA-256 values
  `684c0370c941b7081d9c32f33a9e9734cde011d00d55ba73d74cca2fbb11ffa9`
  and
  `dd905a427df92fd45c2b0ed66d15d2ae75a75564a546570d408fdeceddf876e7`.
- As a separate enumeration check through the first possible survivor size,
  I used raw chamber sets as the orbit key (rather than the cut-signature
  descriptor) and deliberately did not apply the interface-mismatch pruning.
  Through four units this over-enumeration found 1, 2, 7, and 41 raw orbit
  classes; filtering afterward gave the certificate's 1, 2, 4, and 17
  compatible classes and 1, 2, 2, and 10 convex classes.  Its only ideal
  right-angled outputs were again the `[4]` and `[1,1,1,1]` four-unit
  octahedra.  This check is supplementary; the seven-unit completeness rests
  on the audited interface and block-graph lemmas above.
- I attacked missed finite vertices and wrong dihedral angles.  For a convex
  finite union of finite-volume chambers, every actual boundary vertex is the
  intersection of an independent triple of supporting planes and has
  nonpositive Lorentz norm.  Thus an actual finite vertex cannot evade the
  triple enumeration.  Every boundary edge has two recovered endpoints, and
  orthogonality of its two facet normals is exactly the right-angle condition.
- Targeted current searches for `SW2`, Conjecture 7.11, bounded chamber
  classifications, and quarter-octahedron censuses found the cited arXiv v1
  but no separate primary source containing this bounded theorem.  This is
  only a limited nonduplication check, not a priority guarantee.

## Contribution and limitations

The nearest source result supplies canonical blocks but performs no bounded
assembly census.  The accepted delta is a genuine exact lower bound on a
possible counterexample: none can use one through seven quarter units (at
most 84 SW2 chambers), and the unique admissible polyhedron in that range is
the 48-chamber octahedron.  Covering both source branches, including the
non-face-to-face mixed canonical decomposition, is not a routine restatement
of Proposition 7.10 and gives a credible base case and validation target for
larger searches.

No argument here bounds a minimal counterexample globally, handles more than
84 chambers, or proves that arbitrary quarter-octahedron assemblies arise in
the SW2 tiling.  The original Conjecture 7.11 is therefore explicitly and
correctly left unresolved.  Within the frozen bounded scope, I found no
mathematical or evidentiary gap requiring revision.
