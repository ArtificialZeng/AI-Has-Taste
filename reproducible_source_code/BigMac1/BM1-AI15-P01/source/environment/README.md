# Verification environment

The decisive verifiers use only the Python standard library (`json`,
`fractions`, `itertools`, `hashlib`, and `pathlib`).  They have no PyPI
dependencies and use no random numbers.

Primary audit environment:

- macOS / Darwin arm64
- Python 3.13.5 for the root verifier runs
- SymPy 1.13.3 only for non-trusted symbolic cross-checks
- Poppler and TeX versions are recorded in the clean-build log

An independent breaker run was also recorded under Python 3.14.7.  Exact
rational output, rather than interpreter-specific floating-point behavior,
is the certified endpoint.

The final source-archive portability audit used `python3 -I` under Python
3.14.7 in a new `/tmp` extraction directory.  It imported no project cache or
site package for the standard-library verifiers.

Fast verification:

```bash
python verifier/run_all.py --fast
```

Full exact verification (including independent discovery reconstruction):

```bash
python verifier/run_all.py
```
