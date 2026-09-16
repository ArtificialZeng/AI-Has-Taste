# Triage computation replay

Date: 2026-09-11  
Job provenance: `win-00087-p04-triage-d0663423f5b1`

The supervisor-supplied assets named in `source.md` were found at
`/home/ailab/4math-open-problems/batches/inbox/bigWin-87-materials/04_radial/`.
Their SHA-256 hashes at inspection were:

```text
5af0cc5157fd79f06ca8dbed812f34974bc174cf59459b2183ba4cf0110d471a  check_classification.py
b07b163b886806620ac3719278005748b9e665344d1f1dce2f41b96697360b79  verify.py
151aad4a7e4ec0d3f7a2582e7ca604078b65b8cddb8375d7e5891f78328f14d0  exact_census.json
```

Running the classification checker with `python3` produced:

```text
PASS: all 31 classes; precisely the 7 stated linear-forest complement cases fail.
```

For a live replay without overwriting the supplied census, `verify.py` was
imported as a module. Its `small_graphs()` and exact
`fractions.Fraction`-based `hilbert()` routines were run for every graph and
for the pendant-edge realization of its coloop extension. After normalizing
Python tuples to JSON arrays, the newly generated rows, including all echelon
certificates, compared equal to `exact_census.json`:

```text
RECOMPUTE_MATCH True
graphs 31 seconds 6.001
counts_by_n {1: 1, 2: 1, 3: 2, 4: 6, 5: 21}
nonzero 7
```

The seven live nonzero rows have edge counts
`6, 7, 7, 8, 8, 9, 10` and differences, in that order,

```text
[0,0,2,2,0,0]
[0,0,2,2,0,0]
[0,0,2,2,0,0]
[0,0,1,2,0,0]
[0,0,4,0,0,0]
[0,0,4,0,0,0]
[0,0,4,0,0,0]
```

The unique six-edge row is

```text
H     = [1,6,11,6,1]
Hplus = [1,7,19,19,7,1]
delta = [0,0,2,2,0,0].
```

These are exact finite computational observations conditional on the inspected
implementation. They are not yet a proof that the implementation matches the
mathematical definitions, nor an independent second implementation.
