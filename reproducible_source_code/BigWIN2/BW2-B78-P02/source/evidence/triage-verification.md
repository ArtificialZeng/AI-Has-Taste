# Triage verification record

- Job: `win-00078-p02-triage-4c13b35c51f8`
- Date: 2026-09-10
- `sha256sum source.md`:
  `f9adb36e67090507335a9f6da0565b5ccaab0a8243cf217146d1f5c14097e858`
- `sha256sum ../../batches/inbox/bigWin-78-materials/2609.05100.pdf`:
  `948965eb5b52a0229289fb7ac885ad02fdd2860d07b55724ee717f7bb2585bdf`
- The PDF has 30 pages. `pdftotext -f 17 -l 17 -layout` contains equations
  (22)--(25) and Remark 3.6; `pdftotext -f 27 -l 27 -layout` contains Theorem
  3.23. These passages support the comparison recorded in `problem.md` but do
  not resolve the frozen census.
- Fresh output of `python3 evidence/triage_verification.py`:

```text
labelled=31465
fixed=133
orbits=15799
boundary_Sv=(0, 0)
boundary_rank_minor=1
```

This checks only the finite search size, involution count, and one nonempty
boundary example. It is not a proof or disproof of the frozen assertion. No
retained-network count from an absent earlier script is used.
