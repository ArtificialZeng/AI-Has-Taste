# win-00077-p01 — disconnected diagonal maximal-planar Ramsey problem

## Immutable primary-source record

- Adriana Baldacchino, Yair Caro, and Xandru Mifsud, *Ramsey properties of
  maximal (outer)planar graphs*, arXiv:2609.05268v1 [math.CO], 4 September 2026.
- Official HTML: <https://arxiv.org/html/2609.05268v1>
- Local full text: `bigWin-77-materials/2609.05268.pdf`, SHA-256
  `d2c05952bb165545210571a572678338e7766162141549adbf62411e3cf881b2`.
- Locators: Definition 1 (PDF p.2); Section 1.2 notation (p.4);
  Proposition 4 (p.14); Theorem 12 (pp.17--20); Problem 2 (p.21).

## Frozen assertion

Let `S_{2,1,1}` be the tree obtained by identifying one endpoint of three paths
of lengths 2, 1, and 1. Put
`H := S_{2,1,1} disjoint-union K_2`, where the union is vertex-disjoint. Let
`K_MP` be the class of all finite simple maximal planar graphs.

Prove or disprove

```
there exists N in N such that for every n >= N, every n-vertex G in K_MP,
and every c:E(G)->{red,blue}, G contains a non-induced red copy of H or a
non-induced blue copy of H.
```

If true, a proved explicit upper bound is sufficient; determining the least
`r_MP(H,H)` is optional. If false, the certificate must cover arbitrarily large
orders, not just one avoidable graph.

## Nearest result and exact delta

Definition 1 is the eventual-unavoidability quantifier above. Theorem 12 proves
`r_MP(S_{2,1,1},S_{2,1,1})=9`. Problem 2 asks for a complete classification for
disconnected planar `H`. The present graph is the one-disjoint-edge augmentation
of that solved fork. It is not covered by the linear-forest extension in Theorem
11 and Remark 5 because its maximum degree is three.

The source does not state this individual case separately. It is a sourced
specialization of Problem 2, and its status in later literature must be checked.

## Cheapest decisive attack

Generate nonisomorphic maximal planar graphs at small orders with a reproducible
generator and encode a two-colouring having no monochromatic `H` as SAT. Retain
generator version/options and graph hashes. A satisfying instance needs graph6,
the complete edge colouring, and an independent copy-avoidance verifier. An
unsatisfiable instance needs the CNF, encoding proof, and DRAT/LRAT or equivalent
checker transcript.

A finite satisfying instance proves only a lower bound. To disprove the frozen
eventual statement, extract a repeatable triangulated patch or another construction
giving an unbounded family and prove preservation of avoidance. For a positive
route, use Theorem 12 to force a monochromatic fork, then establish that sufficiently
large maximal planar graphs force a disjoint edge of the same colour.

## Failure boundaries

- Copies are ordinary subgraphs, not induced subgraphs.
- One finite counterexample does not refute an eventual quantifier.
- Finite UNSAT checks do not prove all larger orders.
- Registry absence is not a novelty proof.
