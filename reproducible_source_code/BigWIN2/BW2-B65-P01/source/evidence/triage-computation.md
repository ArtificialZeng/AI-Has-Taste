# Exact finite triage computation

On 7 September 2026, `python3 evidence/triage_check.py` completed successfully
for every integer `K` from 1 through 25. The script computes the recurrence with
integer `mex` only. For each such `K` it verifies a length-`c` induction window
of 5-periodicity beginning at `q=2c+5`, the failure of 5-periodicity at `q-1`,
and nonconstancy of the eventual 5-block. In every case the block is `02101`
and the boundary mismatch is `2 != 1`.

This is an exact finite observation, not evidence for the universal quantifier.
The script prints a SHA-256 digest of each computed prefix so its output can be
compared across independent reruns.
