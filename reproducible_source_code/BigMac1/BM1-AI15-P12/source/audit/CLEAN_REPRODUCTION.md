# Clean one-command reproduction audit

Date: 2026-08-29.  Status: **PASS**.

Command:

```bash
bash scripts/reproduce_clean.sh
```

The runner enforced CPython `3.13.5`, created a new temporary virtual
environment, installed only the hash-locked packages
`SymPy==1.13.3` and `mpmath==1.3.0`, and printed
`PINNED 3.13.5 1.13.3`.

It then passed:

- the pure-standard-library SOS verifier;
- the independent SymPy SOS verifier;
- all `badhash/extra/drop/tamper` fail-closed negative tests;
- the equality-family verifier;
- the binary-form discriminant verifier;
- both independent referee verifiers, including the PGL2/equality audit;
- reconstruction of all retained breaker records; and
- a clean `latexmk` build from only `main.tex` and `references.bib` in a
  separate temporary directory.

Final output:

```text
CLEAN LATEX PASS
ALL CLEAN REPRODUCTION CHECKS PASSED
```

Lock and runner hashes:

```text
requirements-repro.txt    2499b3a9bdf7be357e2aa9717150db275cb5b545686c6289b940afa662aff5b3
scripts/reproduce_clean.sh fdb587def08648a6af6cba1031271102c009c971df082d2f3ee10d153c712d05
```

The temporary environment and build directory were deleted after success.
