# Precise problem reading

## Frozen task

The immutable statement is `source.md`. Its question is interpreted literally,
with no change from 21 vertices to “at most 21” and with the closed, rather than
open, left half-plane as the stability region.

## Objects and definitions

- A graph here is finite, undirected, and simple. A **tree** is a connected
  acyclic graph. “Unlabeled trees on exactly 21 vertices” means the finite set
  of isomorphism classes of such trees; a computation may use labeled
  representatives, but each class must occur exactly once.
- A vertex set is **independent** when no two of its vertices are adjacent. For
  a tree `T`, `i_k(T)` is the number of its independent subsets of cardinality
  exactly `k`, including `i_0(T)=1`. Thus
  `I(T,z)=sum_{k=0}^{alpha(T)} i_k(T) z^k` is an integer polynomial, where
  `alpha(T)` is the maximum independent-set size.
- In this problem **stable** means Hurwitz quasi-stable:
  `I(T,zeta)=0` implies `Re(zeta)<=0`. Consequently **unstable** means that at
  least one zero has strictly positive real part. This use of “stable” must not
  be silently replaced by the sometimes-used strict condition `Re(zeta)<0`.

## Quantified decision and required output

Decide the proposition

> For every isomorphism class `[T]` of simple trees with `|V(T)|=21`, every
> complex number `zeta` satisfying `I(T,zeta)=0` also satisfies
> `Re(zeta)<=0`.

There are two exhaustive branches.

1. If the proposition is false, enumerate **all** unstable 21-vertex tree
   isomorphism classes. For every listed class give a canonical exact graph
   representation, its exact coefficient vector, and an exact Routh--Hurwitz
   or real-algebraic certificate proving the existence of a zero in
   `Re(z)>0`. A floating-point root is only a screening aid, not a certificate.
2. If the proposition is true, give a complete once-per-isomorphism-class
   census and exact stability certificates for every resulting polynomial.
   The census and exact arithmetic must be reproducible and auditable.

An exact Routh computation with no singular row may certify the number of
right-half-plane roots by its first-column sign variations. Any zero pivot,
zero row, or vanishing Hurwitz determinant must instead be handled explicitly
(for example by exact imaginary-axis factor detection together with a
non-strict Hermite--Biehler/Sturm analysis); failure of a strict-Hurwitz test
alone does not prove instability under the source's closed-half-plane
definition.

## Scope and nearest prior results

The attached official arXiv v1 PDF by Lei Zhang and Jianhua Tu has SHA-256
`fb1940a98c1cc1ec1e5ba479871431244090771b2b6ce3fa7c72dc888c6c4d82`.
Its Theorem 2 quotes Brown--Cameron: graphs of independence number at most 3
and stars are stable, while some trees have roots arbitrarily far into the
right half-plane. Immediately before Definition 3 it reports that
Brown--Cameron computations found every tree of order at most 20 stable. Its
Theorem 4 proves the stronger strict statement for every spider. Neither
result decides the finite 21-vertex census.

OEIS A000055 records 2,144,505 unlabeled trees on 21 vertices. This is an
external expected total, not by itself a completeness proof for a generated
census.

The source question is therefore treated as a **new finite question** adjacent
to the reported order-20 computation and the open general characterization,
not as a literature-certified open conjecture. The target contribution is:
nearest prior boundary 20 plus all-spider stability; proposed delta, a complete
exact order-21 decision and classification; verification route, streaming
unlabeled-tree generation, canonical duplicate checks, tree dynamic programming
for `I(T,z)`, and exact Routh/Hermite--Biehler arithmetic with independently
recomputed certificates.
