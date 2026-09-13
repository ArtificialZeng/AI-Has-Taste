# Certified finite theorem for the stratum \(i=3\)

## Statement

For every pair of integers \((n,j)\) with

\[
8\le n\le 100{,}000{,}000,\qquad 4\le j\le\lfloor n/2\rfloor,
\]

there is an odd prime \(p\) such that

\[
p\mid\binom n3\quad\text{and}\quad p\mid\binom nj.
\]

Since an odd prime is exactly a prime \(p\ge3\), this is the original weak
Erdős--Szekeres assertion on the complete finite stratum \(i=3\) through the
stated endpoint.  For \(n<8\) the \(i=3\) domain is empty.

## Completeness reduction

Put \(A_n=\binom n3=n(n-1)(n-2)/6\), and let \(S_n\) be the set of odd
prime divisors of \(A_n\).  The set is reconstructed without factoring a
large binomial coefficient:

- every prime \(p>3\) belongs to \(S_n\) exactly when it divides at least one
  of \(n,n-1,n-2\), because \(p\nmid6\);
- among three consecutive integers exactly one is divisible by \(3\), so
  \(3\in S_n\) exactly when that integer is divisible by \(9\), equivalently
  \(n\bmod9\in\{0,1,2\}\).

For a fixed \(p\in S_n\), Lucas's theorem says

\[
p\nmid\binom nj
\quad\Longleftrightarrow\quad
j_r\le n_r\ \text{for every base-}p\text{ digit }r. \tag{14}
\]

Choose any anchor \(a\in S_n\).  A weak counterexample at this \(n\) would
have to belong to the finite set \(T_a(n)\) of all \(j\) in the stated range
whose digits satisfy (14) for \(p=a\).  It is therefore complete to enumerate
\(T_a(n)\) and, for each member, ask whether every \(p\in S_n\) also satisfies
(14).  If none does, every admissible \(j\) has a common odd prime.

The discovery scanner chooses an anchor minimizing the number of base-digit
subchoices and tests (14) directly.  The verifier independently chooses the
largest prime in \(S_n\), regenerates its digit-subchoice set iteratively, and
for every other prime evaluates

\[
v_p\binom nj=v_p(n!)-v_p(j!)-v_p((n-j)!)
\]

by Legendre's formula.  Thus the decisive divisibility predicate is derived
twice.

## Release binding

The already-completed strict verifier output reports
`anchor_candidates=43631335536`; the canonical discovery JSON reports
`candidate_indices_tested=43631335536`.  The C++ verifier reconstructed the
mathematical range but did not read the latter diagnostic field.  Therefore
`code/verify_release_binding.py` supplies a fast, fail-closed cross-artifact
layer.  It pins exactly

\[
n_{\min}=8,\quad n_{\max}=100{,}000{,}000,\quad i=3,
\quad C=43{,}631{,}335{,}536,
\]

parses the canonical certificate and strict output with duplicate rejection,
asserts that both counts equal \(C\), and pins the SHA-256 hashes of the
certificate, verifier source, and strict output plus the binary build command.
It parses elapsed time only as a nonnegative integer and never uses it as
evidence.  The binder and its complete tamper matrix pass from an external
working directory in both normal Python and `python -O` mode.

## Boundary and degeneracy audit

- \(j=4\) and \(j=\lfloor n/2\rfloor\) are included.
- Even and odd \(n\), including the central coefficient when \(n=2j\), are
  included.
- The equality prime \(p=i=3\) is included exactly after the cancellation by
  \(3!\); it is neither always inserted nor discarded.
- Prime multiplicities are irrelevant to the existence statement, but the
  full set of distinct odd prime divisors is reconstructed.  No probable-prime
  test or floating-point computation is used.
- Empty anchor sets are treated as internal errors.  (Sylvester--Schur also
  implies they cannot occur in this domain.)
- Unsigned overflow is absent at the certified endpoint: factor-table indices
  are at most \(10^8\), products used for sieve bounds and base places use
  64-bit integers, and counters use 64-bit integers.

## Independent overlap

`code/brute_oracle.py` directly constructs the two arbitrary-precision
binomial coefficients and their gcd for every \((n,3,j)\) with
\(8\le n\le2000\).  It checks 994,009 pairs and returns no counterexample.
Both optimized implementations agree on this overlap.

## Reproduction

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

Runtime and candidate counts are diagnostic only.  The claim depends on the
exact range, successful exhaustive exits, source hashes, and the completeness
argument above.
