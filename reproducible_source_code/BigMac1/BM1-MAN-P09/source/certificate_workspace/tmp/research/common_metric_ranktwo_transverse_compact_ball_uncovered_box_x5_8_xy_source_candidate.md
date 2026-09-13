# Exact source candidate for a two-coordinate compact-ball box

Date: 2026-08-26. Status: **strict exact source candidate, pending an
independent literal-free no-import referee**. No ledger, release, PDF, or ZIP
is modified.

## 1. Statement

Fix

```text
78/125 <= x <= 313/500,
-1/100 <= y <= 1/100,
Z=z^2=1/8,
0<h<=1, lambda>0.
```

Equivalently `|x-5/8|<=1/1000`. For both signed `z` lifts, the source proves
strict positivity of the original fully conjugated Hermitian scalar gate on
this complete continuum. This opens a genuine two-shape-coordinate box around
the independently audited `y`-strip, but does not prove an open
three-dimensional shape neighborhood or the full compact ball.

## 2. Exact legality

With `S=h^2`, the danger reserve is

```text
D=1-x^2-y^2-Z
 >=1-(313/500)^2-(1/100)^2-1/8
 =30189/62500>0.
```

Using

```text
j=(1+5x)/(3 sqrt(5)),
k=(-3+5y)/(3 sqrt(5)),
ell^2=5/72,
W=j^2+k^2+ell^2,
```

the transverse compression has

```text
det(C)=(5/72)S>0,
Re(Qp)_1=-(5 sqrt(6)/36)lambda*S*D<0.
```

The source explicitly reconstructs the positive and negative signed-`z` Gram
columns; they produce the same Hermitian compression. Hence every datum is
strictly dangerous, positive definite on its transverse support, and rank
two.

## 3. Original gate and exact continuum certificate

The source starts from the original complex frame, proves the frame and
kernel identities modulo `q^2=1-h^2`, constructs `C,H,Q`, computes `Q^2`, and
forms the fully conjugated raw gate. It separately constructs the cyclic
Gram-vector form and proves exact identity before specializing the box.

Write

```text
36 Gamma=sum_(k=0)^4 C_k(S,x,y)lambda^k.
```

The source proves `C_0=5` and exact divisibility of every `C_k`, `k>=1`, by
`S`. Map the box to the unit cube by

```text
y=-1/100+u/50,
x=78/125+v/500,
0<=S,u,v<=1.
```

Exact three-variable power-to-Bernstein conversion gives:

| group | source terms | degree `(S,u,v)` | controls | exact minimum |
|---|---:|---:|---:|---:|
| `C_0` | 1 | `(0,0,0)` | 1 | `5` at `(0,0,0)` |
| `C_1/S` | 5 | `(0,2,2)` | 9 | `12811/18750` at `(0,2,2)` |
| `C_2/S` | 26 | `(1,4,4)` | 50 | `2455906147459/202500000000` at `(0,4,0)` |
| `C_3/S` | 42 | `(2,6,6)` | 147 | `8332318460470459/15187500000000000` at `(0,6,0)` |
| `C_4/S` | 120 | `(3,8,8)` | 324 | `25275849790143404224321/6834375000000000000000` at `(0,8,0)` |

All `531/531` exact controls are strictly positive. Bernstein basis functions
are nonnegative and sum to one; since physical `S>0` and `lambda>0`, this is
a continuum proof of `Gamma>0`, not a sampled assertion.

## 4. Counterexample track and exact classification

After the symbolic proof, 81 exact rational diagnostics use three values each
of `S,x,y,lambda`. They are all strictly positive; the exact minimum is

```text
320484501994297997348013379511
/64072265625000000000000000000 > 0.
```

The nodes are diagnostics only. Exact classification:

```text
chart illegality:              absent,
Bernstein certificate failure: absent,
implementation/resource failure: absent in the frozen run,
legal raw-gate negative:        absent on the stated box.
```

No numerical evidence is promoted to a theorem, and no
CE-046/048/059/060 route is reused.

## 5. Replay and next audit gate

Run

```text
.venv/bin/python -B -u tmp/research/compact_ball_uncovered_box_x5_8_xy_exact_gate.py
```

Six attacks reject optimized execution, bad predecessor binding, bad shape
normalization, deleted `Q^2`, flipped danger, and a corrupted terminal
coefficient. External-cache `py_compile` passes.

Promotion requires an independent no-import referee that treats source bytes
and manifests as opaque hashes, reconstructs the signed Gram columns and all
nine `Q^2` entries in a different order, derives all five trivariate
coefficient polynomials independently, and reproduces the `531` controls by
an implementation not imported from this source.
