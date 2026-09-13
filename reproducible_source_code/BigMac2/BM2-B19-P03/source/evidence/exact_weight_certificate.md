# Exact weighted-cycle UNSAT certificate

## Frozen scope

This note concerns only the labelled 812-vertex cubic graph `B` specified in
`source.md`.  The immutable source has SHA-256
`29441258d1fb9526154bab4ea6f8c973728e4ab25b86dc18932baa2b03e5e596`.
The deposited ZIP and its `agl_29_g14.g6` member have SHA-256 digests
`5dd250b705e4ed8e9fe6be625285adffea0d98d9f18b3640071ed4a6e4290fe4`
and `8b074cd755a5d1e1e6a1d09a7888173821372e6cdcd501cfd2baf1a34bfeb08e`,
respectively.  No claim is made about another labelling, another Cayley base,
or the full Erdős--Gyárfás problem.

## Weighted-cycle lemma

For a cycle `C` of length `L`, let `o_u(C)` be the number of its vertices
whose selected incident edge leaves `C`.  Since each cycle vertex selects one
incident edge,

```
o_u(C) = L - a_u(C).
```

Consequently the constraint in the frozen problem implies

```
o_u(C) >= 33 - 2L.                                      (1)
```

Give finitely many target cycles nonnegative integer weights `w_C`.  For a
vertex `v` and neighbour `z`, define

```
lambda(v,z) = sum of w_C over weighted cycles C for which vz is the
              unique edge at v leaving C.
```

The graph is cubic and every listed cycle is checked to have a unique such
edge.  If an orientation selects neighbour `u(v)` at `v`, summing (1) with
weights gives

```
sum_C w_C (33 - 2|C|)
    <= sum_C w_C o_u(C)
     = sum_v lambda(v,u(v))
    <= sum_v max_{z in N(v)} lambda(v,z).                (2)
```

Thus a strict reversal of the two outer quantities in (2) is an exact UNSAT
certificate.

## The certificate and exact totals

`exact_cycle_weights.tsv` lists each positive weight together with the
canonical labelled cycle carrying it.  It has SHA-256
`26efbe5af6046024de46f3513c8d7c5ef35b4035f2cd7a092aa6818e00a9cc4d`.
Its support consists of 1,172 length-14 cycles and 12 length-16 cycles.  The
weight sums are

```
length 14: 3,243,141
length 15:         0
length 16:       999
```

The left side of (2) is therefore

```
5 * 3,243,141 + 3 * 0 + 1 * 999 = 16,216,704.           (3)
```

The graph-based checker validates every one of the 1,184 serialized cycles
directly against the frozen graph6 member, then accumulates all 2,436 integer
values `lambda(v,z)`.  It obtains

```
sum_v max_z lambda(v,z) = 15,153,552,                   (4)
```

so (3) exceeds (4) by `1,063,152`.  As a coarser transparent check, every
per-vertex maximum lies between 18,488 and 19,015.  Hence any orientation
contributes at most

```
812 * 19,015 = 15,440,180 < 16,216,704,
```

already leaving a gap of `776,524`.  Equations (2)--(4) contradict the
existence of the requested map `u`.

## Reproduction and separation from floating-point discovery

Run from the project directory:

```sh
python3 evidence/check_exact_weight_certificate.py \
  ../../batches/literature/bigMac-19/supplement.zip \
  agl_29_g14.g6 evidence/exact_cycle_weights.tsv source.md \
  evidence/exact_weight_check.json

python3 evidence/replay_exact_weight_certificate.py \
  evidence/exact_cycle_weights.tsv evidence/cycles_14_16.tsv \
  evidence/orientation_search_instance.tsv \
  evidence/exact_weight_replay.json
```

The first checker independently decodes the fixed graph, checks its order,
size, cubicity and girth, validates every weighted cycle and recomputes (3)--
(4) using Python integers.  The second implementation instead checks the
certificate rows against the canonical census and the separately emitted
direct CSP incidence rows.  Both reports record the same exact lower bound,
upper bound and gap.

The weights were discovered by nearest-integer rounding of the nonnegative
cycle part of a HiGHS floating-point dual ray.  Neither that ray nor the solver
status is used as proof: only the serialized nonnegative integers, the fixed
graph, the elementary lemma above, and the exact replays are decisive.

## Scope and remaining audit

The argument disproves the complete frozen decision statement, since a
contradiction from a subset of its length-14 and length-16 constraints also
contradicts the full family (there are no length-15 cycles in the canonical
census).  It excludes only this fixed `AGL(1,29)` base.  A fresh mathematical
referee still must audit the frozen statement, lemma, cycle validation and
integer totals; this research note is a candidate handoff, not acceptance.
