# Exact source candidate for the adjacent positive-x compact-ball cell

Date: 2026-08-26. Status: **strict exact source candidate, pending an
independent literal-free no-import referee**. No ledger, release, PDF, ZIP,
or previously frozen artifact is modified.

## 1. Statement and scope

Fix

```text
313/500 <= x <= 627/1000,
-1/100 <= y <= 1/100,
Z=z^2=1/8,
0<h<=1, lambda>0.
```

For both signed `z` lifts, the source candidate proves strict positivity of
the original fully conjugated Hermitian scalar gate throughout this complete
continuum. The cell is adjacent to the independently audited box
`78/125<=x<=313/500` at the full face `x=313/500`. It is not a full compact-
ball, unrestricted common-metric, arbitrary-node, arbitrary-dimensional, or
fixed-lens-optimum theorem.

## 2. Exact legality and reconstruction

With `S=h^2`, exact endpoint monotonicity gives

```text
D=1-x^2-y^2-Z
 >=1-(627/1000)^2-(1/100)^2-1/8
 =481771/1000000>0.
```

For

```text
j=(1+5x)/(3 sqrt(5)),
k=(-3+5y)/(3 sqrt(5)),
ell^2=5/72,
```

the source reconstructs the signed compact frame, the two signed Gram-column
factorizations, the Hermitian compression, `Q=lambda H`, all nine entries of
`Q^2`, and the fully conjugated raw gate. It proves

```text
det(C)=(5/72)S>0,
Re(Qp)_1=-(5 sqrt(6)/36)lambda*S*D<0.
```

Thus the full cell is strictly legal, strictly dangerous, rank two, and valid
for both signs of `z`.

## 3. Five exact lambda groups

Write

```text
36 Gamma=sum_(k=0)^4 C_k(S,x,y)lambda^k.
```

The source proves `C_0=5` and exact divisibility of every `C_k`, `k>=1`, by
`S`. Map the new cell to the unit cube by

```text
y=-1/100+u/50,
x=313/500+v/1000,
0<=S,u,v<=1.
```

Exact trivariate power-to-Bernstein conversion gives:

| group | source terms | degree `(S,u,v)` | controls | all global minima |
|---|---:|---:|---:|---|
| `C_0` | 1 | `(0,0,0)` | 1 | `(0,0,0): 5` |
| `C_1/S` | 5 | `(0,2,2)` | 9 | `(0,2,2): 204229/300000` |
| `C_2/S` | 26 | `(1,4,4)` | 50 | `(0,4,0): 153893289799/12656250000` |
| `C_3/S` | 42 | `(2,6,6)` | 147 | `(0,6,0): 130268743001281/237304687500000` |
| `C_4/S` | 120 | `(3,8,8)` | 324 | `(0,8,0): 99445552715982526441/26696777343750000000` |

Each displayed minimum is unique. All `531/531` controls are strictly
positive. Since Bernstein basis functions are nonnegative and sum to one,
and physical `S,lambda` are strictly positive, this is a continuum proof.

## 4. Exact seam

The new parameterization at `v=0` equals the predecessor parameterization at
its old `v=1`. The source checks the resulting original raw-gate identity
before coefficient extraction. For every one of the five lambda groups, it
independently recomputes the predecessor tensor on

```text
x=78/125+v/500
```

and proves that every new `v=0` boundary control equals the corresponding old
`v=1` boundary control. This is a parameter/raw-gate/control seam, not merely
a sampled endpoint comparison.

## 5. Counterexample track and exact classification

After the continuum proof, 81 rational nodes use three exact values of each
of `S,x,y,lambda`. All are positive, with diagnostic minimum

```text
5250817175623018829949177505801319
/1049760000000000000000000000000000 > 0.
```

These nodes are falsification diagnostics only. Exact classification on the
stated cell is:

```text
chart illegality:              absent,
Bernstein certificate failure: absent,
implementation/resource failure: absent in the frozen run,
legal raw-gate negative:        absent.
```

No numerical evidence is promoted to a theorem, and no CE-046/048/059/060
route is reused.

## 6. Replay and next gate

Run from the workspace root:

```text
.venv/bin/python -B -u \
  tmp/research/compact_ball_uncovered_box_x5_8_xy_adjacent_x627_1000_exact_gate.py
```

The frozen source attacks reject optimized Python, a false predecessor hash,
altered normalization, deletion of `Q^2`, reversal of the danger sign,
coefficient corruption, deletion of a Bernstein control, and a broken seam.
The separate source-freeze verifier rejects an altered source hash and a
damaged manifest. External-cache `py_compile` passes.

Promotion requires a second-slot independent referee that treats the source
and manifest as opaque hashes, imports no coefficient/control data, rebuilds
the signed Gram columns and all nine `Q^2` entries in a different order, and
recovers all 531 controls and the complete seam independently.
