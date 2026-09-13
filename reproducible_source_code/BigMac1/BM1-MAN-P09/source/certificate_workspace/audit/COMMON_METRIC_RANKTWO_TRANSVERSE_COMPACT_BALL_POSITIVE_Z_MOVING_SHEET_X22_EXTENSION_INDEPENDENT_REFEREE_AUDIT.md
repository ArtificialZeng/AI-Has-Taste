# Independent referee audit: moving-sheet extension through `X=1/22`

Date: 2026-08-24.

## Verdict

**PASS as an exact strict computer-assisted partial theorem on the stated
moving sheet.**

For every

```text
0<S<=1/10000,
1/23<=X<=1/22,
|M|<=1/1000,
|omega|,|nu|<=1/100,
```

and either real sign of `z` satisfying the displayed relation `z^2=Z`, the
definition-level reconstruction proves legality, rank two, strict compact-ball
danger, and strict positivity of the fully conjugated original gate. This does
not prove the full compact-ball quartic, the unrestricted complex Hermitian
gate, the common-metric theorem, or the fixed crossing-lens constant.

The independent verifier is

```text
audit/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x22_extension_independent_referee.py
```

It imports no candidate verifier, discovery module, cached quartic, or cached
coefficient table.

## Reconstruction from definitions

Starting from the displayed vectors `r0,f_h`, the referee independently
checks, modulo only `q^2=1-h^2`, that both vectors are unit, mutually
orthogonal, and orthogonal to the unit kernel vector

```text
n=(c*q*conjugate(zeta), h*conjugate(zeta), a*q).
```

It forms the `2 x 2` compression `C`, `H=U C U*`, `Q=lambda H`, the fully
conjugated square `Q^2`, and the two indexed leakage coordinates in the
original gate. Independently, if `v=Hp`, it forms the three-component Gram
vector

```text
B0 = (i*a*c, 0, 0),
L  = (c*conjugate(v1)+a*v3, c*conjugate(v2), 2*a*v2),
R  = (-i*(H^2)_31, -i*(H^2)_32, 0).
```

Coefficientwise reduction proves

```text
4*G(lambda H)
 = ||B0+lambda*L+lambda^2*R||^2
   -32*a^2*lambda^2*(Re(Hp)_1)^2.
```

All occurrences of the transverse radicals cancel after the relations
`q^2=1-S`, `h^2=S`, and `z^2=Z`; no sign of `z` is selected. The result is a
quartic in `lambda`, and `36*(4G)` has constant term `5`. Thus both real signs
of `z` are covered by the same identity.

## Quantifiers, legality, and rank

The scale numerator satisfies

```text
A=1+M >= 999/1000 > 0.
```

Because the theorem assumes `S>0`, `lambda=A/S>0` and
`lambda*S=A in [999/1000,1001/1000]`. The value `S=0` is expressly excluded:
it is only a polynomial closure point and does not define `lambda`. No result
at `S=0` is inferred by continuity.

Independent endpoint monotonicity gives

```text
y0 >= 46999/100100 > 0,
wc+omega >= 27743/40700,
wc+omega-S*y0^2
 >= 83142836564221/121977900000000 > 0.
```

Since `3X-X^2` increases on the stated cell and `S>0`,

```text
68/529 < Z.
```

The referee obtains the sharper coordinated upper envelope
`1479524961/11011000000`; it then independently verifies the candidate's
slightly looser recorded bound

```text
Z <= 1479554991/11011000000 < 1/7.
```

The exact identity

```text
x^2+y^2+Z = 2/5+(13/5)X+(6/5)Y+Wsh
```

gives

```text
1-x^2-y^2-Z
 >= 267603185879/555555000000 > 0.
```

This is strict compact-ball danger on the entire box. Finally,

```text
C_11=S>0,
det C=(5/9)SZ>0.
```

Hence `C` is positive definite, `U` is an isometry, and `Q=lambda U C U*`
is Hermitian PSD of rank exactly two with the displayed one-dimensional
kernel. This proof divides by no cap coordinate. The only divisions used in
the sign certificate are by `A`, `S`, and later `X`; all three are separately
proved strictly positive. In particular there is no division by `z`, `Z`, or
`Z-1/8`.

