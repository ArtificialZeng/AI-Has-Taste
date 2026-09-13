# Independent referee audit: uncovered-ray `x=5/8` y-strip

## Verdict

**PASS.** Fatal: **0**. Major: **0**. Minor: **0**.

The independently reconstructed exact certificate proves the local statement
only on

\[
 x=\frac58,\qquad Z=\frac18,\qquad |y|\leq\frac1{100},
 \qquad 0<h\leq1,\qquad \lambda>0,
\]

for both signed lifts of `z`. It does not prove the whole compact ball, an
arbitrary ray, an arbitrary transverse compression, or the common-metric
theorem.

## Independence and bindings

The current candidate source, candidate note, and source-freeze manifest were
handled only as opaque bytes for SHA-256 verification. They were never opened,
parsed, imported, executed, or mined for coefficients, controls, minima, or
claims. Their verified hashes are respectively:

- source: `f609a892135bd8de66bd164b153777419646ec9d134bbf4fb5f04031642cfbf3`;
- source note: `982976dc83a0cc7f85fbdccf9e37fdb3a8701220b2dcd2fdb12e12c8a599e154`;
- source manifest: `b367f31b472726cc5b02a4263d26ff82582741f45a021b1595ac4debdf090545`.

The previously audited center-ray referee/report/manifest and the full-cone
reduction note/audit were independently hash-bound before reconstruction.

## Definition-level reconstruction

The literal-free scout used a signed-`z` Gram column before the mixed column,
then compared that Gram form entry-by-entry with direct compression. It
reconstructed the signed Hermitian frame, verified the frame identities,
Hermitian symmetry, equality of the two signed-`z` lifts, and

\[
 \det C=\frac59SZ.
\]

It multiplied `Q^2` in the independent index order `(0,2,1)` and checked all
9 entries against direct matrix multiplication. The fully conjugated literal
gate was then checked identically against the vector gate, followed by exact
elimination of `h`, `q`, and signed `z`. The resulting gate is real and
radical-free.

On the complete strip, the exact legality identities are

\[
 1-x^2-y^2-Z=\frac{31}{64}-y^2
 \geq \frac{19371}{40000}>0,
 \qquad \frac{\det C}{S}=\frac5{72}>0.
\]

Together with `Z=1/8`, `1-Z>0`, the both-sign identity, and `S>0`, these
verify strict compact-ball legality and rank two throughout the claimed cell.

## Exact positivity certificate

Writing the independently reconstructed polynomial as

\[
 36\Gamma=\sum_{k=0}^{4}C_k(S,y)\lambda^k,
\]

the scout derived all five `C_k` from the raw gate. Under
`y=-1/100+u/50`, `0<=u<=1`, it factored the exact `S`-adic order of each
coefficient and converted the residuals to dense tensor Bernstein form. The
certificate shapes `(S-adic order, S degree, u degree, control count)` are

\[
 (0,0,0,1),\ (1,0,2,3),\ (1,1,4,10),\
 (1,2,6,21),\ (1,3,8,36).
\]

Thus all **71/71** controls are present and strictly positive. The complete
derived objects are frozen by

- coefficient-tuple SHA-256:
  `b0ceebda4f845cb5d4d988c2f2b6f4384d0143859a48c5b9779f1f73ac7b3855`;
- full-control-table SHA-256:
  `2a57209ee9fe5745b0ae7bf366534808ec0862e83903036cff95229594bae226`.

The full coefficient polynomials and all controls are printed in the atomic
scout and formal-normal logs. Exact positivity follows from the Bernstein
certificate and `S>0`, `lambda>0`; the 27 exact sampled nodes are retained
only as diagnostics and are not part of the proof.

## Negative attacks

The formal referee passed normally and under syntax compilation. Eight actual
mutations each exited nonzero at the intended exact gate:

1. optimized Python;
2. bad source hash;
3. bad source-manifest hash;
4. bad predecessor hash;
5. deletion of a `Q^2` term;
6. reversal of the danger sign;
7. corruption of one derived coefficient;
8. deletion of one Bernstein control.

The audit also checked that numerical evidence is not promoted to a theorem,
chart illegality is not called raw negativity or maximality, and
CE-046/048/059/060 are not reused.

## Implementation events

The first scout attempt exposed a symbolic-bool implementation error and
failed closed before any conclusion. The corrected exact rational endpoint
gate passed. The first formal-normal invocation selected an existing Python
without `sympy`; the preserved project-compatible Anaconda interpreter with
`sympy 1.13.3` was then used. Neither event is a mathematical finding, and no
environment was installed, copied, or modified.

## Classification

- Fatal findings: **0**.
- Major findings: **0**.
- Minor findings: **0**.

The local y-strip theorem is independently certified, subject strictly to the
scope stated above.
