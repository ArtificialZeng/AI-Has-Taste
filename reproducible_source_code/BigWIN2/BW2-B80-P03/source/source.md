# win-00080-p03 — Exact toughness law under tetrahedral replacement

## Immutable target

Let G be a finite plane triangulation and let v be a vertex of degree three with neighbors a,b,c. Let H=R_v(G) be the tetrahedral replacement from arXiv:2609.05414v1: delete v; add x,y,z,w inducing K_4; join x to a,b, join y to b,c, join z to c,a; and add no other edges incident with x,y,z,w.

With toughness defined for a noncomplete graph J by

tau(J) = min {|S| / c(J-S) : S is a vertex set and c(J-S)>=2},

and with tau(K_n)=infinity, prove or disprove

tau(R_v(G)) = min{tau(G), 3/2}.

The proof must cover every finite plane triangulation with a degree-three vertex and handle G=K_4 separately. A counterexample must provide an exact embedded adjacency list and exact subset certificates for both toughness values.

## Provenance and nearest theorem

Songling Shan, *Non-Hamiltonian 3/2-Tough Plane Triangulations*,
arXiv:2609.05414v1, defines R_v(G) immediately before Theorem 1.4 on PDF
p. 2. Theorem 1.4(ii), also on p. 2, proves only that if G is 3/2-tough,
then R_v(G) is 3/2-tough. The separator proof is on pp. 5--6. The proposed
target asks for the exact numerical law for the same operation.

Primary PDF: batches/inbox/bigWin-80-materials/2609.05414.pdf
SHA-256: 00e7b0fb4e3f3eb45294e978cfdf73e93ce9df94fe23716f1f7c85671ba4a3de

Open/novel status is limited to absence of the exact law from the inspected v1 and absence from the local semantic registry; it is not a global priority claim.
