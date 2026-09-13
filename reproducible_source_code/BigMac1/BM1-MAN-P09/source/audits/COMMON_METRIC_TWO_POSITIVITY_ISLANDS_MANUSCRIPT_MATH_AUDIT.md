# Independent mathematical transcription audit

Date: 2026-08-23

Target: `manuscript/common_metric_two_positivity_islands/main.tex`

Status: **PASS after two minor clarifications**.

## Audited dependency chain

The independent reader compared the manuscript with the project theorem notes
and isolated referee artifacts listed in the manuscript README.  The audit
checked:

1. the finite-dimensional trace-dual equivalence and the coefficient `6`;
2. the direction in which the arrowhead trace-norm inequality is used;
3. the reduction from `P=pp*` and the balanced separator
   `W0=(1/2)diag(1,1,0)` to the original Hermitian scalar gate;
4. both factors `1/4`, the final coefficient `8`, every displayed conjugation,
   and the entries `(Q^2)_31`, `(Q^2)_32`;
5. the unified normalization
   `Gamma=4 mathcal G`, `Delta^2 Gamma=mathsf P(T)`, and `36 Gamma`;
6. every parameter range, PSD/rank statement, dangerous-sign condition, and
   strict-positivity conclusion in Theorems A and B; and
7. all logical scope statements excluding a global common-metric theorem or a
   solution of the fixed-crossing-lens problem.

## Findings

No blocking or major issue was found.  The trace-dual proposition, arrowhead
use, original gate, scale cubic, all-scale island, and positive-`Z`
moving-sheet island match the audited source material.

Two minor exposition points were repaired in `main.tex`:

- The scale-cubic proof now treats the endpoint case `g0=0`, `g1<0`
  explicitly, observing that its discriminant is positive and the criterion
  correctly rejects immediate descent from zero.
- Theorem B now states explicitly that `h=sqrt(S)` and
  `ell=sqrt(5) z/3` when constructing `Q_B`.

These changes clarify the proof but do not alter either certified theorem.

## Scope

This is a transcription and logic audit, not a new computer proof.  The exact
source/referee programs and their manifests remain the authorities for the
large rational certificates.  Release additionally requires clean rebuild,
PDF visual inspection, and a unified release manifest.
