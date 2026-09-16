# Research pass 2: complete positive census

Job: `win-00045-p08-research-734b9cd9143a`

## Exact result

Let `CE[1],...,CE[254]` be the adjacency matrices in the supplied official
`n9_margin1only_tournaments.rds`, the file described by the primary repository
as the 254 nine-vertex tournaments that are 3-inducible but not margin-1
3-inducible. For every `CE[k]`, the transparent certificate in
`research_pass2_results.json` gives five permutations of vertices `0,...,8`.
On every arc of `CE[k]`, exactly three of those permutations place the tail
before the head. Hence every `CE[k]` lies in \(I_{5,1}\).

The repository commit introducing the file is
`f23f6388c5820e6ad7bfd8fbf1bad2b4d6d0eb3b`; the current repository data page
and the commit description both identify the file with the target 254-class
boundary. These primary URLs were checked on 2026-09-06:

- https://github.com/Leonardini/Tournaments/commit/f23f6388c5820e6ad7bfd8fbf1bad2b4d6d0eb3b
- https://github.com/Leonardini/Tournaments/tree/main/data

The supplied binary was snapshotted losslessly as base64. Decoding it gives
5,670 bytes with SHA-256
`f633b784eb573ab142f0f7e4c1bb9e9e97d7a0953405c28a7f0aa0a95d0115a6` and
Git-blob SHA-1 `143524d23cc0cfcf05b8ee5f87e10064a647c591`.

## Why the certificates prove the claim

For each upper-triangle pair `(i,j)`, bit `1` means the arc `i -> j` and bit
`0` means `j -> i`. Every listed order is explicitly a permutation. The
standalone verifier constructs inverse positions and counts the five comparisons
for all 36 pairs. Its successful total of `254*36 = 9,144` target arcs, all with
support exactly 3, is precisely the definition of \(I_{5,1}\). Membership is
invariant under relabelling, so one certificate per isomorphism class proves the
universal finite assertion. The same verifier confirms by exact directed-graph
isomorphism that no two of the 254 serialized representatives are isomorphic.

The Z3 encoding used to discover profiles is not in the proof's trust path:
the emitted permutations can be checked directly. There were no UNSAT or
unknown instances. Consequently no unsupported solver-negative conclusion and
no DRAT/LRAT obligation arises.

## Reproduction

```sh
python3 evidence/research_pass2.py \
  evidence/n9_margin1only_tournaments.rds.base64 --timeout-ms 120000
python3 evidence/research_pass2_verify.py
```

The recorded run used Z3 4.15.3 and took 20.71 seconds for parsing, solving,
recounting, and JSON output. The independent verifier reports 254 records, 1,270
permutations, 9,144 arc recounts, 5,284 degree-compatible isomorphism candidate
pairs checked, and status `PASS`. Timing is operational metadata, not evidence.

## Limitation

This proves only the frozen 254-class assertion. It neither supplies a witness
to \(I_{5,1}\subsetneq I_{5,3}\) nor resolves either global inclusion in
Conjecture 8.1. Identification of the list as the reported boundary family is
source/data provenance; the pass does not independently redo the much larger
paper census that originally selected these 254 classes.
