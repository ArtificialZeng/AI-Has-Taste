# Exact source candidate for the second adjacent positive-x cell

Date: 2026-08-26. Status: **strict exact source candidate, pending an
independent literal-free no-import referee**. The predecessor cell ending at
`x=627/1000` is itself a frozen source candidate and is not treated here as
an independently audited theorem. No ledger, release, PDF, ZIP, or previously
frozen artifact is modified.

## 1. Statement and scope

Fix

```text
627/1000 <= x <= 63/100,
-1/100 <= y <= 1/100,
Z=z^2=1/8,
0<h<=1, lambda>0.
```

For both signed `z` lifts, the source candidate proves strict positivity of
the original fully conjugated Hermitian scalar gate throughout this complete
continuum. It is not a full compact-ball, unrestricted common-metric,
arbitrary-node, arbitrary-dimensional, or fixed-lens-optimum theorem.

## 2. Exact legality and original gate

With `S=h^2`, exact endpoint arithmetic gives

```text
D=1-x^2-y^2-Z
 >=1-(63/100)^2-(1/100)^2-1/8
 =239/500>0.
```

For `j=(1+5x)/(3 sqrt(5))`, `k=(-3+5y)/(3 sqrt(5))`, and
`ell^2=5/72`, definition-level reconstruction from the signed compact frame
gives

```text
det(C)=(5/72)S>0,
Re(Qp)_1=-(5 sqrt(6)/36)lambda*S*D<0.
```

The source reconstructs both signed Gram-column factorizations, `Q=lambda H`,
all nine entries of `Q^2`, the fully conjugated raw gate, and its independent
cyclic-vector form. Thus the cell is strictly legal, strictly dangerous,
rank two, and valid for both signs of `z` throughout the full admissible
positive shape-scale range.

## 3. Five exact lambda groups

Write `36 Gamma=sum_(k=0)^4 C_k(S,x,y)lambda^k`. The source proves
`C_0=5` and exact divisibility of every `C_k`, `k>=1`, by `S`. Map the cell by

```text
y=-1/100+u/50,
x=627/1000+3v/1000,
0<=S,u,v<=1.
```

Exact trivariate power-to-Bernstein conversion gives:

| group | source terms | degree `(S,u,v)` | controls | all global minima |
|---|---:|---:|---:|---|
| `C_0` | 1 | `(0,0,0)` | 1 | `(0,0,0): 5` |
| `C_1/S` | 5 | `(0,2,2)` | 9 | `(0,2,2): 101/150` |
| `C_2/S` | 26 | `(1,4,4)` | 50 | `(0,4,0): 39447892217179/3240000000000` |
| `C_3/S` | 42 | `(2,6,6)` | 147 | `(0,6,0): 533736176784030589/972000000000000000` |
| `C_4/S` | 120 | `(3,8,8)` | 324 | `(0,8,0): 6540698095666461427781281/1749600000000000000000000` |

Each displayed minimum is unique. All `531/531` controls are strictly
positive, giving a continuum proof for every physical `S>0` and
`lambda>0`.

## 4. Exact seam

At new coordinate `v=0`, the parameter equals the previous cell at its
coordinate `v=1`, namely `x=627/1000`. The source proves the raw-gate identity
before coefficient extraction. It also independently recomputes all five
predecessor Bernstein tensors on

```text
x=313/500+v/1000
```

and proves every new left-boundary control equals its corresponding previous
right-boundary control. Hence parameter, raw-gate, and control seams pass
exactly; this is not a sampled endpoint comparison.

## 5. Counterexample track and classification

The 81 exact rational diagnostic nodes are all positive, with minimum

```text
52508145177968978999/10497600000000000000 > 0.
```

The nodes are falsification diagnostics only. Exact classification is:

```text
chart illegality:              absent,
Bernstein certificate failure: absent,
implementation/resource failure: absent in the frozen run,
legal raw-gate negative:        absent.
```

No numerical evidence is promoted to a theorem, and no CE-046/048/059/060
route is reused.

## 6. Replay and next gate

From the workspace root run

```text
.venv/bin/python -B -u \
  tmp/research/compact_ball_uncovered_box_x5_8_xy_adjacent_x63_100_exact_gate.py
```

The frozen source attacks reject optimized Python, a false predecessor hash,
altered normalization, deletion of `Q^2`, reversal of the danger sign,
coefficient corruption, deletion of a Bernstein control, and a broken seam.
The separate source-freeze verifier rejects an altered source hash and a
damaged manifest. External-cache `py_compile` passes.

Promotion requires a new independent no-import referee that treats the
source and manifest as opaque hashes, reconstructs the raw gate and five
coefficient groups without importing source controls, and independently
recovers all 531 controls and the complete seam.
