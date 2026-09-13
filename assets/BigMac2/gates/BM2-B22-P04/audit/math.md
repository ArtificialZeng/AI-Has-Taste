# Fresh mathematical referee report

## Frozen scope and verdict

I reviewed the `result-note` claim frozen by snapshot digest
`2023a3cd86fb4345f524bacaa1ef9971821af45d2177e3e94da7ab0ef3501440`.
The claim concerns every nonempty finite graph, including disconnected graphs,
every singleton anchor, and every `n>=1`; it does not claim to resolve the
frozen cograph torsion-existence problem.  My verdict on this exact scope is
**accept**.

## Reconstruction of the decisive argument

Write

```text
F_n(X,x0) = {(x1,...,xn) in X^n : xi=x0 for at least one i}.
```

A based map induces a coordinatewise map on these spaces.  More importantly,
a based homotopy does too: if the `i`-th input coordinate is `x0`, then its
image remains the target basepoint throughout a based homotopy.  Thus `F_n`
sends a based homotopy equivalence to a homotopy equivalence.

For the graph `G`, choose a spanning tree in each component, rooting the tree
in the component of `k` at `k`, and collapse the trees.  The quotient can be
obtained by standard tree-edge contractions; in the distinguished component
the contractions and their homotopies may be chosen relative to `k`.  Hence
this is a based homotopy equivalence

```text
(G,k) -> (W,*),
```

where `W` is a disjoint union of `c` bouquets, with `c` zero-cells and
`beta=|E|-|V|+c` loop one-cells in total.  It follows that

```text
Sigma(G,{k},n) = F_n(G,k) ~= F_n(W,*).
```

In the product CW structure on `W^n`, the latter fat wedge is precisely the
subcomplex whose product cells have at least one zero-dimensional factor equal
to `*`.  Each loop cell of `W` has cellular boundary zero.  The product
boundary formula therefore makes every cellular differential of this
subcomplex zero.  Its integral homology is consequently its free cellular
chain group.

A degree-`q` cell is obtained by choosing its `q` loop coordinates, one of the
`beta` loops in each, and zero-cells in the remaining coordinates with at least
one choice equal to `*`.  This gives

```text
binom(n,q) beta^q (c^(n-q) - (c-1)^(n-q)).
```

For `q=n`, the last factor is `1-1=0`, consistently using `x^0=1`; there is no
all-loop cell in the fat wedge.  There are no cells above degree `n` (indeed,
none in degree `n`).  This proves the frozen rank formula and torsion-freeness.

## Quantifier and edge-case attacks

- Disconnected graphs cause no failure: the forest collapse is componentwise,
  while only the distinguished component carries the based condition.  The
  count uses all `c` bouquet vertices and all `beta` loops, regardless of their
  components.
- If `beta=0`, the formula reduces to the exact number
  `c^n-(c-1)^n` of zero-cells containing `*` and gives no positive-degree
  homology.  For `c=1`, it gives ranks `binom(n,q) beta^q` for `q<n` and zero
  for `q=n`.  For `n=1`, it gives only `H_0=Z`, as required because the space is
  the point `k`.
- The proof does not infer a homotopy equivalence merely from ordinary graph
  homotopy type: the homotopies must fix `k`, and the rooted forest contraction
  supplies that requirement.
- For an anchor set of size `r`, every cell has at least `r` distinct
  zero-cell coordinates, so its dimension is at most `n-r`.  If `n<=r+1`, the
  space is at most one-dimensional and has torsion-free integral homology.
  The empty-anchor case is `G^n`, also torsion-free by the graph Kunneth
  calculation.  Combining these facts with the singleton theorem proves the
  stated necessary conditions `|K|>=2` and `n>=|K|+2` for any torsion witness.
  It does not settle the original existential assertion, whose status remains
  unresolved.

## Exact computation check

All seven frozen file hashes agree with `audit/snapshot.json`.  I reran the
listed standard-library certificate generator in a fresh temporary directory,
without modifying the frozen evidence.  Its combined summary had SHA-256
`7f5e87b033888463e1939b822f84dc054ab4d2d09b0079edbd0916ba3e1f4515`,
identical to the frozen summary.  For both diamond anchor representatives it
verified `d1*d2=0`, reconstructed `d2` in a 69-element integral cycle basis,
and obtained a rank-63 Smith diagonal whose nonzero entries are all `1`, with
unimodular left and right transformations.  Thus both computations give
`H_0=Z`, `H_1=Z^6`, and `H_2=Z^12`.  Independently, substituting
`c=1,beta=2,n=3` in the proved formula gives exactly ranks `(1,6,12)`.
The rerun is only a consistency check; the general theorem rests on the
topological argument above.

## Prior-result comparison and contribution

The nearest 2026 cograph result, Mamun--Nalikka--Ramos, Corollary 4.18, gives
fixed-parameter finite generation and a uniform restriction on possible
torsion; its subsequent discussion explicitly says integral torsion for
anchored configuration spaces is unknown outside the established tree and
cycle cases.  Kozlov's 2024 paper gives an Euler-characteristic formula for
arbitrary connected graphs and full homology only for circle graphs.  In the
connected singleton case, the alternating sum of the present Betti formula is

```text
(-1)^(n-1) (beta^n - (beta-1)^n),
```

which agrees with the `|K|=1` specialization of Kozlov's Euler formula
(`epsilon=beta-1`).  This is a useful compatibility check but does not supply
the present all-degree theorem.

On 2026-09-09 I also performed a bounded fresh search of arXiv and the cited
open-access primary article for the exact singleton-anchor/fat-wedge reduction;
no equivalent statement was located.  This is not a priority proof, and the
frozen contribution appropriately makes no priority claim.  At its stated
scope the contribution is nevertheless nontrivial and useful: it determines
all integral homology groups for an infinite family covering every finite
graph and every `n`, and it removes the entire singleton-anchor slice from the
torsion search.  It is neither an arbitrary toy restriction nor a finite-census
inference.

## Conclusion

The exact frozen theorem, rank formula, and search-space consequence are
correct.  The original cograph torsion problem remains unresolved, as required
for a `result-note`.  Verdict: **accept**.
