# A seven-sign active-block `t` layer of radius `50/919`

Date: 2026-08-24. Status: **exact source-verified computer-assisted partial
theorem; independent referee audit accompanies this note**. The unrestricted
complex Hermitian gate, common-metric theorem, and fixed crossing-lens problem
remain open.

Fix `a=3/5`, `c=4/5`, and quantify over

```text
ell in [8,10],                 w in [-31/100,-29/100],
k   in [-301/100,-299/100],   z in [-101/100,-99/100],
r   in [99/100,103/100],      t in [3626/919,3726/919].
```

Thus `|t-4|<=50/919`, an exact enlargement of the independently audited
`21/386` box by the strict width difference `1/354734`. Put, for `T>0` and
`s=sqrt(T)`,

```text
Delta = r*t-z^2-w^2,
n     = t*(k^2+ell^2)+r-2*(k*z+ell*w),
g     = (12/25)*ell-z*k-w*ell-t,
Q     = [[r, s(k+i ell), z+i w],
         [s(k-i ell), T*n/Delta, s],
         [z-i w, s, t]].
```

The active `(1,3)` block is positive definite, the scalar Schur complement
vanishes, and `Q` is Hermitian PSD of rank two. The exact complementary strict
branch is `T>0` when `g<=0`, and `T>Delta*g/n` when `g>0`. For every datum in
the box and every such legal scale, the fully conjugated original scalar gate
satisfies `G(Q)>0`; the corresponding closure endpoint is also positive.

## Exact proof gate

Direct extraction from the original Hermitian formula, independently matched
to a phase-retaining residual-square calculation, gives

```text
4*Delta^2*G(Q) = P(T) = C0+C1*T+C2*T^2+n^2*T^3,
C2 = Delta^2*(k^2+ell^2)-2*Delta*g*n.
```

At `TL=Delta*g/n`, `P(TL)=N0/(15625*n^2)` and
`P'(TL)=N1/(625*n)`. The complete terminal DAG uses exactly seven signs:
`danger,Delta,n` for legality; `Delta,n,C0,C1` for the `g<=0` coefficient
proof; `Delta,n,N0,N1` for the `g>0` endpoint and slope; and `Delta,n` for
curvature. On the latter branch,

```text
C2+3*n^2*TL = Delta^2*(k^2+ell^2)+Delta*g*n > 0.
```

Thus `P` is strictly convex and increasing from a positive legal endpoint.
No discriminant, `N_D`, real-part monotonicity, absorption, fixed allocation,
or recorded rejected route is used.

## Fresh `50/919` derivative certificate

The `r` interval is the union of the two closed cells `[99/100,101/100]` and
`[101/100,103/100]`. Starting from the original six-variable terminal
polynomials, the source verifier freshly recomputes these absolute
power-monomial derivative majorants on the new `t` box:

```text
danger = 0
Delta  = 103/100
n      = 1090601/10000
C0     = 11404252065866480644154263/9701894487500000000000
C1     = 63240091596317932598765281/9701894487500000000000
N0     = 16786355916991080483662571267021485103714617907961/
         2097623477825916800000000000000000000
N1     = 2246996618286131674656545174980863/
         1241842494400000000000000
```

All fourteen exact center-minus-radius-times-majorant reserves are strictly
positive. In the order `danger,Delta,n,C0,C1,N0,N1`, they are

```text
low cell:
93/500,
12809761/4595000,
655745491/2297500,
242925468045042215653163747409/891604103401250000000000000,
536600575672403488016095079753/891604103401250000000000000,
271024413499730373992194599135992059116129594487/
  24096449701525219240000000000000000000000,
527592607098284468088362545547608061/
  7132832827210000000000000000;

high cell:
87/500,
13177361/4595000,
655791441/2297500,
262886764340622837232304997121/891604103401250000000000000,
583519690684298422184716005553/891604103401250000000000000,
695222565537315762990076093059939765373235563737587/
  24096449701525219240000000000000000000000,
595031495123164277277188869161948311/
  7132832827210000000000000000.
```

The unique finite bottleneck remains low-cell `N0`, with the freshly
recomputed wider-box value

```text
rho_wide =
22832956414652720419288572875925058067205119308096 /
419658897924777012091564281675537127592865447699025
          > 50/919.
```

The exact comparison cross-product is
`542048826999460747984389198271984118232259188974>0`.

## Independent reconstruction and phase attack

The independent referee imports neither source verifier nor discovery code.
It reconstructs the original gate and scale cubic, recomputes both `t=4`
center tensors by exact nodal Bernstein inversion and inverse replay, and
checks `40,595` strictly positive controls in each `r` cell. It also attacks
all `96` exact endpoint/seam cases, split `48+48` between the two `g` branches.
These finite cases are diagnostic; continuum coverage comes from the two
exact tensors and fourteen derivative reserves.

At the upper endpoint the live opposite-phase datum

```text
ell=9, w=-31/100, k=-301/100, z=-101/100,
r=103/100, t=3726/919, T=1
```

is strictly legal and has

```text
G(Q)=60746927109990602200372569492531/
  16695493268772709728100000000 > 0,
4*(G(Q)-G(Re Q))=-184269381654495888525183/
  118744947221210000000 < 0.
```

Thus phase erasure is unavailable. Both verifiers fail closed under optimized
Python, dependency tampering, and terminal-sign deletion. This theorem is only
the stated seven-real-parameter island (six bounded shape coordinates plus
every legal coupling scale); it does not prove the general complex Hermitian
gate, common-metric theorem, all-node bridge, or fixed-lens statement.
