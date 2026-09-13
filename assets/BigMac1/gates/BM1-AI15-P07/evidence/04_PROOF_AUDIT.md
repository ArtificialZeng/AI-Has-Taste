# Proof audit

Audit date: **2026-08-29**.

## Audited claim

For every \(8\le n\le100{,}000{,}000\) and
\(4\le j\le\lfloor n/2\rfloor\), an odd prime divides both
\(\binom n3\) and \(\binom nj\).  No claim for \(n>10^8\) or general
\(i\ge4\) is included.

## Mathematical completeness

1. The odd-prime support of \(\binom n3=n(n-1)(n-2)/6\) is exact:
   every \(p>3\) comes from one of the three numerator terms, while \(3\)
   survives exactly for \(n\bmod9\in\{0,1,2\}\).
2. Lucas's theorem gives an if-and-only-if characterization of the indices
   avoiding each support prime.  Therefore every counterexample must occur in
   the anchor prime's complete digit-subchoice set; testing all support primes
   on every such index is exhaustive.
3. The interval endpoints \(n=8\), \(n=10^8\), \(j=4\), and
   \(j=\lfloor n/2\rfloor\) are inclusive.  The central case \(n=2j\),
   odd/even rows, and the equality prime \(p=i=3\) are retained.
4. The proof uses exact unsigned integer arithmetic.  At the certified
   endpoint, sieve indices fit in 32 bits, products/base places and counters
   fit in 64 bits, and Legendre valuation sums fit in 32 bits.

## Independent reconstruction and attacks

- Discovery: linear SPF sieve, rolling factorization, minimum-cardinality
  anchor, Lucas evaluator.
- Verifier: classical Eratosthenes SPF table, fresh factorization of all three
  terms at every row, largest-prime anchor, and Legendre valuation evaluator.
- Definition-level oracle: arbitrary-precision binomial coefficients and
  literal gcds for all 994,009 admissible pairs through \(n=2000\).
- Fail-closed parser: missing-field, duplicate-key, and non-null fixtures all
  exit with status 2 before enumeration.
- Release binder: canonical certificate and strict output are parsed together;
  endpoint, stratum, and both 43,631,335,536 counts are equated and bound to
  the certificate/source/output hashes.  Its eight-case external-cwd matrix
  passes under Python normal and `-O`.

The final strict verifier rebuilt the full range from the serialized input and
exited 0 after testing 43,631,335,536 anchor-compatible indices.  The scanner
and verifier report the same diagnostic count, although the count is not a
proof premise.

## Hash binding

| Artifact | SHA-256 |
|---|---|
| `code/scan_i3.cpp` | `4d082ab479f1afe267dd4eea26cbbed03de1038a3f053f108ec34b183b159338` |
| `code/verify_i3.cpp` | `5365f052cd14ae35efa5e7efed5008584fb4ab523f8f1a6c51058a14a2d9bcd5` |
| `code/brute_oracle.py` | `671a1dfe110d59ffedfca81d84b6aa24b5f116a39edd968965ae3261c20e1f06` |
| `certificates/i3_scan_100m.json` | `23c45255e41877ccde381d86564e991ced9b7e08b8559f48405f4a759b51f0ba` |
| `certificates/i3_verify_100m_strict.txt` | `9a1a430068f5813195a90b0f22937095008b50f84c66fb311ca64ff3dc2904ab` |
| `certificates/i3_brute_2000.json` | `7ec7aa3ea271f797b28ac1e920eebcfe046ec60962864950bd02792142d0748a` |
| `code/verify_release_binding.py` | `bfbcf3fd1ef16089cd7f3b6ca6092df64e2d6340ade73788d021392b7cc444cf` |
| `certificates/i3_release_binding.json` | `6f3ad7c49a882c8ea4bcddb81cdd04ba4690055100798f2f9743663077d08195` |
| `logs/release_binding_tamper_matrix.txt` | `093af76e00801f7d20328f11c50462a6015763e2821be504115080c80634a7b9` |

## Verdict

**Pass for the stated finite theorem.**  G01 in `proof/gap_ledger.md` remains
fatal only to a proof of the original infinite conjecture; it is not a gap in
the finite theorem.  The two C++ programs
were independently derived but produced in the same Codex-assisted research
session; the direct-gcd oracle and transparent completeness proof mitigate,
but do not erase, that common-provenance risk.
