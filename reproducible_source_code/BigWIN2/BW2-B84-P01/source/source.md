# Frozen source problem: exact diameter of the K3,3 graph associahedron

Canonical id: win-00084-p01
Frozen on: 2026-09-09 (Asia/Shanghai)
Primary sources:
- Cardinal--Pournin--Valencia-Pabon, arXiv:2106.16130v2,
  definitions on PDF pp.2--3 and Question 2 on p.18.
- Gargantini--Pastine--Torres, arXiv:2406.06317v2,
  Theorem 4.7 on PDF p.28 and Corollary 4.8 on p.29.
Local copies:
- batches/inbox/bigWin-84-materials/2106.16130v2.pdf,
  SHA-256 6b14c1ceeba0887564309e06ba1d934599feed2c6a6f368726335b5b576caa2a.
- batches/inbox/bigWin-84-materials/2406.06317v2.pdf,
  SHA-256 823f3b2b508a4f3f2444c92bc203b264cc7613961716b7f94ea5d96cea99d0b4.

## Definitions

Let G=K_{3,3}, with parts P={p1,p2,p3} and Q={q1,q2,q3}. A tube is a
nonempty vertex subset inducing a connected subgraph. Two tubes are compatible
when one contains the other, or they are disjoint and their union is not a
tube. The vertices of R(G) are maximal compatible tubings (equivalently the
source search trees); two vertices are adjacent when one tube is exchanged by
one legal rotation.

For T,T' in R(G), let d(T,T') be graph distance and let
diam R(G)=max d(T,T') over all ordered pairs.

## Statement

Prove or disprove the exact assertion

> diam R(K_{3,3}) = 12.

## Scope and contribution boundary

The cited sources imply 10 <= diam R(K_{3,3}) <= 13. The lower and upper
bounds use the exact split-complete value, Theorem 4.7, and monotonicity; do not
attribute the full two-sided range to Corollary 4.8 alone. The balanced-family
diameter is source-open, but the fixed value 12 is only a triage conjecture.

A complete computer-assisted proof must independently regenerate every state
and legal edge, prove graph completeness, and supply checked BFS layers or an
equivalent distance certificate. The triage counts 55 tubes, 552 maximal
tubings, 1,380 edges, and diameter 12 are hints, not accepted evidence. A
distance-13 pair or any regeneration mismatch disproves the assertion.

This file is immutable. Any changed convention or restricted claim must be
frozen separately.
