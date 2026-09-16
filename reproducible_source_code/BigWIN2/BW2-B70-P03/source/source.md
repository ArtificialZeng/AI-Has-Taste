# win-00070-p03 — Integral torsion in anchored configuration spaces of cographs

## Immutable primary-source record

- Primary source: Adityo Mamun, Jonathan Nalikka, and Eric Ramos, *Universality in the algebra and topology of cographs*, arXiv:2609.04554v1 [math.CO], 3 September 2026.
- Official abstract: <https://arxiv.org/abs/2609.04554v1>.
- Official HTML: <https://arxiv.org/html/2609.04554v1>.
- Definition 4.13: official PDF p.26 / HTML 576–578; Corollary 4.18: PDF p.27 / HTML 599–622; source-stated open status: PDF p.28 / HTML 627–630.
- Access record: official arXiv HTML was read directly on 2026-09-08. The official PDF is archived as batch material.

## Frozen assertion

A cograph is a finite simple graph with no induced copy of \(P_4\). For a cograph \(G\), a subset \(K\subseteq V(G)\), and an integer \(n\ge|K|\), use Definition 4.13 of the source verbatim for the anchored configuration space
\[
\Sigma(G,K,n)\subseteq G^n,
\]
in which every vertex of \(K\) must occur as at least one coordinate and collisions are allowed as specified there.

Resolve the existence question
\[
\exists(G,K,n,i)\quad
\operatorname{Tor}H_i(\Sigma(G,K,n);\mathbb Z)\ne0.
\]
Equivalently, prove that all such integral homology groups are torsion-free or give one fully certified counterexample tuple \((G,K,n,i)\).

## Nearest result and precise delta

The source records torsion-freeness for anchored configuration spaces of trees and cycles. Corollary 4.18 proves that, for fixed \((|K|,i,n)\), the homology over cographs forms a finitely generated module and that all torsion exponents divide a uniform integer \(d_{i,|K|,n}\). The authors nevertheless state that it is not known whether anchored configuration spaces admit integral torsion at all.

The delta is to settle one side of that explicit existence question within the structurally natural cograph class. A single torsion example is a complete resolution of the existential side; a finite census without torsion is not a global resolution unless paired with a proved reduction.

## Cheapest decisive attack

Generate unlabeled cographs without repetition from canonical cotrees, initially excluding graphs already covered as trees or cycles. For each graph, compute automorphism orbits of anchor subsets \(K\). Increase \((|V(G)|,|K|,n,i)\) by a fixed documented order.

Construct the integer cubical chain complex of \(\Sigma(G,K,n)\) directly from Definition 4.13, with explicit orientations and boundary signs. Compute Smith normal forms of adjacent boundary matrices. Any invariant factor \(d>1\), together with the graph encoding, anchor set, parameters, boundary matrices, and an explicit cycle whose class has order \(d\), is a positive certificate. Independently verify via rank jumps over primes dividing \(d\) and exact integral boundary multiplication.

If no torsion appears in the cheap range, record the exact complete census and park unless the cotree recursion yields a genuine torsion-free induction.

## Failure risks

- Do not substitute ordinary collision-free graph configuration spaces for the anchored space of Definition 4.13.
- Coordinate collisions and the requirement that every anchor appear must be encoded exactly.
- Smith factors from a single boundary matrix do not alone compute homology; quotient by image and kernel must be handled correctly.
- Isomorphic graphs or anchor sets may be deduplicated only with a certified canonical labeling/orbit calculation.
- A finite negative census is evidence, not a proof of universal torsion-freeness.

## Semantic boundary

No current or historical entry was found for arXiv:2609.04554, anchored configuration spaces, or cograph homology torsion. Other graph-homology projects use different complexes and do not duplicate this source-defined object.
