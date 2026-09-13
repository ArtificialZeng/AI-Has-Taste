# A seven-sign active-block `t` layer of radius `5/92`

Date: 2026-08-24. Status: **exact source-verified computer-assisted partial
theorem; independent referee audit accompanies this note**. The unrestricted
complex Hermitian gate, common-metric theorem, and fixed crossing-lens problem
remain open.

Fix `a=3/5`, `c=4/5`, and quantify over

```text
ell in [8,10],                 w in [-31/100,-29/100],
k   in [-301/100,-299/100],   z in [-101/100,-99/100],
r   in [99/100,103/100],      t in [363/92,373/92].
```

Thus `|t-4|<=5/92`, an exact enlargement of the independently audited
`2/37` box.  Put, for `T>0` and `s=sqrt(T)`,

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

## Fresh `5/92` derivative certificate

The `r` interval is covered by the two closed cells
`[99/100,101/100]` and `[101/100,103/100]`.  Starting from the original six-
variable terminal polynomials, the source verifier recomputes the following
absolute power-monomial bounds on the full new `t` box:

| sign | recomputed `M` |
|---|---:|
| danger | `0` |
| `Delta` | `103/100` |
| `n` | `1090601/10000` |
| `C0` | `178768417937073716969/152087500000000000` |
| `C1` | `1982672114117030883131/304175000000000000` |
| `N0` | `659257646688669038744800158786579605896183/82385190400000000000000000000` |
| `N1` | `140892023457352044459673332201/77868800000000000000` |

All fourteen exact reserves `m-(5/92)M` are strictly positive.  In the order
`danger,Delta,n,C0,C1,N0,N1`, they are

```text
low cell:
93/500,
641199/230000,
262589547/920000,
23832861558346092019441/87450312500000000000,
421321424647050445290451/699602500000000000000,
96145360217431855882905344352972293637221/
  189485937920000000000000000000000,
13267008990845903837618573613659/179098240000000000000000;

high cell:
87/500,
659599/230000,
262607947/920000,
25790705395419633264029/87450312500000000000,
458136789263353765094051/699602500000000000000,
5560997909448393192811384868142570554242021/
  189485937920000000000000000000000,
14960331468100346901412418109659/179098240000000000000000.
```

The unique finite ratio bottleneck remains the low-cell `N0`, but with a
freshly recomputed wider-box value

```text
rho_wide =
896775556481533279336770926007341554681088 /
16481441167216725968620003969664490147404575
          > 5/92.
```

This recomputation, rather than the older `rho_new`, proves the enlargement.

## Phase and falsification checks

Both phases remain nonzero and opposite: `-31/10<=ell*w<=-58/25<0`.
At the new upper endpoint, the exact datum

```text
ell=9, w=-31/100, k=-301/100, z=-101/100,
r=103/100, t=373/92, T=1
```

is strictly legal and has

```text
G(Q)=659709262001662465543697/181310688232200000000 > 0,
4*(G(Q)-G(Re Q))=-226554899274721441/145993420000000 < 0.
```

Thus phase erasure is unavailable.  The independent referee also attacks all
96 exact endpoint/seam cases.  Those points are diagnostics; the continuum
proof is furnished by the two reconstructed center tensors and fourteen
fresh derivative reserves.

Run

```text
.venv/bin/python -B \
  tmp/research/verify_common_metric_tilted_rankone_complex_scale_t5over92_enlargement.py
```

The theorem is only this seven-real-parameter island (six bounded shape
coordinates plus every legal coupling scale).  It does not prove the general
complex Hermitian gate or any later common-metric, all-node, or fixed-lens
statement.
