# Frozen source problem: all-parameter two-point-complement boundary for multi-tournament Schütte property

Canonical id: `win-00087-p01`

Frozen on: 2026-09-11 (Asia/Shanghai)

Primary source: Joel Jeffries, *Schütte's property for sets of tournaments and an application to dice games*, arXiv:2604.08790v1, Definitions 2.1--2.2 on PDF p.4, Proposition 2.3 on p.5, Theorem 2.2 on p.6, Figure 7 on p.8, and the discussion on p.10.

## Definitions and statement

A tournament is a loopless orientation of a complete graph; directed cycles are allowed. For integers `m,k>=1`, let `f(m,k)` be the least `n>=k+1` for which there are `m` tournaments `T_1,...,T_m` on a common `n`-element vertex set `V` such that

```text
for every k-set U subset V, there are i in [m] and v in V\U
such that v -> u in T_i for every u in U.
```

The same outside vertex in the same tournament must dominate all of `U`.

Prove or disprove the exact all-parameter claim

```text
f(k-1,k) = k+3 for every integer k>=3.
```

The exception `k=2` is out of scope; the source gives `f(1,2)=7`.

## Required contribution boundary

The source already supplies the relevant gluing upper-bound mechanism and small SAT values. A complete result must establish the lower bound uniformly and must independently validate the upper-bound construction. In particular, prove or refute the proposed structural lemma: for a tournament `T` on `n>=3` vertices, form the graph `H_T` whose edges are the two-point complements of `(n-2)`-sets dominated by one outside vertex in `T`; then `H_T` is contained in a star or is exactly a triangle.

The proposed lower-bound route deletes distinct star centers and then asks too few triangles to cover the remaining complete graph. Every inequality and the cases `n=k+1` and `n=k+2` must be checked explicitly. A finite enumeration does not prove the all-parameter statement.

## Status and novelty limits

The source states that general lower bounds are lacking but does not number or explicitly pose this slice. Treat it as a new question with uncertain publication priority until later versions and the tournament-covering literature have been checked. Do not describe the result as closing a source-listed open problem unless that claim is independently established.

## Evidence to replay

- `batches/inbox/bigWin-87.raw.md`
- `batches/inbox/bigWin-87.capture.json`
- `batches/normalized/bigWin-87.md`
- `batches/inbox/bigWin-87-materials/01_schutte/proof.md`
- `batches/inbox/bigWin-87-materials/01_schutte/verify.py`

The supplied checker enumerates small tournaments and tests the proposed construction. Referee must audit the symbolic proof separately.

Any manuscript must cite the primary source, every standard covering or tournament result actually used, and the closest prior art, in addition to one or two genuinely relevant user-library papers when available. That user-library minimum never limits the rest of the bibliography.

This file is immutable. Weakening the quantifiers or silently excluding tournaments with sources or cycles is a different problem.
