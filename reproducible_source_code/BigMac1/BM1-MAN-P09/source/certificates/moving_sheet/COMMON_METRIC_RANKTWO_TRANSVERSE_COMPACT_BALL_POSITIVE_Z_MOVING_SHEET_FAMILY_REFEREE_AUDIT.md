# Referee audit: strict positive-`Z` moving-sheet parametric family

## Verdict

**PASS**, independently of the source verifier's moving-map coefficient
assembly.  The theorem is a strict five-real-parameter partial theorem.  The
full compact ball, the unrestricted complex Hermitian/common-metric gate, the
fixed crossing-lens optimal constant, arbitrary normalized scale, and a full
positive-`Z` collar remain open.

## Audited statement

For

```text
0<S<=1/10000,
0<=X<=3/10000,
|M|<=1/1000,
|omega|,|nu|<=1/100,
```

put

```text
A=1+M,
lambda=A/S,
Y=S(12/(25A)+nu),
wc=-3(5MX-15M+5X-6)/(25A),
W=S(wc+omega),
Z=3X-X^2-Y^2+W,
x=-1/5+X,
y=3/5+Y.
```

The referee verifies exact legality, `0<Z<1/1000`, strict danger, rank-two
positive semidefiniteness, and strict positivity of the original scalar gate
`36 Gamma`.

## Independent reconstruction

The isolated referee

```text
audit/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_family_referee.py
```

imports neither the source verifier, any discovery script, nor any cached
quartic.  It performs the following checks from definitions.

1. It reconstructs the complete orthonormal transverse frame modulo
   `q^2+h^2=1`.
2. It uses the signed-`z` Cholesky factor

   ```text
   [[h,0],[j-i kappa,ell]]
   ```

   and explicitly obtains the two Gram columns.  It verifies sign symmetry
   in `ell`, the compact substitution `ell^2=(5/9)Z`, and
   `det C=(5/9)h^2 Z`.
3. It reconstructs the raw gate directly from `Q,Q^2` and independently from
   the constant/linear/quadratic Gram vector, then checks the two expressions
   term by term.
4. It independently recovers the danger identity and all rational legality
   reserves.
5. It reconstructs `N=S^3(36 Gamma)` from the independent vector quartic.
   Unlike the source's sparse moving-map assembly, it evaluates a full exact
   nodal tensor at eight nonzero `S` nodes and nine `X` nodes.  The safe raw
   degree forecast is `(7,8)`.  Exact Vandermonde inversion proves that every
   coefficient above the actual bidegree `(5,4)` vanishes and recovers exactly
   20 nonzero `(S,X)` coefficients.
6. Before the nodal inversion, it calibrates the optimized `d`-adic
   denominator clearing at the rational parameter point
   `(M,omega,nu)=(1/1000,1/100,-1/100)` directly against substitution in the
   original `N`.  It also asserts
   `8-2*zdegree-ydegree>=0` separately for every raw monomial.
7. From the nodally reconstructed coefficient polynomials it independently
   checks the nonnegative `H1`, the three strict `H2` reserves, all 947 exact
   parameter-monomial remainder bounds, and the C0/C1 margins.

The two projective charts are

```text
C0: X=S rho,   0<=rho<=1  (X<=S),
C1: S=X sigma, 0<=sigma<=1 (S<=X).
```

They overlap at `X=S`.  C0 contains `X=0` without division by `X`; C1 works
through `X=3/10000` and contains the old MAIN chart.  The actual theorem uses
`S>0`; `S=0` appears only as an algebraic closure used for coefficient
extraction.

## Exact reserves

The referee reproduces

```text
Z >= S * 7858868231111/11088900000000 > 0,
Z <= 974081/1001000000 < 1/1000,

1-x^2-y^2-Z
 >= 332826352979/555555000000
 > 299/500.
```

The common quadratic reserve is

```text
2564950982194530478444050838857341987999
/1274019840000000000000000000 > 0.
```

The exact final margins are

```text
C0:
2157675883946338861464573804693908853416834606352657354865271
/1074954240000000000000000000000000000000000000000 > 0,

C1:
89361321403752495288011515925096895113866165323668871164167
/44789760000000000000000000000000000000000000000 > 0.
```

## Raw PASS output

The ordinary source verifier returned

```text
PASS original Hermitian Q,Q^2 gate and positive-scale quartic
PASS exact map legality, 0<Z<1/1000, rank-two PSD
DANGER_RESERVE 332826352979/555555000000
C0 MARGIN 2157675883946338861464573804693908853416834606352657354865271/1074954240000000000000000000000000000000000000000
C1 MARGIN 89361321403752495288011515925096895113866165323668871164167/44789760000000000000000000000000000000000000000
PASS C0/C1 full remainder, overlap X=S, full rectangle covered
PASS strict raw 36Gamma for the positive-Z moving-sheet family
SCOPE parametric family only; full compact ball and fixed lens open
```

The independent referee returned

```text
PASS independent signed-z two-column Gram and Q,Q^2 reconstruction
PASS independent positive-Z, danger, lambda and rank-two legality
PASS d-adic/direct raw N calibration
NODAL_ROW 1/8 PASS
NODAL_ROW 2/8 PASS
NODAL_ROW 3/8 PASS
NODAL_ROW 4/8 PASS
NODAL_ROW 5/8 PASS
NODAL_ROW 6/8 PASS
NODAL_ROW 7/8 PASS
NODAL_ROW 8/8 PASS
PASS 72-node exact inversion; high safe-degree coefficients vanish
PASS independent C0/C1 reserves and complete ordered cover
PASS independent strict positive-Z moving-sheet family
controls=947 nodal_values=72
scope=parametric family only; full compact ball and fixed lens open
```

Both verifiers raise immediately under `python -O`; the ordinary runs exit
zero and the optimized runs exit nonzero.  No numerical sampling is used as
proof, and no fixed `s=-2` allocation or CE-046/CE-048/CE-059 route enters the
argument.
