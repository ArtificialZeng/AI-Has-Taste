# Independent exact interval-cover verification

Provenance: `win-00046-p03-research-fe7d2696b6ab` (research pass 2).

## Certificate logic

This pass independently verifies every exact value reported in
`lr_breakpoints_results.json`; it does not enumerate or use breakpoints.  For
a speed (v) and rational (0\le q\le 1/2),
\[
 \{t\in[0,1]:\|vt\|\le q\}
 =\bigcup_{k=0}^{v}
 \left[\frac{k-q}{v},\frac{k+q}{v}\right]\cap[0,1].
\]
Consequently, a chain of these closed intervals that begins at (0), has no
gap between consecutive intervals, and ends at (1) proves
\(LR(V)\le q\).  If, at a specified rational time (t_0), direct evaluation
gives \(\min_{v\in V}\|vt_0\|=q\), then (LR(V)\ge q), hence (LR(V)=q).

`lr_interval_cover.py` implements exactly this argument with
`fractions.Fraction`.  The 21 tuples ((n,w,q,t_0)) are constants in the
file.  It does not import, invoke, or read either `lr_breakpoints.py` or its
result JSON.  For each tuple, `lr_interval_cover_results.json` saves:

- every labeled interval in a greedy exact cover chain of ([0,1]);
- all exact distances \(\|vt_0\|\), not merely their asserted minimum; and
- the exact comparison of (q) with (1/n).

Each labeled interval includes its speed (v), nearest integer (k), and
exact endpoints, so the serialized chain is directly checkable against the
displayed formula.  The script asserts chain continuity, terminal coverage,
the direct lower equality, and the expected equality/strict-inequality pattern.

## Verified values

The positive control is
\[
 LR(V_{14,24})=1/14,
 \qquad t_0=1/14.
\]
The 20 residual values group as follows:

| Exact value | Residual pairs | Attaining time |
|:---:|:---|:---:|
| (2/59) | ((46,46),(46,48),(46,49),(46,50),(47,48)) | (5/59) |
| (2/61) | ((46,47),(47,47),(48,48),(48,50)) | (5/61) |
| (2/65) | ((48,49),(50,50),(50,51),(50,52),(50,54),(50,55),(50,56),(51,51),(51,52)) | (27/65) |
| (2/67) | ((50,53),(51,53)) | (28/67) |

All four residual values are strictly greater than the relevant (1/n).
Thus none of the 20 residual pairs is tight.

## Reproduction and cross-check

From the project directory, run:

```text
python3 evidence/lr_interval_cover.py
```

This deterministically rewrites `lr_interval_cover_results.json`.  Two runs
in this pass were byte-identical, with SHA-256
`cc4abaa1dda983faa06ba9608e93f34dfdd34b43a0d25d1dfc60fd922e585551`.
An exact key-by-key comparison found agreement on all 21 pairs, values, and
attaining times with the independently structured breakpoint output.  This is
a reproducibility cross-check, not a substitute for the certificate argument.

Together with the theorem-based exhaustion in `triage_bounds.md`, these
certificates prove that the unique tight pair in the frozen parameter space is
\((14,24)\).  This scope is proposed for fresh referee review; it has not been
accepted merely because the scripts ran successfully.
