# Independent referee audit: uncovered `x=5/8` xy-box

## Verdict

**PASS.** Fatal: **0**. Major: **0**. Minor: **0**.

The independently reconstructed exact certificate proves only

\[
 \left|x-\frac58\right|\leq\frac1{1000},\qquad
 |y|\leq\frac1{100},\qquad Z=\frac18,
 \qquad 0<h\leq1,\qquad \lambda>0,
\]

for both signed lifts of `z`. It does not establish the whole compact ball,
arbitrary `Z`, arbitrary transverse compressions, or a common-metric theorem.

## Opaque bindings and independence

The candidate source, note, and source manifest were handled only as opaque
byte strings for hash verification. They were never opened, parsed, imported,
executed, or used to obtain coefficients, controls, or minima. Their hashes
are respectively:

- source: `5e84519227b8dcae5f52ec62159936d47db1047c9219fc92dc52191d446e9b33`;
- note: `6823af7ee461ec66cbded316b145273b06e24fdf985539415fd369563d14d87a`;
- source manifest: `9655e59e124f8a8dd2aaf661a052f70c9d489c058e638c2d8212c7c6b794422d`.

The already audited `x=5/8` y-strip referee/report/manifest and the full-cone
reduction note/audit were independently hash-bound as predecessor inputs.

## Definition-level reconstruction

The scout rebuilt the original complex signed frame, `C`, `H`, `Q`, and
`Q^2`. It assembled the mixed Gram column before the signed-`z` column and
checked the resulting matrix entry-by-entry against direct compression. It
then multiplied `Q^2` in the independent order `(2,1,0)` and verified all
9/9 entries against direct matrix multiplication.

The fully conjugated literal gate was checked identically against the vector
gate. Exact elimination in the independent order signed `z`, `q`, `h` gave a
real, radical-free polynomial. Both signed-`z` lifts agree exactly.

On the full box,

\[
 1-x^2-y^2-Z=\frac78-x^2-y^2
 \geq\frac{30189}{62500}>0,
 \qquad \frac{\det C}{S}=\frac5{72}>0.
\]

Together with `Z=1/8`, `1-Z>0`, and `S>0`, this proves strict legality and
rank two throughout the claimed box.

## Exact 531-control certificate

Writing

\[
 36\Gamma=\sum_{k=0}^{4}C_k(S,x,y)\lambda^k,
\]

the scout independently derived the five coefficients. It used the exact box
maps

\[
 x=\frac{78}{125}+\frac{v}{500},\qquad
 y=-\frac1{100}+\frac{u}{50},\qquad 0\leq u,v\leq1,
\]

factored each coefficient's `S`-adic order, and applied an independently
implemented dense three-variable power-to-Bernstein transform. The certificate
shapes `(S-adic order, (S,v,u) degrees, control count)` are

\[
 (0,(0,0,0),1),\ (1,(0,2,2),9),\ (1,(1,4,4),50),
\]
\[
 (1,(2,6,6),147),\ (1,(3,8,8),324).
\]

All **531/531** controls are present and strictly positive. The unique global
minimum is the `lambda^3` control at index `(0,0,6)`, with value

\[
 \frac{8332318460470459}{15187500000000000}>0.
\]

The independently derived coefficient tuple and complete control table are
frozen by SHA-256 values

- `b11348d029f2b1fd6bcbf4dfe3ff789f1f5e67a0846f2a83041e7af62bd9497f`;
- `89c49a8ba13aa17da382f3f62666246a9a70906fad34d16705d4f99f059b6a3d`.

The exact certificate—not the 81 diagnostic nodes—proves positivity for every
point and every positive scale in the stated box.

## Fail-closed attacks

The formal normal and syntax gates passed. Nine actual mutations each exited
nonzero at the intended exact gate: optimized Python, bad source hash, bad
source-manifest hash, bad predecessor hash, bad endpoint normalization,
deleted `Q^2` term, flipped danger sign, corrupted coefficient, and deleted
control.

The audit rejects numerical evidence as theorem proof, does not turn chart
illegality into raw negativity or maximality, and does not reuse
CE-046/048/059/060.

## Classification

- Fatal findings: **0**.
- Major findings: **0**.
- Minor findings: **0**.

The local xy-box theorem is independently certified within the exact scope
above.
