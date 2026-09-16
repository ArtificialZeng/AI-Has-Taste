# Exact reflective quarter-octahedron census through seven tiles

Provenance: `win-00069-p04-research-676ea17ad4ed`  
Executable certificate: `evidence/sw2_quarter_census.py`  
Deterministic output: `evidence/sw2_quarter_census.json`

## Scope

This certifies a finite subsidiary statement, not Conjecture 7.11:

> In the reflective tiling by the right-angled triangular bipyramid
> \(T=\tfrac14\mathcal O\), every convex union of at most seven \(T\)-chambers
> whose polyhedral vertices are all ideal and whose boundary dihedral angles
> are all right angles consists of four chambers and is an ideal right-angled
> octahedron.

Because the two quarter-octahedra in Proposition 7.10 have the same scale-free
Gram matrix, this statement applies up to isometry to either quarter used as a
reflective Coxeter chamber. It does **not** enumerate the potentially
non-reflective mixed quarter/half/octahedron decompositions in Proposition
7.10(2).

## Exact source reconstruction

Use Lorentz form \(\operatorname{diag}(-1,1,1,1)\). Oriented normals for the
four faces of SW2 are

\[
n_1=(0,-1,1,0),\quad n_2=(1,1,1,1),\quad
n_3=(0,0,0,-1),\quad n_4=(0,0,-1,1).
\]

Thus its Klein-model chamber is
\(x\ge y\ge z\ge0\), \(x+y+z\le1\). Exact Lorentz products give

\[
(m_{ij})=
\begin{pmatrix}
1&2&2&3\\2&1&4&2\\2&4&1&4\\3&2&4&1
\end{pmatrix},
\]

the face data determined in Section 7.4: the 1-3-4 subgroup is \(B_3\), the
1-2-4 subgroup has order 12, and the unique ideal 2-3-4 vertex has Euclidean
type \((2,4,4)\).

The script constructs reflection matrices by
\(R_nX=X-2\langle n,X\rangle n/\langle n,n\rangle\). It verifies exactly:

- \(\langle R_nX,R_nY\rangle=\langle X,Y\rangle\);
- \(\langle R_1,R_3,R_4\rangle\) has 48 chambers, whose boundary is the eight
  planes \((1,\pm1,\pm1,\pm1)\), with six ideal vertices and no finite vertex;
- \(\langle R_1,R_2,R_4\rangle\) has 12 chambers and boundary only of SW2
  face type 3;
- the sector \(x\ge |y|\) of the reconstructed octahedron has 12 SW2 chambers
  and no boundary face of type 3;
- both 12-chamber sectors have six faces, nine right-angled edges, three ideal
  vertices, two finite vertices, and isomorphic normalized Gram matrices.

This reconstructs the 48-chamber octahedron and both source-described
12-chamber copies of \(T\) without floating-point arithmetic.

## Exhaustiveness of the finite census

The six boundary normals of the no-face-3 copy of \(T\) generate its
right-angled reflection tiling. The script builds the complete Cayley ball of
radius six (2,060 chambers). Any connected union of at most seven chambers
containing the base chamber lies in this ball.

A chamber set is retained exactly when it is closed under every chamber on
every minimal gallery between each pair. For a Coxeter complex this is the
intersection-of-roots criterion, so its chamber union is convex. Starting with
the base chamber, the enumeration repeatedly adjoins every adjacent chamber
and takes this exact interval closure. If a target convex set has not yet been
reached, connectedness supplies an adjacent target chamber, and its interval
closure remains inside the target. Induction therefore enumerates every rooted
convex union in the stated size range. No quotient by the finite stabilizer is
needed; retaining symmetry duplicates makes the negative screen conservative.

For each retained union, outer chamber facets are merged by their primitive
integer Lorentz normal. Every boundary vertex is recovered as the projective
null vector of each independent triple of boundary planes and tested against
all oriented half-spaces. Its Lorentz norm distinguishes finite (negative) from
ideal (zero) vertices. Two facets form a boundary edge when they contain two
common recovered vertices; their exact Lorentz product must vanish for a right
angle. Euler characteristic, facet support, and four-valence at ideal vertices
are also checked.

## Result

The rooted convex-union counts for sizes 1 through 7 are respectively

\[
1,\ 6,\ 18,\ 57,\ 150,\ 450,\ 1218.
\]

Every retained union has a finite boundary vertex except three rooted unions
of size four. Each survivor has \((F,E,V)=(8,12,6)\), all six vertices ideal
and four-valent, and all twelve boundary edges right-angled. Its graph is the
octahedral graph, and its exact half-space data give an ideal right-angled
octahedron. Therefore there is no volume-obstruction counterexample in this
reflective range.

Re-running the certificate produced byte-identical JSON. SHA-256 values at the
checkpoint were:

- script: `a38e75265fd8d574c2393fee9e94348d888dc16616577070e299ec51892402e9`;
- JSON: `684c0370c941b7081d9c32f33a9e9734cde011d00d55ba73d74cca2fbb11ffa9`;
- immutable `source.md`: `dca4196df34842036dd339b43038065ab16b1f0d9d39ac60f956cdaeec3c7e92`.

