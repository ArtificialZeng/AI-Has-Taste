# Adjacent compact-ball source candidate: `63/100 <= x <= 16/25`

## Status and exact scope

This is a frozen **source candidate**, not yet an independently refereed theorem.
It extends the preceding candidate across the single adjacent rational cell

```text
Z = 1/8,
63/100 <= x <= 16/25,
|y| <= 1/100,
0 < h <= 1,
lambda > 0,
both signed-z lifts.
```

The script binds the preceding `x <= 63/100` source, note, verifier, and
source manifest by SHA256.  Those predecessor objects are used only for the
left seam; all formulas and all controls on the new cell are rebuilt from the
original Hermitian frame, compression, `Q=lambda H`, `Q^2`, and the fully
conjugated cyclic raw gate.

## Exact legality and seam

Use

```text
x = 63/100 + v/100,       0 <= v <= 1,
y = -1/100 + u/50,        0 <= u <= 1,
S = h^2,                  0 < S <= 1.
```

The source proves exactly that the cell width is `1/100`,

```text
D = 1-x^2-y^2-Z >= 4653/10000 > 0,
det(C)/S = 5/72 > 0,
```

and verifies the two signed-z Gram lifts, rank two, kernel identity, and the
strict-danger scalar identity.  At `x=63/100` it checks the parameter,
Hermitian matrix, fully cleared raw gate, and every boundary control of all
five scale-coefficient groups against the predecessor's right face.

## Continuum certificate

After independently deriving the coefficient polynomials and their complete
trivariate Bernstein arrays, the source compares the following exact data:

| group | terms | degrees in `(S,u,v)` | controls | unique global minimum |
|---|---:|---:|---:|---|
| `C0` | 1 | `(0,0,0)` | 1 | `(0,0,0): 5` |
| `C1/S` | 5 | `(0,2,2)` | 9 | `(0,2,2): 649/1000` |
| `C2/S` | 26 | `(1,4,4)` | 50 | `(0,4,0): 9900499/810000` |
| `C3/S` | 42 | `(2,6,6)` | 147 | `(0,6,0): 66774911/121500000` |
| `C4/S` | 120 | `(3,8,8)` | 324 | `(0,8,0): 413215508881/109350000000` |

Thus all `531/531` controls are strictly positive.  The stored minimum values
are fail-closed comparison targets only: the code first reconstructs the
original gate, derives each full control array, computes its minimum and all
minimizers, and only then compares these independently derived objects with
the frozen targets.

The `81/81` exact rational nodes are diagnostic only.  Their exact minimum is

```text
648247688938747558319039 / 129600000000000000000000.
```

No chart illegality, Bernstein insufficiency, implementation/resource
failure, or legal raw-gate negative occurs on this cell.  In particular this
is not a use of CE-046, CE-048, CE-059, or CE-060.

## Replay and next gate

From the workspace root:

```sh
.venv/bin/python -B tmp/research/compact_ball_uncovered_box_x5_8_xy_adjacent_x16_25_exact_gate.py
.venv/bin/python -B tmp/research/verify_compact_ball_uncovered_box_x5_8_xy_adjacent_x16_25_source_freeze.py
shasum -a 256 -c tmp/research/compact_ball_uncovered_box_x5_8_xy_adjacent_x16_25_source_freeze_manifest.sha256
```

The next admissible gate is an independent literal-free/no-import referee of
the frozen bytes.  Until that gate passes this candidate must not be promoted
to a theorem or incorporated into a release PDF.
