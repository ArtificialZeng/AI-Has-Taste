# Exact order-21 tree census and stability certificate

## Claim proved by the computation

Every independence polynomial of a tree on exactly 21 vertices is **strictly
Hurwitz stable**: every zero has negative real part. In particular, the
closed-left-half-plane proposition in `source.md` is true. The computation
enumerated 2,144,505 free (unlabeled) trees, found 2,144,505 distinct exact
canonical tree encodings, and obtained a regular exact Routh table with a
strictly positive first column for every tree. There were no singular Routh
cases and no unstable cases.

This is a computer-assisted exhaustive proof. The decisive program is
`evidence/census21.py`; its committed outputs and an integrity audit are under
`evidence/census21/`.

## Enumeration and exact canonical census

Trees are streamed as rooted level sequences by the
Wright--Richmond--Odlyzko--McKay free-tree algorithm with the
Beyer--Hedetniemi rooted-tree successor. This is the algorithm implemented by
NetworkX 3.4.2's `nonisomorphic_trees`; the decisive script contains the
transition functions explicitly rather than serializing NetworkX graph
objects. The correctness theorem of the free-tree generator supplies
exhaustiveness and once-per-isomorphism-class generation. The observed total
2,144,505 also agrees with OEIS A000055, but this numerical agreement is used
only as a cross-check, not as the proof of generator completeness.

For a separate duplicate check, every generated tree is converted to an exact
AHU-style balanced-parenthesis code. A rooted tree is encoded as an opening
bit, the recursively encoded children sorted by their exact `(order, code)`
pairs, and a closing bit. An unrooted tree is rooted at its unique center; for
a bicentered tree, a virtual root is attached to the two center-rooted halves.
Balanced-parenthesis parsing and the recursive sorting show that equal codes
are equivalent to rooted (and hence unrooted) tree isomorphism. At order 21
the code uses at most 44 bits and is stored losslessly as little-endian
`uint64` in generation order. Sorting all 2,144,505 codes found no duplicate.
The raw and sorted-code SHA-256 digests are recorded in
`evidence/census21/audit.json`.

## Exact independence polynomials

For a vertex `v`, let `A_v` and `B_v` be the independence polynomials of its
descendant subtree conditional on excluding and including `v`, respectively.
For the children `w` of `v`, the standard disjoint-subtree decomposition gives

```
A_v = product_w (A_w + B_w),       B_v = z product_w A_w,
I(T,z) = A_r + B_r.
```

The script evaluates these identities from leaves to root using only integer
addition and multiplication. Thus every computed coefficient vector is
exact. The identities also imply that every vector begins with `[1,21,190]`:
a 21-vertex tree has one empty set, 21 singletons, and
`binomial(21,2)-20=190` independent pairs; the independent audit checks these
entries on its 430 selected cases.

Each committed chunk hashes, in order and with unambiguous separators, the
canonical code, complete coefficient vector, Routh status, and signs of the
Routh first column of every tree in that chunk. The 43 chunk hashes are in
`evidence/census21/chunks.jsonl`.

## Exact Routh certificate

For each integer polynomial, `routh_first_column` constructs the ordinary
Routh array. It avoids rational storage as follows. If the current pivot is
`p`, the next-row numerator is multiplied by `sign(p)` and divided only by the
positive gcd of the resulting row. Inductively this makes every stored row a
positive scalar multiple of the corresponding rational Routh row: if two
input rows have positive scaling factors, their cross-product numerator has
the product scaling factor, and multiplication by `sign(p)` differs from
division by `p` by the positive factor `|p|`. Therefore the stored first
column has exactly the signs of the rational Routh first column. All
operations are on exact integers.

For every one of the 2,144,505 polynomials, the table was regular and every
first-column entry was strictly positive. The Routh--Hurwitz criterion then
places every zero in the open left half-plane. No zero-pivot or all-zero-row
case was discarded: either status would have been serialized in
`suspects.jsonl`; no such file was produced. The stronger strict result also
rules out the imaginary-axis boundary cases allowed by the frozen question.

## Reproducibility and adversarial checks

`evidence/audit_census21.py` verifies the completed state, contiguous chunk
indices and totals, absence of exception records, exact binary size, and
global canonical-code uniqueness. Its result is
`evidence/census21/audit.json`.

A second pass, `evidence/independent_checks.py`, used NetworkX graph objects
and regenerated the full count. On the indices 1 and 2,144,505 and every
positive multiple of 5,000 (430 predeclared cases), it:

1. matched the stored canonical code;
2. recomputed the polynomial by the graph recurrence
   `I(G)=I(G-v)+z I(G-N[v])`, with memoized vertex masks;
3. matched that vector to a separately rooted tree DP; and
4. constructed the full Hurwitz matrix and found every leading determinant
   positive by fraction-free Bareiss elimination.

This audit covered sampled independence numbers from 11 through 20, including
the path-like and star endpoints. Its exact result and selected-certificate
digest are in `evidence/census21/independent-checks.json`. The sample audit is
not substituted for the exhaustive primary computation; it is an
implementation cross-check using different polynomial and stability tests.

## Scope and literature boundary

The attached arXiv v1 source `evidence/external/2609.04694.pdf` reports the
prior computation only through order 20 and proves all spiders stable. The
present result decides exactly the finite order-21 question. The literature
search recorded in `evidence/triage.md` was bounded, so this dossier makes no
unqualified priority claim and does not claim a characterization at arbitrary
order.
