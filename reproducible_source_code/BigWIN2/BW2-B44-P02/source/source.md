# Frozen source — win-00044-p02

For every integer `delta>=8`, prove or disprove that there exists a constant `C_delta`, depending only on `delta`, such that every connected `n`-vertex `K_7`-free graph `G` of minimum degree at least `delta` satisfies

> `diam(G) <= 8n/(3delta) + C_delta`.

This is the `k=6` instance of Conjecture 1.3 in arXiv:2609.03346v1 (PDF p.2): its coefficient `3-2/k` becomes `8/3` and its threshold `ceil(3k/2)-1` becomes 8. The paper proves counterexamples, including to the colorable version, for every `k>=7`; the frozen target is the first unresolved even boundary.

The unrestricted target is `K_7`-free, not merely 6-colorable. A 6-colorable counterexample also disproves it; an affirmative result only for 6-colorable graphs is a partial result. The additive term may depend on `delta` but not on `n`. A disproof requires an infinite family for a fixed admissible `delta` whose excess over `8n/(3delta)` is unbounded; one finite graph cannot by itself refute the existence of `C_delta`.

Primary PDF: `bigWin-44-materials/2609.03346.pdf`, SHA-256 `43dad1ab45dc8199b1db0ff71d7adf11347ee38ce70c1358512e6fbd41f4aa82`.