## Independent continuum certificate

After the moving substitution, set

```text
N=S^3*(36*(4G)),
D=25^8*(1+M)^8,
Qhat=D*N/S^2.
```

The referee reconstructs this expression directly from its new original-gate
quartic and verifies the lossless identity

```text
36*(4G)=Qhat/[25^8*(1+M)^8*S].
```

The quotient has exactly twenty `(S,X)` terms and bidegree `(5,4)`. Its first
layer is

```text
25^8*M^2*S*(1+M)^8*(5M^2+14M+14) >= 0.
```

The three centered lower bounds for the quadratic layer
`a2*S^2+b2*S*X+c2*X^2` are all strictly positive. In particular,

```text
c2 >= c0 =
2564950982194530478444050838857341987999
/1274019840000000000000000000.
```

The actual domain has the lossless coordinate `S=sigma*X` with

```text
0<sigma<=23/10000.
```

After division by positive `X^2`, the referee retains all sixteen higher
`(S,X)` terms. Their coefficients contain exactly 947 centered
`(M,omega,nu)` monomials. Direct absolute centered bounds give

```text
Rabs =
45501595887352000690514390785303819932610237699051256372767272123253
/16648891269120000000000000000000000000000000000000000000000.
```

Even after discarding the other nonnegative layers, the strict reserve is

```text
c0-Rabs =
33473277839430772291616341971402441279238321762300948743627232727876747
/16648891269120000000000000000000000000000000000000000000000 > 0.
```

Since the cleared denominator is strictly positive, this proves the original
gate, not a surrogate polynomial.

## Closed endpoints and falsification

At

```text
S=1/10000, M=-1/1000, omega=nu=-1/100,
```

the exact left endpoint `X=1/23` has

```text
Z=7544457381633363719/58660281000000000000,
1-x^2-y^2-Z=6214407683/12765000000,
36*(4G)=
2851967535986553322459201051507517913149039
/11193640000000000000000000000000000000000 > 0.
```

The right endpoint `X=1/22` has

```text
Z=1802860823780958431/13417569000000000000,
1-x^2-y^2-Z=2940739181/6105000000,
36*(4G)=
14817150110247071841775080222180418970749
/53240000000000000000000000000000000000 > 0.
```

A separate exact falsification grid uses

```text
S in {1/10000,1/20000,1/100000},
X in {1/23,45/1012,1/22},
(M,omega,nu) at all eight box corners.
```

All 72 nodes are legal and have positive original gate. The minimum is the
displayed left-endpoint value. This grid is falsification evidence only; the
continuum proof is the exact envelope above.

## Stitch attribution and integrity

The independently audited predecessor proves the closed cell
`1/24<=X<=1/23` and attributes its lower continuation to the earlier audited
moving-sheet cells. The new closed cell contains the common face `X=1/23`.
Consequently the predecessor and present theorem stitch exactly, with no
limit argument, to the same family on `0<=X<=1/22`. The present verifier
directly proves only the new cell `1/23<=X<=1/22`; the lower interval is a
hash-bound predecessor dependency.

Both the nine-entry candidate manifest and the three-entry predecessor
independent-referee manifest verified with exit `0`. The older global
`CHECKPOINT_MANIFEST.sha256` currently exits `1` because the live
`APPROACH_REGISTRY.md`, `CLAIM_LEDGER.md`, `COUNTEREXAMPLE_DB.md`, and
`research_state.json` differ from that frozen checkpoint. None of those four
files was used as a proof dependency or modified by this audit.

Fail-closed tests:

```text
normal exact run                         exit 0, real 160.70 s
python -O                               exit 1
X22_REFEREE_BAD_DEPENDENCY=1            exit 1
X22_REFEREE_DROP_TERM=1                 exit 1, real 163.31 s
candidate manifest verification         exit 0
predecessor referee manifest            exit 0
```

The drop-term test removes one of the twenty reconstructed quotient terms and
fails at the exact support-completeness gate. No proof assistant was used;
this is an exact rational/SymPy computer-assisted partial theorem.
