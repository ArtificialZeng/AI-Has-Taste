# Exact cubical-chain checks

## Reproducer

`evidence/anchored_cubical.py` enumerates the product cells of Definition 4.13
directly.  A factor is either a vertex or an oriented edge; a cell is retained
exactly when each anchor occurs as a vertex factor.  If the edge factors occur
in coordinate positions (j_1<\cdots<j_d), the boundary of the factor at
(j_a) has sign ((-1)^{a-1}) and replaces the oriented edge by head minus
tail.

The script checks (partial^2=0).  It selects a spanning forest of the
1-skeleton.  The nonforest 1-cells index the fundamental-cycle integral basis
of (ker\partial_1); the coordinates of a 2-boundary in this basis are exactly
its coefficients on those nonforest cells.  Thus the Smith form reported for
this restricted matrix is the Smith form computing
(ker\partial_1/\operatorname{im}\partial_2=H_1), not merely the Smith form
of an isolated boundary matrix.

For example, the exact two-anchor computation is reproduced by

```sh
python3 evidence/anchored_cubical.py \
  --graph k4 --anchors 0,1 --n 4 \
  --primes 2,3,5,7,101,1000003 --smith
```

## Smallest connected cographs outside trees and circles

On four vertices, the connected cographs which are neither trees nor geometric
circles are the paw, the diamond, and (K_4).  The named graph encodings in the
script are

- paw: edges (01,02,03,12), with one-anchor orbit representatives
  (0,1,3);
- diamond: (K_4\setminus\{23\}), with representatives (0,2);
- (K_4): one anchor orbit, represented by (0).

For every one-anchor representative at (n=3), exact Smith normal form gave
only unit nonzero factors:

| graph / anchor | cell counts ((C_0,C_1,C_2)) | cycle matrix | Smith diagonal | ((\beta_0,\beta_1,\beta_2)) |
|---|---:|---:|---:|---:|
| paw / 0, 1, or 3 | ((37,84,48)) | (48\times48) | (1^{45},0^3) | ((1,3,3)) |
| diamond / 0 or 2 | ((37,105,75)) | (69\times75) | (1^{63},0^6) | ((1,6,12)) |
| (K_4) / 0 | ((37,126,108)) | (90\times108) | (1^{81},0^9) | ((1,9,27)) |

Here the displayed zero exponent is the cokernel free rank; the kernel free
rank is (3,12,27), respectively.  In particular all six anchor-orbit cases
have torsion-free integral homology.  All six boundary-square checks passed.

For (K_4), (K=\{0,1\}), (n=4), the cell counts are
((110,432,432)).  The integral cycle lattice has rank (323), and the exact
(323\times432) Smith computation returned (311) nonzero diagonal entries,
all equal to (1).  Hence

\[
H_0\cong\mathbb Z,\qquad H_1\cong\mathbb Z^{12},\qquad
H_2\cong\mathbb Z^{121}.
\]

## Further exact finite-field checks

Ranks were recomputed by exact Gaussian elimination over each listed prime.
These are finite checks, not part of the proof of the universal theorem.

| graph, anchors, (n) | cell counts | integral/generic Betti ranks | primes with identical ranks |
|---|---:|---:|---|
| (K_4,\{0,1\},5) | ((570,3300,6480,4320)) | ((1,15,90,646)) | (2,3,5,7,101,1000003) |
| (K_4,\{0,1,2\},6) | ((2100,14040,32400,25920)) | ((1,18,135,5578)) | (2,3,5,101,1000003) |
| (K_4,V(K_4),6) | ((1560,8640,12960)) | ((1,18,5897)) | (2,3,5,7,101,1000003) |

The corresponding boundary ranks were, respectively,
((0,569,2716,3674)), ((0,2099,11923,20342)), and
((0,1559,7063)) over every displayed prime.  Thus no prime in these test sets
produced a rank jump.  The predicted ranks from decomposition (1) in
`evidence/torsion_free_proof.md` agree in every degree.

## Calibration cases

For the path (P_3), one anchor and (n=3), the script returned cell counts
((19,30,12)), Betti ranks ((1,0,0)), and boundary ranks independent of
(2,3,5,7,101,1000003).  For the triangle (a geometric circle), the analogous
values were cell counts ((19,45,27)) and Betti ranks ((1,3,3)).  These agree
with the known tree result and the elementary three-fold fat-wedge calculation.

All computations use integers or finite fields; there is no floating-point
step.  The universal torsion-free conclusion rests on the proof artifact, not
on this finite census.
