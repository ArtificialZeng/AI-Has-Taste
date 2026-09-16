# Fresh mathematical referee report

## Frozen scope and verdict

I reviewed the exact `resolution-paper` claim frozen by snapshot
`5398efaaff7c64542c29a1f6b010817f666fe048b90d1402d4c0280432ba0cf0`.
The claim answers the original question for every unlabeled simple tree on
exactly 21 vertices and strengthens the requested closed-left-half-plane
conclusion to open-left-half-plane stability. I find the scope, exact
computation, and contribution adequate. **Verdict: accept.**

## Snapshot and source checks

I recomputed the SHA-256 digest of every frozen file. All hashes agree with
`audit/snapshot.json`, including the source PDF digest
`fb1940a98c1cc1ec1e5ba479871431244090771b2b6ce3fa7c72dc888c6c4d82`.
The attached Zhang--Tu arXiv v1 paper defines stability using the closed left
half-plane, reports Brown--Cameron's computation only through order 20, and
states in Theorem 4 that every spider has all independence roots in the open
left half-plane. Thus the candidate neither changes the definition nor
mistakes the spider theorem for an order-21 census. The bounded literature
record supports the stated boundary comparison, while correctly avoiding an
unqualified priority claim.

## Reconstruction of the decisive argument

The level sequence processed by `adjacency_and_parent` makes every vertex
after the root adjacent to its nearest preceding vertex one level above.
Consequently each processed object is a connected 21-vertex graph with 20
edges and is a tree. The WROM/Beyer--Hedetniemi successor implemented in
`census21.py` is the standard once-per-free-tree stream. The committed run
terminates after 2,144,505 objects. Independently of the stream order, the
center-rooted AHU balanced-parenthesis encoding is injective on unrooted tree
isomorphism classes: rooted encodings are uniquely parsed recursively after
sorting child encodings, and a virtual root canonically handles the two-center
case. All encodings fit in 44 bits. Sorting the 2,144,505 stored `uint64`
values finds no duplicate. The count also agrees with the external A000055
cross-check; that agreement is corroborative rather than the sole enumeration
argument.

For a rooted tree, let `A_v` and `B_v` count independent sets in the descendant
subtree conditional on excluding and including `v`. Disjoint child subtrees
give

```
A_v = product_w (A_w+B_w),    B_v = z product_w A_w.
```

The program evaluates these identities with integer polynomial arithmetic and
returns `A_r+B_r`, so the coefficient vectors are exact. There is no division,
floating-point root calculation, probabilistic step, or limiting argument in
this part.

For coefficients in descending order, successive ordinary Routh rows satisfy

```
new_j = (p*upper_{j+1} - upper_0*lower_{j+1})/p,
```

where `p=lower_0`. The implementation stores
`sign(p)*(p*upper_{j+1}-upper_0*lower_{j+1})` and then divides by a positive
row gcd. This is `|p|` times the ordinary new row before the harmless positive
gcd rescaling, so every stored first-column sign is exactly the corresponding
rational Routh sign. A zero pivot or all-zero row is reported before it could
be hidden by normalization. Across the complete stream, all tables are
regular and every first-column entry is positive. Hence there are no roots in
the open right half-plane; regularity also excludes an imaginary-axis root
pair (and the constant coefficient is 1, excluding a root at zero). Therefore
all roots have strictly negative real part.

## Checks actually performed

- I ran the complete census afresh in a new temporary directory. It again
  produced 2,144,505 strictly stable cases, zero regular-unstable cases, and
  zero singular cases. All 43 chunk commitments matched in their indices,
  counts, terminal layouts, record hashes, and classifications. The fresh
  `canonical.u64` was byte-for-byte identical to the frozen 17,156,040-byte
  file and had SHA-256
  `58eee5478a09908475cda2f39d43a0ca0f209b12cb91f288b7488c90b7e5bb80`.
- I reran `independent_checks.py`. NetworkX independently completed the same
  2,144,505-object count. On the predeclared 430 cases, all canonical codes
  matched, the vertex-deletion recurrence matched the rooted tree DP, and all
  leading Hurwitz determinants computed by fraction-free Bareiss elimination
  were positive. Its certificate digest reproduced as
  `bef07cd7458f796972933017ef3baaa7d104eb64d0cfa1187192166842df5407`.
- As a separate small-order enumeration attack, I generated every labeled tree
  from all Prüfer sequences for orders 2 through 7, reduced them by an
  independently written string-valued center/AHU encoding, and obtained the
  same isomorphism-class sets as the level-sequence stream (counts
  1, 1, 2, 3, 6, 11).
- For all 986 streamed tree classes through order 12, I brute-forced every
  vertex subset and matched the resulting independence polynomial to the tree
  DP. I also compared Routh positivity to exact leading Hurwitz determinants.
  Adversarial polynomials correctly produced a regular one-variation case for
  a right-half-plane root, a zero pivot for an imaginary pair, and an all-zero
  row for another imaginary-axis case.

## Contribution and limits

The result is a nontrivial full finite resolution rather than a toy
restriction: it exhausts more than two million isomorphism classes and moves
the cited computational boundary from 20 to 21. Its claim is appropriately
limited to exactly 21 vertices and does not assert a general characterization.
The proof remains computer-assisted and depends on the stated generator
theorem, Python integer arithmetic, and reproducible local execution; these
dependencies should be cited and disclosed precisely in the manuscript. The
literature search is bounded, so no absolute novelty or priority statement is
warranted. These are disclosure requirements, not unresolved mathematical
gaps in the frozen claim.
