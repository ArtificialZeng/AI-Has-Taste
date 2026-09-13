# Exact breaker run record

Status: discovery only; this is not an independently checkable finite
certificate.

## Environment

- Date: 2026-08-29 (run timestamps are in the JSON outputs, UTC)
- Host: Darwin 25.5.0, arm64
- C++ compiler: Apple clang 21.0.0, target `arm64-apple-darwin25.5.0`
- C++ language level: C++20 (`__cplusplus = 202002`)
- Python: 3.14.7, Clang 21.0.0
- Floating point and modular arithmetic: not used in any mathematical
  decision
- Deterministic seed: none; both programs are exhaustive and deterministic

## Commands

```sh
c++ -std=c++20 -O3 -Wall -Wextra -pedantic \
  experiments/breaker/exhaustive_rtilde.cpp \
  -o experiments/breaker/exhaustive_rtilde
experiments/breaker/exhaustive_rtilde experiments/breaker/run_summary.json \
  results/breaker_candidates.json
python3 experiments/breaker/independent_crosscheck.py \
  experiments/breaker/python_crosscheck.json
experiments/breaker/exhaustive_rtilde \
  experiments/breaker/run_summary_repeat.json \
  results/breaker_candidates_repeat.json
```

No candidate JSON was created in either C++ run because every visited pair
was accepted.

## Exact counts

| n | elements in `[e,v_n]` | comparable pairs | rejected | max coefficient |
|---:|---:|---:|---:|---:|
| 2 | 1 | 1 | 0 | 1 |
| 3 | 4 | 9 | 0 | 1 |
| 4 | 14 | 69 | 0 | 1 |
| 5 | 46 | 493 | 0 | 2 |
| 6 | 146 | 3,385 | 0 | 3 |
| 7 | 454 | 22,657 | 0 | 4 |
| 8 | 1,394 | 149,021 | 0 | 6 |
| 9 | 4,246 | 967,941 | 0 | 10 |
| 10 | 12,866 | 6,229,297 | 0 | 15 |

For every `n`, the subword enumeration of `[e,v_n]` agreed exactly with a
second enumeration by downward Bruhat covers.  The known endpoint identity
`P_{e,v_n}(t)=F_{n-2}(t)` also passed for every `2 <= n <= 10`.

The independent Python implementation checked `2 <= n <= 8` using all
permutations in `S_n`, the rank-matrix Bruhat criterion, ordinary uncompressed
polynomials in `q`, and exact integer polynomial division.  Its element,
pair, rejection, maximum-coefficient, and factor-pattern counts agree with
the C++ run throughout that range.

The second C++ run reproduced all exact fields, including the `n=10` stream
digest `b9cb2fe24d4461bf`.  Timings and timestamps were excluded from the
repeat comparison.

A separate build with Clang AddressSanitizer and UndefinedBehaviorSanitizer
also completed through `n=10` with the same exact counts and digest.  Leak
detection is unsupported by the installed macOS sanitizer runtime, so it was
explicitly disabled; address and undefined-behavior checks were enabled.

## Structural observation from the search

For every tested `n`, the set of factor patterns that actually occurs is
exactly

```text
F_{h_1} ... F_{h_k},  h_i >= 2,  sum_i h_i <= n-2,
```

including the empty product.  Thus the 22 patterns at `n=10` are in bijection
with all integer partitions of all integers at most eight into parts at least
two.  This is an exact statement about the retained exhaustive output, but it
is not yet a structural proof about arbitrary intervals or larger `n`.

## SHA-256 hashes

```text
5ec308fe603d8ddb70829782d4847574b5b33c183927c66aab5ae49daef37e6d  exhaustive_rtilde.cpp
d17ca58d3236336ef7ecee8ef96cae866a5566ffb5918fae5733972c248bb041  exhaustive_rtilde
a5d00d1b173706aa1bd6ca5c553db5e7827a4f8749e7152f755353024c850e18  run_summary.json
c365c50423e206ff7348b51eea6f486ffaf44b45911fc747a14f3fc3b2443ae1  run_summary_repeat.json
430c2c7f62f15c5787fe56e11ff59d18c4232d0380e78757f1205a6217e8b7d7  independent_crosscheck.py
4343f140610c382ec2d9863b0d0f081a61e76fa37a32dd73d53fc1a69473c50b  python_crosscheck.json
e42146d3283f4d6e6324730bd41af559929fec7e07713109563f7c2e462c258e  run_summary_sanitized.json
```

The FNV-1a stream digests embedded in the summaries are deterministic change
detectors for ordered pair/polynomial streams, not cryptographic
certificates.  The SHA-256 hashes above bind the retained files.
