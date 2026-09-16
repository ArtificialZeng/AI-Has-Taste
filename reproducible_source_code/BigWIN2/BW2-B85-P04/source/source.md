# Frozen source problem: exact three-uniform Kneser Ramsey number R_3^KG(3,3)

Canonical id: win-00085-p04
Frozen on: 2026-09-10 (Asia/Shanghai)
Primary sources:
- Heath--McCourt--Parker--Schwieder--Zerbib, *Ramsey Numbers in Kneser
  Graphs*, arXiv:2510.25734v2, Definition 1 on PDF p.1, Theorems 11--12
  on PDF p.3, and the SAT formulation in Section 3.3 on PDF pp.8--9.
- Gujgiczer--Marits--Ozeki, arXiv:2607.12353v1, the unresolved status of
  `KG(11,3)` and `KG(12,3)` on PDF p.10.

## Definitions

For n>=6, the Kneser graph KG(n,3) has the three-element subsets of `[n]` as
vertices, with two vertices adjacent exactly when the subsets are disjoint.
Let R_3^KG(3,3) be the least n for which every red-blue coloring of the edges
of KG(n,3) contains a monochromatic triangle.

Equivalently, determine when the edges of KG(n,3) can be covered by two
triangle-free spanning subgraphs. This equivalence concerns an ordinary
two-coloring/cover and must not be conflated with the stronger 2.5-colorability
notion in the second source.

## Statement

Determine which value in

```
R_3^KG(3,3) in {11,12,13}
```

is exact.

## Scope and contribution boundary

The first source proves `11 <= R_3^KG(3,3) <= 13`; the second still records
the KG(11,3) and KG(12,3) cases as unresolved. The fixed SAT instances have:

- KG(11,3): 165 vertices, 4,620 edges, and 15,400 triangles;
- KG(12,3): 220 vertices, 9,240 edges, and 61,600 triangles.

A positive instance must supply the complete edge coloring and an independent
checker that verifies every edge and triangle. An UNSAT instance must preserve
the exact graph/CNF generator, hashes, solver configuration and log, and a
standard proof object such as LRAT or FRAT that is replayed by an independent
checker. A solver's bare `UNSAT` line is computational evidence, not a proof.
The natural decision order is n=11 and then, only if necessary, n=12.

This file is immutable. Changing the uniformity, number of colors, forbidden
clique size, or using the stronger 2.5-colorability condition is a different
problem.
