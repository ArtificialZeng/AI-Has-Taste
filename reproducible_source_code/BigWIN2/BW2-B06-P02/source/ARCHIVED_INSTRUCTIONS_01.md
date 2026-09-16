# Reproduction

From the project root, the proof certificate and independent calculation are
checked with only the Python 3 standard library:

```bash
python3 verify/verify_certificate.py
python3 verify/independent_checker.py
python3 verify/test_verifiers.py
```

Expected mathematical endpoints:

- 30 regenerated targets;
- witness length 94;
- maximum assignment overlap 146;
- assignment-dual inequality count 930;
- lower bound `240-146=94`.

The optional discovery replay requires SciPy and NumPy:

```bash
python3 experiments/discover_overlap_milp.py
```

Its floating solver status is diagnostic and is not a proof dependency.
