# Exact computation

`scan_i3.cpp` and `verify_i3.cpp` implement independent complete enumerations
of the stratum \(i=3\).  They share only the theorem endpoint and input/output
format, not source code or the decisive evaluator:

- the scanner uses a linear sieve, rolling factorization, a minimum-cardinality
  Lucas anchor, and Lucas digit tests;
- the verifier uses a classical Eratosthenes SPF table, refactors all numerator
  terms, chooses the largest anchor, and checks the other primes by Legendre
  valuations;
- `brute_oracle.py` computes literal binomial coefficients and gcds over a
  smaller complete overlap.

For \(i=3\), a weak counterexample is exactly a pair for which no odd prime
divides both binomial coefficients.  The programs factor the odd prime support
of

\[
\binom n3=\frac{n(n-1)(n-2)}6.
\]

For every such prime \(p\), Lucas's theorem characterizes the indices \(j\)
where \(p\nmid\binom nj\).  Enumerating the nondivisible indices for one anchor
prime and testing the remaining prime support is therefore complete, not
probabilistic.

`verify_release_binding.py` is a fast fail-closed release layer.  It does not
rerun the exhaustive search.  Instead it pins the exact endpoint, stratum,
canonical certificate, already-completed strict output, verifier source, and
build command; it also checks that the certificate and strict output both
record 43,631,335,536 anchor-compatible indices.  Runtime is ignored.

Build and run:

```bash
c++ -O3 -std=c++17 -Wall -Wextra -pedantic code/scan_i3.cpp -o code/scan_i3
c++ -O3 -std=c++17 -Wall -Wextra -pedantic code/verify_i3.cpp -o code/verify_i3
code/scan_i3 8 100000000 > certificates/i3_scan_100m.json
code/verify_i3 certificates/i3_scan_100m.json
python3 code/brute_oracle.py 8 2000
python3 code/verify_release_binding.py --root . \
  --binding certificates/i3_release_binding.json
python3 code/test_release_binding.py
```

Elapsed times in output are diagnostics only and are not mathematical
evidence.  The certified claim is determined by the exact serialized range and
the independent verifier's successful exit.
The Python tamper test stages copies outside the project and checks normal and
`-O` modes; it rejects changed endpoints, bad hashes, changed counts,
truncated output, and duplicate JSON fields.
