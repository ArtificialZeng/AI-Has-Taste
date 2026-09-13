# Exact certificate for a 13-vertex witness

## Claim

Let \(G=P(13)\) be the Paley graph on \(\mathbb Z/13\mathbb Z\): distinct
vertices \(i,j\) are adjacent exactly when

\[
  j-i\pmod {13}\in\{1,3,4,9,10,12\}.
\]

With vertices ordered \(0,1,\ldots,12\), its graph6 string is

```text
LlthgsL`mEkLkL
```

The exact certificate establishes \(\beta(G)=4\), hence in particular
\(\beta(G)\leq4\).

## Generator and orbit artifact

`lc13_search.cpp` represents each labeled graph by all 78 upper-triangular
adjacency bits, split losslessly into a 64-bit low word and a 14-bit high word.
It starts at the graph6 input, uses a FIFO queue, applies local complementation
at each of all 13 vertices of every dequeued state, and handles duplicates in
an `unordered_set<Key>` whose equality operator compares both full words (hash
collisions therefore do not identify states).  The queue empties after exactly
711,440 distinct labeled states.

`paley13_lc_orbit.bin` serializes those states in BFS discovery order.  Its
format is the 8-byte magic `LC13ORB2`, a little-endian 64-bit count, then
15-byte records `(uint64 low, uint16 high, uint32 parent, uint8 move)`.  The
root has sentinel parent/move values; every other record names an earlier
record and the local-complement vertex that produced it.  The artifact has
10,671,616 bytes and SHA-256

```text
6ee96dec3a2e4c2dcbd4424366e3499b611024c5911b8f20c7d54dca1eb73d02
```

## Independent exact verification

`verify_paley13.py` does not call the C++ generator.  Using a separate Python
implementation and exact integers, it:

1. decodes the graph6 string, cross-checks NetworkX's decoder, and confirms
   that the edge set is exactly the Paley graph above (13 vertices, 39 edges);
2. checks all 711,440 full adjacency keys are distinct and in range;
3. verifies each of the 711,439 parent/move records, proving every listed state
   is reachable from the root;
4. independently recomputes every one of the \(711440\cdot13=9,248,720\)
   local complements and checks that it occurs in the serialized set, proving
   closure; reachability plus closure proves that the set is exactly the full
   labeled LC orbit;
5. for every orbit state, tests each of the \(\binom{13}{5}=1287\) five-sets
   by exact adjacency-mask intersection.  All 915,623,280 state/subset checks
   find an edge, so every orbit member has independence number at most four;
6. finds an independent four-set \(\{0,1,2,3\}\) in orbit record 834, proving
   the matching lower bound \(\beta(G)\geq4\).

The machine-readable result is `paley13_verification.json`.

## Reproduction

From the project directory:

```sh
clang++ -std=c++20 -O3 -DNDEBUG evidence/lc13_search.cpp -o evidence/lc13_search
./evidence/lc13_search certify 'LlthgsL`mEkLkL' evidence/paley13_lc_orbit.bin
/Users/mac/4prove-or-disprove-math/.research-venv/bin/python \
  evidence/verify_paley13.py 'LlthgsL`mEkLkL' \
  evidence/paley13_lc_orbit.bin evidence/paley13_verification.json
```

The generator also independently rejects a candidate immediately if its own
exact search finds an independent five-set.  The decisive independence check,
however, is the separate exhaustive Python verification above.
