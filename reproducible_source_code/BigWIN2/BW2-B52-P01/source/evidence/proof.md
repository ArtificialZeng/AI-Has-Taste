# Exact determination of `eta(K_{1,1,5})`

## Claim

For induced embeddings into finite Abelian Cayley graphs,
\[
\eta(K_{1,1,5})=15.
\]

## Lower floor and finite domain

Let the singleton parts be `a,b` and let the five-vertex part be `C`.
The set `C` is an independent set of size five in the open neighborhood of
`a`.  Theorem 6 of `evidence/external/2609.01486.pdf` therefore gives
`eta >= max(7,2*5)=10`.

The finite Abelian group types of orders 10 through 14 are exactly

- order 10: `Z10`;
- order 11: `Z11`;
- order 12: `Z12` and `Z2 x Z6`;
- order 13: `Z13`;
- order 14: `Z14`.

This follows directly from the primary decomposition/classification of finite
Abelian groups: only order 12 has two types in this range, according as its
Sylow 2-subgroup is cyclic or elementary Abelian.

## Exhaustive exclusion of orders 10--14

For any embedding, translate all labels so that `f(a)=0`.  Translation
preserves every difference.  The label `b=f(b)` then ranges over all `n-1`
nonzero elements.  Since permutations of the five vertices in `C` do not
change the labeled image condition, their labels range over every unordered
five-subset of `Gamma \\ {0,b}`.  Hence the number of cases for a group of
order `n` is exactly
\[
(n-1){n-2\choose5}.
\]

For each case, `evidence/enumerate_embeddings.py` forms both orientations of
all 11 edge differences (the pair `ab`, the five pairs `aC`, and the five
pairs `bC`) and all 10 nonedge differences (the pairs internal to `C`).  A
symmetric connection set exists if and only if these two difference sets are
disjoint: necessity is the induced condition, and for sufficiency take the
connection set to be the oriented edge-difference set itself.

The exact-integer search in `evidence/enumeration-log.json` reports:

| group | cases required | cases tested | valid |
|---|---:|---:|---:|
| `Z10` | 504 | 504 | 0 |
| `Z11` | 1,260 | 1,260 | 0 |
| `Z12` | 2,772 | 2,772 | 0 |
| `Z2 x Z6` | 2,772 | 2,772 | 0 |
| `Z13` | 5,544 | 5,544 | 0 |
| `Z14` | 10,296 | 10,296 | 0 |

Thus all 23,148 normalized cases in every relevant group type were tested,
with no valid labeling.  Consequently `eta >= 15`.

## Exact order-15 certificate

In `Z15`, label
\[
f(a)=1,\quad f(b)=2,\quad f(C)=\{0,3,6,9,12\},
\]
and take
\[
S=\{1,2,4,5,7,8,10,11,13,14\},
\]
the residues not divisible by three.  The serialized certificate is
`evidence/order15-witness.json`.  The separate program
`evidence/verify_order15_witness.py` imports no search code and directly checks
injectivity, `0 not in S`, symmetry of `S`, and all 21 unordered vertex pairs.
Its complete pair log, `evidence/order15-verification.json`, passes every check.
This proves `eta <= 15` and completes the equality.

## Reproduction

From the project root:

```sh
python3 evidence/enumerate_embeddings.py --output /tmp/enumeration-log.json
cmp /tmp/enumeration-log.json evidence/enumeration-log.json
python3 evidence/verify_order15_witness.py \
  --witness evidence/order15-witness.json \
  --output /tmp/order15-verification.json
cmp /tmp/order15-verification.json evidence/order15-verification.json
```

Both computations are finite and exact; neither uses floating-point arithmetic,
randomness, solver heuristics, or timeouts.
