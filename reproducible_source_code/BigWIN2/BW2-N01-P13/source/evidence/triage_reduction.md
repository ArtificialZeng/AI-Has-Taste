# Exact bounded orbit test

Job: `newwin-00001-p13-triage-16d0b42a11dd`. Date: 2026-09-12.
Reproduce: `python3 evidence/triage_orbits.py` (Python standard library only).
The script rewrites `connected_orbits.json` and `triage_test_results.json`.

## Reduction and degree justification

For an exact support S subset B, take its bipartite graph with nonisolated row
and column vertices. Row/column diagonal scaling acts on matrices of this exact
support. On a connected component with r rows, c columns and component rank D,
every orbit has size x^(r+c-1), x=q-1. Indeed the stabilizer consists of the
common nonzero scalar on every vertex. Ranks add across disjoint components.
After division by x^i in M_i, the component's factor is

    x^e O_D(G,x+1),       e = r+c-D-1.

Since D <= min(r,c), e >= max(r,c)-1 >= 0. Thus only components with r,c <= 3
can survive modulo x^3. Isolated vertices contribute 1 and are omitted; arbitrary
disjoint edges have e=0 and cannot be discarded. Positive defects add, so the
surviving patterns are one component of defect two, up to two components of
defect one, or no positive-defect component, together with disjoint edges.
This is a direct consequence of Chen--Selover (3.2), not claimed new.

Fix a spanning tree of a connected support. Successive diagonal scalings make
all tree entries 1, uniquely up to the common scalar, which acts trivially.
The beta = |E|-r-c+1 other entries are free nonzero field elements. Consequently
O_D is precisely a rank count among (q-1)^beta normalized matrices and
0 <= O_D(G,x+1) <= x^beta on the unbounded prime-power domain.

We use the published small-board polynomiality (Remark 2.3 and its use in the
proof of Theorem 3.12) for these components. Equivalently, exact-support counts
are obtained by finite inclusion-exclusion from polynomial small-board counts,
and division by the orbit-size power gives their orbit polynomials. This is an
explicit literature dependency, not inferred from sampling. The growth bound
then proves degree at most beta <= 4. Therefore beta+1 distinct exact field
counts determine the whole polynomial; rational Lagrange interpolation is
justified here. All reconstructed coefficients were integers. Extra prime-field
evaluations check the reconstruction. Without the cited polynomiality this
interpolation would not be a certificate for all prime powers.

## Coverage and outcomes

Enumerating all binary masks with 1 <= r,c <= 3, retaining connected supports
with no isolated vertices, and quotienting by independent row and column
permutations gives 28 graph classes (transposition is not identified). By ordered
dimensions 1x1,1x2,1x3,2x1,2x2,2x3,3x1,3x2,3x3 the counts are
1,1,1,1,2,4,1,4,13. There are 28 nonzero graph/rank types with defect <=2:
1 at defect zero, 4 at defect one, and 23 at defect two.

Every representative was gauge-enumerated over F_p for p=2,3,5,7,11,13.
Reconstruction uses the first beta+1 primes; unused primes serve as extra checks.
The largest gauge search has 12^4=20,736 assignments. Exact integer arithmetic
and modular Gaussian elimination are used throughout.

For each n=1,2,3, every one of the 2^(n^2) boards was evaluated via component
convolution and subset zeta transformation. This covers 530 boards and 2,100
board/index pairs. No negative c_2 occurred. Constant terms agree with direct
permutation-hit enumeration for every pair. These are finite observations with
the stated literature dependency, not universal positivity.

An additional enumeration of every n by n matrix over F_2 and F_3 gives 4,200
exact support/rank comparisons against the full reconstructed orbit polynomials;
all agree. The two paths enumerate different spaces but share the rank routine,
so this is not an independent-code or referee audit. There are also 4,200
normalized M_i residue checks; the F_2 congruence modulo 1 is vacuous, whereas
the full exact-count comparisons at F_2 and the F_3 congruences are substantive.

Empty/full board H-series give the sole nonzero entry at d=0/n, respectively:
[1,0,0] for n=1, [2,3,1] for n=2, and [6,27,50] for n=3. These agree with the
expansion of q^(n(n-1)/2)[n]!_q and check the transform normalization.

## Remaining gap

The local orbit polynomials need not have nonnegative coefficients: for full
2x2 support and rank two, O_2=x-1. Thus the orbit decomposition is not already
a termwise positivity proof. Controlling cancellations after the hit transform
remains necessary. The next finite discriminator is the exhaustive n=4 residue
calculation, with any negative witness reconstructed exactly. No n>=4 test,
novelty claim, independent referee acceptance, or manuscript is asserted here.
