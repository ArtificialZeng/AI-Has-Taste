# Research pass 1 evidence

Job: `win-00058-p02-research-bef70eb13095` (2026-09-07).

## Frozen artifact and runtime

Artifact path:
`/home/ailab/4math-open-problems/batches/inbox/bigWin-58-materials/ternary-synchronization-strings-artifact`.
`git rev-parse HEAD` returned the required clean commit
`5e9e0c05fca32a5d5735cab9914626ffe667c53c`; `git status
--porcelain=v1` was empty.

Runtime: Python 3.10.12; Node was not installed. Thus `python3 verify.py
--integrity-only --verbose` stopped at its explicit Python >=3.11 check (exit
1, 0.02 s). This is an operational limitation, not mathematical evidence.
Direct exact-rational scripts did run.

SHA-256:

- `verify.py`: `34b7ac8cbfceec419aacaa391d195c0c11fcf4d3963d7430599d800032ff40d2`
- `verifiers/verify_d227_lll.py`: `751b918de2d71ce2382b131ba1853e75420c6f3b7ef5a91c2c69d97171d26465`
- `verifiers/independent_verify_d227_lll.py`: `624307b26d8f65c5b13206c5836af4707dadbb6e75eaa506221f4fed2a75b4d4`
- `inputs/codewords_54_952.txt`: `a1b4b912d956419ef59a15e5d0926ce337614a438da25923e19a65485da05e28`

## Exact LLL runs

Both exact implementations reproduced D=227 with the published exclusions,
bilateral conditioning, `alpha=51/100000`, `beta=3/10`. The primary run
reported `D227_exact_finite_and_rational_tail_pass`, 34,788 event types,
`R0=0.000509300736717634449635...`, `109R0+R1=
0.296207062950587881931506...`, positive slope margin
`0.000000699263282365550364...`, and positive constant margin
`0.003792937049412118068493...` (3.11 s). The independent run reported
`INDEPENDENT_D227_EXACT_REPLAY_PASS` with matching displayed margins (20.46 s).

The required D=226 control used the primary script with `--exclude-totals ''
--bilateral --diagnostic`. It reported
`D226_exact_finite_and_rational_tail_fail`, 35,196 event types,
`R0=2.208493245259021453872562...`, `109R0+R1=
766.839396204455042964659574...`, and maximum-charge witness lengths
`(113,114)` at total 227. The first failed verifier condition is the individual
charge cap. Its exact upward-rounded certificate is

`181482402409940458316086075586 / 10^30 > 1/6000`,

as certified by the integer cross-products
`1088894414459642749896516453516000 > 10^30`. The underlying two directional
volumes are 114 and 342; the selected bilateral bound uses the left mass
`1/952`. This raw-bound failure does not establish that the shell is nonempty.

For deletion total `e`, the D=226 event sum gains exactly the totals
`s == e (mod 2)` with `226e < s <= 227e`. Within the finite verifier range
through 4000 these are:

- e=1: 227; e=2: 454; e=3: 679,681; e=4: 906,908;
- e=5: 1131,1133,1135; e=6: 1358,1360,1362;
- e=7: 1583,1585,1587,1589; e=8: 1810,1812,1814,1816;
- e=9: 2035,2037,2039,2041,2043; e=10: 2262,2264,2266,2268,2270;
- e=11: 2487,2489,2491,2493,2495,2497;
  e=12: 2714,2716,2718,2720,2722,2724;
- e=13: 2939,2941,2943,2945,2947,2949,2951;
  e=14: 3166,3168,3170,3172,3174,3176,3178;
- e=15: 3391,3393,3395,3397,3399,3401,3403,3405;
  e=16: 3618,3620,3622,3624,3626,3628,3630,3632;
- e=17: 3843,3845,3847,3849,3851,3853,3855,3857,3859.

Only 227 and 454 are newly relevant bounded one-/two-deletion shells; all
higher additions are retained and exactly charged by the verifier (with the
denominator-specific analytic tail recomputed beyond 4000).

## New shell audit and conditional D=226 test

`evidence/audit_one_deletion_shell.py` independently enumerated total 227.
All 132,240 cases (both orientations, all 54 offsets, all deletion positions,
and every normalized square-free outer context) were killed by a local exact
codebook incompatibility; there were zero CSP residuals. Histogram by killing
edge index: `{0: 99804, 1: 32022, 2: 414}`. Runtime 9.98 s.

As a cross-check, the same script at the published total 229 exactly reproduced
the certificate's 135,240 cases and histogram
`{0: 100219, 1: 27077, 2: 7944}`, with zero residuals.

A conditional D=226 run excluding the published empty shells plus the newly
proved-empty total 227 and the **not-yet-audited** total 454 passed in both
exact implementations. The primary margins were
`alpha-R0=0.000000618068890291343247...` and
`beta-(109R0+R1)=0.003728877584891028227619...`; the independent run displayed
matching margins. This is only a conditional diagnostic until total 454 is
proved empty (or otherwise bounded), and is not yet a proof of C(226).
