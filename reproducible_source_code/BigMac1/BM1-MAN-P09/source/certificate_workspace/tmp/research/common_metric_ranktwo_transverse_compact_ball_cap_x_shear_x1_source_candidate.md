# Seam-preserving transverse cap chart through `X=1`

## Status and scope

This is a frozen **source candidate** pending an independent no-import
referee.  It contains two distinct exact statements:

1. a `Z`-only chart-family obstruction at `X=1` for the old transverse
   coordinates; and
2. a strict local positivity certificate for a new two-coordinate cap chart
   on `497/500 <= X <= 1`.

Neither statement is a raw-gate counterexample.  The positive result is one
local compact-ball family, not the full compact ball, the general complex
common-metric theorem, an arbitrary-node/dimension theorem, or the fixed-lens
optimal constant.

## Exact statement A: `Z`-only no-go

For the old transverse parameters

```text
x_old = -1/5 + X,
y_old = 3/5 + S*y0,
y0 = 12/[25(1+M)] + nu,
0 < S <= 1/10000,
|M| <= 1/1000,
|nu| <= 1/100,
```

one has `y0 >= 46999/100100 > 0`.  At `X=1`,

```text
x_old^2 + y_old^2 - 1
  = S*y0*(6/5 + S*y0) > 0.
```

Hence `1-x_old^2-y_old^2-Z<0` for every `Z>=0`.  No chart that changes only
`Z` while retaining these `x,y` coordinates can be compact-ball legal at
`X=1`.  This is a chart-family obstruction, not a gate counterexample and not
an obstruction to charts that also change `x` or `y`.

## Exact statement B: cap-chart source candidate

Let

```text
Xanchor = 83059/100000,
Xstar   = 1019767/1040000,
Zconstant = Zold + 2*(Xstar-Xanchor),

xcap = xold - (3/2)*(X-497/500),
ycap = yold,
Zcap = Zconstant + 2*(X-497/500),
497/500 <= X <= 1.
```

The full parameter box is

```text
0 < S <= 1/10000,
|M| <= 1/1000,
|omega|, |nu| <= 1/100.
```

The executable binds the independently audited constant-`Z` predecessor and
reconstructs the original signed frame, Hermitian `Q`, all entries of `Q^2`,
and the fully conjugated raw gate.  The raw gate has degree four in `Z`.

At `X=497/500`, it checks the complete `(x,y,Z,lambda)` seam, equality of the
positively cleared raw gates, and equality after removing the common
nonnegative first layer.  The new cleared/core structure is

```text
48/48/2263, bidegree (7,8).
```

## Full-cell and endpoint legality

Before constructing the continuous certificate, the source proves

```text
Z >= 17798406223702873/15857127000000000000 > 0,
Z(X=1,worst corner)
  = 17995576623934873/15857127000000000000 > 0,
Z <= 10967/2600000 < 1,
T <= -1218219/40625 < 0,
danger >= 13993/2600000 > 0,
d(danger)/dX >= 391/500 > 0,
det(C) >= [17798406223702873/28542828600000000000] S > 0.
```

Thus the closed endpoint `X=1`, every physical `S>0`, both signed square
roots of `Z`, and strict rank two are all covered.

## Exact continuous positivity certificate

The transverse shear removes a cancellation present in the old chart.  The
exact bidegree becomes `(7,8)`, so the complete Bernstein tensor has 72
controls rather than the predecessor's 40.  The source does not relabel these
72 controls as 40.

All 72 centered rational controls are strictly positive.  The unique weakest
index is `(7,8)`, with reserve

```text
79085602723906157917988882974367991904890648543683584180560419945180485170965315227
-------------------------------------------------------------------------------------.
239735779200073728000000000000000000000000000000000000000000000000000000
```

The complete weakest polynomial appears in the frozen normal log.  A
separate 72/72 set of exact original-gate nodes is legal and positive, but is
diagnostic only; the 72-control tensor is the continuum proof candidate.

## Replay and referee gate

```bash
.venv/bin/python -B -u tmp/research/compact_ball_cap_x_shear_x1_exact_gate.py
```

The independent referee must not import or execute the source.  It must
rebuild both exact statements, the predecessor bindings, original `Q,Q^2`
gate, full three-layer seam, endpoint legality, all 72 controls, unique
weakest polynomial/reserve, 72 diagnostic nodes, fail-closed attacks, and the
frozen manifest before promotion to a local theorem.
