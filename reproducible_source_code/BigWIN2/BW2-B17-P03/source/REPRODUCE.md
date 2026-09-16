# Reproduction

Run from the project root with Python 3.10 or later:

```sh
python3 computation/check_witness.py
python3 computation/crosscheck_small.py
python3 computation/clique_search.py 528 41 /tmp/clique.log || test $? -eq 1
python3 computation/packing_verify.py 528 41 /tmp/packing.log || test $? -eq 1
tail -1 /tmp/clique.log
tail -1 /tmp/packing.log
```

Both final lines must begin `overall=UNSAT`.  The decision programs use exit
code 1 for UNSAT, so that exit code is expected at the negative endpoint.
No third-party Python package is used.
