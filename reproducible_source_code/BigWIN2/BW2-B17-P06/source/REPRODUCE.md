# Reproduction

Run from this project directory with Python 3.10 or later:

```text
python3 code/verify_certificate.py certificates/mu41_witness.json
PYTHONPATH=code python3 code/bruteforce_crosscheck.py
python3 code/exact_search.py --n 41 --witness certificates/mu41_witness.json --output certificates/mu41_exhaustive_result.json
```

The first command is a fast independent upper-bound check. The second performs
a Cartesian brute-force comparison for every (N\le10). The third is the full
lower-bound enumeration (about seven minutes in the recorded WSL2 run). It
must end with `"cheaper_cover_exists": false` and exit status 0.

The discovery-only environment used SciPy 1.15.3/HiGHS. Discovery output is
not trusted by any proof. Certification uses only the Python standard library,
has no random seed, and compares exact integers or `fractions.Fraction` values.
