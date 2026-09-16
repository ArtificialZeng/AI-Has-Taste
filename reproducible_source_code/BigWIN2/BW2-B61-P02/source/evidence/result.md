# Exact Hall-universality census through six vertices

## Result

Under the precise reading in `problem.md`, every finite simple graph `G` on at most six
vertices is Hall-universal. The census therefore has respectively
`1,1,2,4,11,34,156` positive isomorphism classes for `n=0,1,...,6`, and no negative
classes.

| n | G classes | labelled (G,H) pairs | Hall pairs | colorable pairs | source-covered G | new finite-census G |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 | 1 | 1 | 0 |
| 1 | 1 | 1 | 0 | 0 | 1 | 0 |
| 2 | 2 | 4 | 2 | 2 | 2 | 0 |
| 3 | 4 | 32 | 12 | 12 | 4 | 0 |
| 4 | 11 | 704 | 392 | 392 | 11 | 0 |
| 5 | 34 | 34,816 | 19,984 | 19,984 | 31 | 3 |
| 6 | 156 | 5,111,808 | 3,597,344 | 3,597,344 | 149 | 7 |

The aggregate equalities are only summaries. `census_exact.tsv` records and binds the
two exact status bits separately for every labelled H and every canonical G; in every
row there is no H that satisfies Hall but is uncolorable.

## Exact exhaustive certificate

For each `n`, edge-mask bit `k` represents `(u,v)` in order
`(0,1),(0,2),(1,2),(0,3),...`. The canonicalizer starts from the NetworkX graph atlas,
tries every vertex permutation, and retains the lexicographically least graph6 word.
The main enumerator considers all `2^(n choose 2)` H masks.

For fixed H, its exact independence-number table is computed from

`alpha(S) = max(alpha(S-{v}), 1 + alpha((S-{v})-N_H(v)))`.

For every nonempty connected induced `H[U]`, the enumerator checks

`|U| <= sum_c alpha(U intersect N_G(c))`.

For colorability it enumerates every map `phi:V->V`, retains exactly those with
`phi(v) in N_G(v)`, and records the conflict edge mask
`Q_phi={uv:phi(u)=phi(v)}`. Exactly those H with `E(H) intersect Q_phi` empty for some
retained map are colorable. This also supplies an exhaustive compressed assignment
certificate, including cases with no admissible map.

The independent verifier does not reuse these decisive subroutines. It enumerates all
labelled G and all vertex permutations, recovering exactly the 209 stored canonical
orbits. It obtains every independence number by brute enumeration of independent
submasks, checks Hall on all nonempty U (including disconnected U), independently
generates conflict masks, and directly tests each H against them. Every Hall and
colorability bit agrees with the main census.

The census file has SHA-256
`6effbf9b53bff8c5d0a2773be399e358b55d568ea6672a4da68a0ab617417c27`.
The row-ordered aggregate status hash is
`12221d88ef732ca8cc7dd655fdf473a3635522b4e64b14fe283cfcc120b88531`;
`census_manifest.json` gives a separate binding for every row and all decisive inputs.

## Relation to the source families

`census_classification.tsv` applies, exactly and reproducibly, Proposition 2.10,
Theorem 4.6, Proposition 4.9, Theorem 4.11, Theorem 4.16, Theorem 4.19, and the
disjoint-union observation in Remark 4.12 of the primary source. It records the reason
for every covered class. Of 209 positive classes, 199 are immediate from at least one
of those source results. The ten not covered there are

`DBk, DBw, DB{, E?NW, E?No, E?Nw, E?]o, E?]w, E?^o, E?^w`.

The order is `(n,graph6)` lexicographic. The first uncovered positive class is therefore
`DBk`, edge mask 880: the bull graph with triangle edges `23,24,34` and pendant edges
`13,04` in the zero-based certificate labels.

The source PDF copied to `evidence/external/2609.01889.pdf` has its cited SHA-256
`9920b04ae0db29b5568f063ef9d61d80d267c8e721e0b0d31e63ed87b393efc8`.
It lists Parikshit Chalise as author, not Timothy Sun as frozen in `source.md`; this
bibliographic discrepancy does not affect the matching definitions and theorem numbers.

## Reproduction

From the project root, run:

```bash
python3 evidence/generate_reps.py > evidence/representatives.tsv
python3 evidence/census_numba.py evidence/representatives.tsv evidence/census_exact.tsv
python3 evidence/classify_source_families.py evidence/census_exact.tsv evidence/census_classification.tsv
python3 evidence/make_manifest.py evidence/census_exact.tsv > evidence/census_manifest.json
python3 evidence/verify_census.py evidence/census_exact.tsv evidence/census_manifest.json evidence/representatives.tsv > evidence/verification.json
```

Python 3 with NetworkX 3.4.2, NumPy 2.2.6, and Numba 0.67.0 was used. All decisive
mathematical predicates are integer/Boolean computations.
