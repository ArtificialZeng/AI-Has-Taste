# Independent referee audit: adjacent `+x` compact-ball xy-cell

## Verdict

**PASS.** Fatal: **0**. Major: **0**. Minor: **0**.

The independently reconstructed exact certificate proves only

\[
 \frac{313}{500}\le x\le\frac{627}{1000},\qquad
 |y|\le\frac1{100},\qquad Z=\frac18,
 \qquad 0<S\le1,\qquad \lambda>0,
\]

for both signed lifts of `z`. It does not establish the whole compact ball,
arbitrary `Z`, arbitrary transverse compressions, a full common-metric
theorem, an arbitrary-node theorem, or the fixed crossing-lens constant.

## Opaque bindings and independence

The current candidate source and source manifest were handled only as opaque
byte strings for SHA-256 verification. They were never opened, parsed,
imported, executed, or used to obtain coefficients, controls, minima, or seam
data. Their hashes are respectively

- source: `6ce356083b31927a41808ec54078e104358db2dcdce421cd3ccfc5dfaedf6c92`;
- source manifest: `2ce9ef8ed0dface0c00328a65be9dc7c4c4a1f7c8cfb1053ac21ea96967ff15a`.

The predecessor xy-box source/referee/report/manifests and the full-cone
reduction note/audit were independently hash-bound. The audit used the
original Hermitian definitions and recomputed the predecessor boundary; it
did not read a candidate coefficient or control table.

## Definition-level reconstruction

The scout rebuilt the complex signed frame, `C`, `H`, `Q`, and `Q^2`. It put
the signed-`z` Gram column before the mixed column, checked the Gram form
entry-by-entry against direct compression, and multiplied `Q^2` in the
independent component order `(1,0,2)`, verifying all 9/9 entries.

It reversed the component order in the fully conjugated literal gate, proved
identity with the vector gate, and eliminated radicals in the order `h,z,q`.
The resulting polynomial is real and both signed lifts of `z` agree exactly.
On the complete cell,

\[
 1-x^2-y^2-Z=\frac78-x^2-y^2
 \ge \frac{481771}{1000000}>0,
 \qquad \frac{\det C}{S}=\frac5{72}>0.
\]

Together with `Z=1/8`, `1-Z>0`, and `S>0`, these exact identities prove
strict danger, both-sign legality, and rank two throughout the claimed cell.

## Exact 531-control certificate

Writing

\[
 36\Gamma=\sum_{k=0}^{4}C_k(S,x,y)\lambda^k,
\]

the referee independently derived all five coefficients and used the maps

\[
 x=\frac{313}{500}+\frac{v}{1000},\qquad
 y=-\frac1{100}+\frac{u}{50},\qquad 0\le u,v\le1.
\]

Its own dense three-variable power-to-Bernstein transform produced control
groups of sizes `1/9/50/147/324`. All **531/531** controls are present and
strictly positive. The exact group minima are recorded in the test-results
artifact. The unique global minimum is the `lambda^3` control `(0,0,6)`:

\[
 \frac{130268743001281}{237304687500000}>0.
\]

The independently derived coefficient and complete control tables have
SHA-256 values

- `b11348d029f2b1fd6bcbf4dfe3ff789f1f5e67a0846f2a83041e7af62bd9497f`;
- `f5b16ceedf15a37870ab0373f6bfba67fd47acccaa1b0c10f2258e070305f4ea`.

The exact controls, not the 81 diagnostic nodes, prove positivity at every
point and every positive scale in the stated cell.

## Exact predecessor seam

The referee independently substituted the predecessor map

\[
 x=\frac{78}{125}+\frac{v_-}{500}
\]

and the current map at their shared endpoint `x=313/500`. It verified:

1. exact equality of the endpoint parameter;
2. entrywise equality of the Hermitian parameter matrix;
3. identical fully conjugated raw gates;
4. equality of all five Bernstein boundary faces, totaling
   `1+3+10+21+36=71/71` exact controls.

The full boundary-seam signature has SHA-256
`47f305c5c5e756916f4cf61f6e5552e6a629b763baa6fd92842fd67fd8d4ec2b`.

## Fail-closed and replay audit

The syntax gate, literal-free scout, formal normal, root replay, and a fresh
isolated-copy replay all exited zero. Ten actual mutations exited one at their
intended exact gates: optimized Python, bad source bytes, bad source-manifest
bytes, bad predecessor bytes, altered endpoint normalization, deleted `Q^2`
term, flipped danger sign, corrupted coefficient, deleted control, and broken
boundary seam.

The first scout attempt exposed a non-sequential substitution bug in the
audit harness. The frozen script performs explicit endpoint substitution; the
corrected scout and both replays pass. This is an auditor implementation event,
not a mathematical finding against the candidate.

The audit rejects numerical evidence as theorem proof, does not turn chart
illegality into raw negativity or maximality, and does not reuse
CE-046/048/059/060.

## Classification

- Fatal findings: **0**.
- Major findings: **0**.
- Minor findings: **0**.

The local adjacent `+x` cell theorem is independently certified within the
exact scope above.
