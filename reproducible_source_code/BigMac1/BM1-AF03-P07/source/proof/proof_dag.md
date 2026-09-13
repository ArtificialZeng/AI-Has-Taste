# Proof dependency DAG

## Certified finite endpoint \(n\leq 8\)

`F0` Formal definitions and quantifiers
→ `F1` staircase bound \(\operatorname{sh}(T)\subseteq(n,n-1,\ldots,1)\)
→ `F2` shape-first enumeration is finite and exhaustive
→ `F3` explicit-grid Hecke insertion computes every right transition exactly
→ `F4` all primitive K-Knuth pairs are instantiated at every state
→ `F5` queue closure computes the least right-stable equivalence containing `F4`
→ `F6` Algorithm 1 / Theorem 3.1 identifies `F5` with tableau K-Knuth equivalence
→ `F7` initial components are selected by exact alphabet bitset
→ `F8` for each component shape set \(S\), compute
\(\uparrow S\cap\downarrow S\setminus S\)
→ `F9` the set is empty for every initial component for each \(0\leq n\leq8\)
→ `F10` Conjecture 7.6 holds for every alphabet of cardinality at most eight.

Independent integrity branch:

`I1` strict certificate parser + exact schema
→ `I2` no discovery state/transition/component files are read
→ `I3` expected integer totals match the reconstructed values
→ `I4` six malformed/tampered input tests reject
→ `I5` code/input hashes printed on success.

## General conjecture

`P1` Standardization + fixed outer hook
→ `P2` variations lie in the interior Young diagram
→ `P3` proposed prescribed-cover filling lemma
→ `P4` induction along any saturated chain
→ `P5` general Conjecture 7.6.

The edge `P2 → P3` is open. The finite certificate proves `P3` only for
alphabet size at most eight and does not justify `P5` in general.
