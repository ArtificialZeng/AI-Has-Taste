# Independent post-referee `builder_notes` diff audit

Audit date: 2026-08-29 (Asia/Shanghai)  
Auditor: independent counterexample/referee agent, read-only audit.

## Verdict

**PASS on mathematical scope, with a provenance qualification.**  Every
change to `proof/builder_notes.md` after the referee pass maps to a local or
expository repair explicitly listed in `audit/referee_low_degree.md`.  No
change proves, assumes, or numerically promotes Q4-U or Q5-U.

It would, however, be inaccurate to say that the byte diff consists of only
five narrowly defined hunks.  `audit/PROOF_AUDIT.md` compressed the repairs
into five broad categories.  The direct diff also contains explicit repairs
R3, R8, and R11 from the referee report.  The accurate statement is:

> All changes map to referee-listed local or expository repairs; the proof
> audit summarizes them using five broad categories.

## Byte-level reconstruction

This directory has no Git history and contained no `.bak`, `.orig`, patch
file, or independently preserved pre-referee snapshot.  The project CLI log
does retain the complete echo of all four builder patches.  Reversing those
patches hunk by hunk from the current file uniquely reconstructs a candidate
pre-referee text.

```text
reconstructed pre-referee text: 13707 bytes, 390 lines
reconstructed SHA-256: 4f60148d59831d846831a4701dde91c0a9fb3756aac1bcbf624b9a41d3183ed8
current text: 15651 bytes, 439 lines
current SHA-256: 126ec4120fd2984a300d35805f074fa932a37b79bf555925f53b12c1d34001df
direct reconstructed diff: 10 hunks, +83/-34 lines
four sequential patches: +17/-12, +35/-18, +29/-4, +11/-9 lines
```

The sequential totals differ from the direct totals because the Schur
paragraph was repaired twice.  As a strong cross-check, reversing only the
last Schur rewrite produces SHA-256
`e63837679623d8e7963714c25c3aa23e7b0294f77f78976c43e803651571c880`,
exactly the intermediate hash recorded in the tool log and the subsequent
`PROOF_AUDIT` hash-refresh patch.

The pre-referee digest was reconstructed after the fact, not frozen before
editing.  Therefore this is a **deterministic byte diff reconstructed from
complete tool-patch provenance**, not a comparison against an independently
stored baseline.  The audit found no builder write outside those four logged
patches; other log occurrences were reads, hash calculations, or manifest
references.

## Hunk-to-referee mapping

| Current location | Change | Referee finding |
|---|---|---|
| lines 17--20 | restrict generic phase wording to the rotations actually used | R1 / section 1.1 |
| lines 37--40 | add positive root separation/Rouche justification | R2 / section 1.2 |
| lines 48--49 | state the radial converse for zero as a boundary value | R3 |
| lines 66--76 | make the unit-circle Schur branch and equality/degree handling explicit | R4 / section 1.3 |
| lines 138--149, 424--430 | handle exact degree and equal-product cases | R5, R7, R8 |
| lines 205--221 | replace cubic first-loss shorthand by root-count homotopy | R6 / section 3.4 |
| lines 229--235, 424--430 | separate scalar/modulus equality and record the audited `7/6` radius | R7, R8 |
| lines 301--311 | spell out the quartic endpoint/root-count homotopy | R6 / section 4 |
| lines 398--413 | spell out the quintic homotopy and punctured inclusion | R6, R11 / section 5 |

The referee's table classifies R1--R8 and R11 as local or expository.  The
only major findings, R9 and R10, are Q4-U and Q5-U; current builder lines
337--342 and 415--418 continue to leave both open.

## Scope and proof-assistant disclosure

No theorem range, endpoint condition, all-unimodular condition, or numerical
claim changed.  No proof assistant was used.
