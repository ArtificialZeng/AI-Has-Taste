# Independent referee audit: inward-Z danger-root cell

## Verdict

**PASS.** Fatal findings: **0**. Major findings: **0**. Minor findings:
**0**.

The audited theorem is only the local recentered-chart cell
`39/40 <= X <= 1019767/1040000`, with `0 < S <= 1/10000` and the frozen
`M, omega, nu` box.  It is not a full compact-ball theorem and not the
unrestricted common-metric or crossing-lens theorem.

## Independence and trust boundary

The frozen candidate source, its source note, and its source-produced logs
were treated solely as opaque byte strings for SHA-256 checks.  The referee
does not import, execute, parse, or read candidate specialization data,
coefficient tables, controls, weakest polynomials, or helper functions.

The referee restarts from the original Hermitian `Q` and `Q^2` definitions.
It uses reversed signed-z Gram columns, the elimination order `q,z,h`, an
independent cyclic-vector expansion of the fully conjugated raw gate, and a
dense `u`-first Bernstein transform.  The predecessor cell, compact-ball
reduction, and frozen endpoint preflight are SHA-bound dependencies.

## Exact findings

The literal-free scout and the formal frozen-literal run independently give

```
X* = 1019767/1040000,
T_max = -4181417/143000 < 0,
weakest control = (7,0),
reserve =
74930996060450233534496330989817712955209239262450259704704694012020764601549216227
/239735779200073728000000000000000000000000000000000000000000000000000000.
```

The affine danger base decreases to zero exactly at `X*`.  At the root the
exact identity is `D=-S*T`, so the uniform strict bound `T<=T_max<0` proves
`D>0` for every `S>0`; this is not inferred from sampled nodes.

The independent script also verifies:

- reversed Gram compression and all nine `Q^2` entries;
- literal raw gate, reality/radical cancellation, and `deg_Z=4`;
- positive reversible clearing, `34/34/1659`, and bidegree `(7,4)`;
- exact three-layer splice at `X=39/40`;
- all 40 Bernstein controls strictly positive, with unique weakest control
  and the complete printed weakest polynomial;
- full-cell `Z`, `det(C)`, both signed-z, positive-scale, and rank-two
  legality.

The 72 exact nodes are explicitly classified as diagnostics only.

## Adversarial results

Formal normal exits zero.  Seven serial attacks exit nonzero and stop at the
intended exact gates: optimized Python, bad source hash, bad predecessor hash,
bad sparse normalization, dropped `Q^2`, flipped danger sign, and a dropped
core coefficient.  The last is rejected at `34 core coefficients`.

The audit additionally rejects four scope errors: numerical evidence as a
theorem, chart obstruction as a raw negative or maximality claim, reuse of
CE-046/048/059/060, and extension to the full ball/common metric.

## Reproduction

```sh
python tmp/research/audit/danger_root_referee_literal_free_scout.py
python tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_inward_z_recentered_lift_danger_root_independent_referee.py
```

The atomic normal, attack, compile, and explicit-exit records are under
`tmp/research/audit/`.  No proof assistant was used; the certificate is exact
rational/symbolic arithmetic checked by the independent Python referee.
