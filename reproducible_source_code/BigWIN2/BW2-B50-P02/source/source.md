# Immutable source — win-00050-p02

## Original lead

Complete the acyclic-orientation flip-graph Hamiltonicity atlas through six vertices.

## Precise frozen statement for triage

For every connected unlabeled finite simple graph `G` with `2<=|V(G)|<=6`, let `AO(G)` have as vertices all acyclic orientations of `G`, two adjacent when they differ by reversal of exactly one edge. Determine exactly whether `AO(G)` has a Hamiltonian cycle. Record the acyclic signature `sigma(G)` and decide whether `sigma(G)=0` is sufficient for Hamiltonicity throughout this complete finite domain. If not, classify all minimum-order counterexamples up to graph isomorphism.

The certificate must identify the complete graph6 domain, list every orientation/flip graph, and give a Hamilton cycle for every positive case. Every negative case not already excluded by `sigma(G)!=0` needs an independently replayable exact DP, SAT/DRAT, or comparably complete non-Hamiltonicity certificate. Timeouts and failed searches are unknown, not negative results.

## Primary source and delta

- Leonie Mühlherr and Germain Poullot, *Hamiltonicity of graphs of acyclic orientations and acyclic polynomials*, arXiv:2609.02249v1, Formulations 1–3, Lemma 2.9 and Appendix D/Table 5: https://arxiv.org/abs/2609.02249v1
- Local primary PDF: `batches/inbox/bigWin-50-materials/2609.02249.pdf`
- SHA-256: `fc43647a3fd3beb1173645f93504570e546cb99edb531b62bee6319b0e6abaaf`
- Retrieved: 2026-09-07; 58 pages.

The source reports 22 selected named graphs, not the complete connected graph atlas through six vertices. `win-00048-p03` concerns a congruence for counts of acyclic orientations on grid graphs and is not semantically equivalent.

