# Exact finite certificate

Run from the project root:

```sh
python3 certificates/verify_certificate.py
python3 tests/test_certificate_rejection.py
```

The first command compiles `verify_n10.cpp` with warnings as errors in a fresh
temporary directory, parses `n10_finite_certificate.txt` with a closed schema,
and reconstructs every object needed for the conclusion.  It does not read
any file under `experiments/` or `results/`.

The serialized certificate contains only the endpoint, canonical word,
Fibonacci normalization, and claimed aggregate counts.  The verifier does
not trust these counts: it enumerates the full interval and all comparable
pairs, then rejects any mismatch.  No per-pair polynomial or discovery table
is imported.

The second command first verifies the untouched input and then requires eight
damaged inputs to fail with nonzero status: missing end marker, duplicate key,
wrong endpoint, overflowing endpoint, changed word, changed Fibonacci
recurrence, unknown key, and changed complete-pair count.

For every $2\le n\le10$, the verifier also constructs the canonical product
classes indexed by nondecreasing parts $h_i\ge2$ with
$\sum_i h_i\le n-2$ and requires exact set equality with the normalized
classes seen among all comparable pairs.  This certifies the reported
factor-pattern description as a finite observation.

Mathematical completeness and the two independent recurrences are explained
in `proof/finite_theorem.md`.
