# Proof dependency graph

Endpoint **T00**: generic LV-equivalence of tree classes implies tree
isomorphism for every \(n\ge2\).

| ID | Statement | Depends on | Evidence |
|---|---|---|---|
| L01 | Generic tree-matrix entry formula \(A_{ij}=d_{r,j}\). | Source definition of a tree-system | `proof/main_proof.md`, §1 |
| L02 | C2 forces the exact support of any noncoordinate generic linear DP to induce a connected subtree. | L01; source linear-DP criterion C2 | `proof/main_proof.md`, §2 |
| L03 | No generic linear DP has support at least three. | L01; source criterion C3; algebraic independence; characteristic zero | `proof/main_proof.md`, §2 |
| L04 | The full projective linear-DP set is exactly the \(n\) coordinates and \(n-1\) edge DPs. | L02, L03; two-support case of C3 | `proof/main_proof.md`, Lemma 2 |
| L05 | The projective DP configuration is a reduced incidence representation of the cone over \(T\). | L04; acyclicity of \(T\) | `proof/main_proof.md`, §3 |
| L06 | Its three-element circuits are exactly \(\{x_u,P_{uv},x_v\}\). | L05; forest independence/graph-cycle dependence | `proof/main_proof.md`, §3 |
| L07 | The unlabeled three-circuit hypergraph reconstructs \(T\). | L06; every \(n\ge3\) tree edge has a nonleaf endpoint | `proof/main_proof.md`, Lemma 3 |
| L08 | Linear LV-conjugacy induces an isomorphism of three-circuit hypergraphs. | L04; invertibility preserves DPs and dependence | `proof/main_proof.md`, §5 |
| T00 | \(T_1\cong T_2\). | L07, L08 | `proof/main_proof.md`, §5 |
| F09 | The requested order-nine endpoint covers exactly 47 unlabeled trees and has no invariant collision. | Prüfer completeness; AHU canonicalization; two exact invariant computations | `certificates/trees_n2_n9.json`; independent verifier |
