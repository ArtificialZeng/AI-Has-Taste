# Independent referee audit: inward-Z affine-omega sheet

Date: 2026-08-25. Verdict: **PASS as an independently audited exact partial
theorem**. The audit does not establish the full compact-ball quartic, the
general common-metric gate, an arbitrary-node theorem, or a fixed crossing-
lens constant.

## Audited statement

The quantified sheet is

```text
0<S<=1/10000,                 3/13<=X<=1/4,
|M|<=1/1000,                 |omega|,|nu|<=1/100,
A=1+M,                       lambda=A/S,
y0=12/(25A)+nu,
omega_phys=omega-(10636/275)(X-1/5),
b=(45M+18)/(25A)-(3/5)X+omega_phys,
x=-1/5+X,                    y=3/5+S*y0,
Z=9/13-X^2+S*b-S^2*y0^2.
```

For every such parameter and both real lifts `z=+-sqrt(Z)`, the original
fully conjugated Hermitian scalar gate is strictly positive. The data also
satisfy `lambda>0`, `0<Z<1`, strict danger, and rank-two positivity. At
`X=3/13` the complete `(lambda,x,y,b,Z)` tuple agrees parameter by parameter
with the frozen v12 affine-omega sheet.

## Independence and definition-level reconstruction

The standalone referee imports no discovery/source/predecessor module and
loads no cached coefficient or Bernstein table. It reads the discovery file
only as uninterpreted bytes for SHA-256 binding. Starting from the compact-
ball definitions, it:

1. orders the signed-z frame columns as `(f_h,r)`, with the corresponding
   conjugated compression order, rather than using the source order;
2. verifies frame orthonormality, the one-dimensional kernel, Hermiticity,
   and `det(C)=(5/9)SZ` modulo the exact defining relations;
3. constructs `H=UCU*`, `Q=lambda H`, every entry of `Q^2`, and the literal
   fully conjugated scalar gate;
4. reconstructs the same gate using the cyclic Gram component order
   `(third,first,second)` and proves exact symbolic identity before applying
   the sheet map;
5. substitutes the inward-Z sheet directly, clears only the displayed
   positive denominator, and independently computes every coefficient;
6. performs a dense **u-first, tau-second** power-to-Bernstein conversion,
   not an imported or serialized source transform.

The signed variable cancels before the map, so the gate depends on `z` only
through `z^2=Z`; this verifies both signs rather than sampling one lift.

## Exact algebra and seam

The independently cleared numerator is

```text
Qhat=(25A)^8 S^3 (36 Gamma).
```

It has 32 `(S,X)` coefficients and bidegree `(7,4)`. Subtracting only

```text
S^3 25^8 M^2 A^8 (5M^2+14M+14)
```

leaves 32 nonzero `(S,X)` coefficients containing 1,581 centered
`(M,omega,nu)` monomials. The removed layer is nonnegative because

```text
5M^2+14M+14 = 5(M+7/5)^2+21/5 > 0.
```

The predecessor is reconstructed from its formula as
`Z_v12=3X-X^2+Sb-S^2y0^2`. The identity

```text
Z-Z_v12 = -3(X-3/13)
```

and direct tuple comparison prove the full parameter-by-parameter seam at
`X=3/13`. No continuity inference or decimal comparison is used.

## Exact continuum certificate

The lossless rectangle enlargement is

```text
X=3/13+u/52,
S=(13/30000) tau X,
0<=u,tau<=1.
```

It covers the physical range because
`(1/10000)/(3/13)=13/30000`. The referee obtains bidegree `(7,9)` and 80
tensor Bernstein controls. Independent centered rational lower bounds give

```text
zero controls: (0,0), (0,1), (1,0),
strict controls: 77,
minimum strict control: (2,0),
R* =
10071067674014002577317165966399410637259618083
/128416777961472000000000000000000000000000000 > 0.
```

The three zeros are confined to the artificial `tau=0` closure. The referee
independently expands and checks

```text
W(tau)=sum_(i=2)^7 binom(7,i) tau^i(1-tau)^(7-i)
      =1-(1-tau)^7-7tau(1-tau)^6.
```

