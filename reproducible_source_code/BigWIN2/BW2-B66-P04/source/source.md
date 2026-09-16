# win-00066-p04 — The 12-vertex two-attachment `C4/C8` gadget layer

For every connected simple graph `H` on exactly twelve vertices with two distinguished vertices `s!=t`, assume

- `deg_H(s)=deg_H(t)=2`;
- every other vertex has degree 3; and
- `dist_H(s,t)>=3`.

Prove or disprove:

> `H` contains a simple cycle of length four or a simple cycle of length eight.

If counterexamples exist, classify all rooted isomorphism classes `(H,s,t)` and give graph6 plus explicit terminal labels. If none exist, give a complete independently replayable finite certificate.

Primary evidence: `batches/inbox/bigWin-66-materials/2609.04686.pdf`, SHA-256 `0ab4267dc8b9de8abb3c3868385a2afad9fb8f08614836297581a4ee03ab77f8`, especially Definition 3.1 and Proposition 6.2(2). The source handles orders 4, 6, 8 and a distance-at-least-three nonexistence statement at order 10, not order 12. Its official archive is `batches/inbox/bigWin-66-materials/2609.04686-supplement.zip`, SHA-256 `5dd250b705e4ed8e9fe6be625285adffea0d98d9f18b3640071ed4a6e4290fe4`.

Because `dist_H(s,t)>=3`, adding the edge `st` gives a connected simple cubic graph on twelve vertices; conversely deleting an edge from such a cubic graph and retaining only connected cases covers the domain. Use this bijection to certify complete input coverage. Meringer's official census is stored at `batches/inbox/bigWin-66-materials/12_3_3.asc`, SHA-256 `f32e0b0a0dcaeee8b67fcd1896a261330abecd22bab3a4144463f9011732cac7`; its primary record is <https://mathe2.uni-bayreuth.de/markus/REGGRAPHS/12_3_3.html>.

A screening scan reported 85 input graphs, 1530 graph-edge pairs, 1526 connected deletions, 1110 cases with terminal distance at least three, and no `C4/C8`-free case. Treat every count as an adversarial hypothesis. The final certificate should give the lexicographically least `C4` or `C8` for every eligible pair and should preferably be cross-checked by an independent SAT/UNSAT encoding.
