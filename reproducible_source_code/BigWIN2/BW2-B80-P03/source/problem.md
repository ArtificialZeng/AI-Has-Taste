# Precise problem reading

## Frozen input and scope

The immutable statement is `source.md` (SHA-256
`7c87a821cd1c51ba54c321a23c1f3e417886b3c3c322bc3871a176e44826f3f1`).
Interpret all graphs as finite, simple, undirected graphs. A **plane
triangulation** is a plane graph of order at least three in which every face,
including the outer face, is bounded by a 3-cycle.

The assertion is universally quantified over every ordered input `(G,v)`,
where `G` is a plane triangulation and `v` is a vertex of degree exactly three.
Write the three distinct neighbors of `v` as `a,b,c` in their cyclic order
around `v`. The triangulation forces `ab,bc,ca` to be edges (and the three
triangles incident with `v` are `vab`, `vbc`, and `vca`).

Introduce four new vertices `A={x,y,z,w}` and define `H=R_v(G)` exactly by

\[
 V(H)=(V(G)\setminus\{v\})\mathbin\dot\cup A,
\]
\[
 E(H)=E(G-v)\cup {A\choose 2}\cup
 \{xa,xb,yb,yc,zc,za\}.
\]

There are no further edges incident with `A`. The intended plane embedding
puts `x,y,z` inside the old triangle `abc` and `w` inside `xyz`; toughness
itself depends only on the resulting abstract graph. Relabeling the cyclic
triple merely relabels the construction.

For a graph `J` and `S subseteq V(J)`, `J-S` is the induced graph on
`V(J)\S`, and `c(J-S)` is its number of connected components. For a
noncomplete graph,

\[
 \tau(J)=\min_{S\subseteq V(J),\;c(J-S)\ge2}
             \frac{|S|}{c(J-S)},
\]

while `tau(K_n)=infinity`. The required claim, with the extended-real minimum
in the complete case, is

\[
 \boxed{\tau(R_v(G))=\min\{\tau(G),3/2\}}.
\]

The proof must include `G=K_4`; a disproof must instead give an embedded
adjacency list and exact optimizing subset certificates for both toughness
values. No asymptotic, numerical, or restricted-family interpretation is
intended.

## Boundary normalization

- If `G=K_4`, then `tau(G)=infinity`, `H` has seven vertices and is
  noncomplete, and the asserted value is `tau(H)=3/2`.
- If `G` is not `K_4`, then `|V(G)|>=5`. Deleting `N_G(v)={a,b,c}` leaves
  `v` isolated and at least one further vertex, so this exact separator gives
  `tau(G)<=3/2`. Thus in this branch the assertion reduces to
  `tau(H)=tau(G)`.

## Nearest verified prior result and proposed delta

Songling Shan, *Non-Hamiltonian 3/2-Tough Plane Triangulations*,
[arXiv:2609.05414v1](https://arxiv.org/abs/2609.05414), defines this operation
immediately before Theorem 1.4. Theorem 1.4(i)--(ii) states that `H` is a plane
triangulation and that `tau(G)>=3/2` implies `tau(H)>=3/2`; its separator proof
is on printed pp. 5--6. The paper was inspected on 2026-09-09. It does not
state the boxed exact law.

The proposed delta is exact behavior when `tau(G)<3/2`, plus the matching
upper bound at the threshold. A bounded verification route is to (i) rerun
the theorem's separator cases with `t=min{tau(G),3/2}` and (ii) prove that an
optimal separator of noncomplete `G` can avoid `v`, so its component count is
unchanged when `v` is replaced by the connected gadget `A`. The `K_4` upper
bound should be checked separately with `N_H(w)={x,y,z}`.
