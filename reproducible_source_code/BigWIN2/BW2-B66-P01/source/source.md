# win-00066-p01 — Diagonal MP Ramsey status of `K_{1,3} disjoint-union K_2`

Let `H=K_{1,3} disjoint-union K_2`, with six distinct vertices across the two components. Using exactly the maximal-planar Ramsey conventions of arXiv:2609.05268v1, determine whether there is an integer `N` such that every red-blue edge-colouring of every simple maximal planar graph on at least `N` vertices contains a monochromatic copy of `H`.

If such `N` exists, determine the least `r_MP(H,H)` and give a proof covering all larger orders. If not, give a mechanically checkable infinite family of arbitrarily large maximal planar graphs with a two-colouring in which both colour classes are `H`-free. A lone finite avoiding colouring is only a lower bound, not a disproof of unavoidability.

Primary evidence: `batches/inbox/bigWin-66-materials/2609.05268.pdf`, SHA-256 `d2c05952bb165545210571a572678338e7766162141549adbf62411e3cf881b2`, especially Definition 1, Proposition 4, Corollary 2, Theorem 11/Remark 5, and §5 Problem 2.

Required first attack: prove and exploit the exact dichotomy that an `H`-free graph either has maximum degree at most two, or every edge meets the four vertices of any chosen claw. Reduce the two colour classes to the four resulting cases before broad graph generation. Check the source's explicit infinite constructions first. Do not claim the paper itself calls this exact singleton open; it is a source-grounded refinement of Problem 2.

