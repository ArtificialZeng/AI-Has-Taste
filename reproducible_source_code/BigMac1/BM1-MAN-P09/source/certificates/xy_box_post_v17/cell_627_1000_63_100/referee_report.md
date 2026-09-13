# Independent referee audit: next adjacent `+x` compact-ball xy-cell

## Verdict

**PASS.** Fatal: **0**. Major: **0**. Minor: **0**.

The independently reconstructed exact certificate proves only

\[
 \frac{627}{1000}\le x\le\frac{63}{100},\qquad
 |y|\le\frac1{100},\qquad Z=\frac18,
 \qquad 0<S\le1,\qquad \lambda>0,
\]

for both signed lifts of `z`. It does not establish the whole compact ball,
arbitrary `Z`, arbitrary transverse compressions, a common-metric theorem,
an arbitrary-node theorem, or the fixed crossing-lens constant.

## Opaque bindings and independence

The candidate source and source manifest were handled only as opaque byte
strings for SHA-256 verification. They were never opened, parsed, imported,
executed, or used to obtain coefficients, controls, minima, or seam data.
Their hashes are

- source: `823fbb26a31378530567674cce08ec7f7203c9882256dabed2a776e2ae6b7825`;
- source manifest: `ac8c581ef64e6de4b03e657f3c9201d2864a86d3ee0af91021607a3613c13f2e`.

The preceding `[313/500,627/1000]` source/referee/report/manifests and the
full-cone reduction note/audit were independently hash-bound. The audit
recomputed the predecessor boundary from the original definitions; it did
not copy either source's coefficient or control tensor.

## Definition-level reconstruction and legality

The scout rebuilt the complex signed frame, `C`, `H`, `Q`, and `Q^2`. It put
the signed-`z` Gram column before the mixed column, checked the Gram form
entry-by-entry against direct compression, and multiplied `Q^2` in component
order `(1,0,2)`, verifying all 9/9 entries.

It reversed the component order in the fully conjugated literal gate, proved
the raw/cyclic identity with the vector gate, and eliminated radicals in the
order `h,z,q`. The polynomial is real and both signed lifts agree exactly.
On the full cell,

\[
 1-x^2-y^2-Z=\frac78-x^2-y^2
 \ge \frac{239}{500}>0,
 \qquad \frac{\det C}{S}=\frac5{72}>0.
\]

Together with `Z=1/8`, `1-Z>0`, and `S>0`, these exact identities prove
strict danger, both-sign legality, and rank two. Each positive `S` clearing
is preceded by an exact polynomial-divisibility check.

## Exact 531-control certificate

Writing

\[
 36\Gamma=\sum_{k=0}^{4}C_k(S,x,y)\lambda^k,
\]

the referee independently derived all five coefficients and used

\[
 x=\frac{627}{1000}+\frac{3v}{1000},\qquad
 y=-\frac1{100}+\frac{u}{50},\qquad 0\le u,v\le1.
\]

Its dense exact three-variable power-to-Bernstein transform produced groups
of sizes `1/9/50/147/324`; all **531/531** controls are present and strictly
positive. The unique global minimum is the `lambda^3` control `(0,0,6)` in
the referee's `(S,v_x,u_y)` order:

\[
 \frac{533736176784030589}{972000000000000000}>0.
\]

The coefficient and complete control tables have SHA-256 values

- `b11348d029f2b1fd6bcbf4dfe3ff789f1f5e67a0846f2a83041e7af62bd9497f`;
- `b339535bbefde30457c7c9af08bed3c407ebce15c00a0d4810aaf57cc6125e04`.

The exact controls, not the 81 diagnostic nodes, prove positivity throughout
the stated cell for every positive scale.

## Index-order reconciliation

The referee records controls as `(S,v_x,u_y)`, whereas the candidate report
uses `(S,u_y,v_x)`. The formal verifier applies the permutation

\[
 (i,j,k)\longmapsto(i,k,j)
\]

to every one of the 531 controls and proves that applying it twice recovers
the entire original table. Thus the referee minima `(0,0,4)`, `(0,0,6)`, and
`(0,0,8)` are exactly the candidate-convention indices `(0,4,0)`, `(0,6,0)`,
and `(0,8,0)`, with the same exact values. This is solely a variable-order
convention and not a coefficient, minimum, or seam discrepancy.

## Exact predecessor seam

The current map and the independently reconstructed predecessor map meet at
`x=627/1000`. The referee verified exact equality of the endpoint parameter,
entrywise equality of the Hermitian parameter matrix, identity of the fully
conjugated raw gate, and equality of all five Bernstein boundary faces:
`1+3+10+21+36=71/71` controls. The seam signature SHA-256 is
`0bf006896aa9a52e0fecd449698df34c577134d3fba2e8398b4e2fce64a0b6a0`.

## Fail-closed and replay audit

The syntax gate, literal-free scout, formal normal, root replay, and fresh
isolated-copy replay exited zero. Thirteen actual mutations exited one at
their intended gates: optimized Python, bad source, bad source manifest, bad
predecessor, altered endpoint normalization, invalid `S` clearing, deleted
`Q^2` term, broken conjugation, omitted signed-`z` lift, flipped danger sign,
corrupted coefficient, deleted control, and broken seam.

An initial omit-sign mutation hit an immutable-matrix assignment in the audit
harness. The frozen harness and every frozen normal/attack/replay log were
regenerated; the mutation now fails at the intended both-sign identity. This
is an auditor implementation event, not a candidate finding.

The audit rejects numerical evidence as proof, preserves the cyclic phase and
all `Q^2` terms, does not turn chart illegality into raw negativity or
maximality, and does not reuse CE-046/048/059/060.

## Classification

- Fatal findings: **0**.
- Major findings: **0**.
- Minor findings: **0**.

The next local adjacent `+x` cell theorem is independently certified within
the exact scope above.
