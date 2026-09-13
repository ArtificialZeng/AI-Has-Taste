# Exact source candidate for the `y`-strip around the uncovered ray

Date: 2026-08-26. Status: **strict exact source candidate, pending a
literal-free no-import referee**. No ledger, release, PDF, or ZIP is modified.

## 1. Statement and scope

Fix

```text
x=5/8, Z=z^2=1/8, -1/100<=y<=1/100,
0<h<=1, lambda>0.
```

For both signed `z` lifts, the source proves that the corresponding compact-
ball compression is strict rank two and that the original fully conjugated
Hermitian scalar gate satisfies `Gamma>0` throughout this whole continuum.
This is a one-coordinate thickening of the independently audited fixed ray;
it is not the full compact ball or an arbitrary neighborhood.

## 2. Exact legality

With `S=h^2`, the shape danger is

```text
D=1-x^2-y^2-Z=31/64-y^2>=19371/40000>0.
```

The Cholesky coordinates are

```text
j=11/(8 sqrt(5)),
k=(-3+5y)/(3 sqrt(5)),
ell^2=5/72,
W=j^2+k^2+ell^2.
```

Consequently

```text
det(C)=(5/72)S>0,
Re(Qp)_1=-(5 sqrt(6)/36) lambda S D<0.
```

The source constructs both `ell=+sqrt(5/72)` and
`ell=-sqrt(5/72)` Gram lifts and proves that they give the same compression.
Thus every point in the strip is legal, strictly dangerous, and rank two.

## 3. Definition-level raw-gate reconstruction

Starting from the original complex transverse frame, the source proves the
frame/kernel identities modulo `q^2=1-h^2`, forms the Hermitian matrix `Q`,
computes `Q^2`, and evaluates the literal fully conjugated gate.  A separate
cyclic Gram-vector expression is constructed and shown exactly identical
before the strip is certified.

Write

```text
36 Gamma=sum_(k=0)^4 C_k(S,y) lambda^k.
```

The source verifies `C_0=5` and an exact factor `S` in each `C_k`, `k>=1`.
Map the strip by

```text
y=-1/100+u/50,  0<=S,u<=1.
```

For `C_0` and the four residuals `C_k/S`, exact power-to-Bernstein conversion
gives:

| coefficient | degree `(S,u)` | controls | exact minimum |
|---|---:|---:|---:|
| `C_0` | `(0,0)` | 1 | `5` at `(0,0)` |
| `C_1/S` | `(0,2)` | 3 | `2743/4000` at `(0,2)` |
| `C_2/S` | `(1,4)` | 10 | `6994764611/576000000` at `(0,4)` |
| `C_3/S` | `(2,6)` | 21 | `140490493103/256000000000` at `(0,6)` |
| `C_4/S` | `(3,8)` | 36 | `205239422872780721/55296000000000000` at `(0,8)` |

All 71 controls are strictly positive.  The complete exact coefficient
polynomials are printed by the frozen normal log and are derived afresh by
the source; no cached coefficient table is imported.  Since Bernstein basis
functions are nonnegative and sum to one, all five `C_k` are strictly
positive on the physical domain.  With `lambda>0`, this proves the original
gate strictly positive.

## 4. Symmetric proof/counterexample classification

Twenty-seven exact rational diagnostics use

```text
S in {1/100,1/2,1},
y in {-1/100,0,1/100},
lambda in {1/10,1,10}.
```

They find no legal negative; their exact minimum is

```text
165951810221058284625705719
/33177600000000000000000000 > 0.
```

These nodes are diagnostics only.  The continuum proof is the 71-control
certificate above.  The exact classification is:

```text
chart illegality:              absent,
Bernstein certificate failure: absent,
implementation/resource failure: absent in the frozen run,
legal raw-gate negative:        absent on this strip.
```

No CE-046/048/059/060 route, numerical theorem inference, sampled SDP, or
proof assistant is used.

## 5. Replay and referee gate

Run

```text
.venv/bin/python -B -u tmp/research/compact_ball_uncovered_ray_x5_8_ystrip_exact_gate.py
```

Six attacks reject optimized execution, a bad predecessor manifest, a bad
shape normalization, deleted `Q^2`, a flipped danger sign, and a corrupted
derived coefficient. External-cache `py_compile` passes.

Promotion requires a separately written no-import referee that treats all
source artifacts as opaque hashes, uses a different signed Gram-column and
`Q^2` multiplication order, independently reconstructs the five bivariate
coefficient polynomials, and derives the 71 controls without importing the
source transform.
