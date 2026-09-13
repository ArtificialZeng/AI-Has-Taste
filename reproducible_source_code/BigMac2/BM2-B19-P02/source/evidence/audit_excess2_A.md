# Independent audit record for the `(5,3^23)` exclusion

Research pass 2, job
`bigMac-00019-p02-research-5aca5a76ac53`, 2026-09-08.  This record concerns
only the degree sequence `(5,3^23)`; it is not evidence for all graphs of
minimum degree at least three.  No SAT/DRAT certificate for the frozen
original assertion was produced.

## Exact reduction

Suppose that a simple graph `G` has degree sequence `(5,3^23)` and no
4-cycle, and let `v` be its unique degree-5 vertex.  Write `N(v)` for its five
neighbours.

1. `G[N(v)]` has maximum degree at most one: two edges from one member of
   `N(v)` to two other members, together with `v`, would form a 4-cycle.
   Hence `G[N(v)]` is a matching of size `m` in `{0,1,2}`.
2. No vertex outside `{v} union N(v)` meets two vertices of `N(v)`, since
   those two incidences and their edges to `v` would form a 4-cycle.
3. Delete `{v} union N(v)`.  The residual graph `H` has 18 vertices.  An
   endpoint of the matching in `N(v)` has one neighbour in `H`; an unmatched
   member has two.  These `10-2m` neighbours are all distinct by step 2.
   They have degree 2 in `H`; every other vertex has degree 3.  Thus `H` has
   `22+m` edges, minimum degree 2, and maximum degree 3.  Every forbidden
   cycle already in `H` is also one in `G`.
4. Conversely, every possible `G` in this case arises by taking such an `H`
   and assigning its `10-2m` degree-2 ports to the five arms, with loads one
   at a matched endpoint and two at an unmatched endpoint.  Relabeling the
   matching gadget reduces these assignments to respectively 945, 420, and
   45 representatives.  Quotienting only by gadget automorphisms may repeat
   assignments related by an automorphism of `H`, but cannot omit one.

Therefore it is complete to generate every isomorphism class of C4-free
simple `H` with the stated degree and edge bounds, discard an `H` already
containing a C8 or C16, and test every remaining attachment for C4, C8, and
C16.

## Clean reproduction

The source SHA-256 was
`eb71db5101f32f56e6e5b8ab58b428c270f0336edf0171c9ca2b14bdb0666ee1`.
It was rebuilt with Apple clang 21.0.0 as follows:

```sh
c++ -std=c++17 -O3 -Wall -Wextra -pedantic \
  evidence/geng_excess2_search.cpp \
  -o evidence/bin/geng_excess2_search_pass2
```

The fresh executable SHA-256 was
`d48c0f9a118e975306617dc8bc5c8446e20dc95a2fa7bbcb8c64b0c824b532cf`.
With Homebrew nauty 2.9.3 `geng` (binary SHA-256
`ad2f68adf733dbed7cad543841cfa329740596ee5cd136f17a0a17f6e744f5ad`),
the three commands were:

```sh
geng -q -f -d2 -D3 18 22:22 | \
  evidence/bin/geng_excess2_search_pass2 0 \
  evidence/pass2_A_m0.log evidence/pass2_A_m0.witness
geng -q -f -d2 -D3 18 23:23 | \
  evidence/bin/geng_excess2_search_pass2 1 \
  evidence/pass2_A_m1.log evidence/pass2_A_m1.witness
geng -q -f -d2 -D3 18 24:24 | \
  evidence/bin/geng_excess2_search_pass2 2 \
  evidence/pass2_A_m2.log evidence/pass2_A_m2.witness
```

Each search returned its documented exhaustion code 20 and wrote no witness.
The new logs give:

| `m` | residual graphs | residual C8/C16 survivors | attachments | C4 rejects | C8 rejects | C16 rejects |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 294,693 | 29,143 | 27,540,135 | 15,062,760 | 12,477,375 | 0 |
| 1 | 835,745 | 13,064 | 5,486,880 | 2,331,130 | 3,155,750 | 0 |
| 2 | 1,087,732 | 1,020 | 45,900 | 12,131 | 33,769 | 0 |

In every row, the three reject columns sum exactly to the attachment count.
These figures exactly reproduce pass 1.  Log SHA-256 values are, in row
order,
`b0f767abd49b7aae9cfe5a63c2a5f6d04ed6e1eaf89185cb31b0a8107c00d275`,
`1a0096dac6beafd929f38fba42c2613205e448d73ac650f94ce818cbeb937bbb`,
and `aba9a07682a20c42973d42af68fe2b798d89e5a98b02b61d8a30b1340f04b259`.

## Independent component checks

The following checks were written separately from the search logic and run
against the clean build.

- `attachment_orbit_crosscheck.cpp` exhausts all `10!`, `8!`, and `6!`
  labeled port orders, canonicalizes them under the appropriate gadget
  automorphism group, and compares the resulting sets with the production
  enumerator.  It returned exactly `945`, `420`, and `45`, with no duplicate
  or missing representative.
- `cycle_detector_crosscheck.cpp` compares the production bit-mask DFS with
  an unpruned vertex-scanning DFS.  It returned
  `PASS compared=57234 exhaustive_n6_C4=32768
  random_seed=0x5a17c0de9b31`.  The suite includes all labeled graphs on six
  vertices for C4, rings of every order 3 through 24 for all three requested
  lengths, and 12,000 fixed-seed sparse/medium-density graphs.
- `graph6_parser_dump.cpp` was compared byte-for-byte with nauty `showg -a`
  on 21 graphs selected from three deterministic `geng` shards.  It returned
  `PASS graph6_matrices=21`; the graph6 sample stream had SHA-256
  `6072a6f76f4f4eff52e2684dd4498c7e46e1aedec4c5e276063e8ceaad869046`.

The corresponding source SHA-256 values are
`59eb897aacd2e3e5df136b2d66a721049d9cd335c92a98da15db7456b5b46009`,
`ba83047990b0872ce916470fc46bced0905e0882a1be3b24e76b6ddbbdd8e4f7`,
and `931e436382f0f8dc7bb385097a301751d4a7198708161899dfd6c1332fcbd8ff`.

## Scope and remaining audit

Subject to a fresh referee checking the reduction and the documented nauty
generation semantics, this is an exact finite exclusion: every 24-vertex
simple graph with degree sequence `(5,3^23)` contains a simple cycle of length
4, 8, or 16.  It says nothing about `(4,4,3^22)` or any higher degree excess,
so the frozen original assertion remains unresolved.  A referee should rerun
the commands from source; the logs are exhaustive-computation records, not a
DRAT proof for the original problem.
