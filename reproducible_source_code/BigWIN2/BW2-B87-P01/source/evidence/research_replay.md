# Exact finite sanity-check replay

Job: `win-00087-p01-research-981c2d1e0004`  
Date: 2026-09-11  
Interpreter: Python 3.10.12  
Script SHA-256:
`7e0d5638fdcaecfb0dc8c927abd79ba86c982fa67896c3a8145bc464d70d3ee1`

Command, run from the project root:

```text
python3 evidence/triage_check.py
```

Exact standard output:

```text
structural tournaments checked: {3: 8, 4: 64, 5: 1024, 6: 32768}
upper-construction k-subsets checked: {3: 20, 4: 35, 5: 56, 6: 84, 7: 120, 8: 165, 9: 220, 10: 286, 11: 364, 12: 455}
cover inequality checked for 3 <= q <= 100
```

The process exited with status 0. The tournament enumeration is exhaustive
only for labeled orders 3 through 6; the block-construction check covers only
the displayed values of `k`; and the inequality loop covers only the displayed
finite range. These computations are non-proof sanity checks. The quantified
argument is in `evidence/research_proof.md`.
