# Exact computational proof that the maximum is 2

## Claim

For the frozen domain in `source.md` and the encoding in `problem.md`,

\[
\max_{P\in\mathcal W^6} d(P)=2.
\]

All comparisons below use integers. Being unmatched has rank 3; acceptable
partners have normalized ranks 0, 1, or 2. For a candidate set, componentwise
minimum rank is exactly the rank of each agent's best partner in that set.
For each alternative, the programs add `+1`, `0`, or `-1` according as that
best rank is better, tied, or worse. A candidate is accepted only if all 34
integer margins are nonnegative.

## Primary exhaustive census

`orbit_pair_census.py` generates the 13 normalized rank triples, all 34 partial
matchings by cardinality/subsets/bijections, and all 72 graph automorphisms.
The automorphisms comprise independent permutations of the two sides, with or
without exchanging the sides. A profile is encoded in base 13 in the stated
agent order. Scanning codes upward, the program marks all images of each first
unmarked profile and tests that representative. Thus it covers each orbit once.

As a check independent of orbit marking, for each group element the fixed-profile
count is computed from cycles of its induced permutation of the six agent/order
variables. Burnside's sum is 4,882,680, giving 67,815 orbits. Orbit marking also
gives 67,815 orbits and covers exactly 4,826,809 labelled profiles.

For each representative the program first tests all 34 singletons. If necessary
it tests all 561 unordered pairs of distinct matchings. Each test checks every
one of the 34 alternatives. Candidate best-rank vectors are cached, without
changing the predicate. The census is:

| dimension | profile orbits | labelled profiles |
|---|---:|---:|
| 1 | 67,797 | 4,826,131 |
| 2 | 18 | 678 |
| 3 | 0 | 0 |

The complete Burnside table and terminal assertions are in
`orbit_pair_census_output.txt`. The run used Python 3.10.12, NumPy 2.2.6, and
Numba 0.67.0; `/usr/bin/time` records 2.04 seconds elapsed and exit status 0.

## Independent unreduced verification

`verify_unreduced.py` does not import the primary census, use its symmetry
action, perform orbit marking, use Burnside's lemma, or cache popularity vectors.
It independently generates the 34 matchings as injective partial functions from
men to women and directly enumerates every base-13 code from 0 through
`13^6-1`. For each labelled profile it tests singletons and, only where needed,
all unordered pairs against all alternatives. Parallel Numba compilation changes
execution speed only; all stored ranks and margins are exact integers.

This unreduced pass independently returns the same labelled counts
`d1=4,826,131`, `d2=678`, `d3=0` and asserts that every profile has a singleton
or pair. Its recorded run used four threads, took 2.80 seconds elapsed, and
exited with status 0. This proves the universal upper bound 2 computationally.

## Exact lower-bound witness

In agent order `(m0,m1,m2,w0,w1,w2)`, take

```
((0,0,0), (0,1,2), (0,2,1), (0,2,1), (1,2,0), (1,0,0)).
```

`verify_dimension_two_witness.py` is a pure-standard-library Python verifier.
It prints a strictly defeating alternative for every one of the 34 singleton
matchings. It also checks that

```
{m2-w0},  {m0-w0,m1-w1,m2-w2}
```

is popular winning: its 34 margins, in the verifier's matching order, are

```
6,4,3,5,4,4,5,5,4,5,2,1,3,3,2,3,2,2,3,4,2,3,2,3,3,4,3,3,1,1,0,1,1,2.
```

Hence this profile has dimension exactly 2, proving the lower bound. Combined
with the exhaustive upper bound, the frozen maximum is exactly 2.

## Deterministic file hashes (SHA-256)

```
7af58aa0adb2e2a18fc1777b65fd9180e10372abf56b374f314d31358e22ede0  orbit_pair_census.py
564ffc26b7f4d2ab5f082fe9644447177f526172613db50bf630fefaacb6b683  orbit_pair_census_output.txt
e4c37b40b7c24f78dff0f8cc512a83116d439a5be6f052b8a829274ff942c5b9  verify_unreduced.py
440f47ba320916cdd21acc96d7286e65a90cfb76e698f77d930b617f7e33b76a  verify_unreduced_output.txt
7aa2336bb18b6e8a9ac4fd6a880e650e185edb9f7c8d45335a4bb9d25d4f8d03  verify_dimension_two_witness.py
ba5b2e7f10a78d6656d69dbee82c04e8f7616679e4595adc4414bfdd0b492311  verify_dimension_two_witness_output.txt
1707cb5423c732793ebc688f84b5663dee15ad7ae330ccb6b10cdd210a76bfd2  external/2509.25150v3.pdf
```
