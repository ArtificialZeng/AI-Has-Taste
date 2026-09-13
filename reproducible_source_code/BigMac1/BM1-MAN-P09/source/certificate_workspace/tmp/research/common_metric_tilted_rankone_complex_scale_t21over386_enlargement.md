# A seven-sign active-block `t` layer of radius `21/386`

Date: 2026-08-24. Status: **exact source-verified computer-assisted partial
theorem; independent referee audit accompanies this note**. The unrestricted
complex Hermitian gate, common-metric theorem, and fixed crossing-lens problem
remain open.

Fix `a=3/5`, `c=4/5`, and quantify over

```text
ell in [8,10],                 w in [-31/100,-29/100],
k   in [-301/100,-299/100],   z in [-101/100,-99/100],
r   in [99/100,103/100],      t in [1523/386,1565/386].
```

Thus `|t-4|<=21/386`, an exact enlargement of the independently
audited `13/239` box.  Put, for `T>0` and `s=sqrt(T)`,

```text
Delta = r*t-z^2-w^2,
n     = t*(k^2+ell^2)+r-2*(k*z+ell*w),
g     = (12/25)*ell-z*k-w*ell-t,
Q     = [[r, s(k+i ell), z+i w],
         [s(k-i ell), T*n/Delta, s],
         [z-i w, s, t]].
```

The active `(1,3)` block is positive definite, the scalar Schur complement
vanishes, and `Q` is Hermitian PSD of rank two.  The exact complementary
strict branch is

```text
T>0                    when g<=0,
T>Delta*g/n            when g>0.
```

For every datum in the box and every such legal scale, the fully conjugated
original scalar gate satisfies `G(Q)>0`.  Positivity also holds at the closure
endpoint `T=0` or `T=Delta*g/n`, as applicable.

## Exact proof gate

Direct extraction from the original Hermitian formula, independently matched
to a phase-retaining residual-square calculation, gives

```text
4*Delta^2*G(Q) = P(T) = C0+C1*T+C2*T^2+n^2*T^3,
C2 = Delta^2*(k^2+ell^2)-2*Delta*g*n.
```

At `TL=Delta*g/n`, write

```text
P(TL)=N0/(15625*n^2),       P'(TL)=N1/(625*n).
```

The complete terminal DAG uses exactly seven signs:

```text
danger, Delta, n                  -> legality,
Delta, n, C0, C1                 -> g<=0 coefficient proof,
Delta, n, N0, N1                 -> g>0 endpoint and slope,
Delta, n                         -> g>0 curvature.
```

For `g>0`, the curvature identity is

```text
C2+3*n^2*TL = Delta^2*(k^2+ell^2)+Delta*g*n > 0.
```

Hence `P` is strictly convex and increasing from a positive legal endpoint.
No discriminant, `N_D`, real-part monotonicity, absorption, fixed allocation,
or cited route obstruction is used.

## Fresh `21/386` derivative certificate

The `r` interval is covered by the two closed cells
`[99/100,101/100]` and `[101/100,103/100]`.  Starting from the original six-
variable terminal polynomials, the source verifier recomputes the following
absolute power-monomial bounds on the full new `t` box:

| sign | recomputed `M` |
|---|---:|
| danger | `0` |
| `Delta` | `103/100` |
| `n` | `1090601/10000` |
| `C0` | `13203880792373560734953/11232901562500000000` |
| `C1` | `9152452867325244357267/1404112695312500000` |
| `N0` | `3428738228412320387037179940413870154192337351/428456294708800000000000000000000` |
| `N1` | `1300790062402578390419242978389/718905700000000000000` |

All fourteen exact reserves `m-(21/386)M` are strictly positive.  In the order
`danger,Delta,n,C0,C1,N0,N1`, they are

```text
low cell:
93/500,
336274/120625,
220342139/772000,
472547713172842810833090329/1734360001250000000000000,
1043834928133214098868089393/1734360001250000000000000,
144295501214656178400409723533261255647808421/
  4134603243939920000000000000000000000,
2052705559743129424971457960811557/27749760020000000000000000;

high cell:
87/500,
345924/120625,
220357579/772000,
511376688652080484103904201/1734360001250000000000000,
1135102606310394757177559193/1734360001250000000000000,
119387957198385910350934165825941692113228168221/
  4134603243939920000000000000000000000,
2315071579533623756456975269732057/27749760020000000000000000.
```

The unique finite ratio bottleneck remains the low-cell `N0`, but with a
freshly recomputed wider-box value

```text
rho_wide =
4663813122843737977650051498551334435768458336 /
85718455710308009675929498510346753854808433775
          > 21/386.
```

The exact comparison has positive cross-product
`144295501214656178400409723533261255647808421`.  This new-box
recomputation, rather than the older `rho_wide`, is the source certificate for
the enlargement.

## Phase and falsification checks

Both phases remain nonzero and opposite: `-31/10<=ell*w<=-58/25<0`.
At the new upper endpoint, the exact datum

```text
ell=9, w=-31/100, k=-301/100, z=-101/100,
r=103/100, t=1565/386, T=1
```

is strictly legal and has

```text
G(Q)=29541387207997411577757671059/
  8119057735779760900000000 > 0,
4*(G(Q)-G(Re Q))=-853391406768747308637/
  549933433790000000 < 0.
```

Thus phase erasure is unavailable.  The independent referee also attacks all
96 exact endpoint/seam cases.  Those points are diagnostics; the continuum
proof is furnished by the two reconstructed center tensors and fourteen
fresh derivative reserves.

Run

```text
.venv/bin/python -B \
  tmp/research/verify_common_metric_tilted_rankone_complex_scale_t21over386_enlargement.py
```

The theorem is only this seven-real-parameter island (six bounded shape
coordinates plus every legal coupling scale).  It does not prove the general
complex Hermitian gate or any later common-metric, all-node, or fixed-lens
statement.
