# Exact computational reduction at total positive-gap count t=16

Date: 2026-08-29.  This calculation uses the same exact five-chain Parseval
deficit framework as the audited sparse-gap work.  It makes no use of the
separate proposed `t=15` exclusion and makes no claim beyond `t=16`.

At `t=16`, the exact total deficit is six and the Naimark bound gives chain
length at most `t-9=7`.  There are 48 nonincreasing five-part partitions of
16 with parts between zero and seven.  For each length, the first verifier
enumerates every strictly increasing cut-size sequence in `{1,...,10}` up to
coordinate reflection and computes the minimum certified rational lower bound
described in `t15_computational_notes.md`.

Exactly three gap-count patterns have lower sum below six:

```text
(5,3,3,3,2)
(4,4,3,3,2)
(4,3,3,3,3)
```

The other 45 are excluded exactly at the gap-partition layer.  This first
certificate has SHA-256
`896bf83e423176cc4756a132d6d81c0a810b3bdd0c4fab6d70adc06c4ccb01ae`;
its independent verifier has SHA-256
`3f953352a0544762a530dfab5a43c03c280bc1cbda85e42c5fb9a92c3bfdd023`.

The second certificate enumerates cut-cardinality multisets inside those
three patterns, quotienting independent coordinate reflection and
permutations among coordinates of equal length:

| gap-count pattern | cardinality multisets | survivors |
|---|---:|---:|
| `(5,3,3,3,2)` | 119,133,000 | 78 |
| `(4,4,3,3,2)` | 279,303,750 | 341 |
| `(4,3,3,3,3)` | 65,523,150 | 929 |
| total | 463,959,900 | 1,348 |

The second certificate has SHA-256
`cc09dec77ba7fa9fbada5699c4e142db702099efc810e17cf1bbd7daa0f04102`;
its independent verifier has SHA-256
`f319c81ac8a2a406852fcc7e2c23a803aaebbf6da03de89bf115ae549b9251d0`.

Both verifiers reconstruct all rational term bounds, canonical cut-size
types, totals, pruning decisions, and survivor records from serialized input.
They passed from outside the project under normal, `-O`, `-I`, and explicit
`-O -I`, and rejected wrong-schema certificates with nonzero exit.

## Reproduction

```bash
python3 experiments/t16_gap_partition_reduce.py
python3 certificate/t16_verify_gap_partition_reduction.py \
  certificate/t16_gap_partition_reduction.json

python3 experiments/t16_block_size_reduce.py
python3 certificate/t16_verify_block_size_reduction.py \
  certificate/t16_block_size_reduction.json
```

## Limitation

The 1,348 survivors retain all label-incidence choices.  No finite enumeration
of those incidence order types, no Farkas certificates for their LP branches,
and no exact equilateral witness were produced.  Consequently these results
are necessary structural reductions, not an exclusion of `t=16` and not a
solution of the unrestricted problem.  No proof assistant was used.
