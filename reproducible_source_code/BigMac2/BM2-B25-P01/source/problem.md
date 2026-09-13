# Precise problem statement

## Frozen input and scope

The immutable statement is `source.md` (SHA-256
`ea3d097839f8cdfdfcd8a59c1df8afb91c7c37250f6bef314a0a0f9eda58ff4f`).
This project asks only about the single case \(q=4\), \(r=3\); it does not ask
for a construction or obstruction for every \(r\equiv3\pmod 4\).

## Objects and conventions

- The vertex set is \(\mathbb Z_{12}=\{0,1,\ldots,11\}\), with all vertex
  arithmetic taken modulo \(12\).
- The arc set of \(C_4(3)\) is
  \[
  A=\{x\longrightarrow x+s:x\in\mathbb Z_{12},\ s\in\{1,2,3\}\}.
  \]
  The displayed integer \(s\in\{1,2,3\}\) is the step of the arc.
- For \(j\in\mathbb Z_4\), layer \(j\) is
  \(L_j=\{x\in\mathbb Z_{12}:x\equiv j\pmod4\}\).
- A directed Hamilton cycle \(H\) is a cyclic sequence
  \((v_0,v_1,\ldots,v_{11},v_0)\) in which
  \(v_0,\ldots,v_{11}\) are the twelve distinct vertices and every successive
  difference is one of the allowed steps \(1,2,3\) modulo \(12\).
- Such an \(H\) is **four-layer balanced** precisely when, for every
  \((j,s)\in\mathbb Z_4\times\{1,2,3\}\), exactly one arc of \(H\) has step
  \(s\) and tail in \(L_j\). Thus \(H\) contains one representative of each of
  the twelve translation-orbits \(O_{j,s}\).
- For \(k\in\mathbb Z_3\), put \(H_k=H+4k\), translating both endpoints of
  every arc modulo \(12\). By Proposition 2.2 and Lemma 2.3 of the cited paper,
  balance implies that \(H_0,H_1,H_2\) are pairwise arc-disjoint Hamilton
  cycles and partition all arcs of \(C_4(3)\). These are the **three** developed
  cycles; “four-layer” refers to the four residue layers, not to the number of
  developed cycles.

## Quantified target

Define the three fixed arcs
\[
e_i=(2i\longrightarrow2i+2),\qquad i=0,1,2.
\]
They form the simple directed path \(0\to2\to4\to6\). The question is whether
there exist a four-layer balanced directed Hamilton cycle \(H\) and a
permutation \(\pi\in S_3\) such that
\[
e_i\in A(H_{\pi(i)})\qquad\text{for every }i\in\{0,1,2\}.
\]
Equivalently, each developed cycle contains exactly one of the three fixed
path arcs. Equivalently again, the three fixed arcs have pairwise distinct
development colours. There are no additional or freely chosen path arcs in
this interpretation.

## What constitutes a resolution

An affirmative certificate must give an explicit cyclic ordering for \(H\)
and identify the permutation \(\pi\) (or the developed cycle containing each
\(e_i\)). Direct checks must verify allowed steps, Hamiltonicity, all twelve
balance conditions, and the three distinct cycle memberships. Deleting
\(e_i\) from its corresponding cycle must then give the three asserted
Hamilton paths; the deleted arcs themselves are exactly \(0\to2\to4\to6\).

A negative resolution must give a mathematical obstruction or a complete,
independently replayable exact enumeration. Failure of the paper's ABAB
construction, ordinary Hamiltonicity, existence of an unqualified Hamilton
decomposition, or the equality of a path number does not decide this target.

## Prior-result boundary and exact verification route

The inspected primary source is arXiv:2609.01256v1, local PDF SHA-256
`1ec8a1fc02a7736128e659f5ea152523a2aae73a2ff1ea621555e3b451e8b63c`
(inspected 2026-09-09). Definition 2.1, Proposition 2.2, and Lemma 2.3 give the
balance and development notions; Definition 5.1 gives chain compatibility.
Theorem 4.7 treats \(r\equiv1\pmod4\), \(r\ge9\). Section 9 says that its ABAB
mechanism fails when \(r\equiv3\pmod4\), but explicitly does not claim an
existence obstruction. It therefore does not settle \(r=3\). Proposition 2.4
only supplies the necessary oddness condition and winding number \(2\), both
consistent with this case. No broader literature-status claim is made here.

A bounded exact search is available. For each of the twelve pairs
\((j,s)\), choose one of the three possible tails in \(L_j\), hence one arc in
\(O_{j,s}\). The resulting \(3^{12}=531{,}441\) choices exhaust all balanced
arc sets. Retain exactly those having indegree and outdegree one at every
vertex and forming one directed 12-cycle, then test whether \(e_0,e_1,e_2\)
belong to distinct translates. Recording the program, environment, totals,
and witnesses or a reproducible zero-result certificate would make this test
independently replayable.
