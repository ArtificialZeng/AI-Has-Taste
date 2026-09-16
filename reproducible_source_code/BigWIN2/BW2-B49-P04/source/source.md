# Immutable source statement: win-00049-p04

## Title

All one-card identifying edge orbits in the maximal-planar family (J_m)

## Original lead (preserved)

> The source exhibits one identifying edge of (J_m); classify every such edge in the whole family.

This is a proposed structural refinement of the source's infinite one-card family, not a quotation of an author-declared open subproblem.

## Definitions

For (m\ge6), let (B_m) be the bipyramid over the rim cycle (r_0r_1\cdots r_{m-1}r_0): two nonadjacent hubs (p,q) are adjacent to every rim vertex. Insert a vertex (w) into the triangular face (pr_0r_1) and join it to (p,r_0,r_1). The resulting finite simple maximal planar graph is (J_m).

For a maximal planar graph (G) and (e\in E(G)), the edge card is the unlabeled graph (G-e). Call (e) an identifying edge when the one-card multiset ({!{G-e}!}) identifies (G) within the class (mathcal M) of finite simple maximal planar graphs: for every (H\in\mathcal M), if (G-e) occurs as an edge card of (H), then (H\cong G).

## Exact proposed statement

For every integer (m\ge6):

1. determine all identifying edges of (J_m);
2. partition them into orbits under the full graph automorphism group (operatorname{Aut}(J_m));
3. give a closed formula in (m) for their total number and the multiplicity of each corresponding unlabeled card type; and
4. for every non-identifying edge orbit, exhibit a nonisomorphic maximal-planar parent of its card.

The source proves that (wp) is identifying but does not claim it is the only identifying orbit. A proof covering only generic (m) without checking exceptional isomorphisms, or a search over only flippable edges without justifying completeness of parents, is insufficient.

## Primary source and nearest results

- Sergey Ivanov, *The Class Edge-Reconstruction Number of a Maximal Planar Graph Is One or Two*, arXiv:2609.02389v1.
- Official pages: <https://arxiv.org/abs/2609.02389> and <https://arxiv.org/pdf/2609.02389>.
- Theorem 2.2 on p.2 proves every maximal planar graph needs one or two selected edge cards; Proposition 2.4 gives the exact parent test for one-card reconstruction; Lemma 3.1 gives the two-parent result for a flippable edge; Proposition 5.2 and Figure 4 on p.5 define (J_m) and show that deleting (wp) identifies it; §6 asks for an intrinsic characterization of one-card graphs.
- Proposition 5.2 proves existence of at least one identifying card for each (J_m). It does not classify all identifying edges, card types, or multiplicities.

## Precise delta and value

The delta is an exact internal witness classification inside the source's natural infinite family. It advances the stated structural direction without attempting all maximal planar graphs. The result should explain which local edge configurations yield isomorphic alternate completions and which retain a nonisomorphic rival.

## Required certificate and proof

1. Determine (operatorname{Aut}(J_m)) and its edge orbits uniformly for (m\ge6), treating any exceptional small (m) separately.
2. For each edge-orbit representative, determine every maximal-planar parent of the unlabeled card. When using the diagonal-flip lemma, verify its flippability and three-connectivity hypotheses; handle nonflippable cases independently.
3. Prove parent isomorphism to (J_m) or exhibit an invariant and explicit alternate parent showing nonisomorphism.
4. Compute card-type multiplicities and account for distinct edge orbits that can yield isomorphic cards.
5. Independently enumerate and canonically verify (m=6,7,8,9) as boundary evidence, then give the uniform graph-theoretic proof.

## Cheapest decisive test and falsification

Use the rigid spherical embedding of maximal planar graphs. Deleting an edge exposes its local completion possibilities; compare the original diagonal with every admissible alternative using degree sequences, unique high-degree hubs, the unique degree-three inserted vertex, and rim distances. Any nonisomorphic maximal-planar parent falsifies an identifying claim. Conversely, any omitted card whose complete parent list is isomorphic to (J_m) falsifies completeness.

## Frozen primary material

- `batches/inbox/bigWin-49-materials/2609.02389.pdf`
- SHA-256 `e00321e285529cf345e6700e844504dbaf6614e3286a9679c20727920b11cacc`
- Retrieved from the official arXiv PDF endpoint and checked as a 15-page PDF on 2026-09-07.
