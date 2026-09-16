# Exact certificate

Run from the project root:

```bash
python3 certificates/certify_exact.py
python3 certificates/verify_symbolic.py
```

The first command needs Python 3.10 or later and no third-party package. The
second was checked with Python 3.10.12 and SymPy 1.14.0. Both fail closed on a
missing field, wrong final state, uncertified floor, nonpositive norm gap, or
failed cutoff.

`nonparry_d4.json` is the shared exact input. `certify_exact.py` uses rational
interval arithmetic; `verify_symbolic.py` uses exact Sturm root counts and
symbolic polynomial remainders. Neither verifier imports the floating-point
discovery program.
