# Precise problem reading

## Frozen claim and ambient conventions

The immutable statement is `source.md`.  The following is its precise mathematical
reading; it is not a replacement or correction of the frozen text.

- A **graph** is a finite, undirected, simple graph, realized as a finite
  one-dimensional CW/simplicial complex with vertex set `V(G)` and one closed
  interval for every edge.
- A **cograph** is such a graph with no induced subgraph isomorphic to the
  four-vertex path `P_4`.  Disconnected cographs are included.
- `K` is a set of distinct vertices, possibly empty.  For
  `n in Z_{>=0}`, the coordinates in `G^n` are labeled (ordered), and collisions
  are allowed, both at vertices and in edge interiors.
- With the product cubical structure on `G^n`,

  ```text
  Sigma(G,K,n)
    = {(x_1,...,x_n) in |G|^n :
         for every k in K there is a j in {1,...,n} with x_j=k}.
  ```

  Equivalently, it is the union of product cells for which, for each `k in K`,
  at least one factor is the zero-cell `{k}`.  Thus it is a finite cubical
  subcomplex.  If `n<|K|` it is empty; the frozen question restricts to
  `n>=|K|`.
- Homology is integral singular homology, equivalently cellular homology of this
  finite cubical complex.  `Tor A` denotes the torsion subgroup of a finitely
  generated abelian group `A`.  Its being nonzero is equivalent to the existence
  of a prime `p` and a nonzero element of exact order `p`.

The unrestricted anchored-torsion assertion `(AT)` is the existential statement

```text
there exist a finite graph G, K subseteq V(G), n in Z_{>=0} with n>=|K|,
i in Z_{>=0}, and a prime p such that H_i(Sigma(G,K,n);Z)[p] != 0.
```

The problem frozen for this project is the cograph-restricted assertion

```text
(C-AT)  there exist G,K,n,i,p as above, with G additionally a cograph,
        such that H_i(Sigma(G,K,n);Z)[p] != 0.
```

A single witness to `(C-AT)` proves `(AT)`.  A proof that every cograph case is
torsion-free disproves only `(C-AT)`, not `(AT)`.  A finite census can do neither
unless it produces a valid torsion witness.

## Source status and nearest result

The inspected primary source is A. Mamun, J. Nalikka, and E. Ramos,
*Universality in the Algebra and Topology of Cographs*, arXiv:2609.04554v1
(2026), <https://arxiv.org/abs/2609.04554>.  The PDF inspected on 2026-09-09 has
SHA-256 `f73a5cf3fa71f1c5f387de7cf1d881214831d557a2b46ba43e2e2518bac37480`.
Definition 4.13 (PDF p. 26) gives the space above.  Corollary 4.18 (pp. 27--28)
gives finite generation for fixed `(i,r,n)`, where `r=|K|`, and the subsequent
discussion explicitly says that integral torsion is not known for anchored
configuration spaces, while citing torsion-freeness for trees and cycles.

For fixed `(i,r,n)`, the nearest usable cograph result is therefore a uniform
bound on the exponent of the **torsion subgroup**, not torsion-freeness.  The
literal phrase “the exponent of the group” in Corollary 4.18(2) cannot apply to
a homology group with a nonzero free summand (already `H_0` supplies examples),
so only this torsion-exponent reading is used here.  It has no bearing on whether
torsion exists.

A bounded arXiv search on 2026-09-09 for the exact anchored-torsion and cograph
language also located Kozlov's primary papers on generalized anchored spaces and
on the circle, but no separate resolution of `(C-AT)`.  This is not a priority or
novelty proof.  Conservatively, `(AT)` is **open-supported by the cited 2026
source**, while the separately frozen restriction `(C-AT)` is **status-uncertain
/ a natural new subquestion** rather than a question independently certified as
open by an exhaustive literature review.

## First nontrivial layer

The initial research layer fixes a singleton anchor `K={k}` and `n=3`.

- For `n=1`, `Sigma(G,{k},1)={(k)}`.
- For `n=2`,
  `Sigma(G,{k},2)=(G x {k}) union ({k} x G)`.  This is a graph (with the two
  indicated copies meeting at `(k,k)`), so all its integral homology is free.
- For `n=3`, every product cell has at least one coordinate equal to the
  zero-cell `{k}`, hence has dimension at most two.  Consequently `H_0` is free,
  `H_2=ker(partial_2)` is a subgroup of the free group `C_2` and is free, and
  `H_i=0` for `i>2`.  Thus only `H_1` can contain torsion in this layer.

To remove sign and cell-selection ambiguity, choose an orientation for every
edge and order the three product factors.  The degree-`q` cellular basis is

```text
B_q = {sigma_1 x sigma_2 x sigma_3 :
       sigma_j is a vertex or oriented open edge of G,
       sum_j dim(sigma_j)=q, and sigma_j={k} for some j}.
```

For an oriented edge `[u,v]`, set `partial[u,v]=v-u`, and use the product rule

```text
partial(sigma_1 x sigma_2 x sigma_3)
 = sum_j (-1)^(sum_{h<j} dim sigma_h)
     sigma_1 x ... x partial(sigma_j) x ... x sigma_3.
```

The computation must verify `partial_1 partial_2=0`.  To compute torsion in
`H_1`, one must obtain an integral basis of `ker(partial_1)`, express the columns
of `partial_2` in that basis, and take the Smith normal form of the resulting
relation matrix; the Smith form of `partial_2` in all of `C_1` alone is not a
homology computation.

## First graph and exhaustive finite scope

Let the diamond `D=K_4-e` have

```text
V(D)={a,b,c,d},   E(D)={ac,ad,bc,bd,cd}.
```

It is a connected cograph.  Its automorphism orbits on vertices are exactly
`{a,b}` (degree two) and `{c,d}` (degree three).  The two pointed inputs to test
are therefore `(D,a)` and `(D,c)`; they are not pointed-isomorphic.

If neither diamond input has torsion, the prescribed census consists of every
finite simple cograph `G` with `1<=|V(G)|<=6`, including disconnected graphs,
and, for each `G`, one anchor `k` from every orbit of `Aut(G)` on `V(G)`.  Two
pointed inputs are identified only when a graph isomorphism sends one anchor to
the other.  Each input is tested only at `K={k}, n=3`, with exact integer
matrices and Smith data retained.  Completeness must be justified by canonical
cograph/cotree generation plus pointed-isomorphism deduplication.

## Triage target and limits

Nearest prior result `X`: fixed-parameter finite generation and a bounded
torsion exponent on pointed cographs, plus known torsion-free tree and cycle
families.  Proposed delta `Y`: first seek an explicit torsion witness in the two
diamond anchor orbits; failing that, produce a complete exact census through six
vertices as reproducible intermediate data and use it only to discover a
meaningful infinite subclass that would still require proof.  Verification route
`Z`: build both boundary matrices with the displayed conventions, check the
chain identity, and compute `H_1` over `Z` by kernel-basis Smith reduction.

No finite torsion-free census is a theorem about all cographs, and no infinite
torsion-free subclass may be inferred from samples.  No chain complex, Smith
normal form, torsion witness, or subclass proof has yet been produced in this
triage job.
