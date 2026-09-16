# Fresh mathematical referee report

## Frozen scope

I reviewed the statement frozen by snapshot
`b0f32e249b19267de1624e539fad21470aa6a3e177fa0a41e8ac8a0341bc6763`.
The candidate is exactly the precise frozen target in `source.md`: the minimum
is taken only among integral circulants that are uniquely 3-colorable and have
clique number 2.  It does **not** claim the unrestricted minimum over uniquely
`k`-colorable integral circulants with arbitrary `k>omega`.  The scope caveat
in `problem.md` and the final sentence of the contribution make that boundary
explicit, so the candidate does not silently answer the broader opening lead.

All hashes in `audit/snapshot.json` were recomputed before review and matched
the current files.  In particular, the supplied source PDF has SHA-256
`eec197e27fcab9602c1cd8b033dd84a45d4401abcbdbe225db3de9d6afb9acf2`.

## Reconstructed argument

For each `n`, the proper divisors are enumerated in increasing order and every
bit mask represents one subset `D`.  This gives exactly
`sum_{n=1}^{60} 2^(tau(n)-1)=4091` pairs, of which 2,043 have `n<60`.
There is no quotient or omitted symmetry.  Moreover distinct sets at fixed
`n` give distinct labeled graphs: if `d` is in the symmetric difference, then
`gcd(d,n)=d`, so the edge `{0,d}` distinguishes the two graphs.

For each pair the adjacency relation is constructed directly from
`gcd(v-u,n) in D`.  The exclusion tree is mathematically sufficient:

1. An edgeless graph has chromatic number at most 1.
2. A disconnected graph cannot be uniquely 3-colorable.  If its chromatic
   number is not 3, it already fails.  If it is 3, one component uses all
   three colors; applying a nonidentity color permutation only on another
   nonempty component gives a different unordered global partition.
3. A triangle implies `omega>=3`.
4. A bipartition implies `chi<=2`.
5. Any remaining graph is connected, has an edge, is triangle-free, and is
   nonbipartite.  Hence `omega=2` and `chi>=3`.  Exhaustive 3-color search then
   distinguishes no coloring (`chi>3`), at least two unordered partitions
   (not unique), and exactly one partition (qualifying).

The primary backtracker is exhaustive modulo color names: its vertex choice
depends on saturation cardinality, degree, and label but not on the names of
the used colors, and colors are introduced canonically.  The second verifier
uses the exact-one-color and edge CNF.  Fixing vertex 0 to color 0 loses no
unordered partition.  On the nonbipartite survivors every proper 3-coloring
uses all three colors, and precisely two labeled models with `c(0)=0` realize
one unordered partition; blocking the found model and its `1<->2` swap is
therefore an exact uniqueness test.  Inspection of the DPLL routine found no
unsound pruning: unit propagation preserves satisfiability and the two-way
branching exhausts every remaining Boolean assignment.

The only qualifying record is

`n=60, D={2,5}`.

It has 360 edges, no triangle, and the certified odd cycle
`4,2,0,14,9,4`.  Its sole unordered 3-color partition is

`{x:x=0 mod 3}, {x:x=1 mod 3}, {x:x=2 mod 3}`.

Each class is visibly independent: a nonzero difference within a residue
class is divisible by 3, so its gcd with 60 is neither 2 nor 5.  Exact
exhaustion proves uniqueness.  No pair below order 60 qualifies, and the
other 2,047 divisor sets at order 60 also fail, establishing both minimality
and the claimed complete classification.

## Checks performed

- Recomputed every frozen snapshot hash; all matched.
- Re-ran `enumerate_icg.py` into referee-owned files.  Its JSONL and summary
  were byte-identical to the frozen files, with SHA-256 values
  `2e07ea9bb95406bbe504b7bad544db66f060e3989a5899bb16a56872408a524c`
  and `79c1c3888ae3d7733070abe617f146c8958f00c4797f2f4b54016c172a5dd0dd`.
- Re-ran `verify_census_sat.py`.  It checked all 4,091 records, found no
  classification mismatch or primary-witness error, and reproduced the
  frozen independent JSONL and audit byte for byte.
- Wrote and ran a fresh third checker using set adjacency, direct graph
  predicates, and labeled DSATUR backtracking with only `c(0)=0` fixed.  It
  independently obtained the same aggregate counts and no disagreement with
  any of the 4,091 frozen classifications.  Its report is
  `audit/referee-replay/fresh-check.json`.
- Directly checked the qualifying record's partition and odd cycle from the
  serialized primary certificate.

The common census is:

| Result | Count |
|---|---:|
| edgeless | 60 |
| disconnected | 677 |
| triangle | 3,228 |
| bipartite | 91 |
| not 3-colorable | 17 |
| nonunique 3-colorable | 17 |
| qualifies | 1 |

The explanatory sentence in `evidence/computational-proof.md` saying that
"if no component has chromatic number 3 then the whole graph is at most
2-colorable" omits the possible `chi>3` case.  The displayed disconnected
exclusion remains correct by the complete argument above; this is a minor
expository correction, not a change to the algorithm, statement, or scope.

## Source comparison and contribution

I inspected the supplied arXiv source itself.  Its Theorem 3.1 states that
`ICG_{12p}({2,p})` is uniquely 3-colorable with clique number 2 for primes
`p>=5`, so `p=5` supplies the already known order-60 example and the residue
classes modulo 3.  The inspected paper does not assert least-order status or
classify all divisor sets through order 60.  Thus the candidate's precise
delta is the exact finite minimum and classification, not a reproof of that
family.  The candidate makes no priority claim beyond this bounded comparison;
a broader novelty search belongs to later citation review and is not being
converted here into mathematical evidence.

## Verdict

**Accept.**  The frozen statement is settled in its full stated scope.  The
enumeration is exhaustive, all predicates are exact, the uniqueness test
matches the definition, and three checked implementations agree on every
case.  No unresolved mathematical gap remains in the candidate claim.
