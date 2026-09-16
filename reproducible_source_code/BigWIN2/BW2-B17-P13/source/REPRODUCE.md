# Reproduction

Run from the project root with Python 3.10.12.

Fast exact witness check:

```sh
python3 code/verify_witness.py certificates/witness_65.json --n 38 --k 12 --minimum 65
```

Encoding cross-check (all subsets for every `1 <= k <= n <= 10`):

```sh
PYTHONPATH=code python3 code/crosscheck_small.py
```

Regenerate and solve the target CNF (PySAT 1.8.dev24):

```sh
python3 code/sat_decision.py --target 66 --cnf no_66.cnf --result sat_target66.json --solver glucose42
```

The released target CNF is `certificates/no_66.cnf`; the refutation is
`certificates/no_66.drup`.  Check it with the included Debian drat-trim
0.0~git20240428.effa1dc-2 binary:

```sh
third_party/drat_trim_root/usr/bin/drat-trim certificates/no_66.cnf certificates/no_66.drup
```

The expected terminal line is `s VERIFIED`.  The discovery-only local-search
and CP-SAT commands, seeds, versions, and complete outputs are retained under
`experiments/discovery/` and `logs/`; neither is a theorem dependency.