For `0<tau<1`, its `i=2` term is strictly positive, while `W(1)=1`.
Therefore the core is at least `R* W(tau)>0` on the physical domain. Adding
the nonnegative first layer and dividing by the positive clearing factor
proves strict positivity of the original gate.

## Exact legality and falsification gate

Independent monotonic endpoint arithmetic reproduces

```text
46999/100100 <= y0 <= 16333/33300,
-69948/50875 <= b <= -299011/500500 < 0,
9984760329129934873/15857127000000000000 <= Z < 108/169 < 1.
```

Writing `T=(6/5)y0+b`, the referee proves `Tmax(3/13)=-1/100`, that `T`
decreases with `X`, and the exact danger identity

```text
D=1-x^2-y^2-Z=(2/5)(X-3/13)-S T.
```

At the worst centered parameters, the surplus over the claimed lower bound
is exactly

```text
D - [(2/5)(X-3/13)+S/100]
= 10801 S (13X-3)/3575 >= 0.
```

Thus `D>0`. Also `A>=999/1000`, hence `lambda>0`, and
`det(C)=(5/9)SZ>0`, proving strict rank-two legality.

As a separate falsification test, the referee checks all 72 exact rational
nodes from three scales, three X values, and eight centered corners. Every
node is legal and gate-positive. The minimum is

```text
36 Gamma =
182249907370437372958214245586018359494715888079
/16726464040000000000000000000000000000000000
```

at `(S,X,M,omega,nu)=(1/10000,3/13,-1/1000,1/100,-1/100)`.
The 72 nodes are diagnostics; the Bernstein argument above is the continuum
proof.

## Fail-closed and environment audit

The successful replay used project-local Python 3.11.15 and SymPy 1.14.0;
`uv pip check --python .venv/bin/python` found all 19 installed packages
compatible. External-cache `py_compile` passed. The final verifier rejects
with nonzero status:

- optimized Python (`python -O`);
- an intentionally corrupted frozen source/dependency hash;
- an intentionally deleted exact core coefficient.

The deleted-term attack stops at the 32-coefficient completeness gate before
the Bernstein conclusion.

One pre-freeze implementation run is retained in the test record. It passed
the decisive algebra and all controls, then rejected an un-cancelled SymPy
rational derivative because the prototype compared expression structure to
`1` and `6/5`. Exact `cancel/factor` reduction proved those derivatives equal
the required values. The final code uses the reduced comparison and the
stronger explicit danger factor above, then passed a complete from-scratch
replay. This was an implementation defect, not a negative gate, failed
certificate, mathematical counterexample, or scope change.

## Frozen inputs and executable

```text
6ee91b88c1835f44183a8da833239c817cdd6d079d73cd5b9e9c42428661f6ca
  tmp/research/compact_ball_inward_z_tilt_discovery.py
7b78d77ef418de755f41d8fcbd7b8aaa15eae1b1052276fe1a90274c1989e563
  tmp/research/common_metric_ranktwo_transverse_compact_ball_inward_z_tilt_source_candidate.md
dddb1e18ed0e0972d75d7099ccc75409f7ac609db9bead51a61046ff3f05d614
  tmp/research/compact_ball_inward_z_tilt_source_freeze_manifest.sha256
4ad2db93ed2a14fc6d0d54b723fb55943f15e0ad85e0a130f1c568c473e5aaa3
  tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md
bd127112e0cd59e9f0ed8c565480a612c2c75ba83edd979c3552896b18395067
  tmp/research/common_metric_ranktwo_transverse_compact_ball_affine_omega_tilt_extension.md
e6cb94c9ecd322190e959ede9ce19131e57a6964dfb29ccd88f76c076abff3c0
  tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_inward_z_tilt_independent_referee.py
```

No sampled SDP, numerical theorem inference, real-part monotonicity, dropped
phase, or CE-046/048/059/060 route is used. No proof assistant was used. The
scientifically honest status is **partial theorem**, not a solution of the
full compact-ball, common-metric, arbitrary-node, or fixed-lens problem.
