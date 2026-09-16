# Exact eight-vertex computation: method and certificate

## Claim checked

For every connected simple graph `G` on eight vertices and every
`d = 1,...,7`, the computation checks every coefficient in the Schur
expansion of

`L_(G,d) = F_(G,d)^2 - F_(G,d-1) F_(G,d+1)`, where
`F_(G,d) = Psi_G|degree d`.

All arithmetic in `evidence/eight_vertex_scan.py` is integer arithmetic. No
floating-point value is used in graph enumeration, symmetric-function
arithmetic, basis conversion, or sign testing.

## Why the graph enumeration is exhaustive

NetworkX's graph atlas supplies one representative of each isomorphism class
of graphs on seven vertices. For every such representative `H`, the script
adds a new vertex with each of the 127 nonempty possible neighborhoods, then
discards disconnected extensions. Conversely, if `G` is a connected graph on
eight vertices and `v` is any vertex, an isomorphism from `G-v` to its atlas
representative transports `N_G(v)` to one of those 127 neighborhoods. Hence an
extension isomorphic to `G` occurs in the generated family.

Deduplication first groups extensions by three isomorphism invariants (degree
multiset, triangle-count multiset, and a Weisfeiler--Lehman hash). Isomorphic
graphs necessarily enter the same bucket. Every candidate is then compared
with retained bucket members by NetworkX's exact `is_isomorphic` test. Thus the
invariants are only a speed filter: a hash collision cannot merge classes.
The run tests 119,980 connected extensions and retains 11,117 classes.

## Exact symmetric-function recurrence

For a vertex subset `S`, let `A[S,k]` be the sum, over all partitions of `S`
into `k` nonempty blocks inducing connected subgraphs, of the product of the
Möbius symmetric functions of those induced subgraphs. For `k >= 2`, anchoring
at the least vertex gives

`A[S,k] = sum_B M_(G|B) A[S-B,k-1]`,

where `B` runs over proper connected subsets of `S` containing its least
vertex. Every connected-block partition has exactly one such block, so this
counts each partition exactly once. Subsets are processed in increasing size.
Formula (5.3) of the source then gives, for connected `S` of size at least two,

`M_(G|S) = - sum_(k=2)^|S| h_(k-1) A[S,k]`,

with `M` of a singleton equal to 1. Finally, source Theorem 7.2 gives
`F_(G,d) = A[V,8-d]`. The earlier definition-level `P3` computation is a
regression check for this recurrence and produces the corrected exact value
`L_(P3,1) = 3 s_(2) + 2 s_(1,1)`.

Functions are stored in the complete-homogeneous basis, where
`h_mu h_nu = h_(sort(mu union nu))`. The identity
`h_mu = sum_lambda K_(lambda,mu) s_lambda` is evaluated by successive exact
applications of the horizontal-strip Pieri rule. This converts every `L_(G,d)`
to its complete Schur coefficient vector over the integers.

## Results and replay

There are `p(2)+p(4)+...+p(14) = 294` tested coefficients per class. The run
therefore tests `11,117 * 294 = 3,268,398` exact coefficients. All are positive;
the global minimum is 1. The strata are:

| stratum | classes | coefficients | minima for d=1,...,7 |
|---|---:|---:|---|
| chordal | 1,614 | 474,516 | 7, 158, 490, 490, 196, 28, 1 |
| nonchordal | 9,503 | 2,793,882 | 18, 288, 1176, 1695, 946, 186, 9 |

Degrees `d >= 8` are automatic: all involved homogeneous pieces outside
degrees 0 through 7 vanish, so `L_(G,d)=0`.

Replay command (from the project root):

```text
python3 evidence/eight_vertex_scan.py \
  --records /tmp/eight_vertex_records.replay.jsonl \
  --summary /tmp/eight_vertex_summary.replay.json --progress-every 0
```

Two complete runs under Python 3.10.12 and NetworkX 3.4.2 produced
byte-identical 12,577,195-byte JSONL files with SHA-256
`08142d763b01d1c160a94bdc2caf30d9755c594f5ffa798bd281f86a5d89db65`.
The graph6 representative-list SHA-256 is
`2b12580a607c4282ced83c6f31c81706e1f5dc5efcc105de31fa7af9ddf2d39a`.
The frozen `source.md` SHA-256 remained
`7a813547d00963509314db388cd5de0b75036d1ebfbaead6196b224434ca7dea`.

