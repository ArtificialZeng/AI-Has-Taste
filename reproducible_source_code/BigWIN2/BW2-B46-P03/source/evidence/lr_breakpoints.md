# Exact Lemma 2.2 breakpoint enumeration

Provenance: `win-00046-p03-research-1cb48fc8a166` (research pass 1).

`evidence/lr_breakpoints.py` constructs all three families in Zhang's Lemma
2.2 and evaluates
\(f_V(t)=\min_{v\in V}\|vt\|\) at every distinct candidate using Python
`fractions.Fraction`.  It uses no floating-point arithmetic.  The complete
machine-readable output, including the number of distinct breakpoints and the
active minimizing speeds at the selected witness, is
`evidence/lr_breakpoints_results.json`.

This is an exact finite computation conditional only on the cited breakpoint
lemma and the inspectable implementation.  It has not yet been repeated by an
independently implemented exact checker.

| \(n\) | \(w\) | exact \(LR(V_{n,w})\) | attaining \(t\) | vs. \(1/n\) |
|---:|---:|:---:|:---:|:---:|
| 14 | 24 | 1/14 | 1/14 | equal |
| 46 | 46 | 2/59 | 5/59 | greater |
| 46 | 47 | 2/61 | 5/61 | greater |
| 46 | 48 | 2/59 | 5/59 | greater |
| 46 | 49 | 2/59 | 5/59 | greater |
| 46 | 50 | 2/59 | 5/59 | greater |
| 47 | 47 | 2/61 | 5/61 | greater |
| 47 | 48 | 2/59 | 5/59 | greater |
| 48 | 48 | 2/61 | 5/61 | greater |
| 48 | 49 | 2/65 | 27/65 | greater |
| 48 | 50 | 2/61 | 5/61 | greater |
| 50 | 50 | 2/65 | 27/65 | greater |
| 50 | 51 | 2/65 | 27/65 | greater |
| 50 | 52 | 2/65 | 27/65 | greater |
| 50 | 53 | 2/67 | 28/67 | greater |
| 50 | 54 | 2/65 | 27/65 | greater |
| 50 | 55 | 2/65 | 27/65 | greater |
| 50 | 56 | 2/65 | 27/65 | greater |
| 51 | 51 | 2/65 | 27/65 | greater |
| 51 | 52 | 2/65 | 27/65 | greater |
| 51 | 53 | 2/67 | 28/67 | greater |

The positive control therefore agrees exactly with the known tight pair.  For
all 20 pairs left by `evidence/triage_bounds.md`, the computed value is strictly
greater than \(1/n\), so none is tight if this enumeration is confirmed.

## Reproduction

From the project directory, run:

```text
python3 evidence/lr_breakpoints.py
```

The script deterministically rewrites the JSON result file.
