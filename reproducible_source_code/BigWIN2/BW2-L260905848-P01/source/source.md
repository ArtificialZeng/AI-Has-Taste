# Source freeze: first genuinely non-pairwise binary boundary of the Frankl--Tokushige conjecture

Primary source: Yao Li, Benjian Lv, and Jie Wen, *On the Frankl--Tokushige conjecture and almost complete r-cross t-intersection theorems for vector spaces*, arXiv:2609.05848v1 (5 September 2026), Conjecture 1 and Theorem 1.1.

Corroborating primary source: Toshihiro Shimizu and Norihide Tokushige, *A product theorem for r-cross intersecting families of subspaces*, arXiv:2608.28013v1 (28 August 2026), Conjecture 2, Theorem 3, and the paragraph immediately after Theorem 3.

Let V = F_2^5. For i=1,2,3, let F_i be a family of 3-dimensional linear subspaces of V. Call (F_1,F_2,F_3) 3-cross 1-intersecting if

    dim(U_1 intersect U_2 intersect U_3) >= 1

for every choice U_i in F_i.

Problem. Prove or disprove

    |F_1| |F_2| |F_3| <= 35^3 = 42875.

If equality holds, determine whether necessarily there is a common 1-dimensional subspace L of V such that every F_i is the full star {U <= V : dim U = 3 and L <= U}.

Scope and contribution boundary. This is the q=2, r=3, t=1, k_1=k_2=k_3=3, n=5 instance of the Frankl--Tokushige conjecture. The 2026 theorem of Li--Lv--Wen does not cover it: its displayed sufficient hypothesis gives n >= 3(k+1)/2 + 1 = 7. The older two-family product theorem settles equal dimensions when n >= 2k and therefore covers n=6, but not n=5. Thus n=5 is the first equal-dimension binary boundary where the three-family condition is not reduced to the known pairwise theorem. This note records only noncoverage and a precise finite instance; it does not assert that the instance is separately stated as open or that no other paper settles it.

Cheapest decisive tests. Enumerate the 155 three-dimensional subspaces of F_2^5 exactly; encode forbidden triples with zero common intersection as a three-partite 3-uniform hypergraph. First search for any feasible size triple with product greater than 42875. If none exists, obtain a proof-producing SAT/ILP certificate for the finitely many Pareto-minimal cardinality triples. Independently replay every accepted family triple or unsatisfiability certificate. Only after the inequality is certified should equality orbits under GL(5,2) be classified.

Frozen on 2026-09-10 UTC. Original-status label: unresolved fixed finite instance; claimed novelty/open status requires fresh literature audit.
