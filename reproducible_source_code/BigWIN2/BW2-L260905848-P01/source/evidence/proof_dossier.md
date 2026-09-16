# Exact computer-assisted proof dossier

## Theorem submitted for review

Let \(V=\mathbb F_2^5\). If
\(\mathcal F_i\subseteq\operatorname{Gr}_2(5,3)\), for \(i=1,2,3\), and

\[
 \dim(U_1\cap U_2\cap U_3)\geq 1
 \quad\text{for every }U_i\in\mathcal F_i,
\]

then

\[
 |\mathcal F_1||\mathcal F_2||\mathcal F_3|\leq 35^3=42875.
\]

Equality holds if and only if there is a 1-space \(L\leq V\) such that all
three families are the full star
\(\{U\in\operatorname{Gr}_2(5,3):L\leq U\}\).

This is an exact finite, computer-assisted proof. The DRAT check establishes
unsatisfiability of the frozen CNFs; the inspectable generators and reduction
audit establish the correspondence between those CNFs and the theorem.

## Complete finite domain and forbidden triples

`build_rref_hypergraph.py` enumerates the row-reduced bases of all 3-subspaces
in lexicographic order. Exhausting independent triples of nonzero vectors gives
exactly 155 distinct bases. A basis is also expanded to the 32-bit mask of its
eight vectors.

For each of the \(155^3=3,723,875\) ordered triples, the script calls it
forbidden exactly when the bitwise intersection of the three masks has one
element, namely zero. Independently, it constructs the three orthogonal
2-subspaces and checks that their six generators have rank five. These tests
agree on every triple; 2,499,840 triples are forbidden. The resulting list is
`forbidden_triples_u8.bin`, SHA-256
`ce0d8e6ea2b771ddbd28dc79adb5cdfac1ac735d62b31a0bbb02ef695b05cbf6`.
Thus one three-literal negative clause per listed triple is exactly the cross
intersection condition.

## Lossless normalizations

If a product is positive, permute the three family labels so that their sizes
are \(a\geq b\geq c\). Pick a member of the largest family. Transitivity of
\(\mathrm{GL}(5,2)\) on 3-subspaces maps it to frozen vertex 0. Pick a member
of the second family. Relative to vertex 0, its intersection dimension is 1,
2, or 3. The stabilizer of vertex 0 is transitive on each of those three
classes, so the member can be mapped to the frozen representative 13, 1, or 0,
respectively. Applying the same invertible map to all three families preserves
all intersections and cardinalities.

`verify_reductions.py` audits these statements without a group-theory oracle.
It constructs an invertible transitivity witness for each of the 155 vertices,
then enumerates all \(168\cdot6\cdot 2^6=64,512\) elements of the stabilizer.
The three computed orbits have sizes 112, 42, and 1 and equal exactly the
intersection-dimension classes. Consequently the ordering, fixed vertex, and
three-representative clause lose no positive-product assignment. Empty-family
triples already satisfy the desired inequality strictly.

## Product upper bound

`cnf_product_threshold.py` connects every membership bit to descending unary
cardinality outputs using comparators with outputs exactly \(p\lor q\) and
\(p\land q\). It adds the lossless normalizations above and every forbidden
triple clause. It exhaustively checks the complete sorted cube
\(1\leq c\leq b\leq a\leq155\) and finds 829 componentwise-minimal triples
whose upward closure is exactly \(abc\geq42876\). Tseitin terms impose their
disjunction.

The resulting DIMACS instance has 72,904 variables and 2,718,299 clauses,
SHA-256
`5a04264cfb4b6deaa3ea5b280eab1ba83a483e4ecba86455b4c0475cc0257760`.
CaDiCaL emitted `product_above_bound.bdrat`, and a separate `drat-trim`
process checked that binary DRAT trace in full, reporting `s VERIFIED` and
603,299,890 resolution steps. Therefore no normalized, hence no original,
family triple has product at least 42,876.

## Attainment and equality classification

For every 1-space \(L\), its full star has
\({4\brack2}_2=35\) members. Three copies are feasible because every selected
subspace contains \(L\); hence the upper bound is attained.

For exact product 42,875, the complete sorted cardinality cube has only the
three factorizations

\[
 (a,b,c)=(35,35,35),\ (49,35,25),\ (125,49,7).
\]

`cnf_equality_classification.py` imposes exactly this disjunction using the
same unary outputs. For each of the 31 nonzero vectors (the 31 one-spaces over
\(\mathbb F_2\)), it adds one clause falsified by exactly the assignment in
which all three families are the corresponding complete 35-member star. The
reduction audit independently checks that these 31 stars are distinct, have
size 35, and are feasible.

The non-star equality DIMACS instance has 72,078 variables and 2,715,035
clauses, SHA-256
`ea74dd60145d1e46b6227c0e75f30e740f5ae86b3948f64b2bf2b4c50621f0f5`.
Its binary DRAT trace `nonstar_equality.bdrat` was separately checked by
`drat-trim`, which reported `s VERIFIED` after 183,039,602 resolution steps.
Thus no non-star equality assignment exists. Being a common full-star triple
is invariant under family permutation and simultaneous invertible linear
maps, so undoing the normalizations proves the stated classification.

## Reproduction and limits

The decisive deterministic checks are:

```text
python3 evidence/build_rref_hypergraph.py
python3 evidence/verify_reductions.py
drat-trim evidence/product_above_bound.cnf evidence/product_above_bound.bdrat -i
drat-trim evidence/nonstar_equality.cnf evidence/nonstar_equality.bdrat -i
```

The two recorded checker runs used a `drat-trim` executable with SHA-256
`9d9c6f706cc5ad81f569ac429faf0c3269c5806c7be0ac936af9c2d1daa7260f`.
No floating-point conclusion or unverified solver status is used. This dossier
makes no priority claim and does not assert any parameter case beyond the
frozen \((q,r,t,k,n)=(2,3,1,3,5)\) instance.
