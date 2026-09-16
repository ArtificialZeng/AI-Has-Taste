# Research pass 2 progress

Job: primary-20260913-subsum-denominator-research-983c87564404.

Read source.md, problem.md, checkpoint.md, full research role instructions,
pass-1 mathematical dossier and relevant implementations. No literal
literature/*handoff*.md files exist. Read outer-intake.md and checked
its product and dyadic recurrence against live BBFM Propositions 3.8--3.10;
Chen--Ono--Zhang v2 Table 1 retains the denominator shape claim as open.

The frozen K held-out test is running as a single foreground Python process:
`python3 evidence/research2_kernel_probe.py --B 64`. The algorithm is copied
from research_kernel_probe.py with only output path, provenance and scope
metadata changed; prior scripts and certificates remain intact.
No mathematical conclusion from the pending computation.

One next test: inspect every Newton coefficient for 33<=j<=64; independently
recompute any negative and distinguish K failure from H failure.

## Saved outcome of assigned test

Frozen K passes all 185,185 coefficients through j=64, including 160,688
held-out coefficients in 1,584 polynomials for 33<=j<=64. The new certificate
is research2_kernel_probe.json. The separate logarithmic-derivative verifier
research2_verify.py reproduces every coefficient by signed binomial sums and
checks 3,068 earlier finite cases; see research2_verify.json. This extends the
computer-assisted edge result to 64 for every n, with the pass-1 induction
bases and symmetry. No infinite K conclusion follows.

research2_band.md records a proved uniform positivity band: for Newton order
h=2j-k, the coefficient is nonnegative whenever j>=2k^2+k-1. Lower orders
remain unresolved. The top two rows have explicit Catalan formulas.

A sharpened affine-exponent threshold has been identified algebraically:
all exponents through degree j+1 are affine under doubling once 2n>j+1
(previous sufficient condition was n>=j+1). Testing K at this earlier
starting point is in progress.

This progress note is superseded by the completed dossier `research2.md` and current checkpoint.
