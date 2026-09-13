# Inward-Z extension to a rational chart-legality frontier: exact source candidate

Date: 2026-08-25. Status: **exact source-level partial-theorem candidate,
pending a genuinely independent definition-level referee**.

This candidate extends the independently audited inward-Z sheet only across
the new rational cell

```text
0<S<=1/10000,                131/520<=X<=83059/100000,
|M|<=1/1000,                |omega|,|nu|<=1/100,
A=1+M,                      lambda=A/S,
y0=12/(25A)+nu,
b=(45M+18)/(25A)-(3/5)X+omega-(10636/275)(X-1/5),
x=-1/5+X,                   y=3/5+S y0,
Z=9/13-X^2+S b-S^2 y0^2.
```

For both signed lifts `z=+-sqrt(Z)`, the source executes the frozen predecessor
from its audited hash to rebuild the signed compact-ball Gram columns, the
Hermitian `Q`, every entry of `Q^2`, and the fully conjugated original scalar
gate. It imports no predecessor coefficient or Bernstein table. Clearing only
the positive factor `25^8 A^8 S^3` gives 32 `(S,X)` coefficients of bidegree
`(7,4)`. After removing the manifestly nonnegative layer

```text
S^3 25^8 M^2 A^8 (5M^2+14M+14),
```

the core again has 32 `(S,X)` coefficients and 1,581 centered
`(M,omega,nu)` monomials.

On the lossless new-cell map

```text
X=131/520+(83059/100000-131/520)u,    S=tau/10000,
0<=u,tau<=1,
```

the source regenerates a bidegree-`(7,4)` Bernstein tensor. All 40 centered
rational lower controls are strictly positive; there are no closure-zero
controls. The unique weakest control is `(0,0)`, with exact lower reserve

```text
119539987320009056100108078372012547879
/718761099264000000000000000000.
```

Its complete parameter polynomial is

```text
461578369140625 (M+1)^12 / 2741856.
```

The source checks directly that the predecessor endpoint at `X=131/520`
equals the new-cell polynomial at `u=0` before the Bernstein conclusion.

Exact monotonicity bounds on the complete cell give

```text
b_min = -24601484583/1017500000,
Z_min = 160243869095653/15857127000000000000,
Z_upper = 170039/270400,
danger >= 11/1300+(10931/13000)S,
det(C) >= 160243869095653 S/28542828600000000000.
```

Hence the source candidate is legal, strictly dangerous, rank two, and
raw-gate positive throughout the displayed continuum for both signs of `z`.
It also evaluates 72 exact endpoint/midpoint falsification nodes directly in
the original rational raw gate; all are legal and positive.

The same 40 controls remain strict through the nearby rational point

```text
X=4153/5000.
```

However the exact worst-corner chart coordinate changes sign across

```text
Z_min(83059/100000)
  = 160243869095653/15857127000000000000 > 0,
Z_min(4153/5000)
  = -103795949201927/15857127000000000000 < 0.
```

Thus the first event isolated in this rational bracket is loss of this
coordinate chart's legality, not a negative value of the polynomial gate.
This is not a maximality theorem for the original Hermitian gate, and no
claim is made about illegal points outside the chart.

Run only with the project environment:

```text
.venv/bin/python tmp/research/compact_ball_inward_z_legality_frontier_extension.py
```

The source fails closed under optimized Python, a corrupted predecessor hash,
or deletion of one exact core coefficient. During development, two mechanical
assertion errors were exposed and corrected before freezing: a three-radius
tuple was unpacked into two names, and a loose predecessor danger bound was
mistaken for the exact endpoint value. A symbolic relational was also replaced
by an exact derivative identity. None of these failures supplied mathematical
evidence; the final normal replay is from the source hash recorded in the
freeze manifest.

No sampled SDP, floating sign decision, real-part monotonicity, fixed
allocation, or route CE-046/048/059/060 is used. No proof assistant is used.

The claim remains a source candidate until a separate implementation rebuilds
the original gate, 40 controls, exact reserve and polynomial, splice,
full-cell legality, both signed lifts, rational root bracket, and negative
controls without importing this script's coefficient tables. Even after such
an audit, this is a partial theorem only. It does not prove the full compact
ball, the general common-metric gate, an arbitrary-node bridge, or the fixed
crossing-lens optimal constant. It is not yet a paper or submission package.
