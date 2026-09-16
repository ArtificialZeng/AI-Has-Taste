# win-00066-p03 — All minimum bondage sets of Yavari's counterexample

Let `G` be the graph with vertex set `{0,1,...,17}` and unordered edge set

```text
(0,6) (0,10) (0,16) (1,8) (1,11) (1,12)
(2,4) (2,5) (2,13) (3,4) (3,5) (3,9)
(4,16) (5,11) (6,7) (6,13) (7,8) (7,14)
(8,13) (9,10) (9,14) (10,15) (11,15)
(12,15) (12,17) (14,17) (16,17)
```

Determine exactly every five-edge subset `F` for which `gamma(G-F)>gamma(G)=6`. Classify this complete family under `Aut(G)`, reporting canonical representatives, orbit sizes, stabilizers, and the exact value of `gamma(G-F)` for every orbit.

Primary evidence: `batches/inbox/bigWin-66-materials/2609.04257.pdf`, SHA-256 `6a655bacced3f3c3a38f01b0dbf84638994491da8bcec8a6c4e415a5637828e4`, especially Theorem 1.2, Eq. (3.1), and Propositions 4.1–4.2. The paper proves `b(G)=5`, gives one five-edge witness, and enumerates all four-edge deletions; it does not classify all minimum five-edge bondage sets.

A screening computation suggested 801 qualifying sets in 140 automorphism orbits. Treat both numbers as adversarial hypotheses, not facts. Rebuild the graph and automorphism group independently, scan all `C(27,5)=80730` subsets with exact domination tests, and provide a second implementation or certificate replay. This is distinct from `win-00063-p03`, which established the minimum graph order but left eighteen-vertex classifications unresolved.

