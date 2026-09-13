# Exact baseline reproduction

Date: 2026-08-30 (Asia/Shanghai)

Alphabet: \(A=\{0,1,2,4\}\).

The discovery implementation `src/exact_prefix_dfs.cpp` exhausts every ASF
prefix using exact signed integer prefix sums.  The independent implementation
`certificates/independent_tail_dfs.cpp` rebuilds cumulative sums from the right
end of each current word and is compiled and run by the fail-closed certificate
coordinator.  Neither implementation uses randomness.

Locally reproduced result:

| quantity | exact value |
|---|---:|
| prefix-tree nodes (empty root included) | 19,097,778 |
| terminal leaves | 5,350,440 |
| maximum length | 62 |
| maximizers | 2 |
| reversal orbits | 1 |

These values and both extremal words agree with TheoremDB R28/R19/R18.  The
local discovery run took 1.36 seconds on Apple arm64; runtime is provenance,
not part of the certificate.

Reproduce discovery:

```sh
clang++ -O3 -std=c++20 -Wall -Wextra -pedantic \
  src/exact_prefix_dfs.cpp -o experiments/exact_prefix_dfs
./experiments/exact_prefix_dfs 0 1 2 4 --node-limit 30000000
```

Independent exact verification:

```sh
python3 certificates/verify_finite_census.py \
  certificates/baseline_0124.json
```

Expected terminal record:

```text
{"certificate_sha256": "4111e2281fe2f97178bf05031e870c40cba78cc3454848f14c29bd0b57c209f8", "records": 1, "status": "VERIFIED", "verifier_cpp_sha256": "dc8c5e25393fd58456ab72178b79cd636ec6f4006ccdfd80a4b363e1c766ef19"}
```

Fail-closed tests:

```text
FAIL_CLOSED_TESTS_OK cases=6 rejected_corruptions=5
```

The five rejected mutations remove a required field, replace an integer by a
float, add an unexpected trusted-answer field, break primitive normalization,
or make the witness count inconsistent.
