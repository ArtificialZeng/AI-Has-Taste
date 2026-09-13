# Materially larger adjacent compact-ball source candidate: `16/25 <= x <= 7/10`

## Status and exact scope

This is a frozen **source candidate**, not yet an independently refereed
theorem.  It covers the single rational cell

```text
Z = 1/8,
16/25 <= x <= 7/10,
|y| <= 1/100,
0 < h <= 1,
lambda > 0,
both signed-z lifts.
```

The candidate binds the preceding `x <= 16/25` source, note, verifier, and
manifest by SHA256 for its left seam only.  On the new cell it independently
reconstructs the Hermitian frame and compression, `Q=lambda H`, `Q^2`, and
the fully conjugated cyclic raw gate.

## Exact legality and seam

The rational box map is

```text
x = 16/25 + 3v/50,        0 <= v <= 1,
y = -1/100 + u/50,        0 <= u <= 1,
S = h^2,                  0 < S <= 1.
```

The exact width is `3/50`, and throughout the full cell

```text
D = 1-x^2-y^2-Z >= 3849/10000 > 0,
det(C)/S = 5/72 > 0.
```

The code verifies rank two, the kernel identity, both signed-z Gram lifts,
and the strict-danger identity.  At `x=16/25` it checks parameter,
Hermitian-matrix, raw-gate, and all five coefficient-control seams against
the predecessor's right face.

## Exact continuum certificate

The complete trivariate Bernstein arrays are derived from the original gate
before comparison with the frozen fail-closed targets:

| group | terms | degrees `(S,u,v)` | controls | unique global minimum |
|---|---:|---:|---:|---|
| `C0` | 1 | `(0,0,0)` | 1 | `(0,0,0): 5` |
| `C1/S` | 5 | `(0,2,2)` | 9 | `(0,2,2): 517/1000` |
| `C2/S` | 26 | `(1,4,4)` | 50 | `(0,4,0): 445787099/36000000` |
| `C3/S` | 42 | `(2,6,6)` | 147 | `(0,6,0): 6613713203/12000000000` |
| `C4/S` | 120 | `(3,8,8)` | 324 | `(0,8,0): 845947392310481/216000000000000` |

All `531/531` controls are strictly positive.  The `81/81` exact rational
nodes are diagnostics only; their exact minimum is

```text
648244090066129541362799 / 129600000000000000000000.
```

The direct large-cell certificate succeeds, so no subdivision was used.  No
chart illegality, Bernstein insufficiency, implementation/resource failure,
or legal raw-gate negative occurs.  No route from CE-046, CE-048, CE-059, or
CE-060 is reused.

## Replay and next gate

From the workspace root:

```sh
.venv/bin/python -B tmp/research/compact_ball_uncovered_box_x5_8_xy_adjacent_x7_10_exact_gate.py
.venv/bin/python -B tmp/research/verify_compact_ball_uncovered_box_x5_8_xy_adjacent_x7_10_source_freeze.py
shasum -a 256 -c tmp/research/compact_ball_uncovered_box_x5_8_xy_adjacent_x7_10_source_freeze_manifest.sha256
```

The next gate is an independent literal-free/no-import referee.  The result
must remain a source candidate until that referee passes.
