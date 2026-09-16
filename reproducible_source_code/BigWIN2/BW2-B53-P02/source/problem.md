# Precise problem reading

## Frozen target

For each integer `n >= 1`, write

`Div*(n) = {d in Z_{>0} : d | n and d < n}`.

For every subset `D` of `Div*(n)` (including the empty set), define the simple
labeled graph `ICG_n(D)` on `Z_n = Z/nZ` by

`{x,y} in E(ICG_n(D))` if and only if `x != y` and
`gcd(a,n) in D`,

where `a` is any integer representative of `x-y`.  The gcd is independent of
the representative.  The task is to determine

`N = min {n >= 1 : there exists D subset Div*(n) such that ICG_n(D) is
uniquely 3-colorable and omega(ICG_n(D)) = 2}`

and then determine every `D subset Div*(N)` having those properties.

Here `omega(G)` is the maximum cardinality of a clique.  A graph is *uniquely
3-colorable* precisely when:

1. `chi(G)=3`; and
2. any two proper maps `c,c':V(G) -> {1,2,3}` induce the same unordered
   partition into their three nonempty fibers (equivalently, `c' = pi o c`
   for some permutation `pi` of the colors).

Thus `omega=2` means that the graph has an edge and is triangle-free.  The edge
condition is automatic once `chi=3`, but it should still be checked by the
enumerator.  Connectivity is also checked explicitly, as required by the
source's certificate contract, rather than treated as an implicit consequence
of unique colorability.

Minimality quantifies over **every** `1 <= n < N` and **every** legal divisor
set `D subset Div*(n)`.  Classification at `N` is equality of labeled graphs on
`Z_N`, not graph isomorphism.  In fact the parametrization has no duplicates:
if `D != D'` and `d` lies in their symmetric difference, then `{0,d}` is an
edge of exactly one of `ICG_n(D), ICG_n(D')`, because `gcd(d,n)=d`.  Hence
equality of these labeled graphs is equivalent to `D=D'`.

## Scope caveat

The opening lead asks for the smallest integral-circulant counterexample to the
unrestricted assertion `chi=omega`, whereas the frozen target asks only for the
smallest counterexample with `(chi,omega)=(3,2)`.  These are not logically
equivalent unless one separately rules out a smaller uniquely `k`-colorable
integral circulant with `k>omega` and `k>=4`.  This job treats the explicitly
frozen target above as controlling; any later manuscript must not advertise
its minimum as the unrestricted global minimum without that additional proof.

## Prior result and proposed delta

- Milan Basic, *On uniquely colorable Cayley graphs*, arXiv:2609.03184v1,
  <https://arxiv.org/abs/2609.03184>, retrieved and inspected 2026-09-07.
  The supplied PDF has SHA-256
  `eec197e27fcab9602c1cd8b033dd84a45d4401abcbdbe225db3de9d6afb9acf2`.
  Section 3, especially Lemmas 3.2--3.3 and Theorem 3.1 on pages 4--6,
  proves that `ICG_{12p}({2,p})` is uniquely 3-colorable and has clique
  number 2 for every prime `p>=5`.  Taking `p=5` supplies the upper bound
  `N<=60` and the explicit partition by residues modulo 3.  The inspected
  paper does not claim least order or classify divisor sets of smaller order.
- Walter Klotz and Torsten Sander, *Uniquely colorable Cayley graphs*, Ars
  Mathematica Contemporanea 12 (2017), 155--165,
  <https://doi.org/10.26493/1855-3974.879.d47>, retrieved 2026-09-07.
  Problem 3.6 asks whether every uniquely colorable circulant graph satisfies
  `chi=omega`; it does not pose the present least-order classification.

Accordingly, the unrestricted assertion is already known to be false, while
the frozen least-order/classification problem is a finite new question whose
literature status remains uncertain after this bounded search.  The proposed
delta is: nearest prior result = the order-60 family above; new target = the
exact least `N` in the frozen class and all qualifying `D` at `N`; verification
route = exhaustive exact enumeration with replayable certificates.

## Bounded verification route

There are only

`sum_{n=1}^{59} 2^(tau(n)-1) = 2043`

legal pairs `(n,D)` below 60, since `|Div*(n)|=tau(n)-1`; including order 60
gives 4091 pairs.  The largest individual search below 60 is 512 sets at
`n=48`.  An exact verifier should construct every graph and record, for each
qualifying or exclusion-critical case: connectivity; a 3-coloring; a proof of
non-bipartiteness (or exact chromatic test); triangle/clique checks; and the
number of 3-color partitions modulo color permutation.  For the witness it
must output the unique partition.  A second implementation should replay the
enumeration or its exact SAT/CSP certificates before any resolution claim.

